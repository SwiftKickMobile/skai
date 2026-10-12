# Design Process Design

## Purpose

This document is the standard for SKAI's design process guides: what they are for, what they must
and must not contain, and the decisions behind them. It is used to write and cold-review them; it
is not something an operator reads at runtime.

- [`Guides/Design/design-authoring.md`](../../Guides/Design/design-authoring.md) — take a design
  change from an idea to approved mockups in a change package.
- [`Guides/Design/design-promotion.md`](../../Guides/Design/design-promotion.md) — move an approved
  package's designs into production and close the package.

The process mirrors SKAI's requirements process (authoring and promotion around a change package)
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
- [`Guides/Requirements/requirements-authoring.md`](../../Guides/Requirements/requirements-authoring.md)
  and [`requirements-promotion.md`](../../Guides/Requirements/requirements-promotion.md) — the
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
   the end. A reader of the requirements guides should find nothing surprising in form.
5. **Lean.** Each guide holds what an operator needs at the point of use, and nothing it can read
   elsewhere. No session-specific mistakes codified; no defensive checklists.

## Settled decisions

- **Package**: `skai/changes/<change-id>/` holding `design-authoring.md` and (after promotion)
  `design-promotion.md`. The drafts live in the design file on a **change page** named
  `<change-id>`. A design package may share its folder with a requirements package for the same
  change.
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
- **No archiving**: superseded designs live in the tool's version history.
- **No Concept pages**; the change page is where iteration happens.
- **Humans follow the same process**; no special case for hand edits.
- **Requirements impact is not the guides' concern**; an agent that sees a conflict says so, and the
  supervisor decides whether to run the requirements skill.

## Size budget

`design-authoring.md` is capped at **16,000 bytes** and `design-promotion.md` at **12,000 bytes**
(`wc -c`, managed headers included; the inlined gate and advance-intent blocks count). This keeps
each well under its requirements counterpart (24,000 and 20,800). Every repair states its net size
cost; additions over the cap are paired with trims, and a fix that cannot fit is a supervisor
decision.

## Boundaries

The guides do not cover the tool's conventions, requirements, the UI Map, bug tracking, or
implementing designs in code.
