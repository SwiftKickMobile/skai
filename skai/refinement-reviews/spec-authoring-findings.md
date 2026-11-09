# Spec Authoring Guides — Findings Log

Target 3: `Guides/ProductSpecs/product-specs-authoring.md`, `product-specs-baseline.md`, `Guides/DesignSpecs/design-specs-authoring.md`, `Guides/Design/design-authoring.md` and the three authoring skill wrappers, refined together for fidelity and parallel structure. Standards: [`product-specs-system-design.md`](product-specs-system-design.md), [`design-specs-design.md`](design-specs-design.md), [`design-process-design.md`](design-process-design.md), [`spec-format-design.md`](spec-format-design.md). Refiner-facing cross-pass record: never shown to a cold reviewer; settled decisions go to the prompt's settled-dispositions slot instead. One row per finding per pass; appended at each round's closure.

## Seeded from earlier passes (authoring-relevant rows)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-27 p1 (req) | Redundant `auto` milestone; hard-gate variant for the `shared` announcement | closed; hard gate declined | Process weight not justified; do not re-raise |
| 2026-08-29 r6 (req) | `## Artifact maintenance` read the `C1`–`C5` pass as every-response | closed | Attached to the advancing planned gate only; `auto` bypasses the gate, not the pass |
| 2026-08-29 r6 (req) | A package seeded by another workflow is never completed to the skeleton | closed | Reopening completes Goal/Inputs/Mode |
| 2026-08-30 r8 (req) | Modify-vs-retire had no pointer where the type is chosen | closed | Pointer at the point of use; the rule has one home in the catalog guide |
| 2026-08-30 r10 (req) | The backfill rhythm and the blocked-gate mechanic could not both be obeyed | closed | The gate comes once, after the last subject in scope |
| 2026-08-30 r10 (req) | *Working a scoped change* readable as editing the catalog file | closed | Copy out of the catalog, edit the copy, never the catalog file |
| 2026-08-30 r11 (req) | `## Assumptions and TODOs` is an unguarded bypass around the Discussion gate | closed | The test stated at *What earns an item* |
| 2026-08-30 r11 (req) | A package whose only change is an index line has no `Type` to ride on | logged | Stranded, not broken; it rides in `Touches` |
| 2026-08-30 r14 (req) | The change-request path is taught in three places and worked in none | logged | Fields enumerated in the artifacts guide; off-normal path |
| 2026-08-30 r15 (req) | Three sites decided how a response ends with zero items seeded | closed | The drafting response ends with the blocked or planned gate; no separate "draft is ready" gate |
| 2026-08-30 r16 (req) | Authoring's Discussion gate does not specify what the supervisor is shown | logged | Presentation quality; the artifact (now the rendered page) is the review surface |
| 2026-08-30 r17 (req) | The `Incorporated` precondition has two verbatim homes (authoring, artifacts) | logged | Both defensible; edit together if either changes |
| 2026-08-30 r18 (req) | Authoring reopens a package by judgment where promotion blocks on the same ambiguity | open — supervisor | Adds a stop condition; in the unimplemented ledger; do not re-raise |
| 2026-08-30 r18 (req) | `## Assumptions and TODOs` an ungated second parking lot | logged | No proportionate fix; the *What earns an item* test governs |
| 2026-09-28 r1–r3 (baseline) | Delegated authoring; cited-files-first invariant; product paragraph first from a non-code source | closed (rulings) | Authoring may not be delegated (P10); invariant stays in the baseline guide; a delegated session reports to its spawning supervisor |
| 2026-09-28 r3 (baseline) | The citation invariant is general but read only in Baseline mode | logged (ruling) | Relocation priced out; stays in the baseline guide |
| 2026-09-28 r3 (baseline) | Spec P6 (per file) vs Workflow step 2 ("catalog starts empty") on the Baseline trigger | logged | Standard-level; the guide keys mode per file |
| 2026-10-05 release (req) | Location rebasing creates false diffs; promotion timing keys on shipping; known-difference notes | closed | Compare by prose and resolved targets; timing keyed to shipping in both guides |
| 2026-10-14 p1 (ds) | Audit entry; evidence line per check before the gate; drawing items open until seen | closed | Audit paragraph in Initiation; `## Verification`; gate note |
| 2026-10-14 p1 r4 (ds) | Reopen's "copy from canon" could replace an existing draft | closed | Reuse existing drafts; initialize missing ones from canon |
| 2026-10-14 p1 r14 (ds) | Universal drafting constraints under a baseline-only heading | closed | Relocated into Drafting |
| 2026-10-15 backfill (ds) | Required delegated cold check before the Discussion gate | rejected (supervisor) | Review mechanics are not baked into the guide; do not re-raise |
| 2026-10-12 r1–r3 (design) | Drawing scope; visually-judged items; feedback transitions in one place; reopen removes Design Changes; backfill items | closed | Mockups owns the feedback sequence; trial decisions; Design Changes rewritten after the next approval |
| 2026-10-12 r1 (design) | Intervening production changes on reopen unspecified | logged | No occurrence; the generic blocked gate covers it |
| 2026-10-12 r2 (design) | A decision discovered while drawing has only the generic blocked gate | logged | No occurrence; the generic gate is a safe stop |
| 2026-10-12 post (design) | Per-tool skills replaced by tool-agnostic skills; the guide loads the tool guide | closed (ruling) | Skills tool-agnostic; Purpose names the tool guide |
| 2026-10-18 r1 (content) | Change items carry no inline text; request folders `change-requests/<nnn>/` filed by any consumer | settled (target 2) | Dependents repaired here in the pre-review pass |

## Target 3 passes

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-18 pre-review | Three caps unmet after the efficiency review's trims (requirements-authoring +540, design-specs-authoring +2,011, design-authoring +39) | ruling | Compact Advance intent variant in requirements-authoring (siblings' form); rule-free trims; design-specs-authoring cap provisionally 17,000, group 54,900 |
| 2026-10-18 pre-review | `## Verification` in the product-spec authoring artifact (sweep and pre-gate evidence) | ruling | Approved; requirements-system-design § Authoring artifact lists it |
| 2026-10-18 pre-review | Design-spec change list maintained live (the shared live-render rule takes justifications from it) | ruling | Approved; design-specs-design 9 amended |
| 2026-10-18 pre-review | Concept inventory confirmed as one `[Proposal]` item under the standing blocked gate; design packages list filed requests under Assumptions and TODOs until triaged | decided in pass, upheld | No new gate; target 4 reads the list |
| 2026-10-18 r1 | F1 requirements-authoring *Working a scoped change* copied canon unconditionally, overwriting existing drafts on reopen (design-specs sibling says reuse drafts) | closed | "Reuse an existing draft; initialize a missing draft by copying the catalog file"; scoped change points at it |
| 2026-10-18 r1 | F2 the reference sweep sent a stale citation in any artifact to "a change request against it" | closed | Per-citation dispositions: catalog → draft the file; design specs → change request; work spec or other package → named in the sweep for its owner |
| 2026-10-18 r1 | F3 the review page renders Discussion items as a table of titles; the supervisor cannot resolve an item from the page alone | routed — supervisor (spec-format 12) / tool pass | The standard and the docstring specify a table; acceptance check 4 asks for approval from the page alone |
| 2026-10-18 r1 | F4 `check-changes` matches rule entries to the parent item | routed to the tool pass (re-raise of target 2 r1 F2) | Docstring: "an entry about a rule … names an item that shows as modified" |
| 2026-10-18 r1 | Open: design-process live-render sentence with no design-package render artifact | open question | Standard-level; the design guide invents no render |
| 2026-10-18 r1 | Round score | — | Series A r1 3.75 (2 divergent, 0 noise, 2 routed); sizes 20,102 / 1,698 / 16,998 / 14,360 / 443 / 430 / 549 = 54,580 of 54,900 |
| 2026-10-18 r2 | F1 promotion's worked `C1` bracket greps `^## ` while items are `###`; authoring cites that example | routed to target 4 | Promotion guide read-only here |
| 2026-10-18 r2 | F2 the sweep trigger omitted glossary entries (P8; human's delta) | closed | "Before modifying or retiring an ID or a glossary entry, run `references`"; the inventory points at the sweep |
| 2026-10-18 r2 | F3 design-specs sweep lacked the ownership boundary the product spec sibling states (r1 F2 not swept) | closed | Dispositions parallel in both guides; consolidation trigger counted once |
| 2026-10-18 r2 | F4 design: "The Decision names the request" assumed an item; feedback and trace-pass requests have none | closed | Any phase; listed under Assumptions and TODOs; a Decision names it when one exists |
| 2026-10-18 r2 | F5 `validate` blocks cross-file conflicts confined to untouched canonical files | routed to the tool pass | `spec-tool.py:573` "whole-projection checks: always block" vs spec-format 8 |
| 2026-10-18 r2 | Open: standards still print the 53,550 group cap | open question | Standard hygiene |
| 2026-10-18 r2 | Round score | — | Series A r2 5.625 (3 divergent, 0 noise, 2 routed); sizes 20,255 / 1,698 / 17,000 / 14,396 / 443 / 430 / 549 = 54,771 of 54,900 |
| 2026-10-18 r3 | F1 design-specs sweep omitted the product catalog from its roots and routed a product-spec citation to "named for its owner" instead of a change request (my r2 repair) | closed | Roots and dispositions mirrored from requirements-authoring; consolidation trigger fired twice → structured tier (invariants I1–I4, ownership table, rule impact maps in the working doc) |
| 2026-10-18 r3 | F2 "New specs require the root index, glossary and all three folder indexes" read per screen | closed | "A new specs root needs …", parallel to "A new catalog needs" |
| 2026-10-18 r3 | Round score | — | Series A r3 7.5 (2 divergent, 0 noise); sizes 20,255 / 1,698 /    16990 / 14,396 / 443 / 430 / 549 |
| 2026-10-18 r4 | F1 the renderer resolves Discussion and justification links against the last draft's definitions, not the authoring artifact's | routed to the tool pass | `set_resolver(new.linkdefs, …)` per draft; Discussion rendered after without restoring |
| 2026-10-18 r4 | F2 design-specs Initiation step 4 not conditioned on Baseline in the sentence | logged | Single observation; heading carries the condition; on recurrence "if Baseline, read …" |
| 2026-10-18 r4 | Open: no-delegated-authoring rule only in the baseline guide; `## Situations` not rendered (spec-format 12 omits it) | open questions | Standard-level, for the supervisor |
| 2026-10-18 r4 | No live findings in the binding target | closed — clean fresh round | Stop rule (a); series A r1 3.75 → r2 5.625 → r3 7.5 → r4 0; sizes 59,955 → 54,761 (caps 20,500 / 1,700 / 17,000 / 14,400 / 450 / 450 / 550; group 54,900); tool md5 38a60dcc at close |

Pass converged by a clean round: round 4 (series A) raised no finding in the seven files. Net size change 59,955 → 54,761 (−5,194): 20,255 / 1,698 / 16,990 / 14,396 / 443 / 430 / 549. Consolidation trigger fired twice (r1 F2 → r2 F3; r2 B → r3 F1); the structured tier (invariants I1–I4, ownership table, rule impact maps) applied from round 3. Routed during this pass: Discussion bodies on the page (r1 F3, now spec-format 12), rule-level `check-changes` (r1 F4, re-raise), promotion's `C1` example (r2 F1, target 4), untouched-canonical cross-file conflicts (r2 F5), authoring link context in the renderer (r4 F1). Logged, not codified: baseline dispatch conditioning (r4 F2). Open for the supervisor: the delegation rule's placement; `## Situations` on the rendered page.
| 2026-10-18 r4 | Pass closed by the supervisor | closed | Target 3 closed at 54,761 bytes after clean round 4; r4 F1 and Situations rendering (spec-format 12) with the tool pass; the no-delegated-authoring sentence to the consistency pass; no further rounds |
