Managed-By: skai
Managed-Id: guide.design-specs-authoring
Managed-Source: Guides/DesignSpecs/design-specs-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Specs Authoring

Print `📖 SKAI guide: design-specs-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

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

Draft specs into a change package, resolve supervisor questions and leave it ready to promote.
Edit only the package and drafts. Before drafting, read [content rules and checks](design-specs.md);
use [artifact formats](design-specs-artifacts.md) for typed changes and requests.

Inputs are open-ended: requirements, designs, designer notes, stories or an app to backfill.
Always propose; reserve Discussion for supervisor input.

## The Change Package

[Artifact formats § The Package](design-specs-artifacts.md#the-package) owns contents, path and
decoupling. Use the supplied change ID; otherwise propose a short kebab-case ID and block before
creation. For branches use the final component (`work/pinned-notes` → `pinned-notes`).
Check active and promoted paths: reopen unpromoted work; promoted ID/type pairs need new IDs.
Create the artifact with Goal/Inputs before drafting.

### What `proposed-design-specs/` Holds

Mirror only touched paths, drafting whole files. Reuse existing drafts; initialize a missing
draft from canon, or create it when canon is absent. Carry unchanged items, index lines and glossary entries. New specs require the root index,
glossary and all three folder indexes. Absent files remain untouched; files cannot be deleted.
Restructure with `move` items, retaining unmoved source content.

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

Infer from the specs, never declaration: **Baseline** if nothing exists for the touched screens
(all additions); otherwise **Scoped change** (modify, retire, move or add). In doubt, use Scoped
change: it handles a baseline with explicit items. A change request is input on reopen, not a mode.

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

Begin on explicit intent to write, backfill or audit specs; preceding stories, packages, notes
and app observations are context.

1. For first specs, follow [artifact hosting](../Core/artifact-hosting.md) and add the README link.
2. Read [content rules](design-specs.md), existing specs and affected requirements. Read the design
   tool guide for drawing conventions and production/change pages
   ([Figma](../Design/figma-designer-guide.md)).
3. Reopen a named or contextual unpromoted package; otherwise resolve the ID, check active/promoted
   paths and create its artifact with Goal/Inputs.
4. Infer mode; read *Working a Baseline* before code.
5. Draft under `proposed-design-specs/` and seed Discussion.

A recorded `C3` write awaiting confirmation or archival returns to promotion. Checked `C3`
closes the package; new work needs a new package. On every reopen, reread canon, rederive mode
and recompute the diff. Preserve resolved `D<n>` items unchanged and unrenumbered; continue
numbering and maintain draft links.

**Audit:** on an audit request or changed guides, before any edit run `V1`–`V10` over every
draft. Record each failure with a proposed fix in Discussion; block until resolved, then fix.

On a promotion change request, fill `Reviewer Response` and set `Change Request Status`:
incorporate, reject (name a new package when the valid request belongs there), or supersede.
Mark `Incorporated` only after updating both drafts and Spec Changes. `Proposed` blocks readiness.

## Drafting

Work screen by screen: open production/approved-change drawings, requirements and, for backfills,
the app and code; draft; record uncertainties; continue. Seek decisions only after the last screen.

Answer app-behavior questions from code and requirements; ask only about product intent. Draft
even uncertain items using the recommended reading, linked from Discussion's Concern or Proposal.
Drafts remain complete; Discussion holds uncertainty.

Unobserved platform/service differences are package Assumptions; write specs for every app.
Only observed differences become known-difference notes.

- Draft cited files first. Cite existing draft/canonical IDs, never predictions. For mutual
  references, draft one file, the other, then revisit.
- One author writes drafts. Research/review may be delegated, but returned text is input only.

### Working a Baseline

- Before code, write the root product paragraph from the requirements root and design: organize
  by product, not implementation.

### Working a Scoped Change

Retain draft and canonical IDs. Apply
[Modify vs. Retire](design-specs.md#modify-vs-retire); ambiguous calls need Discussion because they
burn IDs and repoint citations. Moves retain text and repair links; classify text changes by that test.
Include incoming-link spec files in the drafts and list them in the move's Touches after its
source → destination pair.

### Design vs. App Differences

For each confirmed backfill difference, recommend one of two outcomes in Discussion:
**design stands** (note the app's known difference with its tracking issue), or **app stands**
(correct the drawing). Follow project conventions: direct drawing when unmanaged, otherwise a
[design package](../Design/design-authoring.md); the supervisor assigns the work.
For conflicting sources or suspected defects, establish the intended contract and bring one
item, not one per instance.

### Undrawn States

Before requesting a drawing, apply [What Counts as a State](design-specs.md#what-counts-as-a-state):
data, dropped elements, unstyled system UI and motion use words. A needed undrawn state/variant
gets a Discussion proposal naming its drawing. Produce it directly or through design management
as above; resolve only after it exists and the agent sees it. Specs use its product name, never
its drawing location.

### Requirements Gaps

Never quietly specify a screen-independent promise or narrowed requirement. Seed a requirements
package via [requirements authoring § The change package](../Requirements/requirements-authoring.md#the-change-package):
skeleton, Goal/Inputs, Discussion item, and whole-file requirement draft with its new ID.
Stop; requirements authoring owns resolution. Cite that permanent draft ID; spec promotion waits
for requirement promotion.

## Discussion

Group items under `###` topics, never aggregate them into Questions/Open Items sections.

Use `- [ ] D<n> [Kind] <summary>`, with Kind `Question`, `Proposal` or `Tradeoff`.
Bold sub-bullet labels, without separators: **Concern** (required), **Proposal**, **Question**,
**Options**, **Detail**, **Why**, **Decision**. Recommend whenever possible; Tradeoffs name
the preferred option and why. Reserve Questions for cases with no basis to recommend.

Concerns must read without ID links; links supplement prose. Package prose may name frames,
nodes and code files.

### What Earns an Item

Only supervisor-dependent spec changes: design/app differences, undrawn states, ambiguous
modify/retire or placement calls, unresolved product intent, and audit failures.
Draft determined behavior directly; record givens as assumptions.

With no items use: “The listed Inputs determine the proposed specs; review the drafts under
`proposed-design-specs/` before they are finalized in Spec Changes.” Omit when items exist.

**Example** (LumenNotes — undrawn state):

```markdown
### Reminder Badges

- [ ] D1 [Proposal] The acknowledged badge is not drawn
  - **Concern** Acknowledged reminders keep their badge until refresh. Only pending and overdue
    badges are drawn; [UI-NOTES-02] has no acknowledged state to bind.
  - **Proposal** Draw `notes — acknowledged reminder` on Production; the file is unmanaged.
  - **Why** A third badge style belongs in the design.

[UI-NOTES-02]: proposed-design-specs/screens/notes.md#ui-notes-02
```

### Resolution

Follow the item approval/marker lifecycle in *Advance Intent*. Preserve original text; append
Decision last, never into Concern. For drawings, name the product-language drawing in Decision
and check only after seeing it. Apply decisions differing from recommendations before continuing.
If design stands, add the item's known-difference note. Maintain draft links.

## Spec Changes

After Discussion advances, diff canon and drafts by prose and resolved targets, ignoring only
location-required relative paths. Use [typed formats](design-specs-artifacts.md): one item per
difference, granularity by file newness, identity/Touches linked to drafts, changed text inline
for changes inside existing files.

On reopen, reconcile the recomputed diff: retain matching `S#` items and justifications, add new
differences, remove vanished ones. Never reset the section.

Update Assumptions/TODOs and Out of scope, then emit
`🏁 Complete. Let me know if anything needs adjustment.`

Promotion is separately invoked and supervisor-approved; implementation and design state beyond
`V5` are irrelevant.

## Artifact Maintenance

Before responding, update the authoring artifact, align drafts, then emit the prescribed gate.
Apply changes, never merely describe them. Run `V1`–`V10` before the advancing gate, even under
`auto`; on audits run them before edits.

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
