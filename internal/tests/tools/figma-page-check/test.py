"""Automated test for Bin/figma-page-check.js: runs the script under node against a mock Figma
with a page built to hold every breach the script names, plus one clean Section.

Run after any change to figma-page-check.js: python3 internal/tests/tools/figma-page-check/test.py
"""
from pathlib import Path
import json
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / "Bin/figma-page-check.js"

FILL = {"type": "SOLID", "color": {"r": 0xFA / 255, "g": 0xFA / 255, "b": 0xFA / 255}}
WHITE = {"type": "SOLID", "color": {"r": 1, "g": 1, "b": 1}}


def frame(name, x, y, w=393, h=852, type_="FRAME"):
    return {"type": type_, "name": name, "id": name, "x": x, "y": y, "width": w, "height": h, "children": []}


def section(name, x, y, children, fill=FILL, w=None, h=None):
    content = [c for c in children if c["type"] in ("FRAME", "COMPONENT", "INSTANCE", "COMPONENT_SET", "SECTION")]
    inner_w = max(c["x"] + c["width"] for c in content) + 50 if content else 100
    inner_h = max(c["y"] + c["height"] for c in content) + 50 if content else 100
    return {"type": "SECTION", "name": name, "id": name, "x": x, "y": y, "width": w or inner_w, "height": h or inner_h, "fills": [fill], "children": children}


# a clean Section: two columns 50 apart, two states 100 apart
CLEAN = section("Notes", 200, 200, [frame("notes", 50, 50), frame("notes — empty", 50, 1002), frame("note editor", 493, 50)])
# every breach once
BAD = section("A — Bad", 200 + CLEAN["width"] + 100, 250, [
    frame("a · prefixed", 50, 50),
    frame("too close", 50, 950),            # 48 below the first (expected 100)
    frame("far column", 500, 50),           # 57 from the first column's right edge (expected 50)
    {"type": "TEXT", "name": "stray text", "id": "stray", "x": 50, "y": 1900, "width": 100, "height": 20, "children": []},
], fill=WHITE)
NESTED = section("Not A Request", BAD["x"] + BAD["width"] + 100, 200, [section("Inner", 50, 50, [frame("s", 50, 50)])])
REQUEST = section("CR-001 — Pin menu", NESTED["x"] + NESTED["width"] + 100, 200, [section("Note editor", 50, 50, [frame("note editor — pin menu", 50, 50)])])
PAGE = {"type": "PAGE", "name": "Page", "id": "page", "children": [CLEAN, BAD, NESTED, REQUEST, frame("loose frame", 0, 0)]}

HARNESS = """
const figma = { currentPage: PAGE, getNodeByIdAsync: async id => null, setCurrentPageAsync: async p => {} };
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
const run = new AsyncFunction("figma", SRC);
run(figma).then(r => { console.log(JSON.stringify(r)); }).catch(e => { console.error(e.stack || e); process.exit(1); });
"""


class Check(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("node"):
            raise unittest.SkipTest("node is not installed")
        src = SCRIPT.read_text()
        program = f"const PAGE = {json.dumps(PAGE)};\nconst SRC = {json.dumps(src)};\n{HARNESS}"
        result = subprocess.run(["node", "-e", program], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        cls.report = json.loads(result.stdout)
        cls.rules = {}
        for f in cls.report["findings"]:
            cls.rules.setdefault(f["rule"], []).append(f)

    def test_clean_section_has_no_findings(self):
        names = {f["node"] for f in self.report["findings"]}
        for clean in ("Notes", "notes", "notes — empty", "note editor", "CR-001 — Pin menu", "Note editor", "note editor — pin menu"):
            self.assertNotIn(clean, names, clean)

    def test_every_rule_fires_once_where_planted(self):
        by = self.rules
        self.assertEqual({f["node"] for f in by["loose"]}, {"loose frame", "stray text"})
        self.assertEqual({f["node"] for f in by["prefix"]}, {"A — Bad", "a · prefixed"})
        self.assertEqual([f["node"] for f in by["fill"]], ["A — Bad"])
        self.assertTrue(any(f["node"] == "too close" for f in by["columns"]), by["columns"])
        self.assertTrue(any("far column" in f["detail"] or f["node"] == "A — Bad" for f in by["columns"]), by["columns"])
        self.assertEqual([f["node"] for f in by["nesting"]], ["Not A Request"])
        self.assertTrue(any(f["node"] == "A — Bad" and "top at 250" in f["detail"] for f in by["sections"]), by["sections"])
        self.assertNotIn("padding", by, by.get("padding"))


if __name__ == "__main__":
    unittest.main()
