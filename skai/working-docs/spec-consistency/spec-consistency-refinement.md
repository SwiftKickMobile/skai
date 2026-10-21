# Spec Consistency — Refinement Working Document

Target: the whole refined set (13 guides, 6 skill wrappers) judged for cross-guide consistency. Standards: `skai/refinement-reviews/{spec-format-design,requirements-system-design,design-specs-design,design-process-design}.md`. Findings log: `skai/refinement-reviews/spec-consistency-findings.md`. Prior logs read for settled dispositions: `spec-file-shape-findings.md`, `spec-content-findings.md`, `spec-authoring-findings.md`, `spec-promotion-findings.md`. Tool at start: `Bin/spec-tool.py` md5 `144c8081`.

Caps (bytes, `wc -c`): spec-file-shape 8,200 · requirements-catalog 10,500 · requirements-artifacts 6,500 · requirements-authoring 20,500 · requirements-baseline 1,700 · requirements-promotion 17,000 · design-specs 15,000 · design-specs-artifacts 5,000 · design-specs-authoring 17,000 · design-specs-promotion 12,800 · design-authoring 14,400 · design-promotion 11,500 · skills 450/450/450/450/550/500.

Sizes at start: 8,198 · 10,486 · 6,492 · 20,255 · 1,698 · 16,987 · 14,983 · 4,954 · 16,990 · 12,800 · 14,396 · 11,500 · 443 · 449 · 430 · 449 · 549 · 500.

## Pre-review cluster (backlog items 1–3)

| # | Item | Fix | Net bytes | Must remain unchanged |
|---|---|---|---|---|
| B1 | shape § The Spec Tool `validate` row says "a failure blocks" unqualified | Row states spec-format 8's scope: a fault in a held file or a conflict the projection introduces blocks; an untouched canonical fault is a note and becomes a change request (same words as design-specs § Verification Checks and requirements-catalog § Purpose) | see measure | Overlay semantics; every file's shape still checked |
| B1b | shape: decision 3's pointer rule absent | Rule element: a rule or cell points at a top-level rule of its item by its bare bold number, at a nested one as `01-01`; the Table element's duplicate sentence folds into it | ~0 | Example's `**01**` pointer still reads as top-level |
| B2 | no-delegated-authoring rule only in requirements-baseline.md | Stated once in requirements-authoring § Drafting (mirroring design-specs-authoring's inline bullet); the baseline guide's Delegation section removed so the rule has one home | +190 / −250 | Baseline's other two rules; design-specs-authoring's bullet |
| B3 | citation sweep (below) | each mismatch fixed in the citing guide | per row | the cited guide's rule |

### B3 citation sweep

Method: every italic `*Section*`, `§`, bracketed link, check ID (`C1`–`C8`, `V1`–`V10`), command and flag, artifact section, file/folder name and request-folder form in each guide, checked by grep against the cited guide's current text. Searches: `grep -n '\*[A-Z][^*]*\*' <guide>`, `grep -n '§\|](' <guide>`, `grep -n 'C[0-9]\|V[0-9]' <guide>`, `grep -n 'validate\|references\|link-terms\|render\|check-changes\|--' <guide>`, `grep -n 'proposed-\|change-requests\|review.html\|authoring.md\|promotion.md' <guide>`.

| Citing guide | Citation | Cited guide now says | Status |
|---|---|---|---|
| requirements-promotion C4 | "not its Self-check" | requirements-catalog has no Self-check section (Required / Forbidden / Nothing that decays only) | mismatch — fixed (deleted) |
| requirements-catalog § Layout | `<catalog root>/ from the Integration block, never a literal path` | Release 13 removed the Integration block; authoring step 1 and promotion's ruling name the project README (`artifact-hosting.md`) as the root authority | mismatch — fixed ("linked from the project README") |
| requirements-artifacts § Change Requests | consumers "design specs, work specs, tests, promotion" | design-authoring § Resolution files requests "in the form of requirements-artifacts § Change Requests"; design-promotion readiness 5 cites it | mismatch — fixed (list gains design authoring) |
| spec-file-shape § The Spec Tool | no `check-changes` row | requirements-artifacts, design-specs-artifacts, both authoring guides' pre-gate pass and both promotion readiness screens cite `check-changes`, and route "the spec tool" to the shape guide | mismatch — fixed (row added) |
| spec-file-shape `references ID ROOT...` | IDs only | both authoring guides: "run the tool's `references` (the ID, or the term for every linked occurrence)"; tool accepts a term | mismatch — fixed (row names the term form) |
| spec-file-shape `render … --out FILE` / `render-request … --out FILE` | `--out` required | artifacts guides: the tool renders to `product-specs-review.html` / `request-review.html` in the package; tool: `[--out]` optional, default is that name | mismatch — fixed (`[--out FILE]`) |
| spec-file-shape § Glossary File | one `glossary.md`, entries alphabetical | design-specs § Glossary: sections Global, Shared, per family, alphabetical within each; splits per folder; spec-format 4 amended at target 2; tool reads every `glossary.md` under a root as one | mismatch — fixed (optional `##` sections, alphabetical within each; every `glossary.md` under the root reads as one) |
| spec-file-shape § What The Validator Rejects | no revived retired ID | requirements-promotion C1: "`validate` any duplicate or revived ID"; tool rejects a revived retired item or rule | mismatch — fixed (added) |
| design-specs-authoring § Discussion | Kind `Question`, `Proposal` or `Tradeoff` | requirements-authoring and design-authoring: `[Question]`, `[Proposal]`, `[Tradeoff]`; item line shows `[Kind]` | form only — fixed (brackets) |
| requirements-authoring | *Reopening*, *The change package*, *Working a scoped change*, *What `proposed-requirements/` holds*, *Gates*, *Drafting*, *Modify vs. retire* (catalog), `C1`–`C5` / `C6`–`C8` (promotion), artifacts § The Package / § Change Requests, `requirements-baseline.md`, `artifact-hosting.md` | all present as cited | ok |
| requirements-promotion | *Raising a change request*, *Archive the package*, artifacts § Change Requests, `change-requests/<nnn>/request.md`, catalog's Required / Forbidden / Nothing that decays, `C8` | present | ok (after C4 fix) |
| requirements-artifacts | catalog *Modify vs. retire*, `C7`/`C8` meanings, `proposed-product-specs/**` under a request | present; promotion agrees | ok |
| requirements-catalog | "(see authoring)" blocked gate for a split; "authoring's reference sweep" | authoring lists the split gate; the sweep is in *Working a scoped change* and `## Verification` | ok |
| design-specs | *Restatement*, *Citing by Reference*, *Modify vs. Retire*, *Stability*, *Never Appearance*, *Product Language Only*, *Purpose*, artifacts § Change Requests, `figma-designer-guide.md`, `link-terms` | present | ok |
| design-specs-artifacts | `design-specs.md#modify-vs-retire`, `C3`/`C4` meanings, requirements-artifacts | present; promotion agrees | ok |
| design-specs-authoring | `design-specs-artifacts.md#the-package`, `#change-requests`, `design-specs.md#modify-vs-retire`, `#what-counts-as-a-state`, `#verification-checks`, requirements-authoring `#reopening`, requirements-artifacts `#change-requests`, `design-authoring.md`, `artifact-hosting.md`, *Working a Baseline*, *Undrawn States*, *Design vs. App Differences*, *Requirements Gaps*, *Advance Intent*, `V1`–`V10`, `C3` for `C7` | present | ok |
| design-specs-promotion | *Raising a Change Request*, *Archive the Package*, `V1`–`V10` (`#verification-checks`), `V6`/`V8`/`V9` as tool-covered, artifacts § Change Requests, `C2` repoints | present | ok |
| design-authoring | figma guide *Working a backfill* (§ at line 226), requirements-artifacts `#change-requests`, *Mockups*, *Resolution*, *Gates* | present | ok |
| design-promotion | requirements-artifacts § Change Requests, `## Design Changes`, `## Assumptions and TODOs` listing (design-authoring § Resolution) | present | ok |
| skill wrappers | guide paths; "ten checks" (design-specs-promotion), "audit" (design-specs-authoring) | present | ok |

Standard-level residue (not a guide edit): requirements-system-design P1 still says "the root its Integration block names" while its Workflow step 4 calls that wording historical.

Fixture observation at start: `validate design-catalog design-package/proposed-design-specs` exits 1 with two dangling file targets (`[trash]` → `trash-screen.md`, `[REMIND-04]` → a requirements path outside the fixture) where the fixtures README promises 0 issues; the product fixtures behave as documented. Not a guide claim; reported to the supervisor.

## Self-check (pre-review cluster)

Edits landed: spec-file-shape (validate row scoped; `references ID-OR-TERM` with pointers and terms; `[--out FILE]` optional on both renders; `check-changes` row; glossary sections and per-folder glossaries; revived retired ID in the rejects list; pointer rule in the Rule element, the Table element's duplicate folded; funded by trims: intro parenthetical, example's second intro sentence, Statement's descriptive clause, "a new rule takes the next number", live-render trigger list (stated in the artifacts and authoring guides), "both spec types alike", renderer-diff wording, index-file wording — no rule removed); requirements-authoring § Drafting opens with the one-author rule; requirements-baseline § Delegation removed; requirements-catalog Layout root comment "linked from the project README"; requirements-promotion C4 "not its Self-check" deleted; requirements-artifacts consumer list gains design authoring (funded: "to hold it", "on the package"); design-specs-authoring Kind brackets.

- Contradict adjacent text or a sibling? No: the validate row now uses the same sentence as design-specs § Verification Checks and requirements-catalog § Purpose; the pointer rule matches the tool docstring and the example's `**01**`; the glossary sentence matches design-specs § Glossary and spec-format 4; requirements-authoring's rule matches design-specs-authoring's bullet; the catalog root comment matches authoring step 1 and Release 13.
- Stale sentence teaching the old behavior? Searched: `grep -rn "Self-check\|Integration block\|## Delegation"` over the set → 0 occurrences; `grep -n "a failure blocks"` in the shape guide → 0.
- Rule moved away from its point of use? The delegation rule moved toward it (Drafting, read in every mode); the baseline guide keeps its two baseline-only rules.
- Enforced rule weakened? No: "blocks" is kept for held files and projection conflicts; the pointer and glossary sentences add precision; the trims removed description only.
- Net size: shape 8,198 → 8,197; catalog 10,486 → 10,490; artifacts 6,492 → 6,484; authoring 20,255 → 20,470; baseline 1,698 → 1,431; promotion 16,987 → 16,967; design-specs-authoring 16,990 → 16,996. Group authoring 54,761 → 54,715 (cap 54,900).

## Sanity scan (pre-review cluster)

Structure: `Managed-Updated-At` — every edited guide already carries today's date (2026-10-18, `date +%Y-%m-%d`); 0 to bump. Gates/Advance intent sections — untouched (visual: the edits are outside them). Terms — `grep -n "\bhuman"` → 6 hits, all the standard gate-template supervisor definition ("the human or authorized agent"), false positives. Checkpoint/gate mixing — `grep -n checkpoint` → 0. Stack mismatch — none (visual). Working-doc paths — none created by these guides.
Process-flow compliance: `grep -n process-flow` over the set → 0. Standalone Progress Tracking sections — none (visual; the template's Progress tracking block only).
Marker convention: `🟡` in process artifacts — `grep -n 🟡` → hits are the template's convention lines and promotion's C7 grep example (in-code/evidence forms), false positives. `- [ ]` without letter-led ID — the edits added none. Aggregator sections — none added.
Flow control: no STOP added; no new `⏳ GATE:` line; marker clearing untouched (visual review of the edited paragraphs).
Gated-workflow references: pre-edit model and post-edit simulation apply to gated guides edited — requirements-authoring (one paragraph inside Drafting, no gate semantics touched), requirements-promotion (one clause in C4), design-specs-authoring (Kind brackets). Simulation: normal transition (authoring drafts under the one-author rule, reaches the Discussion gate unchanged), blocked case (open items → blocked line unchanged), `auto` case (bypasses the planned gate, not the pre-gate pass; unchanged). No issues found in simulation.

Pre-review cluster accepted by the supervisor (all nine fixes stand; P1 fixed in the standard). Tool build at round 1: md5 `c50cc20e`; both fixture sets validate clean as the README says (re-verified: product 0 issues / 3 notes, design 0 issues, broken exit 1, broken-revive 2 issues, both `check-changes` 0 issues, broken-package 19, `references STAGE-01-01` 4 lines incl. the table pointer).

## Round 1 (series A) — prompt `review/prompt-r1.txt`, report `review/review-r1.md`

Finding matrix:

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 a sibling package's `Design` justification may link a change-page draft that design promotion `C5` deletes; `C4` repoints only its own Design Changes links | supervisor decision (reviewer: supervisor-decision; fix adds verification scope before deletion) | design-process settled "no archiving of designs"; requirements-artifacts § Source; design-specs-artifacts Source; design-promotion `C4`–`C5` | pending ruling: (a) log only; (b) requirements-artifacts § Source: `Design` names the screen by product name, never a draft link (~+60, funded; design-specs-artifacts inherits via "Source as the product spec guide"); (c) `C5` repoints live citations in related artifacts before deleting (proof burden; 11,500/11,500) | production review before deletion; the authoring-return path; no archiving of designs |
| F2 renderer popovers do not load a requirement cited from outside the design-spec roots | routed to the tool pass (not in the binding target; no guide claims popovers — the docstring is the render spec) | `spec-tool.py` `prepare()` roots, `inline()` | tool | diff scope; one home |
| F3 a link that resolved in canon and dangles only because a draft retired or moved its target is printed as `note:`; spec-format 8 names a dangling link as a projection conflict that blocks | routed to the tool pass; reproduced on `c50cc20e` (`scratchpad/f3`: `note: legacy-note.md:12: [STAGE-02] points at #stage-02, which is not in drafts/domains/pipeline-stage.md`) | guides' wording equals the standard (shape `validate` row; both readiness condition 2) | tool: classify a projection-broken link as a conflict | notes for pre-existing untouched faults, including unlinked new-term occurrences |
| F4 artifact-hosting says the fixed root "is named by its content guide"; both content guides show `<catalog root>` / `<specs root>` (HEAD showed `skai/requirements/` and `skai/design-specs/`; the content pass regressed Release 13's fixed roots, artifact-location-design decision 1) | accept — deterministic dangling citation across guides (reviewer said log-only; the codification bar does not gate a dangling reference) | requirements-catalog § Layout; design-specs § Layout | the trees show the fixed root "in the repository the README links" (+2 / +58, funded by the § Indexes rationale clause −48) | promotion's `<catalog root>` command placeholders; `artifact-hosting.md` untouched (outside the target) |

Score: F1 supervisor decision, live pending ruling, divergent · normal · speculative = 2.5 · F2 routed to the tool, neither · F3 routed to the tool, neither · F4 accepted, divergent · normal · speculative = 2.5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.0 | 2 | 0 | 2 | 0 | 0 |

Repair cluster r1-A (F4): requirements-catalog § Layout root line `skai/requirements/   the fixed root, in the repository the README links`; design-specs § Layout `skai/design-specs/   the fixed root, in the repository the README links`; design-specs § Indexes "so a reader seeking a rule recognizes its line" trimmed.

Self-check r1-A: adjacent text — the catalog's "never a literal path" (pre-review wording) is gone with the placeholder, which is right: the root is fixed by Release 13 and only the repository is the README's; promotion's `validate <catalog root>` placeholders still read as "the root". Stale sentence — `grep -n "catalog root\|specs root"` over the set: remaining hits are promotion's command placeholders and "creating the catalog root"/"a new specs root" (the act, not a location) — none teaches a variable root. Point of use — the root is where the layout is. Weakened rule — no. Sizes: catalog 10,490 → 10,488; design-specs 14,983 → 14,993.

Sanity scan r1-A: `Managed-Updated-At` already today's date on both files; neither guide has gates (Structure, Process-flow, Marker, Flow-control checks: not applicable — visual confirmation that no gate, marker or STOP text was touched); `grep -n "\bhuman"` on both → 0; `grep -n 🟡` → 0.

F1 presented to the supervisor (see the report); no edit until ruled. Round 2 commissioned after the ruling.

## Resume (author replaced after round 1)

State re-verified before round 2: every target file's size equals the log's post-r1 record (8,197 / 10,488 / 6,484 / 20,470 / 1,431 / 16,967 / 14,993 / 4,954 / 16,996 / 12,800 / 14,396 / 11,500; wrappers 443 / 449 / 430 / 449 / 549 / 500), all under cap; tool md5 `c50cc20e` unchanged (the tool pass has not landed F3 yet); fixture checks as the README says (product 0 issues / 3 notes, design 0 issues, broken 36 issues exit 1, broken-revive 2, both `check-changes` 0, broken-package 19, `references STAGE-01-01` 4 lines). No F1 ruling is recorded in the log, the standards or this document; round 2 is commissioned on the supervisor's instruction with F1 in the settled slot as a pending ruling (a scheduled deferral, not a decision) and F2/F3 listed as tool-pass assignments.

## Round 2 (series A) — prompt `review/prompt-r2.txt`, report `review/review-r2.md`

Prompt: round 1's with the settled slot refreshed from the log (F1 pending ruling; F2 popovers and F3 projection-broken links assigned to the tool pass; F4's fixed-root closure; the first-catalog strand logged) and the recently-changed slot naming the r1-A repair. Diff against prompt-r1: those two slots only; against the template block: every non-slot line present, the three optional slot sections deleted. Same series (A): scoring model, files, standards, scope and charter unchanged.

Report: two findings, both tool-behavior defects the reviewer assigns to the tool pass; no re-raise of r1; no open questions; verdict usable.

Finding matrix:

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| r2-F1 an index file's intro is parsed (`_parse_index`, `spec.intro`) but `render_index` compares items only, so an index-intro change has no card and `check-changes` cannot see it; spec-format 11 says "intro by text" | routed to the tool pass (outside the binding target: the shape guide's diff list claims nothing about intros; the artifacts guides' "intro changes ride in Touches" is the change-list rule, true today) | `spec-tool.py` `render_index`, `check_changes`; standard decision 11 | tool: diff the index intro as `render_tree` already diffs a spec file's intro (lines 1517–1527); if the tool pass then wants the shape guide's § How The Renderer Diffs to say "intro by text", that is the tool pass's guide sync | orientation nonbinding; index-line matching; change-item granularity |
| r2-F2 `link-terms ROOT...` takes glossary terms only from the roots it may write, so a partial package without its glossary gets context only by passing the catalog root, which the tool then rewrites (`link_terms` iterates `by_rel` over every root and `write_text`s any file it links) | routed to the tool pass (the shape row and standard decision 10 say the same thing, "run while drafting"; the guides claim nothing the tool does not do; settled: tool gaps are fixed in the tool, never worked around in guide prose) | `spec-tool.py` `link_terms`; shape § The Spec Tool `link-terms` row (after the tool changes) | tool: read the projected glossary from every root, write only the last (drafts) root; then the shape row states that contract (tool pass guide sync; ~+40 bytes against 8,197/8,200, needs a trim) | canon read-only in authoring; untouched-file faults stay notes; `convert`'s whole-catalog write scope |

Verification of the reviewer's claims (scratchpad copy of the fixtures, `scratchpad/fx`; originals untouched — the three fixture review pages keep their 19:12 mtime and `check-changes` writes nothing, `prepare()` only records `out_dir`):
- r2-F1: edited `design-package/proposed-design-specs/screens/_screens.md` line 3 ("one file per screen" added); `check-changes` → 0 issues, exit 0, no Touches covering it; `render --out r.html` → counts unchanged, `grep -c "one file per screen" r.html` → 0; the intro text is absent from the page entirely. Reproduced.
- r2-F2: `link-terms catalog package/proposed-product-specs` on the copy → "linked 1 term uses"; `diff -rq` shows `catalog/domains/legacy-note.md` changed, no draft changed. `link-terms` over the drafts alone → 0 uses (the package holds its glossary; the no-glossary case follows from the code read: `terms` is built from `by_rel`, which holds only the supplied roots). Reproduced.

Score: r2-F1 routed to the tool, neither · r2-F2 routed to the tool, neither.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r2 | 0 | 0 | 0 | 0 | 0 | 0 |

Repairs: none (no guide text changed in round 2; no sanity scan or flow reflection due; no release-note or changelog change due). Findings about the refiner's own previous repairs: 0.

Closures r2: r2-F1 routed (tool pass; evidence above) · r2-F2 routed (tool pass; evidence above).

Stop rule: round 2 is a fresh round over the current text with no new live finding in the binding target — stop condition (a) is met, subject to the unimplemented ledger: r1 F1 (supervisor decision, still open). A ruling that changes guide text (option b or c) needs a fresh round after the repair; a `log only` ruling closes the pass by (a) with the ruling recorded.

## Ruling on r1 F1 and repair cluster r3-A

Ruling (supervisor, after round 2): option (b) — a `Design` justification names the screen or state by product name and never links a change-page draft, consistent with design-specs § Citing by Reference ("Never link into the design tool"); recorded in requirements-system-design.md (settled 2026-10-18, consistency pass). r2-F1 and r2-F2 stay with the tool pass; the shape guide's `link-terms` row is synced only when the tool's contract changes (checked at round 2 close on build `f971321f`: `link_terms` and its docstring unchanged — logged for the tool pass's guide sync).

| Defect | Triage | Touches | Minimal fix | Net bytes | Must remain unchanged |
|---|---|---|---|---|---|
| F1 (r1) | accept per ruling (b) | requirements-artifacts § Requirement Change Items, Source bullet; design-specs-artifacts inherits ("Source as the product spec guide") | "`Design` names the screen or state by product name, never a design-tool link; for a spec or request the Justification is the citation" (+63), funded by "`: the drafts realize the change`" (−31, rationale; the rule stays and requirements-authoring § Completion states it in its own home) and "` and the package returns to authoring`" (−37, promotion's rule, stated at promotion's blocked gate) | 6,484 → 6,488 (cap 6,500); content group 36,923 / 37,000 | design promotion `C4`/`C5`; the production review before deletion; no archiving of designs; the example `Design: the share sheet screens.` |

Self-check r3-A: adjacent text — the example R2 already names the screens by product name; design-specs.md § Citing by Reference "Never link into the design tool" and design-specs-artifacts "Packages are independent — never link another package" agree; design-specs-artifacts needs no edit (inherits). Stale sentence — `grep -rn "drafts realize\|returns to authoring\|For a design, spec or request"` over the set: requirements-authoring:152 (its own statement of the checkbox rule, not stale), the three promotion guides' blocked-gate lines (their own rule) — none teaches the old Justification form. Point of use — the rule is in the Source bullet, read when a justification is written. Weakened rule — no; two rationale/restatement trims only. Churn check — `grep -rn Justification` over both authoring guides and the design guides: no instruction to link a design draft.

Sanity scan r3-A (requirements-artifacts.md, not a gated guide): `Managed-Updated-At` 2026-10-18 already (header read). Gates / Advance intent / supervisor definition / gate-line / flow-reflection checks — not applicable, no gates (`grep -c '^## Gates'` → 0, `grep -c '⏳ GATE'` → 0). `grep -c '\bhuman'` → 0; `checkpoint` → 0; `process-flow` → 0; stack mismatch — none (visual); working-doc paths — none. Marker convention: `🟡` → 0; `- [ ]` → 0; aggregator sections — none; Kind labels — no discussion items in this guide. Flow control: no STOP or wait added (visual review of the edited bullet and the two trimmed sentences).

## Round 3 (series A) — prompt `review/prompt-r3.txt`, report `review/review-r3.md`

Prompt: round 2's with the settled slot's F1 sentence replaced by the ruling and the recently-changed slot naming the r3-A edit. Same series (A).

Report: one finding; r1 F1's repair confirmed holding ("`Design` justifications inherit the product-name rule"); no open questions; verdict usable.

Finding matrix:

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| r3-F1 design-specs-artifacts § Spec Change Items, Identity: "Draft every file whose links a move or retirement changes" reads as every citing file, where design-specs-authoring § Working a Scoped Change drafts only a design-spec citation's file (product specs → change request; work specs and other packages → their owner) | accept — a competing instruction at the point `Touches` is built; not in any prior log; the fix sharpens the sentence (codification check 1: the sweep rule exists and covers it) | design-specs-artifacts Identity bullet; design-specs-authoring sweep (unchanged) | "every design-spec file" (+12; 4,954 → 4,966, cap 5,000) | whole-file drafting and Touches coverage for the drafted file; change requests for product specs; owner handoff for work specs and other packages; promotion's repointing of incoming links |

Score: r3-F1 accepted, divergent · off-normal · speculative = 5 × 0.75 × 0.5 = 1.875.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r2 | 0 | 0 | 0 | 0 | 0 | 0 |
| r3 | 1.875 | 1 | 0 | 1 | 0 | 0 |

Findings about the refiner's own previous repairs: 0 (the Identity sentence predates this pass). Tool at round 3 close: md5 `86ddc848`; fixtures as the README says (product 0 issues / 3 notes, design 0, broken 36 exit 1, broken-revive 2, `check-changes` 0 / 19, `references STAGE-01-01` 4).

Repair cluster r3-B (r3-F1): design-specs-artifacts Identity bullet, "Draft every design-spec file whose links a move or retirement changes, in Touches after it." 4,954 → 4,966.

Self-check r3-B: adjacent text — the same bullet's "promotion verifies identical prose and resolved targets and repoints incoming links" unchanged; design-specs-authoring's three sweep dispositions unchanged and now matched ("a spec citation that does not is repaired by drafting its file (in Touches, as the artifact formats say)"). Stale sentence — `grep -rn "every file whose links\|whose links a move"` over the set: only the edited line. Point of use — unchanged (where Touches is written). Weakened rule — no, narrowed to its owner's scope.

Sanity scan r3-B (design-specs-artifacts.md, not a gated guide): `Managed-Updated-At` 2026-10-18 (header read); `## Gates` 0, `⏳ GATE` 0 — gate, advance-intent, supervisor-definition and flow-reflection checks not applicable; `\bhuman` 0; `checkpoint` 0; `process-flow` 0; `🟡` 0; `- [ ]` 0; aggregator sections none; stack mismatch none (visual); working-doc paths none; no STOP or wait added (visual).

Repair cluster r3-C (tool sync, authorized by the supervisor's ruling message): the tool pass landed `link-terms`'s new contract on build `86ddc848` (docstring lines 42–47; `link_terms(roots, write_roots=None)`: terms from every root, later overlaying earlier; writes only the last root by default; `convert` passes every root). Shape guide § The Spec Tool `link-terms` row: "Links every glossary term occurrence in files under the last root, reading terms from every root: `link-terms <catalog> <drafts>` writes only the drafts. Run while drafting and when converting." Funded by trims: intro rationale ", so one parser validates, cross-references and renders both" (−59), "Examples use LumenNotes." (−25), "(below)" in the validate row (−8). 8,197 → 8,188.

Self-check r3-C: adjacent text — the validate row's overlay sentence says the same thing of roots; requirements-catalog:101 and design-specs:80 "`link-terms` writes the links" stay true; spec-format decision 10 ("`link-terms` during drafting and migration") matches. Stale sentence — `grep -rn link-terms` over the set: the three lines above only; "Rewrites files" gone. Point of use — the row. Weakened rule — no; three rationale trims, no rule removed (the example still uses LumenNotes content unnamed).

Sanity scan r3-C (spec-file-shape.md, not a gated guide): `Managed-Updated-At` 2026-10-18 (header read); `## Gates` 0, `⏳ GATE` 0 — gate checks not applicable; `\bhuman` 0; `checkpoint` 0; `process-flow` 0; `🟡` 1 → line "progress markers (`- [ ]`, `🟡`)" in § What The Validator Rejects, false positive (in-code form, as the pre-review scan recorded); `- [ ]` 0; aggregator sections none; stack mismatch none (visual); working-doc paths none; no STOP or wait added (visual).

Closures r3: r3-F1 closed (r3-B; evidence: the sentence names design-spec files; sweep dispositions unchanged) · r2-F2 guide sync closed (r3-C; evidence: `link-terms catalog drafts` on a fixture copy of build `86ddc848` rewrites no catalog file — see the verification line below) · r1 F1 held in round 3.

## Round 4 (series A) — prompt `review/prompt-r4.txt`, report `review/review-r4.md`

Prompt: round 3's with the tool-pass list in the settled slot noting the landed `link-terms` contract and the recently-changed slot naming r3-B and r3-C. Same series (A). Commissioned because round 3 was repaired after.

Verification r3-C (fixture copy `scratchpad/fx2`, build `86ddc848`): `link-terms catalog package/proposed-product-specs` → "linked 0 term uses", `diff -rq` against the originals: 0 catalog files, 0 package files changed (on build `c50cc20e` the same command rewrote `catalog/domains/legacy-note.md`); `link-terms catalog` alone → 0 uses, 0 files (the unlinked term is one the package's glossary introduces, so the catalog alone has no entry for it).

Report: three findings; the r3-B and r3-C repairs confirmed holding ("the narrowed instruction … now agrees with authoring's ownership boundary"; "`link-terms` … the shape guide's row says so" not re-raised); no open questions; verdict usable on the ordinary path.

Finding matrix:

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| r4-F1 design-specs-authoring § Discussion's example "Draw `notes — acknowledged reminder` on Production" names a destination, where *Undrawn States* routes a drawing directly only for an unmanaged file, otherwise through a design package (design-authoring: production stays unchanged) | accept — a worked example competing with its rule, deterministic; not in any prior log (design-specs p1 r2 closed the same class); fix is a deletion | design-specs-authoring § Discussion line 245 | delete " on Production" (−14; 16,996 → 16,982) | direct drawing for unmanaged files; the design-package route; the gate note that a drawing-resolved item stays open until seen; `V5` accepting approved change-page drawings |
| r4-F2 `_parse_index` treats an indented continuation of an index bullet as intro text (requirements-catalog § Indexes route shows a wrapped bullet; valid Markdown) | routed to the tool pass (the guides claim nothing false; Markdown is the source and the tool its parser) | `spec-tool.py` `_parse_index`, `render_index` | tool: a continuation line belongs to its bullet | the index example's wrapped form; intro vs index-line treatment in Touches |
| r4-F3 `check-changes` keys glossary entries by term only, so an entry moved between per-folder glossaries (design-specs § Glossary: entries move with their items; a glossary splits per folder) fails both its `retire` and `add` entries | routed to the tool pass (a tool gap against design-specs-design 5 and the artifacts guide's operations; no guide claims otherwise) | `spec-tool.py` `render_glossary` keys, `check_changes` matching | tool: key by term and glossary file, or recognize removed-here-added-there as a move | terms unique across the projection; `move` for items only; retire-as-removal; entries following their items |

Verification of the tool claims (fixture copies, build `86ddc848`): r4-F2 — wrapped the `[list-screen]` bullet in `fx3/.../screens/_screens.md`; `parse().intro` → `[..., 'screen shares']`, `items` → `('list-screen', 'UI-LIST-', 'What every list')`; `validate` 0 issues, `check-changes` 0 issues (the intro change rides on the `add spec file` entry's Touches, so nothing surfaces). Reproduced. r4-F3 — in `fx4` moved `Reminder badge` from the drafts' root `glossary.md` to `screens/glossary.md` with `S9 retire glossary entry` and `S10 add glossary entry`; `check-changes` → "S9 declares retire but glossary entry Reminder badge is added; glossary entry Reminder badge is removed" and the same for S10, exit 1. Reproduced.

Score: r4-F1 accepted, divergent · off-normal · speculative = 1.875 · r4-F2 routed to the tool, neither · r4-F3 routed to the tool, neither.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r2 | 0 | 0 | 0 | 0 | 0 | 0 |
| r3 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r4 | 1.875 | 1 | 0 | 1 | 0 | 0 |

Findings about the refiner's own previous repairs: 0. Consolidation trigger: not fired (no fix became the next round's finding).

Repair cluster r4-A (r4-F1). Pre-edit workflow model (design-specs-authoring, gated): Initiation → Drafting → Discussion (blocked gate while `- [ ] D<n>` items remain; pre-gate pass, then the planned gate once every screen is drafted and every item resolved) → Completion; artifact `design-specs-authoring.md`; items are cleared one by one on the supervisor's approval of each, a drawing-resolved item only once the drawing exists and was seen; blockers: contradictory inputs, no change ID, design file unreachable (`V5`), prefix collision. Edit: § Discussion, the parenthetical example loses " on Production" (the item still "proposes the drawing by product name").

Self-check r4-A: adjacent text — *Undrawn States* ("produced directly or through design management as above") and *Design vs. App Differences* (direct when unmanaged, otherwise a design package) now own the destination alone; the gate note on drawing-resolved items unchanged. Stale sentence — `grep -rn "on Production"` over the spec and design guides: design-specs.md `V5`'s "on production or any approved change page" (the check's lookup scope), design-specs-promotion's `C1/V5` evidence example (a lookup on Production) and design-promotion's `C3` evidence (production updated in place, that guide's own write) — none a drawing destination for authoring. Point of use — the example stays in § Discussion where the item is written. Weakened rule — no; a deletion that removes a competing instruction. Size 16,996 → 16,982 (cap 17,000); authoring group 20,470 + 1,431 + 16,982 + 14,396 = 53,279 / 54,900.

Sanity scan r4-A (design-specs-authoring.md, gated): `Managed-Updated-At` 2026-10-18 (header read); `## Gates` and `## Advance Intent` present with the supervisor definition (grep counts 1 / 1 / 1); `\bhuman` hits are the standard supervisor definition only (classified false positive); `checkpoint` 0; `process-flow` 0; `🟡` 1 → line 127, the standard Advance Intent template's in-source-file marker bullet (convention statement; false positive); `- [ ]` without a letter-led ID 0; aggregator sections none; discussion items carry `[Kind]`; discussion-phase gate pattern untouched; stack mismatch none; working-doc paths none. Flow control: no STOP or wait added; the `⏳ GATE:` templates trace to the Discussion gate (visual review of § Gates, unchanged).

Flow reflection r4-A: normal transition — an undrawn-state item `- [ ] D3 [Proposal] Draw `notes — acknowledged reminder`` is raised in Discussion; the response ends `⏳ GATE: Blocked: 1 open items in Discussion. Resolve them to proceed to Completion.`; the file is managed, so the drawing comes through a design package; once it exists and the agent has seen it the supervisor's approval resolves D3 (box checked, Decision appended); with every screen drafted, the pre-gate pass runs and the response ends `⏳ GATE: Next: Discussion complete. Say "next" to advance to Completion.`; "next" advances to Completion. Blocked / tooling failure — the design file cannot be reached: `⏳ GATE: Blocked: the design file cannot be reached, so V5 cannot run. Resolve and say "next" to continue.`; nothing is cleared. Ambiguity — whether the state's file is managed is unknown: the agent asks in the item (Concern), not by drawing on production; the example no longer suggests otherwise. `auto` — bypasses the planned gate only; an open drawing-resolved item keeps the blocked gate, as the gate note says. No issues found in simulation.

## Round 5 (series A) — prompt `review/prompt-r5.txt`, report `review/review-r5.md`

Prompt: round 4's with the tool-pass list in the settled slot noting index continuation lines and glossary relocation matching, and the recently-changed slot naming r4-A. Same series (A). Commissioned because round 4 was repaired after.

Report: one finding, tool-side; r4-A confirmed holding ("the revised undrawn-state example leaves routing to the sections that own it"); no open guide question; verdict usable.

Finding matrix:

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| r5-F1 `link-terms` writes a glossary link into a draft as if the glossary sat under the drafts root (`relpath(grel, rel.parent)` on root-relative paths), so with the glossary only in the catalog the draft's definition points at an absent file; projected `validate` resolves it through the overlay and passes, the rendered href is broken | routed to the tool pass (requirements-catalog § Cite dependencies inline already states the rule — within a package, the draft when one exists, otherwise the canonical file; the tool violates it; no guide claims otherwise) | `spec-tool.py` `link_terms` link generation, `resolve_link`, `href_for` | tool: compute the definition from the winning glossary's actual location relative to the actual draft file | overlay precedence; governing-item exemptions; per-folder glossaries; last-root-only writes; promotion's destination-relative link preparation |

Verification (copy of the tool pass's new `fixtures/link-terms` in `scratchpad/fx5`, build `86ddc848`): `link-terms catalog drafts` → "linked 1 term uses"; the draft gains `[g-alpha-term]: ../glossary.md#alpha-term`, and `drafts/glossary.md` does not exist; catalog unchanged; `validate catalog drafts` → 0 issues, 1 note (the catalog's own unlinked use); `render --no-authoring` → href `drafts/glossary.md#alpha-term`. Reproduced.

Score: r5-F1 routed to the tool, neither.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r2 | 0 | 0 | 0 | 0 | 0 | 0 |
| r3 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r4 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r5 | 0 | 0 | 0 | 0 | 0 | 0 |

Findings about the refiner's own previous repairs: 0. Repairs: none in round 5 (no guide text changed; no scan, flow reflection or bookkeeping due).

Closures r5: r5-F1 routed (tool pass; evidence above).

## Stop

Round 5 is a fresh round over the current text that produced no new live finding in the binding target (its one finding routes to the tool, which owns it); every re-raise was answered by the log; the unimplemented ledger is empty (r1 F1 ruled (b) and repaired; no `log only` guide finding this pass). Stop condition (a) is met — convergence by a clean round. Tool at close: `86ddc848`; routed to the tool pass across the pass: r1 F2 popovers, r1 F3 projection-broken links (landed — `fixtures/broken-projection` now exists), r2-F1 index intro diff, r2-F2 `link-terms` write scope (landed — row synced), r4-F2 index continuation lines, r4-F3 glossary relocation in `check-changes`, r5-F1 `link-terms` draft link path.

Net size change for the pass (twelve guides): 139,739 → 139,669 (−70); wrappers unchanged. Final sizes against caps: 8,188/8,200 · 10,488/10,500 · 6,488/6,500 · 20,470/20,500 · 1,431/1,700 · 16,967/17,000 · 14,993/15,000 · 4,966/5,000 · 16,982/17,000 · 12,800/12,800 · 14,396/14,400 · 11,500/11,500; groups: content 36,935/37,000 · authoring 53,279/54,900 · promotion 41,267/42,700.

Closure confirmed by the supervisor after round 5: the pass is closed; the five open tool items (r1 F2, r2-F1, r4-F2, r4-F3, r5-F1) are with the tool pass.
