"""Automated test for Bin/spec-tool.py against the sample files in fixtures/.

Run after any change to spec-tool.py: python3 internal/tests/tools/spec-tool/test.py
Commands that write (render, convert, link-terms) run on a temporary copy, so the
fixtures stay as committed.
"""
from pathlib import Path
import os
import re
import urllib.parse
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
TOOL = ROOT / "Bin/spec-tool.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def run(command, *args, fixtures=FIXTURES):
    """Run a tool command with fixture-relative paths; return (exit code, output lines relative to the fixtures)."""
    resolved = [str(fixtures / a) if not a.startswith("-") and (fixtures / a).exists() else a for a in args]
    result = subprocess.run([sys.executable, str(TOOL), command, *resolved], capture_output=True, text=True)
    output = (result.stdout + result.stderr).replace(f"{fixtures}/", "")
    return result.returncode, output.splitlines()


def issues(lines):
    return [line for line in lines if re.match(r"^[\w./-]+\.md:\d+: ", line)]


def notes(lines):
    return [line for line in lines if line.startswith("note: ")]


class Validate(unittest.TestCase):
    def test_package_projects_onto_catalog_with_notes_only(self):
        code, lines = run("validate", "catalog", "package/proposed-product-specs")
        self.assertEqual(code, 0, lines)
        self.assertEqual(issues(lines), [])
        found = notes(lines)
        self.assertEqual(len(found), 3, found)
        self.assertTrue(any("legacy-note.md" in n and "LEGACY-01 has no statement" in n for n in found))
        self.assertTrue(any("unlinked use of glossary term 'Notebook'" in n for n in found))
        self.assertTrue(any("duplicate ID LEGACY-02" in n for n in found))

    def test_catalog_alone_fails_on_the_defect_and_the_duplicate(self):
        code, lines = run("validate", "catalog")
        self.assertEqual(code, 1, lines)
        found = issues(lines)
        self.assertEqual(len(found), 2, found)
        self.assertTrue(any("LEGACY-01 has no statement" in i for i in found))
        self.assertTrue(any("duplicate ID LEGACY-02" in i for i in found))

    def test_design_package_projects_cleanly(self):
        code, lines = run("validate", "design-catalog", "design-package/proposed-design-specs")
        self.assertEqual(code, 0, lines)
        self.assertEqual(issues(lines) + notes(lines), [])
        self.assertIn("0 issues", lines[-1])

    def test_broken_names_every_injected_defect(self):
        code, lines = run("validate", "broken")
        self.assertEqual(code, 1)
        found = issues(lines)
        files = {i.split(":")[0] for i in found}
        expected_files = {f"broken/{p.name}" for p in (FIXTURES / "broken").glob("*.md") if p.name != "dup-a.md"}
        self.assertEqual(files, expected_files, "every broken file but the duplicate's first copy reports")
        gaps = [i for i in found if i.startswith("broken/gaps.md")]
        for message in ["gap footnote outside an item", "has no definition", "duplicate gap footnote label", "number by first use",
                        "gap footnote must read", "after a gap footnote", "after a known-difference note",
                        "in a canonical file"]:
            self.assertTrue(any(message in g for g in gaps), message)
        self.assertNotIn("broken/terms.md:12:", "\n".join(found), "a table header is a label, not a term use")
        glossary = [i for i in found if i.startswith("broken/glossary.md")]
        for message, count in [("a second Also called note in 'Delta term'", 1), ("an Also called note must read", 5),
                               ("prose after the Also called note", 1),
                               ("follows the entry's definition paragraph", 1), ("a blockquote outside a glossary entry", 1)]:
            self.assertEqual(sum(message in g for g in glossary), count, message)
        self.assertFalse(any("Theta term" in g for g in glossary), "a definition saying 'Also called' is not the note")
        self.assertEqual(len(found), 55, found)

    def test_revived_item_and_rule_are_rejected(self):
        code, lines = run("validate", "broken-revive/catalog", "broken-revive/drafts")
        self.assertEqual(code, 1)
        found = issues(lines)
        self.assertEqual(len(found), 2, found)
        self.assertTrue(all("broken-revive/catalog/domains/retired.md" in i for i in found))
        self.assertTrue(any("RET-01 revived" in i for i in found))
        self.assertTrue(any("RET-02-01 revived" in i for i in found))

    def test_projection_conflicts_fail_at_the_canonical_file(self):
        code, lines = run("validate", "broken-projection/catalog", "broken-projection/drafts")
        self.assertEqual(code, 1)
        found = issues(lines)
        self.assertEqual(len(found), 3, found)
        self.assertTrue(all(i.startswith("broken-projection/catalog/domains/citer.md:") for i in found))
        for target, change in [("[TGT-01]", "retire"), ("[TGT-02]", "move"), ("[g-widget-term]", "remove")]:
            self.assertTrue(any(target in i and change in i for i in found), target)
        found_notes = notes(lines)
        self.assertEqual(len(found_notes), 1, found_notes)
        self.assertIn("[TGT-09]", found_notes[0])

    def test_glossary_link_resolved_only_through_the_catalog_names_the_real_path(self):
        code, lines = run("validate", "broken-glossary-path/catalog", "broken-glossary-path/drafts")
        self.assertEqual(code, 1)
        found = issues(lines)
        self.assertEqual(len(found), 1, found)
        self.assertIn("broken-glossary-path/drafts/domains/wrong.md", found[0])
        self.assertIn("../../catalog/glossary.md", found[0])


class CheckChanges(unittest.TestCase):
    def test_product_change_list_matches(self):
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md")
        self.assertEqual(code, 0, lines)
        self.assertEqual(lines, ["0 issues"])

    def test_broken_product_change_list(self):
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "broken-package/product-specs-authoring.md")
        self.assertEqual(code, 1)
        found = issues(lines)
        text = "\n".join(found)
        decision_log = ["D1 carries 2 Decision lines", "D1 is checked but its last Decision Log entry is gap",
                        "D2 is a gap but its last Decision Log entry is missing", "R1 cites D9",
                        "not a Decision Log entry"]
        for message in decision_log:
            self.assertIn(message, text)
        self.assertEqual(sum(any(m in i for m in decision_log) for i in found), 5)
        pairing = ["D2 is a gap but no draft marks it", "gap footnote [^1] names D3"]
        for message in pairing:
            self.assertIn(message, text)
        self.assertEqual(sum(any(m in i for m in pairing) for i in found), 2)
        for message in ["R2 names item STAGE-04, which is unchanged", "R3 names STAGE-99, which is not in the drafts",
                        "R4 names rule STAGE-09-07, which is not in the drafts", "R5 declares add", "R6 declares retire",
                        "R7 declares move", "R8 declares add but file", "R9 declares modify but file"]:
            self.assertIn(message, text)
        self.assertTrue(any("but no change-list entry names it" in i for i in found))
        self.assertEqual([i for i in found if "D9" in i and "R1 cites D9" not in i], [],
                         "a log entry for an item the Discussion lacks is allowed")

    def test_design_change_list_matches(self):
        code, lines = run("check-changes", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "design-package/design-specs-authoring.md")
        self.assertEqual(code, 0, lines)
        self.assertEqual(lines, ["0 issues"])

    def test_broken_design_change_list_flags_only_the_index_and_the_log(self):
        code, lines = run("check-changes", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "broken-package/design-specs-authoring.md")
        self.assertEqual(code, 1)
        found = issues(lines)
        self.assertEqual(len(found), 4, found)
        self.assertTrue(any("no ## Decision Log section" in i for i in found))
        self.assertTrue(any("rule UI-NOTES-02-01 is modified but no change-list entry names it" in i for i in found))  # design specs list every changed rule
        self.assertTrue(any("_screens.md" in i and "intro is modified" in i for i in found))
        self.assertTrue(any("index line list-screen is added" in i for i in found))


class Writers(unittest.TestCase):
    """Commands that write files, each on a fresh copy of the fixtures."""

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.copy = Path(self.directory.name) / "fixtures"
        shutil.copytree(FIXTURES, self.copy)

    def tearDown(self):
        self.directory.cleanup()

    def test_render_product_package_page(self):
        page = self.copy / "package/product-specs-review.html"
        page.unlink()
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn("</b> gaps</button>", html)
        self.assertIn('data-f="gaps"', html)
        self.assertNotIn("<h2>Gaps (", html)
        self.assertRegex(html, r'class="item (added|modified) has-gap"')
        self.assertNotIn("<h2>Decision Log</h2>", html)
        self.assertNotRegex(html, r'<details class="item request discussion[^"]*"[^>]*><summary><span class="badge', "discussion items carry no square")
        self.assertIn('<section class="discussion"><h2>Discussion</h2>', html)
        self.assertIn('class="gapnote"', html)
        self.assertNotIn('class="gap"', html)
        for href in re.findall(r'(?:href|src)="([^"]*spec-review\.v1\.(?:css|js))"', html):
            self.assertTrue(Path(os.path.normpath(page.parent / urllib.parse.unquote(href))).is_file(), href)
        terminal = re.search(r'id="terminal-stage" open><summary><span class="badge">(\w+)</span>.*?<div class="why">', html, re.S)
        self.assertIsNotNone(terminal, "Terminal stage card")
        self.assertEqual(terminal.group(1), "modified", "a changed Also called note alone modifies the entry")
        self.assertIn('<blockquote class="mod"><b>Also called:</b>', terminal.group(0))
        self.assertIn('done (the web app).</ins>', terminal.group(0))
        self.assertIn("<blockquote><b>Also called:</b> journal (the import service, its API).</blockquote>", html)
        popover = re.search(r'<template id="tip-g-terminal-stage">.*?</template>', html, re.S).group(0)
        self.assertIn("<blockquote><b>Also called:</b> closed stage (support desk); done (the web app).</blockquote>", popover)

    def test_render_moved_glossary_entry_diffs_its_note(self):
        page = self.copy / "glossary-move/page.html"
        code, lines = run("render", "--catalog", "glossary-move/catalog", "--drafts", "glossary-move/drafts",
                          "--no-authoring", "--out", str(page), fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        text = page.read_text()
        for href in re.findall(r'(?:href|src)="([^"]*spec-review\.v1\.(?:css|js))"', text):
            self.assertTrue(Path(os.path.normpath(page.parent / urllib.parse.unquote(href))).is_file(), "assets resolve from an --out elsewhere: " + href)
        end = text.find("Moved from glossary.md")
        self.assertGreater(end, 0, "the moved entry names its old home")
        card = text[text.rfind('id="offer" open>', 0, end):end]
        self.assertIn('<blockquote class="mod"><b>Also called:</b>', card)
        self.assertIn("pitch (the web app).</ins>", card)
        self.assertNotIn("<del", card.split("<blockquote")[0], "the unchanged definition is not marked")

    def test_render_design_package_page(self):
        page = self.copy / "design-package/design-specs-review.html"
        page.unlink()
        code, lines = run("render", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "design-package/design-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        self.assertTrue(page.exists())

    def test_request_package_renders_and_checks_against_its_base(self):
        drafts = "package/change-requests/001/proposed-product-specs"
        page = self.copy / "package/change-requests/001/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", drafts, fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text(encoding="utf-8")
        self.assertIn("Change Package: package | 001", html)  # the base's id, then the request's number
        self.assertIn("tip-gap-base-d3", html)  # a footnote naming the base's item resolves to it
        self.assertTrue(any("'gaps': 1" in ln for ln in lines), lines)
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", drafts,
                          "--authoring", "package/change-requests/001/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        code, lines = run("validate", "catalog", drafts, fixtures=self.copy)  # the base's drafts come in between on their own
        self.assertEqual(code, 0, lines)
        self.assertEqual(issues(lines), [], lines)

    def test_convert_old_shape_validates_and_is_idempotent(self):
        code, lines = run("convert", "old-shape", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        code, lines = run("validate", "old-shape", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        self.assertEqual(issues(lines), [])
        before = {p: p.read_bytes() for p in (self.copy / "old-shape").rglob("*.md")}
        code, lines = run("convert", "old-shape", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        self.assertEqual({p: p.read_bytes() for p in (self.copy / "old-shape").rglob("*.md")}, before)

    def test_link_terms_rewrites_only_the_last_root(self):
        stale = self.copy / "link-terms/catalog/domains/stale.md"
        fresh = self.copy / "link-terms/drafts/domains/fresh.md"
        stale_before = stale.read_bytes()
        code, lines = run("link-terms", "link-terms/catalog", "link-terms/drafts", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        self.assertIn("linked 1 term uses", lines)
        self.assertIn("[g-alpha-term]: ../../catalog/glossary.md#alpha-term", fresh.read_text())
        self.assertEqual(stale.read_bytes(), stale_before)

    def test_link_terms_catalog_alone(self):
        stale = self.copy / "link-terms/catalog/domains/stale.md"
        code, lines = run("link-terms", "link-terms/catalog", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        self.assertIn("linked 1 term uses", lines)
        self.assertIn("[g-alpha-term]: ../glossary.md#alpha-term", stale.read_text())


if __name__ == "__main__":
    unittest.main()
