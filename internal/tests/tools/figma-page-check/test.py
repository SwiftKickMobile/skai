"""Automated test for Bin/figma-page-check.js: runs the script under node against a mock Figma
with a change page built to hold the layout breaches beside clean Sections (a package Section,
requests, a stacked backup, a scratch Section that is skipped), a Production page where nesting is
a breach, a page with a badly padded Section, and a second change page holding one clean screen
beside one that plants every content breach and every signal.

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


NOTE = {"label": "What this frame is for.", "categoryId": "purpose"}
BOUND = {"type": "SOLID", "color": {"r": 0, "g": 0, "b": 1}, "boundVariables": {"color": {"id": "v"}}}
RAW = {"type": "SOLID", "color": {"r": 0, "g": 0, "b": 1}}


def frame(name, x, y, w=393, h=852, type_="FRAME", noted=True, **more):
    node = {"type": type_, "name": name, "id": name, "x": x, "y": y, "width": w, "height": h, "children": [], "annotations": [NOTE] if noted else []}
    node.update(more)
    return node


def layer(type_, name, **more):
    node = {"type": type_, "name": name, "id": name, "x": 0, "y": 0, "width": 10, "height": 10, "children": []}
    node.update(more)
    return node


def instance(name, main, remote=False, fields=(), inside=None, **more):
    """`fields` is what the instance overrides on itself; `inside` maps a layer inside it to what it overrides there."""
    overrides = ([{"id": name, "overriddenFields": list(fields)}] if fields else []) + [{"id": k, "overriddenFields": list(v)} for k, v in (inside or {}).items()]
    return layer("INSTANCE", name, mainComponent={"id": main, "name": main, "remote": remote}, overrides=overrides, **more)


def bound(var):
    return {"type": "SOLID", "color": {"r": 0, "g": 0, "b": 1}, "boundVariables": {"color": {"id": var}}}


def gradient(stop_bound):
    return {"type": "GRADIENT_LINEAR", "gradientStops": [{"color": {"r": 0, "g": 0, "b": 1, "a": 1}, "boundVariables": {"color": {"id": "v"}} if stop_bound else {}}]}


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

# content checks: one clean screen, one planting every content breach and signal, and a component that needs no note
GOOD = frame("notes", 50, 50, fills=[BOUND], layoutMode="VERTICAL", paddingLeft=20, cornerRadius=8,
             boundVariables={"paddingLeft": {"id": "s"}, "cornerRadius": {"id": "r"}}, children=[
                 layer("TEXT", "title", textStyleId="S:1", fills=[BOUND]),
                 instance("bar", "Navigation Bar", remote=True),
                 layer("RECTANGLE", "photo", fills=[{"type": "IMAGE"}]),
                 layer("RECTANGLE", "bound gradient", fills=[gradient(True)]),
                 instance("nav", "Nav Wrapper", children=[instance("kit tab bar", "Tab Bar", remote=True)]),  # a kit used inside its local wrapper
                 # ranges with two text styles and two bound fills: Figma gives the layer no single value, and every range is fine
                 layer("TEXT", "two styles", textStyleId={"mixed": True}, fills={"mixed": True}, ranges=[{"textStyleId": "S:1", "fills": [BOUND]}, {"textStyleId": "S:2", "fills": [BOUND]}]),
             ])
PLANTED = frame("notes — empty", 50, 1002, noted=False, fills=[RAW], layoutMode="VERTICAL", paddingLeft=12, counterAxisSpacing=8, cornerRadius=8, children=[
    layer("TEXT", "bare text", textStyleId="", fills=[BOUND]),
    layer("FRAME", "Navigation Bar"),
    layer("FRAME", "Tab Bar"),                                      # named like the kit component used inside a wrapper
    layer("TEXT", "one bare range", textStyleId={"mixed": True}, fills={"mixed": True}, ranges=[{"textStyleId": "S:1", "fills": [BOUND]}, {"textStyleId": "", "fills": [RAW]}]),
    layer("RECTANGLE", "gradient", fills=[gradient(False)]),
    # the same override on an instance nested in three others: a signal too
    *[instance(f"cell {i}", "Cell", inside={f"cell {i} chip": ("fills",)}, children=[instance(f"cell {i} chip", "Deep Chip", fills=[BOUND])]) for i in (1, 2, 3)],
    # the same override on a plain layer, the chevron, inside three instances of one component: a signal as well
    *[instance(f"item {i}", "List Item", inside={f"item {i} chevron": ("fills",)}, children=[{**layer("VECTOR", "chevron", fills=[BOUND]), "id": f"item {i} chevron"}]) for i in (1, 2, 3)],
    # three instances of one component carrying the same fill override: a signal, and no breach since the override is bound
    instance("row 1", "Row", fields=("fills", "width"), fills=[BOUND]), instance("row 2", "Row", fields=("fills",), fills=[BOUND]), instance("row 3", "Row", fields=("fills",), fills=[BOUND]),
    instance("row 4", "Row", fields=("width",)),
    # a uniform radius override, as Figma lists it (the radius and all four corners), on three instances: one signal, not five
    *[instance(f"pill {i}", "Pill", fields=("cornerRadius", "topLeftRadius", "topRightRadius", "bottomLeftRadius", "bottomRightRadius"),
               cornerRadius=30, topLeftRadius=30, topRightRadius=30, bottomLeftRadius=30, bottomRightRadius=30,
               boundVariables={k: {"id": "r"} for k in ("topLeftRadius", "topRightRadius", "bottomLeftRadius", "bottomRightRadius")}) for i in (1, 2, 3)],
    # a text layer whose ranges differ in fill, overridden differently in each of three instances: no signal;
    # the same ranges in three others: a signal
    *[instance(f"note {i}", "Note Cell", inside={f"note {i} text": ("fills",)}, children=[{**layer("TEXT", "body", textStyleId="S:1", fills={"mixed": True}, ranges=[{"textStyleId": "S:1", "fills": [bound(f"ink {i}")]}, {"textStyleId": "S:1", "fills": [BOUND]}]), "id": f"note {i} text"}]) for i in (1, 2, 3)],
    *[instance(f"quote {i}", "Quote Cell", inside={f"quote {i} text": ("fills",)}, children=[{**layer("TEXT", "body", textStyleId="S:1", fills={"mixed": True}, ranges=[{"textStyleId": "S:1", "fills": [bound("ink")]}, {"textStyleId": "S:1", "fills": [BOUND]}]), "id": f"quote {i} text"}]) for i in (1, 2, 3)],
    # three instances overriding the same field with different values: no signal
    instance("tint 1", "Chip", fields=("fills",), fills=[bound("a")]), instance("tint 2", "Chip", fields=("fills",), fills=[bound("b")]), instance("tint 3", "Chip", fields=("fills",), fills=[bound("c")]),
    instance("inherits", "Card", fills=[RAW]),                      # its component's fill, not an override: no breach here
    # inside an instance, only an overridden layer is the screen's own
    instance("card", "Card", inside={"card label": ("fills",)}, children=[
        layer("TEXT", "card label", textStyleId="", fills=[RAW]),  # fill overridden: a breach; its text style is the component's
        layer("RECTANGLE", "card background", fills=[RAW]),        # not overridden: the component's
    ]),
])
CONTENT = {"type": "PAGE", "name": "Pinned Notes B", "id": "content", "children": [section("Pinned Notes", 200, 200, [
    section("Notes", 50, 50, [GOOD, PLANTED]),
    section("Components", 50 + 493 + 100, 50, [frame("Row", 50, 50, w=200, h=40, type_="COMPONENT", noted=False, children=[layer("TEXT", "row title", textStyleId="S:1", fills=[BOUND])])]),  # a component is made of layers: no loose-layers signal
    # swatches and specimens: no purpose notes, and no screen columns (these two sit 10 apart)
    section("Design System", 50 + 493 + 100 + 300 + 100, 50, [frame("Brand Blue", 50, 50, w=80, h=80, noted=False), frame("Body", 140, 50, w=80, h=80, noted=False)]),
])]}
LIBRARY = {"type": "PAGE", "name": "Components", "id": "library", "children": [section("Controls", 200, 200, [frame("Button", 50, 50, w=200, h=40, type_="COMPONENT_SET", noted=False)])]}
PADDED = {"type": "PAGE", "name": "Pinned Notes C", "id": "padded", "children": [section("Notes", 200, 200, [frame("notes", 30, 50)])]}  # content starts 30 in, not 50
STYLES = [{"name": "Body", "id": "Body", "boundVariables": {"fontSize": {"id": "t"}}}, {"name": "Unbound Size", "id": "Unbound Size", "boundVariables": {}},
          {"name": "Backup/pinned-notes/Body", "id": "backup", "boundVariables": {}},        # a backup style is not checked
          {"name": "Draft/other-change/Body", "id": "theirs", "boundVariables": {}},          # nor is another package's draft
          {"name": "Draft/Pinned Notes B/Caption", "id": "Draft/Pinned Notes B/Caption", "boundVariables": {}}]  # this page's own draft is

HARNESS = """
(function hydrate(n) { if (n.ranges) n.getStyledTextSegments = fields => n.ranges; (n.children || []).forEach(hydrate); })(PAGE);  // a text layer's ranges
const figma = { currentPage: PAGE, getNodeByIdAsync: async id => null, setCurrentPageAsync: async p => {},
  annotations: { getAnnotationCategoriesAsync: async () => CATEGORIES }, getLocalTextStylesAsync: async () => STYLES };
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
const run = new AsyncFunction("figma", SRC);
run(figma).then(r => { console.log(JSON.stringify(r)); }).catch(e => { console.error(e.stack || e); process.exit(1); });
"""


def run_check(page, categories=({"id": "purpose", "label": "Purpose"},), styles=()):
    src = SCRIPT.read_text()
    program = f"const PAGE = {json.dumps(page)};\nconst CATEGORIES = {json.dumps(list(categories))};\nconst STYLES = {json.dumps(list(styles))};\nconst SRC = {json.dumps(src)};\n{HARNESS}"
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
        self.assertEqual([(f["node"], f["rule"]) for f in report["findings"]], [("Notebooks", "nesting")])  # and no purpose note is asked of Production

    def test_content_breaches_fire_where_planted_and_nowhere_else(self):
        report = run_check(CONTENT, styles=STYLES)
        found = sorted((f["rule"], f["node"]) for f in report["findings"])
        self.assertEqual(found, [("color", "card label"), ("color", "gradient"), ("color", "notes — empty"), ("color", "one bare range"),
                                 ("dimension", "notes — empty"), ("dimension", "notes — empty"), ("dimension", "notes — empty"),
                                 ("purpose", "notes — empty"), ("text-style", "bare text"), ("text-style", "one bare range"),
                                 ("type-size", "Draft/Pinned Notes B/Caption"), ("type-size", "Unbound Size")])

    def test_signals_are_reported_apart_from_breaches(self):
        report = run_check(CONTENT, styles=STYLES)
        signals = {s["rule"]: s for s in report["signals"] if s["node"] != "notes"}
        self.assertEqual(signals["loose-layers"]["detail"][:2], "4 ")       # two text layers and the two lookalike frames
        repeated = sorted(s["detail"] for s in report["signals"] if s["rule"] == "repeated-override")
        self.assertEqual(len(repeated), 5, repeated)                        # three different tints are no signal
        self.assertIn('3 instances of "Deep Chip"', repeated[0])            # nested in three other instances
        self.assertIn('3 instances of "List Item" carry the same fills override on "chevron"', repeated[1])  # a plain layer inside
        self.assertIn('3 instances of "Pill" carry the same cornerRadius override', repeated[2])  # once, though five fields are listed
        self.assertIn('3 instances of "Quote Cell"', repeated[3])           # the same ranges; "Note Cell", whose ranges differ, is absent
        self.assertIn('3 instances of "Row"', repeated[4])                  # the fourth overrides only its width
        self.assertEqual({s["node"] for s in report["signals"] if s["rule"] == "loose-layers"}, {"notes", "notes — empty"})  # screens only: not the `Row` component
        self.assertEqual({s["node"] for s in report["signals"] if s["rule"] == "kit-lookalike"}, {"Navigation Bar", "Tab Bar"})  # the second kit is used only inside a wrapper
        self.assertFalse({"loose-layers", "repeated-override", "kit-lookalike"} & {f["rule"] for f in report["findings"]})

    def test_no_purpose_note_is_asked_on_the_components_page(self):
        self.assertEqual(run_check(LIBRARY)["findings"], [])

    def test_a_change_page_named_like_a_main_page_is_still_a_change_page(self):
        for name in ("Production Readiness A", "Components Refresh A"):
            page = {"type": "PAGE", "name": name, "id": name, "children": [section("Readiness", 200, 200, [section("Notes", 50, 50, [frame("notes", 50, 50, noted=False)])])]}
            self.assertEqual([(f["node"], f["rule"]) for f in run_check(page)["findings"]], [("notes", "purpose")], name)  # nesting allowed, note asked

    def test_a_size_pages_backup_keeps_production_rules_whatever_the_size_is_called(self):
        backup = {"type": "PAGE", "name": "Production (Release — Pre QA) — Pre pinned-notes", "id": "odd", "children": [
            section("Nested", 200, 200, [section("Inner Area", 50, 50, [frame("notes", 50, 50, noted=False)])])]}
        self.assertEqual([(f["node"], f["rule"]) for f in run_check(backup)["findings"]], [("Nested", "nesting")])

    def test_only_a_main_pages_backup_is_a_backup_page(self):
        page = {"type": "PAGE", "name": "Planning — Pre Launch", "id": "planning", "children": [section("Planning", 200, 200, [section("Notes", 50, 50, [frame("notes", 50, 50, noted=False)])])]}
        self.assertEqual([(f["node"], f["rule"]) for f in run_check(page)["findings"]], [("notes", "purpose")])  # a change page: its content is checked

    def test_a_backup_page_is_laid_out_as_its_page_and_its_content_is_not_checked(self):
        backup = {"type": "PAGE", "name": "Production — Pre pinned-notes", "id": "backup page", "children": [
            section("Notebooks", 200, 200, [frame("notebooks", 50, 50, noted=False, fills=[RAW])]),
            section("Nested", 200 + 493 + 100, 200, [section("Inner Area", 50, 50, [frame("notes", 50, 50)])])]}
        self.assertEqual([(f["node"], f["rule"]) for f in run_check(backup, styles=STYLES)["findings"]], [("Nested", "nesting")])  # no text style is checked either

    def test_the_design_system_page_is_not_laid_out_as_screen_columns(self):
        page = {"type": "PAGE", "name": "Design System", "id": "ds", "children": [section("Colors", 200, 200, [frame("Brand Blue", 50, 50, w=80, h=80, noted=False), frame("Brand White", 140, 50, w=80, h=80, noted=False)])]}
        self.assertEqual(run_check(page)["findings"], [])  # the two swatches sit 10 apart

    def test_a_badly_padded_section_is_a_breach(self):
        self.assertEqual([(f["node"], f["rule"]) for f in run_check(PADDED)["findings"]], [("Notes", "padding")])

    def test_a_file_with_no_purpose_category_breaches_every_change_page_screen(self):
        report = run_check(CONTENT, categories=())
        self.assertEqual(sorted(f["node"] for f in report["findings"] if f["rule"] == "purpose"), ["notes", "notes — empty"])


if __name__ == "__main__":
    unittest.main()
