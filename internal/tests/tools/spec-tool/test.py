"""Automated test for Bin/spec-tool.py against the sample files in fixtures/.

Run after any change to spec-tool.py: python3 internal/tests/tools/spec-tool/test.py
Commands that write (render, convert, link-terms) run on a temporary copy, so the
fixtures stay as committed.
"""
from pathlib import Path
import os
import re
import html as html_mod
import urllib.parse
import shutil
import subprocess
import sys
import tempfile
import unittest
import importlib.util

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

    def test_render_shows_the_no_items_sentence(self):
        authoring = self.copy / "package/product-specs-authoring.md"
        text = authoring.read_text()
        text = re.sub(r"^## Discussion\n.*?(?=^## )", "## Discussion\n\nThe catalog settles every requirement here; the drafts follow it.\n\n", text, flags=re.M | re.S)
        text = re.sub(r"^## Decision Log\n.*", "## Decision Log\n", text, flags=re.M | re.S)
        authoring.write_text(text)
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn('<span class="status">no discussion items</span>', html)
        self.assertIn('<p class="note">The catalog settles every requirement here; the drafts follow it.</p>', html)

    def test_render_intro_covered_through_touches_shows_the_covering_reason(self):
        draft = self.copy / "package/proposed-product-specs/domains/workflow-stage.md"
        draft.write_text(draft.read_text().replace("\n\n## ", " Stages are listed first.\n\n## ", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        card = re.search(r'<div class="item prose modified"><p class="intro modified">.*?Stages are listed first.*?</p>(<div class="why">.*?</div>)?</div>', html, re.S)
        self.assertIsNotNone(card, "the changed intro renders as modified")
        self.assertIsNotNone(card.group(1), "an intro covered through a requirement entry's Touches shows that entry's reason")
        why = html_mod.unescape(re.sub(r"<[^>]+>", "", card.group(1)))
        if why.count("R") > 1:
            self.assertIn("Changed with this file's entries", why, "several covering entries are named in one line, their reasons never pasted together")
            self.assertNotIn("; R", why, "no concatenated reasons")

    def test_render_justification_citation_stays_a_link_inside_a_draft_card(self):
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        card = re.search(r'id="stage-01".*?<div class="why"><b>Why</b> (.*?)</div>', html, re.S)
        self.assertIsNotNone(card, "STAGE-01 card with a Why")
        self.assertRegex(card.group(1), r'<a class="ref" href="#d1" data-tip="tip-gap-own-d1">D1</a>', "the cited decision is the item itself: a chip linked to its card, with the item's tooltip")

    def test_render_index_line_covered_through_touches_shows_the_covering_reason(self):
        index = ("# Domains\n\n- [workflow-stage] -- `STAGE-` -- the stages a notebook moves through\n"
                 "- [suggestion-status] -- `SUGGESTION-STATUS-` -- reported statuses\n\n"
                 "[workflow-stage]: workflow-stage.md\n[suggestion-status]: suggestion-status.md\n")
        (self.copy / "catalog/domains/_domains.md").write_text(index)
        (self.copy / "package/proposed-product-specs/domains/_domains.md").write_text(index.replace("the stages a notebook moves through", "the stage table and what each stage holds"))
        authoring = self.copy / "package/product-specs-authoring.md"
        authoring.write_text(authoring.read_text().replace("  - **Touches** domains/workflow-stage.md\n", "  - **Touches** domains/workflow-stage.md, domains/_domains.md\n", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn("stage table", html, "the changed index line renders")
        self.assertRegex(html, r'stage table.{0,900}?<div class="why"><b>Why</b> Resolved decision:', "an index line covered through an entry's Touches shows that entry's reason")

    def test_render_added_file_covered_through_touches_shows_the_covering_reason(self):
        drafts = self.copy / "package/proposed-product-specs/domains"
        for name, iid in (("extra.md", "EXTRA-01"), ("extra-two.md", "EXTRA2-01")):
            (drafts / name).write_text(f"# {name[:-3].title()}\n\nSpillover items.\n\n## Items\n\n### {iid}\nSomething a person can observe.\n")
        authoring = self.copy / "package/product-specs-authoring.md"
        text = authoring.read_text()
        text = text.replace("## Requirement Changes\n", "## Requirement Changes\n\n- R9 add file: domains/extra.md\n  - **Justification** Both files hold what the suggestion domain spilled over; Supervisor input\n  - **Touches** domains/extra.md, domains/extra-two.md\n", 1)
        authoring.write_text(text)
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        for name in ("extra.md", "extra-two.md"):
            section = re.search(rf'domains/{re.escape(name)}.{{0,1500}}?<p class="file-why"><b>Why</b> (.*?)</p>', html, re.S)
            self.assertIsNotNone(section, f"{name} shows a file-level reason")
            self.assertIn("spilled over", section.group(1), f"{name} shows the covering entry's reason")

    def test_render_new_section_orientation_text_shows_as_added_with_its_reason(self):
        draft = self.copy / "package/proposed-product-specs/domains/workflow-stage.md"
        draft.write_text(draft.read_text().replace("## Entries\n", "## Extras\n\nSpillover notes about stages.\n\n### STAGE-90\nSomething a person can observe.\n\n## Entries\n", 1))
        authoring = self.copy / "package/product-specs-authoring.md"
        authoring.write_text(authoring.read_text().replace("## Requirement Changes\n", "## Requirement Changes\n\n- R9 add requirement: [STAGE-90]\n  - **Justification** The stage work left notes with no home; Supervisor input\n  - **Touches** domains/workflow-stage.md\n", 1).replace("\n[STAGE-01]:", "\n[STAGE-90]: proposed-product-specs/domains/workflow-stage.md#stage-90\n[STAGE-01]:", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        card = re.search(r'<div class="item prose modified"><p class="intro modified"><span class="badge modified"></span>(.*?)</p>(<div class="why">.*?</div>)?</div>', html, re.S)
        cards = [m for m in re.finditer(r'<div class="item prose modified"><p class="intro modified"><span class="badge modified"></span>(.*?)</p>(<div class="why">.*?</div>)?</div>', html, re.S) if "Spillover notes" in m.group(1)]
        self.assertEqual(len(cards), 1, "the new section's orientation text renders as a changed prose card")
        self.assertIsNotNone(cards[0].group(2), "it carries the covering entry's reason")
        self.assertTrue("no home" in cards[0].group(2) or "Changed with this file" in cards[0].group(2), "one covering entry lends its reason; several are named in one line")

    def test_render_removed_section_orientation_text_shows_as_missing(self):
        base = self.copy / "catalog/domains/workflow-stage.md"
        base.write_text(base.read_text().replace("## Entries\n\n", "## Entries\n\nWhat every entry in a stage carries.\n\n", 1))
        draft = self.copy / "package/proposed-product-specs/domains/workflow-stage.md"
        text = draft.read_text()
        start, end = text.index("## Entries\n"), text.index("## Attention\n")
        draft.write_text(text[:start] + text[end:])
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertRegex(html, r'<div class="item prose modified"><p class="intro modified"><span class="badge modified"></span><del[^>]*>What every entry in a stage carries', "the removed section's orientation text renders as a deleted prose card")

    def test_render_glossary_intro_change_shows_with_its_covering_reason(self):
        glossary = self.copy / "package/proposed-product-specs/glossary.md"
        glossary.write_text(glossary.read_text().replace("Terms the product specs use, and the items that govern each.", "Terms the product specs use, the items that govern each, and the suggestion terms added here.", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        cards = [m for m in re.finditer(r'<div class="item prose modified"><p class="intro modified"><span class="badge modified"></span>(.*?)</p>(<div class="why">.*?</div>)?</div>', html, re.S) if "suggestion terms added here" in m.group(1)]
        self.assertEqual(len(cards), 1, "the changed glossary intro renders as a changed prose card")
        self.assertIsNotNone(cards[0].group(2), "it carries the reason of the entries whose Touches name the glossary")
        self.assertIn("R11", cards[0].group(2), "several covering entries are attributed by ID")

    def test_render_section_prose_takes_no_reason_from_a_same_named_glossary_term(self):
        draft = self.copy / "package/proposed-product-specs/domains/workflow-stage.md"
        draft.write_text(draft.read_text().replace("What the stages are, what each holds, and which are terminal.", "What the stages are, what each holds, which are terminal, and how they are ordered.", 1))
        glossary = self.copy / "package/proposed-product-specs/glossary.md"
        glossary.write_text(glossary.read_text().replace("### Active suggestion", "### Stages\nThe ordered set of workflow stages ([STAGE-01]).\n\n### Active suggestion", 1))
        authoring = self.copy / "package/product-specs-authoring.md"
        authoring.write_text(authoring.read_text().replace("## Requirement Changes\n", "## Requirement Changes\n\n- R9 add glossary entry: Stages\n  - **Justification** A term for the whole set was missing; Supervisor input\n  - **Touches** glossary.md\n", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        cards = [m for m in re.finditer(r'<div class="item prose modified"><p class="intro modified">(.*?)</p>(<div class="why">.*?</div>)?</div>', html, re.S) if "how they are ordered" in m.group(1)]
        self.assertEqual(len(cards), 1, "the changed section prose renders as one card holding text and reason")
        self.assertIsNotNone(cards[0].group(2))
        self.assertNotIn("whole set was missing", cards[0].group(2), "a glossary entry sharing the section's name lends it no reason")
        self.assertIn("R1", cards[0].group(2), "the reason comes from the entries covering the file through Touches, named in one line")

    def test_render_section_with_orientation_text_and_no_items(self):
        draft = self.copy / "package/proposed-product-specs/domains/workflow-stage.md"
        draft.write_text(draft.read_text().replace("## Entries\n", "## Notes\n\nOrientation only, no items yet.\n\n## Entries\n", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn('<h3 class="section">Notes</h3>', html, "a section with no items still renders its heading")
        self.assertRegex(html, r'<div class="item prose modified"><p class="intro modified"><span class="badge modified"></span><ins[^>]*>Orientation only, no items yet\.</ins>', "its new orientation text renders as an added prose card")

    def test_render_design_rule_change_shows_its_entry_reason(self):
        page = self.copy / "design-package/design-specs-review.html"
        code, lines = run("render", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "design-package/design-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        li = re.search(r'<li class="mod" data-rid="UI-NOTES-02-01">.*?</li>', html, re.S)
        self.assertIsNotNone(li, "the changed rule renders as modified")
        self.assertIn('<span class="why">— ', li.group(0), "a changed rule carries its own entry's reason")
        self.assertIn("badge follows the 2026 guidance", li.group(0))

    def test_render_removed_table_column_shows_its_old_cells(self):
        full = "\n| Stage | Holds | Terminal |\n|---|---|---|\n| Archived | finished work | Yes, for good |\n| Deleted | removed notes | Yes, for good |\n"
        narrow = "\n| Stage | Holds |\n|---|---|\n| Archived | finished work |\n| Deleted | removed notes |\n"
        for path, table in ((self.copy / "catalog/domains/workflow-stage.md", full), (self.copy / "package/proposed-product-specs/domains/workflow-stage.md", narrow)):
            text = path.read_text()
            i = text.index("### STAGE-03\n"); j = text.index("\n\n", i) + 1
            path.write_text(text[:j] + table + text[j:])
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertRegex(html, r'<del[^>]*>Yes, for good</del>', "the removed column's old cells show as deletions")

    def test_render_rule_with_table_only_change_shows_its_reason(self):
        rule = "- **01** The title is the note's first line, truncated to one line.\n"
        table = "\n  | Length | Shown |\n  | --- | --- |\n  | Short | whole |\n  | Long | {cut} |\n"
        for path, cut in ((self.copy / "design-catalog/screens/notes.md", "first line"), (self.copy / "design-package/proposed-design-specs/screens/notes.md", "first 40 characters")):
            text = path.read_text(); assert text.count(rule) == 1
            path.write_text(text.replace(rule, rule + table.format(cut=cut), 1))
        authoring = self.copy / "design-package/design-specs-authoring.md"
        text = authoring.read_text()
        text = text.replace("- S1 modify rule: [UI-NOTES-01.02]", "- S10 modify rule: [UI-NOTES-01.01]\n  - **Justification** Long titles were cut at a line, which varies by device; Supervisor input\n  - **Touches** [notes][s-notes]\n\n- S1 modify rule: [UI-NOTES-01.02]", 1)
        text = text.replace("[UI-NOTES-01.02]: proposed-design-specs/screens/notes.md#ui-notes-01", "[UI-NOTES-01.01]: proposed-design-specs/screens/notes.md#ui-notes-01\n[UI-NOTES-01.02]: proposed-design-specs/screens/notes.md#ui-notes-01", 1)
        authoring.write_text(text)
        page = self.copy / "design-package/design-specs-review.html"
        code, lines = run("render", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "design-package/design-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        li = re.search(r'<li class="[^"]*" data-rid="UI-NOTES-01-01">.*?</li>', html, re.S)
        self.assertIsNotNone(li, "rule 01 renders")
        self.assertRegex(li.group(0), r'<ins[^>]*>40\s*characters', "its table change renders as a diff")
        self.assertIn("varies by device", li.group(0), "a rule whose table alone changed shows its entry's reason")

    def test_render_topic_citation_reaches_its_heading_and_an_unshown_section_reaches_the_artifact(self):
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn('<h3 class="section" id="stage-definitions">', html, "a Discussion topic heading carries its anchor")
        authoring = self.copy / "package/product-specs-authoring.md"
        text = authoring.read_text().replace("  - **Proposal** A.\n", "  - **Proposal** A; see [the assumptions][assumptions].\n", 1) + "[assumptions]: #assumptions-and-todos\n"
        authoring.write_text(text)
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertRegex(html, r'<a class="link" href="[^"]*product-specs-authoring\.md#assumptions-and-todos">the assumptions</a>', "a citation to a section the page omits is a plain link to the artifact at that section, not a chip")

    def test_render_citation_into_another_artifact_keeps_that_artifact(self):
        authoring = self.copy / "package/product-specs-authoring.md"
        authoring.write_text(authoring.read_text().replace("[D1]: #stage-definitions", "[D1]: change-requests/001/product-specs-authoring.md#stage-definitions", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn('<h3 class="section" id="stage-definitions">', html, "the page has a same-named local topic")
        card = re.search(r'id="stage-01".*?<div class="why"><b>Why</b> (.*?)</div>', html, re.S)
        self.assertIsNotNone(card)
        self.assertRegex(card.group(1), r'href="[^"]*change-requests/001/product-specs-authoring\.md#stage-definitions"', "a citation into another artifact is not shortened to the same-named local anchor")

    def test_render_id_reference_defined_in_another_artifact_keeps_that_artifact(self):
        authoring = self.copy / "package/product-specs-authoring.md"
        text = authoring.read_text()
        self.assertIn("[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01", text)
        authoring.write_text(text.replace("[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01", "[STAGE-01]: change-requests/001/proposed-product-specs/domains/workflow-stage.md#stage-01", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        d1 = re.search(r'<details class="item request discussion[^"]*" id="d1".*?</details>', html, re.S)
        self.assertIsNotNone(d1)
        self.assertRegex(d1.group(0), r'href="[^"]*change-requests/001/proposed-product-specs/domains/workflow-stage\.md#stage-01"', "an ID reference the artifact defines in another document keeps that document, though the page has an item of that ID")

    def test_render_gap_tooltip_keeps_the_items_nested_bullets(self):
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        tip = re.search(r'<template id="tip-gap-[^"]*-d2">.*?</template>', html, re.S)
        self.assertIsNotNone(tip, "the open Tradeoff D2 has a gap tooltip")
        self.assertIn("Missing expiration leaves a Submitted suggestion active", tip.group(0), "the tooltip carries the item's alternatives, not only the Options label")

    def test_render_gap_tooltip_resolves_citations_as_its_own_artifact_defines_them(self):
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        tip = re.search(r'<template id="tip-gap-[^"]*-d2">.*?</template>', html, re.S)
        self.assertIsNotNone(tip, "the open Tradeoff D2 has a gap tooltip")
        self.assertRegex(tip.group(0), r'href="[^"]*change-requests/001/product-specs-authoring\.md"', "a reference-style citation in the owning item keeps its link in the tooltip, resolved by the artifact's own definitions")

    def test_target_identity_qualifies_headings_by_document_but_not_item_ids(self):
        spec = importlib.util.spec_from_file_location("st", TOOL); st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
        self.assertEqual(st.target_identity("../a.md#stage-01"), st.target_identity("../b.md#stage-01"), "a spec item's ID is the same item wherever its file sits")
        self.assertNotEqual(st.target_identity("../first-review.md#decision"), st.target_identity("../second-review.md#decision"), "a heading belongs to its document")

    def test_render_same_id_in_another_document_gets_its_own_tooltip(self):
        authoring = self.copy / "package/product-specs-authoring.md"
        authoring.write_text(authoring.read_text().replace("[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01", "[STAGE-01]: change-requests/001/proposed-product-specs/domains/workflow-stage.md#stage-01", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        d1 = re.search(r'<details class="item request discussion[^"]*" id="d1".*?</details>', html, re.S).group(0)
        link = re.search(r'<a class="ref" href="[^"]*change-requests/001/[^"]*#stage-01"([^>]*)>STAGE-01</a>', d1)
        self.assertIsNotNone(link, "the citation links to the other document")
        tipid = re.search(r'data-tip="([^"]+)"', link.group(1))
        self.assertIsNotNone(tipid, "it carries a tooltip")
        self.assertNotEqual(tipid.group(1), "tip-stage-01", "not the page's own STAGE-01 tooltip")
        self.assertIn(f'<template id="{tipid.group(1)}">', html, "the other document's item has its own popover")

    def test_render_term_defined_in_another_glossary_shows_no_local_definition(self):
        other = self.copy / "package/other-glossary.md"
        other.write_text("# Other Glossary\n\n### Notebook\nA different definition kept elsewhere.\n")
        authoring = self.copy / "package/product-specs-authoring.md"
        text = authoring.read_text()
        self.assertIn("[g-notebook]: proposed-product-specs/glossary.md#notebook", text)
        authoring.write_text(text.replace("[g-notebook]: proposed-product-specs/glossary.md#notebook", "[g-notebook]: other-glossary.md#notebook", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn('<a class="link" href="other-glossary.md#notebook">notebook</a>', html, "the Goal's term is a plain link to the other glossary: no tooltip, so no chip")
        self.assertNotRegex(html, r'<a class="term" href="[^"]*other-glossary\.md#notebook"', "a term the page cannot explain is not drawn as a term chip")

    def test_render_deleted_text_keeps_the_old_files_citations(self):
        base = self.copy / "catalog/domains/workflow-stage.md"
        draft = self.copy / "package/proposed-product-specs/domains/workflow-stage.md"
        bt = base.read_text(); dt = draft.read_text()
        self.assertIn("### STAGE-03\n", bt)
        i = bt.index("### STAGE-03\n"); j = bt.index("\n\n", i)
        base.write_text(bt[:j] + " See [the review][r]." + bt[j:] + "\n[r]: ../old-review.md#x\n")
        draft.write_text(dt + "\n[r]: ../new-review.md#x\n")
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        card = re.search(r'id="stage-03".*?</details>', html, re.S).group(0)
        deleted = re.search(r'<del[^>]*>.*?the review.*?</del>', card, re.S)
        self.assertIsNotNone(deleted, "the dropped citation renders as deleted text")
        self.assertRegex(deleted.group(0), r'href="[^"]*catalog/old-review\.md#x"', "deleted text links where the old file linked, from the old file's folder")
        self.assertNotIn("new-review", deleted.group(0))

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


    def test_render_every_chip_has_a_tooltip_and_item_references_are_chips(self):
        for args, page in [(("--catalog", "catalog", "--drafts", "package/proposed-product-specs", "--authoring", "package/product-specs-authoring.md"), "package/product-specs-review.html"),
                           (("--catalog", "catalog", "--drafts", "package/change-requests/001/proposed-product-specs", "--authoring", "package/change-requests/001/product-specs-authoring.md"), "package/change-requests/001/product-specs-review.html")]:
            code, lines = run("render", *args, fixtures=self.copy)
            self.assertEqual(code, 0, lines)
            html = (self.copy / page).read_text()
            bare = re.findall(r'<(?:a|span) class="(?:ref|term)"(?![^>]*data-tip)[^>]*>[^<]*<', html)
            self.assertEqual(bare, [], f"{page}: every chip carries a tooltip; a reference the page cannot explain is a plain link or text")
        html = (self.copy / "package/product-specs-review.html").read_text()
        self.assertIn('under option A of <a class="ref" href="#d2" data-tip="tip-gap-own-d2">D2</a>', html, "a bare item reference in prose is the same chip as a footnote owner")
        self.assertIn('<a class="ref" href="#d1" data-tip="tip-gap-own-d1">D1</a>', html, "a linked item reference is the same chip")
        for tip in set(re.findall(r'data-tip="(tip-gap-[^"]+)"', html)):
            self.assertIn(f'<template id="{tip}">', html, f"every item chip's tooltip has its template ({tip})")


    def test_render_design_package_page(self):
        page = self.copy / "design-package/design-specs-review.html"
        page.unlink()
        code, lines = run("render", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "design-package/design-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        self.assertTrue(page.exists())
        html = page.read_text()
        bare = re.findall(r'<(?:a|span) class="(?:ref|term)"(?![^>]*data-tip)[^>]*>[^<]*<', html)
        self.assertEqual(bare, [], "design page: every chip carries a tooltip")

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
