Managed-By: skai
Managed-Id: guide.requirements-authoring
Managed-Source: Guides/Requirements/requirements-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-27

# Requirements Authoring

## Purpose

Draft behavioral requirements into a **change package**, resolve the open questions they raise with
the human, and leave the package ready to promote.

The catalog is canonical and is never written by this workflow. Drafts and
discussion live in the package; [`requirements-promotion.md`](requirements-promotion.md) is the only
writer of the catalog. That separation is what keeps the catalog free of workflow state and lets
this workflow draft a whole subject at once, flagging what it is unsure of rather than stopping at
every uncertainty.

Content rules — scopes, layout, requirement format, IDs, writing style — live in
[`requirements-catalog.md`](requirements-catalog.md). Read it before drafting. Typed formats for
change items and change requests live in
[`requirements-artifacts.md`](requirements-artifacts.md).

## The change package

A package lives at `skai/changes/<change-id>/` and holds:

| Path | What it is |
| --- | --- |
| `requirements-authoring.md` | this workflow's artifact |
| `proposed-requirements/**` | the draft catalog files |
| `change-requests/requirements-<nnn>.md` | requests raised by promotion; may be absent |
| `requirements-promotion.md` | promotion's artifact; may be absent |
| `evidence/` | check output promotion persisted; may be absent |

If the change ID is clear from the user's input, use it. If not, do not create the artifact yet:
propose a short kebab-case default and stop at the blocked gate rather than guessing. When deriving a
proposal from the current branch, use only the final path component, not the full branch path; for
example, `work/billing-ui` proposes `billing-ui`. Once the change ID is resolved, create the artifact
at its final path, then write `## Goal` and `## Inputs` into it before drafting anything.

A package may sit alongside a UI Map change package under the same `<change-id>` when one change
produces both.

### What `proposed-requirements/` holds

**Only the files this package touches**, mirroring their path under the catalog root. A package
changing three requirements in a catalog of two hundred files holds three files, not two hundred —
carrying the rest would bury the change and make the package unreviewable.

Each file is drafted whole: a touched file holds all of its content — unchanged requirements, index
lines, and glossary entries included, because promotion writes the file rather than patching it.

Key this on the file, not on the package's mode: **a file the catalog already holds is copied from
it and then edited; a file it does not hold is drafted fresh.** A package that is baseline for one
scope still rewrites the root index and glossary the catalog already has, so those are copied.

A first promotion creates the catalog, so on a wholly new tree anything not in the package will not
exist — including `_requirements.md`, `glossary.md`, and a scope index for every scope populated. A
package that populates a scope the catalog does not yet have carries the index of every folder it
creates and the root index too, whose scope list would otherwise go stale.
Files absent from the package are untouched, not deleted: a package has no way to express deleting a
file, and retiring a requirement is an edit within its file. A file that must **split** therefore
cannot be expressed either — the old path would have to go. Stop at the blocked gate rather than
drafting both halves and leaving the original behind.

### Artifact skeleton

```
# Requirements — <name>
## Goal                   one or two sentences; no motivation essay
## Inputs                 the sources this artifact was drafted from
## Mode                   Baseline | Scoped change
## Discussion             the open questions and resolved decisions
## Requirement Changes    typed change items from resolved decisions
## Assumptions and TODOs  what the drafts assume; unresolved gaps that need no decision; may be empty
## Out of scope           boundaries this package deliberately doesn't address; may be empty
```

## Modes

- **Baseline** — the catalog for this scope starts empty. Everything is an addition, so there are no
  diffs to narrate.
- **Scoped change** — the catalog already holds requirements this package modifies, retires, or adds
  to.

**Mode is inferred, never declared by a caller.** Read the catalog: if the scope this package
touches has no existing requirements, it is baseline; otherwise it is a scoped change. A package may
be baseline for one scope and a scoped change overall — when in doubt, scoped change, because it
degrades to the same thing with more explicit items.

A **change request** is not a third mode. It arrives as new input on an existing package and is
handled on reopen.

## Gates

Core rule: every time the agent is waiting on the human, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the human.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the human gives advance intent. If the gate is non-standard, make it describe the exact human response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the human resolves it.

Workflow-specific gate notes:
- The Discussion gate uses the canonical discussion-phase behavior: while any `- [ ]` items remain in
  `## Discussion`, every response ends with the blocked gate citing the remaining count; the moment
  every subject this package covers is drafted and every item is resolved — or drafting produced no items
  because the inputs fully specify the requirements — the agent emits the planned gate that advances
  to Requirement Changes.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Requirement Changes.`
  - Planned: `⏳ GATE: Next: Discussion complete. Say "next" to advance to Requirement Changes.`
  Before the Discussion gate advances, run the drafts
  against promotion's **verification** checks — `C1` through `C5` in
  [`requirements-promotion.md`](requirements-promotion.md), including the writing-style check. They are
  enumerated once, there, so nothing is discovered late and the two workflows cannot drift apart. Stop
  at `C5`: `C6` and `C7` belong to promotion.
  The gate presents what the human reviews; fix the artifact before gating.
- There is no separate "draft is ready, please review" gate. The drafting response itself ends with
  whichever gate applies — blocked when it produced items, planned when it produced none.

Planned gates for this workflow:
- After every subject this package covers is drafted and every Discussion item is resolved, before
  Requirement Changes are written.

Workflow-specific blocked gates:
- Inputs are too contradictory or incomplete to draft the requirements for a subject.
- The change ID cannot be determined from the input, so the package has no path yet.
- The Integration doc has no `Section: requirements` block, its values are unfilled, or the shape is
  `none` — so this project either cannot say where its catalog lives or keeps none. The resolution is the
  human filling the block's 🟡 values, or — if the block is absent entirely — re-running the skai
  installation update. Say which applies; under `none` the stop is terminal, and `next` does not
  resolve it.
- A new requirement needs a prefix that collides with one already in use, and the resolution is a
  naming call rather than a placement call.
- A file must be split into a folder, which a package cannot express — see
  *What `proposed-requirements/` holds*.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit human resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestone in this workflow: `discussion complete` — the workflow's single planned gate.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without human approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the human gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns exactly one marker: the `- [ ] D<n>` items
in `## Discussion` of the authoring artifact. They follow the discussion exception rather than the
default gate rule — each item is resolved individually during the discussion loop, on the human's
explicit approval of *that item*, by checking its box and appending `- **Decision** <resolution>.`
Advance intent at the Discussion gate does not clear them; by the time that gate is reached they are
already clear.

`## Requirement Changes` items carry **no checkbox**. The change is realized by the draft files under
`proposed-requirements/`, not by ticking items. Nothing in `proposed-requirements/**` carries a
progress marker of any kind — those files are drafts of canonical content and must already read as
canon. The `(D#)` citations are scaffolding promotion strips, not markers.

**Workflow-specific `auto` behavior.** `auto` is useful for a baseline package where the inputs fully
specify the requirements, batching Requirement Changes after drafting. It never bypasses the
Discussion blocked gate: unresolved items are human decisions, and `auto` does not resolve them.

## Initiation

The workflow starts on an explicit signal — "write the requirements", "backfill the requirements",
"update the requirements for X", or equivalent. Whatever came before — designs, an implementation, a
product brief, a planning document, a retro's seeded package, a change request, a bug report — is
context the agent digests. There is no declared entry point and no declared mode.

On the signal:

1. Read `skai/integration.md`'s `Section: requirements` block to learn this project's repository
   shape and where the catalog lives. If it cannot answer that — or, under `shared`, the root it
   names does not resolve — stop at the blocked gate below. **Never fall back to a literal path**,
   and never read an unresolved root as an empty catalog.
2. Read [`requirements-catalog.md`](requirements-catalog.md) and the existing catalog.
3. Scan `skai/changes/*/requirements-authoring.md`. If an unpromoted package for this work already
   exists — including one seeded by another workflow — reopen it rather than creating a second; see
   below.
4. Otherwise resolve the change id and create the artifact — see *The change package* — then record
   the sources in `## Goal` and `## Inputs`.
5. Infer the mode.
6. Draft the requirement files under `proposed-requirements/` and seed `## Discussion`.

A package whose promotion completed — `C7` checked in its `requirements-promotion.md` — is closed; new work on
the same subject opens a new package. A seeded package may hold only drafts and `## Discussion`; complete
the skeleton — `## Goal`, `## Inputs`, `## Mode` — before continuing. Treat the new input as additional context; a promotion finding is named
in the package's `requirements-promotion.md` Evidence and is fixed in the drafts, not turned into a
Discussion item — unless the fix is itself a decision.

**Re-read the catalog on every reopen.** Another package may have promoted since this one was
drafted, so re-derive the mode and recompute the diff rather than trusting what the artifact says —
both are facts about the catalog, not properties the package owns.

**Resolved decisions are never disturbed.** A resolved `- [x] D<n>` is not removed, rewritten, or
renumbered on reopen, and new items continue the existing numbering. The drafts cite those numbers
and so does every `Resolved decision: D#` justification; renumbering orphans both, and the package is
the durable record of why these requirements say what they say.

When the new input is a **change request** raised by promotion, either incorporate the requested
adjustment, reject it — including when it is valid but belongs to a new scoped-change package, whose
name the `Reviewer Response` then gives — or supersede it with a different decision — and record the outcome on the
request itself: fill its `Reviewer Response` and set its `Change Request Status`. Use `Incorporated`
only once the adjustment is actually reflected in the drafts *and* in `## Requirement Changes`;
leave it `Proposed` until then. A request left at `Proposed` blocks promotion, which is what stops
one being waved through.

### Working a backfill

When the source is an existing implementation and its designs, work **subject by subject**, in
whatever order the catalog's file layout suggests. For each subject: read the designs and the code
that implements it, write the requirements, record what is uncertain as Discussion items, and move
on. Do not stop at each uncertainty — record it and keep drafting. Never interrupt drafting to seek
a decision: that is what lets a backfill run end to end instead of trickling out one subject per
turn. The gate comes once, after the last subject this package covers.

Two sources that disagree is a Discussion item, never a silent choice. An implementation that does
something which looks like a defect rather than intent is a Discussion item too — proposing which,
with a recommendation, is the agent's job; deciding is the human's.

### Working a scoped change

Copy each file being changed out of the catalog into `proposed-requirements/` and edit the copy,
never the catalog file — see *What
`proposed-requirements/` holds* for what a draft must carry. Keep every ID the file already has. For
each requirement whose text changes, apply *Modify vs. retire* in
[`requirements-catalog.md`](requirements-catalog.md): clarifying keeps the ID, changing the contract
retires it and adds a new one. When that call could reasonably go either way it is a Discussion item
like any other placement call — it burns an ID and re-points every work spec citing it.

## Discussion

`## Discussion` holds the decisions this package needs from the human. Topics are `###` subsections
with their items inline. Do not create aggregator sections (`## Questions`, `## Open Items`) that
pull items out of their topics.

Item line: `- [ ] D<n> [Kind] <summary>`, where `[Kind]` is `[Question]`, `[Proposal]`, or
`[Tradeoff]`. Sub-bullet labels are bold with no separator: **Concern** (always), **Proposal**,
**Question**, **Options**, **Detail**, **Why**, and **Decision** on resolution.

**Every item carries a recommendation.** A `[Tradeoff]` names which option the agent recommends and
why; a `[Question]` — reserved for cases with no basis to recommend — is rare. An item the human
cannot answer with "yes" is an item that will sit unresolved.

### What earns an item

Seed an item only where a real decision is needed. If the inputs determine the requirement, write it
and move on; the draft files are the review surface. Requirements that are obvious from the source
do not need the human's approval to exist.

An uncertainty whose resolution would change what a requirement *says* is an item; what the drafts
take as given is an assumption. Items are earned by: two sources disagreeing, behavior that looks like a defect rather than intent, a
rule whose boundary the sources leave undefined, a placement or scope call that could reasonably go
either way, and behavior that exists in the implementation but appears in no design.

If drafting produces no items, leave `## Discussion` as one plain paragraph: "The listed Inputs
determine the proposed requirements; review the drafts under `proposed-requirements/` before they
are finalized in Requirement Changes." Omit that sentence whenever the section holds any item.

### Draft the requirement anyway

An open Discussion item never leaves a hole in the drafts. Write the requirement under the
recommended reading and cite the item inline:

```markdown
## LEAD-04
A lead not acted on before its appointment time is shown as missed and can no longer be booked. (D2)
```

The draft files therefore always read as a complete, coherent catalog. `## Discussion` says which
statements the agent is not confident in and what it would change them to. The `(D2)` citation is
scaffolding: promotion strips it.

**Example** (LumenNotes — a Proposal and a Tradeoff):

```markdown
### Missed reminders

- [ ] D2 [Proposal] A reminder that fires while the app is closed stays pending indefinitely
  - **Concern** Nothing expires an unacknowledged reminder, so the pending list grows without bound.
  - **Proposal** Preserve the current behavior and state it as the requirement.
  - **Why** It is consistent across every entry point and no design contradicts it, which reads as
    intent. It is also exactly the shape an oversight takes, so it is worth your eye rather than
    mine.

### Where sync boundaries fall

- [ ] D5 [Tradeoff] Does the selected theme sync across devices?
  - **Concern** The designs show one theme control with no per-device affordance; the implementation
    stores it locally, so two devices can disagree. One of the two is wrong.
  - **Options**
    - A — Theme syncs, matching the single control in the designs.
    - B — Theme is per-device, matching the implementation.
  - **Proposal** B.
  - **Why** Theme tracks the device's own appearance settings, and a phone in dark mode should not
    drag a desktop with it. The designs are silent rather than contradictory — one control does not
    imply one value.
```

### Resolution

On the human's explicit approval of an item: check the box and append `- **Decision** <resolution>.`
as the last sub-bullet. The original question stays visible — the decision is appended, never
substituted.

When a decision differs from the recommendation the draft was written under, update the draft
requirement to match before continuing. When it matches, the draft already stands. Either way the
`(D#)` citation stays until promotion.

## Requirement Changes

Written after the Discussion gate advances. This section states exactly the difference between the
catalog and the drafts under `proposed-requirements/`, one typed item per difference, in the
format defined in [`requirements-artifacts.md`](requirements-artifacts.md).

Granularity keys on whether the file is new. The rule and its worked examples are in
[`requirements-artifacts.md`](requirements-artifacts.md).

This diff is recomputable at any time. When a package is reopened and already holds change items,
recompute the diff and reconcile the
existing items against it — never reset the section. An item that still matches a difference keeps
its `R#` and its justification; a new difference gets a new item; a difference that no longer holds
loses its item. The IDs and the rationale are the part a raw diff cannot reconstruct.

After writing the section, bring `## Assumptions and TODOs` and `## Out of scope` up to date — they
are the package's record of what the drafts take for granted — and the package is ready to promote.
End with
`🏁 Complete. Let me know if anything needs adjustment.`

Do not promote as a continuation of this workflow. A package recording behavior that **already
ships** promotes on the human's approval, which the `🏁` invites but does not assume; one recording
behavior **still to come** promotes when the work ships, which may be much later and in another
session. The test is the behavior, not the mode. Either way promotion is invoked separately —
say which of the two applies so the human knows whether the next move is theirs now or later.

## Artifact maintenance

Through drafting and Discussion, and on each response in that stretch, update the artifact before speaking: revise
`requirements-authoring.md`, bring `proposed-requirements/` into line with it, then end the response at
whichever gate *Gates* prescribes.
The `C1`–`C5` pass named under *Gates* runs once, at the point the advancing gate would be emitted —
not on every response, and under `auto` too, which bypasses the gate and not the pass. Do not describe intended artifact changes without applying them.

## Cross-references

- [`requirements-catalog.md`](requirements-catalog.md) — catalog content rules
- [`requirements-promotion.md`](requirements-promotion.md) — promoting an approved package
- [`requirements-artifacts.md`](requirements-artifacts.md) — change item and change request formats
