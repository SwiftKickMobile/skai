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
   authoring's completion. Every system's promotion requires zero open gaps in its own package: an
   open gap fails readiness, the blocked gate lists them, and the package returns to authoring
   (supervisor, 2026-10-20: a planned gate is for a step "next" advances; this is a block).
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
8. **No owner field.** skai knows only the supervisor, and the artifacts are workflow-agnostic:
   nothing in an item records who is to answer. The Concern states what is not yet known.
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
- Promotion blocked by open gaps (a readiness failure, blocked gate) returns the package to
  authoring; promotion never resolves a gap itself.
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

## Amendment — 2026-10-23 (promotion into a package carries gaps)

Rule 6's zero-gap requirement is for promotion into production. A workflow that promotes a package
into another open package (design change requests, `design-process-design.md` § Amendment —
2026-10-23) carries the open gaps into the base, as that workflow's guide says. Found by the
design guides' cold review (series CL r3 F1), routed here; one clause, within the 3,400 cap.

## Amendment — 2026-10-23 (inherited gaps are marks, not items)

Supervisor, 2026-10-23, from the design dry run: a package that builds on an input's placeholder
is not re-discussing the question, so carrying a Discussion item for it is wrong. Rule 3 and rule
5 change: a package's own gap is an unchecked item with a Gap line; an inherited gap is the
artifact's marker on what stands on the placeholder, naming the owning item, and no item; the
marker clears when the owning item closes (rule 7 unchanged). Rule 6 counts both kinds as open.
Each artifact's marker is its guide's: the spec-file footnote, the design change list footnote,
the UI Map mirror. Within the 3,400 cap; additions paid by trims in rules 3 and 5.
Cap after the 2026-10-23 change: **3,300 bytes** (compressed 3,343; supervisor, 2026-10-23),
replacing 3,400.
The marker's form for footnoting artifacts is `spec-file-gaps.md`'s (2026-10-24); rule 3 keeps
naming the guides.


## Amendment — 2026-10-26 (a gap is a decision outside the author's authority)

Inventory for rule 1, added to the guide at its definition: a gap is a decision the work needs before shipping that nobody in the work can make yet, because the answer is not yet known outside it (the purpose section's "open question that must be decided before the work ships", with the authority test made explicit). A decision within the author's authority is made and recorded and stands for review with the package; a decision the supervisor can make now is an ordinary Discussion item and blocks as usual (round 1, F1). Naming what the answer waits on is optional (rule 8 already allows the question to name who is awaited; no owner field) — withdrawn the same day, see the next amendment. The existing ❌/✅ example stays, reworded to show the authority test.

Evidence: the Offers package (2026-10-22 to 25) carried D29 ("does the hub owe the digest anything") and D25 ("is the status always one of six") as gaps although the supervisor, acting as product, had decided both; the guide's rule 1 let any unmade decision be parked as a gap. Supervisor, 2026-10-26: gaps are for decisions the author cannot make (a threshold the stakeholder owns, data that may not exist); the rest are requirements awaiting the package's review.

Size: draft 3,399, compressed by Astra to 3,296 (the opening's definition merged into rule 1; rule 8's redundant clause dropped). Cap (supervisor, 2026-10-26): **3,290**, a little under the compressed size. Cold series RG with the catalog and design specs guides' amendments of the same date.

## Amendment — 2026-10-26 (the Gap line is the placeholder only)

Supervisor, 2026-10-26, from the Offers packages' content audit: once the no-placeholder form named what is awaited, Gap lines grew who is to answer, names, dates and narrative, and Decision lines followed; the artifacts are workflow-agnostic and skai knows only the supervisor. Two changes. Rule 8 drops "the question may name what the answer awaits": nothing in an item records who is to answer; the Concern states what is not yet known (requirement 8 reworded). The Gap line's no-placeholder form, owned by process-flow (`product-specs-system-design.md` § Decisions — 2026-10-20, item 1, amended the same day), becomes "no placeholder", in the maintainer reference and every inlined copy alike. Deletions only: known-gaps 3,211 bytes (cap 3,290 held); no compression round. Cold series GL.
