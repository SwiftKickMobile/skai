Managed-By: skai
Managed-Id: guide.product-specs-authoring
Managed-Source: Guides/ProductSpecs/product-specs-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Product Specs Authoring

Print `📖 SKAI guide: product-specs-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Draft product requirements in a **change package**, settle questions with the supervisor and ready
it to promote.

Edit only the package and drafts, not canon. Adjacent findings go in Discussion if they affect
requirement decisions, Assumptions and TODOs if nonblocking, Out of scope if excluded;
adjacent edits need separate authorization. Before drafting, read
[`product-specs-catalog.md`](product-specs-catalog.md) for content rules;
[`product-specs-artifacts.md`](product-specs-artifacts.md) for packages and change items;
[`spec-file-shape.md`](../Core/spec-file-shape.md) for file shape and the spec tool.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## The change package

[`product-specs-artifacts.md`](product-specs-artifacts.md) § The Package owns the path and contents:
`product-specs-authoring.md`, drafts in `proposed-product-specs/`, `product-specs-review.html`,
requests and promotion artifacts; read [`change-requests.md`](../Core/change-requests.md) for the **base**.

Against production, use a supplied change ID or propose a short kebab-case one (from a branch,
its final component) and block before creation. Check the active and promoted paths:
reopen unpromoted work; a recorded `C7` write with repair or archival pending returns to promotion,
not drafting; a closed `C7` ID/type pair needs a new ID.

Sibling types for the same change are independent: each in its canonical repository, linked by
resolved paths, archived separately and updating freely while the change is open. Consumers wanting
changes file requests against them.

### What `proposed-product-specs/` holds

Draft only touched files **whole** at catalog paths, keeping unchanged requirements, index lines and
glossary entries. Reuse drafts; copy missing ones from base drafts, following bases to the catalog,
or create if absent throughout. In every mode, new scopes copy the root and index files they rewrite.

New catalogs need `_product-specs.md`, `glossary.md` and an index per populated scope; new scopes
carry each created folder's index and the root index. Absent files stay untouched. Packages cannot
delete or split files; retirement edits a requirement in its file. Needed splits take a blocked gate.

### Artifact skeleton

```
# Product Specs — <name>
[Review page](product-specs-review.html)
## Goal                   one or two sentences; no motivation essay
## Situations             optional: the situations served, in plain language, each naming its IDs
## Inputs                 draft sources
## Mode                   Baseline | Scoped change
## Discussion             open questions and decisions
## Requirement Changes    typed change items, kept current as the drafts change
## Assumptions and TODOs  what the drafts assume; notes needing no decision; may be empty
## Out of scope           excluded work; may be empty
## Verification           one evidence line per check and per reference sweep
## Decision Log
```

## Modes

- **Baseline** — the base holds none of the files this package writes; everything is an addition.
- **Scoped change** — the base already holds files this package modifies, retires or adds to.

**Infer mode from the base, never caller declaration.** A package may be baseline for one scope
and a scoped change overall. In doubt, use scoped change; it handles baselines with explicit items.

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
  gate and remaining count. Once every subject this package covers is drafted and every non-gap item is resolved — or drafting
  produced no items because the inputs fully specify the requirements — emit the planned
  gate advancing to Completion; there is no separate "draft is ready" gate.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them and I finish the package.`
  - Planned: `⏳ GATE: Next: Discussion complete<; N open gaps carried>. Say "next" to close the discussion; I then finish the package for your review.`
  Before the planned gate, run the **pre-gate pass** once (also under `auto`, which bypasses
  only the gate): the tool's `validate` over the drafts projected on the base (what
  blocks is the catalog guide's), then `check-changes` on `## Requirement Changes`, then promotion's
  `C1`–`C5` in [`product-specs-promotion.md`](product-specs-promotion.md), enumerated only there.
  One evidence line per check under `## Verification`,
  in promotion's evidence form; a check with no line has not run. Stop at `C5`: `C6`–`C8` are
  promotion's. Fix the artifact before the gate so the supervisor reviews it.

Workflow-specific blocked gates:
- Inputs are too contradictory or incomplete to draft a subject.
- The change ID cannot be determined from the input, so the package has no path yet.
- A new prefix collides with one in use, and the resolution is a naming call.
- A file must be split into a folder, which a package cannot express.

## Advance intent

Advance intent passes the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- It approves passing a gate only after you emit a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the active-phase rules below; never skip phases or clear unrelated progress markers.

`auto` is advance intent bypassing planned gates only; blocked gates require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestone in this workflow: `discussion complete` — the workflow's single planned gate.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs): check completed items, preserving their audit trail.
  - **`🟡` in source files** seeded or planned by a skai workflow: **remove** on completion.
- By default, markers mean TODO or pending approval; clearing them requires supervisor approval.
- At a planned gate, stop and wait. Supervisor advance intent then approves clearing guide-owned markers completed by the preceding phase.

**Workflow-specific marker lifecycle.** This workflow owns only `- [ ] D<n>` items in `## Discussion`.
Resolve each on explicit supervisor approval of *that item*: check its box and append
`- **Decision** <resolution>.` Discussion-gate advance intent does not clear them; by then they are clear. Gaps stay unchecked; they block promotion into production. `## Requirement Changes` items
carry no checkbox — the drafts realize the change — and nothing under `proposed-product-specs/**`
carries a progress marker: those files are drafts of canon and must read as canon. Discussion
links to drafts; requirements carry no Discussion citations but a gap footnote's `D#`.

**Workflow-specific `auto` behavior.** `auto` suits fully specified baselines; a concept inventory awaiting confirmation still needs the
supervisor.

## Initiation

Start on an explicit signal: "write", "backfill", "update the requirements for X" or
"request a change to <package>". Earlier context sets no entry point or mode.

1. When the catalog does not exist yet, follow [`artifact-hosting.md`](../Core/artifact-hosting.md)
   to settle where it lives and link it from the README.
2. Read [`product-specs-catalog.md`](product-specs-catalog.md) and the existing catalog.
3. For a request, reopen or create `<base>/change-requests/<nnn>/` per the shared guide; otherwise
   reopen unpromoted work named or in context, including another workflow's seed (*Reopening*).
4. For other new packages, resolve the change ID and check its paths; create the artifact with
   `## Goal` and `## Inputs`.
5. Infer the mode. Baseline: read [`product-specs-baseline.md`](product-specs-baseline.md) before
   reading the implementation.
6. Draft (*Drafting*), starting with the concept inventory, and seed `## Discussion`.

### Reopening

Which package to reopen, return to promotion, or create is *The change package*'s rule. A seeded package may hold only drafts and `## Discussion`: complete Goal, Inputs and Mode first.
Fix promotion findings (the package's `product-specs-promotion.md` Evidence) in drafts; add Discussion
items only when the fix needs a decision.

**Re-read the base on every reopen.** Re-derive mode and list from it, promoted requests'
drafts too.

**Resolved decisions keep their history.** Resolved `- [x] D<n>` items keep their number, Concern,
Options and Proposal; *Resolution* governs state. Continue numbering new items; keep draft links current.

## Drafting

One author writes drafts. Research and review may be delegated, but delegated sessions write
nothing in the package — no draft, item or ID. Their returns are input, never text carried into drafts.

### Concept inventory

Before any app behavior, list the concepts the change touches and check each against the company's
own vocabulary and the base's `domains/` and glossary (its drafts over the catalog). A concept that is absent, or whose
meaning changes, is drafted first, in `domains/` and the glossary, and brought to `## Discussion` as one
`[Proposal]` item naming them: an open non-gap item holds behavior depending on them at the
blocked gate, `auto` included; one the supervisor has already settled is recorded
as *Resolution*'s checked item and drafting continues. An inventory that finds every concept
already in the base says so under `## Assumptions and TODOs`. ❌ sharing requirements
drafted before the base had a Collaborator, each rewritten once it landed · ✅ Collaborator
and its roles confirmed, then the sharing behavior on them.

Optional `## Situations` names situations and the IDs that serve each in the product manager's terms,
so they can confirm their input was understood and a designer has the brief.

### Working a backfill

For an existing implementation and its designs, work **subject by subject** after concepts are
confirmed: read designs and the subject's code, write requirements from product behavior, not code
structure, and record uncertainties in Discussion. Externally unobservable states are not behavior.
Never interrupt drafting for decisions: the gate comes once, after the last subject.

When sources disagree or observed behavior may be defective, identify the intended contract and existing
coverage; bring unresolved intent to Discussion with a recommendation. Never add requirements to
enumerate instances of an already-covered bug.

### Working a scoped change

Edit drafts under `proposed-product-specs/` (initialized as *What `proposed-product-specs/` holds*
says), never catalog files. Keep every ID. For each requirement, rule or table row whose text changes, apply
*Modify vs. retire* in the catalog guide: clarification keeps the ID; changed contracts retire it
and add a new one. **Before modifying or retiring an ID or a glossary
entry, run the tool's `references`** (the ID, or the term for every linked occurrence) over the
catalog, the design specs and the active packages and decide per citation whether it still holds: a
catalog citation that does not is re-pointed by drafting its file into the package; one in the
design specs by a package against their open package, else as input for design specs authoring;
one in a work spec or another package is not the author's to edit — name it in the sweep for that
artifact's owner. Record the sweep under `## Verification`. Ambiguous calls become Discussion items: they burn an ID and re-point every work spec citing it.

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

With no items, Discussion is one sentence saying which input settled the requirements and that the
drafts follow it; omit it when items exist.

### Draft the requirement anyway

Open items never leave holes in drafts: write the recommended requirement or gap placeholder, footnoted
with the item ID per the shape guide, even with no placeholder and dependent text omitted. Link every
affected draft requirement by ID from Concern or Proposal. The item explains uncertainty; the draft
reads as complete.

Cite an item by a stable anchor, or the topic anchor plus the item ID (checkbox IDs create none). Stored links are reference-style, defined at the bottom; conversation links are inline or file/line
links.

**Example** (a Tradeoff):

```markdown
### Where sync boundaries fall

- [ ] D05 [Tradeoff] Does the selected theme sync across devices?
  - **Concern** The drafts say the theme is chosen per device ([THEME-01]). The designs show one theme control and nothing about devices; the app keeps the choice on the
    device, so two devices can show two themes.
  - **Options**
    - A — The theme syncs: one choice sets every device, as the single control suggests.
    - B — The theme stays per device, as the app works today.
  - **Proposal** I recommend B: the theme stays per device.
  - **Why** Appearance is a device matter: a phone in dark mode and a tablet in light mode keep their own
    looks, and the designs do not ask for syncing.

[THEME-01]: proposed-product-specs/features/theme.md#theme-01
```

### Resolution

On the supervisor's explicit approval of an item: check the box and append
`- **Decision** <resolution>.` last; the original is kept. Remove resolved items nothing current cites or needs. For gaps, remove **Gap**; Decision names the outcome and whether the question was answered, the placeholder adopted or the item omitted. Keep at most one Decision: replace it and log `decided` on change. Only withdrawal without replacement reopens: remove Decision, uncheck, log `reopened`. End with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>` per state change; keep entries after item removal. The tool checks they agree. A decision the
supervisor supplies without an item is recorded as a checked item with its Decision line. Apply a decision
that differs from the recommendation before continuing; an approved contract that differs from
confirmed implementation behavior gets the known-difference note under the draft requirement. Keep
the item's links aligned with the drafts.

## Requirement Changes

Maintain `## Requirement Changes` from the first draft: each draft edit updates the base-to-drafts
difference at [`product-specs-artifacts.md`](product-specs-artifacts.md)'s granularity. Never defer
past the gate: the page takes each change's reason from it; the pre-gate `check-changes` confirms it.

On reopen, recompute the difference and reconcile items; never reset the section. Keep matching items' `R#`, and a justification only while it still explains the current difference;
add new differences, remove vanished ones.

## Completion

After the Discussion gate advances, update `## Assumptions and TODOs` and `## Out of scope`,
validate and render once more, say whether promotion can follow now or waits on shipping (promotion's
*When promotion happens*), then end with `🏁 Complete. Let me know if anything needs adjustment.`

## Artifact maintenance

Before each response during drafting and Discussion, update `product-specs-authoring.md` with
`## Requirement Changes`, align `proposed-product-specs/`, run `validate` then `render` on every
material change (listed in the artifacts guide), and emit the prescribed gate. Apply changes, never merely describe them.

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
