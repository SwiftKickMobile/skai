Managed-By: skai
Managed-Id: guide.design-specs
Managed-Source: Guides/DesignSpecs/design-specs.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Specs

Print `📖 SKAI guide: design-specs` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

- [Purpose](#purpose)
- [Layout](#layout)
- [Spec File Shape](#spec-file-shape)
- [IDs](#ids)
- [Writing Style](#writing-style)
- [Verification Checks](#verification-checks)

## Purpose

A **design spec** joins a screen's design to its requirements: which drawn state appears under
which condition, data formatting, variable copy, controls, destinations and referenced shared
patterns. Requirements, designs and design specs fully describe a story. The downstream UI Map
is technical and references none of them.

Write for an implementing agent with the design and requirements open, in language a product
manager can read. This guide owns content and has no gates. Follow
[`design-specs-authoring.md`](design-specs-authoring.md) to draft and
[`design-specs-promotion.md`](design-specs-promotion.md) to promote.

**Check changed items and every touched file whole.** Do not re-examine untouched canonical files;
an unrelated defect found there is routed as [`design-specs-artifacts.md`](design-specs-artifacts.md)
§ Change Requests says; only a contradiction that would make the write inconsistent blocks.

Work-spec implementation may remove or update known-difference notes after verified fixes and
remove unused link definitions. Spec text and IDs remain read-only.

### What Belongs Here

One home per fact:

| Artifact | Owns |
| --- | --- |
| Requirements | Screen-independent product promises and thresholds (a fifteen-minute window, an 8:00 PM cutoff). |
| Design | Appearance and the copy it draws. |
| Design spec | How screens present promises: conditions and states, formatting constants (rounding, a `1 min` floor, initials count), variable copy, controls by function and destinations. |

A promise a product manager would make regardless of screen is a requirement; its screen
presentation is a spec. Cite requirements without restating them (*Restatement*). A spec that
narrows a requirement, such as hiding a notice in an unmentioned case, is a requirements gap:
follow authoring's gap procedure.

The package's item list is its acceptance criteria, not a fourth artifact. Work specs cite spec IDs.
Specs apply to every app named by the requirements root index.

## Layout

```
skai/design-specs/
  _design-specs.md       <- product paragraph + folder map
  glossary.md            <- second index
  screens/
    _screens.md
    <screen>.md
    <family>.md          <- family rules
  shared/
    _shared.md
    <piece>.md           <- cross-family piece
  global/
    _global.md
    <pattern>.md         <- used by every screen
```

**Screen is the primary key**, never subject, class or module. Use one file per product-named
screen; a differently drawn screen earns its own file. Screens sharing a design share a common
file (`notes.md` and `trash.md` use `list-screen.md`).

Put a rule in the first fitting home: screen; family common file under `screens/`; `shared/`
for cross-family pieces; `global/` for patterns every screen uses (loading, errors, empty states,
connectivity). Extract when a rule would first be written twice. Cite another spec's rule rather than copying it;
only a declared override restates (*Citing by Reference*). ❌ a stage file repeating the family's
heading rule · ✅ "Headings as [UI-LIST-01.02]".

Create all three folders and indexes immediately. Moves preserve IDs; restructures use `move`
items and never delete files.

### Index Naming: `<folder>/_<folder>.md`

Each folder's index is named for the folder with a leading `_`.

### Root Index

Include a product paragraph naming the design file and requirements, a folder map with one-line
reminders, and the glossary as second index. Status text (`pending`, `none yet`) belongs in
the package.

### Folder Indexes

Start with a one-line folder reminder. Each file's line lists its prefixes, the questions it
answers and optional `(uses: …)` references last. Name questions, not subjects: readers seeking
a rule must recognize its line. Prefixes are namespaces; after a move each file lists every
prefix it holds, including those spanning files.

```markdown
# Screens

One file per product-named screen. Screens sharing a design share common rules in a family file;
their own files hold the differences.

- [list-screen] -- `UI-LIST-` -- How groups are headed, what an empty list says, how staleness
  and loading show (uses: [SYNC-04])
- [notes] -- `UI-NOTES-` -- Which row and reminder badge a note gets, its date format and tap
  action (uses: [list-screen], [NOTE-08], [REMIND-02])

[list-screen]: list-screen.md
[notes]: notes.md
[SYNC-04]: ../../requirements/platform/sync.md#sync-04
[NOTE-08]: ../../requirements/domains/note.md#note-08
[REMIND-02]: ../../requirements/features/reminders.md#remind-02
```

### Glossary

`glossary.md` is the second index: it answers cross-screen questions such as where a format is
set or which screens show a notice. Give every thing the specs name (rows, cards, badges, marks,
notices) one short product-language paragraph: **what it means and is for**, then links to its
governing items. One or two identifying details may follow. Never inventory elements, position or
appearance; never bind. Conditions, formats and precedence belong in linked numbered items;
screen-specific detail belongs in that screen's item.

❌ **Transfer notice** — a blue banner with an icon, a heading and two links below the toolbar.
✅ **Transfer notice** — explains an unfinished transfer; dismissible ([UI-TRANSFER-03]).

Sections are **Global**, **Shared**, then one per screen family, entries alphabetical within each.
Use the governing item's home, not first appearance or choice. Cross-family terms are extracted
to `shared/` and listed in Shared; entries move with their items. Read Global, Shared and the
current family. If one file becomes too large, split into per-folder glossaries along these seams.

A thing named like a requirements term gets an entry identifying the drawn element and crediting
the requirements for the concept. Requirement terms themselves (*overdue*, *stale*) get no entry.
No design-tool identifiers. Link glossary entries by file.

```markdown
## List Screens

**Pinned row** — the row a pinned note gets, so it stands apart from the rest; whether a note is
pinned is the requirements' ([NOTE-08], [UI-NOTES-01]).

**Reminder badge** — the label on a row naming the note's reminder state ([UI-NOTES-02]).

**Stale notice** — the line telling the person a list is out of date ([UI-LIST-03]).

[UI-LIST-03]: screens/list-screen.md#ui-list-03
[NOTE-08]: ../requirements/domains/note.md#note-08
[UI-NOTES-01]: screens/notes.md#ui-notes-01
[UI-NOTES-02]: screens/notes.md#ui-notes-02
```

## Spec File Shape

Title Case headings. Use a title and intro, no other header; `##` for uncited parts, optionally opening with one
nonbinding orientation line; `###` carrying only the citable item's ID. Open each item with one
sentence identifying its subject and linking its requirement, then bold two-digit rule bullets,
nested as needed. Data (mappings or strings) uses tables or plain lists, never rule numbers.

```markdown
# Notes

The notes belonging to one notebook. Rules common to every list screen are in
[List Screen][spec-list].

## Rows

### UI-NOTES-01
Each note is a row ([NOTE-03]).

- **01** The pinned row when the note is pinned ([NOTE-08]); the plain row otherwise.
- **02** The row's date reads `{Today|Yesterday}` for those days, the weekday name within the
  last week, and `{Mon D}` otherwise, with the year added when it is not the current one.
- **03** Tapping anywhere on the row opens the note ([NOTE-05]; spec pending: `note-editor.md`).
  - **01** A row swiped from the trailing edge reveals the delete action ([NOTE-09]).

### UI-NOTES-02
The reminder badge shows the note's reminder state ([REMIND-02]), in [REMIND-02]'s precedence:

| State | Label |
| --- | --- |
| pending | `{time}` |
| overdue | OVERDUE |
| acknowledged | DONE |

- **01** When pending: due-today pending badge if due today; later pending badge otherwise.

## Empty State

### UI-NOTES-03
With no notes, the empty state with the notebook's message ([UI-LIST-02][spec-empty], [NOTE-11]).

> **Known difference — Android:** the empty state is shown without the message. Tracked in
> [empty-message].

### UI-NOTES-04 (retired)
Superseded by [UI-NOTES-02].

[spec-list]: list-screen.md
[spec-empty]: list-screen.md#ui-list-02
[UI-NOTES-02]: #ui-notes-02
[NOTE-03]: ../../requirements/domains/note.md#note-03
[NOTE-05]: ../../requirements/domains/note.md#note-05
[NOTE-08]: ../../requirements/domains/note.md#note-08
[NOTE-09]: ../../requirements/domains/note.md#note-09
[NOTE-11]: ../../requirements/domains/note.md#note-11
[REMIND-02]: ../../requirements/features/reminders.md#remind-02
[empty-message]: https://github.com/example/lumennotes/issues/412
```

- **Contract unit:** an item includes rules and normative data. Table order binds only when
  stated; data edits follow *Modify vs. Retire*.
- **Conditions:** exhaustive and unambiguous; state precedence for overlaps (“the first that holds”).
- **Known differences:** only observed app/spec differences qualify. Under the affected item use
  `> **Known difference — <app or platform>:** …`, linking a tracking issue when available.
  This records a gap, not an exception. Platform words belong only here.
- **Pending references:** name unwritten specs inline, unlinked: `(spec pending: <file>)`.
  Pending destinations do not block promotion; depended-on global patterns do.
- **Links:** reference-style, definitions at the bottom. Link requirement IDs, including drafts in
  active requirements packages; promotion repoints them after requirements become canonical.
  Link sibling specs by file or item, glossary entries by file; never link into the design tool.
- **Sub-IDs:** cite `UI-NOTES-01.03` at its parent heading:
  `[UI-NOTES-01.03]: notes.md#ui-notes-01`. Retired headings retain an explanation.
- **Every binding claim has an ID.** Intros, indexes and glossary entries orient. What a screen must
  show or do belongs under an ID.

### Citing by Reference

A glossary name brings all governing items; a file reference brings its items. An override of a
family, shared or global rule declares the override and links the superseded rule (“Validation here
replaces [UI-FORM-01.02][spec-validation]: …”). Parents never name overrides. Overrides may
restate the parent with modifications; without a declaration the inherited rule stands.

## IDs

### Format

Items use `UI-<PREFIX>-<NN>`; rules append `.<NN>` per level. `UI-` distinguishes spec IDs
from requirements. Prefixes uniquely name the thing (screen, family, shared piece), never the
file; include its kind if the noun is abstract (`UI-DEFAULT-STAGE`, not `UI-DEFAULT`).
Abbreviations are fine. Zero-pad to two digits; widen new IDs past 99 to three. Data rows get no IDs.

Next number: the prefix's canonical maximum plus one. `V8` catches package collisions on the
later promotion.

### Stability

IDs are file-independent and append-only from first drafting: work specs may already cite them.
Moves never renumber; restructures use `move` items. Retired IDs are burned, never reused.

Retire in place at every level. Keep item headings and rule segments, marking each `(retired)`;
replace binding text with a short explanation naming any successor (see `UI-NOTES-04` above).
Retiring a parent marks its descendants retired too. A rule: `- **02** (retired) Superseded by
**04**.`

### Modify vs. Retire

**Modify** retains the ID for the same promise, clarified; existing citations still
mean it. **Retire and add** when the contract changes so previously conforming behavior no longer
conforms.

Parents are extensible: append new rules; retire and replace changed contracts under the same
parent. Moving a rule to a different parent is retire-and-add.

## Writing Style

Write as a **product manager describing a screen to a developer who sees the design**. These
rules apply to canonical and draft specs and quoted proposed text; package prose may name
frames, nodes and code files.

### Product Language Only

Use product terms (“compact card”, “placeholder profile button”, “stale notice”), never design-tool
frame, component, variant or property names, URLs or node IDs. The design must make drawings
findable by product name; mismatches become Discussion items. Avoid jargon and coined phrases:
“a tip pointing at the profile button”, not “platform-rendered TipKit popover”.

### Never Appearance

Never prescribe color, position, shape, size or style in rules, intros or glossary entries.
**Would a purely visual redesign make the sentence false without changing what the thing is,
is for, or does?** If so, delete it: the design owns appearance. Exceptions are established product names
(“compact card”) and relationships used only to identify a thing (“the button beside the search field”).
❌ “the completed row is gray” · ❌ “a blue notice with an icon, heading and two links”
· ✅ “the completed row” · ✅ “the notice explaining an unfinished transfer”.
Motion and transitions require words; see *What Counts as a State*.

### Copy

Quote only formats (`{N} min`, `Last refreshed {age}`), data-dependent copy (per-notebook
empty messages, badge labels) or copy the design does not draw (a system tip's message).
Carry these as data; the design owns other copy. Name controls by function (“a button that
opens the app's page in device settings”), never labels: ❌ "the OK button" · ✅ "the
acknowledgement button". Map variable labels under the item.

### Mechanism Is the Developer's

Describe what the person sees, not its platform mechanism: “a tip pointing at the profile button”;
“a standard tip bubble”, not “a standard iOS tip bubble”. Rules apply to every app. Tablet/phone
adaptation is a condition; platform words belong only in known-difference notes. Record
single-app verification in package Assumptions.

### Restatement

For requirement citations, delete the citation: without an added screen binding beyond the cited contract, reduce the sentence to its citation. “Tapping anywhere on the row opens the note
([NOTE-05])” adds a tap target; “The list refreshes when pulled down ([SYNC-06])” adds nothing.
Never restate requirements; cite another spec's rule, or restate it only as a declared override
(*Citing by Reference*).

### What Counts as a State

- **Screen state:** different layout. Design draws it; spec binds its condition.
- **Component appearance:** same layout, conditional styling (badge styles, heading looks,
  placeholder glyph). Design draws variants; spec binds each condition to a variant by product
  name.
- **Data substitution:** different string, same look (per-notebook empty messages, day-heading
  text). Specify data; no drawing.
- **Motion and polish:** transitions, animation, timing, haptics, loading/refresh feel, entrances
  and exits. Design cannot draw these and a careful developer will not add them unasked.
  Specify under the applicable item what moves, when and what it conveys (“the new row slides
  in from where it was added, so the person sees where it went”), never easing curves or pixels.
  ❌ "the label gives way to an indicator" (a substitution, not its motion) · ✅ "the label fades
  out as the indicator fades in".

An element disappearing without moving the rest (missing date, absent contact button) is a
component property; internal reflow does not count and not every combination is drawn.
For unstyled standard system UI (tips, confirmations, alerts), specify conditions and choices;
no drawing is required, and the spec never says whether it is drawn.

### Nothing That Decays

As in the catalog, omit temporal references (“as before the redesign”) and workflow state: the
spec must survive the change's memory.

## Verification Checks

Run these ten checks before authoring's Discussion gate advances and before promotion writes.
This is their sole enumeration. Scope: changed items plus every touched file whole.

- `V1 Restatement` — requirement-citing binding prose adds a screen binding beyond the cited
  requirement (*Restatement*). Nonbinding orientation and routing are checked by `V9`.
- `V2 Appearance` — inspect sentences, including glossary entries, against *Never Appearance*'s
  redesign test. Evidence names inspected sentences, never a word list.
- `V3 Product language` — no design-tool or code identifier or mechanism anywhere in spec text;
  platform names only in known-difference notes (*Product Language Only*, *Mechanism Is the
  Developer's*).
- `V4 Static copy` — quoted strings are formats, data-dependent or undrawn copy (*Copy*).
- `V5 Drawn state` — find every prescribed screen state/component variant by product name in
  production or approved change-page mockups, from any package. Look in the design; unapproved
  drafts do not count. Unstyled standard system UI is exempt; unavailable access blocks.
  Page conventions belong to the tool guide ([Figma](../Design/figma-designer-guide.md)).
- `V6 Links` — definitions reach intended items, not just files; overrides link superseded rules
  and parents never name overrides. Pending specs use `(spec pending: <file>)`; tracking links
  identify issues. At promotion, all cited requirements are canonical.
- `V7 One home` — no requirement rule restated in a spec, and no spec rule copied into another
  file without a declared override; the copy is the defect.
- `V8 IDs and prefixes` — every rewritten-file ID remains in its draft, retired in place per *Stability*, or
  at its declared move destination; no renumbering, retired-ID reuse or duplicate IDs in projected canon. Each prefix names one
  thing (with kind when abstract) and appears on file index lines.
- `V9 Indexes, glossary and shape` — each file's index line names answered questions and prefixes,
  without status. Every named thing has a glossary entry under its governing item's home:
  meaning, purpose and routing, no inventory/position/appearance or binding, and any detail it
  carries is supported by the items it links. Each live item opens with its statement and
  requirement link, and a retired one carries the retirement form; no unnumbered binding prose.
- `V10 Completeness` — every binding the inputs require (requirements, drawings, the app in a
  backfill) traces to a governing item; an omission fails. Conditions are exhaustive and
  unambiguous, with precedence for overlaps. For each item, look for motion/polish a careful developer would not
  ship unasked — in a backfill, in the app's code; otherwise in what the designer stated — and
  check it is specified; motion nobody stated is a Discussion item, never assumed absent.

## Cross-References

- [`requirements-catalog.md`](../Requirements/requirements-catalog.md) — requirements, link,
  index and glossary conventions mirrored here

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
