# Design Process Design

## Purpose

This document is the standard for SKAI's design process guides: what they are for, what they must
and must not contain, and the decisions behind them. It is used to write and cold-review them; it
is not something an operator reads at runtime.

- [`Guides/Design/design-authoring.md`](../../Guides/Design/design-authoring.md) — take a design
  change from an idea to approved mockups in a change package.
- [`Guides/Design/design-promotion.md`](../../Guides/Design/design-promotion.md) — move an approved
  package's designs into production and close the package.

The process mirrors SKAI's product specs process (authoring and promotion around a change package)
and the UI Map process (architecture and implementation). It is **tool-agnostic**: the conventions
a design must meet live in a design tool's own guide (for Figma,
[`figma-designer-guide.md`](../../Guides/Design/figma-designer-guide.md)); each process guide
loads the tool guide for the project's design tool, as UI Map implementation loads its stack guide.
The skills (`skai-design-authoring`, `skai-design-promotion`) are tool-agnostic.

Written 2026-10-12 from the planning discussion with the supervisor
(`skai/working-docs/work/swiftui-port/design-process/design-process-plan.md`, ephemeral).

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md), especially Guide house style
  and the standard structure for guides with gates.
- [`Guides/Core/process-flow.md`](../../Guides/Core/process-flow.md) for gates, advance intent,
  markers, and structured discussion items; the gate and advance-intent blocks are inlined
  verbatim in each guide.
- [`Guides/ProductSpecs/product-specs-authoring.md`](../../Guides/ProductSpecs/product-specs-authoring.md)
  and [`product-specs-promotion.md`](../../Guides/ProductSpecs/product-specs-promotion.md) — the
  parallel the design guides follow in shape, not in content.

## Requirements

1. **Tool-agnostic.** The process guides and skills name no design tool except to select its tool
   guide (one line, as UI Map implementation selects its stack guide). They assume only that a
   design file has named pages and a production area; the tool guide says what those are in its
   tool. Everything about what a conforming design looks like is the tool guide's.
2. **Open-ended input, no dependencies.** Authoring starts from whatever the supervisor brings. It
   depends on no other SKAI skill, and the guides never mention the UI Map, which is downstream
   engineering output.
3. **Conventions, not implementation.** Implementing designs in code is out of scope (may be added
   later as its own guides).
4. **Shape of the other SKAI workflows.** Change package at `skai/changes/<change-id>/`;
   discussion items in the canonical format; gates and advance intent inlined; `🏁 Complete.` at
   the end. A reader of the product spec guides should find nothing surprising in form.
5. **Lean.** Each guide holds what an operator needs at the point of use, and nothing it can read
   elsewhere. No session-specific mistakes codified; no defensive checklists.

## Settled decisions

- **Package**: `skai/changes/<change-id>/design/` holding `design-authoring.md` and (after
  promotion) `design-promotion.md`, beside any `product-specs/` or `ui-map/` type for the same
  change (SKAI Release 11's typed layout). The drafts live in the design file on a **change page**
  named `<change-id>`. Promotion archives the type to `skai/promoted/<change-id>/design/`.
- **Authoring artifact**: Goal · Inputs · Discussion · Design Changes · Assumptions and TODOs · Out
  of scope. Design Changes is a high-level inventory (which screens are new or changed, with links),
  written after approval; the designs speak for themselves.
- **Two phases that alternate and never overlap**: Discussion (items raised and resolved; nothing
  drawn) and Mockups (the agent draws on the change page; the supervisor reviews the designs).
  Mockups are the rendering of the resolved items and are new work to review, so they arrive only
  when the supervisor is done with proposals. Feedback on mockups goes into the designs; anything
  needing a recorded decision is parked and opens the next Discussion phase. Repeat until the
  supervisor approves.
- **Every item carries a written recommendation; nothing is drawn to make a proposal.** An item
  that can only be judged visually is deferred: the mockup takes the recommended option and feedback
  resolves it.
- **What earns an item**: a decision the agent needs — a proposed departure from the current app or
  design, behavior that looks like a defect, an open product question, a scope call. Design
  iteration itself is informal and earns none.
- **Approval is per change**: one approval of the mockups, then Design Changes is written.
- **Backfill is an ordinary change** through a change page; no baseline mode.
- **Deviations and defects are not formalised.** Those needing a decision are Discussion items; a
  change the supervisor asks for during review is recorded by the design itself; defects go to
  whatever bug tracking the project has, outside the guides.
- **Promotion**: readiness screen (items resolved, Design Changes written, every entry has a draft);
  checks that the drafts meet the tool guide and the inventory matches the page; production
  refactored to absorb the page; **the supervisor reviews production before the change page is
  deleted**; then the page is deleted and the package marked promoted. A requested design change at
  any point returns the package to authoring.
- **No archiving of designs**: superseded designs live in the tool's version history. The package
  itself is archived to `skai/promoted/` like every SKAI package.
- **No Concept pages**; the change page is where iteration happens.
- **Humans follow the same process**; no special case for hand edits.
- ~~**Requirements impact is not the guides' concern.**~~ Superseded 2026-10-18: a mockup decision
  that changes or adds a product spec is filed as a **change request** against the change's open
  product spec package (or the catalog), in the request format the product specs artifacts guide
  defines, optionally with proposed drafts; the designer never edits that package. Before the
  approval gate, one pass over the change page checks that every drawn state traces to a product
  spec and every package spec is served or recorded as out of scope, filing requests for the gaps.
  Design promotion waits until the package's requests are triaged. Reason: on Offers the concepts
  changed refresh scope, card content and an unseen model, and those decisions lived in a working
  document instead of the specs.

## Size budget

`design-authoring.md` is capped at **16,500 bytes** and `design-promotion.md` at **13,500 bytes**
(`wc -c`, managed headers included; the inlined gate, advance-intent and Project addendum blocks
count). Raised 2026-10-12 from 16,000 / 12,000 when SKAI Release 11's mandatory addendum footer
(about 750 bytes) and the package-archive step were added. This keeps each well under its
product specs counterpart (24,000 and 20,800). Every repair states its net size
cost; additions over the cap are paired with trims, and a fix that cannot fit is a supervisor
decision.

## Boundaries

The guides do not cover the tool's conventions, product specs, the UI Map, bug tracking, or
implementing designs in code.

## Amendments — 2026-10-18

- Design authoring files change requests for mockup-driven product spec changes and runs the
  whole-change trace pass before its approval gate (see the superseded decision above).
- The route depends only on the change-request format, cited from the product specs artifacts
  guide; requirement 2 (no dependencies) is otherwise unchanged.
- The additions cost budget; the caps are re-set by the supervisor at the next refinement, with
  16,500 / 13,500 bytes as the reference point.

## Size Budgets — 2026-10-18

Set by the supervisor from four efficiency reviews (SalesPro checkout, `working-docs/requirements-process/reviews/`), as today's size less measured obsolete content, less the reviewed trim on what remains, plus known growth. Whole-file bytes by `wc -c`, managed header and addendum footer included. They bind every repair per the refinement guide's size-budget rule.

These replace the 16,500 / 13,500 caps above.

| Target | File | Cap |
| --- | --- | --- |
| 3. Authoring | design-authoring.md | 14,400 |
| 3. Authoring | skai-design-authoring skill | 550 |
| 4. Promotion | design-promotion.md | 11,500 |
| 4. Promotion | skai-design-promotion skill | 500 |

Group caps across both spec types and the design process guides: authoring 54,900 (raised 2026-10-18 with design-specs-authoring); promotion 42,700.

**Live render (supervisor, 2026-10-18).** The rendered page is the primary way the supervisor views a change package while it is being iterated on. Any time the package materially changes — a draft edited, a discussion item resolved, a change item added, a request triaged — the agent validates and re-renders before anything else, in every workflow that writes a package. The gate and promotion renders are not the only ones; they are the last of many. Validation and rendering take milliseconds, so there is no cost argument for deferring them. A design package has no rendered artifact of its own, since its drafts live on the change page; the rule reaches it through the change requests it files, each of which has a page (settled 2026-10-18, target 3).

## Adopts — 2026-10-20 (known gaps)

Design authoring and promotion adopt [`product-specs-system-design.md`](product-specs-system-design.md)
§ Decisions — 2026-10-20 (format definitions and propagation) unchanged, with no tool: the **Gap**
sub-bullet, one Decision line, `## Decision Log` as the artifact's last section, the pointer
sentence to `known-gaps.md`, gap items carried past the Discussion gate, readiness item 1 failing on
an open gap. The Figma mirror of a gap (an annotation on the placeholder node) is a later slice.
Caps (supervisor, 2026-10-20, a little under the compressed sizes): `design-authoring.md` 15,100;
`design-promotion.md` 11,500 (unchanged). These supersede the 2026-10-18 rows.

## Adopts — 2026-10-21 (working docs placement)

Working documents serving a package live in its `working-docs/` folder and archive with it at promotion (`design-authoring.md` package table, `design-promotion.md` C6; caps held; skai#92, `Guides/Core/working-doc-conventions.md`); build and test output goes to the scratch root, never the package.

## Adopts — 2026-10-21 (gaps on the change page)

Design authoring mirrors each open gap on the change page as the tool guide says, once its
placeholder is drawn, and removes the mirror when the item closes (one sentence beside the gap
pointer in *Discussion*); design promotion's `C1` confirms no draft still mirrors a gap. The mirror's
form is the tool guide's (for Figma, [`figma-designer-guide-design.md`](figma-designer-guide-design.md)
§ Amendment — 2026-10-21). Caps held (15,100 / 11,500), each sentence paid for by trims in the same
guide (see `design-process-refinement.md` § Slice 5).

## Amendment — 2026-10-23 (change requests: authoring against a base)

Inventory for the guides, per skai#90 (inventory before prose; cap set after the compression
review). Decided with the supervisor 2026-10-23 (skai#99; prototyped on a project's design
package). Supersedes the settled decisions on the package path, the Design Changes inventory and
promotion where they conflict. No sizes here.

**design-authoring.md must say:**

1. A package authors against a **base**: production by default; for a **change request**, another
   open design package. Nothing differs but the base; a request against a request is one more level.
2. Paths: a package against production at `skai/changes/<change-id>/design/`; a request at
   `<base>/change-requests/<nnn>/`, numbered by filing order; the same folder contents, plus
   `change-requests/` and `promoted-change-requests/` when they exist; a request's first input is
   its base.
3. Drawings: a package against production draws on its change page; a request draws in a
   **request section** named `CR-<nnn> — <name>` on the base's change page, holding only what it
   adds or changes, a changed screen as a copy of the base's frame with the change, never an edit
   in place. The section's form is the tool guide's.
4. The rendered page `design-review.html`, written by `Bin/design-tool.py render`, is the
   supervisor's view: package card, Discussion, Design Changes; rendered on every material change
   and before every gate (the 2026-10-18 live-render rule now reaches design packages).
5. **No mockups**: when the supervisor, asked at the tool-access blocked gate, rules that none can
   be drawn, the Mockups phase is skipped; Design Changes is written from the decisions at the
   Discussion gate and is what the review gate reviews; the ruling is recorded under Assumptions
   and TODOs.
6. **Design Changes** is a typed list: `V<n> <add|modify|remove> <screen|state|component>:
   <identity>`, IDs never renumbered, no checkbox; identity the frame's name linked into the file
   (unlinked, the intended name, with no mockups); a **Description**, about a sentence with
   mockups, enough to draw from without them; a **Justification** with a source (spec citation,
   `Resolved decision: D<n>`, `Base decision: D<n>`, `Supervisor input`). Written on "approved"
   with mockups; a reopen that changes the designs or the list removes it until the next approval.
7. Whoever runs the workflow on a package authors it: a request filed by one person and continued
   by another is one package under one set of rules; the second run reopens it, raises what it
   finds as items, and may trim or change anything; no role rules.
8. A request's gaps: it inherits its base's open gaps like any input's; its own travel into the
   base at promotion.
9. Initiation signal for a request ("request a design change to <package>"); the path resolved as
   the next free number under the base.
10. Gates as today, the review gate covering both the drawings and, with no mockups, the Design
    Changes on the page; `auto` never bypasses it.

**design-promotion.md must say:**

1. Promotion folds the package into its base: into production, the drawings move from the change
   page into the production designs and the package archives at `skai/promoted/<change-id>/design/`;
   into a package, the drawings move from the request section into the base's drawings, the
   request's changes are appended to the base's Design Changes (the base's next `V` numbers,
   Description kept, Justification `Change request: <nnn> V<n>; …`, links to the new places), its
   open gap items are appended to the base's Discussion (next `D` numbers, Gap lines and mirrors
   kept, logged `gap`), the base's Assumptions name the promoted request, the base's page is
   re-rendered, and the package archives at `<base>/promoted-change-requests/<nnn>/`.
2. Readiness: non-gap items resolved; into production, gap items too; into a package, open gaps
   are carried by the fold-in. Design Changes written. Every linked entry reaches its draft; an
   unlinked entry allowed only with the recorded no-mockups ruling, and never into production.
   Promoted path absent (either form). Product spec change requests triaged, as today.
3. An undrawn entry folded into a package removes the base's approval: the base returns to Mockups
   to draw it; completion says what the base now owes.
4. Checks `C1`–`C6` as today, each stated for both bases: conventions (gap mirrors only block into
   production); inventory matches the drawings (page or section); the base absorbs the package;
   links point at the base; delete the drafts (page or section); archive (folder moved intact with
   its `working-docs/`, `change-requests/`, `promoted-change-requests/`; links repaired; page
   re-rendered).
5. The review gate is a **Base review**: the supervisor reviews production or the base's
   drawings before anything is deleted; a requested change returns the package to authoring with
   the base restored from version history.

**Clarification — 2026-10-23 (refinement r1, F4):** what represents a change is its drawing, or
under the no-mockups ruling its Design Changes entry. Rules by operation: an `add` or `modify`
entry links its draft and, after promotion, its place in the base; a `remove` entry names the base
design removed and keeps that name after deletion, with no link. Readiness, the inventory check and
the link check apply to the representation that exists; the review of the base covers its
drawings and, for entries folded in undrawn, its Design Changes; drafts are deleted where they
exist. Authoring items 3 and 6 and promotion items 2 and 4 read accordingly.

**Out of this amendment:** the product specs change request model (the design guide's paragraph on
filing requests against the specs package stays on the specs model until skai#99's sweep); a check
command for the design change list; embedded frame images on the page.

### Rulings — 2026-10-23 (after the compression review)

- **No approval word.** The gate after a round of drawings is an ordinary planned gate with the
  standard line; "next" there is the supervisor approving the designs. The list's presence is not
  evidence of anything; promotion readiness checks state. Amends authoring items 6 and 10.
- **The change list is live.** Design Changes is kept current from the first drawing on, as the
  specs keep theirs, so the page shows the round under review; "written on approved" and "a reopen
  removes it" go. Amends authoring item 6 and promotion item 2.
- **Reconcile inputs at that gate's advance, decoupled.** The guide names no upstream type.
  Inputs are whatever the supervisor brings (product specs among them). On "next" the agent
  reconciles the drawings against every input; for each input the decisions changed, it files a
  change request through that input's own process where one exists, with drafts, else tells the
  supervisor what the input needs; the package completes with those named. Requests are batched
  there, not filed per decision (cost: drafting and rendering per decision, and pulling the
  input's supervisor in on something still changing; the Decision lines hold the record until
  then). Replaces the Resolution paragraph that names the product specs request format, and
  the trace pass's "product spec" wording, with input-agnostic ones. Downstream work (design
  specs) is out of the design package's scope; completion names what it owes.

## Size Budgets — 2026-10-23

Set by the supervisor from the third compression round (`design-process-refinement.md` § Change
Requests: Authoring Against A Base), a little under the compressed sizes; whole-file bytes by
`wc -c`. These replace the 2026-10-20 caps and bind every repair.

| File | Compressed | Cap |
| --- | ---: | ---: |
| design-authoring.md | 16,210 | 16,100 |
| design-promotion.md | 12,206 | 12,100 |

## Amendment — 2026-10-23 (change list mirrors the page)

Inventory per skai#90. Decided with the supervisor 2026-10-23: the change list is organized so a
reviewer walks it the way they walk the canvas.

**design-authoring.md must say:**

1. `## Design Changes` groups entries under `### <screen>` headings in canvas order (sections,
   then columns, left to right); under a heading, one entry per frame, top to bottom. A frame
   with several changes lists them as sub-IDs `- **NN** <description> — <justification>` under
   the entry, the way a spec item lists rules; a single change keeps Description and Justification
   on the entry. IDs stay stable and form one sequence per package: a later frame takes the next `V`, placed
   under its screen's heading; a later change to a frame takes the next sub-ID. The renderer shows the headings and the sub-changes.
2. Before the Review gate, run the tool guide's structure check on the page or section and fix
   what it reports.

**design-promotion.md must say:**

1. `C1` runs the structure check. `C2` inventories per section.
2. `C3`: a request's per-screen sections fold into the base's same-named sections (a new
   section where the base has none); into production the per-screen sections do not survive:
   every column is regrouped into `Production`'s feature areas as the tool guide places it.

**Out of this amendment:** the page's renderer mechanics (`design-tool.py`), tested on their own.

## Size Budgets — 2026-10-23 (change list mirrors the page)

Set by the supervisor after the compression round of this amendment, 100 bytes under the
combined proposal "to keep the refiner honest"; whole-file bytes by `wc -c`. These replace the
earlier 2026-10-23 caps and bind every repair.

| File | Draft | Cap |
| --- | ---: | ---: |
| design-authoring.md | 16,614 | 16,450 |
| design-promotion.md | 12,278 | 12,150 |

## Amendment — 2026-10-23 (inherited gaps as footnotes)

Inventory per skai#90. Decided with the supervisor 2026-10-23: a gap this package inherits from
an input is not a question it is asking, so it is not a Discussion item; it is a mark on what
stands on the placeholder, as the spec files mark theirs. Discussion holds only the gaps the
design itself raises. Adopts the same-day amendment of `known-gaps-design.md`.

**design-authoring.md must say:**

1. An inherited gap is a footnote on the Design Changes entry, or sub-change, whose frame stands
   on the placeholder: `[^n]` ending its text, defined under the entry as
   `[^n]: **Gap:** <owning item> — <question>. Placeholder: <one line>`, the owning item named as
   `product specs D21` or `base D04`; labels unique per artifact. The design file mirrors it as the
   tool guide says. A gap of this package's own stays an item with a Gap line, mirrored the same
   way once its placeholder is drawn.
2. "Open gaps" at the Discussion gate and in the card's state count both: open gap items and
   footnoted entries.
3. The renderer shows the footnote under the entry's card and counts it in the gaps tile.

**design-promotion.md must say:**

1. Readiness 1: into production no open gap of either kind; into a package `C3` carries both.
2. `C3` into a package: the package's own open gap items are appended to the base's Discussion as
   today; footnotes ride with their entries, and one naming the base's own item names it as the
   base's (`base D04` becomes `D04`).

**Out of this amendment:** the UI Map's gap mirror.

## Size Budgets — 2026-10-23 (inherited gaps as footnotes)

Set by the supervisor after the compression round, a little under the compressed sizes; whole-file
bytes by `wc -c`. These replace the earlier 2026-10-23 caps and bind every repair.

| File | Compressed | Cap |
| --- | ---: | ---: |
| design-authoring.md | 16,817 | 16,750 |
| design-promotion.md | 12,143 | 12,100 |

## Adopts — 2026-10-24 (the shared gap footnote)

Design authoring's inherited-gap footnote is `spec-file-gaps.md`'s form, cited, not restated (one
per entry that stands on a placeholder). Rendering rulings of 2026-10-24: the owning item's chip
shows the ID alone; its tooltip leads with the owning review page's path when it is another
document; a card's notes share one box; one line per note, no "Gap" or "Placeholder" labels on the
design page; marks are inert. These supersede the footnote form in § Amendment — 2026-10-23
(inherited gaps as footnotes), item 1.
Cap after the shared-footnote change: `design-authoring.md` **16,550 bytes** (compressed 16,616; supervisor, 2026-10-24), replacing 16,750; promotion stays at 12,100.

## Amendment — 2026-10-24 (descriptions say what changed; reasons are sentences)

From the Offers request CR-001 (supervisor, 2026-10-24: entry V06 was unreadable). Three instruction
defects in `design-authoring.md` § Design Changes, repaired there; the writing rules themselves move
to the new shared `writing-style.md`, reached by the pointer sentence process-flow owns.

- **Description** names what changed on the screen, state or component, in the product's words,
  about a sentence; it is not a visual diff of the frame and never names sample data. With no
  mockups it is enough to design from.
- **Justification** is the reason in a sentence, then its source (an input citation, a decision of
  this package or its base, or supervisor input). A citation alone is not a justification. The
  sub-change example carries a reason before its citation.
- An inherited gap's footnote goes on the entry or sub-change whose **change rests on** the
  placeholder; a frame that merely keeps what the base already shows gets none. The footnote's
  Placeholder clause is the provisional answer the entry builds on (spec-format's form), not a
  restatement of the frame.
- The guide keeps its tool-neutral vocabulary (draw, drawings, the package); `writing-style.md`
  tells the agent not to carry it into what a person reads.

Cap: **16,850 bytes** for `design-authoring.md` (compressed 16,786, installed 16,865 after plain-language corrections; supervisor, 2026-10-24), replacing 16,550.

## Adopts — 2026-10-25 (the shared change requests guide)

`design-authoring.md` points at [`change-requests.md`](../../Guides/Core/change-requests.md) for the
base, the request paths and folders, the request signal and filing against inputs, keeping only what
is the design tool's (the request section, copies of base frames, the fold of frames). `design-promotion.md`
readiness 5 points at the shared rule on requests filed against inputs; readiness 1 and C3 carry the
2026-10-25 ruling that into a package open items, gaps and requests move up a level. Caps (supervisor,
2026-10-25): `design-authoring.md` **16,000** (was 16,850), `design-promotion.md` **12,000** (was 12,100).

## Size Budgets — 2026-10-25

Series PL (plain language): `design-authoring.md` **16,000** and `design-promotion.md` **12,000** hold (supervisor, 2026-10-25); the Resolution sentence swept from process-flow and the provenance tag order fit under them by hand trims.

## Amendment — 2026-10-28 (an inherited gap's footnote once)

Supervisor, 2026-10-28 (the Offers CR-001 review; SK-01 of that review): an inherited gap's
footnote goes only on the first entry or sub-change, in list order, whose change rests on that
placeholder; a later entry building on the same placeholder carries none. This matches the Figma
annotation, which marks each gap once at its first occurrence in canvas order, the order the
change list follows (`figma-designer-guide-design.md` § Amendment — 2026-10-28). The rest of the
2026-10-24 footnote rule (on a change that rests on the placeholder, never on what a frame merely
keeps; the Placeholder clause is the provisional answer) stands.
Cap: `design-authoring.md` **16,000** holds (compressed 15,992; supervisor, 2026-10-28).
