Managed-By: skai
Managed-Id: guide.spec-file-shape
Managed-Source: Guides/Core/spec-file-shape.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-26

# Spec File Shape

Print `📖 SKAI guide: spec-file-shape` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

The shape product spec and design spec files share. Content guides own what a file says; this one owns layout.

## Example

```markdown
# Reminders

A reminder is a time attached to a note.

## States

One orientation line, not binding.

### REMIND-01
A reminder is in exactly one of these states.

| State | Meaning |
| --- | --- |
| pending | Its time has not arrived |
| overdue | Its time has passed, unacknowledged |
| acknowledged | Someone acted on it ([NOTE-05]) |

- **01** A reminder that fires while the app is closed becomes overdue and stays so until acknowledged or thirty days pass.
  - **01** After thirty days it is removed from the note and no longer counted.
- **02** (retired) Thirty-day removal is now rule **01-01**.

> **Known difference — Android:** Overdue reminders never expire. Tracked in [expiry-fix].

### REMIND-02 (retired)
The overdue state is now defined in [REMIND-01].

[NOTE-05]: note.md#note-05
[REMIND-01]: #remind-01
[expiry-fix]: https://example.com/i/123
```

## Elements

In file order.

**Title.** One `#` line, Title Case; no other `#`.

**Intro.** Paragraphs before the first `##` or `###`; orientation, never binding.

**Section.** A `##` heading with a Title Case name and no ID; optional; may open with one orientation line. Never cited.

**Item.** A `###` heading carrying only the ID, optionally ` (retired)`. Up to the next heading, in this order: a statement, any mix of tables and rules, [gap footnotes](spec-file-gaps.md), any known differences.

**Statement.** The paragraph(s) under the item heading. Required even when a table holds the detail; a retired item's says what superseded it.

**Rule.** A bullet `- **NN**`, two digits zero-padded, numbered from `01` in order. Rules nest one level by two-space indentation, numbered `01` again within the parent. Cited as `ID-NN`, nested `ID-NN-NN`. Append-only: a withdrawn rule keeps its number and reads `- **NN** (retired) <explanation>`. A rule or table cell points at a top-level rule of its item by the bare bold number, at a nested one as `**01-01**`.

**Table.** A pipe table with header and separator rows. The first column is the key, nonempty and unique within the table. Rows have no IDs and are not cited; the item owns the claim. Row order binds only when the statement says so. A table follows the statement, or a rule it supports; its rows start with two spaces for a top-level rule, four for a nested rule.

**Known difference.** A blockquote `> **Known difference — <app or platform>:** ...` after the rules: observed, never a requirement.

**Link definitions.** All `[name]: target` lines, grouped at the file's end; every `[name]` used is defined and every definition used. Item citations use the ID as the name; rule citations use the parent item's anchor, `[REMIND-01-01]: reminders.md#remind-01`; glossary citations link the entry's heading, `[overdue reminder][g-overdue-reminder]` with `[g-overdue-reminder]: glossary.md#overdue-reminder`.

## Glossary File

`glossary.md` — every one under the root reads as one glossary — a title, then entries, alphabetical within the file or its optional `##` sections, each a `###` heading carrying the term in sentence case, one paragraph and an optional final Also called note:

```markdown
### Overdue reminder
A reminder whose time has passed unacknowledged ([REMIND-01]).

> **Also called:** missed reminder (support); late alert (web app).
```

The heading is the anchor (`#overdue-reminder`); the paragraph ends by linking the governing items. The note lists, in the example's form, names others use, so an agent reading inputs recognizes the term; spec prose never links or uses them.

**Linking terms.** Spec prose, not glossary or index text, links every occurrence of a glossary term — the link is what marks a defined term; the items an entry names as governing it are exempt. Terms stay in sentence case. A term used in its ordinary sense is reworded or linked.

## Index File

`_<folder>.md`: a title, one reminder line, a bullet per file or folder, their link definitions:

```markdown
# Features

What each feature file answers.

- [reminders] -- `REMIND-` -- What states a reminder has and what happens when one is missed
- [widgets] -- What the widget files answer

[reminders]: reminders.md
[widgets]: widgets/_widgets.md
```

File lines carry prefixes in backticks; folder lines none. An app's index also lists the feature files it offers.

## IDs And Citations

- Item ID: `<PREFIX>-<NN>` for product specs, `UI-<PREFIX>-<NN>` for design specs; the prefix uppercase letters, digits and hyphens, two characters or more, each part starting with a letter (`A11Y`), registered on the file's index line; `NN` two digits zero-padded, three past 99; unique across the catalog.
- Anchors: the heading lowercased, `remind-01`; retired, `remind-02-retired`.
- Modify keeps the ID; a changed contract retires it and adds a new one, at item and rule level alike.

## The Spec Tool

`Bin/spec-tool.py` in the skai checkout, run with `python3` from the host project root:

| Command | What it does |
| --- | --- |
| `validate ROOT...` | Every file under the roots against the shape. A later root overlays an earlier one: `validate <catalog> <drafts>` checks a package as its projection (a request's drafts bring their bases in between). A fault in a file the package holds, or a conflict the projection introduces, blocks; a fault in an untouched canonical file is a note. |
| `references ID-OR-TERM ROOT...` | Every file and line citing an ID or one of its rules, or linking a glossary term; given a rule, its bold-number pointers in its item too. Run before modifying or retiring either; decide per citation whether it still holds. |
| `link-terms ROOT...` | Links glossary terms in spec prose under the last root, reading terms from every root: `link-terms <catalog> <drafts>` writes only the drafts. Run while drafting. |
| `convert ROOT...` | Rewrites old-shape files (`## ID` items, dotted rule citations, `**Term** — text` glossary entries) in place, then links terms and validates; idempotent. |
| `render [--base DIR]... --drafts DIR [--authoring FILE] [--out FILE]` | The change package's review page against the catalog of the drafts' type in the production artifacts root, empty before its first promotion (a request's drafts layer on its base's, found from its folder; `--base` overrides), with the card, discussion and justifications of the package's authoring artifact; `--authoring` only points elsewhere; `--no-authoring` gives a bare comparison, never the committed page. `--base` layers another open package's drafts over the catalog. Render conventions and diffing: tool docstring. Gap footnotes: [spec-file-gaps.md](spec-file-gaps.md). |
| `check-changes [--base DIR]... --drafts DIR --authoring FILE` | The catalog is found as for `render`. Checks change-list coverage and operations against the projection, the log against Discussion, and gap footnotes against gap items; coverage rules are in the tool docstring. |

Until promotion writes, whenever a package materially changes, validate, then render, before anything else; the gate and promotion renders are the last of many.

## Change Items

The package's typed change list (`R<n>` product, `S<n>` design: ID, type, identity, justification, touched files) is the spec type's artifacts guide's; the renderer reads it only for justifications.

## What The Validator Rejects

Reports these shape faults, with file and line: headings, Title Case included; a missing statement, or prose after rules or tables; duplicate IDs across the catalog; a retired item or rule revived; rule numbering and nesting; table header, separator and keys; link definitions unused, undefined, duplicated or not at the end; progress markers (`- [ ]`, `🟡`); invalid footnotes or any in canon; glossary entries not `###` headings, out of order, duplicated or not in sentence case; an Also called note malformed, repeated or not last; an index bullet off its shape; a glossary term unlinked outside its governing items.

## Project Addendum

If `<active-project-root>/skai/addenda/spec-file-shape-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
