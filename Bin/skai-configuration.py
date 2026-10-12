#!/usr/bin/env python3
# Managed-By: skai
# Managed-Id: tool.component-selection
# Managed-Source: Bin/skai-configuration.py
# Managed-Adapter: repo-source
# Managed-Updated-At: 2026-10-12
"""Selection resolver, component-history planner, and new-component recorder.

`--resolve` and `--plan-history` read only. `--enable` appends new components to the project
config and `--decline` records declined ones in the component history; these are the installer's
only writes through this helper, and it opens no server. Only use a proposed history after
migrations and actual inventory verification succeed.
"""
from __future__ import annotations

import argparse
import copy
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
ADAPTERS = {"codex", "cursor", "claude-code"}


class ConfigurationError(ValueError):
    pass


def read_manifest(root: Path = ROOT) -> dict:
    try:
        data = json.loads((root / "assets.manifest.json").read_text(encoding="utf-8"))
        assets = data["assets"]
        if not isinstance(assets, list) or len({a["id"] for a in assets}) != len(assets):
            raise ConfigurationError("The SKAI catalog has duplicate or invalid asset IDs.")
        return data
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ConfigurationError(f"Cannot read the SKAI catalog: {exc}") from exc


def components(manifest: dict) -> list[dict]:
    return [a for a in manifest["assets"] if a["type"] in {"skill", "policy"}]


def config_path(project: Path, name: str = "config.json") -> Path:
    return project_path(project, f"skai/{name}")


def project_path(project: Path, relative: str) -> Path:
    project = project.resolve()
    path = project / relative
    if not path.resolve().is_relative_to(project) or path.is_symlink():
        raise ConfigurationError(f"{relative} must be a regular file inside the active project.")
    return path


def read_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ConfigurationError(f"Cannot read {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigurationError(f"{path} must be a JSON object.")
    return data


def validate_schema(data: dict) -> None:
    if type(data.get("schemaVersion")) is not int or data["schemaVersion"] != 1:
        raise ConfigurationError("SKAI configuration must have schemaVersion: 1.")


def read_config(project: Path, manifest: dict) -> tuple[dict | None, set[str]]:
    data = read_json(config_path(project))
    optional = {a["id"] for a in components(manifest) if a.get("installRole") != "required"}
    if data is None:
        return None, optional
    validate_schema(data)
    selected = data.get("components")
    if not isinstance(selected, list) or any(not isinstance(v, str) for v in selected):
        raise ConfigurationError("components must be an explicit list of optional component IDs.")
    if len(selected) != len(set(selected)):
        raise ConfigurationError("components contains duplicate IDs.")
    unknown = set(selected) - optional - set(manifest.get("retiredComponents", []))
    if unknown:
        raise ConfigurationError("Unknown or non-selectable component IDs: " + ", ".join(sorted(unknown)))
    return data, set(selected) & optional


def read_local(project: Path, manifest: dict) -> tuple[dict | None, dict[str, bool]]:
    data = read_json(config_path(project, "config.local.json"))
    if data is None:
        return None, {}
    validate_schema(data)
    values = data.get("overrides")
    optional = {a["id"] for a in components(manifest) if a.get("installRole") != "required"}
    if not isinstance(values, dict) or any(type(v) is not bool for v in values.values()):
        raise ConfigurationError("overrides must map optional component IDs to true/false; omit inherited settings.")
    if set(values) - optional - set(manifest.get("retiredComponents", [])):
        raise ConfigurationError("Unknown or non-selectable local override IDs.")
    return data, {k: v for k, v in values.items() if k in optional}


def eligible(asset: dict, adapter: str, stack: str) -> bool:
    tags = asset.get("tags", [])
    if asset["type"] == "skill":
        return "adapter:" + adapter in tags
    return "core" in tags or (stack == "swift" and "swift" in tags)


def history_state(project: Path, scope: str) -> tuple[dict | None, Path]:
    """Discover installation state: local (when in scope), then shared, then legacy. Read-only."""
    candidates = ["skai/install-state.json", "docs/skai/install-state.json"]
    if scope == "local":
        candidates.insert(0, "skai/install-state.local.json")
    for relative in candidates:
        path = project_path(project, relative)
        state = read_json(path)
        if state is not None:
            return state, path
    return None, project_path(project, candidates[0])


def adapter_records(state: dict | None) -> list[dict]:
    adapters = (state or {}).get("installedAdapters", [])
    if not isinstance(adapters, list) or any(not isinstance(a, dict) for a in adapters):
        raise ConfigurationError("Invalid installedAdapters in installation state.")
    return adapters


def seen_components(state: dict | None, adapter: str | None = None) -> set[str]:
    """IDs an adapter's history (or any adapter's, when adapter is None) has installed, disabled or declined."""
    seen: set[str] = set()
    for record in adapter_records(state):
        if adapter is not None and record.get("adapter") != adapter:
            continue
        history = record.get("componentHistory", {})
        if not isinstance(history, dict):
            raise ConfigurationError("componentHistory must be an object of component records.")
        seen |= set(history)
    return seen


def resolve(project: Path, adapter: str, stack: str, manifest: dict) -> dict:
    if adapter not in ADAPTERS or stack not in {"generic", "swift", "android"}:
        raise ConfigurationError("Unknown adapter or stack.")
    if not project.is_dir():
        raise ConfigurationError("The active project directory does not exist.")
    data, selected = read_config(project, manifest)
    local, overrides = read_local(project, manifest)
    base = "all" if data is None else ",".join(sorted(selected))
    representation = "project=" + base + "\noverrides=" + ",".join(k + ":" + ("on" if v else "off") for k, v in sorted(overrides.items())) + "\n"
    effective = set(selected)
    for key, enabled in overrides.items():
        if enabled:
            effective.add(key)
        else:
            effective.discard(key)
    skills, policies = [], []
    for a in components(manifest):
        if a.get("installRole") != "required" and a["id"] not in effective:
            continue
        if eligible(a, adapter, stack):
            (skills if a["type"] == "skill" else policies).append(a)
    scope = "local" if local is not None or config_path(project, "install-state.local.json").exists() else "project"
    # New to this host: eligible, optional, not chosen in the project config, never seen by this adapter's history.
    # A default host chooses everything, so nothing is new in this sense.
    new = []
    if data is not None:
        seen = seen_components(history_state(project, scope)[0], adapter)
        new = [a for a in components(manifest) if a.get("installRole") != "required" and a["id"] not in selected
               and a["id"] not in seen and eligible(a, adapter, stack)]
    return {"configPath": str(config_path(project)), "localConfigPath": str(config_path(project, "config.local.json")),
            "defaultAll": data is None, "configurationFingerprint": hashlib.sha256(representation.encode()).hexdigest(),
            "trackComponents": data is not None or bool(overrides), "historyScope": scope,
            "historyStatePath": str(config_path(project, "install-state.local.json" if scope == "local" else "install-state.json")),
            "skills": skills, "policies": policies, "newComponents": new}


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def enable_components(project: Path, ids: list[str], manifest: dict) -> dict:
    """Append new components to the project config; never create one (a default host already selects everything)."""
    data, selected = read_config(project, manifest)
    if data is None:
        raise ConfigurationError("No project config: defaults already select every eligible component.")
    optional = {a["id"] for a in components(manifest) if a.get("installRole") != "required"}
    unknown = set(ids) - optional
    if unknown:
        raise ConfigurationError("Unknown or non-selectable component IDs: " + ", ".join(sorted(unknown)))
    data["components"] = sorted(selected | set(ids))
    write_json(config_path(project), data)
    return {"configPath": str(config_path(project)), "enabled": sorted(set(ids))}


def checkout_sha() -> str | None:
    try:
        return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def decline_components(project: Path, ids: list[str], manifest: dict, scope: str, sha: str | None, date: str) -> dict:
    """Record declined new components in every installed adapter's history so they stop counting as new."""
    optional = {a["id"] for a in components(manifest) if a.get("installRole") != "required"}
    unknown = set(ids) - optional
    if unknown:
        raise ConfigurationError("Unknown or non-selectable component IDs: " + ", ".join(sorted(unknown)))
    state, found = history_state(project, scope)
    if state is None:
        raise ConfigurationError("No installation state: run the initial install before declining components.")
    adapters = adapter_records(state)
    if not adapters:
        raise ConfigurationError("Installation state records no adapters.")
    for record in adapters:
        history = record.setdefault("componentHistory", {})
        for key in ids:
            if key in history:
                raise ConfigurationError(f"{key} is already in the component history and is not new.")
            history[key] = {"installed": False, "lastAppliedSHA": None, "lastAppliedAt": None, "declinedSHA": sha, "declinedAt": date}
    destination = config_path(project, "install-state.local.json" if scope == "local" else "install-state.json")
    if found != destination and destination.exists():
        raise ConfigurationError(f"Both {found} and {destination} exist; resolve the state location first.")
    write_json(destination, state)
    return {"statePath": str(destination), "declined": sorted(set(ids)), "declinedSHA": sha, "declinedAt": date}


def plan_history(previous: dict, actual: set[str], desired: set[str], *, fingerprint: str,
                 target_sha: str, date: str, track: bool, baseline_sha: str | None = None,
                 baseline_date: str | None = None) -> dict:
    """Return migration work and proposed adapter state; never write or discard disabled history."""
    for name, value in [("lastSHA", previous.get("lastSHA")), ("lastRunAt", previous.get("lastRunAt")),
                        ("baseline SHA", baseline_sha), ("baseline date", baseline_date)]:
        if value is not None and not isinstance(value, str):
            raise ConfigurationError(f"Invalid {name} in installation history; preserve unknown evidence as null.")
    state = copy.deepcopy(previous)
    if not track and "componentHistory" not in state and not (actual - desired):
        state["lastSHA"] = target_sha
        state["lastRunAt"] = date
        return {"migrations": [], "baselineAdapterState": copy.deepcopy(previous), "nextAdapterState": state, "tracking": False}
    history = state.get("componentHistory", {})
    if not isinstance(history, dict) or any(not isinstance(v, dict) for v in history.values()):
        raise ConfigurationError("componentHistory must be an object of component records.")
    for record in history.values():
        if type(record.get("installed")) is not bool or any(
            record.get(field) is not None and not isinstance(record[field], str)
            for field in ("lastAppliedSHA", "lastAppliedAt", "lastDisabledSHA", "lastDisabledAt")
        ):
            raise ConfigurationError("Invalid component history status/version/date; do not invent missing evidence.")
    # Customization OR any removal starts a full ledger BEFORE changing the inventory.
    # Default/eligibility changes can disable components without a config file.
    for key in actual:
        if key not in history:
            history[key] = {"installed": True, "lastAppliedSHA": previous.get("lastSHA") or baseline_sha,
                            "lastAppliedAt": previous.get("lastRunAt") or baseline_date}
    state["componentHistory"] = history
    baseline = copy.deepcopy(state)
    migrations = []
    for key in sorted(desired | set(history)):
        record = history.setdefault(key, {"installed": False, "lastAppliedSHA": None, "lastAppliedAt": None})
        if key in desired:
            old_sha = record.get("lastAppliedSHA")
            if old_sha != target_sha:
                migrations.append({"id": key, "fromSHA": old_sha, "toSHA": target_sha,
                                   "reason": "version-gap" if old_sha else "no-known-installed-version"})
            record.update(installed=True, lastAppliedSHA=target_sha, lastAppliedAt=date)
        else:
            if record.get("installed"):
                record.update(lastDisabledSHA=target_sha, lastDisabledAt=date)
            record["installed"] = False
    state["componentHistory"] = history
    state["lastSHA"] = target_sha
    state["lastRunAt"] = date
    state["configurationFingerprint"] = fingerprint
    return {"migrations": migrations, "baselineAdapterState": baseline, "nextAdapterState": state, "tracking": True}


def history_proposal(project: Path, adapter: str, resolved: dict, inventory: Path,
                     target_sha: str, date: str, manifest: dict) -> dict:
    state = None
    candidates = ["skai/install-state.json", "docs/skai/install-state.json"]
    if resolved["historyScope"] == "local":
        candidates.insert(0, "skai/install-state.local.json")
    for relative in candidates:
        state = read_json(project_path(project, relative))
        if state is not None:
            break
    state = state or {}
    adapters = state.get("installedAdapters", [])
    if not isinstance(adapters, list) or any(not isinstance(a, dict) for a in adapters):
        raise ConfigurationError("Invalid installedAdapters in installation state.")
    if adapter == "claude-code" and any(a.get("adapter") in (
        "jetbrains-claudecode", "xcode-claudecode", "androidstudio-claudecode"
    ) for a in adapters):
        raise ConfigurationError("Legacy Claude adapter identities require the direct component-history "
                                 "procedure and Claude identity migration; preserve prior evidence.")
    matching = [a for a in adapters if a.get("adapter") == adapter]
    if len(matching) > 1:
        raise ConfigurationError("Duplicate adapter history.")
    previous = matching[0] if matching else {"adapter": adapter}
    previous.setdefault("runbook", {
        "codex": "Install/Codex/install-update-codex.md",
        "cursor": "Install/Cursor/install-update-cursor.md",
        "claude-code": "Install/ClaudeCode/install-update-claudecode.md",
    }[adapter])
    inventory_data = read_json(inventory)
    ids = inventory_data.get("components") if inventory_data is not None else None
    if not isinstance(ids, list) or any(not isinstance(v, str) for v in ids) or len(ids) != len(set(ids)):
        raise ConfigurationError("Inventory must contain unique verified managed component IDs.")
    optional = {a["id"] for a in components(manifest) if a.get("installRole") != "required"}
    retired = set(manifest.get("retiredComponents", []))
    required = {a["id"] for a in components(manifest) if a.get("installRole") == "required"}
    if set(ids) - optional - retired - required:
        raise ConfigurationError("Inventory contains unknown component IDs.")
    desired = {a["id"] for a in resolved["skills"] + resolved["policies"]} & optional
    # A legacy global SHA cannot prove an individual adapter's version after mixed-adapter updates.
    # A sole record is usable only when it belongs to the adapter being planned.
    attributable = len(adapters) == 1 and len(matching) == 1
    baseline_sha = state.get("lastSHA") if attributable else None
    baseline_date = state.get("lastUpdatedAt") if attributable else None
    result = plan_history(previous, set(ids) & (optional | retired), desired,
                          fingerprint=resolved["configurationFingerprint"], target_sha=target_sha, date=date,
                          track=resolved["trackComponents"], baseline_sha=baseline_sha,
                          baseline_date=baseline_date)
    result.update(statePath=resolved["historyStatePath"], historyScope=resolved["historyScope"])
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(required=False)
    mode.add_argument("--resolve", action="store_true")
    mode.add_argument("--plan-history", action="store_true")
    parser.add_argument("--enable", help="comma-separated new component IDs to append to the project config")
    parser.add_argument("--decline", help="comma-separated new component IDs to record as declined")
    parser.add_argument("--adapter", choices=sorted(ADAPTERS), default="codex")
    parser.add_argument("--stack", choices=["generic", "swift", "android"], default="generic")
    parser.add_argument("--inventory", type=Path)
    parser.add_argument("--target-sha")
    parser.add_argument("--date")
    args = parser.parse_args(argv)
    if not (args.resolve or args.plan_history or args.enable or args.decline):
        parser.error("one of --resolve, --plan-history, --enable or --decline is required")
    try:
        manifest = read_manifest()
        result = resolve(args.project_root, args.adapter, args.stack, manifest)
        if args.enable or args.decline:
            if args.resolve or args.plan_history:
                raise ConfigurationError("--enable/--decline cannot be combined with --resolve or --plan-history.")
            ids = lambda value: [v for v in (value or "").split(",") if v]
            result = {"status": "saved"}
            if args.enable:
                result.update(enable_components(args.project_root, ids(args.enable), manifest))
            if args.decline:
                result.update(decline_components(args.project_root, ids(args.decline), manifest, result.get("historyScope") or resolve(args.project_root, args.adapter, args.stack, manifest)["historyScope"],
                                                 args.target_sha or checkout_sha(), args.date or datetime.date.today().isoformat()))
        elif args.plan_history:
            if not args.inventory or not args.target_sha or not args.date:
                raise ConfigurationError("--plan-history requires --inventory, --target-sha and --date.")
            result = history_proposal(args.project_root, args.adapter, result, args.inventory, args.target_sha, args.date, manifest)
        print(json.dumps(result, ensure_ascii=False), flush=True)
        return 0
    except ConfigurationError as exc:
        print(json.dumps({"status": "error", "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
