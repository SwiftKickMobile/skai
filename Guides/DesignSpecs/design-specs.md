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

A **design spec** joins a screen's design to the product's requirements. For each screen it says
which drawn state shows under which condition, how data is formatted, which copy varies with state
or data, what each control does within the screen, where the screen leads, and which shared patterns
it uses by reference. A story is fully described by three artifacts — functional requirements,
designs, design specs. The UI Map is a technical document downstream of all three and references
none of them.

Its primary audience is the **agent** implementing a screen, reading the spec with the design and
the requirements open beside it. People read it too, and every line must read to a product manager.

This guide owns **content rules only** — what good specs look like. It has no gates and is not a
workflow. The workflows that write the specs are:

- [`design-specs-authoring.md`](design-specs-authoring.md) — drafts specs into a change package
- [`design-specs-promotion.md`](design-specs-promotion.md) — promotes an approved package into the specs

**Ordinary authoring/promotion does not retroactively conform the specs.** Rules apply to new or
changed content; pre-existing defects do not block a package.

Work-spec implementation may update or remove known-difference notes after verified fixes, including
link definitions no longer used after that cleanup. Spec text and IDs remain read-only.

### What Belongs Here

Three artifacts, one home per fact:

| Artifact | Owns |
| --- | --- |
| Requirements | What the product promises, stated without naming a screen; product thresholds (a fifteen-minute window, an 8:00 PM cutoff). |
| Design | What things look like, and the copy of everything it draws. |
| Design spec | How a screen presents the promises: which state under which condition; formatting constants (rounding, a `1 min` floor, how many initials); copy that varies with state or data; controls by what they do; where the screen leads. |

The placement test: a sentence a product manager would state as a promise to the user regardless of
screen is a requirement; a sentence that says how a screen presents that promise is a spec. A spec
cites the requirement and never restates its rule (*Restatement*, under Writing Style). A rule that
narrows a requirement — a notice hidden in one case the requirement does not mention — is a
requirements gap, raised as the authoring guide says, never specified quietly.

Acceptance criteria is not a fourth artifact. The change package's item list is the acceptance
criteria, and work specs cite the spec IDs.

The apps a spec holds for are the project's: the requirements root index names them. A spec holds
for every one of them unless a known-difference note under the item says otherwise.

## Layout

```
skai/design-specs/
  _design-specs.md          <- root index (product paragraph + map of folders)
  glossary.md               <- the things the specs name, and the second index
  screens/
    _screens.md
    <screen>.md             <- one file per screen, as product names it
    <family>.md             <- rules common to a family of screens
  shared/
    _shared.md
    <piece>.md              <- a piece shown on screens of different families
  global/
    _global.md
    <pattern>.md            <- a pattern every screen uses by reference
```

**Screen is the primary key.** Readers arrive with a screen in hand, so files are organized by
screen, never by subject, class or module. Files mirror the design's columns, loosely: one file per
screen as product names it, and a common file where several screens share one design (a `notes.md`
and a `trash.md` beside the `list-screen.md` both use). A screen earns its own file when the design
draws it differently.

A rule goes in the first place that fits:

1. The screen's file.
2. If it applies to a family of screens, the family's common file, still under `screens/`.
3. If the piece is shown on screens of different families, `shared/`.
4. If every screen uses it — loading, errors, empty states, connectivity — `global/`.

All three folders exist from the start, each with its index. A piece is extracted the first time a
rule would otherwise be written twice; until then it stays in the screen's file. Zero duplication is
not the goal: restating another *spec's* rule so a file reads on its own is allowed.

Stability comes from the IDs, not the layout, so the layout may follow intuition. Moving items
between files never renumbers them; a restructure is a package of `move` items. A package never
deletes a file: the source keeps whatever items were not moved.

### Index Naming: `<folder>/_<folder>.md`

Every folder carries an index named for its folder with a leading `_`.

### Root Index

A short paragraph describing the product and naming the design file and the requirements it joins,
the folders with a one-line reminder each, and the glossary named as the second index. No status
text (`pending`, `none yet`); that belongs in the package.

```markdown
# LumenNotes Design Specs

LumenNotes is a notes app for people who think in notebooks. Its screens are designed in the
LumenNotes design file; its behavior is set by the product requirements. These specs join the two:
for each screen, which drawn state shows under which condition, how data is formatted, and what each
control does, all in product terms. One product, two apps; a spec holds for both unless it says
otherwise.

- [screens] — one file per screen as product names it; where several screens share a design,
  their common rules have a file of their own
- [shared] — a piece used on screens of different families, specified once
- [global] — patterns every screen uses by reference: loading, errors, empty states, connectivity

[glossary.md] defines the things the specs name and, for each, points at the items that govern it.
It is the specs' second index: a question that cuts across screens is found through it.

[screens]: screens/_screens.md
[shared]: shared/_shared.md
[global]: global/_global.md
[glossary.md]: glossary.md
```

### Folder Indexes

A one-line reminder of what the folder holds, then a line per file: its prefixes, the questions it
answers, and the optional `(uses: …)` cross-references last. **Index lines name the questions a file
answers, not its subject**; when a reader who needs a rule would not recognize it from the line, the
line is wrong. A prefix is a namespace, not a file: after a move it may span files, and each line
lists every prefix its file holds.

```markdown
# Screens

One file per screen as product names it. Where several screens share a design, the common rules
have a file of their own and each screen's file holds only what differs.

- [list-screen] -- `UI-LIST-` -- Rules every list screen shares: how groups are headed, what an
  empty list says, how staleness and loading show (uses: [SYNC-04])
- [notes] -- `UI-NOTES-` -- The notes list: which row a note gets, how its date reads, which
  reminder badge shows, what tapping does (uses: [list-screen], [NOTE-08], [REMIND-02])
- [note-editor] -- `UI-EDITOR-`, `UI-FORMAT-` -- The note editor: what the formatting bar offers
  and when, how a reminder is set, where closing leads (uses: [NOTE-05])

[list-screen]: list-screen.md
[notes]: notes.md
[note-editor]: note-editor.md
[SYNC-04]: ../../requirements/platform/sync.md#sync-04
[NOTE-08]: ../../requirements/domains/note.md#note-08
[REMIND-02]: ../../requirements/features/reminders.md#remind-02
[NOTE-05]: ../../requirements/domains/note.md#note-05
```

### Glossary

`glossary.md` is an alphabetical list of the things the specs name — rows, cards, badges, marks,
notices — one short paragraph each, in product language, with the items that govern each woven into
the definition. It is the specs' **second index**: a question that cuts across screens (where a
format is set, which screens show a notice) is answered here.

An entry **identifies and routes**; it never binds. Any obligation — a condition, a format, a
precedence — lives in a numbered item the entry points at. Not a "used by" list, not examples.

Every thing a spec names gets an entry. A thing that shares its name with a requirements term gets an
entry that identifies the drawn element and says the concept is the requirements'. Requirement terms
themselves (conditions like *overdue*, *stale*) get no entry: they are the requirements glossary's.
No design-tool identifiers. Entries are linked by file, as the catalog's are.

```markdown
**Pinned row** — the notes-list row a pinned note gets; whether a note is pinned is the
requirements' ([NOTE-08], [UI-NOTES-01]).

**Reminder badge** — the label on a notes-list row naming the note's reminder state
([UI-NOTES-02]).

**Stale notice** — the line giving a list's age, above its first group while the list is stale
([UI-LIST-03]).

[NOTE-08]: ../requirements/domains/note.md#note-08
[UI-NOTES-01]: screens/notes.md#ui-notes-01
[UI-NOTES-02]: screens/notes.md#ui-notes-02
[UI-LIST-03]: screens/list-screen.md#ui-list-03
```

## Spec File Shape

A title and an intro paragraph — no header beyond that — then `##` headings for the screen's parts
(not cited), `###` per citable item carrying only its ID, and the item's rules as bullets prefixed
with a bold two-digit local segment, nested as needed. Data under an item — a mapping, a list of
strings — is a table or a plain list, not numbered rules.

```markdown
# Notes

The notes of one notebook, newest first, each as a row. Rules common to every list screen are in
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

- **01** Pending looks different on a row due today and on a later day's row.

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

Rules the template carries:

- **Items are the contract unit.** A table under an item is normative; its row order is significant
  only when the item says so; changing a row is a modify of the item. Citing an item includes its
  rules and its data.
- **Conditions are exhaustive and unambiguous.** Where conditions overlap, the item states the
  precedence ("the first that holds").
- **Known differences** — a confirmed difference between the spec and one app, or between
  platforms — are a blockquote directly under the affected item, in the catalog's form:
  `> **Known difference — <app or platform>:** …`, with the tracking issue linked when one exists.
  The note records a gap, not an exception. A difference is confirmed only by observing it on that
  app; a suspected one stays a Discussion item until the supervisor resolves it. Platform words appear here and nowhere else in a spec.
- **Pending references.** A spec not yet written is named inline as `(spec pending: <file>)`,
  unlinked, with no definition. A pending destination (where a control leads) never blocks
  promotion; a pending global pattern the item depends on does.
- **Links** are reference-style with definitions at the bottom, as the catalog's. Requirement IDs
  are cited as links — stable handles that never change on promotion — and may target a requirement
  that exists only as a draft in an active requirements package; promotion repoints the link
  once the requirement is canonical. Sibling specs are linked by file or item, glossary entries by
  file. Nothing links into the design tool.
- **Sub-ID citations** use the path `UI-NOTES-01.03`, visible in full, with the link targeting the
  parent heading: `[UI-NOTES-01.03]: notes.md#ui-notes-01`. Retired items keep their heading, so a
  citation of one still lands on an explanation.
- **Every binding claim has an ID.** Intro paragraphs, index lines and glossary entries orient; if a
  sentence says what a screen must show or do, it is a rule and needs an ID.

### Citing by Reference

Referencing a thing by its glossary name brings every item that governs it — the glossary lists
them. Referencing a file ("rules common to every list screen are in List Screen") brings the file's
items. Exceptions are stated in the referencing item ("…except the stale notice, which this screen
never shows").

## IDs

### Format

`UI-<PREFIX>-<NN>` for an item; `UI-<PREFIX>-<NN>.<NN>` for a rule under it, one two-digit segment
per level. The leading `UI-` distinguishes a spec ID from a requirement ID. The prefix names **the
thing specified** — a screen, a shell, a family, a shared piece — never the file, and is unique
across the specs. Numbers are zero-padded two digits; past 99, widen to three for new IDs. Sub-IDs
go on rules, not on data rows.

The next number for a prefix is the prefix's maximum in the canonical specs, plus one; a collision
with another package is caught when the later one promotes (`V8`).

### Stability

- IDs are **file-independent**: moving an item between files never renumbers it. A restructure is a
  package of `move` items.
- IDs are **append-only from the moment they are drafted**, not from promotion: a work spec may
  already cite a pending ID. A retired ID is burned — never reused, never renumbered.
- **Retire in place, at every level.** A retired item keeps its heading and takes `(retired)`, with
  its body replaced by a short statement naming the superseding ID when there is one (the
  `UI-NOTES-04` example above). A retired rule keeps its segment: `- **02** (retired) Superseded by
  **04**.`

### Modify vs. Retire

- **Modify — keep the ID.** The same promise, clarified or tightened; anything citing the ID was
  citing this promise and still is.
- **Retire and add — new ID.** The contract changed such that something previously conforming no
  longer conforms.

A parent item is an extensible collection: a new rule is appended to it; a rule whose contract
changes is retired and a new rule added under the same parent; retiring the parent retires its rules;
moving a rule to another parent is retire-and-add.

## Writing Style

Write as a **product manager describing a screen to a developer who can see the design**. These
rules govern the spec files — canonical and draft alike — and quoted proposed text in a package. A
package's Discussion, Inputs and Justification may name frames, nodes and code files.

### Product Language Only

A spec names things in product terms — "the compact card", "the placeholder profile button", "the
stale notice" — and never in design-tool terms: no frame names, component, variant or property
names, URLs or node ids. Making a drawing findable by its product name is the design's job; a
mismatch is a Discussion item. No jargon or coined phrases: "a tip pointing at the profile button",
not "platform-rendered TipKit popover".

### Never Appearance

A rule never prescribes how something looks: no color, position, shape or size words. The ban is
semantic, not lexical. Established product names ("compact card") and the relationships needed to
identify a thing ("the button at the top left") are allowed, in glossary entries especially; what the
thing looks like is the design's. If the only way to say it is in words, the design is incomplete.

### Copy

The design owns the copy of what it draws. A spec quotes a string only when it carries a format
(`{N} min`, `Last refreshed {age}`), varies with data (a per-notebook empty message, a badge's
label), or belongs to something the design does not draw (a system tip's message), which the spec
then carries as data. Controls are named by what they do ("a button that opens the app's page in
device settings"), never by their label; a control whose label changes with state is named by its
function and its labels are a mapping under the item.

### Mechanism Is the Developer's

A spec says what the user sees ("a tip pointing at the profile button"), never how a platform
produces it. A spec holds for every app the product has and never names a platform in a rule ("a
standard tip bubble", not "a standard iOS tip bubble"); intentional adaptive behavior (tablet vs.
phone) is a condition in the rule. Platform words appear only in known-difference notes. What was
verified on one app only is recorded in the package's Assumptions, not in the spec.

### Restatement

Delete the citation; if what remains adds no binding — no target, state, format, control or place
beyond the cited contract — cut it to the citation. "Tapping anywhere on the row opens the note
([NOTE-05])" keeps the tap target and stays; "The list refreshes when pulled down ([SYNC-06])" adds
nothing and goes. Restating a requirement is a defect; restating another spec's rule for
readability is not.

### What Counts as a State

Three kinds of difference, each with a home:

- **Screen state** — the layout differs. The design draws it; the spec binds it to its condition.
- **Component appearance** — the same layout styled by condition (badge styles, heading looks, a
  placeholder glyph). The design draws the variants; the spec binds condition to variant by product
  name ("pending looks different on a row due today").
- **Data substitution** — a different string in the same look (a per-notebook empty message, a day
  heading's text). No drawing; the spec gives the data.

An element dropping out without moving the rest — a missing date, an absent contact button — is a
component property, not a screen state; reflow inside the component's own bounds does not count as
moving the rest, and not every combination is drawn. Standard system UI the app does not style (tip
bubbles, confirmation sheets, alerts) is specified by its condition and choices; the design need not
draw it, and the spec never says whether it is drawn. It ceases to qualify when the app styles it.

### Nothing That Decays

As the catalog: no temporal references ("as before the redesign"), no workflow state ("while the
design is reconsidered"). A spec is read years later by someone with no memory of the change.

### Self-Check

Before writing a rule:

1. Could a product manager read it without losing meaning, and a developer act on it with the
   design open?
2. Does it name a frame, component, variant, node, platform, framework or code identifier? Rewrite.
3. Does it say what something looks like? Cut; the design shows it.
4. With its citation deleted, does it still add a binding? If not, cut it to the citation.
5. Does it quote a string that is neither a format nor data nor undrawn copy? Cut it.
6. Can every state it names be found in the design by the name used here?

## Verification Checks

Ten checks, run by authoring before its Discussion gate advances and by promotion before the write.
They are enumerated once, here, so the two workflows cannot drift apart. Scope: the changed items,
plus every touched file as a whole.

- `V1 Restatement` — every cited sentence still adds a binding with its citation deleted
  (*Restatement*).
- `V2 Appearance` — no rule prescribes a color, position, shape or size (*Never Appearance*).
- `V3 Product language` — no design-tool identifier, platform name, mechanism or code identifier in
  a rule (*Product Language Only*, *Mechanism Is the Developer's*).
- `V4 Static copy` — every quoted string is a format, data-dependent, or the copy of something the
  design does not draw (*Copy*).
- `V5 Drawn state` — every screen state and component variant an item names can be found in the
  design by its product-language name. The agent looks: on the production page, or on any change
  page whose mockups are approved, whichever package drew it (the design tool guide names the
  pages; [`figma-designer-guide.md`](../Design/figma-designer-guide.md) for Figma). An unapproved
  draft does not count; standard system UI the app does not style is exempt. Unavailable design
  access blocks the check rather than passing it.
- `V6 Links` — every definition resolves to the intended item, not merely an existing file; pending
  specs use the `(spec pending: <file>)` notation; tracking links identify their issue. At
  promotion, every cited requirement is canonical.
- `V7 One home` — no rule stated in both a requirement and a spec; the spec is the defect.
- `V8 IDs and prefixes` — every ID in a rewritten file remains in its draft, none renumbered, no
  retired ID reused; every prefix is unique across canon and this package and recorded on its
  file's index line.
- `V9 Indexes and glossary` — every file has an index line naming the questions it answers and
  listing its prefixes; every thing the specs name has a glossary entry pointing at its governing
  items, binding nothing; no status text in an index; no binding claim in unnumbered prose.
- `V10 Completeness` — every item's conditions are exhaustive and unambiguous, with precedence
  stated where they overlap.

## Cross-References

- [`design-specs-authoring.md`](design-specs-authoring.md) — drafting specs into a change package
- [`design-specs-promotion.md`](design-specs-promotion.md) — promoting an approved package
- [`requirements-catalog.md`](../Requirements/requirements-catalog.md) — the requirements the specs
  cite: link format, index and glossary conventions the specs mirror
- [`figma-designer-guide.md`](../Design/figma-designer-guide.md) — where drawings live in a Figma file

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
