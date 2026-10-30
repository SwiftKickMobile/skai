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
        self.assertIn("{'added': 1, 'modified': 1, 'removed': 1, 'open': 0, 'gaps': 3, 'resolved': 1}", out, "V04 has no list marker and is not an entry; a gap is not open; every entry that marks a gap counts")
        page = (artifact.parent / "design-review.html").read_text()
        self.assertIn("<title>Design Change: Package</title>", page, "the bar reads <title>: <path>")
        self.assertIn('<div class="sub">Pinned Notes</div>', page, "the artifact's name is the subtitle")
        pass
        for cid, status, op in [("v01", "modified", "modify screen"), ("v02", "added", "add state"), ("v03", "retired", "remove state")]:
            self.assertRegex(page, rf'<details class="item request {status}(?: has-gap)?" id="{cid}" open><summary><span class="badge">{status}</span><span class="id">{cid.upper()}</span><span class="status">{op}</span>')
        self.assertIn('<a href="https://example.test/file?node-id=1-1">notes</a>', page, "an inline link renders as an anchor")
        self.assertIn('<h3 class="section">Notes</h3>', page, "a heading per screen, in artifact order")
        self.assertIn('<h3 class="section">Note editor</h3>', page)
        self.assertIn('<li><span class="rid">01</span>A <code>Pinned</code> group with its own header above the rest of the list <span class="why">— Resolved decision: <a class="ref" href="#d01" data-tip="tip-gap-own-d01">D01</a></span></li>', page, "sub-changes render as a numbered list with their justification")
        self.assertIn('<b>Why</b> Resolved decision: <a class="ref" href="#d01" data-tip="tip-gap-own-d01">D01</a>', page, "V03 keeps its own Why")
        self.assertIn('shows a hint line.<sup class="fn">2</sup>', page, "the footnote mark is inert")
        self.assertIn('<div class="gapnotes"><div class="gapnote" id="gap-v02-2"><sup class="fn">2</sup><div class="gapbody"><a class="ref" href="#d02" data-tip="tip-gap-own-d02">D02</a> the empty group does not collapse either.</div></div></div>', page, "a card's notes share one box; a note is the owning item's chip, with tooltip and link, then this frame's placeholder in one line")
        self.assertNotIn('<div class="pop-src">', page.split('<template id="tip-gap-own-d02">')[1].split("</template>")[0], "this artifact's items carry no source line")
        self.assertIn('<template id="tip-gap-own-d02">', page, "the owning item's tooltip exists")
        self.assertIn('class="item request added has-gap" id="v02"', page, "a footnoted entry carries has-gap for the gaps filter")
        self.assertIn('<div class="gapnote" id="gap-v01-1">', page, "V01's own footnote renders under V01")
        self.assertIn("discussion complete; 3 gaps carried", page)
        self.assertNotIn("**Gap:**", page)
        self.assertNotIn("[^1]:", page, "the definition is not left in the Why")
        self.assertNotIn('id="v04"', page, "a line without the list marker is not an entry")
        self.assertNotIn("## Inputs", page, "the page shows the card, Discussion and Design Changes only")
        self.assertIn("Bin/spec-review.v1.css", page, "the shared stylesheet is linked from the checkout")
        self.assertNotIn(' open</button>', page, "a gap is not an open item; with none open the tile is absent")
        self.assertIn('<b>3</b> gaps</button>', page, "the gaps tile counts the open gap item and both entries that mark the gap")
        self.assertIn('<b>1</b> resolved</button>', page)

    def test_request_page_names_its_path_and_rewrites_relative_links(self):
        artifact = self.copy / "package/change-requests/001/design-authoring.md"
        code, out = self.render(artifact)
        self.assertEqual(code, 0, out)
        page = (artifact.parent / "design-review.html").read_text()
        self.assertIn("<title>Design Change: Package | 001</title>", page)
        self.assertIn('<a href="../../design-authoring.md">the base</a>', page, "a relative link is rebased from the artifact to the page")
        self.assertIn("no discussion items; 1 gap carried", page, "an inherited gap shows in the card state with no Discussion item")
        self.assertIn("<b>Why</b> Base decision: D01", page)
        self.assertIn('<a class="ref" href="../../design-review.html#d02" data-tip="tip-gap-base-d02">D02</a>', page, "a base item shows its ID alone, links to the base's page and carries its tooltip")
        self.assertIn('<template id="tip-gap-base-d02"><div class="pop-src">../../design-review.html</div>', page, "the tooltip of another document's item starts with that document's review page path")

    def test_package_built_on_a_sibling_package_links_its_base(self):
        artifact = self.copy / "followup/design-authoring.md"
        code, out = self.render(artifact)
        self.assertEqual(code, 0, out)
        page = (artifact.parent / "design-review.html").read_text()
        self.assertIn('<a class="ref" href="../package/design-review.html#d02" data-tip="tip-gap-base-d02">D02</a>', page, "a package's base named first under Inputs resolves a base owner, linked to the base's page with its tooltip")
        self.assertIn('<template id="tip-gap-base-d02"><div class="pop-src">../package/design-review.html</div>', page)


if __name__ == "__main__":
    unittest.main()
