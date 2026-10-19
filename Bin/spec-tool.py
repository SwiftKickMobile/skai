#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""spec-tool.py — validate, cross-reference and render product spec and design spec files.

The file shape is defined in Guides/Core/spec-file-shape.md. This tool is its parser. It needs
only the Python standard library.

Usage:
    python3 spec-tool.py validate ROOT [ROOT ...]
        Parse every .md under the roots; print one line per failure as path:line: message.
        A later root overlays an earlier one: a file at the same relative path replaces the
        earlier file, which is how a package's drafts project onto the catalog. With several
        roots only the drafts block: a per-file diagnostic (shape, link definitions, unlinked
        glossary terms, even for a term the drafts introduce, since a package cannot edit files
        it does not hold) in a file the later roots do not supply (an untouched canonical file,
        or a catalog file a draft replaces) is printed with a "note:" prefix and does not affect
        the exit status, while a whole-projection conflict (duplicate ID, duplicate glossary
        term) counts when at least one side is in a draft file and is a note when both sides are
        untouched canonical files the package does not hold. A draft that revives an item or
        rule its canonical file retired is rejected, naming the ID and the canonical file: a
        retired ID is burned, never modified. Every relative link definition must resolve: the
        file, in the projection (or on disk when the path leaves the roots), and the anchor when
        there is one (an item, a retired item's "-retired" anchor, a glossary entry, a rule's
        parent); external URLs are not checked. A draft's link to a glossary file must also
        reach it on disk: when the projection resolves it only through a catalog glossary the
        package does not hold, the draft is told the glossary's real relative path (the rendered
        link would point at nothing). An unresolvable target is an issue in a draft
        file. In an untouched canonical file it is a note when the catalog alone does not resolve
        it either (the link was dangling before the package), and a blocking issue at that file's
        line when the catalog resolves it and the projection does not: the drafts retired the
        cited item or rule (its anchor became "-retired"), moved the item to another file, or
        removed the glossary entry, a conflict the projection introduces that the package must
        settle (hold the file, or a change request). With a single root everything counts. Exit
        status 1 when there are blocking failures.

    python3 spec-tool.py references ID ROOT [ROOT ...]
        List every file:line that cites ID or one of its rules (ID-NN, ID-NN-NN). For a rule,
        also the bold-number pointers to it inside its own item: a cell or rule saying **01**
        points at top-level rule 01, **01-01** at nested rule 01-01 (the rule's own definition
        line is not a pointer). Given a glossary term instead (as written in its heading,
        case-insensitive), every linked occurrence of it across the roots.

    python3 spec-tool.py link-terms ROOT [ROOT ...]
        Rewrite spec files in place so every occurrence of a glossary term is linked. Terms are
        read from every root (a later root overlays an earlier one, as in validate), but only
        files under the last root are rewritten: `link-terms CATALOG DRAFTS` links the drafts and
        never modifies a catalog file (an unlinked use there is validate's note, settled when
        that file is next touched); `link-terms CATALOG` alone, a migration, rewrites the catalog.

    python3 spec-tool.py convert ROOT [ROOT ...]
        The migration converter: rewrite files in place from the old shape to the new — "## <ID>"
        items to "###", dotted rule citations to dashes (UI-X-01.03 → UI-X-01-03, in prose and
        link definitions), glossary entries from "**Term** — text" paragraphs to "### Term"
        headings with the text beneath, the old index bullet's "- [name] — text" em dash to the
        shape's "--" — then link-terms. Reorganizes nothing; running it again
        changes nothing. Prints what it changed per file, then validates the result as
        `validate ROOT...` would; exit status 1 when that has blocking issues.

    python3 spec-tool.py render --catalog DIR --drafts DIR [--authoring FILE | --no-authoring] [--out FILE.html]
        --base DIR (repeatable) layers another open package's drafts over the catalog, each later
        --base winning, so a package drafted on top of an unpromoted package diffs against that
        package's drafts; check-changes takes the same flag.
        A change package's review page. The authoring artifact is found beside the drafts
        folder: product-specs-authoring.md (or the legacy requirements-authoring.md, accepted like
        the other legacy names for one release after the rename; the new name wins when both exist), or
        design-specs-authoring.md when the drafts folder is proposed-design-specs; --authoring
        points elsewhere, and a missing artifact is an error, so a review render always carries
        the card, discussion and justifications. --no-authoring renders a bare drafts-to-catalog
        comparison, never the committed page. Without --out the page is written into the package
        folder (the drafts' parent) as product-specs-review.html or design-specs-review.html; a
        legacy proposed-requirements drafts folder is a product-specs package.

    python3 spec-tool.py render-request --catalog DIR --package-drafts DIR --request DIR [--out FILE.html]
        A change request's own page, relative to the package it targets (falling back to the
        catalog). --package-drafts may be the legacy proposed-requirements folder. The request's
        own drafts are <request>/proposed-product-specs or <request>/proposed-design-specs,
        whichever exists (requests are new, so they have no legacy name). Without --out it is
        written beside request.md as request-review.html.

    python3 spec-tool.py check-changes --catalog DIR --drafts DIR --authoring FILE
        The list-matches-diff check: every added, modified, retired or missing item, glossary
        entry or index line in the projection has a change-list entry, every added file has one
        (an entry naming it, or naming it in Touches), a changed intro (an index file's reminder
        line too), section line or index line may instead ride in an entry's Touches naming its
        file, and no entry names something unchanged or
        absent, including a rule (ID-NN, ID-NN-NN) the drafts do not define. The declared
        operation must match the projection: add names something added, modify something
        modified, retire something retired, removed or missing (an item whose heading is gone,
        as a catalog rework absorbs it), move (design specs) an item missing from
        one file and added in another, or a glossary entry removed from one glossary file and
        added in another (keyed by term across files, so a relocation is one move, never a retire
        plus an add; a modify entry rides on it when the text changed on the way); a file-typed entry names the file itself (never its index
        line), so "add file" on a file the catalog already has, or "modify file" on a new one,
        fails; an entry about a rule ("sub-item" is accepted as the older
        name) or a known-difference note names an item that shows as modified. A moved item may
        change on the way: then a modify entry rides on the move and both are accepted, and a
        move whose item changed without a modify entry fails, as does a modify entry on a moved
        item whose text is the same. One line per failure as path:line: message; exit
        status 1 when there are any.

GLOSSARY TERMS (what "every occurrence in spec prose" covers, for validate and link-terms)

    Spec prose is every line of a spec file that is not a heading, a link definition, a table
    header or separator row: the intro, a section's orientation line, and every item's statement,
    table body cells, rules (nested and retired ones too) and known-difference notes, in retired
    items as well as live ones. Table headers are column labels, not prose, like the headings
    they sit under. Glossary files and index files are not spec prose. An item that a term's
    entry names as governing is exempt for that term; intro and section lines are never exempt.
    Every glossary.md under a root is part of the glossary and they are read as one (a term
    defined in two of them is rejected); entries stay alphabetical within each file's sections.
    link-terms writes the link and the definition for every unlinked occurrence the validator
    would report, the definition pointing at the glossary file that holds the entry where it
    sits on disk relative to the rewritten file (the drafts' copy when the last root holds one,
    else the earlier root's, so the rendered link resolves); popovers
    and diffing key entries by term wherever they sit.

CHANGE LISTS (what render, render-request and check-changes read from the authoring artifact)

    Entries are "- R<n> <type>: <identity>" (product) or "- S<n> <operation> <object>: <identity>"
    (design), each followed by its indented "**Justification**" field and optional "**Touches**".
    A field runs to the next bold field label, the next list entry, a heading or the first
    link-definition line, whichever comes first, so the last entry's Touches never takes in the
    artifact's link definitions.
    The identity is a plain path or term, or a link: an item or rule ID ("[STAGE-01]",
    "[UI-NOTES-01-02]", dots accepted for dashes), a term ("[Stale notice][s-glossary]"), a file
    title ("[List Screen][s-list]", resolved through the artifact's link definitions to the draft
    path) or a bare path ("domains/offer.md"). A rule identity attaches to its parent item. The
    justification is placed under the item, glossary entry, index line or file the identity
    resolves to; several entries for one target are joined.

RENDER CONVENTIONS (the canonical render spec; update with the code)

 1. Diffing: file by path; intro by text; item by ID (added, modified, retired, missing);
    statement by word; rule by ID-NN, including the tables under it; table by header cells, then
    row by key column (added, removed, changed cells, moved); known difference by parent and app;
    glossary entry by term, whatever its optional "##" section (the draft's section headings
    are shown between entries and never diffed); an index file's reminder line is its intro and
    diffs by text like a spec file's; index line by link name (a wrapped line's indented
    continuation is part of its text, not of the intro), comparing its text and
    the identity of its target (a retargeted line is modified and shows old and new target).
    Row order is compared: a row that moved
    relative to the rows kept around it is marked; whether the order binds is the statement's
    to say and the reviewer's to judge. Glossary link markup is not content. A citation compares
    by its label and the identity of its target (the anchor, or the file name when there is no
    anchor), so a link-definition path change is not a change and a retargeted citation is.
    Sections are not diffed: a section's name, its order and which items it holds are never
    compared, and an item moving between sections is not a change; a section's orientation line
    is prose and is word-diffed like the intro.
 2. Package page: title "Change Package: <id>", the id being the change folder above
    product-specs/ or design-specs/ (a legacy requirements/ parent is accepted too; else the drafts'
    parent); a legend
    row of counts (added, modified, retired or removed, unchanged, added files), each with its
    colored square; a card with the package's status (open item count, or "ready for promotion"),
    title, goal and discussion count; a "Documents" box with one linked line per file (square,
    name, changed count); the discussion items in full, in their "###" topic groups in artifact
    order, each a card with its square (green approved, amber open), ID, kind, title and its
    sub-bullets as written (Concern, Proposal, Options with their lettered choices, Detail, Why,
    Decision), citations linked and popovers as elsewhere, so an item can be resolved from the
    page; then each file in order. When the artifact has a "## Situations" section it is
    rendered after the card, as written (headings, bullets, paragraphs), citations linked. The
    card, Situations and Discussion resolve their links through the authoring artifact's own
    definitions, never a draft's.
 3. Within a file: its intro, its sections with their descriptions, its items in file order.
    Changed items are expanded; unchanged and retired items are collapsed in place so links to
    them resolve and open on arrival. Each change's justification from the authoring artifact
    sits under its card (items, glossary entries and index lines alike); a new file's under its
    heading. A change nothing names directly but that rides in an entry's Touches (a changed
    intro, section line or index line) carries that entry's justification, so every changed
    thing on the page has a reason.
 4. Request page: title "Change Request: <nnn>" with "Change Package: <id>" beneath; the same card
    with status, title, goal and reviewer response; the Documents box; the request's drafts
    diffed against the package's drafts, falling back to the catalog, each requested change's
    justification under its card. A request without drafts shows, after the card, one card per
    requested change: its type, its identity (linked where the request's definitions resolve
    it) and its justification.
 5. Status is a small colored square, never a text pill: green added, amber modified, red retired
    or removed, gray unchanged. It leads the file heading, item, rule or table row it marks. Rows
    and rules inside an item that is itself new carry no square. A card's status, discussion-kind
    or request-type badge is not a change marker and may be a text pill.
 6. Cards are white on a very light gray page with a soft shadow; popovers and summary boxes are
    white too. Section headings and descriptive text are normal weight and color; section
    headings are uppercase. Rule numbers and tables are body size.
 7. Whole deletions (retired items, removed rows, rules, entries) are gray strikethrough with no
    tint, including the ID. A retired or missing item's collapsed card holds its whole old body
    (statement, tables, rules, known differences) struck through, with no squares inside, then
    the retirement statement. Inside a modified block, removed words carry a light red tint with
    strikethrough and added words a light green tint, at normal weight.
 8. Every citation and glossary term that resolves is a link: citations as chips, glossary terms
    as dotted text, both with the link pointer. Hovering opens a popover card with the full cited
    item (statement, tables, rules; a cited rule outlined) or the glossary entry; an item cited
    from outside the roots gets its popover too when its link definition finds the file on disk. Citations that
    cannot resolve are plain muted text, never styled as links. The browser's own tooltip is not
    used.
 9. Dark mode follows the system setting with the same relationships.
"""

import argparse
import difflib
import html
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- shapes

ID_RE = r"[A-Z][A-Z-]*[A-Z]-\d{2,}"
ITEM_HEAD_RE = re.compile(rf"^### (?P<id>{ID_RE})(?P<retired> \(retired\))?\s*$")
ANY_H3_RE = re.compile(r"^### (.*)$")
H2_RE = re.compile(r"^## (.*)$")
H1_RE = re.compile(r"^# (.*)$")
RULE_RE = re.compile(r"^(?P<indent> *)- \*\*(?P<num>\d+)\*\*(?P<retired> \(retired\))?(?P<text>.*)$")
KNOWN_RE = re.compile(r"^> \*\*Known difference — (?P<app>[^:]+):\*\*(?P<text>.*)$")
LINKDEF_RE = re.compile(r"^\[(?P<name>[^\]]+)\]:\s+(?P<target>\S.*)$")
TABLE_ROW_RE = re.compile(r"^( *)\|(.*)\|\s*$")
TABLE_SEP_RE = re.compile(r"^ *\|(\s*:?-+:?\s*\|)+\s*$")
INDEX_LINE_RE = re.compile(r"^- \[(?P<name>[^\]]+)\] -- (?:`(?P<prefixes>[^`]+)` -- )?(?P<text>.*)$")
LINK_USE_RE = re.compile(r"\[([^\]\s][^\]]*)\](?!\()(?:\[([^\]]*)\])?")
MARKER_RE = re.compile(r"(^|\s)- \[[ x]\]|🟡")


@dataclass
class Issue:
    path: Path
    line: int
    msg: str
    note: bool = False  # printed, but outside the projection: does not block

    def __str__(self):
        return f"{'note: ' if self.note else ''}{self.path}:{self.line}: {self.msg}"


@dataclass
class Rule:
    num: str
    text: str
    line: int
    retired: bool = False
    children: list = field(default_factory=list)
    tables: list = field(default_factory=list)

    def rid(self, parent):
        return f"{parent}-{self.num}"


@dataclass
class Table:
    header: list
    rows: list  # list of list[str]
    line: int


@dataclass
class Known:
    app: str
    text: str
    line: int


@dataclass
class Item:
    id: str
    line: int
    retired: bool = False
    section: str = ""
    statement: list = field(default_factory=list)  # paragraphs
    tables: list = field(default_factory=list)
    rules: list = field(default_factory=list)
    knowns: list = field(default_factory=list)


@dataclass
class Spec:
    path: Path
    kind: str  # spec | glossary | index
    title: str = ""
    intro: list = field(default_factory=list)
    items: list = field(default_factory=list)  # Item, or (term, text, line) for glossary, or index lines
    sections: dict = field(default_factory=dict)  # section name -> orientation text
    entry_sections: dict = field(default_factory=dict)  # glossary: term -> section name ("" when none)
    linkdefs: dict = field(default_factory=dict)
    linkdef_lines: dict = field(default_factory=dict)
    issues: list = field(default_factory=list)
    raw: list = field(default_factory=list)


def kind_of(path: Path):
    if path.name == "glossary.md":
        return "glossary"
    if path.name.startswith("_"):
        return "index"
    return "spec"


# ---------------------------------------------------------------- parsing

def parse(path: Path) -> Spec:
    spec = Spec(path=path, kind=kind_of(path))
    lines = path.read_text(encoding="utf-8").splitlines()
    spec.raw = lines
    err = lambda i, m: spec.issues.append(Issue(path, i + 1, m))

    # link definitions: anywhere, but must be after the last content line
    content_end = 0
    for i, line in enumerate(lines):
        m = LINKDEF_RE.match(line)
        if m:
            if m.group("name") in spec.linkdefs:
                err(i, f"duplicate link definition [{m.group('name')}]")
            spec.linkdefs[m.group("name")] = m.group("target")
            spec.linkdef_lines[m.group("name")] = i + 1
        elif line.strip():
            content_end = i
    for name, ln in spec.linkdef_lines.items():
        if ln - 1 < content_end:
            err(ln - 1, f"link definition [{name}] is not at the end of the file")

    body = [(i, l) for i, l in enumerate(lines) if not LINKDEF_RE.match(l)]

    if spec.kind == "glossary":
        _parse_glossary(spec, body, err)
    elif spec.kind == "index":
        _parse_index(spec, body, err)
    else:
        _parse_spec(spec, body, err)

    for i, line in enumerate(lines):
        if MARKER_RE.search(line):
            err(i, "progress marker in spec prose")
    return spec


def _title(spec, body, err):
    """Consume the title line; return index into body after it."""
    j = 0
    while j < len(body) and not body[j][1].strip():
        j += 1
    if j >= len(body) or not H1_RE.match(body[j][1]):
        err(0, "file must start with a single '# Title' line")
        return j
    spec.title = H1_RE.match(body[j][1]).group(1).strip()
    for i, l in body[j + 1:]:
        if H1_RE.match(l):
            err(i, "second '#' heading; only one title allowed")
    return j + 1


def _parse_spec(spec, body, err):
    j = _title(spec, body, err)
    section = ""
    item = None
    para = []
    mode = "intro"  # intro | section | statement | detail
    seen_ids = set()

    def flush_para():
        nonlocal para
        if not para:
            return
        text = " ".join(x.strip() for x in para)
        if mode == "intro":
            spec.intro.append(text)
        elif mode == "section":
            spec.sections[section] = (spec.sections.get(section, "") + " " + text).strip()
        elif mode == "statement":
            item.statement.append(text)
        else:
            err(para_line, "prose after rules or tables; a statement comes first, then tables and rules, then known differences")
        para = []

    para_line = 0
    k = j
    while k < len(body):
        i, line = body[k]
        if not line.strip():
            flush_para()
            k += 1
            continue
        mh2 = H2_RE.match(line)
        mh3 = ANY_H3_RE.match(line)
        if mh2:
            flush_para()
            section = mh2.group(1).strip()
            if re.search(ID_RE, section):
                err(i, "a '##' section heading must not carry an ID")
            item = None
            mode = "section"
            k += 1
            continue
        if mh3:
            flush_para()
            m = ITEM_HEAD_RE.match(line)
            if not m:
                err(i, f"'###' heading must carry only an ID, optionally ' (retired)': {line!r}")
                item = Item(id=mh3.group(1), line=i + 1, section=section)
            else:
                item = Item(id=m.group("id"), line=i + 1, retired=bool(m.group("retired")), section=section)
                if item.id in seen_ids:
                    err(i, f"duplicate ID {item.id} in file")
                seen_ids.add(item.id)
            spec.items.append(item)
            mode = "statement"
            k += 1
            continue
        if item is None:
            if mode == "intro" or mode == "section":
                if not para:
                    para_line = i
                para.append(line)
                k += 1
                continue
        mr = RULE_RE.match(line)
        mk = KNOWN_RE.match(line)
        mt = TABLE_ROW_RE.match(line)
        if item is not None and (mr or mk or mt):
            flush_para()
            mode = "detail"
            if (mr or mt) and item.knowns:
                err(i, "table or rule after a known-difference note; known differences come last in an item")
            if mt:
                k, table = _parse_table(body, k, err)
                indent = len(mt.group(1))
                if indent >= 2 and item.rules:
                    item.rules[-1].tables.append(table)
                else:
                    item.tables.append(table)
                continue
            if mr:
                k = _parse_rule(spec, item, body, k, err)
                continue
            if mk:
                text = [mk.group("text").strip()]
                k += 1
                while k < len(body) and body[k][1].startswith(">"):
                    text.append(body[k][1][1:].strip())
                    k += 1
                item.knowns.append(Known(mk.group("app").strip(), " ".join(t for t in text if t), i + 1))
                continue
        if not para:
            para_line = i
        para.append(line)
        k += 1
    flush_para()
    for it in spec.items:
        if not it.statement:
            err(it.line - 1, f"{it.id} has no statement")


def _parse_table(body, k, err):
    i0, first = body[k]
    rows = []
    while k < len(body) and TABLE_ROW_RE.match(body[k][1]):
        rows.append(body[k])
        k += 1
    if len(rows) < 2 or not TABLE_SEP_RE.match(rows[1][1]):
        err(i0, "table needs a header row and a separator row")
        cells = [[c.strip() for c in TABLE_ROW_RE.match(l).group(2).split("|")] for _, l in rows]
        return k, Table(cells[0] if cells else [], cells[1:], i0 + 1)
    header = [c.strip() for c in TABLE_ROW_RE.match(rows[0][1]).group(2).split("|")]
    data = [[c.strip() for c in TABLE_ROW_RE.match(l).group(2).split("|")] for _, l in rows[2:]]
    keys = set()
    for (i, _), r in zip(rows[2:], data):
        if not r or not r[0]:
            err(i, "table row has an empty key cell (first column)")
        elif r[0] in keys:
            err(i, f"duplicate table key {r[0]!r}")
        keys.add(r[0] if r else "")
    return k, Table(header, data, i0 + 1)


def _parse_rule(spec, item, body, k, err):
    i, line = body[k]
    m = RULE_RE.match(line)
    indent = len(m.group("indent"))
    num, text, retired = m.group("num"), m.group("text").strip(), bool(m.group("retired"))
    if len(num) != 2:
        err(i, f"rule number {num!r} must be two digits")
    rule = Rule(num=num, text=text, line=i + 1, retired=retired)
    if indent == 0:
        expected = f"{len(item.rules) + 1:02d}"
        if num != expected:
            err(i, f"rule {num} out of sequence; expected {expected}")
        item.rules.append(rule)
    elif indent == 2:
        if not item.rules:
            err(i, "nested rule without a parent rule")
            item.rules.append(rule)
        else:
            parent = item.rules[-1]
            expected = f"{len(parent.children) + 1:02d}"
            if num != expected:
                err(i, f"nested rule {num} out of sequence; expected {expected}")
            parent.children.append(rule)
    else:
        err(i, f"rule nested too deep (indent {indent}); one level below a rule is the limit")
        item.rules.append(rule)
    k += 1
    # continuation lines: indented, not a rule/table/known
    while k < len(body):
        _, nxt = body[k]
        if nxt.startswith(" ") and not RULE_RE.match(nxt) and not TABLE_ROW_RE.match(nxt) and nxt.strip():
            rule.text += " " + nxt.strip()
            k += 1
        else:
            break
    if not rule.text:
        err(i, f"rule {num} has no text" + ("; a retired rule says what superseded it" if retired else ""))
    return k


def _parse_glossary(spec, body, err):
    """Entries are '###' headings, alphabetical within their optional '##' section, or within the
    file when there are none; they are keyed by term regardless of section."""
    j = _title(spec, body, err)
    term, para, line_no, section = None, [], 0, ""
    entries = []

    def flush():
        if term is not None:
            entries.append((term, " ".join(x.strip() for x in para), line_no))
            spec.entry_sections[term] = section
        elif para:
            spec.intro.append(" ".join(x.strip() for x in para))

    for i, line in body[j:]:
        if not line.strip():
            continue
        m3, m2 = ANY_H3_RE.match(line), H2_RE.match(line)
        if m3:
            flush()
            term, para, line_no = m3.group(1).strip(), [], i + 1
            if not sentence_case(term):
                err(i, f"glossary term {term!r} should be sentence case: a capital first letter and no capitalized word after it (all-caps acronyms allowed)")
            continue
        if m2:
            flush()
            term, para, section = None, [], m2.group(1).strip()
            if re.search(ID_RE, section):
                err(i, "a '##' section heading must not carry an ID")
            continue
        if line.startswith("**"):
            err(i, "glossary entry must be a '###' heading, not a bold paragraph")
            continue
        para.append(line)
    flush()
    groups = {}
    for t, _, ln in entries:
        groups.setdefault(spec.entry_sections[t], []).append((t, ln))
    for sec, group in groups.items():
        names = [t for t, _ in group]
        if names != sorted(names, key=str.lower):
            err(group[0][1] - 1, "glossary entries are not in alphabetical order within " + (f"section {sec!r}" if sec else "the file"))
    seen = set()
    for t, _, ln in entries:
        if t.lower() in seen:
            err(ln - 1, f"duplicate glossary term {t!r}")
        seen.add(t.lower())
    spec.items = entries


def sentence_case(term):
    """A capital first letter and no later word in Title Case; all-caps tokens (acronyms) pass."""
    words = term.split()
    return bool(words) and words[0][:1].isupper() and not any(re.match(r"[A-Z][a-z]", w) for w in words[1:])


def _parse_index(spec, body, err):
    j = _title(spec, body, err)
    for i, line in body[j:]:
        if not line.strip():
            continue
        if line.startswith("- "):
            m = INDEX_LINE_RE.match(line)
            if not m:
                err(i, f"index line does not match '- [name] -- `PREFIX-` -- questions': {line!r}")
                continue
            spec.items.append((m.group("name"), m.group("prefixes"), m.group("text"), i + 1))
        elif line.startswith(" ") and spec.items:  # a wrapped bullet's indented continuation
            name, prefixes, text, ln = spec.items[-1]
            spec.items[-1] = (name, prefixes, f"{text} {line.strip()}", ln)
        else:
            spec.intro.append(line.strip())


# ---------------------------------------------------------------- validation

def anchor(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def link_uses(text):
    """Return list of link names used in text, for reference-style links."""
    names = []
    for m in LINK_USE_RE.finditer(text):
        label, ref = m.group(1), m.group(2)
        if ref is not None:
            names.append(ref if ref else label)
        else:
            names.append(label)
    return names


def term_pattern(term):
    t = re.escape(term)
    if term.endswith("y"):
        t = re.escape(term[:-1]) + r"(?:y|ies)"
    else:
        t += r"(?:e?s)?"
    return re.compile(rf"(?<![\w-]){t}(?![\w-])", re.I)


def validate(roots):
    """Later roots overlay earlier ones: a file at the same relative path replaces the earlier
    file for the ID-uniqueness check, which is how a package's drafts project onto the catalog."""
    specs, by_rel, canonical, replaced = [], {}, set(), {}  # replaced: rel -> the earlier file a later root overlays
    catalog_by_rel = {}  # the first root alone: what a link resolved to before the projection
    for n, root in enumerate(roots):
        for p in sorted(Path(root).rglob("*.md")):
            s = parse(p)
            specs.append(s)
            rel = p.relative_to(root).as_posix()
            if rel in by_rel:
                replaced[rel] = by_rel[rel]
            by_rel[rel] = s
            if n == 0:
                catalog_by_rel[rel] = s
                if len(roots) > 1:
                    canonical.add(id(s))
    shape = [i for s in specs for i in s.issues]  # per-file checks: notes outside the drafts
    cross = []  # whole-projection checks: block unless both sides are untouched canonical files
    projected = set(id(s) for s in by_rel.values())
    canon = {s.path for s in specs if id(s) in canonical}

    # a retired ID is burned: a draft may not revive an item or rule its canonical file retired
    for rel, old in replaced.items():
        new = by_rel[rel]
        if old.kind != "spec" or new.kind != "spec":
            continue
        old_items = {it.id: it for it in old.items}
        for it in new.items:
            prior = old_items.get(it.id)
            if prior is None:
                continue
            if prior.retired and not it.retired:
                cross.append(Issue(new.path, it.line, f"{it.id} revived; it is retired in {old.path} and a retired ID is never modified"))
            old_rules = {r.rid(it.id): r for r in prior.rules}
            old_rules.update({c.rid(r.rid(it.id)): c for r in prior.rules for c in r.children})
            for r in it.rules:
                for rule, rid in [(r, r.rid(it.id))] + [(c, c.rid(r.rid(it.id))) for c in r.children]:
                    if rid in old_rules and old_rules[rid].retired and not rule.retired:
                        cross.append(Issue(new.path, rule.line, f"{rid} revived; it is retired in {old.path} and a retired rule is never modified"))

    # IDs unique across roots
    seen = {}
    for s in specs:
        if s.kind != "spec" or id(s) not in projected:
            continue
        for it in s.items:
            if it.id in seen and seen[it.id] != s.path:
                cross.append(Issue(s.path, it.line, f"duplicate ID {it.id} also in {seen[it.id]}", note={s.path, seen[it.id]} <= canon))
            seen.setdefault(it.id, s.path)

    # link definitions used and defined
    for s in specs:
        used, first_line = set(), {}
        for ln, l in enumerate(s.raw, 1):
            if LINKDEF_RE.match(l):
                continue
            for name in link_uses(l):
                used.add(name)
                first_line.setdefault(name, ln)
        for name in used:
            if name not in s.linkdefs:
                shape.append(Issue(s.path, first_line[name], f"[{name}] used but not defined"))
        for name, ln in s.linkdef_lines.items():
            if name not in used:
                shape.append(Issue(s.path, ln, f"[{name}] defined but not used"))

    # every relative link definition resolves: the file (in the projection, or on disk when it
    # points outside the roots) and, when there is one, the anchor in that file. In an untouched
    # canonical file, a target the catalog alone resolves but the projection does not is a
    # conflict the drafts introduce (they retired, moved or removed it) and blocks; a target the
    # catalog does not resolve either was dangling before the package and is a note
    rel_of = {id(s): rel for rel, s in by_rel.items()}
    for s in specs:
        if id(s) not in projected:
            continue
        for name, target in s.linkdefs.items():
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            path, frag = target.split("#", 1) if "#" in target else (target, "")
            rel = Path(os.path.normpath(Path(rel_of[id(s)]).parent / path)).as_posix() if path else ""
            found, why = resolve_link(s, rel, path, frag, by_rel)
            if why is None:
                # a draft's glossary link must point at the glossary where it sits on disk: the
                # projection resolving it through a catalog file the package does not hold leaves
                # the rendered link pointing at nothing
                if id(s) not in canonical and canonical and Path(path).name == "glossary.md" and id(found) in canonical and not (s.path.parent / path).resolve().is_file():
                    shape.append(Issue(s.path, s.linkdef_lines[name], f"[{name}] points at {path}, which the package does not hold; the glossary is at {Path(os.path.relpath(found.path.resolve(), s.path.parent.resolve())).as_posix()}"))
                continue
            if id(s) in canonical and resolve_link(s, rel, path, frag, catalog_by_rel)[1] is None:
                cross.append(Issue(s.path, s.linkdef_lines[name], f"[{name}] points at {target}, which the drafts {projection_fate(frag, found, by_rel)}; the catalog resolves it"))
            else:
                shape.append(Issue(s.path, s.linkdef_lines[name], f"[{name}] {why}"))

    # glossary terms (every glossary.md in the projection, read as one) linked on every occurrence in spec prose
    glossaries = [(rel, s) for rel, s in by_rel.items() if s.kind == "glossary"]
    holder = {}
    for rel, g in glossaries:
        for term, _, ln in g.items:
            if term.lower() in holder:
                cross.append(Issue(g.path, ln, f"duplicate glossary term {term!r} also in {holder[term.lower()]}", note={g.path, holder[term.lower()]} <= canon))
            holder.setdefault(term.lower(), g.path)
    terms = glossary_terms(glossaries)
    for s in specs:
        if s.kind != "spec" or id(s) not in projected:
            continue
        gloss_refs = {n for n, t in s.linkdefs.items() if "glossary.md#" in t}
        for i, line, item, start in prose_lines(s):
            for term, (governing, anc, _) in terms.items():
                if item is not None and item.id in governing:
                    continue
                if unlinked_uses(line, term, gloss_refs, start):
                    shape.append(Issue(s.path, i + 1, f"unlinked use of glossary term {term!r}"))  # per file: a package cannot edit files it does not hold

    # with several roots, per-file diagnostics outside the drafts (untouched canonical files, and
    # catalog files a draft replaces) are notes; whole-projection checks always block
    outside = {s.path for s in specs if id(s) not in projected or id(s) in canonical}
    for i in shape:
        i.note = i.path in outside
    return specs, shape + cross


def resolve_link(spec, rel, path, frag, lookup):
    """(file, why) for a link definition's target: the file it names in `lookup` (rel -> parsed
    file; or on disk when the path leaves the roots) and why the target does not resolve there,
    None when it does: the file first, then the anchor in it when there is one."""
    if path:
        found = lookup.get(rel)
        if found is None and rel.startswith(".."):
            disk = (spec.path.parent / path).resolve()
            found = parse(disk) if disk.is_file() else None
        if found is None:
            return None, f"points at {path}, which does not exist"
    else:
        found = spec
    if frag and frag not in heading_anchors(found):
        return found, f"points at #{frag}, which is not in {found.path}"
    return found, None


def projection_fate(frag, found, by_rel):
    """What the drafts did to an anchor the catalog had: retired it in place, moved it to
    another projected file, or removed it."""
    if found is not None and f"{frag}-retired" in heading_anchors(found):
        return "retire"
    for other in by_rel.values():
        if other is not found and frag in heading_anchors(other):
            return f"move to {other.path}"
    return "remove"


def heading_anchors(spec):
    return {anchor(l.lstrip("#").strip()) for l in spec.raw if l.startswith("#")}


def prose_lines(spec):
    """(index, line, item, start) for every spec-prose line: not blank, a heading, a link
    definition, a table header or separator row. item is the Item the line belongs to, None in the
    intro and section lines. Text starts at `start`: after the bold label of a known-difference
    note, after the '>' of its continuation lines, else 0."""
    out, item, by_line = [], None, {it.line - 1: it for it in spec.items}
    lines = spec.raw
    for i, line in enumerate(lines):
        if i in by_line:
            item = by_line[i]
            continue
        if not line.strip() or line.startswith("#") or LINKDEF_RE.match(line) or TABLE_SEP_RE.match(line):
            continue
        if TABLE_ROW_RE.match(line) and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
            continue
        mk = KNOWN_RE.match(line)
        start = mk.start("text") if mk else (1 if line.startswith(">") else 0)
        out.append((i, line, item, start))
    return out


def glossary_terms(glossaries):
    """term -> (governing IDs, anchor, root-relative path of the glossary file holding it) from
    [(rel, parsed glossary)], every glossary.md under a root read as one."""
    terms = {}
    for rel, g in glossaries:
        for term, text, ln in g.items:
            governing = set(re.findall(rf"\[({ID_RE})\]", text))
            terms[term] = (governing, anchor(term), rel)
    return terms


def unlinked_uses(body, term, gloss_refs, start=0):
    """Matches of the term in body, from `start` on, that are not wrapped in a glossary link."""
    out = []
    for m in term_pattern(term).finditer(body, start):
        before, after = body[: m.start()], body[m.end():]
        # linked when the match sits anywhere inside a glossary link's label: "[Appointments
        # stage][g-appointments-stage]" links the shorter term "appointment" too
        lm = re.match(r"[^\]\[]*\]\[([^\]]+)\]", after)
        if before.rfind("[") > before.rfind("]") and lm and lm.group(1) in gloss_refs:
            continue
        out.append(m)
    return out


def link_terms(roots, write_roots=None):
    """Rewrite spec files in place so every occurrence of a glossary term in spec prose is linked.
    Terms come from every glossary under every root (later roots overlaying earlier ones); files
    are rewritten only under `write_roots`, by default the last root alone, so earlier roots (a
    catalog under a package's drafts) are read-only context."""
    by_rel, writable = {}, set()
    for root in roots:
        for p in sorted(Path(root).rglob("*.md")):
            by_rel[p.relative_to(root).as_posix()] = p
            if root in (write_roots if write_roots is not None else roots[-1:]):
                writable.add(p)
    terms = glossary_terms([(rel, parse(p)) for rel, p in by_rel.items() if kind_of(p) == "glossary"])
    changed, per_file = 0, {}  # per_file: path -> term uses linked in it
    for rel, p in by_rel.items():
        if kind_of(p) != "spec" or p not in writable:
            continue
        before = changed
        spec = parse(p)
        lines = spec.raw[:]
        gloss_refs = {n for n, t in spec.linkdefs.items() if "glossary.md#" in t}
        new_defs = {}
        for k, _, item, start in prose_lines(spec):
            for term, (governing, anc, grel) in terms.items():
                if item is not None and item.id in governing:
                    continue
                ref = f"g-{anc}"
                l = lines[k]
                pieces, pos = [], 0
                for m in unlinked_uses(l, term, gloss_refs | set(new_defs), start):
                    pieces.append(l[pos:m.start()] + f"[{m.group(0)}][{ref}]")
                    pos = m.end()
                    changed += 1
                if pieces:
                    lines[k] = "".join(pieces) + l[pos:]
                    # the glossary file as it sits on disk relative to this file: the drafts' copy
                    # when the last root holds one, else the earlier root's
                    new_defs[ref] = f"{Path(os.path.relpath(by_rel[grel].resolve(), p.resolve().parent)).as_posix()}#{anc}"
        if new_defs:
            while lines and not lines[-1].strip():
                lines.pop()
            if lines and not LINKDEF_RE.match(lines[-1]):
                lines.append("")  # definitions stay a block of their own
            lines += [f"[{n}]: {t}" for n, t in new_defs.items() if n not in spec.linkdefs]
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")
            per_file[p] = changed - before
    print(f"linked {changed} term uses")
    return per_file


DOTTED_RE = re.compile(rf"\[({ID_RE})((?:\.\d{{2}})+)\]")
OLD_ENTRY_RE = re.compile(r"^\*\*(?P<term>[^*]+)\*\*\s*[—–-]+\s*(?P<text>.*)$")


def convert(roots):
    """Mechanically rewrite files under the roots from the old shape to the new (decision 16):
    '## <ID>' items to '###', dotted rule citations to dashes in prose and link definitions,
    glossary entries from '**Term** — text' paragraphs to '### Term' headings with the text
    beneath, then link-terms. Reorganizes nothing; idempotent. Prints what changed per file;
    returns the validation issues of the result."""
    summary = {}
    for root in roots:
        for p in sorted(Path(root).rglob("*.md")):
            lines = p.read_text(encoding="utf-8").splitlines()
            kind, out, counts = kind_of(p), [], {"items re-headed": 0, "citations re-dashed": 0, "entries re-headed": 0, "index lines re-dashed": 0}
            for line in lines:
                if kind == "spec" and ITEM_HEAD_RE.match("#" + line) and line.startswith("## "):
                    line = "#" + line
                    counts["items re-headed"] += 1
                if kind == "index" and re.match(r"^- \[[^\]]+\] [—–] ", line):  # the old index bullet's em dashes
                    line = re.sub(r"^(- \[[^\]]+\]) [—–] (?:(`[^`]+`) [—–] )?", lambda m: f"{m.group(1)} -- " + (f"{m.group(2)} -- " if m.group(2) else ""), line)
                    counts["index lines re-dashed"] += 1
                if kind == "glossary":
                    m = OLD_ENTRY_RE.match(line)
                    if m:
                        out += [f"### {m.group('term').strip()}", m.group("text").strip()]
                        counts["entries re-headed"] += 1
                        continue
                line, n = DOTTED_RE.subn(lambda m: f"[{m.group(1)}{m.group(2).replace('.', '-')}]", line)
                counts["citations re-dashed"] += n
                out.append(line)
            if out != lines:
                p.write_text("\n".join(out) + "\n", encoding="utf-8")
            summary[p] = counts
    linked = link_terms(roots, write_roots=roots)  # a migration: every root is rewritten
    for p, counts in summary.items():
        counts["terms linked"] = linked.get(p, 0)
        if any(counts.values()):
            print(f"{p}: " + ", ".join(f"{n} {what}" for what, n in counts.items() if n))
    specs, issues = validate(roots)
    for i in sorted(issues, key=lambda x: (str(x.path), x.line)):
        print(i)
    blocking = [i for i in issues if not i.note]
    print(f"converted {len(summary)} files; {len(specs)} validated, {len(blocking)} issues" + (f", {len(issues) - len(blocking)} notes" if len(blocking) < len(issues) else ""))
    return blocking


def references(target, roots):
    """file:line of every citation of the ID or one of its rules, and, for a rule target, of
    every bold-number pointer to it inside its own item (a cell or rule saying **01**, or
    **01-01** for a nested rule), the rule's own definition line excepted. For a glossary term,
    every linked occurrence ([...][g-<anchor>]) across the roots."""
    is_id = re.match(rf"{ID_RE}(?:[-.]\d{{2}})*$", target)
    if is_id:
        target = target.replace(".", "-")  # dots accepted for dashes
        pat = re.compile(rf"\[{re.escape(target)}(?:[-.]\d{{2}})*\](?!:)")  # dots accepted for dashes in rule citations
    else:
        pat = re.compile(rf"\]\[g-{re.escape(anchor(target))}\]")  # a glossary term: its linked occurrences
    m = re.match(rf"({ID_RE})((?:-\d{{2}})+)$", target)
    parent, pointer = (m.group(1), re.compile(rf"\*\*{m.group(2)[1:]}\*\*(?!-)")) if m else (None, None)
    out = set()  # (path, line number, line)
    for root in roots:
        for p in sorted(Path(root).rglob("*.md")):
            lines = p.read_text(encoding="utf-8").splitlines()
            for i, line in enumerate(lines, 1):
                if pat.search(line) and not LINKDEF_RE.match(line):
                    out.add((str(p), i, line.strip()))
            if parent and kind_of(p) == "spec":
                spec = parse(p)
                starts = [it.line for it in spec.items] + [len(lines) + 1]
                for it, end in zip(spec.items, starts[1:]):
                    if it.id != parent:
                        continue
                    for i in range(it.line + 1, end):
                        line = lines[i - 1]
                        own = RULE_RE.match(line)  # a rule's own "- **NN**" is its definition, not a pointer
                        if pointer.search(own.group("text") if own else line):
                            out.add((str(p), i, line.strip()))
    return [f"{p}:{i}: {l}" for p, i, l in sorted(out)]


# ---------------------------------------------------------------- rendering

RESOLVER = {"linkdefs": {}, "anchors": set(), "base": None}


def collect_texts(spec):
    """ID -> Item, for citation popovers."""
    if spec.kind != "spec":
        return
    for it in spec.items:
        RESOLVER.setdefault("items", {})[it.id] = it


def set_resolver(linkdefs, spec_path):
    """The file whose links are being rendered. A definition pointing outside the roots at a file
    on disk has that file's items collected too, so the citation gets its popover like any other."""
    RESOLVER["linkdefs"] = linkdefs
    RESOLVER["base"] = spec_path.parent
    for target in linkdefs.values():
        path = target.split("#", 1)[0]
        if not path or target.startswith(("http:", "https:", "mailto:")):
            continue
        disk = (spec_path.parent / path).resolve()
        if disk not in RESOLVER.setdefault("collected", set()) and disk.is_file():
            RESOLVER["collected"].add(disk)
            collect_texts(parse(disk))


def href_for(name):
    """Page anchor when the target item is rendered on this page, else the spec file itself."""
    if name.startswith("g-") and name[2:] in RESOLVER["anchors"]:
        return f"#{name[2:]}"
    m = re.match(rf"({ID_RE})(?:-\d{{2}})*$", name)
    if m and anchor(m.group(1)) in RESOLVER["anchors"]:
        return f"#{anchor(m.group(1))}"
    target = RESOLVER["linkdefs"].get(name, "")
    frag = target.split("#", 1)[1] if "#" in target else ""
    if frag and frag in RESOLVER["anchors"]:
        return f"#{frag}"
    if target.startswith("#"):  # page-local: the item may be retired on this page; never the folder
        return f"#{frag}-retired" if f"{frag}-retired" in RESOLVER["anchors"] else f"#{frag}"
    if target and RESOLVER["base"] is not None and not target.startswith(("http:", "https:")):
        path = (RESOLVER["base"] / target.split("#", 1)[0]).resolve()
        try:
            rel = Path(os.path.relpath(path, RESOLVER["out_dir"]))
        except ValueError:
            rel = path
        return rel.as_posix() + (f"#{frag}" if frag else "")
    return target or None


def inline(s, gloss=None):
    s = html.escape(s)
    s = re.sub(r"~~(.+?)~~", r"<del>\1</del>", s, flags=re.S)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)

    def link(m):
        label, ref = m.group(1), m.group(2)
        name = ref if ref else label
        href = href_for(name)
        if gloss and name in gloss:
            tip = f' data-tip="tip-{name}"'
            return (f'<a class="term" href="{href}"{tip}>{label}</a>' if href
                    else f'<span class="term"{tip}>{label}</span>')
        m2 = re.match(rf"({ID_RE})((?:-\d{{2}})*)$", name)
        tip = f' data-tip="tip-{anchor(m2.group(1))}" data-rule="{m2.group(2).lstrip("-")}"' if m2 and m2.group(1) in RESOLVER.get("items", {}) else ""
        return f'<a class="ref" href="{href}"{tip}>{label}</a>' if href else f'<span class="ref"{tip}>{label}</span>'
    s = LINK_USE_RE.sub(link, s)
    return s


GLOSS_LINK_RE = re.compile(r"\[([^\]]+)\]\[g-[^\]]+\]")


def strip_gloss(s):
    """Glossary links are presentation, not content: compare as the bare term."""
    return GLOSS_LINK_RE.sub(r"\1", s)


LINKS = {"old": {}, "new": {}}  # link definitions of the two files being diffed


def target_identity(target):
    """What a link definition points at, independent of where the file sits: the anchor, else
    the file name, else the URL."""
    if "#" in target:
        return target.split("#", 1)[1]
    return Path(target).name if target and not target.startswith(("http:", "https:")) else target


def diff_key(text, side):
    """Text as compared: a glossary link is its bare term; a citation is its label plus the
    identity of its target in that side's link definitions."""
    def sub(m):
        label, ref = m.group(1), m.group(2)
        name = ref if ref else label
        target = LINKS[side].get(name, "")
        if name.startswith("g-") or "glossary.md#" in target:
            return label
        return f"[{label}@{target_identity(target)}]"
    return LINK_USE_RE.sub(sub, text)


def same(old, new):
    """Old text (in the old file's link definitions) reads as new text (in the new file's)."""
    return collapse(diff_key(old, "old")) == collapse(diff_key(new, "new"))


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def tok(s):
    return re.findall(r"\[[^\]]*\](?:\[[^\]]*\])?|\S+", s)


def word_diff(old, new, gloss=None):
    a, b = tok(old), tok(new)
    ka, kb = [diff_key(t, "old") for t in a], [diff_key(t, "new") for t in b]
    sm = difflib.SequenceMatcher(a=ka, b=kb, autojunk=False)
    parts = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            parts.append(inline(" ".join(a[i1:i2]), gloss))
        if op in ("delete", "replace"):
            parts.append('<del class="w">' + inline_old(" ".join(a[i1:i2]), gloss) + "</del>")
        if op in ("insert", "replace"):
            parts.append('<ins class="w">' + inline(" ".join(b[j1:j2]), gloss) + "</ins>")
    return " ".join(parts)


def inline_old(s, gloss=None):
    """Removed text resolves its links through the old file's definitions."""
    current, RESOLVER["linkdefs"] = RESOLVER["linkdefs"], LINKS["old"]
    try:
        return inline(s, gloss)
    finally:
        RESOLVER["linkdefs"] = current


def norm(s):
    return collapse(strip_gloss(s))


def render_table(old: Table, new: Table, gloss, tag=True):
    """Header cells by position, then rows by key column; a kept row that moved among the other
    kept rows is marked as moved."""
    oh, nh = old.header if old else [], new.header if new else []
    changed = False
    if old and new and (len(oh) != len(nh) or not all(same(a, b) for a, b in zip(oh, nh))):
        changed = True
        pairs = zip(oh + [""] * (len(nh) - len(oh)), nh + [""] * (len(oh) - len(nh)))
        head = '<tr class="mod"><th><span class="badge">changed</span>' + "</th><th>".join(word_diff(a, b, gloss) for a, b in pairs) + "</th></tr>"
    else:
        head = "<tr>" + "".join(f"<th>{inline(h, gloss)}</th>" for h in (nh or oh)) + "</tr>"
    o = {r[0]: r for r in (old.rows if old else [])}
    n = {r[0]: r for r in (new.rows if new else [])}
    moved = moved_keys([r[0] for r in old.rows], [r[0] for r in new.rows]) if old and new else set()
    out = ['<table class="t">', head]
    for key in [r[0] for r in (new.rows if new else [])] + [k for k in o if k not in n]:
        orow, nrow = o.get(key), n.get(key)
        if orow and nrow:
            if len(orow) == len(nrow) and all(same(a, b) for a, b in zip(orow, nrow)) and key not in moved:
                out.append("<tr>" + "".join(f"<td>{inline(c, gloss)}</td>" for c in nrow) + "</tr>")
            else:
                changed = True
                cells = []
                for oc, nc in zip(orow + [""] * (len(nrow) - len(orow)), nrow):
                    cells.append(f"<td>{inline(nc, gloss) if same(oc, nc) else word_diff(oc, nc, gloss)}</td>")
                cells[0] = cells[0].replace("<td>", f'<td><span class="badge">{"moved" if key in moved else "changed"}</span>', 1)
                out.append('<tr class="mod">' + "".join(cells) + "</tr>")
        elif nrow:
            changed = True
            t = '<span class="badge">added</span>' if tag else ""
            cells = [f'<td>{t}{inline(nrow[0], gloss)}</td>'] + [f"<td>{inline(c, gloss)}</td>" for c in nrow[1:]]
            out.append(f'<tr class="{"add" if tag else ""}">' + "".join(cells) + "</tr>")
        else:
            changed = True
            cells = [f'<td><span class="badge">removed</span><del>{inline(orow[0], gloss)}</del></td>'] + [f"<td><del>{inline(c, gloss)}</del></td>" for c in orow[1:]]
            out.append('<tr class="rem">' + "".join(cells) + "</tr>")
    out.append("</table>")
    return "".join(out), changed


def moved_keys(old_keys, new_keys):
    """Keys present in both lists that fall outside their longest common order."""
    a = [k for k in old_keys if k in new_keys]
    b = [k for k in new_keys if k in old_keys]
    kept = set()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op == "equal":
            kept |= set(b[j1:j2])
    return set(b) - kept


def render_rules(old_rules, new_rules, parent, gloss, tag=True):
    o = {r.num: r for r in old_rules}
    n = {r.num: r for r in new_rules}
    out, changed = ["<ul>"], False
    for num in sorted(set(o) | set(n)):
        orule, nrule = o.get(num), n.get(num)
        rid = f"{parent}-{num}"
        if orule and nrule:
            if orule.retired != nrule.retired and nrule.retired:
                changed = True
                body = f'<del>{inline(orule.text, gloss)}</del> {inline(nrule.text, gloss)}'
                cls = "ret"
            elif not same(orule.text, nrule.text):
                changed = True
                body, cls = word_diff(orule.text, nrule.text, gloss), "mod"
            else:
                body, cls = inline(nrule.text, gloss), ""
            kids, kc = render_rules(orule.children, nrule.children, rid, gloss) if (orule.children or nrule.children) else ("", False)
            tbl = ""
            for idx in range(max(len(orule.tables), len(nrule.tables))):
                h, tc = render_table(orule.tables[idx] if idx < len(orule.tables) else None,
                                     nrule.tables[idx] if idx < len(nrule.tables) else None, gloss)
                tbl += h
                changed = changed or tc
            changed = changed or kc
        elif nrule:
            changed = True
            body, cls = inline(nrule.text, gloss), ("add" if tag else "")
            kids, _ = render_rules([], nrule.children, rid, gloss, tag) if nrule.children else ("", False)
            tbl = "".join(render_table(None, t, gloss, tag)[0] for t in nrule.tables)
        else:
            changed = True
            body, cls = f'<del>{inline(orule.text, gloss)}</del>', "rem"
            kids = render_rules(orule.children, [], rid, gloss)[0] if orule.children else ""
            tbl = "".join(render_table(t, None, gloss)[0] for t in orule.tables)
        mark = '<span class="badge"></span>' if cls else ""
        out.append(f'<li class="{cls}" data-rid="{rid}">{mark}<span class="rid">{num}</span> {body}{tbl}{kids}</li>')
    out.append("</ul>")
    return "".join(out), changed


def render_item(old: Item, new: Item, gloss, why):
    status, parts = "", []
    if old is None:
        status = "added"
        parts.append("".join(f"<p>{inline(p, gloss)}</p>" for p in new.statement))
        for t in new.tables:
            parts.append(render_table(None, t, gloss, tag=False)[0])
        if new.rules:
            parts.append(render_rules([], new.rules, new.id, gloss, tag=False)[0])
        for k in new.knowns:
            parts.append(f'<blockquote><b>Known difference — {html.escape(k.app)}:</b> {inline(k.text, gloss)}</blockquote>')
    elif new is None:
        status = "missing"
        parts.append(f"<del>{render_plain_item(old, gloss)}</del><p>Present in the catalog but absent from the draft.</p>")
    else:
        changed = False
        if new.retired and not old.retired:
            status = "retired"
            parts.append(f"<del>{render_plain_item(old, gloss)}</del>")
            parts.append("".join(f"<p>{inline(p, gloss)}</p>" for p in new.statement))
            changed = True
        else:
            os_, ns = " ".join(old.statement), " ".join(new.statement)
            if not same(os_, ns):
                changed = True
                parts.append(f"<p>{word_diff(os_, ns, gloss)}</p>")
            else:
                parts.append("".join(f"<p>{inline(p, gloss)}</p>" for p in new.statement))
            for idx in range(max(len(old.tables), len(new.tables))):
                ot = old.tables[idx] if idx < len(old.tables) else None
                nt = new.tables[idx] if idx < len(new.tables) else None
                h, c = render_table(ot, nt, gloss)
                parts.append(h)
                changed = changed or c
            if old.rules or new.rules:
                h, c = render_rules(old.rules, new.rules, new.id, gloss)
                parts.append(h)
                changed = changed or c
            ok = {k.app: k for k in old.knowns}
            nk = {k.app: k for k in new.knowns}
            for app in sorted(set(ok) | set(nk)):
                a, b = ok.get(app), nk.get(app)
                if a and b and same(a.text, b.text):
                    parts.append(f'<blockquote><b>Known difference — {html.escape(app)}:</b> {inline(b.text, gloss)}</blockquote>')
                else:
                    changed = True
                    body = word_diff(a.text if a else "", b.text if b else "", gloss)
                    parts.append(f'<blockquote class="mod"><b>Known difference — {html.escape(app)}:</b> {body}</blockquote>')
            status = "modified" if changed else "unchanged"
    iid = new.id if new else old.id
    aid = anchor(iid) + ("-retired" if (new and new.retired) else "")
    return status, card(status, aid, iid, "".join(parts), why, gloss)


def card(status, aid, name, body, why="", gloss=None):
    """A card: expanded for added and modified, collapsed (details) for everything else, with the
    change's justification under it."""
    w = f'<div class="why"><b>Why</b> {inline(why, gloss)}</div>' if why else ""
    label = f'<span class="id">{html.escape(name)}</span>'
    ident = f' id="{aid}"' if aid else ""
    if status in ("added", "modified"):
        return f'<div class="item {status}"{ident}><div class="head"><span class="badge">{status}</span>{label}</div>{body}{w}</div>'
    badge = "unchanged" if status == "unchanged" else ""
    return f'<details class="item {status}"{ident}><summary><span class="badge">{badge}</span>{label}</summary>{body}{w}</details>'


def render_plain_item(it: Item, gloss):
    parts = ["".join(f"<p>{inline(p, gloss)}</p>" for p in it.statement)]
    for t in it.tables:
        parts.append(render_table(None, t, gloss, tag=False)[0])
    if it.rules:
        parts.append(render_rules([], it.rules, it.id, gloss, tag=False)[0])
    for k in it.knowns:
        parts.append(f'<blockquote><b>Known difference — {html.escape(k.app)}:</b> {inline(k.text, gloss)}</blockquote>')
    return "".join(parts)


def render_popovers(gloss):
    out = []
    for ref, (term, text) in sorted(gloss.items()):
        out.append(f'<template id="tip-{ref}"><div class="pop-head"><span class="id">{html.escape(term)}</span>'
                   f'</div><p>{inline(text, gloss)}</p></template>')
    for iid, it in sorted(RESOLVER.get("items", {}).items()):
        out.append(f'<template id="tip-{anchor(iid)}"><div class="pop-head"><span class="id">{html.escape(iid)}</span>'
                   f'{" <span class=\"badge retired\"></span>" if it.retired else ""}</div>{render_plain_item(it, gloss)}</template>')
    return "".join(out)


@dataclass
class Entry:
    """One diffed thing in a file: its card, what it is, its name, the keys a change-list entry may
    name it by, its status, and where it sits (the draft, or the base file when it is missing)."""
    html: str
    what: str  # file | intro | section | section line | item | glossary entry | index line
    name: str
    keys: set
    status: str  # added | modified | retired | missing | removed | unchanged
    line: int
    path: Path = None
    file: str = ""  # draft-relative path of the file it belongs to


def render_glossary(old: Spec, new: Spec, gloss, changes):
    """Entries by term in the draft's order, its section headings between them, then removed ones."""
    o = {t: (x, ln) for t, x, ln in (old.items if old else [])}
    n = {t: (x, ln) for t, x, ln in new.items}
    out, section = [], None
    for term in [t for t, _, _ in new.items] + [t for t in o if t not in n]:
        ot, nt = o.get(term), n.get(term)
        aid = anchor(term)
        if nt and new.entry_sections.get(term) != section:
            section = new.entry_sections.get(term)
            if section:
                out.append(Entry(f'<h3 class="section">{html.escape(section)}</h3>', "section", section, set(), "unchanged", nt[1]))
        why = why_for(changes, {aid})
        if ot and nt and same(ot[0], nt[0]):
            status, body = "unchanged", f"<p>{inline(nt[0], gloss)}</p>"
        elif ot and nt:
            status, body = "modified", f"<p>{word_diff(ot[0], nt[0], gloss)}</p>"
        elif nt:
            status, body = "added", f"<p>{inline(nt[0], gloss)}</p>"
        else:
            status, body = "removed", f"<p><del>{inline(ot[0], gloss)}</del></p>"
        out.append(Entry(card(status, aid, term, body, why, gloss), "glossary entry", term, {aid}, status, (nt or ot)[1]))
    return out


def render_index(old: Spec, new: Spec, gloss, changes, rel):
    """The reminder line (the index's intro) by text, then index lines by link name, comparing
    the line's text and the identity of its target; unchanged lines get no card."""
    o = {x[0]: x[1:] for x in (old.items if old else [])}
    n = {x[0]: x[1:] for x in new.items}
    out = intro_entries(old, new, gloss, changes, rel)
    fmt = lambda v: (f"`{v[0]}` " if v[0] else "") + v[1]
    for name in [x[0] for x in new.items] + [k for k in o if k not in n]:
        a, b = o.get(name), n.get(name)
        ot, nt = (target_identity(s.linkdefs.get(name, "")) if s else "" for s in (old, new))
        keys = {anchor(name), Path((new if b else old).linkdefs.get(name, "")).name}
        why = why_for(changes, keys, rel)
        if a and b and same(fmt(a), fmt(b)) and ot == nt:
            status, body = "unchanged", ""
        elif a and b:
            retarget = f' <code><del class="w">{html.escape(ot)}</del> <ins class="w">{html.escape(nt)}</ins></code>' if ot != nt else ""
            status, body = "modified", f"<p>{word_diff(fmt(a), fmt(b), gloss)}{retarget}</p>"
        elif b:
            status, body = "added", f"<p>{inline(fmt(b), gloss)}</p>"
        else:
            status, body = "removed", f"<p><del>{inline(fmt(a), gloss)}</del></p>"
        out.append(Entry(card(status, "", name, body, why, gloss) if body else "", "index line", name, keys, status, (b or a)[2]))
    return out


CHANGE_RE = re.compile(r"^- (?P<cid>[RS]\d+) (?P<type>[a-z][a-z -]*?): (?P<identity>.+?)\s*$", re.M)


@dataclass
class Change:
    """One typed change-list entry; see CHANGE LISTS above."""
    cid: str
    line: int
    type: str
    name: str  # the identity without link markup
    keys: set  # what it may be matched to: item or term anchor, draft-relative path, file name
    touched: set  # draft-relative paths and file names its Touches field names
    why: str
    identity: str = ""  # the identity as written, links included
    rule: str = ""  # ID-NN or ID-NN-NN when the identity names a rule, dashes normalized


def parse_changes(text, linkdefs, base_dir, drafts):
    heads = list(CHANGE_RE.finditer(text))
    out = []
    for c, nxt in zip(heads, heads[1:] + [None]):
        block = text[c.end(): nxt.start() if nxt else len(text)]
        j = change_field("Justification", block)
        t = change_field("Touches", block)
        identity = c.group("identity").strip()
        # a linked identity keys a file only when the entry is about a file; "[Stale notice][s-glossary]" keys the term, not glossary.md
        name, keys = identity_keys(identity, linkdefs, base_dir, drafts, paths=bool(re.search(r"file|folder", c.group("type"))) or not LINK_USE_RE.fullmatch(identity))
        touched = set()
        pieces = [m.group(0) for m in LINK_USE_RE.finditer(t)] + re.split(r"[\s,]+|→|->", LINK_USE_RE.sub(" ", t))
        for piece in pieces:
            if piece:
                touched |= identity_keys(piece, linkdefs, base_dir, drafts)[1]
        rm = re.match(rf"({ID_RE})((?:[-.]\d{{2}})+)$", name)
        out.append(Change(c.group("cid"), text.count("\n", 0, c.start()) + 1, c.group("type"), name, keys, touched, norm(j),
                          identity, rm.group(1) + rm.group(2).replace(".", "-") if rm else ""))
    return out


def change_field(name, block):
    """The text of an entry's bold field: from its label to the next bold field label, the next
    list entry, a heading or the first link-definition line, whichever comes first, so the last
    entry's field never runs into the artifact's link definitions."""
    m = re.search(rf"\*\*{name}\*\*\s*(.+?)(?=\n\s*- \*\*|\n- |\n#|\n\[[^\]]+\]:\s|\Z)", block, re.S)
    return m.group(1) if m else ""


def identity_keys(identity, linkdefs, base_dir, drafts, paths=True):
    """(name, keys) for one identity: a link, a bare path or a term. A rule ID keys its item; a
    link with an anchor keys that anchor; with `paths`, a link to a file keys its draft-relative
    path and name."""
    m = LINK_USE_RE.fullmatch(identity)
    label = m.group(1) if m else identity
    target = linkdefs.get(m.group(2) or label, "") if m else identity
    keys = {label, anchor(label)}
    rid = re.match(rf"({ID_RE})(?:[-.]\d{{2}})*$", label)
    if rid:
        keys.add(anchor(rid.group(1)))
    path, frag = target.split("#", 1) if "#" in target else (target, "")
    if frag:
        keys.add(re.sub(r"-retired$", "", frag))
    elif path and paths:
        keys.add(Path(path).name)
        try:
            keys.add((base_dir / path).resolve().relative_to(drafts.resolve()).as_posix())
        except ValueError:
            pass
    return label, keys


def why_for(changes, keys, file=""):
    """The joined justifications of every change-list entry naming one of the keys; when none
    does and `file` is given, of every entry whose Touches names that file (a change riding in
    another entry's Touches carries the owning entry's reason)."""
    hits = [c for c in changes if c.keys & keys and c.why]
    if not hits and file:
        hits = [c for c in changes if c.touched & {file, Path(file).name} and c.why]
    if len(hits) == 1:
        return hits[0].why
    return "; ".join(f"{c.cid} {c.why}" for c in hits)


def parse_authoring(path, drafts):
    """(title, goal, discussion items, changes, link definitions, situations text) of an authoring artifact."""
    if not path:
        return "", "", [], [], {}, ""
    text = Path(path).read_text(encoding="utf-8")
    tm = re.search(r"^# (.+)$", text, re.M)
    title = tm.group(1).strip() if tm else ""
    section = lambda name: (lambda m: m.group(1).strip() if m else "")(re.search(rf"^## {name}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S))
    linkdefs = {m.group("name"): m.group("target") for m in map(LINKDEF_RE.match, text.splitlines()) if m}
    return (title, section("Goal"), parse_discussion(text),
            parse_changes(text, linkdefs, Path(path).resolve().parent, Path(drafts)), linkdefs, LINKDEF_RE.sub("", section("Situations")).strip())


DISC_ITEM_RE = re.compile(r"^- \[(?P<done>[ x])\] (?P<did>D\d+) \[(?P<kind>[^\]]+)\] (?P<title>.+?)\s*$")


def parse_discussion(text):
    """The '## Discussion' section as [(topic, [item])] in artifact order; an item is
    {done, id, kind, title, bullets} and bullets are the item's sub-bullets as written,
    [(text, [child text])], continuation lines joined to their bullet."""
    m = re.search(r"^## Discussion\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return []
    topics, item = [], None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        h = ANY_H3_RE.match(line)
        it = DISC_ITEM_RE.match(line)
        indent = len(line) - len(line.lstrip())
        if h:
            topics.append((h.group(1).strip(), []))
            item = None
        elif it:
            if not topics:
                topics.append(("", []))
            item = {"done": it.group("done") == "x", "id": it.group("did"), "kind": it.group("kind"), "title": it.group("title"), "bullets": []}
            topics[-1][1].append(item)
        elif item is None:
            continue
        elif line.lstrip().startswith("- ") and indent <= 2:
            item["bullets"].append([line.lstrip()[2:].strip(), []])
        elif line.lstrip().startswith("- ") and item["bullets"]:
            item["bullets"][-1][1].append(line.lstrip()[2:].strip())
        elif item["bullets"]:  # continuation line
            tail = item["bullets"][-1]
            if tail[1]:
                tail[1][-1] += " " + line.strip()
            else:
                tail[0] += " " + line.strip()
    return topics


CSS = """
:root{--bg:#fff;--page:#f6f6f7;--fg:#1b1b1b;--muted:#666;--line:#e3e3e3;--ref:#eef3ff;--refc:#2a4e9a;--term:#5a3e9a;
--tag-add:#2e8b3d;--tag-mod:#b7791f;--tag-ret:#c0392b;--tag-neutral:#777}
@media(prefers-color-scheme:dark){:root{--bg:#1e1e1e;--page:#141414;--fg:#eaeaea;--muted:#999;--line:#333;--ref:#1e2a44;--refc:#9db6ff;--term:#c9b3ff;
--tag-add:#3da550;--tag-mod:#d19a2f;--tag-ret:#e05545;--tag-neutral:#888}}
body{margin:auto;padding:24px 16px;background:var(--page);color:var(--fg);font:15px/1.5 -apple-system,system-ui,sans-serif;max-width:900px}
h1{font-size:30px;margin:0 0 4px}.subtitle{font-size:18px;margin:0 0 8px}h3.section{font-size:15px;margin:22px 0 4px;text-transform:uppercase;letter-spacing:.04em}h2 .badge{margin-right:10px;vertical-align:middle;width:14px;height:14px}h2{font-size:24px;margin:44px 0 10px;border-bottom:1px solid var(--line);padding-bottom:6px}
.sum{display:flex;gap:12px;flex-wrap:wrap;margin:12px 0}.sum div{border:1px solid var(--line);border-radius:8px;padding:6px 12px;background:var(--bg)}
.toc{border:1px solid var(--line);border-radius:10px;background:var(--bg);padding:10px 14px;margin:16px 0}.toc .toc-title{font-weight:600;margin-bottom:6px}.toc ol{list-style:none;margin:0;padding:0}.toc li{display:flex;align-items:center;gap:10px;padding:3px 0}.toc a{color:var(--refc);text-decoration:none;font-family:ui-monospace,Menlo,monospace;font-size:14px}.toc a:hover{text-decoration:underline}.toc .n{color:var(--muted);font-size:13px}
.item{border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:12px 0;background:var(--bg);box-shadow:0 1px 3px rgba(0,0,0,.08),0 4px 12px rgba(0,0,0,.06)}
@media(prefers-color-scheme:dark){.item{box-shadow:0 1px 3px rgba(0,0,0,.5),0 4px 12px rgba(0,0,0,.35)}}
.head{display:flex;gap:10px;align-items:center;margin-bottom:4px}
.badge{display:inline-block;width:12px;height:12px;border-radius:3px;background:var(--tag-neutral);vertical-align:middle;font-size:0;color:transparent;overflow:hidden;flex:none}
.added .badge,.badge.added,tr.add .badge,li.add>.badge{background:var(--tag-add)}
.modified .badge,.badge.modified,tr.mod .badge,li.mod>.badge{background:var(--tag-mod)}
.retired .badge,.missing .badge,.removed .badge,.badge.retired,.badge.missing,tr.rem .badge,li.rem>.badge,li.ret>.badge{background:var(--tag-ret)}
.badge.unchanged{background:var(--tag-neutral)}
.sum div{display:flex;align-items:center;gap:8px}
.id{font-weight:700;font-family:ui-monospace,Menlo,monospace}
.retired .id,.removed .id,.missing .id,li.rem .rid,li.ret .rid{text-decoration:line-through;color:var(--muted)}
.rid{font-weight:700;font-family:ui-monospace,Menlo,monospace;margin-right:4px}
a.ref{background:var(--ref);color:var(--refc);border-radius:4px;padding:0 4px;font-family:ui-monospace,Menlo,monospace;font-size:12.5px;white-space:nowrap;text-decoration:none}a.ref:hover{text-decoration:underline}
span.ref{font-family:ui-monospace,Menlo,monospace;font-size:12.5px;color:var(--muted);white-space:nowrap}
span.term{color:var(--muted);border-bottom:1px dotted var(--muted)}
.item:target{outline:2px solid var(--refc)}
details.item{padding:6px 14px}details.item summary{cursor:pointer;list-style:none;display:flex;gap:10px;align-items:center}details.item.unchanged summary .badge{background:var(--tag-neutral)}details.item[open]{padding-bottom:10px}details.item[open] summary{margin-bottom:4px}
.term,a.term{color:var(--term);border-bottom:1px dotted var(--term);cursor:pointer;text-decoration:none}a.term:hover{border-bottom-style:solid}
del{text-decoration:line-through;color:var(--muted)}del .ref,del .term{opacity:.6}
del.w{color:inherit;background:#fbe3e3;border-radius:3px;padding:0 2px}ins.w{text-decoration:none;background:#dcf4dc;border-radius:3px;padding:0 2px}
@media(prefers-color-scheme:dark){del.w{background:#4a2020}ins.w{background:#1f3f22}}
blockquote{border-left:3px solid var(--line);margin:8px 0;padding:2px 12px;color:var(--muted)}
.why{font-size:13px;color:var(--muted);border-top:1px dashed var(--line);margin-top:8px;padding-top:6px}
p{margin:6px 0}
ul{padding-left:18px;margin:6px 0}li{margin:2px 0}
table.t{border-collapse:collapse;width:100%;margin:8px 0}table.t td,table.t th{border-bottom:1px solid var(--line);padding:4px 8px;text-align:left;vertical-align:top}
table.t td .badge,table.t th .badge{margin-right:6px}li>.badge{margin-right:4px}
.file-why{font-size:13px;color:var(--muted);margin:0 0 8px}
.item.request .status{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;border:1px solid var(--line);border-radius:999px;padding:1px 8px}.item.request .title{font-weight:600}
p.intro{margin:4px 0 10px}p.intro .badge{margin-right:8px}
#pop{position:absolute;z-index:10;max-width:560px;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18);padding:10px 14px;font-size:14px;display:none}
#pop .pop-head{margin-bottom:4px}#pop li.hit{outline:2px solid var(--refc);border-radius:4px}
"""


BUCKET = {"added": "added", "modified": "modified", "retired": "retired", "missing": "retired", "removed": "retired", "unchanged": "unchanged"}


def render_tree(bases, drafts, gloss, changes, prefix=""):
    """Diff every file under drafts against the first base root that has it.
    Returns (sections, toc, totals, entries); entries include one per file."""
    sections, toc, all_entries = [], [], []
    totals = {"added files": 0, "added": 0, "modified": 0, "retired": 0, "unchanged": 0}
    for draft in sorted(drafts.rglob("*.md")):
        rel = draft.relative_to(drafts).as_posix()
        new = parse(draft)
        base = next((b / rel for b in bases if (b / rel).exists()), None)
        old = parse(base) if base else None
        set_resolver(new.linkdefs, draft.resolve())
        LINKS["old"], LINKS["new"] = (old.linkdefs if old else {}), new.linkdefs
        if new.kind == "glossary":
            entries = render_glossary(old, new, gloss, changes)
        elif new.kind == "index":
            entries = render_index(old, new, gloss, changes, rel)
        else:
            entries = render_spec(old, new, gloss, changes, prefix, rel)
        for e in entries:
            e.path, e.file = (base if e.status == "missing" else draft), rel
            if e.what in ("item", "glossary entry", "index line"):
                totals[BUCKET[e.status]] += 1
        n_changed = sum(1 for e in entries if e.status != "unchanged")
        kind = "added" if old is None else ("modified" if n_changed else "unchanged")
        all_entries += [Entry("", "file", rel, {rel, Path(rel).name}, kind, 1, draft, rel)] + entries
        if kind == "unchanged":
            continue
        totals["added files"] += kind == "added"
        fid = f"{prefix}file-" + anchor(rel)
        toc.append((fid, kind, rel, n_changed))
        body = f'<h2 id="{fid}"><span class="badge {kind}">{kind}</span> {html.escape(rel)}</h2>'
        why = why_for(changes, {rel, Path(rel).name})
        if why:
            body += f'<p class="file-why"><b>Why</b> {inline(why, gloss)}</p>'
        if new.issues:
            body += '<p class="file-why">Validation: ' + "; ".join(html.escape(str(i)) for i in new.issues) + "</p>"
        body += "".join(e.html for e in entries)
        sections.append(body)
    return sections, toc, totals, all_entries


def render_spec(old: Spec, new: Spec, gloss, changes, prefix, rel):
    """Entries for a spec file: intro, section headings with their lines, items in file order,
    then items the base has that the draft lacks. A changed intro or section line carries the
    reason of the entry whose Touches names the file."""
    o = {it.id: it for it in old.items} if old else {}
    old_sections = ({it.section for it in old.items} | set(old.sections)) if old else set()
    out = intro_entries(old, new, gloss, changes, rel)
    section = None
    for it in new.items:
        if it.section != section:
            section = it.section
            if section:
                head = next((i for i, l in enumerate(new.raw) if H2_RE.match(l) and H2_RE.match(l).group(1).strip() == section), 0)
                out.append(Entry(f'<h3 class="section">{html.escape(section)}</h3>', "section", section, set(), "unchanged", head + 1))
                desc_new = new.sections.get(section, "")
                desc_old = old.sections.get(section, "") if old else ""
                if section in old_sections and not same(desc_old, desc_new):
                    out.append(Entry(prose_card(word_diff(desc_old, desc_new, gloss), True, why_for(changes, {anchor(section)}, rel), gloss), "section line", section, {anchor(section)}, "modified", prose_line(new.raw, head)))
                elif desc_new:
                    out.append(Entry(prose_card(inline(desc_new, gloss)), "section line", section, {anchor(section)}, "unchanged", prose_line(new.raw, head)))
        status, h = render_item(o.get(it.id), it, gloss, why_for(changes, {anchor(it.id)}))
        if prefix:
            h = h.replace(' id="', f' id="{prefix}', 1)
        out.append(Entry(h, "item", it.id, {anchor(it.id)}, status, it.line))
    for k, it in o.items():
        if k not in {it.id for it in new.items}:
            out.append(Entry(render_item(it, None, gloss, why_for(changes, {anchor(k)}))[1], "item", k, {anchor(k)}, "missing", it.line))
    return out


def intro_entries(old, new, gloss, changes, rel):
    """The file's intro (a spec file's opening paragraphs, an index file's reminder line) diffed
    by text: a modified intro is a prose card with its square, carrying the reason of the entry
    whose Touches names the file."""
    intro_new, intro_old = " ".join(new.intro), " ".join(old.intro) if old else ""
    if old and not same(intro_old, intro_new):
        return [Entry(prose_card(word_diff(intro_old, intro_new, gloss), True, why_for(changes, {"intro"}, rel), gloss), "intro", "intro", {"intro"}, "modified", prose_line(new.raw, 0))]
    if intro_new:
        return [Entry(prose_card(inline(intro_new, gloss)), "intro", "intro", {"intro"}, "unchanged", prose_line(new.raw, 0))]
    return []


def prose_card(body, modified=False, why="", gloss=None):
    if not modified:
        return f'<p class="intro">{body}</p>'
    w = f'<div class="why"><b>Why</b> {inline(why, gloss)}</div>' if why else ""
    return f'<p class="intro modified"><span class="badge modified"></span>{body}</p>{w}'


def prose_line(raw, after):
    """1-based line of the first non-blank line after index `after`."""
    return next((i + 1 for i in range(after + 1, len(raw)) if raw[i].strip()), after + 1)


def parse_request(path, drafts):
    """request.md: 'Label: value' header lines, a title, '## Goal', and '## Requested Changes' in the
    same typed format as a package's change list. Returns (fields, title, goal, changes, linkdefs)."""
    text = path.read_text(encoding="utf-8")
    fields, body = {}, []
    for line in text.splitlines():
        m = re.match(r"^(Change Request Status|Reviewer Response):\s*(.*)$", line)
        if m and not body:
            fields[m.group(1)] = m.group(2).strip()
        else:
            body.append(line)
    text = "\n".join(body)
    tm = re.search(r"^# (.+)$", text, re.M)
    title = tm.group(1).strip() if tm else ""
    gm = re.search(r"^## Goal\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    goal = norm(LINKDEF_RE.sub("", gm.group(1))) if gm else ""
    linkdefs = {m.group("name"): m.group("target") for m in map(LINKDEF_RE.match, body) if m}
    return fields, title, goal, parse_changes(text, linkdefs, path.resolve().parent, Path(drafts)), linkdefs


def page_shell(title, summary_totals, head, sections, gloss, subtitle=""):
    sub = f'<p class="subtitle">{html.escape(subtitle)}</p>' if subtitle else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style></head><body>
<h1>{html.escape(title)}</h1>{sub}
<div class="sum"><div><span class="badge added"></span><b>{summary_totals['added']}</b> added</div>
<div><span class="badge modified"></span><b>{summary_totals['modified']}</b> modified</div>
<div><span class="badge retired"></span><b>{summary_totals['retired']}</b> retired or removed</div>
<div><span class="badge unchanged"></span><b>{summary_totals['unchanged']}</b> unchanged</div>
<div><span class="badge added"></span><b>{summary_totals['added files']}</b> added files</div></div>
{head}{''.join(sections)}
{render_popovers(gloss)}
<div id="pop"></div>
<script>
(function(){{var pop=document.getElementById('pop'),timer;
function show(a){{var t=document.getElementById(a.dataset.tip);if(!t)return;pop.innerHTML='';pop.appendChild(t.content.cloneNode(true));
var rule=a.dataset.rule;if(rule){{var rid=a.textContent.trim();var li=pop.querySelector('[data-rid="'+rid+'"]');if(li)li.classList.add('hit');}}
var r=a.getBoundingClientRect();pop.style.display='block';var top=r.bottom+window.scrollY+6,left=Math.min(r.left+window.scrollX,window.scrollX+document.documentElement.clientWidth-pop.offsetWidth-16);
pop.style.top=top+'px';pop.style.left=Math.max(8,left)+'px';}}
document.addEventListener('mouseover',function(e){{var a=e.target.closest('[data-tip]');if(a){{clearTimeout(timer);show(a);}}}});
document.addEventListener('mouseout',function(e){{if(e.target.closest('[data-tip]'))timer=setTimeout(function(){{pop.style.display='none';}},150);}});
pop.addEventListener('mouseenter',function(){{clearTimeout(timer);}});pop.addEventListener('mouseleave',function(){{pop.style.display='none';}});
}})();
function openTarget(){{var el=location.hash&&document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!el)return;var d=el.closest('details');while(d){{d.open=true;d=d.parentElement&&d.parentElement.closest('details');}}el.scrollIntoView();}}
addEventListener('hashchange',openTarget);openTarget();
</script>
</body></html>"""


def toc_html(toc):
    if not toc:
        return ""
    return '<nav class="toc"><div class="toc-title">Documents</div><ol>' + "".join(
        f'<li><span class="badge {k}"></span><a href="#{fid}">{html.escape(rel)}</a><span class="n">{n} changed</span></li>'
        for fid, k, rel, n in toc) + "</ol></nav>"


def prepare(catalog, bases, drafts, out):
    """Glossary and popover texts from the catalog and every base, drafts winning; page anchors
    from the drafts alone, since only their files are rendered on the page (drafts may be None)."""
    gloss = {}
    RESOLVER["out_dir"] = Path(out).resolve().parent
    for root in [catalog] + list(bases) + ([drafts] if drafts else []):
        for g in sorted(root.rglob("glossary.md")):  # every glossary.md under a root is part of the glossary
            for term, text, _ in parse(g).items:
                gloss[f"g-{anchor(term)}"] = (term, text)
        for d in sorted(root.rglob("*.md")):
            sp = parse(d)
            RESOLVER.setdefault("collected", set()).add(d.resolve())
            collect_texts(sp)
            if root is drafts:
                if sp.kind == "spec":
                    RESOLVER["anchors"] |= {anchor(it.id) + ("-retired" if it.retired else "") for it in sp.items}
                elif sp.kind == "glossary":
                    RESOLVER["anchors"] |= {anchor(t) for t, _, _ in sp.items}
    return gloss


DRAFT_FOLDERS = ("proposed-product-specs", "proposed-design-specs")


def render_request(catalog, package_drafts, request_dir, out):
    """A change request's own page: its header and body, then its proposed drafts diffed against the package."""
    catalog, package_drafts, request_dir = Path(catalog), Path(package_drafts), Path(request_dir)
    out = Path(out) if out else request_dir / "request-review.html"
    cr_drafts = next((request_dir / d for d in DRAFT_FOLDERS if (request_dir / d).exists()), None)
    fields, title, goal, changes, linkdefs = parse_request(request_dir / "request.md", cr_drafts or package_drafts)
    gloss = prepare(catalog, [package_drafts], cr_drafts, out)
    set_resolver(linkdefs, (request_dir / "request.md").resolve())
    status = fields.get("Change Request Status", "Proposed")
    response = fields.get("Reviewer Response", "")
    head = (f'<div class="item request"><div class="head"><span class="status">{html.escape(status)}</span>'
            f'<span class="title">{html.escape(title)}</span></div>'
            + (f"<p>{inline(goal, gloss)}</p>" if goal else ""))
    head += f'<div class="why"><b>Reviewer response</b> {inline(response, gloss) if response else "<i>none yet</i>"}</div></div>'
    sections, toc, totals = [], [], {"added files": 0, "added": 0, "modified": 0, "retired": 0, "unchanged": 0}
    if cr_drafts:
        sections, toc, totals, _ = render_tree([package_drafts, catalog], cr_drafts, gloss, changes)
    else:
        # no drafts: one card per requested change, so the page still says what is asked
        sections = [f'<div class="item request"><div class="head"><span class="status">{html.escape(c.type)}</span>'
                    f'<span class="id">{inline(c.identity, gloss)}</span></div>'
                    f'<div class="why"><b>Why</b> {inline(c.why, gloss) if c.why else "<i>none given</i>"}</div></div>' for c in changes]
    page = page_shell(f"Change Request: {request_dir.name}", totals, head + toc_html(toc), sections, gloss,
                      subtitle=f"Change Package: {package_id(package_drafts)}")
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out}: {totals}")


def package_id(drafts):
    """The change id: the folder above product-specs/, design-specs/ or the legacy requirements/,
    else the drafts' parent."""
    parent = drafts.resolve().parent
    return parent.parent.name if parent.name in ("product-specs", "design-specs", "requirements") else parent.name


def render(catalog, drafts, authoring, out, no_authoring=False, bases=()):
    """bases: further base roots layered over the catalog in order, each overlaying the last, so a
    package can be drafted on another open package's drafts (the drafts diff against the top layer
    that holds each file)."""
    catalog, drafts, bases = Path(catalog), Path(drafts), [Path(b) for b in bases]
    design = drafts.name == "proposed-design-specs"
    out = Path(out) if out else drafts.parent / ("design-specs-review.html" if design else "product-specs-review.html")
    if not authoring and not no_authoring:
        names = ["design-specs-authoring.md"] if design else ["product-specs-authoring.md", "requirements-authoring.md"]
        authoring = next((drafts.parent / n for n in names if (drafts.parent / n).exists()), None)
        if not authoring:
            sys.exit(f"no authoring artifact ({' or '.join(names)}) in {drafts.parent}; pass --authoring FILE, or --no-authoring for a bare comparison")
    title, goal, disc, changes, linkdefs, situations = parse_authoring(authoring, drafts)
    gloss = prepare(catalog, bases, drafts, out)
    # everything from the authoring artifact resolves its links through the artifact's own
    # definitions, so it is rendered before the drafts (whose loop re-sets the resolver per file)
    if authoring:
        set_resolver(linkdefs, Path(authoring).resolve())
    head, discussion = "", ""
    if title or goal:
        items = [it for _, its in disc for it in its]
        n_open = sum(1 for it in items if not it["done"])
        n_done = len(items) - n_open
        state = "ready for promotion" if items and not n_open else (f"{n_open} open" if n_open else "no discussion items")
        foot = f"Discussion: {n_done} approved, {n_open} open" if items else "No discussion items"
        head += (f'<div class="item request"><div class="head"><span class="status">{html.escape(state)}</span>'
                 f'<span class="title">{html.escape(title)}</span></div>'
                 + (f"<p>{inline(goal, gloss)}</p>" if goal else "")
                 + f'<div class="why"><b>{foot}</b></div></div>')
    if situations:
        head += f'<h2>Situations</h2><div class="item request">{render_markdown(situations, gloss)}</div>'
    if disc:
        discussion = "<h2>Discussion</h2>" + "".join(
            (f'<h3 class="section">{html.escape(topic)}</h3>' if topic else "") + "".join(render_discussion_item(it, gloss) for it in items)
            for topic, items in disc)
    sections, toc, totals, _ = render_tree([*reversed(bases), catalog], drafts, gloss, changes)
    head += toc_html(toc) + discussion
    page = page_shell(f"Change Package: {package_id(drafts)}", totals, head, sections, gloss)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out}: {totals}")


def render_discussion_item(it, gloss):
    """A discussion item in full: square, ID, kind, title, then its sub-bullets as written."""
    status = "added" if it["done"] else "modified"
    head = (f'<div class="head"><span class="badge {status}"></span><span class="id">{it["id"]}</span>'
            f'<span class="status">{html.escape(it["kind"])}</span><span class="title">{inline(it["title"], gloss)}</span></div>')
    bullets = "".join(
        f"<li>{inline(text, gloss)}" + (f"<ul>{''.join(f'<li>{inline(c, gloss)}</li>' for c in kids)}</ul>" if kids else "") + "</li>"
        for text, kids in it["bullets"])
    return f'<div class="item request" id="{it["id"].lower()}">{head}{f"<ul>{bullets}</ul>" if bullets else ""}</div>'


def render_markdown(text, gloss):
    """A section as written: '###' headings, one- or two-level bullets, paragraphs; citations linked."""
    out, para, stack = [], [], 0  # stack: open <ul> depth

    def close(to):
        nonlocal stack
        while stack > to:
            out.append("</ul>")
            stack -= 1

    def flush():
        nonlocal para
        if para:
            out.append(f"<p>{inline(' '.join(para), gloss)}</p>")
            para = []

    for line in text.splitlines():
        h = ANY_H3_RE.match(line)
        b = re.match(r"^( *)- (.*)$", line)
        if not line.strip():
            flush()
            continue
        if h:
            flush(); close(0)
            out.append(f'<h3 class="section">{html.escape(h.group(1).strip())}</h3>')
        elif b:
            flush()
            depth = 2 if len(b.group(1)) >= 2 else 1
            close(depth)
            while stack < depth:
                out.append("<ul>")
                stack += 1
            out.append(f"<li>{inline(b.group(2).strip(), gloss)}</li>")
        elif stack and line.startswith(" "):  # continuation of the last bullet
            out[-1] = out[-1][:-5] + " " + inline(line.strip(), gloss) + "</li>"
        else:
            close(0)
            para.append(line.strip())
    flush(); close(0)
    return "".join(out)


# ---------------------------------------------------------------- list-matches-diff

def kind_matches(change_type, what):
    """A change entry names only things of its own kind, so a glossary term, an item and an index
    line that share a name never collide: a glossary-typed entry names glossary entries, an
    index-line entry names index lines, a file or folder entry names files (an index line rides on
    it through Touches, never as its identity), and every other type names items."""
    if "glossary" in change_type:
        return what == "glossary entry"
    if "index" in change_type:
        return what == "index line"
    if re.search(r"file|folder", change_type):
        return what == "file"
    return what == "item"


def check_changes(catalog, drafts, authoring, bases=()):
    """Every added, modified, retired or missing item, glossary entry or index line in the
    projection has a change-list entry naming it; every added file has one naming it or its path
    in Touches (its contents ride on it); intro, section and index lines may also ride in Touches;
    no entry names something unchanged or absent."""
    catalog, drafts, authoring, bases = Path(catalog), Path(drafts), Path(authoring), [Path(b) for b in bases]
    _, _, _, changes, _, _ = parse_authoring(authoring, drafts)
    gloss = prepare(catalog, bases, drafts, drafts.parent / "product-specs-review.html")
    _, _, _, entries = render_tree([*reversed(bases), catalog], drafts, gloss, changes)
    added_files = {e.name for e in entries if e.what == "file" and e.status == "added"}
    rules = {rid for d in drafts.rglob("*.md") for rid in rule_ids(parse(d))}
    bad_rules = [c for c in changes if c.rule and c.rule not in rules]
    issues = [Issue(authoring, c.line, f"{c.cid} names rule {c.rule}, which is not in the drafts") for c in bad_rules]
    changes = [c for c in changes if c not in bad_rules]
    matched, covering, actual = set(), set(), {}  # actual: cid -> {(what, name, status)} it names
    for e in entries:
        if e.what == "section":
            continue
        # a file-typed entry names the file itself, never that file's index line
        hits = [c for c in changes if c.keys & e.keys and kind_matches(c.type, e.what)]
        if e.status == "unchanged":
            issues += [Issue(authoring, c.line, f"{c.cid} names {describe(e.what, e.name)}, which is unchanged") for c in hits]
            matched |= {c.cid for c in hits}
            continue
        matched |= {c.cid for c in hits}
        for c in hits:
            if e.what != "file" or re.search(r"file|folder", c.type):  # a file's status counts for file-typed entries
                actual.setdefault(c.cid, set()).add((e.what, e.name, e.status))
        if hits or (e.file in added_files and e.what != "file") or (e.what == "file" and e.status == "modified"):
            continue
        riders = [c for c in changes if c.touched & {e.file, Path(e.file).name}] if e.what in ("file", "intro", "section line", "index line") else []
        covering |= {c.cid for c in riders}
        if not riders:
            issues.append(Issue(e.path, e.line, f"{describe(e.what, e.name)} is {e.status} but no change-list entry names it"))
    # a file or folder entry may cover its files through Touches alone; anything else must name a change
    issues += [Issue(authoring, c.line, f"{c.cid} names {c.name}, which is not in the drafts") for c in changes
               if c.cid not in matched and not (c.cid in covering and re.search(r"file|folder", c.type))]
    # the declared operation must match what the projection shows; a moved item is missing from
    # one file and added in another, and a modify entry may ride on the move when its text changed
    moves = [c for c in changes if c.type.split()[0] == "move"]
    for c in changes:
        if c.cid not in actual:
            continue
        op = c.type.split()[0]
        found = {s for _, _, s in actual[c.cid]}
        if re.search(r"rule|sub-item|known-difference", c.type):  # sub-item: older name for rule
            ok = found <= {"modified"}  # a change inside an existing item shows as that item modified
        elif op == "move" or (op == "modify" and any(c.keys & m.keys for m in moves)):
            ok = found in ({"added", "missing"}, {"added", "removed"})  # an item leaves a file; a glossary entry leaves a glossary file
        else:
            ok = found <= {"add": {"added"}, "modify": {"modified"}, "retire": {"retired", "removed", "missing"}}.get(op, set())
        if not ok:
            seen_ = "; ".join(f"{describe(w, n)} is {s}" for w, n, s in sorted(actual[c.cid]))
            issues.append(Issue(authoring, c.line, f"{c.cid} declares {op} but {seen_}"))
    for m in moves:
        if {s for _, _, s in actual.get(m.cid, ())} not in ({"added", "missing"}, {"added", "removed"}):
            continue  # not a move; reported above
        for what, name in {(w, n) for w, n, _ in actual[m.cid] if w in ("item", "glossary entry")}:
            modifies = [c for c in changes if c.type.split()[0] == "modify" and c.keys & m.keys]
            status = moved_item_status(name, catalog, drafts) if what == "item" else moved_entry_status(name, catalog, drafts)
            if status == "modified" and not modifies:
                issues.append(Issue(authoring, m.line, f"{m.cid} declares move but {what} {name} also changed; a modify entry is needed"))
            for c in modifies if status == "unchanged" else []:
                issues.append(Issue(authoring, c.line, f"{c.cid} declares modify but moved {what} {name} is unchanged"))
    return issues


def describe(what, name):
    """'item X-01', 'index line notes'; the intro is just 'intro'."""
    return what if name == what else f"{what} {name}"


def moved_entry_status(term, catalog, drafts):
    """Whether a glossary entry that left one glossary file for another changed on the way: the
    catalog's text against the draft's, keyed by term across files."""
    def find(root):
        for g in sorted(Path(root).rglob("glossary.md")):
            for t, text, _ in parse(g).items:
                if t == term:
                    return text
        return None
    old, new = find(catalog), find(drafts)
    return "unchanged" if old is None or new is None or same(old, new) else "modified"


def moved_item_status(iid, catalog, drafts):
    """Whether an item that left one file for another changed on the way: the catalog's copy
    diffed against the draft's, each read with its own link definitions."""
    def find(root):
        for p in sorted(Path(root).rglob("*.md")):
            s = parse(p)
            for it in (s.items if s.kind == "spec" else []):
                if it.id == iid:
                    return it, s
        return None, None
    old, os_ = find(catalog)
    new, ns = find(drafts)
    if not old or not new:
        return "unchanged"
    LINKS["old"], LINKS["new"] = os_.linkdefs, ns.linkdefs
    return render_item(old, new, {}, "")[0]


def rule_ids(spec):
    """Every ID-NN and ID-NN-NN a spec file defines."""
    if spec.kind != "spec":
        return []
    return [f"{it.id}-{r.num}" + (f"-{c.num}" if c else "") for it in spec.items for r in it.rules for c in [None] + r.children]


# ---------------------------------------------------------------- cli

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate"); v.add_argument("roots", nargs="+")
    r = sub.add_parser("references"); r.add_argument("id"); r.add_argument("roots", nargs="+")
    lt = sub.add_parser("link-terms"); lt.add_argument("roots", nargs="+")
    cv = sub.add_parser("convert"); cv.add_argument("roots", nargs="+")
    d = sub.add_parser("render"); d.add_argument("--catalog", required=True); d.add_argument("--drafts", required=True)
    d.add_argument("--base", action="append", default=[], help="a further base root layered over the catalog (repeatable, later wins)")
    d.add_argument("--authoring"); d.add_argument("--no-authoring", action="store_true"); d.add_argument("--out")
    q = sub.add_parser("render-request"); q.add_argument("--catalog", required=True); q.add_argument("--package-drafts", required=True)
    q.add_argument("--request", required=True); q.add_argument("--out")
    c = sub.add_parser("check-changes"); c.add_argument("--catalog", required=True); c.add_argument("--drafts", required=True)
    c.add_argument("--authoring", required=True); c.add_argument("--base", action="append", default=[], help="a further base root layered over the catalog (repeatable, later wins)")
    a = ap.parse_args(argv)
    if a.cmd == "validate":
        specs, issues = validate(a.roots)
        for i in sorted(issues, key=lambda x: (str(x.path), x.line)):
            print(i)
        blocking = [i for i in issues if not i.note]
        print(f"{len(specs)} files, {len(blocking)} issues" + (f", {len(issues) - len(blocking)} notes outside the projection" if len(blocking) < len(issues) else ""))
        return 1 if blocking else 0
    if a.cmd == "check-changes":
        issues = check_changes(a.catalog, a.drafts, a.authoring, a.base)
        for i in sorted(issues, key=lambda x: (str(x.path), x.line)):
            print(i)
        print(f"{len(issues)} issues")
        return 1 if issues else 0
    if a.cmd == "link-terms":
        link_terms(a.roots)
        return 0
    if a.cmd == "convert":
        return 1 if convert(a.roots) else 0
    if a.cmd == "references":
        for line in references(a.id, a.roots):
            print(line)
        return 0
    if a.cmd == "render":
        if a.authoring and a.no_authoring:
            ap.error("--authoring and --no-authoring exclude each other")
        render(a.catalog, a.drafts, a.authoring, a.out, a.no_authoring, a.base)
        return 0
    if a.cmd == "render-request":
        render_request(a.catalog, a.package_drafts, a.request, a.out)
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
