# Known Gaps — Refinement Working Document

Slice 1 of the known-gaps effort (`working-docs/requirements-process/known-gaps-planning.md` in the SalesPro checkout). Target: `Guides/Core/known-gaps.md` (new) plus the changed § Structured discussion items of `Guides/Core/process-flow.md`. Design specs: `skai/refinement-reviews/known-gaps-design.md`; `product-specs-system-design.md` § Decisions — 2026-10-20.

## Drafts — 2026-10-20

- `Guides/Core/known-gaps.md` first draft: 4,334 bytes.
- `Guides/Core/process-flow.md`: 19,424 → 21,313 bytes (addition 1,889). `internal/maintenance/gated-workflows.md` Discussion-phase list and `guide-authoring.md` sanity scan kept in step. Manifest entry `guide.known-gaps` added. README rows deferred to slice 2 (no guide points at the new guide until the pointer is propagated; a README row saying a skill reads it would be false now).

### Sanity scan after the drafts (guide-authoring § Sanity scan)

- Managed header on the new guide; `Managed-Updated-At` 2026-10-20 on both edited managed files: visual review of the headers — ok.
- `## Gates` / `## Advance intent`: not applicable, known-gaps is a reference, not gated (no `⏳ GATE:` lines: `grep GATE Guides/Core/known-gaps.md` — 0 occurrences).
- "human" for supervisor: `grep -n '\bhuman\b' Guides/Core/known-gaps.md` — 0 occurrences.
- Runtime reference to process-flow: `grep -n process-flow.md Guides/Core/known-gaps.md` — 0 occurrences.
- Skill invocation in the new guide: `grep -n 'invoke\|load ' Guides/Core/known-gaps.md` — 0 occurrences.
- Marker conventions: the new guide defines no artifact and carries no `- [ ]` items; process-flow's new example items carry IDs (`D02`) — visual review of § Example.
- Discussion-phase gate behavior in process-flow: changed deliberately (gap items excluded from the blocked gate; planned gate names carried gaps) per the design amendment item 1 — recorded, not a defect.
- Flow reflection for process-flow (a house-style reference, not an executing workflow): the gate cycle still has exactly two states; a reader with only gap items open gets the planned gate and knows promotion will block — no issues found in simulation.

## Compression review — 2026-10-20

Astra (`gpt-6-astra`, read-only), prompt and output in the scratchpad `compress/`. Rewrites applied with one exception: its guide rule 3 sent the agent to `process-flow.md` at runtime, replaced with "the formats your workflow inlines" (house style: process-flow is never a runtime read). Its flags were real and are in: no owner field (requirement 8), LumenNotes named (9), the tool check and the sanity-scan check in process-flow (amendment items 3 and 4).

| File | Before | After | Note |
|---|---|---|---|
| `Guides/Core/known-gaps.md` | 4,334 | 3,232 | body 2,672; header, cue and footer ≈ 560 |
| `Guides/Core/process-flow.md` | 21,313 | 20,906 | addition 1,482 over the pre-slice 19,424 |

Caps set by the supervisor: known-gaps 3,400; process-flow 21,000 on an unreviewed baseline (skai#89 filed for the baseline pass).

## Round 1 — 2026-10-20

Reviewer: Astra (`gpt-6-astra`, read-only). Prompt: template block verbatim, slots filled; Legacy, Observed failures, Proposed edits and Report charter sections deleted (scratchpad `review-r1/`).

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 pointer sentence links `known-gaps.md` relative to Core; copied verbatim into ProductSpecs/Design/Spec it dangles (verified by the reviewer: resolves only from Core) | accept | amendment item 4; process-flow § Sub-bullet labels | destination `../Core/known-gaps.md` (resolves from every Guides subdirectory, Core included); +8 bytes | both triggers; verbatim reuse; formats inlined / workflow shared; no runtime route through process-flow |
| F2 resolving a gap leaves **Gap** beside **Decision** on a checked item, contradicting the current-state invariant (checked ⇔ decided) | accept | amendment items 1–3; process-flow § Resolution step 2; known-gaps rule 4 | step 2: "For a gap, remove its **Gap** line and say which …"; guide rule 4 "remove the artifact's marker" so the two markers are distinct; +39 bytes / +11 bytes | append-only log; original item text stays; three outcomes; when gaps block |
| F3 gate subsection's closing summary still says the planned gate comes "when the draft produced zero items", not covering the gap-only case | log only (reviewer's own triage; the operative rule two lines above is explicit) | process-flow § Discussion-phase gate behavior | none now | — |

Open question (reported on its own, not scored): how an item records a gap that has no placeholder — the **Gap** line's payload is described as the placeholder. Raised to the supervisor.

### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 2 | 0 | 2 | 0 | 1 |

> F1 divergent · normal · verified = 5 · F2 divergent · off-normal · speculative = 5 × 0.75 × 0.5 = 1.875 · F3 log only, noise · open question on no-placeholder gaps, neither

### Repairs

- Cluster 1 (F1): pointer destination. Self-check: template and sanity scan say "copy from process-flow" and grep `known-gaps.md`, both still true; no adjacent text names the old destination (`grep -n known-gaps.md` across Guides and internal/maintenance). Nothing moved or weakened.
- Cluster 2 (F2): Resolution step 2 and guide rule 4. Self-check: the Decision Log paragraph's invariant now matches the recipe; the guide's rule 3 ("unchecked item with a Gap line") is unchanged and still agrees; "artifact's marker" in rule 4 pairs with rule 3's artifact markers. Nothing moved or weakened.
- Sizes after repairs: known-gaps 3,243 / 3,400; process-flow 20,953 / 21,000.

### Closure

- F1 closed — process-flow line 256 now links `../Core/known-gaps.md`; verified by resolving the path from `Guides/ProductSpecs/`, `Guides/Design/`, `Guides/Spec/` and `Guides/Core/` (all exist).
- F2 closed — step 2 removes the Gap line on resolution; the example's D02, resolved, would carry Decision only.
- F3 logged — rationale: the operative rule is explicit and the summary is pre-existing prose; qualifying it adds weight for a case the rule already covers.

## Round 2 — 2026-10-20

Same prompt with the recently-revised slot updated and F3's disposition added to settled dispositions (scratchpad `review-r2/`).

### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the **Gap** field's description names only a placeholder; a gap with no placeholder has no stated representation (the r1 open question, restated) | log only (reviewer's own triage; recurrence 2 — supervisor asked whether to sharpen the field description) | amendment item 1; process-flow § Sub-bullet labels; known-gaps rules 2, 5 | if ruled: sharpen the field description to allow "none; waiting on <what>"; free text, no new field | a "no placeholder" statement is never permission to build; rule 5's three options stand |

Open question (not scored): a placeholder revised while the item stays `gap` produces no log entry, since the log records state changes only — consistent with decided item 7; noted for the audit-scope discussion, no change.

### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 2 | 0 | 2 | 0 | 1 |
| r2 | 0 | 0 | 0 | 0 | 0 | 1 |

> F1 log only (restates r1's open question), noise · placeholder-revision logging, open question, neither

### Closure

- F1 logged — rationale: the operator has the workflow's gate as the escalation route and no strand has occurred; sharpening the field is a one-line change awaiting the supervisor's ruling, not a review repair.
- Terminal round: no new live findings in the binding target (stop rule (a)). Sizes unchanged: known-gaps 3,243 / 3,400; process-flow 20,953 / 21,000.

## Maintenance retro — 2026-10-20

Maintenance retro: DONE

1. Inventory: new Core reference guide `known-gaps.md`; Discussion-schema house-style additions in `process-flow.md` mirrored in the gated-workflows template and the sanity scan; two design specs; manifest entry. Host-install-visible (new managed guide asset; managed content change in process-flow).
2. Bookkeeping: `Releases/unreleased.md` entry (two bullets, migration: none) and `CHANGELOG.md` Unreleased line present and agree — `grep -n "Known gaps" CHANGELOG.md`, `grep -c known-gaps Releases/unreleased.md` → 1 each. Manifest has `guide.known-gaps` with an existing `sourcePath`. `Managed-Updated-At` 2026-10-20 on both managed files edited (`git status --short`; headers read). README: no change — a row claiming a skill reads the guide would be false until slice 2 propagates the pointer; recorded as a slice 2 item. `internal/maintain-skai.md`: no new invariant introduced.
3. Integration doc: untouched.
4. Installer: untouched.
5. Consistency: stale section name `§ Gaps` — `grep -rn "§ Gaps" Guides internal` → 0 occurrences. New file referenced exists at the linked path from every Guides subdirectory (shell test, 4 ok). Terminology drift (`Next Command`, `human`) in the new guide → 0 occurrences each. New guide has the managed header and addendum footer (visual). Not a gated workflow, so no `## Gates` section (0 `⏳ GATE:` lines). Marker conventions: no `- [ ]` items in the new guide; process-flow's example items carry IDs. Change-package verification: not applicable (no package workflow changed). Addendum contract: entry cue and footer copy the boilerplate with the name `known-gaps` (visual diff against `guide-addenda.md`).
6. Process reflection: (a) the draft-then-cap compression review worked and belongs in the refinement guide as standard procedure for new or added guide content — to be filed as a skai issue on the supervisor's go (recorded in the planning doc); (b) my first drafts dropped two inventory items the compression reviewer caught — a checklist pass against the design spec's numbered requirements before any review would have caught it; suggest adding "check the draft against the inventory item by item" to the draft-then-cap procedure when it is written up.

Maintenance retro complete; no misses found. Follow-ups: README rows with slice 2; the no-placeholder Gap wording awaits the supervisor; the refinement-guide procedure issue awaits the supervisor's go.

## Round 3 — 2026-10-20

Commissioned over the final text after the supervisor's no-placeholder ruling (scratchpad `review-r3/`). No findings; no open questions rising to a defect. Reviewer verified the sanity-scan check exists and that the Decision Log tool check is not implemented (deferred to slice 2, as scoped).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 2 | 0 | 2 | 0 | 1 |
| r2 | 0 | 0 | 0 | 0 | 0 | 1 |
| r3 | 0 | 0 | 0 | 0 | 0 | 0 |

> r3: nothing scored, nothing logged — convergence by clean round over the final text (stop rule (a)). Sizes: known-gaps 3,243 / 3,400; process-flow 20,983 / 21,000.

## Slice 2 — Propagation — 2026-10-20

Target: the family guides (see `slice-affected-documents.md` rows marked 2). Done so far: eleven guides edited (product specs, design specs and design authoring; UI Map implementation; the four artifact references; the three promotion guides), `spec-file-shape.md` command rows, README Gaps rows, `spec-tool.py` (Decision Log check in `check-changes`; gap state, gap count and the log on the page; docstring), fixtures and their README, release entries, design-spec amendments. Waiting on the supervisor: work spec creation, work spec implementation, UI Map architecture (three design conflicts).

### Sanity scan after the guide edits

- `Managed-Updated-At` 2026-10-20 on every edited managed file (`git status --short`; headers read) — ok.
- Pointer sentence present and verbatim in the four edited Discussion-phase guides: `grep -c known-gaps.md` → 1 each (ui-map-implementation 2: pointer plus the official-write rule); byte-identical to process-flow's by eye.
- Runtime references to process-flow in the edited guides: `grep -rn process-flow.md ProductSpecs DesignSpecs Design UIMap/ui-map-implementation.md` → 0 occurrences.
- Link resolution: `../Core/known-gaps.md` exists from each edited guide's folder (shell test, 4 ok).
- Artifact skeletons: `## Decision Log` is the last skeleton line in product specs, design specs, design authoring and UI Map implementation — visual.
- Gate wording: blocked gate counts non-gap items; planned gate carries `<; N open gaps carried>` in all four — `grep -n "open gaps carried"` → 4 files.
- Marker lifecycle exception present in the three spec-family authoring guides — `grep -c "Gap items are the exception"` → 1 each.
- "human", "Next Command" in edited guides → 0 occurrences.

### Flow reflection (gated guides edited)

- Product specs authoring, normal: D1 decided, D2 a gap → response ends `⏳ GATE: Next: Discussion complete; 1 open gaps carried. Say "next" to advance to Completion.`; Completion runs; promotion's readiness item 1 then fails on D2 and returns the package to authoring. Blocked: D1 open → `Blocked: 1 open items in Discussion`. `auto`: bypasses the planned gate; D2 still blocks promotion. No issues found in simulation.
- Design specs authoring and design authoring: same cycle; design authoring's planned gate names the change-id as before. No issues found in simulation.
- UI Map implementation: Discussion with a gap item → planned gate names it; Code Changes written; Build runs; promotion step 1 blocks on the open gap and returns to its authoring. `auto` same. No issues found in simulation.
- Promotion guides: readiness item 1 fails on a gap → recorded in Evidence, blocked gate `readiness condition failed`, package returns to authoring; unchanged otherwise. No issues found in simulation.

### Tool verification

- Fixture suite run after the patch: `validate` both catalogs 0 issues; `check-changes` package and design-package 0 issues; broken-package product fails with its five log lines plus the existing change-list lines; broken-package design fails on the reminder line, the added index line and the missing log (3 issues); both packages render, the Offers page showing `1 open, 1 gap` on the card, a `gap` card for D3 and the Decision Log list.

### Rulings applied — 2026-10-20 (G06, G07, G09)

- G06: the changed-decision sentence added to process-flow's Resolution rule, the template, the four inlined copies and work spec creation; the slice 1 amendment now lists every transition; logged in the findings log against slice 1. Work spec creation's "never unchecked, supersede with a new D#" rule replaced by the house-style reopen; its skeleton, gates, Discussion rules and pointer done. Readiness (G08) still pending.
- G07 reversed / G09: house style follows UI Map's lean Discussion. Lean sentence in process-flow, the template, product specs, design specs, design, UI Map implementation and work spec creation; UI Map architecture gains the Gap label, pointer, skeleton line, gate wording and the one-Decision-line/log sentence, keeping its collapse rule. Tool: the orphan-entry check dropped (the log outlives its items); new check that every `D#` a change entry cites is in the Discussion. Fixture: `broken-package` R1 now cites `D9` (reported), its `D9` log entry tolerated; README row updated. Suite rerun: package and design-package 0 issues; broken product shows the five log/citation lines; render ok.
- Sanity scan after these edits: `Managed-Updated-At` 2026-10-20 on process-flow, ui-map-architecture, work-spec-creation (headers read); pointer present once in ui-map-architecture and work-spec-creation (`grep -c known-gaps.md` → 1 each); `grep -rn process-flow.md` in the edited family guides → 0; planned gate lines carry `<; N open gaps carried>` in ui-map-architecture and work-spec-creation (`grep -c "open gaps carried"` → 1 each).
- Flow reflection, UI Map architecture: baseline map with one gap item → blocked while non-gap items remain, then `Next: Discussion complete; 1 open gaps carried`; Map Changes written; implementation's promotion step 1 blocks on the gap. No issues found in simulation. Work spec creation: gap item carried past the Discussion gate; readiness for implementation planning pending G08.

### Compression review — slice 2 (Astra, 2026-10-20)

Rewrites applied for all sixteen files (scratchpad `compress2/out.md`), plus the pre-existing passages it flagged as contradicting carried gaps: UI Map architecture's gate explanation and Completeness line, UI Map implementation's blocked-gate reason, work spec creation's Advance intent rule, all now say non-gap; the retention rule aligned across copies (cited by current work or explaining the current drafts/map/changes); the artifact references no longer say every gap is a placeholder. Not taken: repeating the no-dates rule and last-entry mapping in each local copy (process-flow is canonical and the tool enforces it).

| File | Before | Drafted | Compressed |
|---|---|---|---|
| Guides/Core/process-flow.md | 20983 | 21324 |    21220 |
| Guides/Core/spec-file-shape.md | 8170 | 8261 |     8234 |
| Guides/ProductSpecs/product-specs-authoring.md | 20481 | 21561 |    21311 |
| Guides/ProductSpecs/product-specs-artifacts.md | 6484 | 6870 |     6839 |
| Guides/ProductSpecs/product-specs-promotion.md | 16988 | 17112 |    17052 |
| Guides/DesignSpecs/design-specs-authoring.md | 16967 | 18061 |    17811 |
| Guides/DesignSpecs/design-specs-artifacts.md | 4927 | 5030 |     4927 |
| Guides/DesignSpecs/design-specs-promotion.md | 12778 | 12882 |    12839 |
| Guides/Design/design-authoring.md | 14357 | 15419 |    15178 |
| Guides/Design/design-promotion.md | 11497 | 11621 |    11561 |
| Guides/UIMap/ui-map-architecture.md | 34970 | 35856 |    35712 |
| Guides/UIMap/ui-map-architecture-artifacts.md | 5225 | 5500 |     5502 |
| Guides/UIMap/ui-map-implementation.md | 50025 | 51130 |    50949 |
| Guides/UIMap/ui-map-implementation-artifacts.md | 6485 | 6617 |     6599 |
| Guides/Spec/work-spec-creation.md | 14595 | 15641 |    15364 |
| Guides/Spec/work-spec-implementation.md | 17068 | 17262 |    17262 |

### Round 1 — slice 2 — 2026-10-20 (commissioned)

Target: the fourteen family guides whole, process-flow § Structured discussion items, and the two command-table rows of spec-file-shape. Prompt: template block verbatim, slots filled; Legacy, Observed failures, Proposed edits and Report charter sections deleted (scratchpad `review2-r1/`). Findings log: `known-gaps-findings.md`, rows prefixed "slice 2". Series: new (different files and spec sections from slice 1's rounds).

### Round 1 — slice 2 — results

Reviewer: Astra, read-only; ran three in-memory checks of `check_decision_log` (verified the gap/decided/orphan cases).

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 reopening paragraphs still freeze decisions ("not removed, rewritten or renumbered") in product specs and design authoring (design specs imports it); work spec implementation's return path mandates "a new D#" | accept | format item 2, propagation item 5; product-specs-authoring § Reopening, design-authoring § Initiation, work-spec-implementation § Local fixes and design returns | preservation means stable IDs and untouched Concern/Options/Proposal, state per Resolution; the return path reopens or adds a D# | stable IDs; supervisor approval; append-only log; design authoring's removal of `## Design Changes` on a design-changing reopen |
| F2 planned-gate inventories ("every Discussion item is resolved") in the three spec-family authoring guides, and UI Map implementation's after-drafting line ("any `- [ ]` items remain … every item `- [x]`"), still count carried gaps | accept | propagation item 2; the `## Gates` planned-gate lists; ui-map-implementation § Organization and gate | non-gap in all four places | drafting completeness; the block on unresolved non-gap items; UI Map's block on open change requests |
| F3 the promotion guides return a gap-bearing package through readiness failure (blocked gate), while known-gaps rule 6, which they point at, says promotion's *planned* gate lists the gaps and "next" returns it; the standards disagree too (propagation item 1 vs known-gaps-design requirement 3 / decided item 4) | supervisor decision (standards contradiction) | known-gaps.md rule 6; known-gaps-design.md req. 3; plan decided item 4; the three readiness screens | reconcile the standards, then sharpen rule 6 to own only the zero-open-gaps condition and the return to authoring, leaving the gate form to the invoking workflow | zero open gaps before any canonical write; promotion never resolves a gap |

Open questions (not scored): a UI Map gap can hold a composed work spec run at the sibling's promotion boundary (consequence of the per-type promotion model, see skai#91); propagation item 3 listed "entry naming no item" as a failure while item 5 allows it — amendment wording fixed this round.

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s2-r1 | 6.3 | 3 | 0 | 3 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · normal · speculative = 2.5 · F3 divergent · off-normal · speculative = 1.875 · two open questions, neither

#### Repairs

- Cluster F2 (gate predicates): four edits. Self-check: `grep "every Discussion item\|every item \`- [x]\`"` without non-gap → 0 across the five Discussion guides; blocked-gate lines unchanged. Nothing moved or weakened.
- Cluster F1 (reopening): three edits. Self-check: `grep "never disturbed\|not removed, rewritten\|as a new \`D#\`"` → 0; design authoring's `## Design Changes` removal sentence intact; design specs inherits product specs' paragraph by reference. Nothing weakened: IDs still stable, originals still unrewritten.
- Size: every cap was set just under the compressed size, so every repair needed a compensating trim. Trims taken inside the additions first (shorter retention and artifact-reference wording), then in adjacent pre-existing readiness text (dropping "the authoring artifact's" before a section name, tightening the `Proposed` request clause, a reference's intro). Every file now at or under cap (table in scratchpad `review2-r1/sizes.md`); work spec set 32,598 / 32,600. Pointer sentence verbatim in all seven Discussion guides (grep, 1 each); no runtime reference to process-flow; fixture suite still 0 issues.
- F3: not repaired; awaiting the supervisor.

### Round 2 — slice 2 — 2026-10-20

Commissioned after G10 (blocked gate at promotion) landed in known-gaps rule 6 and its design spec.

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 operational stops still block on gap items: product specs' concept-inventory clause, design specs' gate note ("The gate stays blocked that long" for a requirements gap), design authoring's feedback branch ("(blocked)") | accept | propagation item 2 | non-gap in the concept clause; design specs: a placeholder lets a requirements-gap item ride as a gap, the gate stays blocked otherwise, and Requirements Gaps names the Gap line; design authoring: drop "(blocked)" | blockers for unusable inputs and ordinary unresolved decisions; a drawing still required before resolving an item that needs it |
| F2 design specs promotion's canonical-contract prerequisite sat before the readiness list and said to wait without returning the package, so an open gap never reached its return route | accept | propagation item 1 | prerequisite moved after the readiness list | a gap-free package citing an unpromoted requirement still waits |
| F3 artifact reference's compressed "checks they agree" read as a placeholder-vs-draft check the tool does not do (verified against `check_decision_log`) | accept | propagation item 3 | name the comparison (item state vs last log entry) and the page outputs | no new tool obligation |
| F4 work spec creation's "always appear" heading list omitted Decision Log beside "do not emit other empty boilerplate" | accept (reviewer said log-only; a deterministic document defect, one-word sharpen) | format item 3 | add Decision Log to the list | optional sections stay optional |

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s2-r1 | 6.3 | 3 | 0 | 3 | 0 | 0 |
| s2-r2 | 11.0 | 4 | 0 | 3 | 1 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · normal · speculative = 2.5 · F3 divergent · normal · verified = 5 · F4 cosmetic · normal · speculative = 1 · composition question (logged r1), neither. The rise is pre-existing text the additions contradict, reached by deeper simulation; none of the four is about round 1's repairs.

#### Repairs

- F1 (three edits), F2 (one move), F3 (one paragraph), F4 (one list), each paired with a trim in adjacent pre-existing text (concept-inventory wording, the Requirements Gaps outcome sentence, the design specs readiness intro, the artifact reference's re-render sentence, work spec creation's Implementation Design note). Self-check: `grep "stays blocked that long\|(blocked)\. On\|Prerequisite:"` → 0; pointer count unchanged; `known-gaps.md` linked once in the artifact reference. Every file at or under cap (`review2-r2/sizes.md`; design-specs-authoring needed four trims to land at 17,798).

### Round 3 — slice 2 — 2026-10-20

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 unconditional drafting instructions assume a proposal always exists: product specs' "an open item never leaves a hole … under the recommended reading"; work spec creation's "fill gaps with the agent's best proposal" (the word "gaps" now collides with the term) and a Question's mandatory provisional resolution; also found by sweep: design specs' "draft even uncertain items under the recommended reading" and work spec creation's "approve all proposals resolves every open item" | accept | format item 1 | draft under the recommended reading *or the gap's placeholder*; a gap with none leaves that behavior out; "unknowns" for "gaps"; a Question states its provisional resolution or carries a Gap line; approve-all resolves non-gap items | coherent first drafts; recommendations wherever defensible; a usable placeholder is built on without a decision |
| F2 revision branches bypass the lifecycle: UI Map architecture's "remove an unresolved item when the direction changes" would delete a gap without its omitted resolution; design authoring's "a change the supervisor asks for needs no item, the design is the record" and "a decision feedback has since changed is history" leave a changed decision's item stale | accept | format item 2 | UI Map: remove an unresolved *non-gap* item; a gap is resolved as omitted first per Resolution. Design: feedback changing an existing decision updates it through Resolution, old outcome in the log | UI Map's collapse rule; informal visual iteration earns no new item; append-only log |
| F3 UI Map's justification source taxonomy has no accurate label for an agent-proposed placeholder carried by an open gap (`Resolved decision` needs a resolved item; `Agent proposal` means it did not go through Discussion) | log only (reviewer's triage; the operator has the blocked route) | ui-map-architecture-artifacts § Map change items | if it recurs, sharpen `Agent proposal` to cover a provisional proposal | every map difference keeps a justification |

Sweep (defect class seen in three rounds: pre-existing item phrasing beside the additions): grep over the seven Discussion guides for `open item|unresolved|every item|any item|recommended reading|provisional|remove.*item` and classified each hit; the `auto`-never-bypasses-the-blocked-gate sentences and the blocked-gate lines are consistent (the blocked gate already counts non-gap items); UI Map implementation's "every item must still match" is about Map Changes items. Two extra hits repaired under F1 above.

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s2-r1 | 6.3 | 3 | 0 | 3 | 0 | 0 |
| s2-r2 | 11.0 | 4 | 0 | 3 | 1 | 0 |
| s2-r3 | 4.4 | 2 | 0 | 2 | 0 | 1 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875 · F3 log only, noise · composition question (logged r1), neither. None of the findings is about an earlier round's repair.

#### Repairs

- F1 (five edits across product specs, design specs, work spec creation) and F2 (UI Map architecture's loop; design authoring's What-earns-an-item and Mockups), each paired with trims in adjacent pre-existing text (the empty-Discussion sentences' "before they are finalized", a defect example, the UI Map loop's wording, work spec creation's Question and topic sentences). Self-check: the old phrasings are gone (`grep` → 0); no runtime reference to process-flow; every file at or under cap (`review2-r3/sizes.md`).

### Round 4 — slice 2 — 2026-10-20

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 design specs' requirements-gap wording (a round 2 repair) made a placeholder the condition for carrying the item ("unless a placeholder lets it ride as a gap"; "a Gap line if a placeholder exists"; "drafted under the recommended reading"), contradicting the guide's own bare-gap drafting rule and the `none; waiting on` form | accept | format item 1 | the gate note says "unless it carries a **Gap** line"; Requirements Gaps says "a **Gap** line to carry it, drafted per *Drafting*" | drawing-exists rule; change-request ownership; a bare upstream gap still gets the known-gaps ruling |
| F2 work spec creation's re-entry ("reopen the affected item or add the minimum new D#", a G06 repair) turns a replaced decision into a spurious reopen or a duplicate item | accept | format item 2 | re-entry changes an affected item through the transitions under *Discussion items*; a new `D#` only for a new decision | Implementation Design removed and rewritten; renewed review; genuine reopen on withdrawal |

Both findings are about earlier repairs (r2's F1 wording, G06's re-entry clause): the "watch who the findings are about" signal. Not the consolidation trigger (neither repair became a finding by the same mechanism twice), but noted: both came from writing a gap qualification into a specialized branch instead of pointing that branch at the guide's own general rule, which is what the repairs now do.

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s2-r1 | 6.3 | 3 | 0 | 3 | 0 | 0 |
| s2-r2 | 11.0 | 4 | 0 | 3 | 1 | 0 |
| s2-r3 | 4.4 | 2 | 0 | 2 | 0 | 1 |
| s2-r4 | 3.8 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875 · composition question (logged r1), neither.

#### Repairs

- F1 (two edits, both shorter than the text they replace) and F2 (one edit, paired with two trims in the same section). Self-check: the gate note and Requirements Gaps now agree with Drafting; work spec creation's re-entry defers to its Discussion-items transitions; `## Implementation Design` removal and rewrite intact. Sizes: design-specs-authoring and the work spec set under cap.

### Round 5 — slice 2 — 2026-10-20

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 UI Map architecture's Reopen bullet ("never replace `## Discussion` with the empty state on a reopened artifact") contradicts the lean retention rule (UI Map's own) and the empty-state rule when nothing still cites or explains | accept | propagation item 5 (G07/G09) | the bullet now retains items that still explain the map or that a map change item cites; the absolute prohibition is gone | cited items stay; stable IDs; append-only log; the collapse rule |

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s2-r1 | 6.3 | 3 | 0 | 3 | 0 | 0 |
| s2-r2 | 11.0 | 4 | 0 | 3 | 1 | 0 |
| s2-r3 | 4.4 | 2 | 0 | 2 | 0 | 1 |
| s2-r4 | 3.8 | 2 | 0 | 2 | 0 | 0 |
| s2-r5 | 1.9 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · composition question (logged r1), neither. Pre-existing text, not an earlier repair.

#### Repairs

- F1: one sentence in the Reopen bullet, shorter than before. Self-check: the empty-state rule (line 185) and the retention rule (line 291) now agree with the bullet; no other sentence forbids the empty state on reopen (`grep "empty state"`). Size under cap.

### Round 6 — slice 2 — 2026-10-20

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 artifact skeletons route "gaps needing no decision" (product specs, design specs, design) and "unresolved design gaps" (UI Map skeleton and completion step) into Assumptions and TODOs — a competing destination for a carried gap now that the word is a term | accept | format item 1; known-gaps-design req. 5 | "notes needing no decision"; "nonblocking design notes" / "design notes that do not block the map" | ordinary notes still allowed there; design's filed-request inventory stays there |

Sweep (the word "gap" in pre-existing text across the sixteen files): also repaired design authoring's trace-pass "a gap either way is a change request" (mismatch), UI Map implementation's "two kinds of gap" (finding), UI Map architecture's intro "any approved gap" (deviation), spec-file-shape's known-difference "an observed gap" (observed). Deliberately kept: design specs' "requirements gap" / § Requirements Gaps — it names the design-spec case of an upstream gap and now ties to the Gap line, and renaming it would ripple into `design-specs.md`, outside this target; the product specs catalog guide's "implementation gap" (known differences), outside this target.

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s2-r1 | 6.3 | 3 | 0 | 3 | 0 | 0 |
| s2-r2 | 11.0 | 4 | 0 | 3 | 1 | 0 |
| s2-r3 | 4.4 | 2 | 0 | 2 | 0 | 1 |
| s2-r4 | 3.8 | 2 | 0 | 2 | 0 | 0 |
| s2-r5 | 1.9 | 1 | 0 | 1 | 0 | 0 |
| s2-r6 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · composition question (logged r1), neither. Pre-existing text, not an earlier repair.

#### Repairs

- F1 (five skeleton/completion edits) plus the sweep's four, all shorter than or equal to the text replaced except the shape guide's, trimmed in the same sentence. Self-check: `grep -i gap` over the sixteen files now matches only the term's uses, "requirements gap", and the two kept cases; every file at or under cap (`review2-r6/sizes.md`).

### Round 7 — slice 2 — 2026-10-20

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 work spec implementation invokes UI Map implementation during its audit and consumes the plan "after it completes"; with a proposed map, UI Map completes only through promotion, which blocks on open gaps; so a UI Map gap stops work spec planning although gaps never block implementation (the composition tension logged since r1, now a finding) | supervisor decision (the reviewer's triage; the fix is a lifecycle rule) | G05 / slice 7; skai#91 | A — leave to slice 7, where G05 removes the sibling invocation that creates the dependency; no slice 2 change. B — an early-handoff rule now (bloat) | zero open gaps before the official write; UI Map owns promotion |

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s2-r1 | 6.3 | 3 | 0 | 3 | 0 | 0 |
| s2-r2 | 11.0 | 4 | 0 | 3 | 1 | 0 |
| s2-r3 | 4.4 | 2 | 0 | 2 | 0 | 1 |
| s2-r4 | 3.8 | 2 | 0 | 2 | 0 | 0 |
| s2-r5 | 1.9 | 1 | 0 | 1 | 0 | 0 |
| s2-r6 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| s2-r7 | 1.9 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875; no other findings. No new live findings outside F1, which is the unimplemented ledger presented for the supervisor's ruling (stop rule (b)); the ruling is G11 in the plan.

## Maintenance retro — slice 2 — 2026-10-20

Maintenance retro: DONE

1. Inventory: the gap format, pointer, Decision Log, gap-aware gates, lean Discussion and promotion readiness propagated into fourteen family guides; process-flow's Resolution rule and the spec-file-shape command rows; `spec-tool.py` (Decision Log check, `D#` citation check, gap rendering, log rendering); README Gaps rows; design-spec amendments; fixtures. Host-install-visible (managed guides and the tool change).
2. Bookkeeping: `Releases/unreleased.md` has the propagation entry with its re-runnable migration (seed `## Decision Log` into active artifacts) and the tool entry; `CHANGELOG.md` has the "part two" line; both agree (`grep`). Manifest unchanged (no asset added or moved; `json.load` ok). `Managed-Updated-At` 2026-10-20 on all seventeen modified managed guides (headers read). README: ten Gaps rows across the Discussion-based skills and the promotion skills (markdown links). `internal/maintain-skai.md`: no new invariant.
3. Integration doc: untouched. 4. Installer: untouched.
4. Consistency: stale section name / terminology drift — `grep -rn "§ Gaps\|Next Command" Guides internal` → 2 occurrences, both the checklists naming the term (false positives). Runtime references to process-flow in the family guides → 0. Pointer sentence verbatim in the seven Discussion guides plus its canonical line (`grep -rl` → 8 files). Template and sanity scan name `known-gaps` (1 and 2 hits). Gated guides: `## Gates` sections intact in all seven edited gated guides; planned-gate lines carry `<; N open gaps carried>`; blocked gates count non-gap items. Change-package verification (promotion readiness changed): a gap-bearing package fails readiness before any write, Evidence records it, the package returns to authoring, and coexistence / independent promotion / archival recovery are unchanged (readiness item 1 only). Fixture suite: validate both catalogs 0 issues; check-changes both packages 0 issues; broken product fails with its five log/citation lines; broken design 3 issues; render ok; `validate broken` fails as before.
5. Process reflection (seven rounds, scores 6.3 → 11.0 → 4.4 → 3.8 → 1.9 → 2.5 → 1.9, converged by ruling on the composition finding):
   - (a) Six of seven rounds found pre-existing sentences beside the additions that still assumed every item resolves or has a proposal. A propagation like this should start with a sweep of the phrases the new rule changes the meaning of (`open item`, `unresolved`, `every item`, `recommended reading`, the new term's own word), classified before round 1. Suggest adding that to the house-style procedure's third step in `gated-workflows.md` § Process-flow house style: "propagate, then sweep every guide for the phrases whose meaning the change alters."
   - (b) Caps set just under the compressed size meant every repair needed a compensating trim, and finding those trims cost more time than the repairs. That is the intended pressure, but the trims came from pre-existing text the review target excluded. Worth deciding whether a repair's trim may touch excluded text (it did here) or whether the cap should leave a repair allowance.
   - (c) Round 4's two findings were about my own earlier repairs; both came from writing a gap qualification into a specialized branch instead of pointing the branch at the guide's general rule. Suggest one line in the refinement guide's Repairing section: "a branch instruction defers to the general rule rather than restating it with a qualification."
   - (d) A guarded shell script that stops on a size failure must build the next round's prompt before the guard, or the launch step silently has nothing to run (it happened once; caught by checking the task output).

Maintenance retro complete; no misses found. Follow-ups: G11 is slice 7's; README rows for the promotion skills say "read when readiness finds an open gap", which is now accurate.

## Slice 3 — Gaps In Spec Files — 2026-10-20

Target: `Guides/Core/spec-file-shape.md` (the footnote element, example, validator list, command rows) plus one sentence each in product specs authoring, design specs authoring and the product specs artifact reference. Design specs: `spec-format-design.md` decision 21; `product-specs-system-design.md` § Decisions — 2026-10-20 (known gaps: spec files); design specs adopt line. Tool: `spec-tool.py` parses `[^n]` markers and `[^n]: **Gap:** D<n> — <question>. Placeholder: <one line>` definitions; `validate` pairs/rejects (no definition, duplicate label, outside an item, off shape, after a known difference, in canon); `check-changes` pairs footnotes with open gap items both ways (G12); `render` superscript links, Gap lines under items, "Gaps (n)" list; docstring updated. Fixtures: `package/offer.md` OFFER-08 carries `[^1]` → D3; `broken/gaps.md` holds every rejection; README rows and commands.

### Sanity scan after the edits

- `Managed-Updated-At` 2026-10-20 on the four edited guides (already today's date; headers read).
- Shape guide example still validates as a draft under a projection (the footnote is in the example only; the guide is not a spec file). No runtime reference to process-flow (`grep` → 0). No "human"/"Next Command" drift (0).
- Flow reflection: not gated guides (the shape guide is a reference; the authoring sentences change no gate).

### Tool verification

- `validate` catalog+package 0 issues (the draft's footnote allowed); design 0; `validate broken` names `gaps.md`'s seven lines (one per injected defect plus "in a canonical file" per definition, since `broken` is a single root); `check-changes` package and design 0 issues; `check-changes` with the broken artifact reports the footnote naming `D3` (absent there) and `D2` (a gap no draft marks), plus its earlier lines; `render` both packages and `render-request` ok; the Offers page shows "Gaps (1)", the superscript on OFFER-08's Expiration row and the Gap line linking D3.
- Found and fixed while testing: glossary and index files' `items` are tuples, so the drafts walk in `check-changes` and `render` filters on `kind == "spec"`.

### Compression review — pending

Four guides at cap: shape 8,200, product specs authoring 21,300, design specs authoring 17,800, product specs artifacts 6,800.

### Compression review — slice 3 (Astra, 2026-10-20)

Rewrites applied for all four files (scratchpad `compress3/out.md`): the shape guide's footnote element shortened and its placement, uniqueness and canon rules each stated once (Item sentence, validator list, `validate` row "Canon is the first root"); the `render` row names the page behavior; the authoring sentences say "footnoted with the item ID per the shape guide"; the artifact reference's list sentence tightened. Its flag was real and is fixed: the authoring guides' pre-existing marker-lifecycle sentences said requirements/specs "carry no Discussion citations" and design specs' drafts carry "no marker of any kind", both contradicting a footnote that names its `D#`; now "no Discussion citations but a gap footnote's `D#`", and "progress marker" in design specs. Sizes after: shape 8,950; product specs authoring 21,345; design specs authoring 17,811; product specs artifacts 6,850. Caps: pending the supervisor.

### Restructure per G13 (option C) — 2026-10-20

New companion `Guides/Core/spec-file-gaps.md` (managed, `guide.spec-file-gaps`, no wrapper): the form, edge cases, example and the tool's checks. The shape guide keeps the element's place in the Item order, a one-line **Gap footnote** element pointing at the companion, one validator clause, and the command rows' pointers; its example no longer carries a footnote (the companion's does). Manifest entry added; `spec-format-design.md` decision 21 records the placement; release entry updated; affected-documents table row B14. Sizes before compression: shape 8,470 (addition 277 over 8,193), companion 2,398. Second compression review running over the companion and the four existing files.

### Caps and round 1 — slice 3 — 2026-10-20

Caps set by the supervisor a little under the compressed sizes: spec-file-gaps 1,850; spec-file-shape 8,350 (was 8,200); product specs authoring 21,300, design specs authoring 17,800 and product specs artifacts 6,800 held (the one-sentence additions forced trims in adjacent pre-existing text). All five at or under cap (companion 1,846 after four trim passes; the "a little under" cap bit hardest on the smallest file). Round 1 commissioned over the companion, the shape guide's gap passages and the three sentences (scratchpad `review3-r1/`); series: new.

### Round 1 — slice 3 — 2026-10-20

Reviewer: Astra, read-only; probed the parser in memory (four inputs) and read `check_changes`.

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the validator promised to reject a definition outside an item and footnotes out of order, but the parser's intro/section branch swallowed a definition before the footnote check, and a rule or table after a definition passed (verified by the reviewer's probes) | accept | decision 21 (what the validator rejects); the companion's checks paragraph | parser: recognize the definition line before the prose branch; reject a rule or table after a gap footnote | marker-less definitions; optional Placeholder; label uniqueness; the canon/projection distinction |
| F2 product specs' drafting sentence could be read as footnoting any open item's requirement | log only (reviewer) → applied anyway as a one-word sharpen ("or, for a gap, its placeholder footnoted …") | workflow item 1 | reword | ordinary open items still drafted under the recommended reading |
| F3 the `validate` and `check-changes` rows carry no companion link | log only | decision 21 placement | none now; the item-order link and the render row's link route the reader | no duplication of the form in the shape guide |

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s3-r1 | 1.3 | 1 | 0 | 1 | 0 | 2 |

> F1 divergent · past-a-rule · verified = 5 × 0.25 × 1.0 = 1.25 · F2 log only (sharpened), noise · F3 log only, noise · two open questions (the "no placeholders" guarantee is about marked gaps; "nearest requirement" when none suits), neither.

#### Repairs

- F1: `_parse_spec` checks the footnote line before the intro/section prose branch; a rule or table after a gap footnote is rejected. Verified: the reviewer's four probes now give "outside an item" for the before-first-item and section cases, "table or rule after a gap footnote" for the rule-after case, and no errors for the example; `broken/gaps.md` gained the rule-after case and now reports nine lines; the suite is otherwise unchanged (0 issues on both packages; render ok). The companion's checks paragraph was already correct; no guide text changed for F1.
- F2: one-word sharpen plus a 1-byte trim to stay at 21,300.

### Round 2 — slice 3 — 2026-10-20

#### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 both drafting sentences said "(none: leave it out)", which a literal author reads as omitting the gap's whole representation when there is no placeholder; `check-changes` then fails on the unmarked open gap (verified) | accept | workflow item 1 | the footnote applies even when no placeholder exists; what is left out is the dependent text | no invented placeholders; the companion owns the marker-less form |
| F2 the page's Gaps list linked `#<item>` while a retired draft item's card is `#<item>-retired` (verified by the reviewer's probe) | accept | workflow item 3 (page lists footnotes with item links) | the list uses the item's real anchor | retired-item anchors; the Gap line's own anchor; Discussion links |

#### Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s3-r1 | 1.3 | 1 | 0 | 1 | 0 | 2 |
| s3-r2 | 7.5 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · verified = 3.75 · F2 divergent · off-normal · verified = 3.75 · open question (an empty draft with no requirement to host a note), neither. Neither finding is about round 1's repairs; F1 is the compressed adoption wording, F2 the renderer.

#### Repairs

- F1: both sentences now say the placeholder is footnoted "even when none exists and the dependent text is left out", paired with trims in adjacent pre-existing text (aggregator-section examples, the example's theme label, an undrawn-state example). Self-check: the marker-lifecycle exception sentences unchanged; both under cap.
- F2: `render`'s Gaps list links the item's real anchor. Verified by an in-memory render of a retired draft item carrying a footnote: the list's href matches an `id` on the page. Fixture suite unchanged (0 issues; render ok).

### Round 3 — slice 3 — 2026-10-20

No accept-level findings. One log-only renderer limitation (verified by the reviewer in memory): with `--base`, a superscript in removed text from the base draft links into the current item's footnote namespace, so a relabeled footnote leaves the old superscript dead; the current marker, Gap line and Gaps list are intact. Logged for renderer maintenance, not a guide change.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| s3-r1 | 1.3 | 1 | 0 | 1 | 0 | 2 |
| s3-r2 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| s3-r3 | 0 | 0 | 0 | 0 | 0 | 1 |

> F1 log only (cosmetic · off-normal · verified; renderer, old-side markers under `--base`), noise. Terminal round: no new live findings in the binding target (stop rule (a)).

## Maintenance retro — slice 3 — 2026-10-20

Maintenance retro: DONE

1. Inventory: new companion guide `Guides/Core/spec-file-gaps.md`; the shape guide's gap pointers; one sentence each in product specs authoring, design specs authoring and the product specs artifact reference; `spec-tool.py` (footnote parsing and placement checks, canon rejection, footnote ↔ gap-item pairing, superscript and Gap-line rendering, the Gaps list); fixtures; design-spec amendments. Host-install-visible (new managed guide; managed content changes; tool).
2. Bookkeeping: `Releases/unreleased.md` has the companion/shape entry (migration: none) and the tool entry; `CHANGELOG.md` has the "part three" line; they agree (grep: 1 and 1). Manifest has `guide.spec-file-gaps` (json loads). `Managed-Updated-At` 2026-10-20 on all five edited managed guides (headers read). README: a "Gap footnotes" row under both Shape rows (product specs and design specs authoring entries). `internal/maintain-skai.md`: no new invariant (G14, the placement rule, awaits the supervisor's go and is a separate edit).
3. Integration doc, 4. installer: untouched.
4. Consistency: runtime references to process-flow in the two Core guides → 0; "human"/"Next Command" in the companion → 0; the companion has the managed header, cue and addendum footer (visual); the shape guide links the companion twice (item order, render row), the known-gaps guide points at the shape as decided. Fixture suite: both catalogs validate clean; both packages pass `check-changes`; the broken artifact reports its 18 lines (log, citation and the two pairing lines); `validate broken` fails with `gaps.md`'s nine lines among 45; both renders and the request render ok; revive and projection fixtures unchanged. Change-package verification: promotion unchanged this slice (readiness and the canon write rely on `validate`/`check-changes`, whose new checks were exercised).
5. Process reflection: (a) a compression review flagged a real contradiction (the "no Discussion citations" sentences) that the cold review would otherwise have found a round later — worth keeping the compression reviewer's "flags" output as part of the procedure in skai#90; (b) G13 (placement) surfaced only when the supervisor saw the byte table; the affected-documents table should carry a "read by" column (always-read vs when-triggered) so placement is decided before drafting, not after; (c) the "a little under" cap on a 1,850-byte file took four trim passes for 30 bytes, each pass risking meaning; for a new small guide the cap is better set at the compressed size exactly.

Maintenance retro complete; no misses found. Follow-ups: G14 (house-style capture, Tim's go); the renderer's old-side superscripts under `--base` (logged).

## Slice 4 — Working Docs Placement And Scratch Output — 2026-10-21

Implementation only (skai#92); the reviewing session decides on a refinement cycle. Nothing committed. This document stays at its old path (`main/` segment); moving skai's own working docs is left for the supervisor.

### Sanity scan (guide-authoring § Sanity scan), per edited file

Search per file: `Managed-Updated-At` header; grep `\bhuman`, `Next Command`, `branch-path`, `<branch>`, `working-docs/…\.md`, `🟡`, `checkpoint`, `process-flow.md`, `- \[ \] [^A-Z]`, `evidence/`; count of `known-gaps.md` and `## Gates`. Visual review of each edited passage for the gated checks (gate lines, marker clearing, Gates entries): no edit touched gate, advance-intent or marker text.

- `Guides/Core/working-doc-conventions.md`: header 2026-10-21; all patterns 0 except six example paths (all `skai/working-docs/<session>/…` or a package `working-docs/`, intended). No gates.
- `Guides/Spec/work-spec-creation.md`: header 2026-10-21; `human` 1 → supervisor definition (false positive); `branch-path` 0; known-gaps pointer 1; Gates 1.
- `Guides/Spec/work-spec-implementation.md`: header 2026-10-21; `human` 1 (supervisor definition), `🟡` 1 (line 126, in-code markers, intended); `evidence/` 0; `branch-path` 0.
- `Guides/ProductSpecs/product-specs-artifacts.md`: header 2026-10-21; `evidence/` 1 (package layout, promotion check output, pre-existing, out of scope).
- `Guides/DesignSpecs/design-specs-artifacts.md`: header bumped (the first edit attempt failed its assert; fixed on rescan).
- `Guides/UIMap/ui-map-architecture-artifacts.md`, `ui-map-implementation-artifacts.md`: headers 2026-10-21; all 0.
- `Guides/Design/design-authoring.md`: header 2026-10-21; `human` 1, `🟡` 1 (process-flow inline definitions, pre-existing); `evidence/` 1 (package table, promotion check output, pre-existing).
- `Guides/UIMap/ui-map-implementation.md`: header 2026-10-21; `human` 1, `🟡` 4 (inline definitions and scaffold markers, pre-existing); `- [ ] <id>` 1 (format template, false positive); `evidence/` 0.
- Promotion guides (`product-specs-promotion.md`, `design-specs-promotion.md`, `design-promotion.md`): headers 2026-10-21; `human`/`🟡` hits are pre-existing definitions and readiness checks; `evidence/` in product specs and design promotion examples = package check output (pre-existing, out of scope).
- Unit testing guides (three): headers 2026-10-21; `branch-path` 0; example paths flattened; test-output paths moved to `/tmp/skai/<session-name>/…`.
- `Guides/Process/ticket-filing.md`, `process-refinement-guide.md`: headers 2026-10-21; `branch-path` 0; ticket-filing `- [ ] ~~T03` 1 (skipped-ticket template, pre-existing, ID present inside the strike).
- `internal/maintain-tickets.md`, `internal/maintain-retro.md`: headers 2026-10-21 (maintain-retro's bump was missed at first and caught by the header sweep); `Next Command` in retro is the check's own text.
- `internal/maintain-skai.md`, `internal/maintenance/guide-authoring.md`, `internal/maintenance/change-packages.md`, `Install/*`, `Templates/docs/skai/integration.md`, `README.md`: no header (not manifest assets); `branch-path` 1 in guide-authoring = the new check's own text; `🟡` in the template only on pre-existing fields (the new Scratch root field has none, since it has a default).
- Header sweep over `git diff --name-only`: every managed file at 2026-10-21.

### Pre-edit workflow model (work spec guides)

Modelled from the read before editing; the edits touch only artifact location and evidence wording, no gate, marker or advance-intent text.

- Creation: happy path resolve spec name → create `skai/working-docs/<spec-name>/<spec-name>-design.md` → Discussion (blocked gate while non-gap items open) → planned gate → design approved → handoff. Artifact: the design doc. Markers: `D#` checkboxes and the Decision Log. Blockers: no stable spec name (blocked gate before creation), unresolvable input.
- Implementation: start condition (approved design, no unchecked non-gap items) → audit and plan → implementation-plan gate → continuous implement/verify with evidence brackets → completion. Artifact: `<spec-name>-impl.md` beside the design. Markers: `T#` checked only on passing evidence. Blockers: verification failure needing a design return, tooling failure.

### Flow reflection (post-edit simulations)

- Creation, normal: request names "observable wrapper"; agent resolves `observable-wrapper`, creates `skai/working-docs/observable-wrapper/observable-wrapper-design.md` with no branch lookup; gates unchanged.
- Creation, blocked: no stable name → blocked gate before creating (unchanged). Name already used by an unrelated earlier spec (more likely now that committed specs accumulate in one flat folder): the guide's reopen rule is limited to the same work ("because implementation returned new evidence or a later slice is starting"), and the linked conventions guide says to choose a name no other effort uses. Covered by the link, not inline; with 6 bytes of combined headroom no sentence was added. Flagged for the reviewer.
- Creation/implementation, `auto`: the work spec skills support no `auto` (README § gates); unchanged by this edit.
- Implementation, normal: T02 build passes → `[evidence: <command>; exit 0]`, task checked.
- Implementation, blocked/tooling failure: T03 tests fail → output captured at `/tmp/skai/<spec-name>/t03.txt` (or the root `skai/integration.md` names) → `[evidence: <command>; exit 65; output: /tmp/skai/<spec-name>/t03.txt]`, task stays unchecked; a later reader whose scratch file is gone reruns the command. Gate behaviour unchanged.
- Implementation, resume: the design and impl are found by spec name at `skai/working-docs/<spec-name>/`. No issues found in simulation.
- UI Map implementation (also gated; edited): normal Build chunk passes → bracket with no output; failure → output in the scratch root, bracket names it, blocked gate as before; promotion moves the type folder with `working-docs/`; `auto` still stops on collisions/render failures (unchanged). No issues found in simulation.
- Promotion guides (gated; one clause each in archival): archival moves `working-docs/` with the package; collision and recovery text unchanged. No issues found in simulation.
- Ticket filing, ticket maintenance, unit testing guides (gated; path-only): gate lines and artifacts unchanged, only the artifact path formula. No issues found in simulation.

### Change package verification (change-packages.md § Verification)

- Path formulas: `working-docs/` sits inside the type folder in every artifact reference; no globs; no shared folder at the grouping level (cross-package notes go with the upstream package and are linked).
- Coexistence and independent promotion: unaffected; each type's `working-docs/` moves only with its own type.
- Reopen: unaffected.
- Promotion verifies canon before moving: unchanged; the move now names `working-docs/` explicitly in all four archival texts and in `change-packages.md` step 3.
- Collision/recovery: unchanged.
- UI Map Plan and no-proposal runs: conformance runs stay working documents at `skai/working-docs/<session-name>/ui-map-implementation.md`.
- Migration: `Releases/unreleased.md` covers discovery, classification with a supervisor stop, collisions, empty-folder cleanup, build output left out, links and a second discovery pass; each step re-runnable.

### Tool tests

- `python3 internal/tests/tools/spec-tool/test.py`: 17 tests OK (assertions from the host fixtures README's rows and command list; fixtures copied without the README).
- `python3 internal/tests/tools/ui-map-render/test.py`: 1 test OK (demo YAML renders to the guide's Mermaid block exactly, via `uv run`).
- `bash internal/tests/tools/skai-configuration/test.sh`: exit 0 (native checks passed; 2 Python history tests OK; 63 resolver comparisons), build output in `/tmp/skai/component-configuration/build`.

### Caps

| File | Cap | Before | After |
| --- | --- | --- | --- |
| work-spec-creation + work-spec-implementation | 32,600 | 32,584 | 32,594 |
| product-specs-artifacts | 6,800 | 6,799 | 6,776 |
| design-specs-artifacts | 5,000 | 4,927 | 4,944 |
| ui-map-architecture-artifacts | 5,500 | 5,491 | 5,496 |
| ui-map-implementation-artifacts | 6,500 | 6,499 | 6,498 |
| design-authoring | 15,100 | 15,091 | 15,084 |
| product-specs-promotion | 17,000 | 16,987 | 17,000 |
| design-specs-promotion | 12,800 | 12,758 | 12,778 |
| design-promotion | 11,500 | 11,492 | 11,497 |
| ui-map-implementation | 50,900 | 50,899 | 50,769 |

Trims made to fit (pre-existing text): product-specs-artifacts dropped the enumerated consumer list in § Change Requests and the request page's filename in the render sentence, and realigned the layout block; ui-map-architecture-artifacts dropped "Both formats are defined below."; design-authoring dropped the promoted path after "archives each type independently" (Purpose still names it) and shortened the `evidence/` row; product-specs-promotion dropped "active" before "change-ID grouping directory"; design-promotion "sibling types" → "siblings" and "the archived `design-promotion.md`" → "the archived artifact".

## Maintenance retro — slice 4 — 2026-10-21

Maintenance retro: DONE

1. Inventory: working-doc placement rule and flat session path; package `working-docs/` archived at promotion; working docs committed (managed `.gitignore` block, skai's own `.gitignore`); build/test output to the scratch root (conventions guide, work spec and UI Map evidence, unit test output paths, Integration template field, ConfigureSKAI build); `internal/tests/` created. Host-install-visible.
2. Bookkeeping: unreleased entry (four bullets plus a six-step migration) and the CHANGELOG "Working documents" line agree; no manifest change (no installable asset added or moved; `internal/tests/` is maintainer-only); headers swept; README working-documents section, test locations and paths updated; `maintain-skai.md` gains the tool-test rule and the tests home.
3. Integration doc: Special instructions section intact; the Scratch root field carries no 🟡 (it has a default); the installer guide now adds a template field a host form lacks.
4. Installer safety: the migration's classification step stops for the supervisor; moves never overwrite; deletion of build output is proposal-only.
5. Consistency: change package verification above; guide addenda untouched; no skill wrapper changed.
6. Fixed during retro: `internal/maintain-retro.md` header bump.

Follow-ups for the reviewer: the copied spec-tool fixtures are partly SalesPro-derived (Offers drafts, pipeline stages, `apps/salespro/`), against the LumenNotes house style, and need scrubbing before commit; skai's own existing working docs (`skai/working-docs/main/…`, top-level `working-docs/main/…`) are now visible to git and not yet moved to `skai/working-docs/<session>/`; package `evidence/` folders holding promotion check output were left as they are (not build/test output by the slice's wording, but close to it); a flat session folder makes name collisions between unrelated work specs likelier.

Process suggestions: (1) set caps with a little headroom (the slice's one-clause additions needed trims in six guides whose headroom was 1–13 bytes) — record the policy in `skai/refinement-reviews/` beside the caps; (2) the per-file sanity scan is mechanical enough to be a guard script under `internal/tests/` (echoes slice 2's suggestion).

### Review finding R1 — fixtures rewritten in LumenNotes terms — 2026-10-21

The 18 SalesPro-derived fixture files were rewritten: the workflow (formerly pipeline) and its stages, reminders (formerly appointments), collaborator suggestions (formerly offers), notebooks (formerly opportunities), the sync service (formerly the back office). IDs, defects, change-list shapes, the D3 gap footnote and the Decision Log defects are unchanged. A before/after run of every validate and check-changes command differs only in names (same counts, same line numbers). The three product-package pages were re-rendered. `test.py`: one assertion renamed (`Opportunity` → `Notebook`); 17 tests OK. The host copy was not touched.

### Cold review round 1 (Astra, scoped: conventions guide, migration entry, evidence paragraph, Scratch root field) — 2026-10-21

Standard: the slice's rules extracted to a clean file (no findings, no status). Five findings, all speculative, all accepted; collapsed to three defects per the reviewer's root causes.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 3 | 0 | 3 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2+F4+F5 (one defect, labels from F2) divergent · normal · speculative = 2.5 · F3 divergent · off-normal · speculative = 1.875 · two open questions, neither
 Root causes named by the reviewer: creation instructions bypassing the placement decision; migration completion defined by folder shape and `git status` instead of the documents.

- F1 closed: conventions step 3 now creates the folder chosen in step 1 or 2; "a work spec serves a change, not a package, so it is a session document" added to the no-package bullet and the release entry. The appendix item (work-spec-implementation line 57) is answered by the same sentence; the work spec guides are unchanged.
- F2 closed: discovery covers a top-level `working-docs/` and skai's own checkout; the list is the inventory steps 3–6 account for.
- F3 closed: step 4 distinguishes a move within one repository from a transfer into another (copy, remove, each reviewed in its own repository).
- F4 closed: step 6 repairs links into moved documents and the relative links inside them.
- F5 closed: step 6 verifies against the inventory; `git status` reviews the changes and is not the inventory.
Open questions logged, no change: partially migrated folder identity on restart (escalation route covers it); collisions stop, no merge procedure (intended).

### Cold review round 2 — 2026-10-21

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 3 | 0 | 3 | 0 | 0 |
| r2 | 6.3 | 2 | 0 | 2 | 0 | 0 |

> F1+F2 (one defect, the migration's unit of work; labels from F1) divergent · normal · speculative = 2.5 · F3 (scratch rule covers shipped build products; verified against `build.sh`) divergent · off-normal · verified = 3.75 · three open questions, neither

- F1+F2 closed: migration restructured. Discovery lists current locations as already placed (with their workflow subfolders) and makes the list the inventory; classification bins every entry (relocate with destination / captured output with disposition / already placed) before one approval stop; move and disposition follow; verification checks each entry against its classification and that no unresolved legacy entry remains; the supervisor's review-and-commit moved after verification.
- F3 closed: the rule now covers "output captured to verify a build or test"; a build's deliverable is not captured output and goes where its own guide says (conventions guide, Scratch root field, release line).
Open questions logged, no change: several old sessions serving one package collide and stop (intended); no name-reservation machinery.

### Cold review round 3 — 2026-10-21

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 3 | 0 | 3 | 0 | 0 |
| r2 | 6.3 | 2 | 0 | 2 | 0 | 0 |
| r3 | 2.5 | 1 | 0 | 1 | 0 | 1 |

> F1+F2 (one defect: "already placed" decided by path, exempting contents from classification and conflicting with link repair; labels from F1) divergent · normal · speculative = 2.5 · F3 (interrupted cross-repository copy needs the supervisor on rerun) log-only, noise · A1 (template's Android example teaches in-repository results) outside the binding passages, repaired in place · two open questions, neither

- F1+F2 closed: discovery no longer classifies by path (a current-looking folder is an inventory entry like any other); "already placed" is assigned in classification only after the association test on the contents; verification checks "not relocated" and allows the link repair step 5 requires.
- F3 logged — rationale: the collision stop already protects the work; no recurrence observed; an automatic duplicate-removal rule would be disproportionate.
- A1 repaired: the Test artifacts example now names the scratch root for Xcode results and says Gradle's `build/` output is copied to the scratch root after the run.
Open questions logged, no change: gate wording belongs to the enclosing update workflow; the integration updater's legacy-cleanup route covers superseded host values.

### Cold review round 4 — 2026-10-21

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 3 | 0 | 3 | 0 | 0 |
| r2 | 6.3 | 2 | 0 | 2 | 0 | 0 |
| r3 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F1 (discovery scope narrower than classification scope: package-level `evidence/` build captures never enter the inventory) divergent · normal · speculative = 2.5 · appendix (the round 3 repair of the Android example introduced a copy-from-`build/` step that contradicts the rule) outside the binding passages, repaired · open question (restart after relocation but before link repair relies on the approved inventory being kept) logged, neither

- F1 closed: discovery lists every place the old guides sent captured output (work spec `evidence/`, package type folders' `evidence/` from UI Map implementation; promotion check output stays), so classification and verification see them.
- Appendix repaired: the example now says every result is written under the scratch root by pointing the build's output options there, never under the repository's `build/`.
- Reviewer note: skill dispatch loaded the refiner-facing process-refinement guide into the reviewer's context before it noticed the exclusion; it reports excluding that framing. Logged for the skai#90 procedure: the host's installed skai skills can fire inside a Codex review when a guide name appears in the prompt.

### Cold review round 5 — 2026-10-21

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 6.9 | 3 | 0 | 3 | 0 | 0 |
| r2 | 6.3 | 2 | 0 | 2 | 0 | 0 |
| r3 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r5 | 0 | 0 | 0 | 0 | 0 | 1 |

> F1 restates round 3's logged interrupted-copy case (log-only, same rationale), noise · open question (step 6 does not repeat link verification; step 5 already requires it) neither · tooling claims verified by the reviewer: ignore-line removal in the three adapter runbooks, scratch field insertion, spec-tool's draft-only traversal, build.sh's scratch intermediates

### Closure

- Terminal round: no new live findings in the binding target (stop rule (a)). Convergence by clean round, 2026-10-21.
- Every repair was in the conventions guide, the release entry's migration, or the integration template; no capped guide was touched by the review repairs.

## Maintenance retro — slice 4, after refinement — 2026-10-21

Maintenance retro: DONE (covers the five review rounds' repairs; the Opus session's retro covers the implementation).

1. Inventory: repairs in the conventions guide, the release migration, the integration template's Scratch root field and Test artifacts example; host-install-visible (template and release entry).
2. Bookkeeping: CHANGELOG line and unreleased entry re-aligned to the narrowed rule ("output captured to verify a build or test"); README line 560, change-packages.md line 99 and maintain-skai.md's build-output line sharpened the same way (misses found and fixed). No manifest change. Headers: the conventions guide already at 2026-10-21; the integration template carries no managed header (project-owned form).
3. Integration doc: Special instructions section intact; Scratch root field has a default, no 🟡.
4. Installer safety: unchanged by the repairs; the migration's classification stop and collision stop preserved.
5. Consistency: `grep -rn 'branch-path\|<branch>' Guides internal Templates README.md Install` — 1 occurrence, the sanity-scan check in guide-authoring.md that looks for the stale segment (intended). `grep -rn -i 'build and test output'` across the repo — the four phrasings above fixed; dev-retro.md line 89 is the dev retro's evidence list, unrelated. Tool tests: spec-tool 17 pass, ui-map-render 1 pass, skai-configuration PASS.

Retro complete after fixes; no further misses.

## Migration of skai's own working documents — 2026-10-21

Run per the release entry's migration on skai's checkout (step 1 not applicable: no host install). Inventory: 8 session folders under `skai/working-docs/main/`, 3 under a top-level `working-docs/main/`, 1 under `working-docs/work/context/`; no packages, so all (a) relocate to `skai/working-docs/<name>/`; (b) three output files removed on the supervisor's approval (two build captures, one rendered SVG); (c) none. No collisions. Links repaired: `update-installation-findings.md` row 23 (pointer to its moved record) and `placeholder-scaffold-plan.md` line 15 (sibling reference); four mentions of host-checkout paths in `ui-map-system-findings.md`, `design-specs-design.md` and this record's slice 4 retro are history and stay. Verified: 12 documents at their destinations, no `.txt`/`.svg` output under `skai/working-docs/`, legacy folders removed; a second discovery finds no `main/` or top-level `working-docs/`.
