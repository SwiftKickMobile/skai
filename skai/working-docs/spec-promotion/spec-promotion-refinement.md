# Spec Promotion Guides Refinement

Working document for target 4: the promotion workflows of the three spec-bearing systems, refined together for fidelity and parallel structure. Standards: `skai/refinement-reviews/requirements-system-design.md` (P1, P8, P9, P10, Artifacts incl. the promotion artifact, Workflow § Promotion, Decisions 2026-10-18, Size Budgets, live render), `design-specs-design.md` (9 and 10 as amended, Amendments 2026-10-18, live render), `design-process-design.md` (Settled decisions incl. Promotion and the superseded requirements-impact entry, Amendments 2026-10-18, live render), `spec-format-design.md` (8–16). Read-only context: `Guides/Core/spec-file-shape.md`, `Guides/Requirements/{requirements-catalog,requirements-artifacts,requirements-authoring}.md`, `Guides/DesignSpecs/{design-specs,design-specs-artifacts,design-specs-authoring}.md`, `Guides/Design/design-authoring.md`. Findings log: `skai/refinement-reviews/spec-promotion-findings.md`. Tool: `Bin/spec-tool.py` (not edited; md5 b9da30fe at start); fixtures: SalesPro `working-docs/requirements-process/fixtures/`, run on a scratchpad copy.

| File | Start | Cap |
|---|---|---|
| Guides/Requirements/requirements-promotion.md | 19,789 | 17,000 |
| Guides/DesignSpecs/design-specs-promotion.md | 13,270 | 12,800 |
| Guides/Design/design-promotion.md | 12,549 | 11,500 |
| Templates/skills/skai-requirements-promotion/SKILL.md | 514 | 450 |
| Templates/skills/skai-design-specs-promotion/SKILL.md | 516 | 450 |
| Templates/skills/skai-design-promotion/SKILL.md | 995 | 500 |
| Group | 47,633 | 42,700 |

## Inherited from targets 2 and 3

- Routed here (target 3 r2 F1): requirements-promotion's worked `C1` evidence greps `^## ` while items are `###`; authoring cites that example. Fix: the tool's output is the evidence.
- Dependents named in the target 2 working doc: `requirements-promotion.md` § Raising a change request "Promotion alone raises these" → promotion files one like any consumer; `design-specs-promotion.md` § Raising a Change Request likewise; promotion artifacts gain the review-page link at the top.
- Settled in targets 2 and 3 and reused here: change items carry no inline text; request folders `change-requests/<nnn>/request.md`, filed by any downstream consumer, triaged on the request; promotion's own failed check on the package is not a request (artifacts guides); `check-changes` verifies coverage and the declared operation; validation blocks only for faults in held files and projection conflicts; the sweep is recorded under the authoring artifact's `## Verification`; design packages list filed requests under `## Assumptions and TODOs` until triaged.

## Pre-review tool facts (2026-10-18, tool md5 b9da30fe, fixtures copied to the scratchpad)

- `validate catalog package/proposed-product-specs` → 7 files, 0 issues, 3 notes outside the projection (untouched `legacy-note.md`: no statement, unlinked term; `legacy-twin.md`: duplicate ID shared by two untouched files), exit 0. Design fixtures: 9 files, 0 issues. `validate catalog` alone → 2 issues, exit 1 (single root: everything counts).
- Held-file fault (a second `#` title appended to a held draft) → issues, exit 1. Projection conflict (a draft item reusing a canonical ID `LEGACY-01`) → `duplicate ID … also in …/legacy-note.md`, exit 1. Retired-ID reuse inside a draft (`### STAGE-02` beside `### STAGE-02 (retired)`) → `duplicate ID STAGE-02 in file`, exit 1.
- `check-changes` on the fixture package → 0 issues; on `broken-package` → 18 issues (unchanged item named, absent item, absent rule, `add`/`retire`/`move` operation mismatches, every unlisted change), exit 1. A dropped item (deleted from the draft, catalog has it): with no entry → `item STAGE-10 is missing but no change-list entry names it`; with a `modify` entry → `declares modify but item STAGE-08 is missing`; with a `retire` entry → `declares retire but item STAGE-08 is missing`. So `C1` (no dropped ID, no renumbering, no retired-ID reuse) is mechanical: `check-changes` plus `validate`.
- `render` without `--out` writes `product-specs-review.html` / `design-specs-review.html` into the package folder, finding the authoring artifact itself; legacy names (`requirements-authoring.md`, `proposed-requirements/`) accepted, the page still named `product-specs-review.html`. `render-request` on request 002 (no drafts) writes `request-review.html` beside `request.md`.
- Post-write render (drafts copied over a catalog copy, then `render`) → legend `added 0, modified 0, retired 0, unchanged 30`: canon equal to the drafts renders as all unchanged.
- The validator does not resolve anchors (only `[name] used but not defined` / `defined but not used`), does not check that a new file's prefix is registered on its index line (only the line's shape), and checks that every glossary term occurrence is linked. So `C2`, `C3`'s target identity and `C5`'s judgment halves stay inspections; `C4` is judgment throughout.

## Pre-edit workflow models (gated guides; `gated-workflows.md` § Pre-edit workflow model)

### requirements-promotion.md

Happy path: explicit promotion signal → inspect existing Evidence (resume `C7`/archive if recorded) → collision and reference checks → readiness screen → `## Promotion Checks` written unchecked → planned gate "Promote N requirements to paths" → `next` → `C1`–`C8` in order with evidence → 🏁. Artifact: `requirements-promotion.md` (Inputs, Promotion Checks, Change Requests, Evidence). Markers: `- [ ] C<n>`, checked one by one after advance intent as each passes; `C1`–`C5` failure leaves the rest unchecked and returns to authoring; a fault after `C7`'s write is repaired in place; changed drafts reset all checks (prior evidence retained under `### Run <n>`); archival recovery retains `C1`–`C7`. Blockers: readiness failure, `C1`–`C5` failure, requested wording, catalog contradiction (authoring-return line); archive collision, inaccessible references, archival failure (standard line).
Target model (known deltas): the artifact links `product-specs-review.html` under its title; the readiness screen validates and renders first (`validate <catalog> <drafts>` with scoped blocking, `check-changes`, `render`) so the supervisor reviews the current page; `check-changes` replaces the hand recompute of the diff; the recorded reference sweep is checked; a `Proposed` request blocks whoever filed it; `C1`–`C5` keep one enumeration, the mechanical parts cite the tool's output, `C4` stays judgment; promotion files its own requests as `change-requests/<nnn>/request.md` (artifacts guide); the page is re-rendered after the write; the page moves with the package on archive; legacy names stay; prose says "product specs"; `C7` remains the completion identity; compact Advance intent block.
Simulations (pre-edit, on the target model): (1) normal — package with 9 requirements, readiness runs `validate` (0 issues, 1 note in an untouched file → change request filed, linked under `## Change Requests`), `check-changes` 0 issues, `render`; checks listed unchecked; planned gate; `next` → `C1`–`C7` pass with evidence, re-render, `C8` archive → 🏁 naming the request still `Proposed`. (2) blocked/tooling — `validate` reports a fault in a held draft: readiness condition fails, recorded in Evidence, authoring-return line; python missing → standard blocked gate. (3) ambiguity — `check-changes` passes but `C4` finds a mechanism word in REMIND-06: `C4` unchecked, evidence persisted, authoring-return line. (4) `auto` — already-reviewed drafts: the planned gate is bypassed, checks execute, a `C3` dangling target still stops at the blocked gate.

### design-specs-promotion.md

Happy path: signal → inspect Evidence → collision check → prerequisite (cited requirements canonical) → readiness → `C1`–`C4` unchecked → planned gate "Promote N items to paths" → `next` → `C1` (`V1`–`V10`), `C2` links, `C3` write, `C4` archive → 🏁. Markers as the product spec sibling with `C3` for `C7`, `C4` for `C8`. Blockers: readiness, `V1`–`V10` failure, requested wording, spec contradiction (authoring-return line); collision, references, design file unreachable for `V5`, archival failure (standard line); an uncanonical cited requirement waits at the standard line without returning the package.
Target model: page link `design-specs-review.html`; readiness validates (scoped blocking), `check-changes` (replacing the hand diff and the move-identity clause, which the tool checks), `render`; sweep recorded; `Proposed` blocks whoever filed; `C1` cites the readiness `validate` output where it covers a check; promotion files its own requests in the product spec form via the design artifacts guide; re-render after the write; the page moves with the package.
Simulations: (1) normal — two screens, `V5` found on Production, write, archive, 🏁. (2) blocked — design file unreachable: listed blocked gate. (3) ambiguity — a `validate` note in an untouched canonical spec (unlinked term): change request, write continues, check checked with its linked request. (4) `auto` — bypasses the review for reviewed drafts; `C1/V5` not found still stops.

### design-promotion.md

Happy path: signal → tool guide → continue an unfinished `design-promotion.md` or readiness (items resolved, Design Changes written, page exists with every draft, promoted path absent) → `C1`–`C6` unchecked → Promotion Checks gate → `next` → `C1`–`C4` → Production review gate (non-standard, never bypassed by `auto`) → `next` → `C5` delete page, `C6` archive → 🏁. Markers: `- [ ] C<n>`; `C1`/`C2` failure returns to authoring; `C3`/`C4` faults repaired in place; a new run after an authoring return unchecks every check. Blockers: readiness, `C1`/`C2`, requested design change (authoring-return line); access or library missing (standard line).
Target model: readiness condition 5 — every change request the package filed against the product spec package (listed under the authoring artifact's `## Assumptions and TODOs` until triaged) is `Incorporated`, `Rejected` or `Superseded`; a `Proposed` one waits at the standard blocked gate naming it (its triage is the product spec package's, not design authoring's); statuses cited from `requirements-artifacts.md` § Change Requests. No rendered page.
Simulations: (1) normal — three screens, checks pass, production reviewed, page deleted, archived, 🏁. (2) blocked — request 002 still `Proposed`: standard blocked gate naming it; triaged → readiness re-run. (3) ambiguity — supervisor asks for a design change at the production review: authoring-return line, production restored from version history. (4) `auto` — stops at the Production review gate always.

## Pre-review pass (known deltas, decided by the supervisor)

Clusters, one per file, each with self-check and sanity scan, then the post-edit flow reflection for the three gated guides. Trims come from the efficiency review the caps were derived from (SalesPro `working-docs/requirements-process/reviews/efficiency-4-promotion.md`) where they survive the deltas.

### Cluster A — requirements-promotion.md (19,789 → 16,998; cap 17,000)

Applied: Purpose says "product specs" and routes to the catalog, artifacts and shape guides (Cross-references section dropped — the same three links); artifact skeleton gains `[Review page](product-specs-review.html)` under the title and `## Change Requests` says "filed"; compact Advance intent block (identical to the authoring guides' form apart from the milestone and the workflow-specific paragraphs); readiness runs `validate <catalog root> <drafts>`, `check-changes` and `render` first, then five conditions — Discussion resolved, `validate` clean within scope (an untouched-file note becomes a change request), `check-changes` passes (replacing the hand recompute of the diff and the "ignore location-required path changes" rule, which the tool's diff applies), the reference sweep recorded under the authoring artifact's `## Verification`, no `Proposed` request whoever filed it; Promotion Checks preamble says the tool's readiness output is the evidence where it covers a check; `C1` cites `check-changes` (missing items) and `validate` (duplicate IDs) — the `^## ` grep is gone; `C2` says `validate` checks only the index line's shape; `C3` cites `validate` for definitions and inspects targets; `C5` cites `validate` for term links; `C7` re-renders after the write (canon equals the drafts, so every item shows unchanged); Raising a change request cites the artifacts guide's folder format and `render-request`, names a `validate` note in an untouched file as a case, and no longer says "Promotion alone raises these"; Archive step 1 says rendered pages move with the package. Trims: the worked checklist (prose states the boundary), the C1 command paths, the chat-link paragraph, the evidence-section lead and re-run sentence (the lifecycle owns `### Run <n>`), Initiation and Completion compression, the archive example's prose, "Record writes honestly" (C7's "record the write outcome … retaining failures" carries it), "Missing completion evidence needs archival recovery" (Initiation's resume rules carry it), "Check C8 only after …" in the lifecycle (Archive step 3 carries it).

Self-check: no contradiction — requirements-authoring still cites "promotion's `C1`–`C5`, enumerated only there" and "promotion's evidence form", both unchanged in identity; requirements-artifacts' "checked `C7` means written, `C8` archived" and "promotion's own failed check is not a request" hold (an untouched-file note is not the package's failure); the catalog guide's Purpose scope sentence matches readiness condition 2. Stale text: grep `Promotion alone|comm -23|\^## |Recompute|location-required|canonical catalog|Requested draft edits return` → 0. Rule not moved from its point of use: the authoring-return rule stays in the blocked-gate bullet; `C8`'s timing in Archive step 3. Nothing weakened: `C1`–`C5` failure still returns to authoring; a post-write fault is still repaired in place, never reworded; `Proposed` still blocks readiness.

Sanity scan: Managed-Updated-At 2026-10-18 (header read) → ok; `## Gates` line 47, `## Advance intent` line 85, supervisor definition present; the standard gate block diffs identical to design-specs-promotion's; the advance block diffs identical to requirements-authoring's compact form apart from the milestone; `\bhuman` → 1 (the standard definition); `Next Command|checkpoint` → 0; `🟡` → 3 (compact block, `C7` bullet, `C7` evidence grep — all intentional); live `- [ ]` items → 0 (skeleton and prose only); `⏳ GATE` → 8 (unchanged count); fences → 10 (five blocks, balanced); links → `requirements-catalog.md`, `requirements-artifacts.md`, `../Core/spec-file-shape.md` resolve; working-doc paths → 0; stack mismatch → 0; marker clearing tied to advance intent in the lifecycle paragraph; `auto` names what it does not bypass.

Flow reflection: (1) normal — signal; readiness runs the tool (0 issues, 1 note → request filed and linked); checks written unchecked; `⏳ GATE: Next: Promote 9 requirements to features/reminders.md, features/_features.md, glossary.md. Say "next" or what to change.`; STOP; `next` → `C1`–`C8` executed and checked one by one with evidence; 🏁 naming the `Proposed` request. (2) blocked — `validate` reports a fault in a held draft: readiness condition 2 fails, recorded in `## Evidence`, `⏳ GATE: Blocked: readiness condition failed — duplicate rule number in proposed-requirements/features/reminders.md:41. The package returns to authoring; re-run promotion once it is resolved.`; STOP; resumes only by a fresh promotion run. (3) `auto` — reviewed drafts: the planned gate is bypassed, checks execute; a `C3` dangling target stops at the blocked line regardless. No issues found in simulation.

Later in the pass (cluster B parallelism): the preamble sentence "Known-difference notes are observations, not obligations or markers" was dropped from both spec promotion guides; `C7`/`C3` carry it at the point of use ("only retirement marks and labeled known-difference observations accompany the contract"). 16,998 → 16,929.

### Cluster B — design-specs-promotion.md (13,270 → 12,799; cap 12,800)

Applied, parallel to cluster A: Purpose cites the shape guide; skeleton gains `[Review page](design-specs-review.html)` and "filed"; readiness runs `validate <specs root> <drafts>`, `check-changes`, `render` first, then five conditions (Discussion; `validate` scoped; `check-changes` — replacing the hand diff and the move-identity clause, which the tool checks (a moved item that changed without a modify entry fails); sweep recorded; `Proposed` whoever filed); the prerequisite paragraph (cited requirements canonical) stays a wait, not a return; Promotion Checks preamble says the tool's readiness output is the evidence; `C1` cites the readiness `validate` output for `V6` definitions, `V8` duplicates, `V9` term links; `C3` re-renders after the write; Raising a Change Request cites the artifacts guide, names a `validate` note in an untouched file, says a request filed here rides to completion `Proposed`; Archive step 1 moves rendered pages with the package. Trims: the worked checklist and the `V1` and `V3` excerpt lines (`V5`'s not-found pattern kept), the `C1/V<n>` template line (the excerpt shows the form), the `grep -rhoE` ID-comparison sentence (the tool compares), "Open the design for V5; unavailable access blocks" (the content guide's `V5` and the blocked-gate list both say it), "Failures return to authoring" in `C1` (the blocked-gate bullet), "Contradictions … follow Raising a Change Request" in the preamble (the blocked-gate bullet and the section), the Completion duplicate of "never re-promote" (Initiation keeps "never reopened or re-promoted"), Initiation merged into one paragraph, Archive compressed.

Self-check: no contradiction — design-specs.md § Verification Checks still opens with "run the spec tool's validate … then these ten checks, enumerated only here" and this guide cites them by anchor; design-specs-artifacts' "checked `C3` means written, `C4` archived" and "promotion's own failed check is not a request" hold; design-specs-authoring's "Reopening … with `C3` for `C7`: a recorded write returns to promotion" matches Initiation. Stale text: grep `Only promotion|Promotion alone|grep -rhoE|\.NN\]|Compare IDs|Current canon/draft` → 0; the dotted `UI-NOTES-01.02` in the excerpt is now `UI-NOTES-01-02` / `UI-NOTES-02-02`. Rule not moved: the prerequisite wait and the readiness returns keep their places; `C4`'s timing in Archive step 3. Nothing weakened: `V1`–`V10` failure still returns to authoring; the post-write fault still repaired in place; `Proposed` still blocks.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; `## Gates` line 36, `## Advance Intent` line 74, supervisor definition present; standard gate block identical to requirements-promotion's; advance block identical apart from the heading case and milestone; `\bhuman` → 1 (definition); `Next Command|checkpoint` → 0; `🟡` → 2 (compact block, `C3` bullet); live `- [ ]` → 0; `⏳ GATE` → 8 (unchanged); fences → 6 (three blocks, balanced); links → `design-specs.md`, `design-specs.md#verification-checks` (heading `## Verification Checks` at line 209 of the content guide), `design-specs-artifacts.md`, `../Core/spec-file-shape.md` resolve; working-doc paths → 0; stack mismatch → 0 ("design file" only); marker clearing tied to advance intent; `auto` names what still stops it.

Flow reflection: (1) normal — signal; prerequisite met; tool runs (0 issues); checks `C1`–`C4` unchecked; `⏳ GATE: Next: Promote 5 items to screens/notes.md, screens/list-screen.md, glossary.md. Say "next" or what to change.`; `next` → `C1` (`V1`–`V10`, each with a line), `C2`, `C3` (write, confirm, re-render), `C4`; 🏁. (2) blocked — the design file unreachable: `V5` cannot run, listed blocked gate (standard line), STOP; resumes when the supervisor restores access. (3) `auto` — reviewed drafts: planned gate bypassed; `C1/V5` not found stops at the authoring-return line. No issues found in simulation.

### Cluster C — design-promotion.md (12,549 → 11,497; cap 11,500)

Applied: readiness condition 5 — every change request the package filed against the product spec package (listed under the authoring artifact's `## Assumptions and TODOs` until triaged) is `Incorporated`, `Rejected` or `Superseded` per `requirements-artifacts.md` § Change Requests; a `Proposed` one blocks — with its own blocked-gate bullet (standard line naming the request; its triage is the product spec package's, so it is a wait, not an authoring return), the authoring-return line scoped to conditions 1–4; the tool guide stays the only tool-specific line; no rendered page. Trims: the "Planned gates for this workflow" list (the two gate notes name both gates and their placement), the worked checklist (prose states the `C1`–`C4` / `C5`–`C6` boundary) and the `C4` evidence line, the Cross-references section (Purpose loads the tool guide; the authoring guide is not a runtime read here), "This guide is tool-agnostic" (the delegation sentence says it), "where it stays as the record of why the designs are what they are", "Record what was checked and how" in `C1` and "a mismatch returns the package to authoring" in `C2` (the Evidence section and the blocked-gate bullet own them), compressed Initiation, lifecycle, Evidence lead and Completion.

Self-check: no contradiction — design-authoring lists filed requests under `## Assumptions and TODOs` until triaged and says at completion "promotion waits for its triage", which condition 5 enforces; design-authoring's reopen rule ("a package promotion holds is promotion's") matches Initiation; the design-process standard's "A requested design change at any point returns the package to authoring" stands in both gate notes. Stale text: grep `Planned gates for|Cross-references|see the marker lifecycle|This guide is tool-agnostic|record of why|3 links repointed` → 0. Rule not moved: the production-review-before-delete rule stays in the gate note, `C5` and the `auto` paragraph. Nothing weakened: `C1`/`C2` failure still returns to authoring; `C3`/`C4` faults still repaired in place, never by redesign; `auto` still never bypasses the Production review gate.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; `## Gates` line 33, `## Advance intent` line 75, supervisor definition present; standard gate and advance blocks identical to requirements-promotion's apart from the milestones; `\bhuman` → 1 (definition); `Next Command|checkpoint` → 0; `🟡` → 1 (compact block); live `- [ ]` → 0; `⏳ GATE` → 9 (unchanged: two planned lines, one authoring-return line, the standard pair, the notes); fences → 6 (three blocks, balanced); links → `figma-designer-guide.md`, `../Requirements/requirements-artifacts.md` (`## Change Requests` at its line 95) resolve; working-doc paths → 0; stack: "Figma" selector only; marker clearing tied to advance intent; `auto` names the hard gate.

Flow reflection: (1) normal — signal; tool guide read; readiness 1–5 pass; `C1`–`C6` unchecked; `⏳ GATE: Next: Promote 3 screens from pinned-notes to production. Say "next" or what to change.`; `next` → `C1`–`C4` checked with evidence; `⏳ GATE: Next: Review production in the design file. Say "next" to confirm it and delete the change page pinned-notes, or what to change.`; `next` → `C5`, `C6`; 🏁. (2) blocked — request 002 still `Proposed`: readiness condition 5 fails, recorded in `## Evidence`, `⏳ GATE: Blocked: change request 002 against the product spec package is still Proposed. Resolve and say "next" to continue.`; STOP; once triaged, a new run re-screens. (3) `auto` — bypasses the Promotion Checks gate, stops at the Production review gate always. No issues found in simulation.

### Cluster D — the three skill wrappers (514 / 516 / 995 → 449 / 449 / 500; caps 450 / 450 / 500)

Each is a plain dispatcher: frontmatter name and description (what it promotes, the three things the guide does, the invocation phrases), the heading, one instruction bullet reading the guide in full including its Project Addendum instructions. The design wrapper keeps one clause — "it names the tool guide to read first" — as the design authoring wrapper does, and loses the two bullets that restated the guide's hard boundaries (thin-wrapper invariant; the guide owns them). Self-check: no contradiction (each description matches its guide's Purpose); nothing weakened — the boundaries the design wrapper restated are rules in the guide (Purpose, the gate note, the `auto` paragraph). Sanity scan: wrappers carry no managed header by design (manifest `sourcePath` unchanged, `id` unchanged; the manifest descriptions still describe the skills); no gates; `\bhuman` → 0; markers → 0.

### Dependents and bookkeeping

- README: the two "Shape" rows said "promotion picks it up with its refinement" → "(cited by the content, authoring and promotion guides)"; the design promotion prerequisites add "and whose change requests against the product spec package are triaged". The Usage phases for the three promotion skills still describe the workflows correctly (readiness, unchecked checklist, gate, execute, archive).
- CHANGELOG `## Unreleased`: one net "Spec promotion guides" entry with the migration (refresh wrappers; add the page link to an existing promotion artifact; design packages: requests triaged before promotion).
- `assets.manifest.json`: no change (ids, paths and descriptions still correct; no date field).
- Change-package checks (`change-packages.md` § Verification): paths use the type folder (`skai/changes/<change-id>/<type>/`, `skai/promoted/<change-id>/<type>/`, `change-requests/<nnn>/request.md`), no discovery globs; siblings coexist and promote in either order (Archive step 1 in all three); reopen vs. promoted: an archived package is never reopened or re-promoted (all three); promotion verifies before moving, repairs links, records archived evidence, then checks the terminal item (`C8` / `C4` / `C6`); a collision blocks before the write, a failure after the write resumes archival only (all three); migration guidance in the changelog entry.
- Guide-addendum contract: footers and lookup names unchanged in all three guides.

### Pre-review verification (tool md5 cbb25721 — changed from b9da30fe during the pass; every claim re-run on a fresh fixture copy)

- `validate catalog package/proposed-product-specs` → 0 issues, 3 notes outside the projection, exit 0; design fixtures → 0 issues, exit 0. Held-file fault (second `#` title appended to a held draft) → blocking issues, exit 1. Projection conflict (draft item reusing canonical `LEGACY-01`) → `duplicate ID LEGACY-01 also in …/legacy-note.md`, exit 1. So readiness condition 2's wording (held-file faults and projection conflicts block; untouched-file faults are notes) matches the tool.
- `check-changes` fixture → 0 issues, exit 0; `broken-package` → 18 issues, exit 1; design fixture (with `move` + `modify` on `UI-NOTES-04`) → 0 issues; a dropped item (`STAGE-10` deleted from the draft) → `item STAGE-10 is missing but no change-list entry names it`, exit 1. So `C1`'s claim (`check-changes` names any item missing from a draft) and condition 3's claim (coverage and operation) match the tool.
- `render` without `--out` writes `product-specs-review.html` into the package folder; post-write render (drafts copied over a catalog copy) → `added 0, modified 0, retired 0, unchanged 30` — `C7`/`C3`'s "every item shows unchanged" matches. `render-request` on request 002 writes `request-review.html`. Legacy names (`requirements-authoring.md`, `proposed-requirements/`) render to `product-specs-review.html` — the product spec guide's artifact-skeleton link name holds for legacy packages.
- Validator coverage claims (`C2`: index-line shape only; `C3`: definitions only; `C5`: term links) checked against the validator's diagnostics list (`index line does not match …`, `[name] used but not defined`, `defined but not used`, `unlinked use of glossary term …`; no anchor-resolution or prefix-registration diagnostic).

Sizes after the pre-review pass: 16,929 / 12,799 / 11,497 / 449 / 449 / 500 = 42,623 of 42,700.

Open question for the supervisor (not a blocker; implemented as instructed): the post-write re-render replaces the committed page with one showing every item unchanged (canon now equals the drafts), so the archived page no longer shows the reviewed diff. The guides make this `C7`'s / `C3`'s confirmation. If the archived page should keep the diff, the re-render after the write should be dropped from the delta.

## Supervisor Rulings After The Pre-Review Pass (2026-10-18)

(1) The committed page is rendered last before the readiness screen and never after the write, so the archived page keeps the approved diff; after the write, `C7`/`C3` confirm with `validate` on the catalog and the read-back, not a re-render (spec-format 15 amended). (2) The sweep readiness check stays in design-specs-promotion for parallelism.

### Ruling cluster — requirements-promotion.md and design-specs-promotion.md (design-promotion has no page: nothing to change)

Applied: `C7` / `C3` confirm by reading the written text back and running `validate <catalog root>` / `validate <specs root>` — single root, so everything counts: the guides say a fault in a written file is the check's, one elsewhere was readiness's note (already a change request) — and state "No render after the write: the page keeps the approved diff"; the `C7` evidence example ends `validate skai/requirements: 0 issues in the written files` instead of a render legend. Funded by: the chat-link sentence, "needed adjustment" → "needed it", "every occurrence" → "every term", `render-request` parentheticals (the artifacts guides own rendering), "reference sweep" → "sweep", the prerequisite's "(a draft link is fine; …)", "annotate external references with new locations" → "annotate external references", the evidence lead, "the change-item count", "(their defects …)", "either package path" → "either path", "remove the active grouping directory only if empty" → "remove an emptied grouping directory".

Tool probe for the new claim: `validate` over a catalog copy with the drafts written in (single root) → the two untouched legacy files' faults print and exit 1 (everything counts with one root); with a `- [ ]` left in a written file → `offer.md:76: progress marker in spec prose` among the issues. So the guides' reading rule (written-file faults are `C7`'s; others were readiness's notes) is what makes the single-root run usable.

Self-check: no contradiction — the readiness intro still renders "first, so the supervisor reviews the current page" (the last render); the artifacts guides' "re-render … the authoring gate and promotion's readiness screen are the last renders of many" agrees; spec-format 15 as amended is the standard. Stale text: grep `re-render|shows unchanged|0 added` → only the "No render after the write" sentences. Rule not moved; nothing weakened — the marker/citation confirmation is still `C7`'s/`C3`'s, now with the tool behind it. Sanity scan (both guides): Managed-Updated-At 2026-10-18; Gates and Advance intent present; gate lines 8 / 8; fences 10 / 6; `\bhuman` 1 / 1; markers only in the compact block and the check bullets; links unchanged.

Flow reflection (`C7` branch re-run): write → read back → `validate skai/requirements` prints the two pre-existing legacy faults (readiness's notes, requests filed) and nothing in the written files → confirmation recorded → `C7` checked → `C8`. With a marker left in a written file: the fault is `C7`'s, repaired in place, re-validated, then checked. No issues found in simulation.

Sizes after the ruling cluster: 16,998 / 12,790 / 11,497 / 449 / 449 / 500 = 42,683 of 42,700.

## Round 1 (series A)

First commission aborted: the reviewer (Codex gpt-6-astra, prompt `scratchpad/r1/prompt.txt`) read the ruling cluster landing mid-run (the `C3` text changed between two reads) and stopped without findings; not a round, not scored. My error: the guides were edited while a review was running. Recommissioned over the stable text with the settled slot carrying ruling (1); prompt diffed against the template block (slot replacements and the three deleted optional slot sections only); report `scratchpad/r1/review-r1.md`. Six findings, one open question.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 readiness condition 2 files a request for an untouched-file note, then condition 5 rejects every `Proposed` request — the screen fails itself; the continue branch (a request filed here rides to completion `Proposed`) says otherwise | accept | req-sys P8/P10, design-specs 9; both spec guides § Readiness screen condition 5 | "No request filed before this run remains `Proposed`, whoever filed it" | A request already `Proposed` when promotion begins blocks whoever filed it; a request filed on the continue branch still rides to completion | −4 / +23 |
| F3 post-write confirmation says "a fault in a written file is `C7`'s; one elsewhere was readiness's note", but the validator reports a cross-file duplicate on the later-visited file (`cross.append(Issue(s.path, …, "duplicate ID … also in …"))`), so a duplicate the write introduced can land on an untouched file's path and be dismissed | accept (same root cause as F1: provenance between phases) | spec-format 8; both spec guides `C7` / `C3` | "a fault readiness did not note is `C7`'s, wherever reported" | Untouched faults readiness noted stay non-blocking; read-back plus `validate`; repair in place; no render after the write | −10 / −10 |
| F2 `check-changes` matches a rule entry against its parent item's status, so a wrong rule or operation can pass; readiness condition 3 (design specs) promises more | routed — re-raise | spec-format 15; tool `check-changes` | Tool pass (already assigned: target 2 r1 F2, r4 ruling, r5; target 3 r1 F4); the guide's wording equals the standard and the artifacts guide | Exact list-to-diff agreement stays mandatory | 0 |
| F4 design-promotion's authoring-return line covers readiness conditions 1–4, but condition 4 (promoted path already present) is a collision the spec guides send to the standard blocked gate | accept | design-process Settled § Promotion; design-promotion § Gates blocked list | Authoring-return group is conditions 1–3; condition 4 joins the standard-gate bullet with condition 5 | A collision still blocks; never overwrite, merge or re-promote | +45, funded by trims |
| F5 design-promotion's worked block says `C1`–`C4` checked but shows evidence for `C1`–`C3` only, under "Example"; the Evidence rule says one bracket per check | accept | design-promotion § Promotion Checks example | "Example" → "Excerpt", as the design-specs guide | `C4` evidence stays mandatory | 0 |
| F6 the readiness standard's "Integration block resolvable under its shape" has no operational step in promotion; `<catalog root>` is assumed | log only | req-sys Workflow § Promotion step 4; requirements-promotion § Initiation | None now: the standing blocked gate catches an unresolved root and the catalog guide forbids a literal path (requirements-system-findings r5/r6: logged, `shared` clause); sharpen Initiation's destination sentence on a strand | — | 0 |

Open question (neither): root-location authority — the product standard says Integration block while authoring's initiation routes first hosting through `artifact-hosting.md`; standard-level, for the supervisor.

### Round score

> F1+F3 one defect (provenance between phases), heaviest F3 (divergent · off-normal · verified = 3.75) · F4 divergent · off-normal · speculative = 1.875 · F5 divergent · normal · speculative = 2.5 · F2 re-raise of a routed defect, routed · F6 log only, noise

Note: F1 and F3 are one root cause by the reviewer's own section 0 and share one fix shape (preserve what readiness saw); collapsed, the row takes F3's labels (heaviest).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 8.125 | 3 | 0 | 3 | 0 | 1 |

Who the findings are about: F3, F4 (the "1–4" scope) and F5 (the dropped `C4` line) are pre-review-pass text of mine; F1 is the readiness condition as the delta shaped it. None is a prior round's repair (no prior round), so the consolidation trigger count is zero.

### Round 1 repairs — cluster A (F1 + F3; requirements-promotion.md 16,998 → 16,986; design-specs-promotion.md 12,790 → 12,796)

F3 reproduced first: on a catalog copy with the drafts written in, a duplicate `STAGE-03` appended to `domains/offer.md` is reported as `domains/pipeline-stage.md:28: duplicate ID STAGE-03 also in …/offer.md` — on the untouched, later-visited file. Readiness condition 5 now reads "No request filed before this run remains `Proposed`, whoever filed it" in both guides; the `C7` / `C3` parenthetical reads "(a fault readiness did not note is `C7`'s / `C3`'s, wherever reported)". Funded in the design-specs guide by "the other blockers" → "other blockers".

Self-check: no contradiction — Raising a change request's "A request filed here rides to completion still `Proposed`" and the artifacts guides' continue-branch sentence now agree with condition 5; the artifacts guides' "`Proposed` blocks promotion's readiness" still holds for every request that existed when the run began. Stale text: grep `elsewhere was|readiness's note` → 0; "in the package remains" → 0. Rule not moved. Nothing weakened: a pre-existing `Proposed` request still blocks whoever filed it; untouched faults readiness noted stay non-blocking; everything the write introduced is `C7`'s/`C3`'s.

### Cluster B (F4 + F5; design-promotion.md 11,497 → 11,500)

The authoring-return bullet covers readiness conditions 1–3; condition 4 (promoted path already present) joins condition 5 in the standard-blocked-gate bullet ("waits at the standard blocked gate naming it; a request's triage is the product spec package's"); "Example" → "Excerpt". Funded by: the second signal phrase, "the readiness screen being for a new run" → "; the readiness screen is for a new run", "and need no entry" → "; no entry", "with evidence recorded" → "with evidence".

Self-check: no contradiction — the readiness section's "A failure is a blocked gate (*Gates*)" now resolves to two bullets by condition number; design-process Settled § Promotion ("A requested design change at any point returns the package to authoring") and the spec guides' collision handling (standard blocked gate) both hold. Stale text: grep `conditions 1–4|\*\*Example\*\*|evidence recorded|promote this package` → 0. Rule not moved. Nothing weakened: a collision still blocks; `C4` evidence is still one bracket per check (the Evidence section), the excerpt no longer implies otherwise.

Sanity scan (three guides, after round 1 repairs): Managed-Updated-At 2026-10-18 → ok; Gates and Advance intent present; supervisor definition present; standard blocks unchanged (diffed earlier, untouched this round); `\bhuman` → 1 / 1 / 1 (definitions); `Next Command|checkpoint` → 0; `🟡` → 3 / 2 / 1 (compact block and check bullets); live `- [ ]` → 0; `⏳ GATE` → 8 / 8 / 9 (unchanged); fences → 10 / 6 / 6; links unchanged and resolving; working-doc paths → 0; stack: "Figma" selector only.

Flow reflection (branches touched): (1) product spec promotion with an untouched-file note — readiness files request 003, condition 5 sees no request filed before the run still `Proposed` → the screen passes, checks listed, planned gate; `next` → `C1`–`C7`; `C7`'s `validate skai/requirements` prints the noted legacy faults (readiness's, now request 003) and nothing new → checked; 🏁 names 003 still `Proposed`. (2) design promotion with `skai/promoted/pinned-notes/design/` present — condition 4 fails, recorded in Evidence, `⏳ GATE: Blocked: skai/promoted/pinned-notes/design/ already exists. Resolve and say "next" to continue.`, STOP; the supervisor resolves the collision; a new run re-screens. (3) `auto` unchanged. No issues found in simulation.

### Round 1 verification (tool md5 cbb25721, unchanged since the pre-review verification)

- F3's claim reproduced before the repair (above) and nothing else about the tool changed this round; the pre-review probes (scoped `validate`, `check-changes` coverage and operations, dropped item, post-write single-root `validate`, legacy names) stand.
- Caps: 16,986 / 12,796 / 11,500 / 449 / 449 / 500 = 42,680 of 42,700.

### Round 1 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 readiness filed a request then failed on it | closed | Condition 5 is "No request filed before this run remains `Proposed`, whoever filed it" in both spec guides; the continue-branch sentence agrees |
| F2 rule-level `check-changes` | routed — re-raise | Already with the tool pass (target 2 r1 F2 / r4 ruling / r5; target 3 r1 F4); the guides' wording equals spec-format 15 |
| F3 post-write fault attributed by reported file | closed | Reproduced (`pipeline-stage.md:28: duplicate ID STAGE-03 also in …/offer.md`); "a fault readiness did not note is `C7`'s/`C3`'s, wherever reported" |
| F4 design collision sent to authoring | closed | Authoring-return group is conditions 1–3; condition 4 waits at the standard blocked gate with condition 5 |
| F5 design worked block implied `C4` without evidence | closed | "Excerpt", as the design-specs guide |
| F6 root resolution not operational in promotion | logged | Standing blocked gate and the catalog guide's literal-path ban cover it; sharpen Initiation on a strand |
| Open: root-location authority (Integration block vs README hosting) | open question | Standard-level, for the supervisor |

Stop rule not met: round 1 produced live findings and was repaired after. Consolidation trigger count: zero. Round 2 to be commissioned over the current text, series A, settled slot refreshed (routine: F1/F3/F4/F5 dispositions).

## Supervisor Ruling After Round 1 (2026-10-18)

Round 1 accepted. The open question is settled in requirements-system-design § Workflow step 4: the project README is the root-location authority (`artifact-hosting.md` for a first artifact); the Integration-block wording was historical. No guide edit unless a strand occurs. Round 2 commissioned over the current text, series A, settled slot refreshed (routine: the four closures, the routed tool gap, the root-authority ruling). Prompt `scratchpad/r2/prompt.txt`, diffed clean; report `scratchpad/r2/review-r2.md`.

## Round 2 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r2/prompt.txt` (diffed clean), report `scratchpad/r2/review-r2.md`. Three findings, one open question.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 `check-changes` skips the operation check for an entry naming an existing, modified file (`if not (e.what == "file" and e.status == "modified")` … `if c.cid not in actual: continue`), so `add spec file` on an existing file passes | routed to the tool pass | spec-format 15; tool `check-changes` | Tool: assess the declared operation for a named modified file | The guides' claim equals the standard; no manual check added | 0 |
| F2 the `C7` evidence example ends "validate skai/requirements: 0 issues in the written files" — the old file-based boundary — while the rule now says a fault readiness did not note is `C7`'s wherever reported (my ruling-cluster text) | accept | spec-format 8/15; requirements-promotion § Evidence `C7` bracket | "validate skai/requirements: nothing beyond readiness's 1 note" | Noted faults non-blocking; new faults `C7`'s wherever reported; no render after the write | ±0 |
| F3 readiness condition 4 says "Every modify or retire has its sweep recorded", but authoring sweeps only before modifying or retiring an ID or a glossary entry; an index-line-only modify would be returned to authoring for evidence it was never asked to record | accept (same root cause as F2: a compressed qualifier) | req-sys P8; both spec guides § Readiness condition 4 | "Every modified or retired ID or glossary entry has its sweep …" in both guides | Sweeps for IDs (rules included) and terms stay required; promotion never reruns them | +12 / +12, funded in the design-specs guide |

Open question (neither): a resumed `C7`/`C3` confirmation may need the identities of readiness's notes, which successful evidence need not persist; the uncertain-outcome blocked route covers it (the reviewer's own reading); not a case for a readiness record.

### Round score

> F1 outside the binding target (tool), routed · F2 divergent · normal · speculative = 2.5 · F3 divergent · normal · speculative = 2.5 (one root cause with F2 per the reviewer's section 0, but two instances with two fixes in two places, so two rows — collapsing would need one fix)

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 8.125 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 5.0 | 2 | 0 | 2 | 0 | 0 |

Who the findings are about: F2 is the ruling cluster's evidence bracket (my repair after round 1's commission) — the consolidation trigger fires once; F3 is pre-review text. Both are compression dropping a qualifier: the class was swept once at the pre-review pass; this round's sweep re-reads every shortened example bracket and every readiness condition against the rule it illustrates.

### Round 2 repairs — one cluster (F2 + F3; requirements-promotion.md 16,986 → 17,000; design-specs-promotion.md 12,796 → 12,794)

F1 reproduced before routing: on the product fixture, an entry `R0 add file: domains/pipeline-stage.md` (an existing file the drafts modify) → `check-changes` 0 issues, exit 0. (On the design fixture a bare path `screens/notes.md` resolves to the index line `notes` and is rejected as unchanged — a second identity quirk of the same checker, noted for the tool pass.) The `C7` bracket now ends `validate skai/requirements: nothing beyond readiness's 1 note`; readiness condition 4 reads "Every modified or retired ID or glossary entry has its sweep under the authoring artifact's `## Verification`" in both guides, matching the authoring guides' "Before modifying or retiring an ID or a glossary entry, run the tool's `references`" (requirements-authoring:231, design-specs-authoring:193). Funded by "reading the written text back" → "read-back" (design specs) and "is already claimed" → "is claimed" (`C2`, requirements).

Class sweep (compression dropping a qualifier, second sighting after target 2's trim-damage class): every example bracket re-read against its check — `C1` (tool outputs plus the three ID properties), `C2` (empty-subject form), `C3` (definitions plus targets), `C4` (failure with persisted output), `C5` (index, glossary, term links, unnumbered prose), `C6` (rebased definition), `C7` (files, count, markers, links, retirement, notes, validate beyond readiness's notes), `C8` (move, absence, links, sibling), design `C1`–`C3`, design-specs `V5`; every readiness condition re-read against the rule it enforces (Discussion resolved; `validate` scoped; `check-changes`; sweep for IDs and glossary entries; pre-run `Proposed` requests; design 1–5). No further instance.

Self-check: no contradiction — condition 4 now matches the authoring guides' sweep trigger word for word in subject; the `C7` bracket matches the `C7` rule and the `C5`/`C1` brackets still cite the tool the same way. Stale text: grep `in the written files|Every modify or retire|reading the written text back` → 0. Rule not moved. Nothing weakened: a missing sweep for an ID or glossary entry still returns the package; a new post-write fault is still `C7`'s wherever reported.

Sanity scan (two guides): Managed-Updated-At 2026-10-18; Gates and Advance intent present; supervisor definition present; `\bhuman` 1 / 1; `Next Command|checkpoint` 0; `🟡` 3 / 2; live `- [ ]` 0; `⏳ GATE` 8 / 8; fences 10 / 6; links unchanged; working-doc paths 0; stack 0.

Flow reflection (readiness branch): a package whose only change is an index line — condition 4 has no modified or retired ID or glossary entry to check, passes; `C7` evidence records the read-back and `validate` with nothing beyond readiness's notes; 🏁. No issues found in simulation.

### Round 2 verification (tool md5 cbb25721, unchanged)

- F1's reproduction above is the only new tool fact; the guides' `check-changes` sentence equals spec-format 15 and the artifacts guides, so the tool is the stale side (routed). All earlier probes stand.
- Caps: 17,000 / 12,794 / 11,500 / 449 / 449 / 500 = 42,692 of 42,700.

### Round 2 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 `check-changes` skips the operation check for a named modified file | routed to the tool pass | Reproduced: `add file` on an existing modified file → 0 issues |
| F2 `C7` bracket taught the file-based boundary | closed | "nothing beyond readiness's 1 note"; consolidation trigger count one |
| F3 condition 4 demanded sweeps for every modify or retire | closed | "Every modified or retired ID or glossary entry has its sweep …" in both guides; matches the authoring trigger |
| Open: identities of readiness's notes on a resumed confirmation | open question | The uncertain-outcome blocked route covers it; no readiness record |

Stop rule not met: round 2 produced live findings and was repaired after. Consolidation trigger count: one (not twice). Round 3 to be commissioned over the current text, series A, settled slot refreshed (routine).

## Supervisor Ruling After Round 2 (2026-10-18)

Round 2 accepted; F1 with the tool pass. A round 3 fix that cannot be funded by a rule-free trim is reported as a size-rule supervisor decision with its byte cost. Round 3 commissioned over the current text, series A, settled slot refreshed (routine: F2/F3 closures, both routed `check-changes` gaps, the resumed-confirmation reading). Prompt `scratchpad/r3/prompt.txt`, diffed clean; report `scratchpad/r3/review-r3.md`.

## Round 3 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r3/prompt.txt` (diffed clean), report `scratchpad/r3/review-r3.md`. Three findings, no open question beyond F3.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 Raising a change request says "block if writing would leave canon inconsistent" (specs: "leave inconsistent specs") — an untouched-file defect (a duplicate ID between two untouched files, which the tool notes) remains after any write, so the sentence reverses readiness's "never blocks"; the gate bullets already say "would make the write inconsistent" | accept | spec-format 8; req-sys P2; both spec guides § Raising a change request | "block only if the write itself would contradict canon / the specs" | Held-file faults and projection conflicts still block; continue-branch requests ride to completion `Proposed` | ±0 |
| F2 the `C1` bracket concludes "no ID dropped, renumbered or reused" from `check-changes` and `validate` alone, and the `C1` rule's colon reads as if the tools cover all three; a retired item revived live under its ID with a `modify` entry passes both (probed below) — the inspection half is unstated | accept | req-sys P2 (a retired ID is burned), P8; requirements-promotion `C1` and its bracket | `C1`: the tools cover missing items and duplicates; inspect that no retired item is made live; the bracket records that inspection | Tool output stays the evidence for missing items and duplicate IDs; no whole-content check (P9) | +~70, funded by rule-free trims |
| F3 design rollback after a rejected production review does not say what to restore when unrelated work entered the design file meanwhile | log only | design-process Settled (superseded designs live in version history); design-promotion § Gates note 2 | None now; the standing blocked route catches it (design-process-findings p1 F4 logged the same recovery case); sharpen the restoration sentence on an occurrence | — | 0 |

### Round score

> F1 divergent · off-normal · verified = 3.75 · F2 divergent · normal · verified = 5 · F3 log only, noise

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 8.125 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r3 (A) | 8.75 | 2 | 0 | 2 | 0 | 1 |

Who the findings are about: F1 is text older than this pass (the request branch's blocking sentence), F2 is the pre-review `C1` rewrite; neither is a round repair, so the consolidation trigger count stays one. F3 is a second sighting of design-process-findings p1 F4 (restoration after rejection): logged again; a third sighting codifies.

### Round 3 repairs — one cluster (F1 + F2; requirements-promotion.md 17,000 → 16,997; design-specs-promotion.md 12,794 → 12,797)

F2 reproduced first: on a catalog copy with `STAGE-04` retired, a draft carrying `### STAGE-04` live with a `modify requirement` entry → `validate` 0 issues, `check-changes` 0 issues. Raising a change request now says "block only if the write itself would contradict canon" / "the specs" (the gate bullets' own formulation); `C1` reads "`check-changes` names any item missing from a draft, `validate` any duplicate ID; inspect that no retired item is made live", and its bracket ends "inspection: REMIND-07 is the only retired item and stays retired". Funded by rule-free trims: the `C3` bracket's "each reach their intended ID in the projected catalog" → "reach their intended IDs", "never assume an unrecorded write succeeded" → "never assume an unrecorded write", "is not promoted again" → "is never re-promoted", "Inspections and preparations name" → "Inspections name", "the host supports", "never on the mode" → "not the mode" (requirements); "Preserve sibling types" → "Preserve siblings" (design specs).

Self-check: no contradiction — readiness condition 2 ("never blocks … becomes a change request") and the request branch now agree; the gate bullets already said "would make the write inconsistent"; the catalog guide's Stability ("a retired ID is burned") is what the `C1` inspection enforces; P9 untouched (no whole-content check). Stale text: grep `would leave|no ID dropped|succeeded|not promoted again` → 0 in both guides. Rule not moved. Nothing weakened: a write that would contradict canon still blocks; held-file faults and projection conflicts still block at readiness; tool output remains the evidence for missing items and duplicates.

Sanity scan (two guides): Managed-Updated-At 2026-10-18; Gates and Advance intent present; supervisor definition present; `\bhuman` 1 / 1; `Next Command|checkpoint` 0; `🟡` 3 / 2; live `- [ ]` 0; `⏳ GATE` 8 / 8; fences 10 / 6; links unchanged; working-doc paths 0; stack 0.

Flow reflection (request branch): readiness notes a duplicate ID between two untouched files → request filed, linked, run continues; at `C7` the write touches neither file, so nothing it writes contradicts canon → no block; 🏁 names the request `Proposed`. A draft that revives a retired item: `C1`'s inspection finds the live heading where canon has `(retired)` → `C1` unchecked, authoring-return line. No issues found in simulation.

### Round 3 verification (tool md5 94407e0b — changed again during the round; every claim re-run)

- Clean projection → 0 issues, 3 notes, exit 0; held-file fault → exit 1; projection conflict → exit 1; `check-changes` fixture → exit 0; dropped item → `item STAGE-10 is missing but no change-list entry names it`; post-write single-root `validate` → the untouched legacy faults print, exit 1, and the write-introduced duplicate still lands on the later-visited file (`pipeline-stage.md:28: duplicate ID STAGE-03 also in …/offer.md`, so the "wherever reported" rule stays load-bearing); legacy names render to `product-specs-review.html`; `render-request` on request 002 writes its page.
- Round 2's routed F1 is now fixed in the tool: `add file` on an existing modified file → `R0 declares add but file domains/pipeline-stage.md is modified`, exit 1. Round 3's F2 case (revived retired item with a `modify` entry) still passes both commands, so the `C1` inspection stands.
- Caps: 16,997 / 12,797 / 11,500 / 449 / 449 / 500 = 42,692 of 42,700.

### Round 3 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 the request branch's "leave canon inconsistent" reversed readiness's "never blocks" | closed | "block only if the write itself would contradict canon / the specs" in both guides; greps for the old wording → 0 |
| F2 the `C1` bracket attributed retired-ID safety to tool output alone | closed | Reproduced (revived retired item passes `validate` and `check-changes`); `C1` names the inspection and its bracket records it |
| F3 design rollback scope with intervening work | logged | Second sighting of design-process-findings p1 F4; the standing blocked route covers it; a third sighting codifies |

Stop rule not met: round 3 produced live findings and was repaired after. Consolidation trigger count: one. Round 4 to be commissioned over the current text, series A, settled slot refreshed (routine).

## Supervisor Ruling After Round 3 (2026-10-18)

Round 3 accepted. The revived-retired-ID case goes into the validator as a rejection (tool pass); once it lands, `C1`'s bracket may cite the tool for it if the cap allows, otherwise the inspection wording stays. Round 4 commissioned over the current text, series A, settled slot refreshed (routine: F1/F2 closures, F3 logged, the tool fix and the pending validator rejection). Prompt `scratchpad/r4/prompt.txt`, diffed clean; report `scratchpad/r4/review-r4.md`.

## Round 4 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r4/prompt.txt` (diffed clean), report `scratchpad/r4/review-r4.md`. Two findings; open questions are restatements of settled ground (live render vs the frozen page; legacy artifacts; budget).

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 readiness condition 3 says "every changed requirement, glossary entry, index line and file has a `## Requirement Changes` entry", but the artifacts guide says an index line or intro rides in `Touches`, never as an entry, and a new file is one entry; the tool enforces the artifacts guide's granularity (`e.file in added_files`, `Touches` coverage); a literal reader returns a conforming package for extra entries; the design-specs "every change has an entry" has the same reading | accept | spec-format 15; requirements-artifacts § Granularity, design-specs-artifacts § Granularity; both spec guides § Readiness condition 3 | "every change has an entry, or rides in one's Touches, at the artifacts guide's granularity, with the right operation" — cite, never restate | `check-changes` still passes; operations still match; no entry names an unchanged or absent target | ±0 |
| F2 `C1`'s bracket (round 3's repair) evidences the retirement inspection only; `C1` also requires no renumbering, and swapping two live identities with `modify` entries passes both commands (probed below) | accept — round 3's repair is the finding: consolidation trigger fires a second time → structured tier from here | req-sys P2, P8; requirements-promotion `C1` and its bracket | `C1`'s inspection clause names identity continuity (each ID still heads the promise it headed in canon; none revived, none renumbered) and the bracket records it | Tool output for missing items and duplicates; no whole-content check (P9); single enumeration | +~40, funded by rule-free trims |

### Round score

> F1 divergent · normal · verified = 5 · F2 divergent · normal · verified = 5

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 8.125 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r3 (A) | 8.75 | 2 | 0 | 2 | 0 | 1 |
| r4 (A) | 10.0 | 2 | 0 | 2 | 0 | 0 |

Who the findings are about: F2 is round 3's `C1` repair; F1 is pre-review text (condition 3 as the pre-review pass wrote it). Consolidation trigger: twice (r2 F2 on the ruling cluster's bracket; r4 F2 on r3's `C1` repair) — the editing method is the problem: each `C1` repair patched the instance the reviewer named (the dropped-ID grep, then the retired-ID reuse) without restating the check's whole subject. Structured tier applied below before any edit.

### Structured tier

**Invariants**

- P1 `C1`–`C5` are enumerated once, in requirements-promotion; `V1`–`V10` once, in design-specs.md; every other surface cites.
- P2 Where the tool covers part of a check, the check names what the tool covers and what remains inspection; every example bracket shows the inspection the check names, in full, never only the tool's output.
- P3 The artifacts guides own the package layout, the change-list format and granularity, and the request format and lifecycle; promotion cites them and restates none of it.
- P4 Promotion blocks only on what the package introduced or would introduce: held-file faults, projection conflicts, a write that would contradict canon; a defect in an untouched canonical file is a change request, never a block, and a request promotion files rides to completion.
- P5 The three guides handle the same situation the same way unless a standard gives a reason; each sibling is re-read whenever one is edited.

**Canonical ownership**

| Content | Owner | Derivative surfaces |
|---|---|---|
| `C1`–`C5` text and subjects | requirements-promotion § Promotion Checks | its example brackets; requirements-authoring pre-gate pass (cites) |
| `V1`–`V10` | design-specs.md § Verification Checks | design-specs-promotion `C1`; design-specs-authoring pre-gate pass |
| Change-list granularity and `Touches` coverage | requirements-artifacts § Granularity (design: design-specs-artifacts) | readiness condition 3 in both spec guides; the tool's `check-changes` |
| Scoped blocking | spec-format 8; catalog guide § Purpose; design-specs § Purpose | readiness condition 2; Raising a change request; `C7`/`C3` confirmation |
| Request format and lifecycle | requirements-artifacts § Change Requests (design: design-specs-artifacts) | readiness condition 5; Raising a change request; design-promotion condition 5 |
| Tool commands and what the validator rejects | spec-file-shape.md § The Spec Tool; tool docstring | readiness intro; `C1`, `C2`, `C3`, `C5`, `C7` tool citations |
| ID stability (append-only, retired IDs burned, modify vs retire) | requirements-catalog § Stability, § Modify vs. retire | `C1`'s inspection clause |

**Rule impact maps**

- F1 — violates P3 (restated granularity, wrongly). Owner: the artifacts guides. Dependents by grep `check-changes` in the three guides: requirements-promotion lines 137, 144, 162 and the `C1` bracket; design-specs-promotion lines 127, 134. Edit: condition 3 in both guides cites the artifacts guide's granularity. Must not change: `C1`'s use of `check-changes` for missing items; the readiness intro.
- F2 — violates P2 (the bracket shows less inspection than the check names) and P1-adjacent (the check's subject was re-cut per instance). Owner: `C1` in requirements-promotion. Dependents by grep `C1`: its bracket; requirements-authoring:112–115 (cites, no restatement — unchanged); the findings log rows. Edit: restate `C1`'s whole subject once — the tool's two coverages, then one inspection of identity continuity covering both revival and renumbering — and a bracket that records that inspection. Must not change: P9; tool output as evidence for missing items and duplicates; the catalog guide's Stability wording (owner of the ID rules).
- Class sweep under P2 (the whole class, not the instance): every bracket in the three guides re-read against its check's named inspection — `C2` (registration on the index line: present), `C3` (targets and tracking issue: present), `C4` (three rule lists: present), `C5` (questions, glossary pointing, unnumbered prose: present), `C6` (definitions rebased, identities unchanged: present), `C7` (links, markers, retirement, notes, validate beyond readiness's notes: present), `C8` (move, absence, links, sibling: present), design `C1`–`C3` (script scope plus inspected rules; entries vs frames both ways; identity kept, placement, components: present), design-specs `C1/V5` (locations searched: present). `C1` is the only bracket short of its check.
- Class sweep under P3: grep `glossary entry, index line|index line and file|every changed` in the three guides → only condition 3 (both spec guides) restated granularity; `C5`'s "index lines name the questions" is traversal, not list granularity.

### Round 4 repairs — one cluster (F1 + F2; requirements-promotion.md 16,997 → 16,987; design-specs-promotion.md 12,797 → 12,800)

Tool first (md5 144c8081): the validator now rejects a revived retired ID (`STAGE-04 revived; it is retired in … and a retired ID is never modified`, exit 1), so `C1` cites it; two live items exchanging bodies with a `modify` entry still pass `validate` (exit 0) and `check-changes` (0 issues), so renumbering stays the inspection. Condition 3 in both guides: "every change has a `## Requirement Changes` / `## Spec Changes` entry, or rides in one's Touches, at the artifacts guide's / artifact formats' granularity, with the right operation; no entry names an unchanged or absent target". `C1` restated whole: "every ID in a rewritten file remains in its draft, heading the promise it headed in canon: `check-changes` names any item missing from a draft, `validate` any duplicate or revived ID; inspect that none is renumbered (two live promises exchanging IDs pass both)"; its bracket: "inspection: each of the 9 IDs heads its canonical promise, none renumbered". Funded by rule-free trims: `C2` and `C6` brackets shortened, "labeled known-difference observations" → "known-difference notes" (`C4`, `C7`), the readiness intro's "Then, before writing" (requirements); "(a draft link is fine; `C2` repoints it)" → "(`C2` repoints a draft link)", "verification failures and other blockers" → "blockers", "duplicate IDs" → "duplicates", "not siblings or promoted history" → "not its siblings or history", "beyond" → "past", "the shape guide" → "shape guide", "within" → "in", "do not block" → "never block", "re-promoted" → "promoted" (design specs).

Self-check: no contradiction — condition 3 now defers to the granularity the artifacts guides own and the tool enforces; `C1` matches the catalog guide's Stability (IDs never renumbered, a retired ID burned) and cites what the tool now rejects; the authoring guide's pre-gate pass cites `C1`–`C5` without restating. Stale text: grep `no retired item is made live|every changed requirement, glossary entry|labeled known-difference|stays retired|re-promoted|do not block` → 0. Rule not moved. Nothing weakened: `check-changes` still must pass with matching operations; identity continuity is now the whole of `C1`'s inspection rather than one instance of it; P9 untouched.

Sanity scan (two guides): Managed-Updated-At 2026-10-18; Gates and Advance intent present; supervisor definition present; `\bhuman` 1 / 1; `Next Command|checkpoint` 0; `🟡` 3 / 2; live `- [ ]` 0; `⏳ GATE` 8 / 8; fences 10 / 6; links unchanged; working-doc paths 0; stack 0.

Flow reflection (`C1` and readiness 3): a package modifying one requirement and its index line, listed as one entry with the index line in Touches — `check-changes` 0 issues, condition 3 passes (rides in Touches at the artifacts guide's granularity); `C1`: tool output clean, inspection finds each ID heading its canonical promise → checked. A draft that exchanges two IDs' bodies: tool output clean, inspection finds two IDs heading other promises → `C1` unchecked, authoring-return line. No issues found in simulation.

### Round 4 verification (tool md5 144c8081)

- Every claim re-run: clean projection exit 0; held-file fault exit 1; projection conflict exit 1; `check-changes` fixture exit 0; dropped item exit 1; `add file` on a modified file exit 1; revived retired ID → `validate` exit 1 (new); identity swap → both pass; post-write single-root `validate` prints the untouched legacy faults and the write-introduced duplicate on the later-visited file.
- Caps: 16,987 / 12,800 / 11,500 / 449 / 449 / 500 = 42,685 of 42,700.

### Round 4 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 condition 3 restated change-list granularity against the artifacts guides | closed | "or rides in one's Touches, at the artifacts guide's granularity" (both spec guides); P3 sweep clean |
| F2 `C1`'s bracket evidenced revival only; renumbering unstated (round 3's repair) | closed | `C1` restated whole (tool: missing, duplicate, revived; inspection: none renumbered — swap probed passing both); bracket records the inspection; consolidation trigger twice → structured tier (P1–P5, ownership table, impact maps) |

Stop rule not met: round 4 produced live findings and was repaired after. Consolidation trigger count: two; the structured tier stays for the rest of the pass. Round 5 to be commissioned over the current text, series A, settled slot refreshed (routine).

## Supervisor Ruling After Round 4 (2026-10-18)

Round 4 accepted; the tool has no open items, so round 5 runs against a stable build (md5 144c8081). If round 5's findings are again compression defects (meaning lost to a trim), report that classification with the byte cost of a full restatement; the supervisor will consider a cap adjustment rather than a sixth compression repair. Round 5 commissioned over the current text, series A, settled slot refreshed (routine: F1/F2 closures, tool state). Prompt `scratchpad/r5/prompt.txt`, diffed clean; report `scratchpad/r5/review-r5.md`.

## Round 5 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r5/prompt.txt` (diffed clean), report `scratchpad/r5/review-r5.md`, tool md5 144c8081 throughout. One finding, one open question.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 the `C7` bracket's marker grep tests `\(D[0-9]+\)` — the pre-2026-10-05 inline citation form — while Discussion citations are reference-style `[D2]` (artifacts guide example), so a copied bracket can report "returned nothing" over a file still citing Discussion; `validate` checks definitions used and defined, not what they cite | accept — stale original text (the regex predates this pass's link-style decision), **not a compression defect**: byte cost 0 | req-sys release decision (links); requirements-promotion § Evidence `C7` bracket | Regex `\[D[0-9]+\]` in the bracket | The bracket stays a repeatable command (`## Evidence`: inspections name repeatable inputs); validate beyond readiness's notes; no render after the write | 0 |

Open question (logged, not scored): removing an item's last numbered rule leaves valid numbering and only a modified parent item, so `validate` and `check-changes` both pass; `C1`'s opening "every ID in a rewritten file remains" covers rules (spec-format 2: rules are append-only and retire in place) and its named inspection says "none is renumbered" — the reviewer notes the opening clause carries more than the inspection names. Logged for a second sighting: on recurrence, "inspect that no item or rule is dropped or renumbered" (+16 bytes).

### Round score

> F1 divergent · normal · verified = 5

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 8.125 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r3 (A) | 8.75 | 2 | 0 | 2 | 0 | 1 |
| r4 (A) | 10.0 | 2 | 0 | 2 | 0 | 0 |
| r5 (A) | 5.0 | 1 | 0 | 1 | 0 | 0 |

Who the findings are about: F1 is text older than this pass (the grep's `(D#)` alternative survived the 2026-10-05 link-style migration unchanged); not a round repair and not a trim. Consolidation trigger count stays two; the structured tier applies (P2: the bracket must show the inspection the check names — the check names Discussion citations; the bracket's command must find the current form).

Rule impact map — F1: violates P2. Owner: `C7` (requirements-promotion). Dependents by grep `D\[0-9\]|\(D` across the three guides and the authoring guides: only this bracket carries the pattern; requirements-authoring says "requirements carry no Discussion citations" and the artifacts guide shows `[D2]` with a definition. Edit: the regex only. Sweep of the class (commands in brackets whose pattern predates a format decision): the `C7` grep is the only command-form bracket left in the three guides (the `C1` grep was replaced in the pre-review pass). Probe: the new regex matches `[D2]`, `- [ ]`, `🟡` and not a clean fixture file.

### Round 5 repair — one cluster (F1; requirements-promotion.md 16,987 → 16,987)

The `C7` bracket's command is now `grep -E '\[D[0-9]+\]|- \[[ x]\]|🟡'` (same length). Probed on literal input: matches `The reminder follows [D2].`, its definition line, `- [ ] T1 open` and `done 🟡`; the old pattern matched none of the first two; the new pattern returns nothing over a clean fixture draft (exit 1).

Self-check: no contradiction — `C7`'s rule ("no Discussion citations, checkboxes or `🟡` remain") is unchanged and the bracket now finds the current citation form; the authoring and artifacts guides' `[D<n>]` form is what the command tests. Stale text: grep `\(D\[0-9\]` → 0. Rule not moved. Nothing weakened: the confirmation still runs a repeatable command plus the read-back plus `validate`.

Sanity scan (requirements-promotion): Managed-Updated-At 2026-10-18; Gates and Advance intent present; supervisor definition present; `\bhuman` 1; `Next Command|checkpoint` 0; `🟡` 3; live `- [ ]` 0; `⏳ GATE` 8; fences 10; links unchanged.

Flow reflection (`C7` confirmation): write → read back → grep over the three written files finds a leftover `[D3]` in reminders.md → mechanical fault, `C7`'s, repaired in place (the citation removed, the draft untouched), re-run returns nothing → `validate skai/requirements` nothing beyond readiness's notes → `C7` checked. No issues found in simulation.

### Round 5 verification (tool md5 144c8081, stable)

- No tool claim changed; the regex probe above is the round's only new evidence. Caps: 16,987 / 12,800 / 11,500 / 449 / 449 / 500 = 42,685 of 42,700.

### Round 5 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 `C7` bracket's grep tested the legacy `(D#)` citation form | closed | Regex `\[D[0-9]+\]`; probed on literal input and a clean fixture file; stale original text, not a compression defect |
| Open: an item's last rule removed leaves valid numbering; `C1`'s opening clause covers rules, its named inspection says items | logged (first sighting) | spec-format 2 makes rules append-only; on recurrence "inspect that no item or rule is dropped or renumbered" (+16 bytes) |

Stop rule not met: round 5 produced a live finding and was repaired after. The round's finding was not a compression defect (the supervisor's classification question): it was original text that survived the link-style migration; full restatement cost 0. Consolidation trigger count: two (unchanged). Round 6 to be commissioned over the current text, series A, settled slot refreshed (routine).

## Supervisor Ruling After Round 5 (2026-10-18)

Round 5 accepted; no cap change. Round 6 commissioned over the current text, series A, settled slot refreshed (routine: the `C7` bracket closure, the logged rule case). Prompt `scratchpad/r6/prompt.txt`, diffed clean; report `scratchpad/r6/review-r6.md`.

## Round 6 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r6/prompt.txt` (diffed clean), report `scratchpad/r6/review-r6.md`, tool md5 144c8081 throughout. **No findings**: "No new findings recommended for acceptance, logging, or supervisor decision"; no open questions beyond the settled resumed-confirmation reading and the headroom note. The reviewer re-verified by implementation read the four tool claims the guides rest on (scoped validation, ID coverage including revived items, `check-changes` coverage and operations, render discovery and page naming) and the repaired `C7` command, and walked every requested branch of the three workflows and the wrappers without a strand.

### Finding matrix

No rows: nothing reported.

### Round score

> nothing scored — a clean fresh round over the current text

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 8.125 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r3 (A) | 8.75 | 2 | 0 | 2 | 0 | 1 |
| r4 (A) | 10.0 | 2 | 0 | 2 | 0 | 0 |
| r5 (A) | 5.0 | 1 | 0 | 1 | 0 | 0 |
| r6 (A) | 0 | 0 | 0 | 0 | 0 | 0 |

### Round 6 verification (tool md5 144c8081, stable)

No edit this round; the text the reviewer read is the text on disk. Caps: 16,987 / 12,800 / 11,500 / 449 / 449 / 500 = 42,685 of 42,700.

### Round 6 closure

| Finding | Disposition | Evidence |
|---|---|---|
| No live findings in the binding target | closed — clean fresh round | Stop rule (a): the round produced no new live finding; nothing was repaired after it |

### Maintenance retro (`internal/maintain-retro.md`, at pass close)

Inventory: six promotion files (three gated guides, three wrappers) brought to the 2026-10-18 decisions and shortened to their caps; README shape rows and design promotion prerequisites; one CHANGELOG `## Unreleased` entry with migration (sizes and the no-render-after-write rule brought current at close). Host-install-visible (guide content and wrapper descriptions). Bookkeeping: CHANGELOG entry carries migration for open packages and wrapper refresh; `assets.manifest.json` unchanged (ids, sourcePaths — all exist — and descriptions still correct; not touched by this pass); every edited managed file carries `Managed-Updated-At: 2026-10-18` (headers read); README Usage phases still match the gate behavior (readiness → unchecked checklist → gate → execute → archive; the design promotion prerequisites now name triaged requests); `internal/maintain-skai.md` unchanged (no new invariant). Consistency: README references to the three guides are markdown links (grep for bare-path mentions → 0); stale paths (`requirements-<nnn>`, `design-specs-<nnn>`, "promotion picks it up") across `Guides/` and README → 0; terminology drift (`Next Command`, `checkpoint`) in the six files → 0; each guide has its managed header and `## Gates` with the standard control model (diffed identical across the three); markers `- [ ]` only in skeletons and prose, `🟡` only in the compact block and check bullets; no discussion phases in these guides; no working-doc paths; wrappers are ten-line dispatchers; addendum footers and lookup names unchanged in all three guides. Change-package verification and guide-addendum contract recorded under "Dependents and bookkeeping" above and unchanged since. Retro complete; no misses found.

**Stop rule met (a):** round 6 was a fresh round over the current text with no new live findings in the binding target. Series A: r1 8.125 → r2 5.0 → r3 8.75 → r4 10.0 → r5 5.0 → r6 0. Consolidation trigger fired twice (r2 F2, r4 F2); the structured tier (P1–P5, ownership table, rule impact maps) applied from round 4 and held through rounds 5 and 6. Net size change 47,633 → 42,685 (−4,948) against the 42,700 group cap. Routed during the pass and since fixed in the tool: `add file` on a modified file (r2 F1), the revived retired ID (r3 F2's tool half); still with the tool pass by contract: rule entries matched through the parent item. Logged, not codified: root resolution step (r1 F6), design rollback scope (r3 F3, second sighting), last-rule removal (r5 open).

## Closure (2026-10-18)

Closure confirmed by the supervisor: target 4 closed with a clean round 6 at 42,685 bytes; no further rounds. Final sizes 16,987 / 12,800 / 11,500 / 449 / 449 / 500 against caps 17,000 / 12,800 / 11,500 / 450 / 450 / 500 (group 42,700). Nothing committed, deleted or pushed.
