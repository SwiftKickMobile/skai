Managed-By: skai
Managed-Id: guide.design-specs-authoring
Managed-Source: Guides/DesignSpecs/design-specs-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Specs Authoring

Print `- 📖 SKAI guide: design-specs-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

- [Purpose](#purpose)
- [The Change Package](#the-change-package)
- [Modes](#modes)
- [Gates](#gates)
- [Advance Intent](#advance-intent)
- [Initiation](#initiation)
- [Drafting](#drafting)
- [Discussion](#discussion)
- [Spec Changes](#spec-changes)

## Purpose

Draft design specs into a **change package**, resolve the questions they raise with the supervisor,
and leave the package ready to promote.

Authoring edits the package and its drafts; the canonical specs stay unchanged. Content rules —
layout, item format, IDs, writing style, the verification checks — live in
[`design-specs.md`](design-specs.md). Read it before drafting. Typed formats for change items and
change requests live in [`design-specs-artifacts.md`](design-specs-artifacts.md).

Inputs are open-ended: a requirements change, a design change, designer notes, a story, an existing
app to backfill from. The agent always proposes; Discussion items are only for what needs the
supervisor's input.

## The Change Package

A package lives at `skai/changes/<change-id>/design-specs/` in the repository that holds the specs
and holds:

| Path | What it is |
| --- | --- |
| `design-specs-authoring.md` | this workflow's artifact |
| `proposed-design-specs/**` | the draft spec files |
| `change-requests/design-specs-<nnn>.md` | requests raised by promotion; may be absent |
| `design-specs-promotion.md` | promotion's artifact; may be absent |
| `evidence/` | check output promotion persisted; may be absent |

Use a supplied change ID; otherwise propose a short kebab-case ID and block before creation. Derive
branch-based proposals from the branch's final component (`work/pinned-notes` → `pinned-notes`).
Check active and promoted paths: reopen unpromoted work; a promoted ID/type pair needs a new ID.
Create the artifact and Goal/Inputs before drafting.

This type owns its collateral independently of any `requirements/`, `design/` or `ui-map/` sibling
under the same change ID. It never assumes a sibling exists; where a drawing
was made — production or a change page, named for this change or another — is incidental, and the
spec never references it. Promotion moves this type to `skai/promoted/<change-id>/design-specs/`,
leaving siblings active.

### What `proposed-design-specs/` Holds

Only touched files, mirroring the specs' paths, each drafted **whole**: carrying its unchanged items,
index lines and glossary entries. Copy existing files then edit; draft absent files fresh. New specs
need `_design-specs.md`, `glossary.md` and all three folder indexes. Absent package files stay
untouched; a package cannot delete a file. A restructure is `move` items, each source file keeping
whatever was not moved.

### Artifact Skeleton

```
# Design Specs — <name>
## Goal                   one or two sentences; no motivation essay
## Inputs                 the sources this artifact was drafted from
## Mode                   Baseline | Scoped change
## Discussion             the open questions and resolved decisions
## Spec Changes           typed change items from resolved decisions
## Assumptions and TODOs  what the drafts assume; unresolved gaps that need no decision; may be empty
## Out of scope           boundaries this package deliberately doesn't address; may be empty
```

## Modes

- **Baseline** — the specs hold nothing for the screens this package touches. Everything is an
  addition.
- **Scoped change** — the specs already hold items this package modifies, retires, moves or adds to.

**Mode is inferred, never declared.** Read the specs: if nothing exists for the screens touched, it
is baseline; otherwise a scoped change. When in doubt, scoped change — it degrades to the same thing
with more explicit items. A change request is not a third mode; it is new input on an existing
package, handled on reopen.

## Gates

Core rule: every time the agent is waiting on the supervisor, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion items and reviews its gates; the executing agent does not resolve or approve its own.

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the supervisor.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the supervisor gives advance intent. If the gate is non-standard, make it describe the exact supervisor response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the supervisor resolves it.

Workflow-specific gate notes:
- The Discussion gate uses the canonical discussion-phase behavior: while any `- [ ]` item remains
  in `## Discussion`, every response ends with the blocked gate citing the remaining count; the
  moment every screen this package covers is drafted and every item is resolved — or drafting
  produced no items because the inputs fully specify the specs — the agent emits the planned gate
  that advances to Spec Changes.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Spec Changes.`
  - Planned: `⏳ GATE: Next: Discussion complete. Say "next" to advance to Spec Changes.`
  Before the Discussion gate advances, run the drafts against the verification checks `V1`–`V10`
  in [`design-specs.md`](design-specs.md) § Verification Checks. They are enumerated once, there,
  so nothing is discovered late and authoring and promotion cannot drift apart. `V5` means looking
  at the design file; a drawing not found is a Discussion item (*Undrawn States*), not a failed
  gate. The gate presents what the supervisor reviews; fix the artifact before gating.
- An item whose resolution is a drawing (*Undrawn States*, *Design vs. App Differences*) stays open
  until the drawing exists and the agent has seen it, so the Discussion gate stays blocked that long.
- There is no separate "draft is ready, please review" gate. The drafting response ends with
  whichever gate applies — blocked when it produced items, planned when it produced none.

Planned gates for this workflow:
- After every screen this package covers is drafted and every Discussion item is resolved, before
  Spec Changes are written.

Workflow-specific blocked gates:
- Inputs are too contradictory or incomplete to draft a screen.
- The change ID cannot be determined from the input, so the package has no path yet.
- The design file cannot be reached, so `V5` cannot run.
- A new prefix collides with one already in use, and the resolution is a naming call.

## Advance Intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestone in this workflow: `discussion complete` — the workflow's single planned gate.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the supervisor gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns exactly one marker: the `- [ ] D<n>` items
in `## Discussion`. Each is resolved individually, on the supervisor's explicit approval of *that
item*, by checking its box and appending `- **Decision** <resolution>.` Advance intent at the
Discussion gate does not clear them; by the time that gate is reached they are already clear.
`## Spec Changes` items carry no checkbox, and nothing under `proposed-design-specs/**` carries a
marker of any kind — those files are drafts of canon and must already read as canon. Discussion
links to drafts; specs carry no Discussion citations.

**Workflow-specific `auto` behavior.** `auto` suits a baseline whose inputs fully specify the specs,
batching Spec Changes after drafting. It never bypasses the Discussion blocked gate: unresolved items
are supervisor decisions.

## Initiation

The workflow starts on an explicit signal — "write the design specs", "spec the pipeline screens",
"backfill the specs for X", or equivalent. Whatever came before — a story, a requirements package, a
design package, designer notes, a running app — is context the agent digests.

On the signal:

1. When the specs do not exist yet, follow [`artifact-hosting.md`](../Core/artifact-hosting.md) to
   settle where they will live and link them from the README.
2. Read [`design-specs.md`](design-specs.md), the existing specs, and the requirements the inputs
   touch. Learn from the design file's tool guide
   ([`figma-designer-guide.md`](../Design/figma-designer-guide.md) for Figma) where production and
   change pages are. Drawing conventions are the tool guide's; this guide does not restate them.
3. If an unpromoted package for this work is named or already in context, reopen it rather than
   creating a second.
4. Otherwise resolve the change ID, check its active and promoted paths, create the artifact, and
   record `## Goal` and `## Inputs`.
5. Infer the mode. Baseline: read *Working a Baseline* before opening the code.
6. Draft the spec files under `proposed-design-specs/` and seed `## Discussion`.

A recorded `C3` write with confirmation or archival pending returns to promotion, not fresh
drafting. A package whose specs are written — `C3` checked in its `design-specs-promotion.md` — is
closed; new work on the same screens opens a new package. **Re-read the specs on every reopen**: another
package may have promoted since, so re-derive the mode and recompute the diff. **Resolved decisions
are never disturbed**: a resolved `- [x] D<n>` is not removed, rewritten or renumbered; new items
continue the numbering. Keep its draft links current.

When the new input is a **change request** raised by promotion, incorporate it, reject it (including
when it is valid but belongs in a new package, which the `Reviewer Response` names), or supersede it,
and record the outcome on the request: fill `Reviewer Response` and set `Change Request Status`.
`Incorporated` only once the adjustment is in the drafts *and* in `## Spec Changes`; a request left
`Proposed` blocks promotion.

## Drafting

Work **screen by screen**. For each screen: open its drawings (production, and any change page
whose mockups are approved), the requirements it presents, and — in a backfill — the running app and
its code; write the spec; record what is uncertain as Discussion items; move on. Never interrupt
drafting to seek a decision; the gate comes once, after the last screen.

**Look before asking.** "What does the app do" is answered from the code and the requirements, never
asked of the supervisor. Only genuine product intent is a Discussion item.

**Draft the item anyway.** An open item never leaves a hole: write the item under the recommended
reading, and link it from the item's Concern or Proposal. The drafts read as complete specs; the
Discussion explains the uncertainty.

Platform differences the agent could not observe — the other app, a remote service — are recorded
as assumptions in `## Assumptions and TODOs`, and the spec is written for every app alike. A
difference becomes a known-difference note only once observed on that app.

### Working a Baseline

Three things go wrong where every file is new:

- **Orient before reading the code.** Write the root index's product paragraph first, from the
  requirements root and the design file; every draft is then held to *what the product shows*, not
  how the code is shaped.
- **Draft cited files first.** A citation uses an ID already present in a draft or a canonical file,
  never a predicted one. Where two new files cite each other, draft one, then the other, then return
  for the citations the first could not yet make.
- **No delegated authoring.** Research and review may be delegated; what comes back is input the
  one author drafts from, never text carried into a draft. One author holding the whole package is
  what keeps IDs, terms and the glossary coherent.

### Working a Scoped Change

Copy each file being changed out of the specs into `proposed-design-specs/` and edit the copy,
keeping every ID. For each item whose text changes apply *Modify vs. Retire* in
[`design-specs.md`](design-specs.md); when the call could go either way it is a Discussion item,
since it burns an ID and re-points every citation. An item that belongs in another file is a `move`
— text identical, links repaired; a move that also changes the text is a move and a modify.

### Design vs. App Differences

In a backfill, the drawings and the app will disagree somewhere. Each confirmed difference is a
Discussion item with a recommendation and two options: **the design stands** — the app is in known
difference, noted under the item, with the tracking issue — or **the app stands** — the design is
changed. The supervisor decides; the resolution is recorded on the item. When the app stands, the
drawing is corrected: directly, by the agent on the supervisor's say-so, when the project's design
file is not under change management, or through a design package
([`design-authoring.md`](../Design/design-authoring.md)) when it is. The project's design conventions
or Integration say which; the supervisor says who. When sources disagree or observed behavior may be
a defect, identify the intended contract and its existing coverage first, then bring it to
Discussion with a recommendation. Do not multiply items to enumerate instances of one defect.

### Undrawn States

A rule that needs a screen state or component variant the design does not draw is a Discussion
item with a proposal naming the drawing. First check it needs one: a different string in the same
look is data; an element dropping out without moving the rest is a component property; standard
system UI the app does not style is specified by condition and choices and never drawn (*What
Counts as a State* in [`design-specs.md`](design-specs.md)). The fix is a drawing, made directly or
through a design package as above; the item resolves when the drawing exists and the agent has seen
it. The spec binds to the drawing by its product-language name and never says where it was drawn.

### Requirements Gaps

A rule that belongs in the requirements — a promise the product makes regardless of screen, a
visibility rule that narrows a requirement — is a requirements gap, never specified quietly. Seed a
requirements package for this change, chosen by
[`requirements-authoring.md`](../Requirements/requirements-authoring.md) § *The change package*.
Create its artifact skeleton with `## Goal`, `## Inputs` and
the Discussion item, and draft the requirement whole-file under its `proposed-requirements/` with
its new ID (as that guide's *What `proposed-requirements/` holds*). Then go no further: requirements authoring is invoked separately
and owns the item. The spec cites the draft ID — permanent from first drafting — and its promotion
waits for the requirement's. The two packages stay decoupled otherwise.

## Discussion

`## Discussion` holds the decisions this package needs from the supervisor. Topics are `###`
subsections with their items inline. Do not create aggregator sections (`## Questions`,
`## Open Items`) that pull items out of their topics.

Item line: `- [ ] D<n> [Kind] <summary>`, where `[Kind]` is `[Question]`, `[Proposal]`, or
`[Tradeoff]`. Sub-bullet labels are bold with no separator: **Concern** (always), **Proposal**,
**Question**, **Options**, **Detail**, **Why**, and **Decision** on resolution.

Bring a recommendation whenever possible; Tradeoffs name the preferred option and why. Reserve
Questions for cases with no basis to recommend.

**Concerns are plain prose** that reads correctly with every ID link deleted; links supplement the
explanation, never replace it. A Concern may name frames, nodes and code files — the restrictions
on product language govern the spec files, not the package's prose.

### What Earns an Item

Create items for what changes a spec and needs the supervisor: a design-vs-app difference, an
undrawn state, a modify-or-retire call that could go either way, a placement call that could go
either way, genuine product intent the inputs leave open. Draft fully specified behavior directly;
assumptions record what is taken as given.

With no items, leave Discussion as: "The listed Inputs determine the proposed specs; review the
drafts under `proposed-design-specs/` before they are finalized in Spec Changes." Omit this
sentence when items exist.

**Example** (LumenNotes — an undrawn state and a design-vs-app difference):

```markdown
### Reminder Badges

- [ ] D1 [Proposal] The acknowledged badge is not drawn
  - **Concern** A note whose reminder was acknowledged keeps its badge until the list is next
    refreshed, so the person sees that the reminder was handled. The notes list is drawn with
    pending and overdue badges only; the spec item binding the badge's states ([UI-NOTES-02]) has
    nothing to bind the acknowledged state to.
  - **Proposal** Draw a `notes — acknowledged reminder` state. The file is not under change
    management, so draw it directly on Production.
  - **Why** It is a third style of the same badge, the kind of difference the design owns.

### Stale Notice

- [ ] D2 [Tradeoff] The stale notice is drawn above the list; the app shows it below
  - **Concern** The design places the stale notice above the first group, where it is seen before
    the person starts reading. The app places it at the bottom of the list, where it is seen only
    after scrolling everything. The spec item ([UI-NOTES-05]) is drafted to the design.
  - **Options**
    - A — The design stands; the app is in known difference.
    - B — The app stands; the frame is changed.
  - **Proposal** A.
  - **Why** A notice about freshness is useful before reading, not after; nothing suggests the
    app's placement was chosen.

[UI-NOTES-02]: proposed-design-specs/screens/notes.md#ui-notes-02
[UI-NOTES-05]: proposed-design-specs/screens/notes.md#ui-notes-05
```

### Resolution

On the supervisor's explicit approval of an item: check the box and append
`- **Decision** <resolution>.` as the last sub-bullet. The original stays visible — the decision is
appended, never substituted or inserted into the Concern. When the decision calls for a drawing, the
box is checked once the drawing exists and the agent has seen it; the Decision records the call and
names the drawing by its product-language name. When the decision differs from the recommendation,
update the draft before continuing; when the design stands over the app, add the known-difference
note under the affected item. Keep the item's draft links aligned.

## Spec Changes

Written after the Discussion gate advances. Compare the specs and the drafts by prose and resolved
link targets, ignoring only relative-path changes caused by location, and record one typed item per
difference using [`design-specs-artifacts.md`](design-specs-artifacts.md): each item's identity a
link to the draft, its Touches links to the draft files, the new or changed text inline. Granularity
keys on whether the file is new.

This diff is recomputable at any time. On reopen with items already written, recompute and
reconcile: an item that still matches keeps its `S#` and justification; a new difference gets a new
item; a difference that no longer holds loses its item. Never reset the section.

Then bring `## Assumptions and TODOs` and `## Out of scope` up to date, and the package is ready to
promote. End with `🏁 Complete. Let me know if anything needs adjustment.`

Promotion is invoked separately. A spec promotes on the supervisor's approval; promotion has no
concern with implementation or with the design file beyond what `V5` checks.

## Artifact Maintenance

Through drafting and Discussion, update the artifact before speaking: revise
`design-specs-authoring.md`, bring `proposed-design-specs/` into line with it, then end the response
at whichever gate *Gates* prescribes. The `V1`–`V10` pass runs once, at the point the advancing gate
would be emitted — under `auto` too, which bypasses the gate and not the pass. Do not describe
intended artifact changes without applying them.

## Cross-References

- [`design-specs.md`](design-specs.md) — content rules and the verification checks
- [`design-specs-artifacts.md`](design-specs-artifacts.md) — change item and change request formats
- [`design-specs-promotion.md`](design-specs-promotion.md) — promoting an approved package
- [`design-authoring.md`](../Design/design-authoring.md) — the design package, when a drawing goes
  through change management; the tool guide it names holds the drawing conventions
- [`requirements-authoring.md`](../Requirements/requirements-authoring.md) — the workflow that
  receives a requirements gap

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-authoring-addendum.md` exists, read it and immediately print
`- 📎 Addendum loaded` as a line of its own, nested under this guide's line; its rules are part of this
guide and win any conflict.
