"""Behavioral checks for the read-only installer history/selection planner."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("selection", ROOT / "Bin/skai-configuration.py")
selection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selection)


class ComponentHistoryTests(unittest.TestCase):
    def test_legacy_claude_identities_defer_without_losing_evidence(self):
        for alias in ["jetbrains-claudecode", "xcode-claudecode", "androidstudio-claudecode"]:
            with self.subTest(alias=alias), tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                (project / "skai").mkdir()
                component = "skill.skai-debugging"
                (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": [component]}))
                state = project / "skai/install-state.json"
                state.write_text(json.dumps({"installedAdapters": [{"adapter": alias, "lastSHA": "N", "componentHistory": {
                    component: {"installed": True, "lastAppliedSHA": "N-1", "lastAppliedAt": "2026-10-08"}}}]}))
                before = state.read_bytes()
                inventory = project / "inventory.json"
                inventory.write_text(json.dumps({"components": [component]}))
                manifest = selection.read_manifest()
                resolved = selection.resolve(project, "claude-code", "generic", manifest)
                with self.assertRaisesRegex(selection.ConfigurationError, "direct component-history"):
                    selection.history_proposal(project, "claude-code", resolved, inventory, "N+1", "2026-10-10", manifest)
                self.assertEqual(state.read_bytes(), before)
                # Another adapter's planner retains its independent identity boundary.
                resolved = selection.resolve(project, "codex", "generic", manifest)
                proposal = selection.history_proposal(project, "codex", resolved, inventory, "N+1", "2026-10-10", manifest)
                self.assertIsNone(proposal["migrations"][0]["fromSHA"])

    def test_legacy_discovery_precedence_and_read_only_destination(self):
        for local in [False, True]:
            with self.subTest(local=local), tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                (project / "skai").mkdir()
                (project / "docs/skai").mkdir(parents=True)
                component = "skill.skai-debugging"
                (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": [component]}))
                if local:
                    (project / "skai/config.local.json").write_text(json.dumps({"schemaVersion": 1, "overrides": {component: True}}))
                inventory = project / "inventory.json"
                inventory.write_text(json.dumps({"components": [component]}))
                manifest = selection.read_manifest()
                paths = ["docs/skai/install-state.json", "skai/install-state.json"]
                if local:
                    paths.append("skai/install-state.local.json")
                for index, relative in enumerate(paths):
                    state_path = project / relative
                    version = f"N{index}"
                    state_path.write_text(json.dumps({"lastSHA": version, "lastUpdatedAt": "2026-10-08", "installedAdapters": [{"adapter": "codex"}]}))
                    before = {p: p.read_bytes() for p in project.rglob("*.json")}
                    resolved = selection.resolve(project, "codex", "generic", manifest)
                    proposal = selection.history_proposal(project, "codex", resolved, inventory, "N+1", "2026-10-10", manifest)
                    self.assertEqual(proposal["migrations"][0]["fromSHA"], version)
                    self.assertEqual(proposal["baselineAdapterState"]["componentHistory"][component]["lastAppliedAt"], "2026-10-08")
                    destination = "install-state.local.json" if local else "install-state.json"
                    self.assertEqual(proposal["statePath"], str(project.resolve() / "skai" / destination))
                    self.assertEqual({p: p.read_bytes() for p in project.rglob("*.json")}, before)

    def test_invalid_legacy_state_blocks_and_canonical_state_wins(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "docs/skai").mkdir(parents=True)
            legacy = project / "docs/skai/install-state.json"
            inventory = project / "inventory.json"
            inventory.write_text(json.dumps({"components": []}))
            manifest = selection.read_manifest()
            resolved = selection.resolve(project, "codex", "generic", manifest)
            for contents in ["broken", "[]", '{"installedAdapters": false}']:
                legacy.write_text(contents)
                with self.subTest(contents=contents), self.assertRaises(selection.ConfigurationError):
                    selection.history_proposal(project, "codex", resolved, inventory, "N", "2026-10-10", manifest)
            (project / "skai").mkdir()
            (project / "skai/install-state.json").write_text('{"installedAdapters": []}')
            selection.history_proposal(project, "codex", resolved, inventory, "N", "2026-10-10", manifest)

    def test_legacy_symlink_escape_blocks(self):
        for directory_link in [False, True]:
            with self.subTest(directory_link=directory_link), tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
                project = Path(directory)
                external = Path(outside) / "install-state.json"
                external.write_text('{"installedAdapters": []}')
                (project / "docs").mkdir()
                if directory_link:
                    (project / "docs/skai").symlink_to(Path(outside), target_is_directory=True)
                else:
                    (project / "docs/skai").mkdir()
                    (project / "docs/skai/install-state.json").symlink_to(external)
                inventory = project / "inventory.json"
                inventory.write_text('{"components": []}')
                manifest = selection.read_manifest()
                resolved = selection.resolve(project, "codex", "generic", manifest)
                with self.assertRaises(selection.ConfigurationError):
                    selection.history_proposal(project, "codex", resolved, inventory, "N", "2026-10-10", manifest)

    def plan(self, previous, actual, desired, version="N+1", track=True):
        return selection.plan_history(previous, set(actual), set(desired), fingerprint="selection",
                                      target_sha=version, date="2026-10-09", track=track,
                                      baseline_sha="N", baseline_date="2026-10-08")

    def test_defaults_need_no_component_ledger(self):
        result = self.plan({"adapter": "codex", "lastSHA": "N"}, ["A"], ["A"], track=False)
        self.assertFalse(result["tracking"])
        self.assertNotIn("componentHistory", result["nextAdapterState"])

    def test_disable_then_reenable_at_same_global_version(self):
        disabled = self.plan({"adapter": "codex", "lastSHA": "N", "lastRunAt": "2026-10-08"}, ["A"], [])
        baseline = disabled["baselineAdapterState"]
        self.assertEqual(baseline["lastSHA"], "N")
        self.assertTrue(baseline["componentHistory"]["A"]["installed"])
        state = disabled["nextAdapterState"]
        self.assertEqual(state["lastSHA"], "N+1")
        self.assertEqual(state["componentHistory"]["A"]["lastAppliedSHA"], "N")
        self.assertEqual(state["componentHistory"]["A"]["lastDisabledSHA"], "N+1")
        enabled = self.plan(state, [], ["A"])
        self.assertEqual(enabled["migrations"], [{"id": "A", "fromSHA": "N", "toSHA": "N+1", "reason": "version-gap"}])
        self.assertEqual(enabled["nextAdapterState"]["componentHistory"]["A"]["lastAppliedSHA"], "N+1")
        self.assertEqual(state["componentHistory"]["A"]["lastAppliedSHA"], "N")  # pure proposal

    def test_failed_migration_can_resume_from_saved_baseline(self):
        proposal = self.plan({"lastSHA": "N"}, ["A"], ["A"])
        failed_state = proposal["baselineAdapterState"]
        retried = self.plan(failed_state, [], ["A"])
        self.assertEqual(retried["migrations"][0]["fromSHA"], "N")

    def test_return_to_defaults_retains_disabled_history(self):
        state = self.plan({"lastSHA": "N"}, ["A"], [])["nextAdapterState"]
        default = self.plan(state, [], ["A"], version="N+3", track=False)
        self.assertTrue(default["tracking"])
        self.assertEqual(default["migrations"][0]["fromSHA"], "N")
        self.assertEqual(default["migrations"][0]["toSHA"], "N+3")

    def test_default_selection_removal_preserves_version_until_reenabled(self):
        # A default/eligibility change can remove A without any custom configuration.
        original = {"adapter": "codex", "lastSHA": "N", "lastRunAt": "2026-10-08"}
        disabled = self.plan(original, ["A", "B"], ["B"], track=False)
        self.assertTrue(disabled["tracking"])
        baseline = disabled["baselineAdapterState"]
        self.assertEqual(baseline["lastSHA"], "N")
        self.assertTrue(baseline["componentHistory"]["A"]["installed"])
        state = disabled["nextAdapterState"]
        self.assertFalse(state["componentHistory"]["A"]["installed"])
        self.assertEqual(state["componentHistory"]["A"]["lastAppliedSHA"], "N")
        later = self.plan(state, ["B"], ["B"], version="N+2", track=False)
        record = later["nextAdapterState"]["componentHistory"]["A"]
        self.assertEqual(record["lastAppliedSHA"], "N")
        self.assertEqual(record["lastDisabledSHA"], "N+1")
        enabled = self.plan(later["nextAdapterState"], ["B"], ["A", "B"], version="N+3", track=False)
        migration = next(m for m in enabled["migrations"] if m["id"] == "A")
        self.assertEqual((migration["fromSHA"], migration["toSHA"]), ("N", "N+3"))
        self.assertNotIn("componentHistory", original)  # proposals never mutate prior evidence

    def test_newly_enabled_component_does_not_inherit_other_components_version(self):
        proposal = self.plan({"lastSHA": "N"}, ["A"], ["A", "B"])
        migration = next(m for m in proposal["migrations"] if m["id"] == "B")
        self.assertIsNone(migration["fromSHA"])
        self.assertEqual(migration["reason"], "no-known-installed-version")
        self.assertNotIn("B", proposal["baselineAdapterState"]["componentHistory"])

    def test_failed_default_removal_can_resume_from_baseline(self):
        failed = self.plan({"lastSHA": "N"}, ["A"], [], track=False)["baselineAdapterState"]
        # Removal happened but success was not recorded. History still proves the old version.
        retry = self.plan(failed, [], ["A"], track=False)
        self.assertEqual(retry["migrations"][0]["fromSHA"], "N")
        self.assertEqual(failed["lastSHA"], "N")

    def test_retired_component_history_is_not_discarded(self):
        previous = {"lastSHA": "N+1", "componentHistory": {
            "retired": {"installed": False, "lastAppliedSHA": "N", "lastDisabledSHA": "N+1"}}}
        result = self.plan(previous, [], ["A"], version="N+3", track=False)
        self.assertEqual(result["nextAdapterState"]["componentHistory"]["retired"], previous["componentHistory"]["retired"])

    def test_invalid_history_blocks_instead_of_resetting(self):
        for history in [[], {"A": None}, {"A": {"installed": 1, "lastAppliedSHA": "N"}},
                        {"A": {"installed": False, "lastAppliedSHA": 7}}]:
            with self.subTest(history=history), self.assertRaises(selection.ConfigurationError):
                self.plan({"lastSHA": "N", "componentHistory": history}, ["A"], ["A"])

    def test_empty_local_overrides_do_not_start_ledger(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "skai").mkdir()
            (project / "skai/config.local.json").write_text(json.dumps({"schemaVersion": 1, "overrides": {}}))
            resolved = selection.resolve(project, "codex", "generic", selection.read_manifest())
            self.assertFalse(resolved["trackComponents"])
            self.assertEqual(resolved["historyScope"], "local")
            (project / "skai/config.local.json").unlink()
            (project / "skai/install-state.local.json").write_text(json.dumps({"installedAdapters": []}))
            self.assertEqual(selection.resolve(project, "codex", "generic", selection.read_manifest())["historyScope"], "local")

    def test_local_ledger_takes_precedence_over_newer_shared_state(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "skai").mkdir()
            component = "skill.skai-debugging"
            (project / "skai/install-state.json").write_text(json.dumps({"installedAdapters": [
                {"adapter": "codex", "lastSHA": "N+5"}]}))
            (project / "skai/install-state.local.json").write_text(json.dumps({"installedAdapters": [
                {"adapter": "codex", "lastSHA": "N+1", "componentHistory": {
                    component: {"installed": False, "lastAppliedSHA": "N"}}}]}))
            (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": [component]}))
            inventory = project / "inventory.json"
            inventory.write_text(json.dumps({"components": []}))
            manifest = selection.read_manifest()
            resolved = selection.resolve(project, "codex", "generic", manifest)
            proposal = selection.history_proposal(project, "codex", resolved, inventory, "N+6", "2026-10-10", manifest)
            self.assertEqual(proposal["migrations"][0]["fromSHA"], "N")
            self.assertEqual(proposal["baselineAdapterState"]["lastSHA"], "N+1")

    def test_mixed_adapter_global_sha_does_not_invent_component_version(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "skai").mkdir()
            component = "skill.skai-debugging"
            (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": [component]}))
            (project / "skai/install-state.json").write_text(json.dumps({"lastSHA": "N+5", "installedAdapters": [
                {"adapter": "codex"}, {"adapter": "cursor", "lastSHA": "N+5"}]}))
            inventory = project / "inventory.json"
            inventory.write_text(json.dumps({"components": [component]}))
            manifest = selection.read_manifest()
            resolved = selection.resolve(project, "codex", "generic", manifest)
            proposal = selection.history_proposal(project, "codex", resolved, inventory, "N+6", "2026-10-10", manifest)
            self.assertIsNone(proposal["migrations"][0]["fromSHA"])

    def test_unknown_baseline_is_not_invented(self):
        result = selection.plan_history({}, {"A"}, {"A"}, fingerprint="f", target_sha="N+1", date="2026-10-09", track=True)
        self.assertIsNone(result["migrations"][0]["fromSHA"])

    def test_single_adapter_global_fallback_requires_matching_identity(self):
        for recorded, expected in [("codex", "N"), ("cursor", None)]:
            with self.subTest(recorded=recorded), tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                (project / "skai").mkdir()
                component = "skill.skai-debugging"
                (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": [component]}))
                (project / "skai/install-state.json").write_text(json.dumps({"lastSHA": "N", "lastUpdatedAt": "2026-10-08", "installedAdapters": [{"adapter": recorded}]}))
                inventory = project / "inventory.json"
                inventory.write_text(json.dumps({"components": [component]}))
                manifest = selection.read_manifest()
                resolved = selection.resolve(project, "codex", "generic", manifest)
                proposal = selection.history_proposal(project, "codex", resolved, inventory, "N+1", "2026-10-10", manifest)
                self.assertEqual(proposal["migrations"][0]["fromSHA"], expected)
                self.assertEqual(proposal["baselineAdapterState"]["componentHistory"][component]["lastAppliedAt"], "2026-10-08" if expected else None)

    def test_invalid_new_baseline_blocks_before_record_creation(self):
        for previous in [{"lastSHA": 7}, {"lastSHA": True}, {"lastSHA": "N", "lastRunAt": 4}]:
            with self.subTest(previous=previous), self.assertRaises(selection.ConfigurationError):
                self.plan(previous, ["A"], ["A"])

    def test_local_override_precedence_and_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "skai").mkdir()
            (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": ["skill.skai-debugging"]}))
            (project / "skai/config.local.json").write_text(json.dumps({"schemaVersion": 1, "overrides": {"skill.skai-debugging": False, "skill.skai-ui-map-architecture": True}}))
            result = selection.resolve(project, "codex", "generic", selection.read_manifest())
            self.assertEqual({a["id"] for a in result["skills"]}, {"skill.skai-configure", "skill.skai-ui-map-architecture"})
            self.assertEqual(result["historyScope"], "local")
            self.assertTrue(result["historyStatePath"].endswith("install-state.local.json"))

    def test_known_retired_ids_do_not_block_other_selections(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "skai").mkdir()
            (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": ["skill.skai-ui-map-planning", "skill.skai-debugging"]}))
            result = selection.resolve(project, "codex", "generic", selection.read_manifest())
            self.assertEqual({a["id"] for a in result["skills"]}, {"skill.skai-configure", "skill.skai-debugging"})

    def test_local_history_proposal_preserves_shared_state(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "skai").mkdir()
            shared = project / "skai/install-state.json"
            shared.write_text(json.dumps({"lastSHA": "N", "installedAdapters": [{"adapter": "codex", "lastSHA": "N"}]}))
            before = shared.read_bytes()
            (project / "skai/config.local.json").write_text(json.dumps({"schemaVersion": 1, "overrides": {"skill.skai-debugging": False}}))
            inventory = project / "inventory.json"
            inventory.write_text(json.dumps({"components": ["skill.skai-debugging"]}))
            manifest = selection.read_manifest()
            resolved = selection.resolve(project, "codex", "generic", manifest)
            proposal = selection.history_proposal(project, "codex", resolved, inventory, "N+1", "2026-10-09", manifest)
            record = proposal["nextAdapterState"]["componentHistory"]["skill.skai-debugging"]
            self.assertFalse(record["installed"])
            self.assertEqual(record["lastAppliedSHA"], "N")
            self.assertTrue(proposal["statePath"].endswith("install-state.local.json"))
            self.assertEqual(shared.read_bytes(), before)
            self.assertFalse((project / "skai/install-state.local.json").exists())  # planner is read-only

    def test_new_components_enable_and_decline(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "skai").mkdir()
            manifest = selection.read_manifest()
            # Default host: nothing is new.
            self.assertEqual(selection.resolve(project, "codex", "generic", manifest)["newComponents"], [])
            with self.assertRaisesRegex(selection.ConfigurationError, "No project config"):
                selection.enable_components(project, ["skill.skai-debugging"], manifest)
            (project / "skai/config.json").write_text(json.dumps({"schemaVersion": 1, "components": ["skill.skai-debugging"], "note": "keep"}))
            state = project / "skai/install-state.json"
            state.write_text(json.dumps({"managedBy": "skai", "installedAdapters": [
                {"adapter": "codex", "componentHistory": {"skill.skai-dev-retro": {"installed": False, "lastAppliedSHA": "N"}}},
                {"adapter": "claude-code"}]}))
            new = {c["id"] for c in selection.resolve(project, "codex", "generic", manifest)["newComponents"]}
            self.assertIn("skill.skai-suggestion", new)
            self.assertNotIn("skill.skai-debugging", new)       # chosen
            self.assertNotIn("skill.skai-dev-retro", new)       # seen by this adapter
            self.assertNotIn("skill.skai-configure", new)       # required
            self.assertIn("skill.skai-dev-retro", {c["id"] for c in selection.resolve(project, "claude-code", "generic", manifest)["newComponents"]})
            result = selection.enable_components(project, ["skill.skai-suggestion"], manifest)
            config = json.loads((project / "skai/config.json").read_text())
            self.assertEqual(config["components"], ["skill.skai-debugging", "skill.skai-suggestion"])
            self.assertEqual(config["note"], "keep")
            self.assertEqual(result["enabled"], ["skill.skai-suggestion"])
            with self.assertRaisesRegex(selection.ConfigurationError, "Unknown"):
                selection.enable_components(project, ["skill.skai-configure"], manifest)
            result = selection.decline_components(project, ["skill.skai-unit-testing"], manifest, "project", "N+1", "2026-10-12")
            records = json.loads(state.read_text())["installedAdapters"]
            for record in records:
                entry = record["componentHistory"]["skill.skai-unit-testing"]
                self.assertEqual((entry["installed"], entry["lastAppliedSHA"], entry["declinedSHA"], entry["declinedAt"]), (False, None, "N+1", "2026-10-12"))
            self.assertEqual(result["declined"], ["skill.skai-unit-testing"])
            new = {c["id"] for c in selection.resolve(project, "codex", "generic", manifest)["newComponents"]}
            self.assertNotIn("skill.skai-unit-testing", new)
            self.assertNotIn("skill.skai-suggestion", new)
            with self.assertRaisesRegex(selection.ConfigurationError, "already in the component history"):
                selection.decline_components(project, ["skill.skai-unit-testing"], manifest, "project", "N+1", "2026-10-12")
            # A declined record is a valid, unknown-version baseline for the planner once re-enabled.
            proposal = selection.plan_history(records[0], set(), {"skill.skai-unit-testing"}, fingerprint="f", target_sha="N+2", date="2026-10-13", track=True)
            self.assertEqual(proposal["migrations"][0]["reason"], "no-known-installed-version")


if __name__ == "__main__":
    unittest.main()
