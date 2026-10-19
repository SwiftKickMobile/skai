Managed-By: skai
Managed-Id: guide.design-specs
Managed-Source: Guides/DesignSpecs/design-specs.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-18

# Design Specs

Print `📖 SKAI guide: design-specs` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

A **design spec** joins a screen's design to its requirements: which drawn state appears under
which condition, data formatting, variable copy, controls, destinations and referenced shared
patterns. The UI Map is downstream of requirements, design and spec and references none of them.

Write for an implementing agent with the design and requirements open, in language a product
manager can read. This guide owns content and the ten checks; no gates. How a spec file is laid
out — headings, statements, rules, tables, known differences, links, IDs and anchors, glossary and
index form, the validating tool — is [`spec-file-shape.md`](../Core/spec-file-shape.md), cited,
never restated. [`design-specs-authoring.md`](design-specs-authoring.md) drafts;
[`design-specs-promotion.md`](design-specs-promotion.md) promotes.

**Check changed items and every touched file whole.** Do not re-examine untouched canonical files;
an unrelated defect found there is a change request
([`design-specs-artifacts.md`](design-specs-artifacts.md) § Change Requests); only a contradiction
that would make the write inconsistent blocks. Work-spec implementation may update or remove
known-difference notes after verified fixes; spec text and IDs are otherwise read-only.

### What Belongs Here

One home per fact. **Requirements** own screen-independent promises and thresholds; the
**design** owns appearance and the copy it draws; the **spec** owns how screens
present promises — conditions and states, formatting constants (rounding, a `1 min` floor),
variable copy, controls by function, destinations. Cite requirements without restating them
(*Restatement*). A spec that narrows a requirement, such as hiding a notice in an unmentioned
case, is a requirements gap: file a change request against the open product spec package or the
catalog, never specify it quietly.

The package's item list is its acceptance criteria, not a fourth artifact. Work specs cite spec IDs.
Specs apply to every app in the catalog's `apps/` index.

## Layout

```
skai/design-specs/   the fixed root, in the repository the README links
  _design-specs.md   glossary.md
  screens/   _screens.md   <screen>.md   <family>.md
  shared/    _shared.md    <piece>.md
  global/    _global.md    <pattern>.md
```

**Screen is the primary key**, never subject, class or module. One file per product-named screen;
a differently drawn screen earns its own file; screens sharing a design share a family file.

Put a rule in the first fitting home: screen; family file under `screens/`; `shared/` for
cross-family pieces; `global/` for patterns every screen uses (loading, errors, empty states).
Extract when a rule would first be written twice. Cite another spec's rule rather
than copying it; only a declared override restates (*Citing by Reference*). ❌ a screen file
repeating the family's heading rule · ✅ "Headings as [UI-LIST-01-02]".

Create all three folders and indexes immediately.

### Indexes

The root index holds a product paragraph naming the design file and requirements, a folder map
with one-line reminders, and the glossary as second index; status text belongs in the package.
Each file's line in a folder index, in the shape guide's form, lists every prefix the file holds
(including those spanning files after a move), the questions it answers and optional `(uses: …)`
references last. Name questions, not subjects: ✅ "Which row and reminder
badge a note gets, its date format and tap action".

### Glossary

`glossary.md` is the second index, answering cross-screen questions. Give every thing the specs
name (rows, cards, badges, notices) one short product-language paragraph: **what it means and is
for**, then links to its governing items; one or two identifying details may follow. Never
inventory elements, position or appearance; never bind — conditions, formats and precedence
belong in the linked items. Every occurrence of a term in spec prose links its entry (`link-terms`).

❌ *Transfer notice* — a blue banner with an icon, a heading and two links below the toolbar.
✅ *Transfer notice* — explains an unfinished transfer; dismissible ([UI-TRANSFER-03]).

Sections are **Global**, **Shared**, then one per screen family, entries alphabetical within each,
each under its governing item's home; entries move with their items, and
cross-family terms sit in Shared once extracted. Read Global, Shared and the current family. A
glossary that outgrows one file splits per folder along these seams. A thing named like a
requirements term gets an entry identifying the drawn element and crediting the requirements for
the concept ("whether a note is pinned is the requirements' ([NOTE-08], [UI-NOTES-01])");
requirement terms themselves (*overdue*, *stale*) get no entry.

## Items

An item is one `###` heading carrying its ID, in the shape guide's form. It opens with one
sentence identifying its subject and linking the requirement it presents — ✅ "The [reminder
badge][g-reminder-badge] shows the note's reminder state ([REMIND-02]):" — then its rules; data
(mappings, strings) goes in tables, never under rule numbers.
A `##` part groups and may open with one nonbinding orientation line; anything that says what
shows or when belongs under an item.

- **Contract unit:** an item is its rules and its data; data edits follow *Modify vs. Retire*.
- **Conditions:** exhaustive and unambiguous; state precedence for overlaps ("the first that holds").
- **Known differences:** only observed app/spec differences qualify, under the affected item with a
  tracking issue when available; a gap, not an exception. Platform words belong only here.
- **Pending references:** name unwritten specs inline, unlinked: `(spec pending: <file>)`. A
  pending destination does not block promotion; a depended-on global pattern does.
- **Links:** link requirement IDs, drafts in active product spec packages included; promotion
  repoints them once canonical. Never link into the design tool.
- **Every binding claim has an ID.** Intros, indexes and glossary entries orient; what a screen
  must show or do belongs under an ID.

### Citing by Reference

A glossary name brings all governing items; a file reference brings its items. An override of a
family, shared or global rule declares itself and links the superseded rule ("Validation here
replaces [UI-FORM-01-02]: …", with `[UI-FORM-01-02]: form.md#ui-form-01`); parents never name
overrides. An override may restate the parent with modifications; without a declaration the
inherited rule stands.

## IDs

Form and anchors are the shape guide's; `UI-` distinguishes spec IDs from requirements. Prefixes
uniquely name the thing (screen, family, shared piece), never the file, with its kind if the noun
is abstract (`UI-DEFAULT-FOLDER`, not `UI-DEFAULT`). Next number: the prefix's canonical maximum
plus one; two packages colliding surface at the later promotion.

### Stability

IDs are file-independent and append-only from first drafting. Moves never renumber; restructures
use `move` items. Retired IDs are burned. Retire in place at every level, keeping headings and
rule numbers and replacing binding text with a short explanation naming any successor; retiring a
parent retires its descendants.

### Modify vs. Retire

**Modify** retains the ID for the same promise, clarified; existing citations still mean it.
**Retire and add** when the contract changes so previously conforming behavior no longer
conforms. Append new rules under a parent; a changed rule retires and is replaced there; moving a
rule to another parent is retire-and-add. Before either, run `references`
and decide per citation whether it still holds.

## Writing Style

Write as a **product manager describing a screen to a developer who sees the design**. These
rules apply to canonical and draft specs and quoted proposed text; package prose may name
frames, nodes and code files.

### Product Language Only

Use product terms ("compact card", "stale notice"), never design-tool frame, component, variant or
property names, URLs or node IDs; a drawing the design does not make findable by product name is
a Discussion item. No jargon or coined phrases: "a tip pointing at the profile button", not
"platform-rendered TipKit popover".

### Never Appearance

Never prescribe color, position, shape, size or style in rules, intros or glossary entries.
**Would a purely visual redesign make the sentence false without changing what the thing is,
is for, or does?** If so, delete it: the design owns appearance. Exceptions: established product
names ("compact card") and relationships that only identify a thing ("the button beside the
search field"). ❌ "the completed row is gray" · ❌ "a blue notice with an icon, heading and two
links" · ✅ "the completed row" · ✅ "the notice explaining an unfinished transfer".

### Copy

Quote only formats (`{N} min`, `Last refreshed {age}`), data-dependent copy (badge labels) or copy
the design does not draw (a system tip's message), carried as data; the design owns other copy.
Name controls by function ("a button that opens the app's page in device settings"), never
labels: ❌ "the OK button" · ✅ "the acknowledgement button". Map
variable labels under the item.

### Mechanism Is the Developer's

Describe what the person sees, not its platform mechanism: "a standard tip bubble", not "a standard
iOS tip bubble". Rules apply to every app; tablet/phone adaptation is a condition. Record
single-app verification in package Assumptions.

### Restatement

A sentence citing a requirement must add a screen binding beyond the cited contract, or shrink to
the citation. "Tapping anywhere on the row opens the note ([NOTE-05])" adds a tap target; "The
list refreshes when pulled down ([SYNC-06])" adds nothing. Cite another spec's rule, or restate
it only as a declared override (*Citing by Reference*).

### What Counts as a State

- **Screen state:** different layout. Design draws it; spec binds its condition.
- **Component appearance:** same layout, conditional styling (badge styles, heading looks).
  Design draws variants; spec binds each condition to a variant by product name.
- **Data substitution:** different string, same look (per-notebook empty messages, day-heading
  text). Specify data; no drawing.
- **Motion and polish:** transitions, animation, timing, haptics, loading and refresh feel,
  entrances and exits. Design cannot draw these and a careful developer will not add them unasked,
  so specify under the item what moves, when and what it conveys ("the new row slides in from
  where it was added, so the person sees where it went"), never easing curves or pixels.
  ❌ "the label gives way to an indicator" (a substitution, not its motion) · ✅ "the label fades
  out as the indicator fades in".

An element disappearing without moving the rest (a missing date) is a component property;
internal reflow does not count and not every combination is drawn. For unstyled standard system
UI (tips, alerts), specify conditions and choices; no drawing is required, and the spec never
says whether it is drawn.

### Nothing That Decays

As in the catalog, omit temporal references ("as before the redesign") and workflow state: the
spec must survive the change's memory.

## Verification Checks

Before authoring's Discussion gate advances and before promotion writes, run the spec tool's
`validate` over the drafts projected on canon: a fault in a file the package holds, or a conflict
the projection introduces, blocks; a fault in an untouched canonical file is reported and becomes
a change request. Then these ten checks, enumerated only here, over the scope in *Purpose*.

- `V1 Restatement` — requirement-citing binding prose adds a screen binding beyond the cited
  requirement. Nonbinding orientation and routing are `V9`'s.
- `V2 Appearance` — inspect sentences, including glossary entries, against *Never Appearance*'s
  redesign test. Evidence names inspected sentences, never a word list.
- `V3 Product language` — no design-tool or code identifier or mechanism anywhere in spec text;
  platform names only in known-difference notes (*Product Language Only*).
- `V4 Static copy` — quoted strings are formats, data-dependent or undrawn copy.
- `V5 Drawn state` — find every prescribed screen state or component variant by product name in
  production or approved change-page mockups ([Figma](../Design/figma-designer-guide.md)), from
  any package; unapproved drafts do not count. Unstyled standard system UI is exempt; unavailable
  access blocks.
- `V6 Links` — definitions reach intended items, not just files; overrides link superseded rules
  and parents never name overrides; pending specs use `(spec pending: <file>)`; tracking links
  identify issues. At promotion, all cited requirements are canonical.
- `V7 One home` — no requirement rule restated in a spec, no spec rule copied into another file
  without a declared override; the copy is the defect.
- `V8 IDs and prefixes` — every rewritten-file ID remains in its draft, retired in place per
  *Stability*, or at its declared move destination; no renumbering or retired-ID reuse. Each
  prefix names one thing and appears on file index lines.
- `V9 Indexes, glossary and shape` — each file's index line names answered questions and prefixes,
  without status. Every named thing has a glossary entry under its governing item's home: meaning,
  purpose and routing, no inventory, position, appearance or binding, any detail supported by the
  items it links. Each live item opens with its statement and requirement link, a retired one
  carries the retirement form; orientation prose binds nothing.
- `V10 Completeness` — every binding the inputs require (requirements, drawings, the app in a
  backfill) traces to a governing item; an omission fails. Conditions are exhaustive and
  unambiguous, with precedence for overlaps. For each item, look for motion or polish a careful
  developer would not ship unasked — in the app's code in a backfill, otherwise in what the
  designer stated — and check it is specified; unstated motion is a Discussion item, never
  assumed absent.

## Cross-References

- [`spec-file-shape.md`](../Core/spec-file-shape.md) · [`design-specs-artifacts.md`](design-specs-artifacts.md)
- [`product-specs-catalog.md`](../ProductSpecs/product-specs-catalog.md) — mirrored conventions

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
