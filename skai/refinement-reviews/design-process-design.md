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

## Amendment — 2026-11-11: Items Stay Where Raised (skai#118)

The design guides adopt [`product-specs-system-design.md`](product-specs-system-design.md) § Amendment — 2026-11-10 with `V` for `R` and `C3`–`C6` for `C7`/`C8`; the shared rules are `change-requests.md`'s ([`change-requests-design.md`](change-requests-design.md)). Recorded during the refinement pass for that change.

1. **Change item source** (`design-authoring.md` § Design Changes): `Resolved decision: D<n>` cites a Discussion item, another package's by link; `Base decision: D<n>` is retired.
2. **Readiness into production** (`design-promotion.md` condition 1): no open item, request, gap or footnote in the package, nor in its promoted requests at any depth, where a footnote whose gap closed is history (corrected after cold round 5: the exemption covers archived requests only, so a stale footnote in the live package still blocks).
3. **Folding into a package** (`C3`): the type guide folds screen sections and appends change entries, each under its screen, a change to a frame the base already lists as the next sub-ID under the base's entry (authoring's one entry per frame; supersedes § Amendment — 2026-10-23's "the base's next `V` numbers" for that case; Offers design CR-001 folded this way); a footnote whose gap the base owns, or one the base already carries for the same gap, is dropped (only inherited gaps are footnoted, one each); footnotes, base-item decisions and open requests fold per `change-requests.md`, named by file; mirrors follow the tool guide's Gaps rules (move with their frames, update on owner-path changes, removed when the owning item closes) (corrected after cold round 1: `change-requests.md` has no mirror rule).
4. **Archive** (`C6`): the package moves with `working-docs/` and `promoted-change-requests/`; open requests never reach archive. After the move, the moved page and a request's base are re-rendered, so the base's page shows the request's items where they now live.
5. **Completion** names the gaps left open, where they were raised.

Caps: `design-authoring.md` 16,000 holds (15,953 before this pass); `design-promotion.md` **12,100** (was 12,000; 11,878 before this pass; supervisor, 2026-11-11, after cold round 5, so the fold rulings are written out rather than compressed). Compression round skipped: each change replaces a clause in place.

## Amendment — 2026-11-11: Requests As Folders Of Sub-Packages; Confirming The Route (skai#108, skai#129)

Adopts [`change-requests-design.md`](change-requests-design.md) § Amendment — 2026-11-11: this standard's guides say the items that amendment lists for their kind of guide (artifacts, authoring, promotion, Figma), and every request path, ID and provenance tag in them takes the new form. Caps for this change: `change-requests-design.md` § Amendment — 2026-11-11 (supervisor, 2026-11-11).

## Amendment — 2026-11-11: A Fold Carries Every Change; The Change List Says What Changed; Scratch (skai#111, skai#106, skai#100)

Rulings: skai#111 (body updated 2026-11-11, with the CR-001 fold's prototyped process and mistakes in its comments), skai#106 and skai#100 (supervisor, 2026-11-11; the B1 plan's Q1–Q3, Q7–Q12). Supersedes `C3`'s "designs outside the inventory change only by the placement and relocation the tool guide needs to absorb them", § Amendment — 2026-10-24's "not a visual diff" for modify entries, and the base review's "restore the base from version history". Inventory per skai#90, before prose.

**design-promotion.md must say:**

1. **A package's drafts illustrate its changes; the fold carries every change across the whole base.** This holds for every fold: a request into its base package, and a change's own package into `Production`. A changed screen is drawn once or twice to show a change; the fold applies that change to every base frame it affects, whether or not the package redrew it.
2. **Work from the change list, change by change.** List the rules the changes set (each: what it says, the entries that set it); audit every base frame against them, by rule and by eye, hosts behind sheets, dialogs and popovers included; record the audit in a working document (frame, rules that apply, what changes). Updates that follow from the package's changes are applied; removing a frame, or redrawing beyond the package's changes, goes to the supervisor.
3. **Back up the base before it changes, and copy, never move.** The backup and the drafts stay until the supervisor deletes them (supervisor, 2026-11-11: for now). Where they go is the tool guide's.
4. **Apply, then look.** Screenshot every touched frame; check what copying can break (pairings such as a tab's unread dot and unseen content on screen, a header pattern that belongs to one stage, component references to the request's copies).
5. **Record it.** Into a package: the package's entries append per `change-requests.md` (unchanged), and changes propagated to the base's own frames are recorded on the base's entries (a sentence on an add entry, a sub-change on a modify entry, a remove entry for a trim). Into production: the evidence carries it.
6. **Evidence names every base frame inspected and what was applied**, so a frame swap cannot pass as a fold.
7. **Base review**: a requested design change restores the base from the backup and returns to authoring; advancing the gate no longer deletes the drafts (`C5` runs only when the supervisor asks).
8. The prototype's independent cold review of the fold (step 11) is a candidate step; the proposal review weighs whether it earns a place.

**design-authoring.md must say:**

9. **The change list is written for the promoting agent as well as for people** (supervisor, 2026-11-11): it follows `writing-style.md` and states precisely each change the fold must carry, so the promoter can find every frame it affects.
10. **Description says what changed; Justification says why (skai#106; supervisor, 2026-11-11).** For every entry, the Description says what changed in a reader's words: anything new is named, not described (no account of its design); no measurements, style names or sample data. Why it was added, changed or removed is the Justification's. The rule itself lists no element kinds (screen, state, component, card): it holds at any level. One example each for added, changed (with a ❌) and removed.
11. **Scratch (skai#100), kept minimal** (supervisor, 2026-11-11: rapid, low-friction exploration; don't over-engineer). The supervisor may ask for exploratory work in a scratch Section on the change page; it is outside the change list and the structure check. Scratch is settled in the session that made it: what the supervisor keeps is carried into the package's frames, every change to every frame it affects, and listed.
12. Drawings sit in the package's container Section on the change page; the tool guide owns its form.

**Writing style:** unchanged (supervisor, 2026-11-11). It covers everything a person reads, not only designs, so the visual wording of a modify entry stays in `design-authoring.md`; rule 3 is about naming the thing, not the instance, and does not conflict.

**Tools:** `figma-page-check.js` per the tool guide's amendment of the same date.

**Caps (supervisor, 2026-11-11, after the proposal review and compression; a little under the compressed sizes):** `design-promotion.md` **13,350** (compressed 13,390); `design-authoring.md` **16,650** (16,681). The writing style guide is unchanged (supervisor, 2026-11-11).

## Amendment — 2026-11-17: How Designs Are Drawn (skai#74, skai#104, skai#107, skai#110, skai#112, skai#113, skai#126, skai#141)

One amendment for a whole stream of changes, written before any guide text so each guide is rewritten once: the Figma guides first, then these two, each in its own refinement pass. The tool guide's half is [`figma-designer-guide-design.md`](figma-designer-guide-design.md) § Amendment — 2026-11-17. Sources: the tickets above; the practices and failures recorded from a full design backfill (the comments on skai#110, skai#126 and skai#72); supervisor rulings of 2026-10-22, 2026-10-26, 2026-10-31, 2026-11-16 and 2026-11-17, cited where they apply. Planning record (ephemeral): the host checkout's `skai-plan/stream-f-plan.md`.

The guides today say where things go and how a change is recorded. This amendment adds how to draw well, in the order a design session meets it.

**Supersedes:**

- Requirement 1's "assume only that a design file has named pages and a production area". The process guides also assume a component library and a design system of named styles and values, and name them in those words. What each is in a tool stays the tool guide's.
- § Settled decisions, "Two phases that alternate and never overlap", for a package whose mockups already exist (item 11).
- § Amendment — 2026-11-11 (A Fold Carries Every Change): item 1's "drawn once or twice" (item 2); item 3's "until the supervisor deletes them" (item 20); and item 7's restore, which now reaches the design system (item 18). Item 3's "copy, never move" stands for the package's drafts.
- § Amendment — 2026-10-23 (change list mirrors the page), item 1: the list also holds design system entries, which are not frames (item 8).

**design-authoring.md must say:**

*Know the file (skai#74, skai#107, skai#110)*

1. After reading the tool guide and before the first Discussion item or drawing, read from the design file its recorded conventions, its app-wide designs, and what its component library and design system already hold; and read any specs among the inputs, or linked by the project, that say how the app-wide designs apply. The tool guide says where each of these is in the file. Design authoring never requires such specs (supervisor, 2026-11-16).

*Decide what to draw (skai#141, skai#107)*

2. A package draws each distinct change. It does not have to draw every frame that change lands on. Each distinct change is drawn in as few frames as show it, normally one, cropped where the tool guide's crop rule applies, and its Description says where else it applies; promotion carries it there, as `design-promotion.md` already says. A package that does this is complete. Where the design file keeps screens at several target sizes, the tool guide says what the package also draws at each size.
3. A case an app-wide design already covers is not drawn again and raises no Discussion item. The change entry that relies on it, or `## Out of scope`, cites the app-wide design by name, and the case then counts as covered. A screen that departs from an app-wide design is an ordinary change to that screen: drawn and listed (supervisor, 2026-11-16). Where it is unclear whether an app-wide design covers a case, that is a Discussion item.
4. Which states earn a frame is the tool guide's rule; this guide points to it and does not restate it.

*Draw with what exists (skai#110; supervisor, 2026-10-31)*

5. A `## Design Practices` section: a short list, each practice with a stable ID `DP-<nn>` (never reused; a retired practice keeps its line, marked retired), a bold name, and a statement in words that fit any design tool. Each is self-contained. Why the IDs (supervisor, 2026-10-31): the list is meant to grow into a catalog shaped like the spec catalog, files of practices with an index whose descriptions let the agent read only the practices that apply to the change at hand (skai#149). It stays a list in the guide until it is large enough to need that. Stable IDs let a review or a change list cite a practice, and the citation still resolves after the move. They are a trial of stable rule IDs, which may later extend to other guide rules, whose numbers are positional today. The starting list is five (supervisor, 2026-11-17; two further candidates, a general habit of looking for the same mistake elsewhere and a check on frames made from copies, were dropped):
   - **DP-01 Look before drawing.** Check the component library, the styles and the values for something that fits before drawing anything. Where something nearly fits, add a variant or a property to it as a drafted change; never draw a lookalike.
   - **DP-02 What recurs is defined once.** An element that recurs across screens (a card, a row, a header) is a component and each use an instance; a look that recurs (a separator, a field shape) lives in one component or value that screens inherit. Ordinary content that happens to repeat is not meant. The definition exists by the time the package is reviewed. A fix is made to the definition, so every use gets it.
   - **DP-03 A change to something shared is checked everywhere it is used.** Before changing a shared component, style or value, see where it is used; after, look for the old look surviving anywhere, the component library's own examples and other features' screens included.
   - **DP-04 Content goes in through component properties.** A component has a property for what varies from one use to the next (a label, an icon, an optional part); screens set properties and never detach or restructure an instance.
   - **DP-05 States live in the component; screens choose them.** A control's states and a recurring overlay's forms are variants in the library; a screen picks one of them and does not draw its own.
6. The practices apply to everything drawn, a scratch Section included, because what the supervisor keeps becomes production. Scratch stays outside the change list and the structure check (supervisor, 2026-11-11, unchanged).

*Change the design system in the package (skai#126; supervisor, 2026-10-26 and 2026-11-17)*

7. Authoring never changes in place how a production style, value or component looks. A package that needs a new or changed one drafts it in the form the tool guide gives, and its mockups use the draft; production's own stays as it is until promotion. Only what changes is drafted, plus **supporting copies**: the few components copied only to show a changed one inside them. Nothing else that depends on a changed item is drafted.
8. Every design system change is a `## Design Changes` entry. Entries gain a kind, `style`, beside `component`: any named style or value of the design system (a color, a text style, an effect, a dimension). One entry per item, under a heading named for the place the design file shows the package's design system drafts, in canvas order like any other. Identity is the item's name: for `add` and `modify`, linked to where the draft is shown and, after promotion, to where the base shows the item; for `remove`, unlinked. The Description says what changed in a reader's words, as for a screen. A `remove` entry drafts nothing and says what each use of the item becomes. A rename is a `modify` entry that drafts nothing: its identity is the item's current name, unlinked, and its Description gives the new name. A supporting copy is not a change and has no entry.
9. A structure-only fix is not a change (supervisor, 2026-10-26). Replacing a hand-drawn element with a component, or a raw value with a named one, so that nothing looks different, is made directly in the base, production included, with no package, request, draft or entry. The agent verifies that each affected screen looks the same before and after, saves the comparison as a working document serving no package ([`working-doc-conventions.md`](../../Guides/Core/working-doc-conventions.md)), and says where it is in its report (supervisor, 2026-11-17).

*Keep the canvas readable and current (skai#112, skai#104)*

10. Every screen frame the package draws carries a purpose note in the design file, in the form the tool guide gives (it also says which frames carry one where a screen is kept at several target sizes): written when the frame is drawn, and rewritten when what the frame is for changes. It is separate from the change list: a Description says what changed, a note says what the frame is for, and the two never disagree.
11. Once a package has mockups of its own (on a reopen, or any time after its first drawing round; a new request with nothing drawn yet is a first pass), resolving a Discussion item updates the affected frames, the change list and the gap mirrors along with the Decision line, before anything else is done (for an agent, in the same turn), and the page is re-rendered. The Mockups phase still draws what has never been drawn. A first pass with nothing drawn is unchanged.

*Check before review (skai#107, skai#110, skai#113, skai#141)*

12. The tool guide's structure check reports two kinds of result. Breaches are fixed. Signals are looked at and judged; a signal is never fixed by rote.
13. One check with three parts then replaces the trace pass:
    - **Coverage.** Every drawn state traces to an input. Everything the inputs ask of this change is drawn (once, per item 2), covered by a cited app-wide design (item 3), or under `## Out of scope`.
    - **Reuse.** The practices hold across the package's frames, and every design system change is listed, and drafted where it needs a draft (items 7 and 8).
    - **Sample data.** Within a frame, what is shown could occur together (states, dates, counts, statuses, indicators). Across related frames, the same sample people and records agree. Against the inputs, what is shown follows them (ordering, grouping, what a state requires) and every indicator has what it indicates on screen. An edge case is drawn once, on the frame that is about it; frames showing the main case do not also show it. Each frame shows what its purpose note says it is for.

    A finding is fixed, or becomes a Discussion item where the inputs and the drawing disagree and the call is the supervisor's.
14. Items 2 and 3 state what makes a package complete, so anyone reviewing a package from the guides reaches the same answer: a repeated change drawn once and a case covered by a cited app-wide design are not missing drawings.

*A large rollout*

15. Withdrawn (supervisor, 2026-11-17). Reviewing a large mechanical rollout after its first Sections belongs with backfill, which the guides leave light; see *Out of this amendment*.

**design-promotion.md must say:**

16. Purpose notes travel with their frames into the base, production included, and are never stripped. The fold rewrites a note that no longer fits, such as a draft's "the one change this frame shows" on what is now the approved design of a whole state (supervisor, 2026-11-17).
17. `C2` inventories design system drafts as it does screen drafts, both ways. A supporting copy has no entry; a `remove` or rename entry has no draft and names an item the base has or, for a base package, uses from production. This inventory is the check skai#126 asks for: a design system change listed with no draft was never drafted, or was made in place, and fails `C2` by name. A change made in place and never listed is beyond any check.
18. `C3`, the design system (supervisor, 2026-11-17). A **shared definition** is a style, a value or a component. A **use** of one is anything that refers to it: a frame's or a component's binding or instance, and another definition's reference (a text style's size, a value that points at another value). Three rules hold throughout:
    - **Nothing is lost before the base is approved.** The fold deletes no definition and leaves the package's drafts as they are.
    - **Identity is kept.** A definition the base already has is changed and restored in place. It is not swapped for another object, because its uses follow its identity. The fold applies the change the entry lists to it; it does not replace the definition with the draft.
    - **Afterward nothing in the base uses the promoted package's drafts,** in any frame or definition, on any page the fold changes. This extends `C3`'s existing check for an instance still linked to a draft's component.

    Into production, for each entry:
    - **Changed:** back up production's definition, then apply the change to it in place.
    - **New:** copy the draft into place under its final name. It needs no backup.
    - **Renamed:** rename production's definition in place.
    - **Removed:** point each use in the base at what the entry says it becomes, then move production's definition aside into the backup. Uses outside the base are left alone, as the first rule requires: the package's own drafts, backups and other open packages keep using the definition that was moved aside, and a cleanup that would delete it blocks while they do (item 20).

    Into a base package, production is never touched: the base package's draft of an item stands where production's definition does above. Where the base package has no draft of an item the request changes, one is made for it from the current definition with the request's change applied, and the base package's uses of the item are pointed at it. A removal or rename of an item only production defines carries its entry to the base's list, and production's definition waits for that package's own promotion. Until then a removal re-points the base package's uses of the item; a rename changes no use, since uses follow the definition's identity and that definition is renamed only when the base package is promoted. An undrawn entry is carried as `C3` already carries one.

    Then every use of a draft in what was copied into the base is pointed at the base's definition, a supporting copy's uses included, with the care after each swap that the tool guide gives. Where the design file keeps screens at several target sizes, the fold keeps every size's set complete, as the tool guide says.

    The base's own documentation of its design system is brought up to date: production's when the base is production, the base package's when it is a package. How each step is done in the tool, the names, and where backups go are the tool guide's. `C3`'s evidence names each definition and what was done to it. A fold run again after a return to authoring replaces the earlier run's backups.

    At the Base review gate, the existing restore on a requested design change covers the design system changes too. The promotion guide adds only those words; the steps are the tool guide's (supervisor, 2026-11-17).
19. The sample-data part of authoring's check runs again on the merged base, with `C3`'s look at every touched frame: a fold puts frames beside frames they were not drawn with.
20. **Cleanup** (supervisor, 2026-11-17). On the supervisor's request for a named package, any time after its promotion completes and usually in a later session, the agent removes everything the package left in the design file: its change pages or request Section; its backups; its drafts of styles, values and components; and the definitions the fold moved aside. It finds them by the tool guide's names alone and needs nothing from the session that promoted. Cleaning up a change's own package takes with it whatever that change's promoted requests left. It first confirms that nothing outside what it is deleting still uses any of it; anything still in use blocks the cleanup and is named. The request is the approval to delete, for that package only. It reports what it removed and records that as evidence in the archived promotion artifact. Deleting by hand stays possible. This replaces "the supervisor deletes drafts and backup" in the Purpose and Completion, and Initiation gains the signal. The `skai-design-promotion` skill's description gains the trigger.

21. **Another package changed the same thing first** (supervisor, 2026-11-17, replacing the same day's earlier readiness condition that sent the package back to authoring). Promotion merges the package's changes into the base as it stands, which `C3` already does by applying each listed change to the base's own frames and definitions. A package is never sent back to be redrawn because the base moved: the base has a backup and the drafts are only copied, so a merge can be stepped back from, and a redraw of approved drafts cannot. This holds for any base. At the readiness screen the agent finds, from source control history, the packages promoted into this base since this package was first recorded, and compares their `## Design Changes` with its own; a base package's own list already holds the entries of the requests promoted into it. For each item both changed:
    - Where both changes can stand, the fold applies this package's change to the base as it stands and keeps the other's. It marks each such place in the design file, in the form the tool guide gives, and the Base review gate names every marked place so the supervisor can find and check it. The marks come off when the supervisor confirms.
    - Where the two cannot both stand, the agent blocks for the supervisor's choice before the base is changed, records the choice in the promotion artifact's evidence, and the fold follows it in place of any entry it overrules.

    The readiness evidence names the packages compared. The mark's form is the tool guide's: [`figma-designer-guide-design.md`](figma-designer-guide-design.md) § Amendment — 2026-11-17, item 24.
22. **One promotion into a base at a time** (supervisor, 2026-11-17). The readiness screen gains a condition: no other package's promotion has changed this base and is still waiting for its Base review. Restoring a promotion's backup would otherwise erase the later promotion's changes.

**Out of this amendment:** whether the project's files are up to date with source control before a promotion, which item 21's check assumes and which the planned single promotion skill owns for every promotion guide (skai#91; supervisor, 2026-11-17); how a backfill is carried out, which the guides leave light on purpose and which is documented separately if at all (supervisor, 2026-11-17); known differences and defects (skai#109) and stopping on a conflict (skai#120), which a later stream owns; a catalog for the practices, built when the list grows (skai#149); one platform's design choices and a designer's own method, which the guides never prescribe; any change to `Bin/design-tool.py`, whose change-list parser already takes any kind word (`CHANGE_RE`, checked 2026-11-17).

**Where the text lives (refiner, 2026-11-17).** What only some packages need is kept out of the two guides every session reads, as the tool guide was broken up the same day. `design-system-changes.md`, a new guide linked from both, holds items 7 to 9, 17 and 18: read only for a package that changes the design system, its promotion, or a structure-only fix. `design-cleanup.md`, a new guide linked from promotion, holds item 20: read only on a cleanup request. Everything else is in `design-authoring.md` and `design-promotion.md`; the practices stay in `design-authoring.md` (supervisor, 2026-10-31).

**Gate and advance text (supervisor, 2026-11-17).** Both guides carried the default gate template nearly whole. This pass trims their `## Gates` and `## Advance intent` sections to what each workflow needs, as the maintenance guide for gated workflows intends ("inline the applicable process-flow invariants … using the template below as the default"). What must survive: a gate line whenever the agent waits on the supervisor, and the completion line; the one-sentence supervisor definition; gate persistence; no fabricated gates; each planned gate with when it comes and its exact line; the blocked line and the stop; what counts as advance intent and that it counts only after a gate line; what `auto` and `auto to <milestone>` do and never bypass; and each workflow's own marker lifecycle. What goes: the generic planned-gate line and the note on writing one, since every planned gate here has its exact line; the separate list of planned gates, merged into the gate notes; and the generic progress-marker rules, including markers in source files, which neither workflow uses and which each workflow's own lifecycle replaces. No gate, line or behavior changes.

**Caps (supervisor, 2026-11-17, after the proposal review and the compression review; a little under the compressed sizes):** `design-authoring.md` **18,900** (compressed 18,905; was 16,650); `design-promotion.md` **13,350** holds (13,345); `design-system-changes.md` **5,700** (5,716); `design-cleanup.md` **1,800** (1,817).

**Cap (supervisor, 2026-11-18, skai#144 pass):** `design-authoring.md` **18,900** holds (18,857 settled).
