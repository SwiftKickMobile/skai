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
                        'R7 has type "move requirement"', "R8 declares add but file", "R9 declares modify but file"]:
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

    def test_product_change_list_rejects_types_the_guide_does_not_allow(self):
        authoring = self.copy / "package/product-specs-authoring.md"
        entry = "- {} {}: [STAGE-09-07]\n  - **Justification** The rule changed; Supervisor input\n\n"
        authoring.write_text(authoring.read_text().replace("## Requirement Changes\n", "## Requirement Changes\n\n" + entry.format("R90", "add rule") + entry.format("R91", "retire rule"), 1))
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 1)
        found = issues(lines)
        self.assertEqual(len(found), 2, found)
        for line, kind in zip(found, ("add rule", "retire rule")):
            self.assertIn(f'has type "{kind}", which is not allowed', line)
            self.assertIn("add requirement, modify requirement", line)
            self.assertIn("a change to a rule goes under modify requirement on its parent", line)

    def test_design_change_list_rejects_types_the_guide_does_not_allow(self):
        authoring = self.copy / "design-package/design-specs-authoring.md"
        entry = "- S90 retire spec file: [List Screen][s-list]\n  - **Justification** The screen went away; Supervisor input\n\n"
        authoring.write_text(authoring.read_text().replace("## Spec Changes\n", "## Spec Changes\n\n" + entry, 1))
        code, lines = run("check-changes", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "design-package/design-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 1)
        found = issues(lines)
        self.assertEqual(len(found), 1, found)
        self.assertIn('S90 has type "retire spec file"', found[0])
        self.assertNotIn("modify requirement", found[0])

    def test_design_change_list_rejects_an_allowed_type_the_projection_contradicts(self):
        authoring = self.copy / "design-package/design-specs-authoring.md"
        authoring.write_text(authoring.read_text().replace(" modify item:", " move item:", 1).replace("- S4 add spec file:", "- S4 modify spec file:", 1))
        code, lines = run("check-changes", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                          "--authoring", "design-package/design-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 1)
        text = "\n".join(issues(lines))
        self.assertIn("declares move but", text)
        self.assertIn("S4 declares modify but file", text)

    def design_check(self):
        return run("check-changes", "--catalog", "design-catalog", "--drafts", "design-package/proposed-design-specs",
                   "--authoring", "design-package/design-specs-authoring.md", fixtures=self.copy)

    def test_design_change_list_takes_a_rule_change_riding_a_move(self):
        catalog = self.copy / "design-catalog/screens/notes.md"
        catalog.write_text(catalog.read_text().replace("with a prompt to write one.\n", "with a prompt to write one.\n\n- **01** The prompt opens a new note.\n", 1))
        draft = self.copy / "design-package/proposed-design-specs/screens/list-screen.md"
        draft.write_text(draft.read_text().replace(
            "A list's empty state reads `No notes yet` or `Trash is empty` with a prompt to write a note.\n",
            "The empty state reads `No notes yet` with a prompt to write one.\n\n- **01** The prompt opens a new note in the current list.\n", 1))
        authoring = self.copy / "design-package/design-specs-authoring.md"
        text = authoring.read_text().replace("- S8 modify item: [UI-NOTES-04]", "- S8 modify rule: [UI-NOTES-04-01]", 1)
        authoring.write_text(text.replace("[s-notes]: ", "[UI-NOTES-04-01]: proposed-design-specs/screens/list-screen.md#ui-notes-04\n[s-notes]: ", 1))
        code, lines = self.design_check()
        self.assertEqual(issues(lines), [], "a changed rule of a moved item takes its own modify rule entry, as Granularity says")
        self.assertEqual(code, 0, lines)

    def moved_item_with_parts(self, draft_body, entries):
        catalog = self.copy / "design-catalog/screens/notes.md"
        catalog.write_text(catalog.read_text().replace("with a prompt to write one.\n", "with a prompt to write one.\n\n- **01** The prompt opens a new note.\n\n> **Known difference — LumenNotes iOS:** the prompt is missing.\n", 1))
        draft = self.copy / "design-package/proposed-design-specs/screens/list-screen.md"
        draft.write_text(draft.read_text().replace(
            "A list's empty state reads `No notes yet` or `Trash is empty` with a prompt to write a note.\n",
            "The empty state reads `No notes yet` with a prompt to write one.\n\n" + draft_body, 1))
        authoring = self.copy / "design-package/design-specs-authoring.md"
        lines_ = "".join(f"- {cid} {kind}: [{ident}]\n  - **Justification** The empty state changed on the way; Design: the empty list\n  - **Touches** [list-screen][s-list]\n\n" for cid, kind, ident in entries)
        text = re.sub(r"- S8 modify item: \[UI-NOTES-04\]\n(  - .*\n)*\n?", lines_, authoring.read_text(), count=1)
        authoring.write_text(text.replace("[s-notes]: ", "[UI-NOTES-04-01]: proposed-design-specs/screens/list-screen.md#ui-notes-04\n[s-notes]: ", 1))
        return self.design_check()

    def test_design_change_list_takes_a_note_change_riding_a_move(self):
        code, lines = self.moved_item_with_parts(
            "- **01** The prompt opens a new note.\n\n> **Known difference — LumenNotes iOS:** the prompt shows only after a sync.\n",
            [("S8", "modify known-difference note", "UI-NOTES-04")])
        self.assertEqual(issues(lines), [], "a moved item's changed note takes its own entry, as Granularity says")

    def test_design_change_list_takes_a_rule_retirement_riding_a_move(self):
        code, lines = self.moved_item_with_parts(
            "- **01** (retired) Every list now opens its own composer.\n\n> **Known difference — LumenNotes iOS:** the prompt is missing.\n",
            [("S8", "retire rule", "UI-NOTES-04-01")])
        self.assertEqual(issues(lines), [], "a moved item's retired rule takes its own entry, as Granularity says")

    def test_design_change_list_still_needs_an_entry_for_a_moved_item_that_changed(self):
        code, lines = self.moved_item_with_parts(
            "- **01** The prompt opens a new note in the current list.\n\n> **Known difference — LumenNotes iOS:** the prompt is missing.\n", [])
        self.assertIn("rule UI-NOTES-04-01 of the moved item is modified and no change-list entry names it", "\n".join(issues(lines)))

    def test_design_change_list_needs_an_entry_per_changed_part_of_a_moved_item(self):
        body = "- **01** The prompt opens a new note in the current list.\n\n> **Known difference — LumenNotes iOS:** the prompt is missing.\n"
        code, lines = self.moved_item_with_parts(body.replace("new note", "new note", 1), [("S8", "modify item", "UI-NOTES-04")])
        self.assertIn("rule UI-NOTES-04-01 of the moved item is modified", "\n".join(issues(lines)), "modify item does not cover a changed rule")
        self.setUp()
        draft_body = "- **01** The prompt opens a new note.\n\n> **Known difference — LumenNotes iOS:** the prompt shows only after a sync.\n"
        code, lines = self.moved_item_with_parts(draft_body, [("S8", "modify rule", "UI-NOTES-04-01")])
        self.assertIn("also changed; a modify entry is needed", "\n".join(issues(lines)), "a rule entry does not cover the item's own change")

    def test_footnote_labels_renumbering_is_not_a_change(self):
        spec = importlib.util.spec_from_file_location("st", TOOL); st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
        self.assertTrue(st.same("Reminders expire after 30 days.[^2]", "Reminders expire after 30 days.[^1]"), "a renumbered marker is the same text")
        self.assertFalse(st.same("Reminders expire after 30 days.", "Reminders expire after 30 days.[^1]"), "a new marker is a change")

    def test_design_modify_spec_file_covers_its_own_intro_by_identity(self):
        draft = self.copy / "design-package/proposed-design-specs/screens/notes.md"
        draft.write_text(draft.read_text().replace("How a row reads.", "How a row reads, top to bottom.", 1))
        authoring = self.copy / "design-package/design-specs-authoring.md"
        entry = "- S13 modify spec file: [Notes Screen][s-notes]\n  - **Justification** The rows section now says its reading order; Catalog: the notes screen\n  - **Touches** [list-screen][s-list]\n\n"
        authoring.write_text(authoring.read_text().replace("## Decision Log\n", entry + "## Decision Log\n", 1))
        code, lines = self.design_check()
        self.assertEqual(issues(lines), [], "the entry names the file, so it covers that file's orientation line wherever its Touches point")

    def test_design_change_list_takes_a_note_on_a_new_item(self):
        draft = self.copy / "design-package/proposed-design-specs/screens/notes.md"
        item = ("### UI-NOTES-05\nThe list shows a sync badge while a sync runs.\n\n- **01** The badge clears when the sync ends.\n\n"
                "> **Known difference — LumenNotes iOS:** the badge never shows.\n\n")
        draft.write_text(draft.read_text().replace("[REMIND-04]: ", item + "[REMIND-04]: ", 1))
        authoring = self.copy / "design-package/design-specs-authoring.md"
        entries = "".join(f"- {cid} {kind}: [{ident}]\n  - **Justification** The list now shows sync progress; Design: the syncing list\n  - **Touches** [notes][s-notes]\n\n"
                          for cid, kind, ident in (("S10", "add item", "UI-NOTES-05"), ("S11", "add rule", "UI-NOTES-05-01"),
                                                   ("S12", "add known-difference note", "UI-NOTES-05")))
        text = authoring.read_text().replace("## Decision Log\n", entries + "## Decision Log\n", 1)
        defs = "[UI-NOTES-05]: proposed-design-specs/screens/notes.md#ui-notes-05\n[UI-NOTES-05-01]: proposed-design-specs/screens/notes.md#ui-notes-05\n"
        authoring.write_text(text.replace("[s-notes]: ", defs + "[s-notes]: ", 1))
        code, lines = self.design_check()
        self.assertEqual(issues(lines), [], "a new item's known-difference note takes an add entry, as Granularity says")
        self.assertEqual(code, 0, lines)

    def test_design_change_list_rejects_a_footnote_whose_linked_owner_closed(self):
        upstream = self.copy / "upstream/product-specs-authoring.md"
        upstream.parent.mkdir()
        upstream.write_text("# Upstream\n\n## Discussion\n\n### Expiry\n\n"
                            "- [x] D7 [Tradeoff] How long a reminder lasts\n  - **Decision** 30 days.\n\n"
                            "- [ ] D8 [Tradeoff] Whether badges count muted notes\n  - **Gap** Counted until support confirms.\n\n"
                            "## Decision Log\n\n- D7 decided — 30 days.\n- D8 gap — Counted until support confirms.\n")
        draft = self.copy / "design-package/proposed-design-specs/screens/notes.md"
        text = draft.read_text().replace("for those days, the weekday name within the last week, and `{Mon D}` otherwise.\n",
                                         "for those days, the weekday name within the last week, and `{Mon D}` otherwise.[^1]\n\n"
                                         "[^1]: **Gap:** [D7][up D7]. Placeholder: 30 days.\n", 1)
        text = text.replace("| 1 to 9 | The count |\n", "| 1 to 9 | The count[^1] |\n\n[^1]: **Gap:** [D8][up D8]. Placeholder: muted notes count.\n", 1)
        text += "[up D7]: ../../../upstream/product-specs-authoring.md#d7\n[up D8]: ../../../upstream/product-specs-authoring.md#d8\n"
        draft.write_text(text)
        code, lines = self.design_check()
        found = "\n".join(issues(lines))
        self.assertIn("gap footnote [^1] links D7, which is not an open gap there", found, "a marker outlives its owner's closing")
        self.assertNotIn("links D8", found, "a marker whose linked owner is still an open gap passes")

    def test_design_change_list_takes_an_intro_change_alone_under_modify_spec_file(self):
        draft = self.copy / "design-package/proposed-design-specs/screens/notes.md"
        draft.write_text(draft.read_text().replace("How a row reads.", "How a row reads, top to bottom.", 1))
        authoring = self.copy / "design-package/design-specs-authoring.md"
        entry = "- S13 modify spec file: [Notes Screen][s-notes]\n  - **Justification** The rows section now says its reading order; Catalog: the notes screen\n  - **Touches** [notes][s-notes]\n\n"
        authoring.write_text(authoring.read_text().replace("## Decision Log\n", entry + "## Decision Log\n", 1))
        code, lines = self.design_check()
        self.assertEqual(issues(lines), [], "a section orientation line rides on modify spec file, as the artifacts guide says")

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
        assets = re.findall(r'<link rel="stylesheet" href="([^"]+)">|<script src="([^"]+)"></script>', html)
        assets = [a or b for a, b in assets]
        self.assertEqual([Path(a).name for a in assets], ["skai-pages.v1.css", "spec-review.v2.css", "skai-pages.v1.js", "spec-review.v2.js"],
                         "the shared page library, then the review pages' own stylesheet and script")
        for href in assets:
            self.assertFalse(href.startswith("/") or "://" in href, "assets are linked by a relative path: " + href)
            self.assertTrue(Path(os.path.normpath(page.parent / urllib.parse.unquote(href))).is_file(), href)
        self.assertNotIn("Archivo", html)
        self.assertIn("<title>Product Specs package</title>", html, "the title is the document type, then the package's ID")
        self.assertIn('<div class="top"><h1 class="title">Product Specs <span class="pkg">package</span></h1>', html, "one line: the type in ink, the ID in cyan")
        self.assertNotIn("Change Package", html)
        summary = re.search(r'<div class="item request"><div class="head">(.*?)</div>', html).group(1)
        self.assertRegex(summary, r'^<span class="status pill">[^<]+</span>$', "the summary box shows the state and goal, no title line")
        self.assertIn('<div id="pop" class="popover">', html, "the popover is the shared one")
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
        self.assertIn('<span class="status pill">no discussion items</span>', html)
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
        authoring.write_text(authoring.read_text().replace("[D1]: #stage-definitions", "[D1]: ../changes/CR-01/package/product-specs-authoring.md#stage-definitions", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        self.assertIn('<h3 class="section" id="stage-definitions">', html, "the page has a same-named local topic")
        card = re.search(r'id="stage-01".*?<div class="why"><b>Why</b> (.*?)</div>', html, re.S)
        self.assertIsNotNone(card)
        self.assertRegex(card.group(1), r'href="[^"]*changes/CR-01/package/product-specs-authoring\.md#stage-definitions"', "a citation into another artifact is not shortened to the same-named local anchor")

    def test_render_id_reference_defined_in_another_artifact_keeps_that_artifact(self):
        authoring = self.copy / "package/product-specs-authoring.md"
        text = authoring.read_text()
        self.assertIn("[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01", text)
        authoring.write_text(text.replace("[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01", "[STAGE-01]: ../changes/CR-01/package/proposed-product-specs/domains/workflow-stage.md#stage-01", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        d1 = re.search(r'<details class="item request discussion[^"]*" id="d1".*?</details>', html, re.S)
        self.assertIsNotNone(d1)
        self.assertRegex(d1.group(0), r'href="[^"]*changes/CR-01/package/proposed-product-specs/domains/workflow-stage\.md#stage-01"', "an ID reference the artifact defines in another document keeps that document, though the page has an item of that ID")

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
        self.assertRegex(tip.group(0), r'href="[^"]*changes/CR-01/package/product-specs-authoring\.md"', "a reference-style citation in the owning item keeps its link in the tooltip, resolved by the artifact's own definitions")

    def test_request_base_walks_up_the_chain_then_to_production(self):
        spec = importlib.util.spec_from_file_location("st", TOOL); st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
        change = self.copy / "offers"
        nested = change / "changes/CR-01/changes/CR-01-01/product-specs"
        for d in (change / "product-specs", change / "changes/CR-01/product-specs", change / "changes/CR-01/design", nested, change / "changes/CR-01/changes/CR-01-01/design-specs"):
            d.mkdir(parents=True, exist_ok=True)
            (d / "a-authoring.md").write_text("# A\n")
        self.assertEqual(st.chain_bases(nested), [change / "changes/CR-01/product-specs", change / "product-specs"], "the parent request's sub-package first, then the change's own")
        self.assertEqual(st.base_authoring(nested / "a-authoring.md", ""), (change / "changes/CR-01/product-specs/a-authoring.md").resolve())
        self.assertEqual(st.package_id(nested / "proposed-product-specs"), "offers | CR-01 | CR-01-01")
        self.assertEqual(st.chain_bases(change / "changes/CR-01/changes/CR-01-01/design"), [change / "changes/CR-01/design"])
        self.assertEqual(st.chain_bases(change / "changes/CR-01/changes/CR-01-01/design-specs"), [], "no package of its type up the chain: production")
        self.assertIsNone(st.base_authoring(change / "changes/CR-01/changes/CR-01-01/design-specs/a-authoring.md", ""))
        shutil.rmtree(change / "changes/CR-01/product-specs")
        self.assertEqual(st.chain_bases(nested), [change / "product-specs"], "a parent request without the type passes to the change's own package")
        self.assertIsNone(st.request_folder(self.copy / "skai/changes/CR-01/product-specs"), "a change named like a request is never read as one")
        promoted = change / "promoted/CR-02/product-specs"
        promoted.mkdir(parents=True)
        (promoted / "a-authoring.md").write_text("# A\n")
        self.assertEqual([rid for rid, _ in st.request_subpackages(change / "product-specs/a-authoring.md", "promoted")], ["CR-02"])
        self.assertEqual([rid for rid, _ in st.request_subpackages(change / "product-specs/a-authoring.md", "changes")], ["CR-01-01"], "open sub-packages of the type at any depth")

    def test_target_identity_qualifies_headings_by_document_but_not_item_ids(self):
        spec = importlib.util.spec_from_file_location("st", TOOL); st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
        self.assertEqual(st.target_identity("../a.md#stage-01"), st.target_identity("../b.md#stage-01"), "a spec item's ID is the same item wherever its file sits")
        self.assertNotEqual(st.target_identity("../first-review.md#decision"), st.target_identity("../second-review.md#decision"), "a heading belongs to its document")

    def test_render_same_id_in_another_document_gets_its_own_tooltip(self):
        authoring = self.copy / "package/product-specs-authoring.md"
        authoring.write_text(authoring.read_text().replace("[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01", "[STAGE-01]: ../changes/CR-01/package/proposed-product-specs/domains/workflow-stage.md#stage-01", 1))
        page = self.copy / "package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs",
                          "--authoring", "package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text()
        d1 = re.search(r'<details class="item request discussion[^"]*" id="d1".*?</details>', html, re.S).group(0)
        link = re.search(r'<a class="ref" href="[^"]*changes/CR-01/package/[^"]*#stage-01"([^>]*)>STAGE-01</a>', d1)
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
        for href in re.findall(r'(?:href|src)="([^"]*(?:skai-pages\.v1|spec-review\.v2)\.(?:css|js))"', text):
            self.assertTrue(Path(os.path.normpath(page.parent / urllib.parse.unquote(href))).is_file(), "assets resolve from an --out elsewhere: " + href)
        end = text.find("Moved from glossary.md")
        self.assertGreater(end, 0, "the moved entry names its old home")
        card = text[text.rfind('id="offer" open>', 0, end):end]
        self.assertIn('<blockquote class="mod"><b>Also called:</b>', card)
        self.assertIn("pitch (the web app).</ins>", card)
        self.assertNotIn("<del", card.split("<blockquote")[0], "the unchanged definition is not marked")


    def test_render_every_chip_has_a_tooltip_and_item_references_are_chips(self):
        for args, page in [(("--catalog", "catalog", "--drafts", "package/proposed-product-specs", "--authoring", "package/product-specs-authoring.md"), "package/product-specs-review.html"),
                           (("--catalog", "catalog", "--drafts", "changes/CR-01/package/proposed-product-specs", "--authoring", "changes/CR-01/package/product-specs-authoring.md"), "changes/CR-01/package/product-specs-review.html")]:
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
        self.assertIn("<title>Design Specs design-package</title>", html, "design-spec drafts are titled Design Specs")
        self.assertIn('<h1 class="title">Design Specs <span class="pkg">design-package</span></h1>', html)

    def test_request_package_renders_and_checks_against_its_base(self):
        drafts = "changes/CR-01/package/proposed-product-specs"
        page = self.copy / "changes/CR-01/package/product-specs-review.html"
        code, lines = run("render", "--catalog", "catalog", "--drafts", drafts, fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        html = page.read_text(encoding="utf-8")
        self.assertIn("<title>Product Specs package | CR-01</title>", html)  # the document type, the base's id, then the request's number
        self.assertIn('<h1 class="title">Product Specs <span class="pkg">package<span class="sep">|</span>CR-01</span></h1>', html)
        self.assertIn("tip-gap-base-d3", html)  # a footnote naming the base's item resolves to it
        self.assertTrue(any("'gaps': 1" in ln for ln in lines), lines)
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", drafts,
                          "--authoring", "changes/CR-01/package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        code, lines = run("validate", "catalog", drafts, fixtures=self.copy)  # the base's drafts come in between on their own
        self.assertEqual(code, 0, lines)
        self.assertEqual(issues(lines), [], lines)

    def test_request_deciding_a_base_item_shows_on_the_base_and_needs_it_open(self):
        request = self.copy / "changes/CR-01/package/product-specs-authoring.md"
        request.write_text(request.read_text().replace("## Decision Log\n", "## Decision Log\n\n- [D2][base D2] decided — Option A: a missing date keeps it active.\n", 1)
                           + "[base D2]: ../../../package/product-specs-authoring.md#d2\n[base D1]: ../../../package/product-specs-authoring.md#d1\n")
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", "changes/CR-01/package/proposed-product-specs",
                          "--authoring", "changes/CR-01/package/product-specs-authoring.md", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        d2 = re.search(r'<details[^>]* id="d2" open>.*?</details>', (self.copy / "package/product-specs-review.html").read_text(), re.S)
        self.assertIn('Decided in request <a href="../changes/CR-01/package/product-specs-review.html">CR-01</a>', d2.group(0), "the base item stays open and shows the request's pending decision")
        request.write_text(request.read_text().replace("- [D2][base D2] decided", "- [D1][base D1] decided", 1))
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", "changes/CR-01/package/proposed-product-specs",
                          "--authoring", "changes/CR-01/package/product-specs-authoring.md", fixtures=self.copy)
        self.assertTrue(any("[D1][base D1] is decided but ../../../package/product-specs-authoring.md has no open item D1" in ln for ln in issues(lines)), lines)
        request.write_text(request.read_text().replace("- [D1][base D1] decided", "- base D3 decided", 1))  # the older form still reads
        code, lines = run("check-changes", "--catalog", "catalog", "--drafts", "changes/CR-01/package/proposed-product-specs",
                          "--authoring", "changes/CR-01/package/product-specs-authoring.md", fixtures=self.copy)
        self.assertTrue(any("still marks base D3, which this request decides" in ln for ln in issues(lines)), lines)  # the base's footnotes and the request's own

    def test_open_items_stay_in_a_promoted_request_and_a_footnote_links_them(self):
        promoted = self.copy / "promoted/CR-02/package"
        promoted.mkdir(parents=True)
        (promoted / "product-specs-authoring.md").write_text(
            "# Product Specs Authoring — Reminder Sound\n\n## Goal\n\nPick the reminder sound.\n\n## Discussion\n\n"
            "- [ ] D5 [Proposal] Which sound a reminder plays\n  - **Concern** It follows D6 and base D1.\n  - **Gap** The default chime stands in until the sound team picks one.\n"
            "- [x] D6 [Proposal] Reminders play a sound\n  - **Decision** They do.\n\n"
            "## Decision Log\n\n- D6 decided — They do.\n- D5 gap — The default chime stands in.\n")
        spec = self.copy / "package/proposed-product-specs/domains/suggestion.md"
        text = spec.read_text().replace("validity ends[^1] |", "validity ends[^1][^2] |", 1)
        text = text.replace("Expiration arrives.\n", "Expiration arrives.\n[^2]: **Gap:** [D5][CR-02 D5]. Placeholder: the default chime.\n", 1)
        spec.write_text(text + "[CR-02 D5]: ../../../promoted/CR-02/package/product-specs-authoring.md#d5\n")
        args = ("--catalog", "catalog", "--drafts", "package/proposed-product-specs", "--authoring", "package/product-specs-authoring.md")
        code, lines = run("check-changes", *args, fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        code, lines = run("validate", "catalog", "package/proposed-product-specs", fixtures=self.copy)
        self.assertEqual(issues(lines), [], "a footnote linking another package's item, beside another footnote, validates")
        code, lines = run("render", "--catalog", "catalog", "--drafts", "package/proposed-product-specs", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        page = (self.copy / "package/product-specs-review.html").read_text()
        self.assertIn('Open in promoted request <a href="../promoted/CR-02/package/product-specs-review.html">CR-02</a>', page)
        self.assertIn('id="rcr-02-d5"', page, "the promoted request's open item shows under its own anchor")
        d5 = re.search(r'<details[^>]* id="rcr-02-d5".*?</details>', page, re.S).group(0)
        self.assertRegex(d5, r'href="\.\./promoted/CR-02/package/product-specs-review\.html#d6"', "its own items are the request's, not the page's")
        self.assertRegex(d5, r'<a class="ref" href="#d1" data-tip="tip-gap-own-d1">base D1</a>', "its base is this package")
        self.assertRegex(page, r'<a class="ref" href="\.\./promoted/CR-02/package/product-specs-review\.html#d5" data-tip="(tip-gap-linked-\d+-d5)">D5</a>')
        self.assertIn('<template id="tip-gap-linked-', page, "the linked owner gets its tooltip")
        self.assertTrue(any("'gaps': 3" in ln for ln in lines), lines)  # the base's gap item, its footnoted requirement and the promoted request's gap item
        spec.write_text(spec.read_text().replace("[D5][CR-02 D5]", "[D7][CR-02 D5]", 1))
        code, lines = run("check-changes", *args, fixtures=self.copy)
        self.assertTrue(any("links D7, which its target does not hold" in ln for ln in issues(lines)), lines)

    def test_a_link_named_with_a_scope_word_reaches_its_definition(self):
        promoted = self.copy / "promoted/CR-09/package"
        promoted.mkdir(parents=True)
        (promoted / "product-specs-authoring.md").write_text(
            "# Product Specs Authoring — Snooze\n\n## Goal\n\nSnooze.\n\n## Discussion\n\n"
            "- [ ] D3 [Question] How long a snooze lasts\n\n## Decision Log\n")
        request = self.copy / "changes/CR-01/package/product-specs-authoring.md"
        request.write_text(request.read_text().replace("the open question base D3", "the open question [D3][base D3]", 1)
                           + "[base D3]: ../../../promoted/CR-09/package/product-specs-authoring.md#d3\n")
        code, lines = run("render", "--catalog", "catalog", "--drafts", "changes/CR-01/package/proposed-product-specs", fixtures=self.copy)
        self.assertEqual(code, 0, lines)
        page = (self.copy / "changes/CR-01/package/product-specs-review.html").read_text()
        self.assertRegex(page, r'<a class="ref" href="\.\./\.\./\.\./promoted/CR-09/package/product-specs-review\.html#d3"[^>]*>D3</a>',
                         "the definition decides, though the package this request sits under has its own D3")

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


# ---------------------------------------------------------------- render matrix (skai#102)
#
# What the review page compares × the case (added, modified, removed, moved where the guides allow
# a move) × where a citation's link definition lives (the draft, the base, the authoring artifact,
# a document outside the projection). Each cell builds a small catalog and change package in a
# temporary folder, checks that the package is valid (validate, check-changes), renders it and
# asserts the three things the page promises: the difference shows; its reason shows and is the
# right entry's; its citations resolve where the author's definitions point. Product cells run in
# both flavors (the change types differ); moves are design-only, as the guides allow them only there.

_ST_SPEC = importlib.util.spec_from_file_location("spec_tool_matrix", TOOL)
ST = importlib.util.module_from_spec(_ST_SPEC); _ST_SPEC.loader.exec_module(ST)
anchor, ID_RE = ST.anchor, ST.ID_RE  # the tool's own anchors and IDs

MATRIX_BASE = {
    "{f}/_{f}.md": ("# Index\n\nWhat each file answers.\n\n"
                    "- [alpha] -- `{P}ALPHA-` -- What the alpha board holds\n"
                    "- [beta] -- `{P}BETA-` -- What the beta board holds\n\n"
                    "[alpha]: alpha.md\n[beta]: beta.md\n"),
    "{f}/alpha.md": ("# Alpha\n\nThe alpha board in brief.\n\n## Basics\n\nHow the basics read.\n\n"
                     "### {P}ALPHA-01\nThe alpha board lists its cards in order.\n\n"
                     "- **01** A new card goes to the bottom.\n\n  | Kind | Place |\n  | --- | --- |\n  | Plain | bottom |\n  | Pinned | top |\n\n"
                     "- **02** A done card greys out.\n\n"
                     "### {P}ALPHA-02\nThe alpha board shows a title.\n\n"
                     "### {P}ALPHA-03\nThe alpha board can be archived.\n\n"
                     "## Extras\n\nHow the extras read.\n\n"
                     "### {P}ALPHA-04\nThe alpha board shows a count.\n"),
    "{f}/beta.md": "# Beta\n\nThe beta board in brief.\n\n### {P}BETA-01\nThe beta board lists its lanes.\n",
    "glossary.md": ("# Glossary\n\nTerms the specs use.\n\n"
                    "### Board lane\nA column the alpha board draws ([{P}ALPHA-01]).\n\n"
                    "### Card stack\nA pile of cards the alpha board keeps ([{P}ALPHA-02]).\n\n"
                    "[{P}ALPHA-01]: {f}/alpha.md#{a}alpha-01\n[{P}ALPHA-02]: {f}/alpha.md#{a}alpha-02\n"),
}
NEW_TEXT = "Freshly written, per [the memo][memo] and [EXT-01]."  # the draft's words: memo defined in the draft, EXT-01 outside the projection
OLD_TEXT = "Formerly written, per [the memo][memo]."  # the base's words: memo defined in the base, to another document
NEW_MEMO, OLD_MEMO, BRIEF = "../ref/new-memo.md#point", "../ref/old-memo.md#point", "../ref/brief.md#point"  # as the page (in pkg/) links them
EXT_ITEM, EXT_CITE = "../shared/ext.md#ext-01", "../shared/charter.md#rule"


class MatrixPackage:
    """A small catalog and change package for one cell: root/catalog, root/pkg (drafts, authoring
    artifact, page), root/ref (documents the specs cite) and root/shared (a spec document outside
    the projection, whose item EXT-01 cites its own neighbour)."""

    def __init__(self, root, design):
        self.root, self.design = Path(root), design
        self.P, self.a, self.f = ("UI-", "ui-", "screens") if design else ("", "", "domains")
        self.catalog, self.pkg = self.root / "catalog", self.root / "pkg"
        self.drafts = self.pkg / ("proposed-design-specs" if design else "proposed-product-specs")
        self.authoring = self.pkg / ("design-specs-authoring.md" if design else "product-specs-authoring.md")
        self.page = self.pkg / ("design-specs-review.html" if design else "product-specs-review.html")
        self.base = {self.t(k): self.t(v) for k, v in MATRIX_BASE.items()}
        self.pristine = dict(self.base)  # a draft starts from the catalog file as the cell found it
        self.drafted, self.entries, self.defs = {}, [], {}
        for name in ("new-memo", "old-memo", "brief"):
            self.write(self.root / f"ref/{name}.md", "# Memo\n\n## Point\n\nWhat the memo says.\n")
        self.write(self.root / "shared/ext.md", "# Shared\n\n### EXT-01\nThe shared board rule, per [the charter][charter].\n\n[charter]: charter.md#rule\n")
        self.write(self.root / "shared/charter.md", "# Charter\n\n## Rule\n\nThe charter's rule.\n")

    def t(self, s):
        return s.replace("{P}", self.P).replace("{a}", self.a).replace("{f}", self.f)

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    # --- files
    def draft(self, rel):
        rel = self.t(rel)
        self.drafted.setdefault(rel, self.pristine.get(rel, ""))
        return rel

    def add_base(self, rel, text):
        self.base[self.t(rel)] = self.pristine[self.t(rel)] = self.t(text)

    def sub(self, rel, old, new, base=False):
        """Replace once in the draft (drafting the file) or, with `base`, in the catalog file."""
        files = self.base if base else self.drafted
        rel = self.t(rel) if base else self.draft(rel)
        old, new = self.t(old), self.t(new)
        assert files[rel].count(old) == 1, (rel, old)
        files[rel] = files[rel].replace(old, new, 1)

    def define(self, rel, name, target, base=False):
        files = self.base if base else self.drafted
        rel = self.t(rel) if base else self.draft(rel)
        text = files[rel].rstrip("\n")
        files[rel] = text + ("\n" if LINKDEF_LINE.match(text.rsplit("\n", 1)[-1]) else "\n\n") + f"[{self.t(name)}]: {self.t(target)}\n"

    def up(self, rel, base):
        return "../" * ((1 if base else 2) + self.t(rel).count("/"))

    def new_defs(self, rel):
        """The draft's definitions for NEW_TEXT."""
        self.define(rel, "memo", self.up(rel, False) + "ref/new-memo.md#point")
        self.define(rel, "EXT-01", self.up(rel, False) + "shared/ext.md#ext-01")

    def old_defs(self, rel):
        """The base's definition for OLD_TEXT."""
        self.define(rel, "memo", self.up(rel, True) + "ref/old-memo.md#point", base=True)

    # --- change list
    def ident_item(self, iid, file="alpha", retired=False):
        iid = self.t(iid)
        self.defs[iid] = f"{self.drafts.name}/{self.f}/{file}.md#{anchor(re.match(ID_RE, iid).group(0))}" + ("-retired" if retired else "")
        return f"[{iid}]"

    def ident_file(self, rel):
        rel = self.t(rel)
        if not self.design:
            return rel
        name = "s-" + anchor(rel)
        self.defs[name] = f"{self.drafts.name}/{rel}"
        return f"[{Path(rel).stem}][{name}]"

    def ident_term(self, term, rel="glossary.md"):
        return f"[{term}][{self.ident_file(rel)[1:-1].split('][')[1]}]" if self.design else term

    def entry(self, kind, identity, touches=(), arrow=False):
        """An entry with a unique reason tag citing [the brief][brief]; returns the tag."""
        cid = f"{'S' if self.design else 'R'}{len(self.entries) + 1}"
        tag = f"why-{cid}-end"
        sep = " → " if arrow else ", "
        lines = [f"- {cid} {kind}: {identity}", f"  - **Justification** The cell needs this change {tag}, per [the brief][brief]; Supervisor input"]
        if touches:
            lines.append("  - **Touches** " + sep.join(self.ident_file(r) for r in touches))
        self.entries.append(("\n".join(lines), tag))
        return tag

    def item_entry(self, op, iid, file="alpha", retired=False):
        kind = f"{op} item" if self.design else f"{op} requirement"
        return self.entry(kind, self.ident_item(iid, file, retired), [f"{{f}}/{file}.md"])

    def rule_entry(self, op, rid):
        """Design specs list a changed rule; product specs put it under modify requirement on its parent."""
        if self.design:
            return self.entry(f"{op} rule", self.ident_item(rid), ["{f}/alpha.md"])
        return self.item_entry("modify", rid.rsplit("-", 1)[0])

    def term_entry(self, op, term, rel="glossary.md"):
        return self.entry(f"{op} glossary entry", self.ident_term(term, rel), [rel])

    def carrier(self, *rels):
        """A change to BETA-01 whose Touches also name `rels`: the entry covering their prose."""
        self.sub("{f}/beta.md", "lists its lanes.", "lists its lanes left to right.")
        return self.entry("modify item" if self.design else "modify requirement", self.ident_item("{P}BETA-01", "beta"), ["{f}/beta.md", *rels])

    def tags(self):
        return [tag for _, tag in self.entries]

    # --- run
    def build(self):
        for rel, text in self.base.items():
            self.write(self.catalog / rel, text)
        for rel, text in self.drafted.items():
            self.write(self.drafts / rel, text)
        heading = "## Spec Changes" if self.design else "## Requirement Changes"
        defs = "".join(f"[{k}]: {v}\n" for k, v in {"brief": "../ref/brief.md#point", **self.defs}.items())
        self.write(self.authoring, f"# Matrix Cell\n\n## Goal\n\nExercise one cell of the review page.\n\n## Discussion\n\n"
                                   f"Nothing is open; the brief settles every change.\n\n{heading}\n\n"
                                   + "\n\n".join(e for e, _ in self.entries) + f"\n\n{defs}")

    def tool(self, command, *args):
        result = subprocess.run([sys.executable, str(TOOL), command, *map(str, args)], capture_output=True, text=True)
        return result.returncode, (result.stdout + result.stderr).splitlines()

    def unlisted(self):
        """What check-changes requires an entry for: its reports against this package with an empty
        change list, as (file, what, name, status)."""
        kept, self.entries = self.entries, []
        self.build()
        code, lines = self.tool("check-changes", "--catalog", self.catalog, "--drafts", self.drafts, "--authoring", self.authoring)
        self.entries = kept
        self.build()
        whats = ("glossary entry", "section line", "index line", "intro", "title", "item", "rule", "file")
        out = set()
        for line in lines:
            m = re.match(rf"^{re.escape(str(self.root))}/(?:catalog|pkg/{self.drafts.name})/(.+?):\d+: (.+) is (\w+) but no change-list entry names it$", line)
            if m:
                what = next(w for w in whats if m.group(2) == w or m.group(2).startswith(w + " "))
                out.add((m.group(1), what, m.group(2)[len(what) + 1:] or what, m.group(3)))
        return out

    def render(self):
        self.build()
        common = ("--catalog", self.catalog, "--drafts", self.drafts)
        code, lines = self.tool("validate", self.catalog, self.drafts)
        self.validate_issues = issues([l.replace(f"{self.root}/", "") for l in lines])
        code, lines = self.tool("check-changes", *common, "--authoring", self.authoring)
        self.check_issues = [l.replace(f"{self.root}/", "") for l in lines if l != "0 issues"]
        code, lines = self.tool("render", *common, "--authoring", self.authoring)
        assert code == 0, lines
        self.html = self.page.read_text(encoding="utf-8")
        return self.html


LINKDEF_LINE = re.compile(r"^\[[^\]]+\]:\s")


def section_of(html, rel):
    """A file's section on the page."""
    m = re.search(rf'<section class="file" data-kind="(\w+)"><h2 id="file-{re.escape(anchor(rel))}">.*?</section>', html, re.S)
    return m.group(0) if m else None


def card_of(html, aid):
    m = re.search(rf'<details class="item [^"]*" id="{re.escape(aid)}"[^>]*>.*?</details>', html, re.S)
    return m.group(0) if m else None


def prose_of(html, word):
    cards = [m.group(0) for m in re.finditer(r'<div class="item prose modified"><p class="intro modified">.*?</p>(?:<div class="why">.*?</div>)?</div>', html, re.S) if word in m.group(0)]
    return cards[0] if len(cards) == 1 else None


def index_card_of(html, name):
    m = re.search(rf'<details class="item [^"]*"(?: open)?><summary><span class="badge">[^<]*</span><span class="id">{re.escape(name)}</span></summary>.*?</details>', html, re.S)
    return m.group(0) if m else None


def rule_of(card, rid):
    """A rule's own line in an item card: its class and its text up to its tables or child rules."""
    m = re.search(rf'<li class="([^"]*)" data-rid="{re.escape(rid)}">(.*?)(?=<table|<ul|</li>)', card or "", re.S)
    return (m.group(1), m.group(2)) if m else (None, None)


class RenderMatrix(unittest.TestCase):
    """One test per cell: test_<row>__<case>__<flavor>."""

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.directory.cleanup()

    def package(self, design):
        return MatrixPackage(self.directory.name, design)

    # --- the three promises
    def valid(self, m):
        self.assertEqual(m.validate_issues, [], "the cell's package validates")
        self.assertEqual(m.check_issues, [], "the cell's change list matches its projection")
        self.page_agrees_with_check(m)
        for root in {str(m.root), str(m.root.resolve())}:  # a committed page reads the same on every machine
            for form in (root, anchor(root)):
                self.assertNotIn(form, m.html, "the page holds no absolute filesystem path, written out or folded into an anchor")

    def page_agrees_with_check(self, m):
        """The differences the page shows are the ones check-changes requires entries for: each
        mark on the page (one per difference, where it shows it), folded to the unit an entry is
        written for (an added file's contents ride on the file; a product rule on its requirement),
        equals check-changes' reports against the same package with an empty change list."""
        shown = set()
        for kind, rel, body in re.findall(r'<section class="file" data-kind="(\w+)"><h2 id="[^"]*"><span class="badge \w+">\w+</span> ([^<]+)</h2>(.*?)</section>', m.html, re.S):
            rel = html_mod.unescape(rel)
            if kind == "added":
                shown.add((rel, "file", rel, "added"))
                continue
            for mark in re.findall(r"<!-- diff: (.*?) -->", body):
                what, name, status = html_mod.unescape(mark).split("|")
                if what == "rule" and not m.design:
                    continue
                shown.add((rel, what, name, status))
        self.assertEqual(shown, m.unlisted(), "the page shows exactly the differences check-changes requires entries for")

    def shows(self, frag, how, word=None):
        self.assertIsNotNone(frag, "the difference is on the page")
        if how == "inserted":
            self.assertTrue(any(word in s for s in re.findall(r'<ins class="w">(.*?)</ins>', frag, re.S)), f"{word!r} shows as inserted")
        elif how == "deleted":
            self.assertTrue(any(word in s for s in re.findall(r"<del[^>]*>(.*?)</del>", frag, re.S)), f"{word!r} shows as deleted")
        elif how == "unmarked":
            self.assertNotRegex(frag, r"<ins|<del", "nothing is marked")

    def reason(self, frag, m, *tags):
        """The expected entries' reasons show, no other entry's does, and the reason's citation
        resolves through the authoring artifact's definitions."""
        self.assertIsNotNone(frag)
        for tag in tags:
            self.assertIn(tag, frag, f"the reason of {tag} shows")
        for tag in m.tags():
            if tag not in tags:
                self.assertNotIn(tag, frag, f"{tag} is another entry's reason")
        if tags:
            self.assertIn(f'href="{BRIEF}"', frag, "the reason's citation resolves where the authoring artifact defines it")

    def cites(self, frag, html, new=False, old=False, inside=None):
        """NEW_TEXT's citations resolve through the draft's definitions (EXT-01 to the outside
        document, its popover through that document's own); OLD_TEXT's through the base's."""
        self.assertIsNotNone(frag)
        pick = lambda tag: "".join(re.findall(rf"<{tag}[^>]*>(.*?)</{tag}>", frag, re.S)) if inside else frag
        if new:
            scope = pick("ins") if inside else frag
            self.assertIn(f'href="{NEW_MEMO}"', scope, "an added citation resolves where the draft defines it")
            ext = re.search(rf'<a class="ref" href="{re.escape(EXT_ITEM)}" data-tip="([^"]+)"', scope)
            self.assertIsNotNone(ext, "a citation of an outside document's item links there with a tooltip")
            tip = re.search(rf'<template id="{re.escape(ext.group(1))}">.*?</template>', html, re.S)
            self.assertIsNotNone(tip, "the outside item's popover exists")
            self.assertIn(f'href="{EXT_CITE}"', tip.group(0), "the outside item's own citation resolves where that document defines it")
        if old:
            scope = pick("del") if inside else frag
            self.assertIn(f'href="{OLD_MEMO}"', scope, "a deleted citation resolves where the base defines it")
            self.assertNotIn(f'href="{NEW_MEMO}"', pick("del"), "never where the draft defines the same name")


def matrix_cell(row, case, flavors=("product", "design")):
    def wrap(fn):
        for flavor in flavors:
            def test(self, fn=fn, flavor=flavor):
                fn(self, self.package(flavor == "design"))
            test.__doc__ = f"{row} | {case} | {flavor}"
            setattr(RenderMatrix, f"test_{row}__{case}__{flavor}", test)
        return fn
    return wrap


def matrix_skip(row, case, why, flavors=("product", "design")):
    for flavor in flavors:
        def test(self):
            self.skipTest(why)
        test.__doc__ = f"{row} | {case} | {flavor}"
        setattr(RenderMatrix, f"test_{row}__{case}__{flavor}", test)


# --- file intro

@matrix_cell("intro", "added")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board in brief.\n\n", "", base=True)
    m.sub("{f}/alpha.md", "The alpha board in brief.", NEW_TEXT); m.new_defs("{f}/alpha.md")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.reason(frag, m, tag); self.cites(frag, html, new=True, inside=True)


@matrix_cell("intro", "modified")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board in brief.", "The alpha board in brief. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "The alpha board in brief.", "The alpha board in brief. " + NEW_TEXT); m.new_defs("{f}/alpha.md")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, new=True, old=True, inside=True)


@matrix_cell("intro", "removed")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board in brief.", "The alpha board in brief. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "The alpha board in brief.\n\n", "")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Formerly")
    self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag); self.cites(frag, html, old=True, inside=True)


@matrix_cell("intro", "modified-by-spec-file-entry", flavors=("design",))
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board in brief.", "The alpha board in brief, top to bottom.")
    tag = m.entry("modify spec file", m.ident_file("{f}/alpha.md"))  # no Touches: the entry names the file, so it is the intro's entry
    html = m.render(); self.valid(m)
    frag = prose_of(html, "top to bottom")
    self.shows(frag, "inserted", "bottom"); self.reason(frag, m, tag)


# --- section orientation text

@matrix_cell("section", "added-with-new-section")
def _(self, m):
    m.sub("{f}/alpha.md", "### {P}ALPHA-04\nThe alpha board shows a count.\n",
          "### {P}ALPHA-04\nThe alpha board shows a count.\n\n## Later\n\n" + NEW_TEXT + "\n\n### {P}ALPHA-05\nThe alpha board shows a footer.\n")
    m.new_defs("{f}/alpha.md")
    tag = m.item_entry("add", "{P}ALPHA-05")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.reason(frag, m, tag); self.cites(frag, html, new=True, inside=True)


@matrix_cell("section", "added-itemless-section")
def _(self, m):
    m.sub("{f}/alpha.md", "## Extras\n", "## Later\n\n" + NEW_TEXT + "\n\n## Extras\n"); m.new_defs("{f}/alpha.md")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.reason(frag, m, tag); self.cites(frag, html, new=True, inside=True)


@matrix_cell("section", "added-to-existing-section")
def _(self, m):
    m.sub("{f}/alpha.md", "How the basics read.\n\n", "", base=True)
    m.sub("{f}/alpha.md", "How the basics read.", NEW_TEXT); m.new_defs("{f}/alpha.md")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.reason(frag, m, tag); self.cites(frag, html, new=True, inside=True)


@matrix_cell("section", "modified")
def _(self, m):
    m.sub("{f}/alpha.md", "How the basics read.", "How the basics read. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "How the basics read.", "How the basics read. " + NEW_TEXT); m.new_defs("{f}/alpha.md")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, new=True, old=True, inside=True)


@matrix_cell("section", "modified-by-spec-file-entry", flavors=("design",))
def _(self, m):
    m.sub("{f}/alpha.md", "How the basics read.", "How the basics read, top to bottom.")
    m.sub("{f}/alpha.md", "The alpha board shows a title.", "The alpha board shows a short title.")
    tag = m.entry("modify spec file", m.ident_file("{f}/alpha.md"))  # names the file: the section text's entry, though another entry touches the file
    m.item_entry("modify", "{P}ALPHA-02")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "top to bottom")
    self.shows(frag, "inserted", "bottom"); self.reason(frag, m, tag)


@matrix_cell("section", "removed-with-section")
def _(self, m):
    m.sub("{f}/alpha.md", "How the extras read.", "How the extras read. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "## Extras\n\nHow the extras read.\n\n", "")  # its item now sits under Basics: no change
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Formerly")
    self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag); self.cites(frag, html, old=True, inside=True)


@matrix_cell("section", "removed-from-kept-section")
def _(self, m):
    m.sub("{f}/alpha.md", "How the extras read.", "How the extras read. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "## Extras\n\nHow the extras read.\n\n", "## Extras\n\n")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Formerly")
    self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag); self.cites(frag, html, old=True, inside=True)


@matrix_cell("section", "removed-from-kept-itemless-section")
def _(self, m):
    m.sub("{f}/alpha.md", "## Extras\n", "## Later\n\n" + OLD_TEXT + "\n\n## Extras\n", base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "## Extras\n", "## Later\n\n## Extras\n")
    tag = m.carrier("{f}/alpha.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Formerly")
    self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag); self.cites(frag, html, old=True, inside=True)


# --- requirement (spec item)

@matrix_cell("requirement", "added")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board shows a count.\n", "The alpha board shows a count.\n\n### {P}ALPHA-05\nThe alpha board shows a footer. " + NEW_TEXT + "\n")
    m.new_defs("{f}/alpha.md")
    tag = m.item_entry("add", "{P}ALPHA-05")
    html = m.render(); self.valid(m)
    frag = card_of(html, m.a + "alpha-05")
    self.assertIn('class="item added', frag); self.reason(frag, m, tag); self.cites(frag, html, new=True)


@matrix_cell("requirement", "modified")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board shows a title.", "The alpha board shows a title. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "The alpha board shows a title.", "The alpha board shows a title. " + NEW_TEXT); m.new_defs("{f}/alpha.md")
    tag = m.item_entry("modify", "{P}ALPHA-02")
    html = m.render(); self.valid(m)
    frag = card_of(html, m.a + "alpha-02")
    self.shows(frag, "inserted", "Freshly"); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, new=True, old=True, inside=True)


@matrix_cell("requirement", "retired")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board can be archived.", "The alpha board can be archived. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "### {P}ALPHA-03\nThe alpha board can be archived.", "### {P}ALPHA-03 (retired)\nArchiving is no longer offered.")
    tag = m.item_entry("retire", "{P}ALPHA-03", retired=True)
    html = m.render(); self.valid(m)
    frag = card_of(html, m.a + "alpha-03-retired")
    self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag); self.cites(frag, html, old=True, inside=True)


@matrix_cell("requirement", "missing")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board can be archived.", "The alpha board can be archived. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "### {P}ALPHA-03\nThe alpha board can be archived.\n\n", "")
    tag = m.item_entry("retire", "{P}ALPHA-03")
    html = m.render(); self.valid(m)
    frag = card_of(html, m.a + "alpha-03")
    self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag); self.cites(frag, html, old=True, inside=True)


@matrix_cell("requirement", "unchanged-citing-outside-document")
def _(self, m):
    """Both files cite the same outside document, spelled from their own folders: no change."""
    m.sub("{f}/alpha.md", "The alpha board shows a title.", "The alpha board shows a title, per [the memo][memo].", base=True)
    m.define("{f}/alpha.md", "memo", m.up("{f}/alpha.md", True) + "ref/new-memo.md#point", base=True)
    m.sub("{f}/alpha.md", "The alpha board shows a title.", "The alpha board shows a title, per [the memo][memo].")
    m.define("{f}/alpha.md", "memo", m.up("{f}/alpha.md", False) + "ref/new-memo.md#point")
    m.sub("{f}/alpha.md", "shows a count.", "shows a total.")  # an unchanged file is not on the page
    m.item_entry("modify", "{P}ALPHA-04")
    html = m.render(); self.valid(m)
    frag = card_of(html, m.a + "alpha-02")
    self.assertIn('class="item unchanged"', frag, "a citation whose target keeps its identity is no change")
    self.reason(frag, m); self.assertIn(f'href="{NEW_MEMO}"', frag)


@matrix_cell("requirement", "moved", flavors=("design",))
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board can be archived.", "The alpha board can be archived, per [the memo][memo].", base=True)
    m.define("{f}/alpha.md", "memo", m.up("{f}/alpha.md", True) + "ref/new-memo.md#point", base=True)
    m.sub("{f}/alpha.md", "### {P}ALPHA-03\nThe alpha board can be archived.\n\n", "")
    m.sub("{f}/beta.md", "The beta board lists its lanes.\n", "The beta board lists its lanes.\n\n### {P}ALPHA-03\nThe alpha board can be archived, per [the memo][memo].\n")
    m.define("{f}/beta.md", "memo", m.up("{f}/beta.md", False) + "ref/new-memo.md#point")
    tag = m.entry("move item", m.ident_item("{P}ALPHA-03", "beta"), ["{f}/alpha.md", "{f}/beta.md"], arrow=True)
    html = m.render(); self.valid(m)
    new = card_of(section_of(html, m.t("{f}/beta.md")) or "", m.a + "alpha-03")
    self.assertIn('class="item added', new or "", "the moved item shows as added in its new file")
    self.shows(new, "unmarked"); self.reason(new, m, tag); self.assertIn(f'href="{NEW_MEMO}"', new)
    old = re.search(r'<details class="item missing" id="([^"]+)".*?</details>', section_of(html, m.t("{f}/alpha.md")) or "", re.S)
    self.assertIsNotNone(old, "and as missing from its old one")
    self.reason(old.group(0), m, tag); self.assertIn(f'href="{NEW_MEMO}"', old.group(0), "its struck-through old body links where the old file linked")
    self.assertEqual(re.findall(rf'id="{m.a}alpha-03"', html), [f'id="{m.a}alpha-03"'], "one card holds the item's anchor: a link to the item lands on its new home")
    self.assertNotEqual(old.group(1), f"{m.a}alpha-03"); self.assertEqual(html.count(f'id="{old.group(1)}"'), 1, "the missing card's qualified anchor is its own")


@matrix_cell("requirement", "moved-and-revised", flavors=("design",))
def _(self, m):
    """A moved item is the same identity: its new home's card diffs it against its old home, each
    side's citations resolving through its own file's definitions."""
    m.sub("{f}/alpha.md", "The alpha board can be archived.", "The alpha board can be archived. " + OLD_TEXT + "\n\n- **01** An archived board is read-only.", base=True)
    m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "### {P}ALPHA-03\nThe alpha board can be archived.\n\n", "")
    m.sub("{f}/beta.md", "The beta board lists its lanes.\n", "The beta board lists its lanes.\n\n### {P}ALPHA-03\nThe alpha board can be archived. " + NEW_TEXT + "\n\n- **01** An archived board is read-only and hidden.\n")
    m.new_defs("{f}/beta.md")
    move = m.entry("move item", m.ident_item("{P}ALPHA-03", "beta"), ["{f}/alpha.md", "{f}/beta.md"], arrow=True)
    own = m.entry("modify item", m.ident_item("{P}ALPHA-03", "beta"), ["{f}/beta.md"])
    rule = m.entry("modify rule", m.ident_item("{P}ALPHA-03-01", "beta"), ["{f}/beta.md"])
    html = m.render(); self.valid(m)
    frag = card_of(section_of(html, m.t("{f}/beta.md")) or "", m.a + "alpha-03")
    self.assertIn('class="item added', frag or "", "it shows as added in its new home")
    self.assertIn(m.t("Moved from {f}/alpha.md"), frag, "naming its old home")
    statement = frag.split("<ul>")[0]
    self.shows(statement, "inserted", "Freshly"); self.shows(statement, "deleted", "Formerly")
    self.cites(statement, html, new=True, old=True, inside=True)
    self.reason(frag.split('<div class="why">')[1], m, move, own)
    cls, text = rule_of(frag, m.t("{P}ALPHA-03-01"))
    self.assertEqual(cls, "mod", "its rule is diffed against the old rule"); self.shows(text, "inserted", "hidden"); self.reason(text, m, rule)


# --- rule

@matrix_cell("rule", "added")
def _(self, m):
    m.sub("{f}/alpha.md", "- **02** A done card greys out.\n", "- **02** A done card greys out.\n- **03** " + NEW_TEXT + "\n"); m.new_defs("{f}/alpha.md")
    tag = m.rule_entry("add", "{P}ALPHA-01-03")
    html = m.render(); self.valid(m)
    self.rule_cell(html, m, "03", "add", tag, new=True)


@matrix_cell("rule", "modified")
def _(self, m):
    m.sub("{f}/alpha.md", "A done card greys out.", "A done card greys out. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "A done card greys out.", "A done card greys out. " + NEW_TEXT); m.new_defs("{f}/alpha.md")
    tag = m.rule_entry("modify", "{P}ALPHA-01-02")
    html = m.render(); self.valid(m)
    self.rule_cell(html, m, "02", "mod", tag, new=True, old=True)


@matrix_cell("rule", "retired")
def _(self, m):
    m.sub("{f}/alpha.md", "A done card greys out.", "A done card greys out. " + OLD_TEXT, base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "- **02** A done card greys out.", "- **02** (retired) Done cards now hide.")
    tag = m.rule_entry("retire", "{P}ALPHA-01-02")
    html = m.render(); self.valid(m)
    self.rule_cell(html, m, "02", "ret", tag, old=True)


matrix_skip("rule", "moved", "the guides allow no move for a rule: one changing parent retires and is re-added")


def rule_cell(self, html, m, num, cls, tag, new=False, old=False, table=False):
    card = card_of(html, m.a + "alpha-01")
    rid = m.t("{P}ALPHA-01-") + num
    got, text = rule_of(card, rid)
    self.assertEqual(got, cls if not table else "", f"rule {rid} carries its change")
    if table:
        whole = re.search(rf'data-rid="{re.escape(rid)}">.*?</table>', card, re.S).group(0)
        self.assertRegex(whole, r'<tr class="(add|mod|rem)">', "the rule's table shows its change")
        self.cites(whole, html, new=new, old=old, inside=cls == "mod")
    else:
        if cls == "mod":
            self.shows(text, "inserted", "Freshly"); self.shows(text, "deleted", "Formerly")
        elif cls == "ret":
            self.shows(text, "deleted", "Formerly")
        self.cites(text, html, new=new, old=old, inside=cls in ("mod", "ret"))
    if m.design:  # design specs list the rule: its entry's reason sits on the rule
        self.reason(text, m, tag)
    else:  # product specs: the parent's modify requirement entry, under the card
        self.reason(card.split('<div class="why">', 1)[1] if '<div class="why">' in card else None, m, tag)


RenderMatrix.rule_cell = rule_cell


# --- rule table

@matrix_cell("rule-table", "added")
def _(self, m):
    m.sub("{f}/alpha.md", "- **02** A done card greys out.\n", "- **02** A done card greys out.\n\n  | State | Look |\n  | --- | --- |\n  | Done | " + NEW_TEXT + " |\n")
    m.new_defs("{f}/alpha.md")
    tag = m.rule_entry("modify", "{P}ALPHA-01-02")
    html = m.render(); self.valid(m)
    self.rule_cell(html, m, "02", "add", tag, new=True, table=True)


@matrix_cell("rule-table", "modified")
def _(self, m):
    m.sub("{f}/alpha.md", "| Pinned | top |", "| Pinned | top. " + OLD_TEXT + " |", base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "| Pinned | top |", "| Pinned | top. " + NEW_TEXT + " |"); m.new_defs("{f}/alpha.md")
    tag = m.rule_entry("modify", "{P}ALPHA-01-01")
    html = m.render(); self.valid(m)
    self.rule_cell(html, m, "01", "mod", tag, new=True, old=True, table=True)


@matrix_cell("rule-table", "removed")
def _(self, m):
    m.sub("{f}/alpha.md", "| Pinned | top |", "| Pinned | top. " + OLD_TEXT + " |", base=True); m.old_defs("{f}/alpha.md")
    m.sub("{f}/alpha.md", "\n  | Kind | Place |\n  | --- | --- |\n  | Plain | bottom |\n  | Pinned | top |\n", "")
    tag = m.rule_entry("modify", "{P}ALPHA-01-01")
    html = m.render(); self.valid(m)
    self.rule_cell(html, m, "01", "rem", tag, old=True, table=True)


matrix_skip("rule-table", "moved", "a table moves only with its rule, and a rule takes no move")


# --- glossary entry

@matrix_cell("glossary-entry", "added")
def _(self, m):
    m.sub("glossary.md", "\n\n[", "\n\n### Dial tone\nThe ready signal. " + NEW_TEXT + "\n\n["); m.new_defs("glossary.md")
    tag = m.term_entry("add", "Dial tone")
    html = m.render(); self.valid(m)
    frag = card_of(html, "dial-tone")
    self.assertIn('class="item added', frag); self.reason(frag, m, tag); self.cites(frag, html, new=True)


@matrix_cell("glossary-entry", "modified")
def _(self, m):
    m.sub("glossary.md", "draws ([{P}ALPHA-01]).", "draws ([{P}ALPHA-01]). " + OLD_TEXT, base=True); m.old_defs("glossary.md")
    m.sub("glossary.md", "draws ([{P}ALPHA-01]).", "draws ([{P}ALPHA-01]). " + NEW_TEXT); m.new_defs("glossary.md")
    tag = m.term_entry("modify", "Board lane")
    html = m.render(); self.valid(m)
    frag = card_of(html, "board-lane")
    self.shows(frag, "inserted", "Freshly"); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, new=True, old=True, inside=True)


@matrix_cell("glossary-entry", "modified-also-called")
def _(self, m):
    m.sub("glossary.md", "keeps ([{P}ALPHA-02]).\n", "keeps ([{P}ALPHA-02]).\n\n> **Also called:** pile (support).\n", base=True)
    m.sub("glossary.md", "keeps ([{P}ALPHA-02]).\n", "keeps ([{P}ALPHA-02]).\n\n> **Also called:** pile (support); heap (the web app).\n")
    tag = m.term_entry("modify", "Card stack")
    html = m.render(); self.valid(m)
    frag = card_of(html, "card-stack")
    self.assertIn('class="item modified', frag); self.shows(frag, "inserted", "heap"); self.reason(frag, m, tag)


@matrix_cell("glossary-entry", "removed")
def _(self, m):
    m.sub("glossary.md", "keeps ([{P}ALPHA-02]).", "keeps ([{P}ALPHA-02]). " + OLD_TEXT, base=True); m.old_defs("glossary.md")
    m.sub("glossary.md", "### Card stack\nA pile of cards the alpha board keeps ([{P}ALPHA-02]).\n\n", "")
    m.sub("glossary.md", "\n[{P}ALPHA-02]: {f}/alpha.md#{a}alpha-02\n", "\n")
    tag = m.term_entry("retire", "Card stack")
    html = m.render(); self.valid(m)
    frag = card_of(html, "card-stack")
    self.assertIn('class="item removed', frag); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, old=True, inside=True)


def glossary_move(m, old_text, new_text, new_memo_only):
    """Card stack leaves the folder's glossary for the root glossary: the old home two folders
    down in the catalog, the new one two down in the package, so each spells its links its own way."""
    entry = "### Card stack\nA pile of cards the alpha board keeps ([{P}ALPHA-02]). "
    m.add_base("{f}/glossary.md", "# Screen Terms\n\n" + entry + old_text + "\n\n### Lane badge\nA badge on a lane ([{P}BETA-01]).\n\n"
               "[{P}ALPHA-02]: alpha.md#{a}alpha-02\n[{P}BETA-01]: beta.md#{a}beta-01\n")
    m.define("{f}/glossary.md", "memo", m.up("{f}/glossary.md", True) + ("ref/new-memo.md#point" if new_memo_only else "ref/old-memo.md#point"), base=True)
    m.sub("glossary.md", "### Card stack\nA pile of cards the alpha board keeps ([{P}ALPHA-02]).\n\n", "", base=True)
    m.sub("glossary.md", "\n[{P}ALPHA-02]: {f}/alpha.md#{a}alpha-02\n", "\n", base=True)
    m.sub("{f}/glossary.md", entry + old_text + "\n\n", "")
    m.sub("{f}/glossary.md", "[{P}ALPHA-02]: alpha.md#{a}alpha-02\n", "")
    m.sub("glossary.md", "keeps ([{P}ALPHA-02]).", "keeps ([{P}ALPHA-02]). " + new_text)
    if new_memo_only:
        m.define("glossary.md", "memo", m.up("glossary.md", False) + "ref/new-memo.md#point")
    else:
        m.new_defs("glossary.md")
    return m.entry("move glossary entry", m.ident_term("Card stack", "glossary.md"), ["{f}/glossary.md", "glossary.md"], arrow=True)


@matrix_cell("glossary-entry", "moved", flavors=("design",))
def _(self, m):
    """A pure move: the same definition, its citation spelled from each file's folder."""
    tag = glossary_move(m, "Kept, per [the memo][memo].", "Kept, per [the memo][memo].", True)
    html = m.render(); self.valid(m)
    frag = card_of(section_of(html, "glossary.md") or "", "card-stack")
    self.assertIn('class="item added', frag or "", "the moved entry shows as added in its new file")
    self.assertIn(m.t("Moved from {f}/glossary.md"), frag, "naming its old home")
    self.shows(frag, "unmarked"); self.reason(frag, m, tag); self.assertIn(f'href="{NEW_MEMO}"', frag)
    old = re.search(r'<details class="item removed" id="([^"]+)".*?</details>', section_of(html, m.t("{f}/glossary.md")) or "", re.S)
    self.assertIsNotNone(old, "and as removed from its old home"); self.reason(old.group(0), m, tag)
    self.assertIn(f'href="{NEW_MEMO}"', old.group(0), "its old text links where its old home linked")
    self.assertEqual(re.findall(r'id="card-stack"', html), ['id="card-stack"'], "one card holds the term's anchor: a link to the term lands on its new home")
    self.assertNotEqual(old.group(1), "card-stack"); self.assertEqual(html.count(f'id="{old.group(1)}"'), 1, "the removed card's qualified anchor is its own")


@matrix_cell("glossary-entry", "moved-and-revised", flavors=("design",))
def _(self, m):
    move = glossary_move(m, OLD_TEXT, NEW_TEXT, False)
    tag = m.term_entry("modify", "Card stack", "glossary.md")
    html = m.render(); self.valid(m)
    frag = card_of(section_of(html, "glossary.md") or "", "card-stack")
    self.assertIn(m.t("Moved from {f}/glossary.md"), frag or "")
    self.shows(frag, "inserted", "Freshly"); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, move, tag)
    self.cites(frag, html, new=True, old=True, inside=True)


# --- glossary intro

@matrix_cell("glossary-intro", "added")
def _(self, m):
    m.sub("glossary.md", "Terms the specs use.\n\n", "", base=True)
    m.sub("glossary.md", "Terms the specs use.", NEW_TEXT); m.new_defs("glossary.md")
    tag = m.carrier("glossary.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.reason(frag, m, tag); self.cites(frag, html, new=True, inside=True)


@matrix_cell("glossary-intro", "modified")
def _(self, m):
    m.sub("glossary.md", "Terms the specs use.", "Terms the specs use. " + OLD_TEXT, base=True); m.old_defs("glossary.md")
    m.sub("glossary.md", "Terms the specs use.", "Terms the specs use. " + NEW_TEXT); m.new_defs("glossary.md")
    tag = m.carrier("glossary.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Freshly")
    self.shows(frag, "inserted", "Freshly"); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, new=True, old=True, inside=True)


@matrix_cell("glossary-intro", "removed")
def _(self, m):
    m.sub("glossary.md", "Terms the specs use.", "Terms the specs use. " + OLD_TEXT, base=True); m.old_defs("glossary.md")
    m.sub("glossary.md", "Terms the specs use.\n\n", "")
    tag = m.carrier("glossary.md")
    html = m.render(); self.valid(m)
    frag = prose_of(html, "Formerly")
    self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag); self.cites(frag, html, old=True, inside=True)


# --- index line

def gamma_file(m):
    m.draft("{f}/gamma.md"); m.drafted[m.t("{f}/gamma.md")] = m.t("# Gamma\n\nThe gamma board in brief.\n\n### {P}GAMMA-01\nThe gamma board exists.\n")
    m.sub("{f}/_{f}.md", "\n\n[alpha]", "\n- [gamma] -- `{P}GAMMA-` -- What the gamma board holds. " + NEW_TEXT + "\n\n[alpha]")
    m.define("{f}/_{f}.md", "gamma", "gamma.md"); m.new_defs("{f}/_{f}.md")
    return m.entry("add spec file" if m.design else "add file", m.ident_file("{f}/gamma.md"), ["{f}/gamma.md", "{f}/_{f}.md"])


def index_change(m, op):
    """Design specs list the index line; product specs carry it in another entry's Touches."""
    if m.design:
        name = "s-" + anchor(m.t("{f}/_{f}.md")); m.defs[name] = f"{m.drafts.name}/{m.t('{f}/_{f}.md')}"
        return m.entry(f"{op} index line", f"[alpha][{name}]", ["{f}/_{f}.md"])
    return m.carrier("{f}/_{f}.md")


@matrix_cell("index-line", "added")
def _(self, m):
    tag = gamma_file(m)
    html = m.render(); self.valid(m)
    frag = index_card_of(html, "gamma")
    self.assertIn('class="item added', frag or ""); self.reason(frag, m, tag); self.cites(frag, html, new=True)


@matrix_cell("index-line", "modified")
def _(self, m):
    m.sub("{f}/_{f}.md", "What the alpha board holds", "What the alpha board holds. " + OLD_TEXT, base=True); m.old_defs("{f}/_{f}.md")
    m.sub("{f}/_{f}.md", "What the alpha board holds", "What the alpha board holds. " + NEW_TEXT); m.new_defs("{f}/_{f}.md")
    tag = index_change(m, "modify")
    html = m.render(); self.valid(m)
    frag = index_card_of(html, "alpha")
    self.shows(frag, "inserted", "Freshly"); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, new=True, old=True, inside=True)


@matrix_cell("index-line", "retargeted")
def _(self, m):
    m.sub("{f}/_{f}.md", "[alpha]: alpha.md", "[alpha]: beta.md")
    tag = index_change(m, "modify")
    html = m.render(); self.valid(m)
    frag = index_card_of(html, "alpha")
    self.assertIn('class="item modified', frag or "")
    self.assertIn(m.t('<del class="w">{f}/alpha.md</del> <ins class="w">{f}/beta.md</ins>'), frag, "old and new target show")
    self.reason(frag, m, tag)


@matrix_cell("index-line", "removed")
def _(self, m):
    m.sub("{f}/_{f}.md", "What the alpha board holds", "What the alpha board holds. " + OLD_TEXT, base=True); m.old_defs("{f}/_{f}.md")
    m.sub("{f}/_{f}.md", "- [alpha] -- `{P}ALPHA-` -- What the alpha board holds\n", "")
    m.sub("{f}/_{f}.md", "[alpha]: alpha.md\n", "")
    tag = index_change(m, "retire")
    html = m.render(); self.valid(m)
    frag = index_card_of(html, "alpha")
    self.assertIn('class="item removed', frag or ""); self.shows(frag, "deleted", "Formerly"); self.reason(frag, m, tag)
    self.cites(frag, html, old=True, inside=True)


# --- file heading

@matrix_cell("file-heading", "added")
def _(self, m):
    tag = gamma_file(m)
    html = m.render(); self.valid(m)
    frag = section_of(html, m.t("{f}/gamma.md"))
    self.assertRegex(frag or "", r'^<section class="file" data-kind="added">', "the new file shows as added")
    self.assertIn(f'href="#file-{anchor(m.t("{f}/gamma.md"))}"', html, "and is listed under Documents")
    head = re.search(r'<p class="file-why">.*?</p>', frag).group(0)
    self.reason(head, m, tag)


@matrix_cell("file-heading", "modified")
def _(self, m):
    m.sub("{f}/alpha.md", "The alpha board shows a title.", "The alpha board shows a short title.")
    tag = m.item_entry("modify", "{P}ALPHA-02")
    tag2 = m.entry("modify spec file" if m.design else "modify file", m.ident_file("{f}/alpha.md"), ["{f}/alpha.md"])
    m.sub("{f}/alpha.md", "The alpha board in brief.", "The alpha board in brief, top to bottom.")
    html = m.render(); self.valid(m)
    frag = section_of(html, m.t("{f}/alpha.md"))
    self.assertRegex(frag or "", r'^<section class="file" data-kind="modified">')
    head = re.search(r'<p class="file-why">.*?</p>', frag)
    self.reason(head.group(0) if head else None, m, tag2)  # the file's own entry


matrix_skip("file-heading", "removed", "a draft cannot remove a file: files never retire, and drafts hold only the files they touch")
matrix_skip("file-heading", "moved", "the guides allow no move for a file")
@matrix_cell("file-heading", "retitled")
def _(self, m):
    """A changed '#' title is a difference: shown at its file, and the change list names it with a
    file entry (modify spec file in design specs, modify file in product specs)."""
    m.sub("{f}/alpha.md", "# Alpha\n", "# Alpha Board\n")
    tag = m.entry("modify spec file" if m.design else "modify file", m.ident_file("{f}/alpha.md"), ["{f}/alpha.md"])
    html = m.render(); self.valid(m)
    frag = section_of(html, m.t("{f}/alpha.md"))
    self.assertRegex(frag or "", r'^<section class="file" data-kind="modified">', "the retitled file shows as modified")
    title = prose_of(frag, "Board")
    self.shows(title, "inserted", "Board"); self.reason(title, m, tag)
    m.entries.pop(); m.render()
    self.assertTrue(any("title Alpha Board is modified but no change-list entry names it" in i for i in m.check_issues), m.check_issues)



if __name__ == "__main__":
    unittest.main()
