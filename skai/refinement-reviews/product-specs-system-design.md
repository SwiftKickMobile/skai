# Product Specs System Design

## Purpose

This document defines SKAI's product specs system (called the requirements system until
2026-10-18; the individual ID'd item is still a *requirement*): a per-project catalog of behavioral
requirements, the authoring workflow that drafts changes to it, the promotion workflow that writes
them, and the change requests downstream consumers file against either. The spec file shape and the
tool that validates, cross-references and renders it are shared with design specs and have their own
standard, [`spec-format-design.md`](spec-format-design.md). This document is the standard used to
write and cold-review the runtime guides; it is not another guide an executing agent must read.

The catalog exists so an agent implementing, testing, or debugging can learn what the system must do
without reading code or chat history. Everything below follows from that: stable IDs a work spec can
cite, indexes an agent can route by, prose a non-engineer can verify, and a write path narrow enough
that nothing reaches canon unchecked.

Reconstructed 2026-09-28 from the four guides and the findings log at
[`product-specs-system-findings.md`](product-specs-system-findings.md), which had been carrying the
design decisions without a spec to record them.

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md), especially Guide house style.
- [`Guides/Core/process-flow.md`](../../Guides/Core/process-flow.md) for gates, advance intent,
  `auto`, markers, and structured discussion items.
- [`Guides/UIMap/ui-map-architecture.md`](../../Guides/UIMap/ui-map-architecture.md) for the
  change-package model this system adopted: drafts and discussion in a package, a canonical artifact
  written only by promotion.

This document is authoritative for product specs behavior. Where a guide and this document conflict,
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

**2026-10-18:** the guides are renamed `product-specs-*.md`, the file-shape rules move out to the
shared spec-format guide, and authoring gains the concept inventory, Situations, the reference sweep
and change-request triage. The budget is re-measured after those moves and re-set by the supervisor;
until then 11,000 words is the reference point, not a binding cap.

A new gate, check, artifact, mirror field, or proof burden is a complexity tradeoff, not an
improvement. The characteristic failure of this guide set, visible across its findings log, is a rule
re-cut on one line while every other sentence describing it stayed behind; repairs that add a second
home for a rule are worse than the defect.

## Design invariants

### P1. One catalog, controlled writers

Every project has at most one catalog, at the root the project README links (since Release 13;
earlier an Integration block named it and a `local | shared | none` shape vocabulary applied), in
whichever repository the supervisor names for it. IDs need no catalog namespace; citations are linked.
**Promotion writes requirement contracts.** Authoring and retro never touch the catalog. Work-spec
implementation may update/remove confirmed known-difference notes for verified fixes only; contracts
and IDs remain read-only. Approved release migrations may change link presentation without changing
contracts. A literal path is never a fallback for an unfilled Integration
block: the workflow stops instead.

### P2. The catalog is a stable contract

A requirement is a `###` item carrying only its ID, in the shared spec file shape
([`spec-format-design.md`](spec-format-design.md)): a statement, then numbered rules cited as `ID-NN`
(one nesting level, `ID-NN-NN`, and no deeper) and tables whose rows carry no IDs, grouped under
uncited `##` sections. Rules retire in place like items. IDs are `<PREFIX>-<NN>`,
append-only **from the moment they are drafted** — a work spec may cite a `(pending)` ID — and never
renumbered. A retired requirement keeps its heading and ID with `(retired)` and a pointer to what
superseded it; nothing else in the catalog carries a status, a checkbox, a `🟡`, or a `(D#)`.
Modifying keeps the ID; changing the contract retires and adds. Prefixes are unique across the
catalog and recorded on the file's line in its scope index.

An existing catalog is not retroactively conformed during ordinary authoring/promotion. Explicit
release migrations are separate; a package is never blocked by a defect it did not introduce.

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
every entry is a `###` heading (so it has an anchor) ending by pointing at the requirements that
govern the term, and it gains each cross-cutting term in the package that introduces it. **Every
occurrence of a glossary term in spec prose links its entry**; the link is what tells a reader a word
is a defined term, so terms stay in sentence case (2026-10-18). The items an entry names as governing
it are exempt. An app's index lists the shared feature files that app offers; a feature absent from an
app's index is not in that app (`features/` exists to avoid duplicating shared behavior across apps,
not as a third kind of rule). Every behavioral claim has an ID; orientation prose carries none.

### P5. Drafts live in a package; the package is the review surface

Authoring writes `skai/changes/<change-id>/product-specs/`: the authoring artifact,
`proposed-product-specs/**`, and whatever promotion and change requests later add. The package holds **only the files it touches**, each drafted whole
(supervisor decision, pass 1). A file the catalog already has is copied out and edited; one it lacks is
drafted fresh. A package cannot express deleting or splitting a file; either stops at a blocked gate.

The drafts always read as a complete catalog. An open question never leaves a hole: the requirement
is drafted under the recommended reading. Discussion links to affected draft requirements; draft
requirements do not cite Discussion. Requirement dependencies remain inline reference-style links.

The artifacts of one change (product specs, designs, design specs) update freely while the change is
open; promotion is the control point, not the boundary between them (2026-10-18). A downstream
consumer that wants the package changed files a change request (P10) instead of editing it.

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

Drafting starts with a **concept inventory** (2026-10-18): the concepts the change touches, checked
against the company's own vocabulary and against `domains/` and the glossary. New or changed concepts
are drafted and confirmed by the supervisor before any app behavior is drafted on them; the Offers
package drafted app behavior on a catalog that had no Opportunity, and every app requirement had to
be rewritten. The authoring artifact may carry a `## Situations` section: the concrete situations the
requirements serve, in plain language, each pointing at the IDs that serve it, so the product manager
can confirm their input was understood in their own terms and a designer has the brief.

A backfill drafts every subject in scope before stopping — never one subject per turn — and the
Discussion gate comes once, after the last subject. `auto` bypasses that planned gate, never the
blocked one: unresolved items are supervisor decisions.

### P8. Verification precedes the only write

Promotion runs `C1`–`C5` (IDs append-only, prefixes collide nowhere, cross-references resolve,
writing style, traversal), then `C6` prepares destination-relative link definitions without changing
prose or the drafts, `C7` writes the catalog and confirms the written text, and `C8` archives the
package. The five verifying
checks are enumerated once, in promotion; authoring runs the same five before its gate so nothing is
discovered late. Each check covers what the package **adds or changes**; two verify wider and say so.

Promotion never rewrites a requirement's prose. A failing check blocks and returns the package to
authoring with the finding. When the catalog itself is wrong, promotion raises a **change request**
instead; the package cannot promote while one is `Proposed`.

The spec tool validates the drafts projected onto the catalog — shape, IDs unique, rule numbering,
table keys, link definitions, glossary links — at authoring's gate and before promotion writes; a
validation failure blocks (2026-10-18). Before modifying or retiring an ID **or a glossary entry**, authoring runs the tool's
`references` command, lists every citing location (for a term, every linked occurrence) across the
catalog, the design specs and active packages, and decides per citation whether the surrounding text
still holds; promotion checks that the sweep was recorded (glossary terms added 2026-10-18).

**A check records a result or it did not run.** Silence is never a pass; an empty subject records
its emptiness. Codified after the third sighting of silence-as-proof.

### P9. Whole-file writes are the drafter's obligation, not a check's

`C7` writes each held file whole. Glossary entries and index lines an ID-only check cannot see are
carried forward by the drafting rule in P5, deliberately backed by no check: three successive
attempts to encode a whole-content check each shipped a defect of their own, no observed run has
dropped content, and any real catalog is in version control. This is an **accepted, stated risk**;
revisit only if an observed run actually drops content.

### P10. Workflow ownership stays narrow

Authoring owns the package and its drafts. Promotion owns the catalog write and its checks.
**Change requests** (2026-10-18) may be filed by any downstream consumer — design authoring, design
specs, work specs, tests, promotion — for any reason, against the open package when there is one,
otherwise against the catalog, which opens a new package. A request carries a status, a reviewer
response, a title, a goal, and a `## Requested Changes` list in the same typed format as Requirement
Changes, optionally with its own `proposed-product-specs/**` drafts in the spec shape. Authoring
triages each to Incorporated, Rejected or Superseded and records the outcome on the request; the
proposer never edits the package; a package cannot promote while a request is `Proposed`. Work-spec design invokes authoring for backfill and never places provisional requirements
in a design document; retro seeds a package and hands off. A promoted package is closed; new work on
the same subject opens a new package. Each workflow points at the others' artifacts rather than
restating their rules.

Research and review may be delegated to subordinate sessions; authoring may not. A delegated session
reports to the supervisor that spawned it, which escalates by judgment — the hierarchy, not a
reporting rule, is what carries a concern to the human.

## Artifacts

```text
<catalog root>/                       written only by promotion
  _product-specs.md   glossary.md
  platform/ domains/ features/ apps/<app>/   each with <folder>/_<folder>.md

skai/changes/<change-id>/product-specs/
  product-specs-authoring.md          authoring's artifact
  proposed-product-specs/**           the drafts, mirroring the catalog layout
  change-requests/<nnn>/request.md    status, reviewer response, title, Goal, Requested Changes
  change-requests/<nnn>/proposed-product-specs/**   the request's drafts; optional
  product-specs-promotion.md          promotion's artifact; may be absent
  evidence/                           persisted check output; may be absent
```

The tool renders a package as one review page and a request as its own page relative to the package;
what those pages show is in [`spec-format-design.md`](spec-format-design.md).

### Authoring artifact

`## Goal` · `## Situations` (optional, 2026-10-18) · `## Inputs` · `## Mode` · `## Discussion` (topic `###` subsections, `- [ ] D<n> [Kind]`
items with **Concern** / **Proposal** / **Why**, resolved by appending **Decision**) ·
`## Requirement Changes` (typed `R<n>` items stating exactly the catalog-to-drafts difference, maintained
as the drafts change — the rendered page takes each change's reason from it, so it is never deferred to
after the gate (2026-10-18) — checked against the computed diff by the tool, reconciled on reopen) · `## Verification` (evidence of the pre-gate pass and the reference sweep; a check records a
result or did not run, 2026-10-18, target 3) · `## Assumptions and TODOs` · `## Out of
scope`. Formats for change items and change requests live in `product-specs-artifacts.md`, the
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
2. **Draft**: the concept inventory first, confirmed by the supervisor; then every subject in scope
   under `proposed-product-specs/`, running the baseline guide first when the catalog starts empty.
   Run the reference sweep before any modify or retire, and the spec tool's validation before the gate. Seed items only where a decision is real. End at the blocked
   Discussion gate while items remain; at the planned gate when none do or once all are resolved,
   after the `C1`–`C5` pass.
3. **Completion** after advance intent: the change list already current (it is maintained with the
   drafts; the tool's `check-changes` confirms it), bring assumptions and out-of-scope current, render,
   and end `🏁 Complete.`, saying whether promotion is the supervisor's next move or waits for a ship.

### Promotion

4. **Readiness screen**: Discussion fully resolved, change items match a recomputed diff, no change
   request `Proposed`, the catalog root linked from the project README (the root-location authority
   since Release 13, via `artifact-hosting.md` for a first artifact; the "Integration block" wording
   above is historical, 2026-10-18). Failure is a blocked gate.
5. **Checks listed** unchecked; planned gate: the human reviews what will become canon.
6. **Execute** `C1`–`C8` in order with evidence. A `C1`–`C5` failure blocks and returns to authoring;
   a fault after `C7` is repaired in place, since the write happened. Change requests go on reopen.

## Acceptance checks for the guides

A cold reviewer should verify:

1. Contract writes belong to promotion; verified known-difference cleanup is the narrow implementation exception. Catalog roots are resolved, never guessed.
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
13. Files follow the shared spec shape and the tool validates them at both gates; the guides cite the
    shape guide rather than restating it.
14. The concept inventory precedes app behavior and is gated; Situations is present and optional.
15. Glossary entries are headings and every occurrence of a term is linked.
16. Modify and retire trigger the reference sweep with the tool, recorded as evidence.
17. Change requests come from any consumer, are triaged on the request, and the proposer never
    edits the package.
18. An app's index lists the feature files it offers.

## Approved release decisions — 2026-10-05

These supervisor-approved decisions (#49, #52, #53, #55, #64) qualify the earlier invariants and
are the standard for this scoped refinement. No new runtime guide or peer-guide reference is needed.

- Content: clarify product guarantees versus screen arrangement with examples in the existing
  catalog guide. Preserve meaningful navigation/presentation guarantees. Before turning a source
  bug into a requirement, identify its underlying contract and reuse coverage; negative boundaries
  remain valid when they express an essential product constraint.
- Known differences: immediately below a requirement, a blockquote labeled **Known difference —
  <app/platform>** states confirmed current behavior and the gap, with a tracking link when available.
  This observation is not a new normative claim or exception. Same format in drafts and canon;
  suspected differences await a Discussion decision. This is the narrow exception to P2/P3's ban on
  implementation notes and transient state. Verified cleanup belongs in work-spec implementation.
- Promotion timing: approval may publish an intended contract alongside a confirmed known-difference
  note while its fix is pending; this qualifies P6's ship-before-promotion rule. Unnoted future behavior
  still waits for shipment. Notes persist until the affected implementation is verified.
- Adjacent findings: sharpen authoring's existing scope only if needed. Use Discussion, Assumptions
  and TODOs, or Out of scope; existing authorization governs editing adjacent artifacts. No new section
  or live-design keyboard policy.
- Links: requirement and Discussion citations in chat use inline links to the exact draft/canonical
  target; stored requirements documents use reference-style links with definitions at the bottom,
  relative paths, and real anchors. Definition headings/IDs and recorded tool output are not citations.
  Discussion item links use supported explicit anchors or topic anchors with item context, and verified
  file/line links when appropriate. Promotion rebases destinations, including dependencies outside a
  partial package; keep C7 as the completion identity so history remains interpretable.
- Migration: the release document instructs upgrading agents to sweep existing catalogs/open packages, convert
  links, transfer draft-to-Discussion associations before removing `(D#)`, and verify destinations.
  Preserve prose, IDs, decisions, approval/completion state and verification history; surface ambiguity.
  Honor shared roots and existing upgrade approval. No historical promoted-package rewrite for style.
  Do not infer known differences or rewrite contracts from old bug reports during migration.

## Earlier open decisions (unimplemented ledger)

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

## Decisions — 2026-10-18 (product specs)

Supervisor decisions from the Offers retrospective, recorded in the SalesPro checkout at
`working-docs/requirements-process/planning.md` (ephemeral) with the format draft, fixtures and tool
beside it. They qualify the invariants above and are the standard for the next refinement pass.

- **Name.** Requirements become *product specs*: folders (`skai/product-specs/`,
  `proposed-product-specs/`), the four guides, four skills, README rows, the artifact tree above.
  *Requirement* stays as the name of the ID'd item. Done in one pass so files move once.
- **Shape.** The design-spec item shape, shared: sections, `###` items, numbered rules cited with
  dashes, tables keyed on their first column, glossary entries as headings, every term occurrence
  linked. One nesting level below a rule. Reason: tables and nested rules are how a product manager
  conveys enumerations (stages, fields, statuses) and related constraints; the flat paragraph form
  turned seven stages into nine requirements.
- **Tool.** One script beside the UI Map renderer: `validate`, `references`, `link-terms`, `render`,
  `render-request`. The validator is the enforcement of the shape; the renderer is how a human reads
  a package. Markdown stays the source.
- **Concept inventory** before app behavior; **Situations** section, optional.
- **Change requests** from any consumer, with optional drafts, triaged by authoring.
- **Reference sweep** on modify or retire.
- **Design justifications name screens, never drafts** (settled 2026-10-18, consistency pass): a
  change item's `Design` source names the screen or state by product name; it never links a
  change-page draft, which design promotion deletes.
- **Retired items stay in place.** Deleting uncited retired items at promotion was considered and
  declined for now.
- **Migration.** After the release lands, the tool's converter rewrites every existing catalog,
  the unpromoted design-specs baseline and open packages mechanically; the release document instructs it.
  The rename and migration entry in the release document spells out a **reviewed process**, beyond the standard
  migration activities (supervisor, 2026-10-18): convert, validate, render, supervisor review of the
  rendered catalog and of every open package's page before anything is committed, addendum rename
  with lookup-name compatibility, link and README verification, with the converter's run recorded
  as evidence.
- **Refinement order.** The shared shape guide and tool first, then product specs, then design
  specs, then one consistency pass; sequential because design specs cite product specs and a cold
  review needs a stable target.
- **Open:** the word budget after the rename and the shape move; whether the catalog guide keeps
  the judgment half of its layout section (topic-file sizing, index lines name questions, glossary
  as second index) or that also moves to the shared guide.

## Decisions — 2026-10-19 (change request triage)

Supervisor decisions after the catalog rework, where the agent proposed rejecting a request the
product owner had made. Shared by product specs, design specs and UI Map architecture.

1. **The supervisor rules; the agent applies.** A change request is read and decided by the
   supervisor, who tells the agent what to do with it ("incorporate 001", "reject 001, it belongs
   with the sync work"). The agent then applies that: for an incorporation the drafts and the
   change list, then `Incorporated`; otherwise the status and the supervisor's reason in
   `Reviewer Response`; then re-render. Until told, the agent leaves a `Proposed` request alone;
   it summarizes open requests when asked. `Proposed` keeps blocking promotion. The agent never
   rejects or supersedes on its own, and does not raise Discussion items to drive the ruling.
2. **A change request exists only against an open package.** It is the trace of someone other than
   the package's author asking for its drafts to change, without editing them. With no package
   open for the subject, whoever finds the defect opens a change package through authoring; the
   supervisor reviews it like any other. There is no request against the catalog, and supervisor
   input during authoring is a decision, never a request.
3. **A request carries drafts (supervisor, 2026-10-19).** Filing a request is authoring in
   miniature: the agent drafts the requested changes, in the spec shape, from the supervisor's
   input, and its page diffs them against the package's drafts like the package's own page. Where
   the input does not settle what the drafts should say, the agent asks at the filing workflow's
   own Discussion gate; a request goes out without drafts only when the supervisor, asked, agrees
   the drafts cannot be written from what they know. Observed 2026-10-19: a request filed from a
   fully stated model as a bare list, because the guide called drafts "optional".

## Decisions — 2026-10-20 (known gaps: format definitions)

From the known-gaps planning (SwiftKickMobile/skai#82). These are the house-style definitions in
`process-flow.md` § Structured discussion items; the workflow that uses them is the shared
[`known-gaps.md`](../../Guides/Core/known-gaps.md) guide (its own design spec:
[`known-gaps-design.md`](known-gaps-design.md)). Propagation into the family guides and the
promotion readiness rule are a later slice and amend this spec again.

1. **A gap item stays open with a Gap line.** An item that cannot be resolved because something
   outside the work is not yet known carries `- **Gap** <placeholder: what stands where until it is
   answered, or "no placeholder; waiting on <what>">` as its last sub-bullet and keeps its box unchecked
   (supervisor, 2026-10-20: a gap without a placeholder says so in the same field; free text, no
   new field). An open gap item does not count
   toward the discussion-phase blocked gate: with only gap items open the planned gate is emitted,
   naming them (`⏳ GATE: Next: Discussion complete; <n> open gaps carried. Say "next" …`). It
   does block promotion (zero open gaps), which the later slice applies to the promotion guides.
2. **A gap resolves like any item** — box checked, `- **Decision**` appended, and the Decision says
   which of the three it was: answered, placeholder adopted, or omitted. Transitions (added
   2026-10-20 after a supervisor finding; the first text listed states only): open → decided
   (Decision appended, log `decided`); open → gap (Gap line, log `gap`); gap → decided (Gap line
   removed, Decision says answered / adopted / omitted, log `decided`); decided → decided (the
   decision changes: Decision line replaced, log `decided` again); decided → open (withdrawn with
   no replacement: Decision line removed, box unchecked, log `reopened`). A gap's placeholder
   changing while it stays a gap is not a state change and logs nothing.
3. **`## Decision Log`, one per artifact, append-only.** The last `##` section before any
   trailing link definitions. One line per state change, naming the item: `- <ID> <state> —
   <one line>` with state one of `decided`, `gap`, `reopened`. Order is the history; no dates. An
   item carries only its current state: one Decision line at most, removed when the item is
   reopened (the log keeps what it said). Every Discussion-based artifact has the section, empty
   when nothing has changed state. The tool checks that the last log entry for each item agrees
   with the item (checked ⇔ `decided`; Gap line ⇔ `gap`; otherwise none or `reopened`).
4. **One pointer sentence, inlined.** Every Discussion-phase guide carries, next to its Discussion
   rules, the sentence process-flow gives verbatim, naming both triggers (a gap on an input the
   agent relies on; an item of its own that cannot be resolved because something outside the work
   is not yet known) and sending the agent to the known-gaps guide. The sanity scan checks for it.
5. **Why house style, not the shared guide.** The Gap line and the log are written every time an
   item changes state, in every Discussion workflow, so they are inlined with the schema; the gap
   workflow is conditional and lives in the shared guide (two-bucket rule, supervisor 2026-10-20).

Size cap for `process-flow.md`: **21,200 bytes** (supervisor, 2026-10-20; was 21,000 after slice 1), set
just under the compressed size after slice 2's additions (21,220). The baseline itself has never been
compressed; SwiftKickMobile/skai#89 is the pass that will reset it.

## Decisions — 2026-10-20 (known gaps: propagation)

Slice 2 of the known-gaps effort. The format definitions above are inlined into every
Discussion-phase guide; these are the rules that go beyond the format.

1. **Promotion readiness requires zero open gaps.** Readiness item 1 ("every Discussion item is
   resolved") now says gap items included: an open gap fails readiness, is recorded in Evidence,
   and the package returns to authoring to resolve it per the known-gaps guide. Promotion never
   resolves a gap. The same rule sits before the UI Map official write.
2. **Authoring's gate carries gaps.** The Discussion blocked gate counts non-gap items only; the
   planned gate names the open gaps carried (`Discussion complete<; N open gaps carried>`). The
   marker lifecycle's "by then they are already clear" gains the gap exception.
3. **The tool enforces the log.** `check-changes` fails when the authoring artifact's
   `## Decision Log` disagrees with its Discussion (section missing once items exist, not last,
   malformed entry, last entry not matching the item's state, two Decision lines, checked with a Gap
   line, a change entry citing a `D#` the Discussion lacks; an entry whose item was removed is allowed); `render` shows gap items with state "gap", counts gaps on the
   card, and renders the log after the Discussion. The artifact reference says so.
4. **Caps (supervisor, 2026-10-20).** Set a little under each file's compressed size, so the next
   round earns its bytes (not old cap plus addition): `product-specs-authoring.md` 21,300;
   `product-specs-artifacts.md` 6,800; `product-specs-promotion.md` 17,000 (unchanged);
   `spec-file-shape.md` 8,200 (unchanged; recorded in `spec-format-design.md`). These supersede the
   2026-10-18 table rows for those files.
5. **Lean Discussion, from UI Map (supervisor, 2026-10-20).** A resolved item stays while
   something current cites it (a change item's justification, a map change, a known-difference
   note) or it still explains the current drafts; otherwise it is removed. The Decision Log keeps
   its record, so an entry may outlive its item; the tool tolerates that and instead checks that
   every `D#` a change entry cites is in the Discussion. The earlier rule that the original stays
   visible forever is withdrawn.

## Decisions — 2026-10-20 (known gaps: spec files)

Slice 3. The spec-file representation of a gap is `spec-format-design.md` decision 21; these are the
workflow consequences.

1. **Authoring marks the placeholder.** *Draft the requirement anyway* (product specs) and
   *Drafting* (design specs) say the placeholder is marked with the shape guide's gap footnote
   naming the item. Nothing else in the authoring guides changes: the footnote is the shape's.
2. **The tool pairs footnotes and items (G12, supervisor, 2026-10-20).** `check-changes` fails when
   a draft's gap footnote names a `D#` that is not an open gap item, or when an open gap item has
   no footnote in any draft (a marker-less note counts). That is what makes zero open gaps at
   promotion mean the drafts carry no placeholder.
3. **The page lists gaps.** The artifact reference says the page lists the drafts' gap footnotes,
   each linked to its item, beside the gap-item marks and the log.
4. **Caps** for `product-specs-authoring.md` (21,300) and `product-specs-artifacts.md` (6,800) held
   (supervisor, 2026-10-20): the one-sentence additions were compressed and the old caps forced the
   trims.

## Size Budgets — 2026-10-18

Set by the supervisor from four efficiency reviews (SalesPro checkout, `working-docs/requirements-process/reviews/`), as today's size less measured obsolete content, less the reviewed trim on what remains, plus known growth. Whole-file bytes by `wc -c`, managed header and addendum footer included. They bind every repair per the refinement guide's size-budget rule.

These replace the 11,000-word budget above for the product spec guides.

| Target | File | Cap |
| --- | --- | --- |
| 2. Content | product-specs-catalog.md | 10,500 |
| 2. Content | product-specs-artifacts.md | 6,500 |
| 3. Authoring | product-specs-authoring.md | 20,500 (compact Advance intent block adopted) |
| 3. Authoring | product-specs-baseline.md | 1,700 |
| 3. Authoring | skai-product-specs-authoring skill | 450 |
| 4. Promotion | product-specs-promotion.md | 17,000 |
| 4. Promotion | skai-product-specs-promotion skill | 450 |

Group caps across both spec types and the design process guides: content 37,000; authoring 54,900 (raised 2026-10-18 with design-specs-authoring); promotion 42,700.

**Rendered page, prominently linked (supervisor, 2026-10-18).** The authoring artifact and the promotion artifact each link the package's rendered review page (`product-specs-review.html`) at the top, directly under the title, before Goal or Inputs; a change request's `request.md` links `request-review.html` the same way. The link is the first thing a reviewer sees.

**Live render (supervisor, 2026-10-18).** The rendered page is the primary way the supervisor views a change package while it is being iterated on. Any time the package materially changes — a draft edited, a discussion item resolved, a change item added, a request triaged — the agent validates and re-renders before anything else, in every workflow that writes a package. The gate and promotion renders are not the only ones; they are the last of many. Validation and rendering take milliseconds, so there is no cost argument for deferring them.

## Adopts — 2026-10-21 (working docs placement)

Working documents serving a package live in its `working-docs/` folder and archive with it at promotion (`product-specs-artifacts.md` layout, `product-specs-promotion.md` § Archive the package; caps held; skai#92, `Guides/Core/working-doc-conventions.md`); build and test output goes to the scratch root, never the package.
