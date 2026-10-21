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
