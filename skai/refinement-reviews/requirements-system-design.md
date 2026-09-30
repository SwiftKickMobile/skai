# Requirements System Design

## Purpose

This document defines SKAI's requirements system: a per-project catalog of behavioral requirements,
the authoring workflow that drafts changes to it, and the promotion workflow that writes them. It is
the standard used to write and cold-review the runtime guides; it is not another guide an executing
agent must read.

The catalog exists so an agent implementing, testing, or debugging can learn what the system must do
without reading code or chat history. Everything below follows from that: stable IDs a work spec can
cite, indexes an agent can route by, prose a non-engineer can verify, and a write path narrow enough
that nothing reaches canon unchecked.

Reconstructed 2026-09-28 from the four guides and the findings log at
[`requirements-system-findings.md`](requirements-system-findings.md), which had been carrying the
design decisions without a spec to record them.

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md), especially Guide house style.
- [`Guides/Core/process-flow.md`](../../Guides/Core/process-flow.md) for gates, advance intent,
  `auto`, markers, and structured discussion items.
- [`Guides/UIMap/ui-map-architecture.md`](../../Guides/UIMap/ui-map-architecture.md) for the
  change-package model this system adopted: drafts and discussion in a package, a canonical artifact
  written only by promotion.

This document is authoritative for requirements behavior. Where a guide and this document conflict,
the guide is the stale side unless the findings log records a later decision.

## Complexity baseline

The guide set is four runtime guides plus one read only in Baseline mode:

| Guide | Role | 2026-09-28 |
| --- | --- | --- |
| `requirements-catalog.md` | content rules | 2,583 words · 16,901 bytes |
| `requirements-authoring.md` | drafting workflow | 3,599 words · 23,188 bytes |
| `requirements-promotion.md` | writing workflow | 3,496 words · 22,537 bytes |
| `requirements-artifacts.md` | typed formats | 1,342 words · 9,475 bytes |
| `requirements-baseline.md` | baseline-only concerns | 328 words · 2,162 bytes |

**Size budget: 11,000 words across the four runtime guides.** Provenance: set at 9,500 during round
8 (2026-08-29) without derivation; raised to 10,500 on the human's approval when it priced out a
correct fix; raised to 11,000 on 2026-09-28 when the set measured 11,024, with the expectation that the
existing guides can be trimmed. Record each guide's size and the delta from the budget after every
refinement round; a real defect whose fix cannot fit is a supervisor decision, never a silent overrun.

A new gate, check, artifact, mirror field, or proof burden is a complexity tradeoff, not an
improvement. The characteristic failure of this guide set, visible across its findings log, is a rule
re-cut on one line while every other sentence describing it stayed behind; repairs that add a second
home for a rule are worse than the defect.

## Design invariants

### P1. One catalog, one writer

Every project has at most one catalog, at the root its Integration block names, in one of three
repository shapes: `local`, `shared` (another repo's catalog, typically a submodule), or `none` (a
deliberate opt-out; requirements workflows skip). IDs are therefore always bare. **Promotion is the
only writer.** Authoring never touches the catalog; work-spec implementation, retro, and every other
workflow read it and never mutate it. A literal path is never a fallback for an unfilled Integration
block: the workflow stops instead.

### P2. The catalog is a stable contract

A requirement is an `##` heading carrying only its ID, with prose beneath. IDs are `<PREFIX>-<NN>`,
append-only **from the moment they are drafted** — a work spec may cite a `(pending)` ID — and never
renumbered. A retired requirement keeps its heading and ID with `(retired)` and a pointer to what
superseded it; nothing else in the catalog carries a status, a checkbox, a `🟡`, or a `(D#)`.
Modifying keeps the ID; changing the contract retires and adds. Prefixes are unique across the
catalog and recorded on the file's line in its scope index.

An existing catalog is not retroactively conformed. The rules bind what a package **writes**, not
what it carries forward; a package is never blocked by a defect it did not introduce.

### P3. Written from outside

Requirements state what the system must do as observed by a user, QA, or another system — `must` /
`should` / `will` — and are verifiable without reading code. Forbidden: data structures, storage,
concurrency, code identifiers, file paths, frameworks, temporal references, workflow state. The test
for placement is behavioral: a rule that holds with no UI is a domain rule; one that only matters
because a user is interacting is a feature or app rule. Scope is never by codebase, module, target,
or team.

### P4. Traversable from any entry point

A requirement that depends on another cites it inline by ID at the point of dependency. Index lines
name the questions a file answers, not its subject. The glossary is the catalog's second index:
every entry ends by pointing at the requirements that govern the term, and it gains each cross-cutting
term in the package that introduces it. Every behavioral claim has an ID; orientation prose carries
none.

### P5. Drafts live in a package; the package is the review surface

Authoring writes `skai/changes/<change-id>/`: the authoring artifact, `proposed-requirements/**`, and
whatever promotion later adds. The package holds **only the files it touches**, each drafted whole
(supervisor decision, pass 1). A file the catalog already has is copied out and edited; one it lacks is
drafted fresh. A package cannot express deleting or splitting a file; either stops at a blocked gate.

The drafts always read as a complete catalog. An open question never leaves a hole: the requirement
is drafted under the recommended reading and cites its `(D#)` inline. That citation is scaffolding,
stripped at promotion, never a marker.

### P6. Mode is inferred, per scope, from the catalog

Baseline means the catalog holds none of the files this package writes; scoped change means it holds
some. Never declared by a caller, re-derived on every reopen. A package may be baseline for one scope
inside a live catalog, so the distinction keys on **whether the catalog already holds the file**, not
on the package as a whole. Promotion timing keys on something else again: a package recording
behavior that **already ships** promotes on approval; one recording behavior still to come promotes
when the change ships. Baseline is structural and says nothing about shipping.

### P7. Discussion earns its items and gates once

An item is earned by a real decision: two sources disagreeing, behavior that looks like a defect
rather than intent, an undefined boundary, a placement call that could go either way, behavior in the
implementation that appears in no design. Every item carries the agent's recommendation. Implications
forced by the inputs are encoded directly. `## Assumptions and TODOs` is not a second parking lot:
anything whose resolution would change what a requirement *says* is an item.

A backfill drafts every subject in scope before stopping — never one subject per turn — and the
Discussion gate comes once, after the last subject. `auto` bypasses that planned gate, never the
blocked one: unresolved items are supervisor decisions.

### P8. Verification precedes the only write

Promotion runs `C1`–`C5` (IDs append-only, prefixes collide nowhere, cross-references resolve,
writing style, traversal), then `C6` strips the scaffolding from the text to be written — leaving the
drafts as they are — then `C7` writes the catalog and confirms the written text. The five verifying
checks are enumerated once, in promotion; authoring runs the same five before its gate so nothing is
discovered late. Each check covers what the package **adds or changes**; two verify wider and say so.

Promotion never rewrites a requirement's prose. A failing check blocks and returns the package to
authoring with the finding. When the catalog itself is wrong, promotion raises a **change request**
instead; the package cannot promote while one is `Proposed`.

**A check records a result or it did not run.** Silence is never a pass; an empty subject records
its emptiness. Codified after the third sighting of silence-as-proof.

### P9. Whole-file writes are the drafter's obligation, not a check's

`C7` writes each held file whole. Glossary entries and index lines an ID-only check cannot see are
carried forward by the drafting rule in P5, deliberately backed by no check: three successive
attempts to encode a whole-content check each shipped a defect of their own, no observed run has
dropped content, and any real catalog is in version control. This is an **accepted, stated risk**;
revisit only if an observed run actually drops content.

### P10. Workflow ownership stays narrow

Authoring owns the package and its drafts. Promotion owns the catalog write, its checks, and change
requests. Work-spec design invokes authoring for backfill and never places provisional requirements
in a design document; retro seeds a package and hands off. A promoted package is closed; new work on
the same subject opens a new package. Each workflow points at the others' artifacts rather than
restating their rules.

Research and review may be delegated to subordinate sessions; authoring may not. A delegated session
reports to the supervisor that spawned it, which escalates by judgment — the hierarchy, not a
reporting rule, is what carries a concern to the human.

## Artifacts

```text
<catalog root>/                       written only by promotion
  _requirements.md   glossary.md
  platform/ domains/ features/ apps/<app>/   each with <folder>/_<folder>.md

skai/changes/<change-id>/
  requirements-authoring.md           authoring's artifact
  proposed-requirements/**            the drafts, mirroring the catalog layout
  change-requests/requirements-<nnn>.md   raised by promotion; may be absent
  requirements-promotion.md           promotion's artifact; may be absent
  evidence/                           persisted check output; may be absent
```

### Authoring artifact

`## Goal` · `## Inputs` · `## Mode` · `## Discussion` (topic `###` subsections, `- [ ] D<n> [Kind]`
items with **Concern** / **Proposal** / **Why**, resolved by appending **Decision**) ·
`## Requirement Changes` (typed `R<n>` items stating exactly the catalog-to-drafts difference, written
after the gate, recomputable and reconciled on reopen) · `## Assumptions and TODOs` · `## Out of
scope`. Formats for change items and change requests live in `requirements-artifacts.md`, the
consumer-facing layer a downstream reader resolves without the authoring method.

### Promotion artifact

`## Inputs` · `## Promotion Checks` (`- [ ] C<n>`, execution order) · `## Change Requests` ·
`## Evidence` (one bracket per check, check ID first; a failed run's output persisted under a
run-keyed path; re-runs append below history). `## Completion` defines the promoted state.

## Workflow

### Authoring

1. **Initiate** on an explicit signal — "write", "backfill", "update the requirements for X" — with
   any input. Read the Integration block; stop if it cannot say where the catalog lives. Reopen an
   unpromoted package for this work rather than creating a second. Resolve the change id or stop.
2. **Draft** every subject in scope under `proposed-requirements/`, running `requirements-baseline.md`
   first when the catalog starts empty. Seed items only where a decision is real. End at the blocked
   Discussion gate while items remain; at the planned gate when none do or once all are resolved,
   after the `C1`–`C5` pass.
3. **Requirement Changes** after advance intent; bring assumptions and out-of-scope current; end
   `🏁 Complete.`, saying whether promotion is the human's next move or waits for a ship.

### Promotion

4. **Readiness screen**: Discussion fully resolved, change items match a recomputed diff, no change
   request `Proposed`, Integration block resolvable under its shape. Failure is a blocked gate.
5. **Checks listed** unchecked; planned gate: the human reviews what will become canon.
6. **Execute** `C1`–`C7` in order with evidence. A `C1`–`C5` failure blocks and returns to authoring;
   a fault after `C7` is repaired in place, since the write happened. Change requests go on reopen.

## Acceptance checks for the guides

A cold reviewer should verify:

1. Promotion is the only writer of the catalog, and no guide names a literal catalog path.
2. IDs are append-only from drafting; retire never deletes; every prefix is registered.
3. Every requirement is verifiable from outside; no code identifier, path, or storage mechanism.
4. Cross-references are inline by ID; index lines route; glossary entries point.
5. The package holds only touched files, each whole; deletion and splitting stop.
6. Mode is inferred per file from the catalog; promotion timing keys on shipping, not mode.
7. A backfill drafts all subjects before the single Discussion gate; `auto` never clears an item.
8. `C1`–`C5` have one enumeration; authoring runs them pre-gate; every check records a result.
9. Promotion never rewrites prose; a catalog defect becomes a change request, not an edit.
10. The whole-content risk is stated as accepted, and no guide claims a check covers it.
11. Each round reports the four guides' word counts against the 11,000 budget.
12. A fresh agent can author and promote from the artifacts without chat history.

## Open decisions (unimplemented ledger)

Recorded so a cold review does not re-raise them as findings:

- `C1`'s "accounted for" is a substring match; a shell one-liner cannot encode the judgment asked
  of it (r7). Architecture decision, open.
- No worked example of a passing `C4`; `C5` has no evidence bracket (r11). Priced out by budget.
- Mandatory inline cross-references have no check (r15). A proof burden; open.
- Drafting-complete conjunct not propagated to every gate surface (r16, F1a/F1c). Open.
- Authoring reopens a package by judgment where promotion blocks on the same ambiguity (r18). Open.
- Zero-padding inside a legacy file with unpadded IDs (r3). Convention call, logged.
- The four guides measure 11,020 against the 11,000 budget: 20 words over. Trim expected.
- P6 keys Baseline per file while Workflow step 2 says "when the catalog starts empty"; reconcile in the spec before either guide is edited on the trigger (r3 open question).
- The citation invariant is general but read only in Baseline mode; relocating it to the catalog guide costs ~35 budgeted words (r3 F4, logged by ruling).
