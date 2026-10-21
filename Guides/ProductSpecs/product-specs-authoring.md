Managed-By: skai
Managed-Id: guide.product-specs-authoring
Managed-Source: Guides/ProductSpecs/product-specs-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-21

# Product Specs Authoring

Print `📖 SKAI guide: product-specs-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Draft requirements into a **change package** against the product specs, resolve the open questions
they raise with the supervisor, and leave the package ready to promote.

Authoring edits the package and its drafts; the canonical catalog stays unchanged. Adjacent findings
go in Discussion when they affect a requirement decision, in Assumptions and TODOs when nonblocking,
in Out of scope when excluded; editing adjacent artifacts needs its own authorization. Read the
content rules, [`product-specs-catalog.md`](product-specs-catalog.md), before drafting; the package,
change items and requests are [`product-specs-artifacts.md`](product-specs-artifacts.md), the file
shape and the spec tool [`spec-file-shape.md`](../Core/spec-file-shape.md).

## The change package

[`product-specs-artifacts.md`](product-specs-artifacts.md) § The Package owns the path and contents:
this workflow's artifact `product-specs-authoring.md`, the drafts under `proposed-product-specs/`,
the rendered page `product-specs-review.html`, and what change requests and promotion add.

Use a supplied change ID; otherwise propose a short kebab-case ID and block before creation (from a
branch, its final component). Check the active and promoted paths:
reopen unpromoted work; a recorded `C7` write with repair or archival pending returns to promotion,
not drafting; a closed `C7` ID/type pair needs a new ID. Create the artifact with Goal and Inputs
before drafting.

Sibling types for the same change are independent: each in
its canonical repository, linked by resolved paths, archived on its own, updating freely while the
change is open. A consumer wanting this package changed files a change request (*Reopening*), never
edits it.

### What `proposed-product-specs/` holds

Only touched files, mirroring catalog paths, each drafted **whole** — carrying unchanged
requirements, index lines and glossary entries. Reuse an existing draft; initialize a missing draft
by copying the catalog file, or draft it fresh when the catalog lacks it. Per file, whatever the
mode: a new scope still copies the root and index files it rewrites.

A new catalog needs `_product-specs.md`, `glossary.md` and an index per populated scope; a new scope
carries each created folder's index and the root index. Absent files stay untouched; a package
cannot delete or split a file, and retirement edits a requirement within its file; a needed split
is a blocked gate.

### Artifact skeleton

```
# Product Specs — <name>
[Review page](product-specs-review.html)
## Goal                   one or two sentences; no motivation essay
## Situations             optional: the situations served, in plain language, each naming its IDs
## Inputs                 draft sources
## Mode                   Baseline | Scoped change
## Discussion             open questions and decisions
## Verification           one evidence line per check and per reference sweep
## Requirement Changes    typed change items, kept current as the drafts change
## Assumptions and TODOs  what the drafts assume; notes needing no decision; may be empty
## Out of scope           excluded work; may be empty
## Decision Log
```

## Modes

- **Baseline** — the catalog holds none of the files this package writes; everything is an addition.
- **Scoped change** — the catalog already holds files this package modifies, retires or adds to.

**Mode is inferred, never declared by a caller.** Read the catalog: a package may be baseline for
one scope and a scoped change overall — in doubt, scoped change, which handles a baseline with
explicit items. A change request is input on reopen, not a mode.

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
- The Discussion gate uses the canonical discussion-phase behavior: while any non-gap `- [ ]` item remains
  in `## Discussion`, every response ends with the blocked gate citing the remaining count; the
  moment every subject this package covers is drafted and every non-gap item is resolved — or drafting
  produced no items because the inputs fully specify the requirements — the agent emits the planned
  gate that advances to Completion; there is no separate "draft is ready" gate.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Completion.`
  - Planned: `⏳ GATE: Next: Discussion complete<; N open gaps carried>. Say "next" to advance to Completion.`
  Before emitting the planned gate, run the **pre-gate pass** once (under `auto` too, which bypasses
  the gate, not the pass): the tool's `validate` over the drafts projected on the catalog (what
  blocks is the catalog guide's), then `check-changes` on `## Requirement Changes`, then promotion's
  `C1`–`C5` in [`product-specs-promotion.md`](product-specs-promotion.md), enumerated only there.
  One evidence line per check under `## Verification`,
  in promotion's evidence form; a check with no line has not run. Stop at `C5`: `C6`–`C8` are
  promotion's. The gate presents what the supervisor reviews; fix the artifact before gating.

Planned gates for this workflow:
- After every subject is drafted and every non-gap Discussion item is resolved, before Completion.

Workflow-specific blocked gates:
- Inputs are too contradictory or incomplete to draft a subject.
- The change ID cannot be determined from the input, so the package has no path yet.
- A new prefix collides with one in use, and the resolution is a naming call.
- A file must be split into a folder, which a package cannot express.

## Advance intent

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
Discussion gate does not clear them; by then they are already clear. Gaps stay unchecked; they block promotion. `## Requirement Changes` items
carry no checkbox — the drafts realize the change — and nothing under `proposed-product-specs/**`
carries a progress marker: those files are drafts of canon and must read as canon. Discussion
links to drafts; requirements carry no Discussion citations but a gap footnote's `D#`.

**Workflow-specific `auto` behavior.** `auto` suits a baseline whose inputs fully specify the
requirements. It never bypasses the Discussion blocked gate: unresolved items — a concept inventory
awaiting confirmation included — are supervisor decisions.

## Initiation

The workflow starts on an explicit signal — "write", "backfill" or "update the requirements for X".
Whatever came before is context the agent digests; there is no declared entry point or mode.

1. When the catalog does not exist yet, follow [`artifact-hosting.md`](../Core/artifact-hosting.md)
   to settle where it lives and link it from the README.
2. Read [`product-specs-catalog.md`](product-specs-catalog.md) and the existing catalog.
3. If an unpromoted package for this work is named or in context — including one seeded by another
   workflow — reopen it rather than creating a second (*Reopening*).
4. Otherwise resolve the change ID, check its paths, create the artifact with `## Goal` and
   `## Inputs`.
5. Infer the mode. Baseline: read [`product-specs-baseline.md`](product-specs-baseline.md) before
   reading the implementation.
6. Draft (*Drafting*), starting with the concept inventory, and seed `## Discussion`.

### Reopening

Which package to reopen, return to promotion, or create is *The change package*'s rule. A seeded
package may hold only drafts and `## Discussion`: complete Goal, Inputs and Mode first. A promotion
finding (the package's `product-specs-promotion.md` Evidence) is fixed in the drafts, not made a
Discussion item unless the fix is itself a decision.

**Re-read the catalog on every reopen.** Re-derive the mode and the change list from the current
catalog, not from the artifact.

**Resolved decisions keep their history.** A resolved `- [x] D<n>` keeps its number, Concern,
Options and Proposal; *Resolution* governs its state; new items continue the numbering. Keep its
draft links current.

**Change requests** arrive as input on reopen, in the form and lifecycle of
[`product-specs-artifacts.md`](product-specs-artifacts.md) § Change Requests. The supervisor reads
each and says what to do with it; the agent applies that — for an incorporation the drafts and
`## Requirement Changes`, then `Incorporated`; otherwise the status and the supervisor's reason in
`Reviewer Response` — and re-renders its page. Until told, leave a `Proposed` request alone,
summarizing open requests when asked; never reject or supersede one on its own, and raise no
Discussion item to drive the ruling.

## Drafting

One author writes the drafts. Research and review may be delegated, but a delegated session writes
nothing in the package — no draft, item or ID — and what it returns is input, never text carried
into a draft.

### Concept inventory

Before any app behavior, list the concepts the change touches and check each against the company's
own vocabulary, the catalog's `domains/` and the glossary. A concept that is absent, or whose
meaning changes, is drafted first, in `domains/` and the glossary, and brought to `## Discussion` as one
`[Proposal]` item naming them: an open non-gap item holds behavior depending on them at the
blocked gate, `auto` included; one the supervisor has already settled is recorded
as *Resolution*'s checked item and drafting continues. An inventory that finds every concept
canonical says so under `## Assumptions and TODOs`. ❌ sharing requirements
drafted before the catalog had a Collaborator, each rewritten once it landed · ✅ Collaborator
and its roles confirmed, then the sharing behavior on them.

`## Situations` (optional) states the situations the requirements serve in the product manager's
own terms, each naming the IDs that serve it, so they can confirm the input was understood and a
designer has the brief.

### Working a backfill

When the source is an existing implementation and its designs, work **subject by subject** once the
concepts are confirmed: read the designs and the code implementing the subject, write the
requirements — from what the product does, not from how the code is shaped; a state nothing outside
can observe is not behavior — record what is uncertain as Discussion items, and move on. Never
interrupt drafting to seek a decision: the gate comes once, after the last subject.

When sources disagree or observed behavior may be a defect, identify the intended contract and its
existing coverage, then bring the unresolved intent to Discussion with a recommendation. Do not
multiply requirements to enumerate instances of an already-covered bug.

### Working a scoped change

Edit the draft under `proposed-product-specs/` (initialized as *What `proposed-product-specs/` holds*
says), never the catalog file. Keep every ID the file has. For each requirement, rule or table row
whose text changes, apply *Modify vs. retire* in the catalog guide: clarifying keeps the ID; a
changed contract retires it and adds a new one. **Before modifying or retiring an ID or a glossary
entry, run the tool's `references`** (the ID, or the term for every linked occurrence) over the
catalog, the design specs and the active packages and decide per citation whether it still holds: a
catalog citation that does not is re-pointed by drafting its file into the package; one in the
design specs by a change request against their open package, else as input for design specs
authoring ([§ Change Requests](../DesignSpecs/design-specs-artifacts.md#change-requests)); one in
a work spec or another package is not the author's to edit — name it in the sweep for that
artifact's owner. Record the sweep under `## Verification`. A call that could
go either way is a Discussion item: it burns an ID and re-points every work spec citing it.

## Discussion

Group items under `###` topics, never in aggregator sections.

Item line: `- [ ] D<n> [Kind] <summary>`, with Kind `[Question]`, `[Proposal]` or `[Tradeoff]`.
Bold sub-bullet labels, no separator: **Concern** (always), **Proposal**, **Question**, **Options**,
**Detail**, **Why**, **Gap** last for unchecked gaps (placeholder or "no placeholder; waiting on <what>"), **Decision** on resolution. Recommend when possible; Tradeoffs name the
preferred option and why; reserve Questions for cases with no basis to recommend.

A gap on an input you rely on, or an item of yours that cannot be resolved because something outside this work is not yet known, is handled per [`known-gaps.md`](../Core/known-gaps.md).

### What earns an item

Uncertainties that change a requirement: conflicting sources, apparent defects, undefined
boundaries, genuine placement or scope choices, implemented behavior absent from designs, the
inventory's new or changed concepts. Draft fully specified behavior directly; assumptions record
what is taken as given.

With no items, leave Discussion as: "The listed Inputs determine the proposed requirements; review
the drafts on the review page." Omit it when items exist.

### Draft the requirement anyway

An open item never leaves a hole in the drafts: write the requirement under the recommended reading
or, for a gap, its placeholder, footnoted with the item ID per the shape guide even when none
exists and the dependent text is left out, and, in the
item's Concern or Proposal, link every affected draft requirement by ID. The item explains the
uncertainty; the draft reads as complete.

Cite an item by a stable anchor, or the topic anchor plus the item ID (checkbox IDs create none). Stored links are reference-style, defined at the bottom; conversation links are inline or file/line
links.

**Example** (a Tradeoff):

```markdown
### Where sync boundaries fall

- [ ] D05 [Tradeoff] Does the selected theme sync across devices?
  - **Concern** [THEME-01] is drafted as device-local. Designs show one control; the implementation
    stores it locally, so two devices can disagree.
  - **Options**
    - A — Theme syncs, matching the single control in the designs.
    - B — Theme is per-device, matching the implementation.
  - **Proposal** B.
  - **Why** Theme follows each device's appearance.

[THEME-01]: proposed-product-specs/features/theme.md#theme-01
```

### Resolution

On the supervisor's explicit approval of an item: check the box and append
`- **Decision** <resolution>.` last; the original is kept. Remove a resolved item nothing current cites or needs. For gaps, remove **Gap**; Decision says answered, placeholder adopted, or omitted. At most one Decision: replace it and log `decided` on change; only withdrawal without replacement reopens (remove Decision, uncheck, log `reopened`). End with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>` per state change; keep entries after item removal. The tool checks they agree. A decision the
supervisor supplies without an item is recorded as a checked item with its Decision line. Apply a decision
that differs from the recommendation before continuing; an approved contract that differs from
confirmed implementation behavior gets the known-difference note under the draft requirement. Keep
the item's links aligned with the drafts.

## Requirement Changes

`## Requirement Changes` is maintained with the drafts, from the first draft on: whenever a draft
changes, the list states exactly the catalog-to-drafts difference, one typed item per difference,
compared and granulated as [`product-specs-artifacts.md`](product-specs-artifacts.md) says. It is
never deferred past the gate: the rendered page takes each change's reason from it, and
`check-changes` confirms it in the pre-gate pass.

On reopen, recompute the difference and reconcile the existing items against it — never reset the
section: an item that still matches keeps its `R#` and justification, a new difference gets a new
item, one that no longer holds loses its item.

## Completion

After the Discussion gate advances: bring `## Assumptions and TODOs` and `## Out of scope` up to
date, validate and render once more, and end with
`🏁 Complete. Let me know if anything needs adjustment.`

Promotion is invoked separately. A package recording shipping behavior, or approved intended
behavior with confirmed known-difference notes, may promote on supervisor approval; other future
behavior waits until it ships. Say which applies at completion.

## Artifact maintenance

On each response through drafting and Discussion, update the artifact before speaking: revise
`product-specs-authoring.md` with `## Requirement Changes`, bring `proposed-product-specs/` into line,
run `validate` then `render` on every material change (the artifacts guide lists them), and end at
whichever gate *Gates* prescribes. The pre-gate pass runs once, where the planned gate would be
emitted. Apply changes, never merely describe them.

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
