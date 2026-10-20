# Known Gaps Guide Design

## Purpose

This document is the standard for SKAI's known-gaps guide: what it is for, what it must and must
not contain, and the decisions behind it. It is used to write and cold-review the guide; it is not
something an operator reads at runtime.

- [`Guides/Core/known-gaps.md`](../../Guides/Core/known-gaps.md) — how an agent works with a gap:
  an open question that must be decided before the work ships, carried as a placeholder so work
  can continue.

The guide is a reference, like the debugging guide: not a gated workflow and not a skill. A
workflow guide sends the agent to it with one inlined sentence that names the two triggers (a gap
on an input the agent relies on; an item of its own that cannot be resolved because something
outside the work is not yet known). The agent reads it whole when triggered.

Written 2026-10-20 from the known-gaps planning (SwiftKickMobile/skai#82).

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md), especially Common house style.
- [`Guides/Core/process-flow.md`](../../Guides/Core/process-flow.md) § Structured discussion items
  owns the formats the guide uses (the **Gap** sub-bullet, `## Decision Log`, the pointer
  sentence). This guide uses them; it does not define them.
- [`product-specs-system-design.md`](product-specs-system-design.md) § Decisions — 2026-10-20
  records the format decisions.
- Spec-file representation (the footnote on a requirement) belongs to
  [`spec-format-design.md`](spec-format-design.md); the UI Map and Figma representations to their
  own design specs. The guide names each representation and points at its owner.

## Requirements

1. **One concept.** A gap is "X must be decided before this ships". Shipping without X is a
   different thing (out of scope, or a known difference) and is not a gap. The guide says this
   once, with a ❌/✅ pair.
2. **Placeholder means proceed.** A placeholder is the provisional answer work is built against
   until the gap closes. It exists to be built on: a downstream agent never second-guesses it, and
   one that thinks it wrong files a change request upstream. A gap with no placeholder gives
   nothing to proceed on.
3. **Gaps do not block authoring; they block promotion.** A gap item stays open through
   authoring's completion. Every system's promotion requires zero open gaps in its own package: a
   planned gate lists them, and "next" returns the package to authoring to resolve them.
4. **Three resolutions.** Answered (the decision replaces the placeholder); placeholder adopted
   (the provisional text becomes the rule); omitted (the dependent behavior leaves the drafts,
   recorded under Out of scope). A follow-up after adoption is a ticket, not the artifact's
   concern. Each resolution is recorded on the item (Decision, box checked) and in the artifact's
   Decision Log, in the formats process-flow defines.
5. **Inherited gaps.** An artifact built on an upstream placeholder carries its own gap marker
   that names the upstream gap. With a placeholder upstream the agent proceeds, no decision. Only a
   bare upstream gap forces a Discussion item: request a placeholder upstream (a change request),
   leave the dependent part out, or wait; the agent recommends and the supervisor rules.
6. **Catch-up on a changed upstream gap** follows the general catch-up rule for inputs (the
   consumer compares its recorded version marker, reads what changed, and applies it under the
   normal Discussion bar). The guide states only what is gap-specific: an upstream gap answered
   differently from its placeholder is a change that may undercut an approved decision; an upstream
   gap adopted as written changes nothing downstream.
7. **Representation by artifact kind, pointed, not defined.** One short list: a Discussion item
   carries the **Gap** line (all artifact kinds); a spec file marks the placeholder with the
   footnote form the spec-file shape defines; a UI Map proposal and a Figma change page mirror
   each open gap as their own guides say. The guide never restates another guide's syntax.
8. **No owner field.** skai knows only the supervisor. The question's free text may name whoever
   is waited on; the guide and tools never read it.
9. **Agent-facing, short, plain.** Rules in numbered form with a bold lead sentence, LumenNotes
   examples, no narrative about why the mechanism exists beyond one sentence of purpose. Read whole
   when triggered, so it stays small; if it ever needs splitting, split by trigger (inherited gaps
   apart from raising and resolving one's own).
10. **Never invokes a skill.** It names no sibling workflow to run. Where a step belongs to
    another workflow (filing a change request, promotion), it says what to do and leaves the
    supervisor to start that workflow.

## Settled decisions

- The gap workflow is one shared guide reached by a pointer, not inlined boilerplate: gaps are not
  always present, and the workflow would clutter every Discussion-phase guide. The format (the Gap
  line, the Decision Log) is inlined house style because it is used every time an item changes
  state (2026-10-20).
- The pointer sentence names the use case, not just the location, so it fires when the agent sees
  a footnote on its input or cannot resolve an item of its own.
- Promotion blocked by open gaps returns the package to authoring; promotion never resolves a gap
  itself.
- Offers is not in this effort's scope; it adopts gaps after the release that ships them.

## Size budget

**3,400 bytes**, set by the supervisor 2026-10-20 from the compression review of the first draft
(draft then cap: 4,334 drafted, 3,232 after Astra's compression). Whole-file bytes by `wc -c`,
managed header and addendum footer included. It binds every repair per the refinement guide's
size-budget rule.

## Boundaries

The guide does not define the Discussion schema, the spec-file footnote syntax, the UI Map `gap`
field, the Figma annotation convention, the Decision Log line shape, or the Inputs version marker
and catch-up procedure; each belongs to its owning guide. It does not describe promotion's checks
beyond the zero-open-gaps condition, and it has no gates of its own: an agent that reaches a
decision it cannot make returns to its workflow's gate model.
