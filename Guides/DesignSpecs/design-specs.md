Managed-By: skai
Managed-Id: guide.design-specs
Managed-Source: Guides/DesignSpecs/design-specs.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Design Specs

Print `📖 SKAI guide: design-specs` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

A **design spec** joins a screen's design to its requirements: drawn states and their conditions,
data formatting, variable copy, controls, destinations and referenced shared patterns. The UI Map is downstream of requirements, design and spec and references none of them.

Write for an implementing agent with the design and requirements open, in product-manager language.
This guide owns content and the ten checks, not gates. File layout — headings, statements, rules,
tables, known differences, links, IDs and anchors, glossary and index form, the validating tool — belongs to [`spec-file-shape.md`](../Core/spec-file-shape.md), cited,
never restated. [`design-specs-authoring.md`](design-specs-authoring.md) drafts;
[`design-specs-promotion.md`](design-specs-promotion.md) promotes.

**Inspect changed items and every touched file whole; block only on what this package changed.**
A pre-existing fault in unchanged content, held file or not, starts a package against the
base ([`change-requests.md`](../Core/change-requests.md)); only a contradiction that would make
the write inconsistent blocks. `validate` faults in held files and conflicts the projection
introduces always block. Work-spec implementation may update or remove
known-difference notes after verified fixes; spec text and IDs are otherwise read-only.

### What Belongs Here

One home per fact. **Requirements** own screen-independent promises and thresholds; **design** owns
appearance and drawn copy; **specs** own how screens present promises — conditions and states, formatting
constants (rounding, a `1 min` floor), variable copy, controls by function, destinations. Cite requirements without restating them
(*Restatement*). A spec that narrows a requirement, such as hiding a notice in an unmentioned
case, is a requirements gap, routed as authoring § Requirements Gaps says, never
specified quietly.

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

Put each rule in the first fitting home: screen; family file under `screens/`; `shared/` for
cross-family pieces; `global/` for patterns every screen uses (loading, errors, empty states).
Extract before first repeating a rule. Cite another spec's rule rather
than copying it; only a declared override restates (*Citing by Reference*). ❌ a screen file
repeating the family's heading rule · ✅ "Headings follow the list family's rule ([UI-LIST-01-02])".

Create all three folders and indexes immediately.

### Indexes

The root index holds a product paragraph naming the design file and requirements, a folder map
with one-line reminders, and the glossary as second index; status text belongs in the package.
Each file's folder-index line follows the shape guide: every prefix held (including those spanning
files after a move), questions answered, then optional `(uses: …)` references. Name questions, not subjects: ✅ "Which row and reminder
badge a note gets, its date format and tap action".

### Glossary

`glossary.md`, the second index, answers cross-screen questions. Give every named thing (rows,
cards, badges, notices) one short product-language paragraph: **meaning and purpose**, then links
to governing items; one or two identifying details may follow. Never
inventory elements, position or appearance; never bind — conditions, formats and precedence
belong in the linked items. Every occurrence of a term in spec prose links its entry (`link-terms`).

❌ *Transfer notice* — a blue banner with an icon, a heading and two links below the toolbar.
✅ *Transfer notice* — explains an unfinished transfer; dismissible ([UI-TRANSFER-03]).

Sections are **Global**, **Shared**, then each screen family, with alphabetical entries under their
governing item's home. Entries move with their items; extracted cross-family terms sit in Shared.
Read Global, Shared and the current family. Split an overgrown glossary per folder along these seams. A thing named like a
requirements term gets an entry identifying the drawn element and crediting the requirements for
the concept ("the pin glyph at a row's leading edge; the requirements say when a note is pinned ([NOTE-08], [UI-NOTES-01])");
requirement terms themselves (*overdue*, *stale*) get no entry.

## Items

An item has one `###` heading with its ID in the shape guide's form. Its opening sentence names
its subject and links the requirement it presents — ✅ "The [reminder
badge][g-reminder-badge] shows the note's reminder state ([REMIND-02]):" — then its rules; data
(mappings, strings) goes in tables, never under rule numbers.
A `##` part groups items and may open with one nonbinding orientation line; what shows or when
belongs under an item.

- **Contract unit:** an item is its rules and its data; data edits follow *Modify vs. Retire*.
- **Conditions:** exhaustive and unambiguous; state precedence for overlaps ("the first that holds").
- **Known differences:** only observed app/spec differences, under the affected item with a tracking
  issue when available; gaps, not exceptions. Platform words belong only here.
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
overrides. Overrides may restate parents with modifications; without a declaration, the inherited rule stands.

## IDs

Form and anchors follow the shape guide; `UI-` distinguishes spec IDs from requirements. Prefixes
uniquely name the thing (screen, family, shared piece), never its file; include its kind for abstract
nouns (`UI-DEFAULT-FOLDER`, not `UI-DEFAULT`). Next number: one above the prefix's base maximum, including
unpromoted IDs; collisions between packages surface at the later promotion.

### Stability

IDs are file-independent and append-only from first drafting. Moves never renumber; restructures
use `move` items. Retired IDs are burned. Retire in place: keep headings and rule numbers; replace binding text with a
sentence saying in product words what replaced it, then its citation; retiring a parent retires its
descendants.

### Modify vs. Retire

**Modify** keeps the ID for a clarified promise that existing citations still mean.
**Retire and add** when a changed contract makes previously conforming behavior nonconforming. Append new rules under a parent; a changed rule retires and is replaced there; moving a
rule to another parent is retire-and-add. Before either, run `references`
and decide per citation whether it still holds.

## Writing Style

Write as a **product manager describing a screen to a developer who sees the design** in canon,
drafts and quoted proposals; package prose names a frame, node or code file only where the reader must go to it.

### Product Language Only

Use product terms ("compact card", "stale notice"), never design-tool frame, component, variant or
property names, URLs or node IDs; raise drawings unfindable by product name in Discussion. No jargon or coined phrases: "a tip pointing at the profile button", not
"platform-rendered TipKit popover". Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

### Never Appearance

No color, position, shape, size or style in rules, intros or glossary entries.
**Would a purely visual redesign falsify the sentence without changing what the thing is,
is for, or does?** If so, delete it: design owns appearance. Exceptions: established product
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

Describe what people see, not platform mechanisms: "a standard tip bubble", not "a standard
iOS tip bubble". Rules cover all apps; tablet/phone adaptation is a condition. Log single-app
verification in package Assumptions.

### Restatement

A sentence citing a requirement adds a screen binding beyond the cited contract; one that adds
nothing goes, or names in words the rule it applies, never a bare citation. "Tapping anywhere on
the row opens the note ([NOTE-05])" adds a tap target; "The list refreshes when pulled down
([SYNC-06])" adds nothing.

### What Counts as a State

- **Screen state:** different layout. Design draws it; spec binds its condition.
- **Component appearance:** same layout, conditional styling (badge styles, heading looks).
  Design draws variants; spec binds each condition to a variant by product name.
- **Data substitution:** different string, same look (per-notebook empty messages, day-heading
  text). Specify data; no drawing.
- **Motion and polish:** transitions, animation, timing, haptics, loading and refresh feel,
  entrances and exits. Design cannot draw these; a careful developer will not add them unasked.
  Specify under the item what moves, when and what it conveys ("the new row slides in from
  where it was added, so the person sees where it went"), never easing curves or pixels.
  ❌ "the label gives way to an indicator" (a substitution, not its motion) · ✅ "the label fades
  out as the indicator fades in".

An element disappearing without moving the rest (a missing date) is a component property;
internal reflow does not count, and not every combination is drawn. For unstyled standard system
UI (tips, alerts), specify conditions and choices; no drawing is required, and specs never say whether it is drawn.

### Nothing That Decays

Omit temporal references ("as before the redesign") and workflow state; specs must outlive memory
of the change.

## Verification Checks

Before authoring's Discussion gate advances and before promotion writes, run the spec tool's
`validate` over the drafts projected on canon: a fault in a file the package holds, or a conflict
the projection introduces, blocks; a fault in an untouched canonical file is reported and starts a package against the base. Then these ten checks, enumerated only here, over the scope in *Purpose*.

- `V1 Restatement` — requirement-citing binding prose adds a screen binding beyond the cited
  requirement. Nonbinding orientation and routing are `V9`'s.
- `V2 Appearance` — inspect sentences, including glossary entries, against *Never Appearance*'s
  redesign test. Evidence names inspected sentences, never a word list.
- `V3 Product language` — no design-tool or code identifier or mechanism anywhere in spec text;
  platform names only in known-difference and Also called notes (*Product Language Only*); changed sentences read as the writing guide says.
- `V4 Static copy` — quoted strings are formats, data-dependent or undrawn copy.
- `V5 Drawn state` — find every prescribed screen state or component variant by product name in
  production or approved change-page mockups ([Figma](../Design/figma-designer-guide.md)), from
  any package; unapproved drafts do not count. Unstyled standard system UI is exempt; unavailable
  access blocks.
- `V6 Links` — definitions reach intended items, not just files; overrides link superseded rules
  and parents never name overrides; pending specs use `(spec pending: <file>)`; tracking links
  identify issues.
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
- `V10 Completeness` — every binding required by inputs (requirements, drawings, the app in a
  backfill) traces to a governing item; omissions fail. Conditions are exhaustive and unambiguous,
  with precedence for overlaps. For each item, check that motion or polish a careful developer
  would not ship unasked is specified: inspect app code in a backfill, otherwise the designer's
  statements. Unstated motion is a Discussion item, never assumed absent.

## Cross-References

- [`spec-file-shape.md`](../Core/spec-file-shape.md) · [`design-specs-artifacts.md`](design-specs-artifacts.md)
- [`product-specs-catalog.md`](../ProductSpecs/product-specs-catalog.md) — mirrored conventions

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
