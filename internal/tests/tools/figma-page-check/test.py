"""Automated test for Bin/figma-page-check.js: runs the script under node against a mock Figma
with a change page built to hold every breach the script names beside clean Sections (a package
Section, requests, a stacked backup, a scratch Section that is skipped), and a Production page
where nesting is a breach.

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
PACKAGE = section("Pinned Notes", 200 + CLEAN["width"] + 100, 200, [section("Notes List", 50, 50, [frame("notes list", 50, 50)])])  # the package's Section
BAD = section("A — Bad", PACKAGE["x"] + PACKAGE["width"] + 100, 250, [
    frame("a · prefixed", 50, 50),
    frame("too close", 50, 950),            # 48 below the first (expected 100)
    frame("far column", 500, 50),           # 57 from the first column's right edge (expected 50)
    {"type": "TEXT", "name": "stray text", "id": "stray", "x": 50, "y": 1900, "width": 100, "height": 20, "children": []},
], fill=WHITE)
TOO_DEEP = section("Too Deep", BAD["x"] + BAD["width"] + 100, 200, [section("Mid", 50, 50, [section("Inner", 50, 50, [frame("s", 50, 50)])])])
REQUEST = section("CR-01 — Pin menu", TOO_DEEP["x"] + TOO_DEEP["width"] + 100, 200, [section("Note editor", 50, 50, [frame("note editor — pin menu", 50, 50)])])
NESTED_REQUEST = section("CR-01-01 — Pin order", REQUEST["x"] + REQUEST["width"] + 100, 200, [section("Pinned list", 50, 50, [frame("pinned list — order", 50, 50)])])  # a request against CR-01
BACKUP = section("Base — Pre CR-01", REQUEST["x"], 200 + REQUEST["height"] + 100, [section("Notes List", 50, 50, [frame("notes list", 50, 50)])])  # stacked under the request
STRAY_BACKUP = section("Base — Pre CR-02", NESTED_REQUEST["x"] + 30, 200 + NESTED_REQUEST["height"] + 300, [section("Notes List", 50, 50, [frame("notes list", 50, 50)])])
SCRATCH = section("Scratch — Card Layouts", NESTED_REQUEST["x"] + NESTED_REQUEST["width"] + 140, 900, [frame("a · anything", 7, 7), {"type": "TEXT", "name": "note", "id": "note", "x": 0, "y": 0, "width": 10, "height": 10, "children": []}], fill=WHITE)
PAGE = {"type": "PAGE", "name": "Pinned Notes A", "id": "page", "children": [CLEAN, BAD, PACKAGE, TOO_DEEP, REQUEST, NESTED_REQUEST, BACKUP, STRAY_BACKUP, SCRATCH, frame("loose frame", 0, 0)]}
PRODUCTION = {"type": "PAGE", "name": "Production", "id": "production", "children": [section("Notebooks", 200, 200, [section("Inner Area", 50, 50, [frame("notebooks", 50, 50)])])]}

HARNESS = """
const figma = { currentPage: PAGE, getNodeByIdAsync: async id => null, setCurrentPageAsync: async p => {} };
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
const run = new AsyncFunction("figma", SRC);
run(figma).then(r => { console.log(JSON.stringify(r)); }).catch(e => { console.error(e.stack || e); process.exit(1); });
"""


def run_check(page):
    src = SCRIPT.read_text()
    program = f"const PAGE = {json.dumps(page)};\nconst SRC = {json.dumps(src)};\n{HARNESS}"
    result = subprocess.run(["node", "-e", program], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


class Check(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("node"):
            raise unittest.SkipTest("node is not installed")
        cls.report = run_check(PAGE)
        cls.rules = {}
        for f in cls.report["findings"]:
            cls.rules.setdefault(f["rule"], []).append(f)

    def test_clean_section_has_no_findings(self):
        names = {f["node"] for f in self.report["findings"]}
        for clean in ("Notes", "notes", "notes — empty", "note editor", "Pinned Notes", "Notes List", "notes list", "CR-01 — Pin menu", "Note editor", "note editor — pin menu", "CR-01-01 — Pin order", "Pinned list", "Base — Pre CR-01", "Scratch — Card Layouts", "a · anything", "note"):
            self.assertNotIn(clean, names, clean)

    def test_every_rule_fires_once_where_planted(self):
        by = self.rules
        self.assertEqual({f["node"] for f in by["loose"]}, {"loose frame", "stray text"})
        self.assertEqual({f["node"] for f in by["prefix"]}, {"A — Bad", "a · prefixed"})
        self.assertEqual([f["node"] for f in by["fill"]], ["A — Bad"])
        self.assertTrue(any(f["node"] == "too close" for f in by["columns"]), by["columns"])
        self.assertTrue(any("far column" in f["detail"] or f["node"] == "A — Bad" for f in by["columns"]), by["columns"])
        self.assertEqual([f["node"] for f in by["nesting"]], ["Mid"])  # one level is allowed on a change page, two are not
        self.assertEqual([f["node"] for f in by["backup"]], ["Base — Pre CR-02"])
        self.assertTrue(any(f["node"] == "A — Bad" and "top at 250" in f["detail"] for f in by["sections"]), by["sections"])
        self.assertNotIn("padding", by, by.get("padding"))

    def test_backup_checked_alone_reports_no_placement(self):
        report = run_check(BACKUP)  # a Section target: the script cannot see its neighbours
        self.assertEqual([f for f in report["findings"] if f["rule"] == "backup"], [])

    def test_production_page_allows_no_nesting(self):
        report = run_check(PRODUCTION)
        self.assertEqual([(f["node"], f["rule"]) for f in report["findings"]], [("Notebooks", "nesting")])


if __name__ == "__main__":
    unittest.main()
