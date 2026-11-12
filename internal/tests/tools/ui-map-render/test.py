"""Automated test for Bin/ui-map-render.py against the worked example in Guides/UIMap/ui-map-demo.md.

Run after any change to ui-map-render.py: python3 internal/tests/tools/ui-map-render/test.py
Renders the guide's YAML block with `uv run` (the renderer declares its own dependencies) and checks
the Mermaid text matches the guide's Mermaid block exactly, and that the HTML page links the shared
page library and the viewer by relative paths, loads no web font, titles itself by package, and
carries the demo's form factors for the viewer's drop-down.
A change package's page (fixtures below, in temporary folders) carries the Review tab, change badges
and side panel entries from its architecture artifact's Discussion and Map Changes; an entry naming a
scene the proposed map lacks fails the render, except a removed scene or a list pending re-derivation;
a request's page layers its map over its bases', nearest winning.
"""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
RENDERER = ROOT / "Bin/ui-map-render.py"
DEMO = ROOT / "Guides/UIMap/ui-map-demo.md"


def fenced_block(text, language):
    blocks = re.findall(rf"^```{language}\n(.*?)^```$", text, flags=re.S | re.M)
    if len(blocks) != 1:
        raise AssertionError(f"expected one ```{language} block in {DEMO.name}, found {len(blocks)}")
    return blocks[0]


class DemoRender(unittest.TestCase):
    def test_demo_yaml_renders_to_the_guide_mermaid_block(self):
        self.assertIsNotNone(shutil.which("uv"), "uv is required to run the renderer")
        guide = DEMO.read_text()
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "ui-map-demo.yaml"
            output = Path(directory) / "ui-map-demo.mmd"
            source.write_text(fenced_block(guide, "yaml"))
            result = subprocess.run(["uv", "run", "--quiet", str(RENDERER), str(source), "-o", str(output)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(output.read_text().rstrip("\n"), fenced_block(guide, "mermaid").rstrip("\n"))


class HtmlPage(unittest.TestCase):
    def render_at(self, directory, relative):
        """Renders the demo YAML from `relative` under `directory` to a page beside it; the page's text and its model."""
        source = Path(directory) / relative
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(fenced_block(DEMO.read_text(), "yaml"))
        page = source.with_suffix(".html")
        result = subprocess.run(["uv", "run", "--quiet", str(RENDERER), str(source), "--html", str(page)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        text = page.read_text()
        model = json.loads(re.search(r"<script>window\.UI_MAP = (.*?);</script>", text).group(1).replace("<\\/", "</"))
        return page, text, model

    def test_page_links_the_shared_library_and_viewer_and_loads_no_web_font(self):
        with tempfile.TemporaryDirectory() as directory:
            page, text, model = self.render_at(directory, "skai/ui-map/ui-map.yaml")
            assets = [a or b for a, b in re.findall(r'<link rel="stylesheet" href="([^"]+)">|<script src="([^"]+)"></script>', text)]
            self.assertEqual([Path(a).name for a in assets], ["skai-pages.v1.css", "ui-map-viewer.v2.css", "skai-pages.v1.js", "ui-map-viewer.v2.js"],
                             "the shared page library first, then the viewer's own stylesheet and script")
            for href in assets:
                self.assertFalse(href.startswith("/") or "://" in href, "assets are linked by a relative path: " + href)
                self.assertTrue(Path(os.path.normpath(page.parent / href)).is_file(), "assets resolve from the page: " + href)
            self.assertNotIn("Archivo", text)
            self.assertNotIn("fonts.googleapis", text, "no web font: the system font")
            self.assertIn(f"<title>{model['app']} UI Map</title>", text, "the HTML title keeps the app's name")
            self.assertEqual(model["package"], "Production", "the official map is titled UI Map Production")

    def test_page_model_carries_the_demo_form_factors(self):
        with tempfile.TemporaryDirectory() as directory:
            model = self.render_at(directory, "skai/ui-map/ui-map.yaml")[2]
            scenes = model["scenes"]
            self.assertEqual(model["formFactors"], ["phone", "tablet"], "the page shows its form-factor drop-down for two or more")
            self.assertEqual(scenes["outline"]["formFactors"], ["tablet"])
            self.assertIsNone(scenes["note"]["formFactors"], "a scene on every form factor is unmarked")
            routes = {r["kind"]: r for r in scenes["notes"]["routes"]}
            self.assertEqual((routes["nav"]["formFactors"], routes["composite"]["formFactors"]), ([["phone"]], [["tablet"]]),
                             "each route into Note carries its own form factors, for the gray-out and the route label's icon")
            self.assertEqual(scenes["tag_picker"]["modalStyle"], {"phone": "sheet", "tablet": "popover"})

    def test_title_names_the_change_package_and_its_requests(self):
        with tempfile.TemporaryDirectory() as directory:
            for relative, package in [("skai/changes/offers/ui-map/proposed-ui-map.yaml", "offers"),
                                      ("skai/changes/offers/changes/CR-01/ui-map/proposed-ui-map.yaml", "offers | CR-01"),
                                      ("skai/promoted/offers/promoted/CR-01/changes/CR-01-01/ui-map/proposed-ui-map.yaml", "offers | CR-01 | CR-01-01"),
                                      ("elsewhere/map.yaml", "Production")]:
                self.assertEqual(self.render_at(directory, relative)[2]["package"], package, relative)


PROPOSED = """version: 1
app: LumenNotes
modal_styles: [sheet, popover]
domains:
  app:
    child:
      - library
      - login: {}
  library:
    tab:
      - notes:
          nav:
            - note
      - folders
  note:
    modal:
      - share_sheet:
          modal_style: popover
      - version_history:
          modal_style: sheet
  storage:
    scenes:
      - folders: {}
"""

ARTIFACT = """# UI Map — Note Versions

## Goal

Let people restore a note's older versions.

## Discussion

### Storage

- [ ] D01 [Question] Does Folders stay a tab of Library?
  - **Concern** It moves to its own domain.
  - **Question** Whether it stays a tab.
  - **Gap** It stays a tab for now.
- [x] D02 [Proposal] Version History opens as a sheet
  - **Concern** People need earlier text.
  - **Proposal** A sheet.
  - **Decision** Adopted.

## Map Changes

### App

- M1 remove route: login
  - **Description** Login no longer leads to Welcome.
  - **Justification** Welcome is gone; Resolved decision: D02
- M2 remove scene: welcome
  - **Description** The onboarding scene that was never built.
  - **Justification** Onboarding is no longer planned; Supervisor input

### Note

- M3 modify scene: note
  - **01** It opens Version History as a modal — older versions are a side task; Resolved decision: D02
  - **02** Its note says restoring replaces the text — restoring can't be undone; Supervisor input
- M4 add scene: version_history
  - **Description** A sheet listing a note's older versions.
  - **Justification** People need earlier text; Resolved decision: D02
- M5 modify scene-attribute: share_sheet
  - **Description** It opens as a popover.
  - **Justification** The note stays in view; Supervisor input

### Storage

- M6 add domain: storage
  - **Description** A new domain for the places notes are kept.
  - **Justification** Folders grew beyond the library; Supervisor input
- M7 move scene: folders
  - **Description** It moves here from Library.[^1]
  - **Justification** It belongs with the places notes are kept; Supervisor input

  [^1]: **Gap:** D01. Placeholder: it stays a tab of Library for now.

## Decision Log
"""


class ChangePackagePage(unittest.TestCase):
    """A change package's page: fixtures written to a temporary skai/ tree."""

    def write(self, root, relative, text):
        path = Path(root) / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def render(self, target, page):
        return subprocess.run(["uv", "run", "--quiet", str(RENDERER), str(target), "--html", str(page)], capture_output=True, text=True)

    def page_model(self, page):
        text = page.read_text()
        return text, json.loads(re.search(r"<script>window\.UI_MAP = (.*?);</script>", text).group(1).replace("<\\/", "</"))

    def package(self, root, artifact=ARTIFACT, proposed=PROPOSED):
        folder = Path(root) / "skai/changes/note-versions/ui-map"
        self.write(root, "skai/ui-map/ui-map.yaml", fenced_block(DEMO.read_text(), "yaml"))
        self.write(folder, "proposed-ui-map.yaml", proposed)
        self.write(folder, "ui-map-architecture.md", artifact)
        return folder

    def test_review_tab_badges_and_panel_entries_come_from_the_artifact(self):
        with tempfile.TemporaryDirectory() as root:
            folder = self.package(root)
            page = folder / "proposed-ui-map.html"
            result = self.render(folder / "proposed-ui-map.yaml", page)
            self.assertEqual(result.returncode, 0, result.stderr)
            text, model = self.page_model(page)
            assets = [Path(a or b).name for a, b in re.findall(r'<link rel="stylesheet" href="([^"]+)">|<script src="([^"]+)"></script>', text)]
            self.assertEqual(assets, ["skai-pages.v1.css", "spec-review.v2.css", "ui-map-viewer.v2.css", "skai-pages.v1.js", "ui-map-viewer.v2.js"],
                             "a change package's page takes the review pages' cards for its Review tab")
            review = model["review"]
            self.assertEqual({k: review["counts"][k] for k in ("added", "modified", "removed", "moved", "resolved")},
                             {"added": 2, "modified": 2, "removed": 2, "moved": 1, "resolved": 1})
            self.assertEqual(review["changed"], ["login", "note", "share_sheet", "version_history", "folders"],
                             "a scene is marked when an entry names it, in map order; a removed scene and a domain change mark nothing")
            html = review["html"]
            self.assertIn('<h2>Map Changes</h2>', html)
            self.assertRegex(html, r'<h3 class="section"><i class="dm" style="--c:#[0-9A-F]{6}"></i>Storage</h3>', "a domain heading carries its colour square")
            self.assertIn('<a class="scene" href="#scene=login" data-scene="login">Login</a>', html, "a route entry names its start scene, linked to the map")
            self.assertIn('<span class="gone">Welcome</span>', html, "a removed scene is greyed and unlinked")
            self.assertRegex(html, r'<span class="status pill">add domain</span><span class="title">Storage</span>', "a domain change names its domain unlinked")
            self.assertIn('<details class="item request moved has-gap" id="m7" open>', html, "a moved scene is its own change type; a footnoted entry has a gap")
            self.assertIn('<span class="rid">01</span>', html, "numbered sub-changes")
            self.assertIn('id="gap-m7-1"', html, "the gap footnote")
            self.assertIn('id="d01"', html, "the Discussion")
            panel = review["changes"]["note"][0]
            self.assertIn('<a class="id" href="#m3">M3</a>', panel, "the panel entry's ID links to the entry in the Review tab")
            self.assertIn("older versions are a side task.", panel)
            self.assertNotIn("Resolved decision", panel, "the panel's reasons drop their source")
            self.assertNotIn("welcome", review["changes"])

    def test_an_entry_naming_a_scene_off_the_map_fails_except_a_removed_scene(self):
        for entry, fails in [("- M8 modify scene: ghost", True), ("- M8 add route: ghost", True), ("- M8 move scene: ghost", True),
                             ("- M8 modify domain: ghost", True), ("- M8 remove scene: ghost", False), ("- M8 remove domain: ghost", False),
                             ("- M8 rename scene: note", True), ("- M8 remove scene: old-ghost", False), ("- M8 modify scene: new-ghost", True), ("- M8 remove scene: `old ghost`", False), ("- M8 modify scene: `new ghost`", True)]:
            with self.subTest(entry=entry), tempfile.TemporaryDirectory() as root:
                folder = self.package(root, ARTIFACT.replace("## Decision Log", f"### Other\n\n{entry}\n  - **Description** x.\n\n## Decision Log"))
                result = self.render(folder, folder / "proposed-ui-map.html")
                self.assertEqual(result.returncode, 3 if fails else 0, result.stderr)
                if fails:
                    self.assertIn("M8", result.stderr)

    def test_a_list_pending_re_derivation_is_shown_but_never_checked(self):
        with tempfile.TemporaryDirectory() as root:
            artifact = ARTIFACT.replace("## Map Changes\n", "## Map Changes\n\nPending re-derivation.\n").replace("## Decision Log", "### Other\n\n- M8 modify scene: ghost\n\n## Decision Log")
            folder = self.package(root, artifact)
            result = self.render(folder, folder / "proposed-ui-map.html")
            self.assertEqual(result.returncode, 0, result.stderr)
            review = self.page_model(folder / "proposed-ui-map.html")[1]["review"]
            self.assertIn("Pending re-derivation.", review["html"])
            self.assertIn('id="m8"', review["html"], "the pending list is still shown")
            self.assertNotIn("ghost", review["changes"], "a scene the map lacks gets no badge")

    def test_the_production_page_has_no_review_tab(self):
        with tempfile.TemporaryDirectory() as root:
            self.package(root)
            map_file = Path(root) / "skai/ui-map/ui-map.yaml"
            self.write(root, "skai/ui-map/ui-map-architecture.md", ARTIFACT)
            result = self.render(map_file, map_file.with_suffix(".html"))
            self.assertEqual(result.returncode, 0, result.stderr)
            text, model = self.page_model(map_file.with_suffix(".html"))
            self.assertIsNone(model["review"])
            self.assertNotIn("spec-review", text)

    def test_a_request_layers_its_map_over_its_bases_nearest_winning(self):
        with tempfile.TemporaryDirectory() as root:
            base = self.package(root)
            request = base.parent / "changes/CR-01/ui-map"
            self.write(request, "ui-map-architecture.md", "# UI Map — CR-01\n\n## Goal\n\nA request.\n\n## Map Changes\n\n### Note\n\n- M1 modify scene: version_history\n  - **Description** x.\n")
            page = request / "proposed-ui-map.html"
            result = self.render(request, page)
            self.assertEqual(result.returncode, 0, result.stderr)
            model = self.page_model(page)[1]
            self.assertEqual(model["package"], "note-versions | CR-01")
            self.assertIn("version_history", model["scenes"], "no map of its own: its base's proposed map")
            self.assertEqual(model["review"]["changed"], ["version_history"], "its own Map Changes")
            self.write(request, "proposed-ui-map.yaml", PROPOSED.replace("      - version_history:\n          modal_style: sheet\n", "      - version_history:\n          modal_style: sheet\n      - history_detail:\n          modal_style: sheet\n"))
            self.assertEqual(self.render(request / "proposed-ui-map.yaml", page).returncode, 0)
            self.assertIn("history_detail", self.page_model(page)[1]["scenes"], "its own map wins")
            (base / "proposed-ui-map.yaml").unlink()
            (request / "proposed-ui-map.yaml").unlink()
            orphan = self.write(request, "ui-map-architecture.md", "# UI Map — CR-01\n\n## Goal\n\nA request.\n")
            self.assertEqual(self.render(orphan.parent, page).returncode, 0)
            self.assertIn("welcome", self.page_model(page)[1]["scenes"], "no package map up the chain: the production map")


if __name__ == "__main__":
    unittest.main()
