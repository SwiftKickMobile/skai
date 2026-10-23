"""Automated test for Bin/design-tool.py against the sample package in fixtures/.

Run after any change to design-tool.py: python3 internal/tests/tools/design-tool/test.py
Rendering writes a page, so it runs on a temporary copy of the fixtures.
"""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
TOOL = ROOT / "Bin/design-tool.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


class Render(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.copy = self.tmp / "fixtures"
        shutil.copytree(FIXTURES, self.copy)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def render(self, artifact):
        result = subprocess.run([sys.executable, str(TOOL), "render", "--authoring", str(artifact)], capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr

    def test_package_page(self):
        artifact = self.copy / "package/design-authoring.md"
        code, out = self.render(artifact)
        self.assertEqual(code, 0, out)
        self.assertIn("{'added': 1, 'modified': 1, 'removed': 1, 'open': 1, 'gaps': 1}", out, "V04 has no list marker and is not an entry")
        page = (artifact.parent / "design-review.html").read_text()
        self.assertIn("<title>Design Change: Package</title>", page, "the bar reads <title>: <path>")
        self.assertIn('<div class="sub">Pinned Notes</div>', page, "the artifact's name is the subtitle")
        self.assertIn("discussion complete; 1 gap carried", page)
        for cid, status, op in [("v01", "modified", "modify screen"), ("v02", "added", "add state"), ("v03", "retired", "remove state")]:
            self.assertRegex(page, rf'<details class="item request {status}" id="{cid}" open><summary><span class="badge">{status}</span><span class="id">{cid.upper()}</span><span class="status">{op}</span>')
        self.assertIn('<a href="https://example.test/file?node-id=1-1">notes</a>', page, "an inline link renders as an anchor")
        self.assertIn("<b>Why</b> Resolved decision: D01", page)
        self.assertNotIn('id="v04"', page, "a line without the list marker is not an entry")
        self.assertNotIn("## Inputs", page, "the page shows the card, Discussion and Design Changes only")
        self.assertIn("Bin/spec-review.v1.css", page, "the shared stylesheet is linked from the checkout")

    def test_request_page_names_its_path_and_rewrites_relative_links(self):
        artifact = self.copy / "package/change-requests/001/design-authoring.md"
        code, out = self.render(artifact)
        self.assertEqual(code, 0, out)
        page = (artifact.parent / "design-review.html").read_text()
        self.assertIn("<title>Design Change: Package | 001</title>", page)
        self.assertIn('<a href="../../design-authoring.md">the base</a>', page, "a relative link is rebased from the artifact to the page")
        self.assertIn("no discussion items", page)
        self.assertIn("<b>Why</b> Base decision: D01", page)


if __name__ == "__main__":
    unittest.main()
