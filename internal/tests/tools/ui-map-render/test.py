"""Automated test for Bin/ui-map-render.py against the worked example in Guides/UIMap/ui-map-demo.md.

Run after any change to ui-map-render.py: python3 internal/tests/tools/ui-map-render/test.py
Renders the guide's YAML block with `uv run` (the renderer declares its own dependencies) and checks
the Mermaid text matches the guide's Mermaid block exactly, and that the HTML page links the shared
page library and the viewer by relative paths, loads no web font, and titles itself by package.
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

    def test_title_names_the_change_package_and_its_requests(self):
        with tempfile.TemporaryDirectory() as directory:
            for relative, package in [("skai/changes/offers/ui-map/proposed-ui-map.yaml", "offers"),
                                      ("skai/changes/offers/changes/CR-01/ui-map/proposed-ui-map.yaml", "offers | CR-01"),
                                      ("skai/promoted/offers/promoted/CR-01/changes/CR-01-01/ui-map/proposed-ui-map.yaml", "offers | CR-01 | CR-01-01"),
                                      ("elsewhere/map.yaml", "Production")]:
                self.assertEqual(self.render_at(directory, relative)[2]["package"], package, relative)


if __name__ == "__main__":
    unittest.main()
