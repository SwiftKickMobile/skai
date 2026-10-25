Managed-By: skai
Managed-Id: guide.design-specs-authoring
Managed-Source: Guides/DesignSpecs/design-specs-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Design Specs Authoring

Print `📖 SKAI guide: design-specs-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Draft specs in a change package; settle supervisor questions; ready it to promote.
Edit only the package and drafts. Before drafting, read [content rules/checks](design-specs.md);
[formats](design-specs-artifacts.md) owns packages, typed changes and requests;
[shape/tool](../Core/spec-file-shape.md) owns file shape and the spec tool.

Inputs are open-ended; always propose; reserve Discussion for supervisor input.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## The Change Package

[Artifact formats § The Package](design-specs-artifacts.md#the-package) owns contents, path and
decoupling; read [`change-requests.md`](../Core/change-requests.md) for the **base**.
For a production base, use the supplied change ID or propose a short kebab-case ID (from a branch,
its final component) and block before creation. Check active and promoted paths: reopen unpromoted work; use new IDs for promoted ID/type pairs.
Sibling types update freely while the change
is open; a consumer wanting it changed files a request against it.

### What `proposed-design-specs/` Holds

Draft whole files at touched paths only. Reuse drafts; copy missing ones from base drafts, following
bases to canon, or create if absent throughout. Keep unchanged items, index lines and glossary entries.
New specs roots need the root index, glossary and all three folder indexes. Leave absent files untouched;
delete none. Restructure via `move` items; keep unmoved source content.

### Artifact Skeleton

```
# Design Specs — <name>
[Review page](design-specs-review.html)
## Goal                   one or two sentences; no motivation essay
## Inputs                 draft sources
## Mode                   Baseline | Scoped change
## Discussion             open questions and decisions
## Spec Changes           typed change items, kept current as the drafts change
## Assumptions and TODOs  what the drafts assume; notes needing no decision; may be empty
## Out of scope           excluded work; may be empty
## Verification           one evidence line per check and per reference sweep
## Decision Log
```

## Modes

Infer from the base, never declaration: **Baseline** if nothing exists for the touched screens (all
additions); otherwise **Scoped change**. In doubt, use Scoped change.

## Gates

When waiting on the supervisor, end the message with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is a human or authorized agent outside this workflow who resolves its discussion items and reviews its gates; the executing agent cannot resolve or approve its own.

**Gate persistence.** After emitting a `⏳ GATE:` line, end every response — including discussion, clarifications and refinements — with that line verbatim until the gate moves. Change it only when its content changes (e.g., a blocker emerges or `Next` needs revision); then emit the new line in full at the response's end. Never paraphrase, shorten or silently change it.

**No fabricated gates.** Use `⏳ GATE:` only at gates this `## Gates` section defines or a properly emitted blocked gate. Never invent categories or labels for discussion state, partial completion or intermediate review. If a needed gate is undefined here, file the missing gate as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are this workflow's expected review points. At each:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the supervisor.

In a planned gate, `<what happens after your response>` describes the agent's action after supervisor advance intent. For a non-standard gate, describe the exact supervisor response or handoff needed to resume.

For an unexpected blocker, use the blocked gate line and STOP until the supervisor resolves it.

Workflow-specific gate notes:
- While any non-gap `- [ ]` item remains in `## Discussion`, end every response with the blocked
  gate and remaining count. Once every screen this package covers is drafted and every non-gap item is resolved — or no items were produced — emit the planned gate; there is no separate "draft is ready" gate.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them and I finish the package.`
  - Planned: `⏳ GATE: Next: Discussion complete<; N open gaps carried>. Say "next" to close the discussion; I then finish the package for your review.`
  Before the planned gate, run the **pre-gate pass** once (also under `auto`, which bypasses
  only the gate): the tool's `validate` over the drafts projected on the base (what blocks is
  the content guide's), then `V1`–`V10` in [`design-specs.md`](design-specs.md) § Verification
  Checks, then `check-changes` on `## Spec Changes`. One evidence line per check under
  `## Verification`, in promotion's evidence form; a check with no line has not run. `V5` means
  inspecting the design file; a missing drawing for a state this package's changes prescribe is
  a Discussion item, not a failed gate. Fix the artifact before the gate.
- Drawing items (*Undrawn States*, *Design vs. App Differences*) stay open until the drawing exists
  and the agent has seen it. Requirements gaps (*Requirements Gaps*) stay open until the product
  spec outcome reaches the draft, unless they carry a **Gap** line; otherwise the gate stays blocked.

Workflow-specific blocked gates:
- Inputs are too contradictory or incomplete to draft a screen.
- The change ID cannot be determined from the input, so the package has no path yet.
- The design file cannot be reached, so `V5` cannot run.
- A new prefix collides with one already in use, and the resolution is a naming call.

## Advance Intent

Advance intent passes the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- It approves passing a gate only after you emit a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the active-phase rules below; never skip phases or clear unrelated progress markers.

`auto` is advance intent bypassing planned gates only; blocked gates require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestone here: `discussion complete`, the single planned gate.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs): check completed items, preserving their audit trail.
  - **`🟡` in source files** seeded or planned by a skai workflow: **remove** on completion.
- By default, markers mean TODO or pending approval; clearing them requires supervisor approval.
- At a planned gate, stop and wait. Supervisor advance intent then approves clearing guide-owned markers completed by the preceding phase.

**Workflow-specific marker lifecycle.** This workflow owns only `- [ ] D<n>` items in `## Discussion`.
Resolve each on explicit supervisor approval of *that item*: check its box and append
`- **Decision** <resolution>.` Discussion-gate advance intent does not clear them; they are already clear
when that gate is reached. Gaps stay unchecked and block promotion into production.
`## Spec Changes` items carry no checkbox, and nothing under `proposed-design-specs/**` carries a
progress marker — those files are drafts of canon and must read as canon. Discussion
links to drafts; specs carry no Discussion citations but a gap footnote's `D#`.

**Workflow-specific `auto` behavior.** `auto` suits fully specified baselines.

## Initiation

Begin on explicit intent to write, backfill or audit specs, or request a package change; prior
conversation is context.

1. For first specs, follow [artifact hosting](../Core/artifact-hosting.md) and add the README link.
2. Read [content rules](design-specs.md), existing specs, affected requirements and the design tool
   guide ([Figma](../Design/figma-designer-guide.md)).
3. For a request, reopen or create `<base>/change-requests/<nnn>/` per the shared guide; otherwise
   reopen named or contextual unpromoted work, or resolve the ID and check its paths for a new
   package. Create the artifact with Goal/Inputs.
4. Infer mode; read *Working a Baseline* before code.
5. Draft under `proposed-design-specs/` and seed Discussion.

Reopening follows product specs authoring
[§ The change package](../ProductSpecs/product-specs-authoring.md#the-change-package) and
[§ Reopening](../ProductSpecs/product-specs-authoring.md#reopening), with `C3` for `C7`,
`## Spec Changes` for `## Requirement Changes`, the canonical specs for the catalog and
`design-specs-promotion.md` for its promotion artifact.

**Audit:** on an audit request or changed guides, before any edit run `V1`–`V10` over every
draft. A failure in what this package changed is a Discussion item with a proposed fix, blocking
until resolved; one already in unchanged content starts a package against the base.

## Drafting

Work screen by screen: open drawings, requirements and, for backfills, the app and code; draft and
record uncertainties. Seek decisions only after the last screen.

Answer app-behavior questions from code and requirements; ask only about product intent. Draft uncertain
items under the recommended reading or gap placeholder. Footnote with the item ID per the shape guide,
even with no placeholder and dependent text omitted; link from Discussion's Concern or Proposal.

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
tool's `references`** over the specs, the product
catalog and the active packages and decide per citation whether it still holds: a spec citation
that does not is repaired by drafting its file; one in
the product specs by *Requirements Gaps*; one in a work spec or
another package is not the author's to edit — name it in the sweep for its owner. Record the sweep
under `## Verification`. Moves preserve text; classify edits by that test.

### Design vs. App Differences

For each confirmed backfill difference, recommend in Discussion: **design stands** (note the app's
known difference with its tracking issue), or **app stands** (correct the drawing), directly for an
unmanaged file, otherwise through a
[design package](../Design/design-authoring.md). For conflicting
sources or suspected defects, establish the intended contract and bring one item, not one per
instance.

### Undrawn States

Before requesting a drawing, apply [What Counts as a State](design-specs.md#what-counts-as-a-state):
data, dropped elements, unstyled system UI and motion use words. A needed undrawn state/variant
gets a Discussion proposal naming its drawing, produced directly or through design management as
above.

### Requirements Gaps

Never quietly specify a screen-independent promise or narrow a requirement. Draft a product-specs
package against the subject's open package; if none is open, send the gap to product specs authoring. Link the work in a Discussion item (**Gap** to carry it); draft per *Drafting*.
Apply the recorded outcome — keep, revise, remove or wait — before resolving it. After promotion into the product
spec package, cite the requirement's draft ID.

## Discussion

Group items under `###` topics, never in aggregator sections.

Use `- [ ] D<n> [Kind] <summary>`, with Kind `[Question]`, `[Proposal]` or `[Tradeoff]`.
Bold sub-bullet labels, without separators: **Concern** (required), **Proposal**, **Question**,
**Options**, **Detail**, **Why**, **Gap** last for unchecked gaps (placeholder or "no placeholder; waiting on <what>"), **Decision**. Recommend when possible; Tradeoffs name
the preferred option and why. Reserve Questions for cases with no basis.

A gap on an input you rely on, or an item of yours that cannot be resolved because something outside this work is not yet known, is handled per [`known-gaps.md`](../Core/known-gaps.md).

Name a frame, node or file only where the reader must go to it.

### What Earns an Item

Only supervisor-dependent spec changes: design/app differences, undrawn states, requirements gaps
awaiting a decision, ambiguous modify/retire or placement calls, unresolved product intent, and audit
failures. Draft determined behavior directly; record givens as assumptions. A decision the
supervisor supplies without an item is recorded as a checked item with its Decision line.

With no items, Discussion is one sentence saying which input settled the specs and that the drafts
follow it; omit it when items exist. An undrawn-state item proposes
the drawing by product name.

### Resolution

Follow the marker lifecycle in *Advance Intent*. Append Decision last, never into Concern. Remove resolved items nothing current cites or needs. For gaps, remove **Gap**; Decision names the outcome and whether the question was answered, the placeholder adopted or the item omitted. Keep at most one Decision: replace it and log `decided` on change. Only withdrawal without replacement reopens: remove Decision, uncheck, log `reopened`. End with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>` per state change; keep entries after item removal. Tools check log and items agree. For drawings, name the product-language drawing in Decision.
Apply decisions differing from recommendations before continuing. If design stands, add the item's
known-difference note. Maintain draft links.

## Spec Changes

Maintain `## Spec Changes` from the first draft, updating the base-to-drafts difference with each
edit at [artifact formats](design-specs-artifacts.md)'s granularity, omitting spec text. Never defer
past the gate: it supplies the page's change reasons and the pre-gate `check-changes` confirms it.

On reopen, reconcile the recomputed diff: retain matching `S#` items, a justification only while it still explains the current
difference; add new differences, remove vanished ones. Never reset the section.

## Completion

After the Discussion gate advances: update Assumptions/TODOs and Out of scope, validate and render
once more, then emit `🏁 Complete. Let me know if anything needs adjustment.`

Promotion is invoked separately; implementation and design state beyond `V5` are irrelevant.

## Artifact Maintenance

Before responding, update the authoring artifact with `## Spec Changes`, align drafts, run
`validate` then `render` on every material change, then emit the prescribed gate. Apply changes, never merely describe
them.

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
