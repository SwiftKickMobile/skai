Managed-By: skai
Managed-Id: guide.design-specs-authoring
Managed-Source: Guides/DesignSpecs/design-specs-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-18

# Design Specs Authoring

Print `📖 SKAI guide: design-specs-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Draft specs into a change package, resolve supervisor questions and leave it ready to promote.
Edit only the package and drafts. Read [content rules and checks](design-specs.md) before drafting;
[artifact formats](design-specs-artifacts.md) owns the package, typed changes and requests,
[the shape guide](../Core/spec-file-shape.md) the file shape and the spec tool.

Inputs are open-ended; always propose and reserve Discussion for supervisor input.

## The Change Package

[Artifact formats § The Package](design-specs-artifacts.md#the-package) owns contents, path and
decoupling. Use the supplied change ID; otherwise propose a short kebab-case ID and block before
creation (from a branch, its final component). Check active
and promoted paths: reopen unpromoted work; promoted ID/type pairs need new IDs. Create the
artifact with Goal/Inputs before drafting. Sibling types of one change update freely while it is
open; a consumer wanting this package changed files a change request, never edits it.

### What `proposed-design-specs/` Holds

Mirror only touched paths, drafting whole files. Reuse existing drafts; initialize a missing draft
from canon, or create it when canon is absent. Carry unchanged items, index lines and glossary
entries. A new specs root needs the root index, glossary and all three folder indexes. Absent files
remain untouched; files cannot be deleted. Restructure with `move` items, retaining unmoved source
content.

### Artifact Skeleton

```
# Design Specs — <name>
[Review page](design-specs-review.html)
## Goal                   one or two sentences; no motivation essay
## Inputs                 draft sources
## Mode                   Baseline | Scoped change
## Discussion             open questions and decisions
## Verification           one evidence line per check and per reference sweep
## Spec Changes           typed change items, kept current as the drafts change
## Assumptions and TODOs  what the drafts assume; gaps needing no decision; may be empty
## Out of scope           excluded work; may be empty
```

The page link sits directly under the title, here and in every request's `request.md`.

## Modes

Infer from the specs, never declaration: **Baseline** if nothing exists for the touched screens (all
additions); otherwise **Scoped change**. In doubt, use Scoped change. A change request is input on
reopen, not a mode.

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
  that advances to Completion; there is no separate "draft is ready" gate.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Completion.`
  - Planned: `⏳ GATE: Next: Discussion complete. Say "next" to advance to Completion.`
  Before emitting the planned gate, run the **pre-gate pass** once (under `auto` too, which bypasses
  the gate, not the pass): the tool's `validate` over the drafts projected on canon (what blocks is
  the content guide's), then `V1`–`V10` in [`design-specs.md`](design-specs.md) § Verification
  Checks, then `check-changes` on `## Spec Changes`. One evidence line per check under
  `## Verification`, in promotion's evidence form; a check with no line has not run. `V5` means
  looking at the design file; a drawing not found is a Discussion item, not a failed gate. The gate
  presents what the supervisor reviews; fix the artifact before gating.
- An item resolved by a drawing (*Undrawn States*, *Design vs. App Differences*) stays open until
  the drawing exists and the agent has seen it; one resolved by a change request's triage
  (*Requirements Gaps*) until it is triaged. The gate stays blocked that long.

Planned gates for this workflow:
- After every screen is drafted and every Discussion item is resolved, before Completion.

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

**Workflow-specific `auto` behavior.** `auto` suits a baseline whose inputs fully specify the specs.
It never bypasses the Discussion blocked gate: unresolved items are supervisor decisions.

## Initiation

Begin on explicit intent to write, backfill or audit specs; whatever came before is context.

1. For first specs, follow [artifact hosting](../Core/artifact-hosting.md) and add the README link.
2. Read [content rules](design-specs.md), existing specs, affected requirements and the design tool
   guide ([Figma](../Design/figma-designer-guide.md)).
3. Reopen a named or contextual unpromoted package; otherwise resolve the ID, check its paths and
   create the artifact with Goal/Inputs.
4. Infer mode; read *Working a Baseline* before code.
5. Draft under `proposed-design-specs/` and seed Discussion.

Reopening follows product specs authoring
[§ The change package](../ProductSpecs/product-specs-authoring.md#the-change-package) and
[§ Reopening](../ProductSpecs/product-specs-authoring.md#reopening), with `C3` for `C7`: a recorded
write returns to promotion; resolved `D<n>` items are never disturbed.

**Audit:** on an audit request or changed guides, before any edit run `V1`–`V10` over every
draft. Record each failure with a proposed fix in Discussion; block until resolved, then fix.

**Change requests** arrive as input on reopen, filed by any downstream consumer against this
package or the specs, in the form and lifecycle of
[artifact formats § Change Requests](design-specs-artifacts.md#change-requests). Triage each on the
request itself — `Rejected` names the new package a valid request belongs to — and re-render its
page. `Proposed` blocks readiness.

## Drafting

Work screen by screen: open the drawings, requirements and, for backfills, the app and code; draft;
record uncertainties; continue. Seek decisions only after the last screen.

Answer app-behavior questions from code and requirements; ask only about product intent. Draft
even uncertain items under the recommended reading, linked from Discussion's Concern or Proposal.

Unobserved platform/service differences are package Assumptions; write specs for every app.
Only observed differences become known-difference notes.

- Draft cited files first. Cite existing draft/canonical IDs, never predictions. For mutual
  references, draft both, then revisit the first.
- One author writes drafts. Research/review may be delegated, but returned text is input only.

### Working a Baseline

- Before code, write the root product paragraph from the requirements root and design: organize
  by product, not implementation.

### Working a Scoped Change

Retain draft and canonical IDs. Apply
[Modify vs. Retire](design-specs.md#modify-vs-retire); ambiguous calls need Discussion because they
burn IDs and repoint citations. **Before modifying or retiring an ID or a glossary entry, run the
tool's `references`** (the ID, or the term for every linked occurrence) over the specs, the product
catalog and the active packages and decide per citation whether it still holds: a spec citation
that does not is repaired by drafting its file (in Touches, as the artifact formats say); one in
the product specs by a change request against them (*Requirements Gaps*); one in a work spec or
another package is not the author's to edit — name it in the sweep for its owner. Record the sweep
under `## Verification`. Moves preserve text; classify edits by that test.

### Design vs. App Differences

For each confirmed backfill difference, recommend one of two outcomes in Discussion:
**design stands** (note the app's known difference with its tracking issue), or **app stands**
(correct the drawing) — directly when the file is unmanaged, otherwise through a
[design package](../Design/design-authoring.md). For conflicting
sources or suspected defects, establish the intended contract and bring one item, not one per
instance.

### Undrawn States

Before requesting a drawing, apply [What Counts as a State](design-specs.md#what-counts-as-a-state):
data, dropped elements, unstyled system UI and motion use words. A needed undrawn state/variant
gets a Discussion proposal naming its drawing, produced directly or through design management as
above.

### Requirements Gaps

Never quietly specify a screen-independent promise or narrowed requirement. File a change request
against the change's open product spec package, or the catalog when there is none, in the form of
[`product-specs-artifacts.md` § Change Requests](../ProductSpecs/product-specs-artifacts.md#change-requests),
optionally with proposed drafts; never edit that package. The gap is a Discussion item linking the
request, drafted under the recommended reading and resolved on triage; once incorporated, the spec
cites the requirement's draft ID, and spec promotion waits for that requirement's promotion.

## Discussion

Group items under `###` topics, never in aggregator sections.

Use `- [ ] D<n> [Kind] <summary>`, with Kind `[Question]`, `[Proposal]` or `[Tradeoff]`.
Bold sub-bullet labels, without separators: **Concern** (required), **Proposal**, **Question**,
**Options**, **Detail**, **Why**, **Decision**. Recommend whenever possible; Tradeoffs name
the preferred option and why. Reserve Questions for cases with no basis to recommend.

Concerns must make sense without ID links. Package prose may name frames, nodes and code files.

### What Earns an Item

Only supervisor-dependent spec changes: design/app differences, undrawn states, requirements gaps
awaiting triage, ambiguous modify/retire or placement calls, unresolved product intent, and audit
failures. Draft determined behavior directly; record givens as assumptions.

With no items use: “The listed Inputs determine the proposed specs; review the drafts on the
review page before they are finalized.” Omit when items exist. An undrawn-state item proposes
the drawing by product name (“Draw `notes — acknowledged reminder`”).

### Resolution

Follow the item approval/marker lifecycle in *Advance Intent*. Append Decision last, never into
Concern. For drawings, name the product-language drawing in Decision.
Apply decisions differing from recommendations before continuing. If design stands, add the item's
known-difference note. Maintain draft links.

## Spec Changes

`## Spec Changes` is maintained with the drafts, from the first draft on: whenever a draft changes,
the list states exactly the canon-to-drafts difference, one typed item per difference, compared and
granulated as [artifact formats](design-specs-artifacts.md) says, no text inline. Never deferred
past the gate: the rendered page takes each change's reason from it, and `check-changes` confirms
it in the pre-gate pass.

On reopen, reconcile the recomputed diff: retain matching `S#` items and justifications, add new
differences, remove vanished ones. Never reset the section.

## Completion

After the Discussion gate advances: update Assumptions/TODOs and Out of scope, validate and render
once more, then emit `🏁 Complete. Let me know if anything needs adjustment.`

Promotion is invoked separately; implementation and design state beyond `V5` are irrelevant.

## Artifact Maintenance

Before responding, update the authoring artifact with `## Spec Changes`, align drafts, run
`validate` then `render` — on every material change: a draft edited, an item resolved, a change
item added, a request triaged — then emit the prescribed gate. Apply changes, never merely describe
them. The pre-gate pass runs once, where the planned gate would be emitted.

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
