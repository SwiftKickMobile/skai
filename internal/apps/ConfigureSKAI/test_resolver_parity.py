"""Check the shipped headless Mac resolver against the portable resolver (no UI)."""
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
APP = ROOT / "Bin/SKAIConfigure.app/Contents/MacOS/SKAIConfigure"
spec = importlib.util.spec_from_file_location("selection", ROOT / "Bin/skai-configuration.py")
selection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selection)


def normalized(result):
    result = dict(result)
    for key in ("configPath", "localConfigPath", "historyStatePath"):
        result[key] = str(Path(result[key]).resolve())
    for key in ("skills", "policies", "newComponents"):
        result[key] = sorted(
            ({field: asset[field] for field in ("id", "type", "sourcePath", "tags")} for asset in result[key]),
            key=lambda asset: asset["id"])
    return result


class ResolverParityTests(unittest.TestCase):
    def test_schema_types_match_between_native_and_portable(self):
        for local in [False, True]:
            with self.subTest(local=local), tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                (project / "skai").mkdir()
                filename = "config.local.json" if local else "config.json"
                payload = '{"schemaVersion":1.0,"overrides":{}}' if local else '{"schemaVersion":1.0,"components":[]}'
                (project / "skai" / filename).write_text(payload)
                native = subprocess.run([str(APP), "--project-root", str(project), "--skai-root", str(ROOT), "--resolve"], capture_output=True, text=True)
                with self.assertRaises(selection.ConfigurationError):
                    selection.resolve(project, "codex", "generic", selection.read_manifest())
                self.assertEqual(native.returncode, 2, native.stdout)

    def test_all_adapters_stacks_and_configuration_scopes(self):
        scenarios = [
            (None, None, False),
            ([], None, False),
            (["skill.skai-debugging", "policy.error-handling", "policy.swift-code-organization"], None, False),
            (None, {"skill.skai-debugging": False, "skill.skai-ui-map-architecture": True}, False),
            (["skill.skai-debugging"], {"skill.skai-debugging": False, "skill.skai-ui-map-architecture": True}, False),
            (None, {}, True),
            (["skill.skai-debugging"], None, "history"),
        ]
        checked = 0
        manifest = selection.read_manifest()
        for index, (components, overrides, local_history) in enumerate(scenarios):
            with tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                config_dir = project / "skai"
                config_dir.mkdir()
                if components is not None:
                    (config_dir / "config.json").write_text(json.dumps({"schemaVersion": 1, "components": components}))
                if overrides is not None:
                    (config_dir / "config.local.json").write_text(json.dumps({"schemaVersion": 1, "overrides": overrides}))
                if local_history == "history":
                    # Seen components (installed, disabled or declined) are not new; unseen eligible ones are.
                    (config_dir / "install-state.json").write_text(json.dumps({"installedAdapters": [
                        {"adapter": "codex", "componentHistory": {"skill.skai-dev-retro": {"installed": False, "lastAppliedSHA": "N"},
                                                                  "policy.error-handling": {"installed": False, "lastAppliedSHA": None, "declinedSHA": "N", "declinedAt": "2026-10-12"}}},
                        {"adapter": "claude-code", "componentHistory": {"skill.skai-suggestion": {"installed": True, "lastAppliedSHA": "N"}}}]}))
                elif local_history:
                    (config_dir / "install-state.local.json").write_text(json.dumps({"installedAdapters": []}))
                before = {p.name: p.read_bytes() for p in config_dir.iterdir()}
                for adapter, stack in itertools.product(("codex", "cursor", "claude-code"), ("generic", "swift", "android")):
                    with self.subTest(scenario=index, adapter=adapter, stack=stack):
                        native = json.loads(subprocess.check_output([
                            str(APP), "--project-root", str(project), "--skai-root", str(ROOT),
                            "--resolve", "--adapter", adapter, "--stack", stack], text=True))
                        portable = selection.resolve(project, adapter, stack, manifest)
                        self.assertEqual(normalized(native), normalized(portable))
                        self.assertEqual({p.name: p.read_bytes() for p in config_dir.iterdir()}, before)
                        new_ids = {c["id"] for c in portable["newComponents"]}
                        if components is None:
                            self.assertEqual(new_ids, set())
                        else:
                            self.assertEqual("skill.skai-debugging" in new_ids, "skill.skai-debugging" not in components)
                            self.assertNotIn("skill.skai-configure", new_ids)
                            if local_history == "history":
                                # History is per adapter: declined under codex, still new to the others.
                                self.assertEqual("policy.error-handling" in new_ids, adapter != "codex")
                                self.assertEqual("skill.skai-dev-retro" in new_ids, adapter != "codex")
                                self.assertEqual("skill.skai-suggestion" in new_ids, adapter != "claude-code")
                        checked += 1
        self.assertEqual(checked, 63)
        print("PASS 63 Mac/Python resolver comparisons incl. newComponents; no configuration writes")


if __name__ == "__main__":
    unittest.main()
