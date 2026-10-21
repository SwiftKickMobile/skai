# Spec Authoring Guides Refinement

Working document for target 3: the authoring workflows of the three spec-bearing systems, refined together for fidelity and parallel structure. Standards: `skai/refinement-reviews/requirements-system-design.md` (P5, P7, P8, P10, Artifacts, Workflow § Authoring, Decisions 2026-10-18, Size Budgets, live render), `design-specs-design.md` (8, 9 as amended, Amendments 2026-10-18, live render), `design-process-design.md` (settled decisions incl. the superseded requirements-impact entry, Amendments 2026-10-18, Size Budgets, live render), `spec-format-design.md` (9–16). Read-only context: `Guides/Core/spec-file-shape.md`, `Guides/Requirements/requirements-catalog.md`, `requirements-artifacts.md`, `Guides/DesignSpecs/design-specs.md`, `design-specs-artifacts.md`, the three promotion guides. Findings log: `skai/refinement-reviews/spec-authoring-findings.md`. Tool: `Bin/spec-tool.py` (not edited; md5 4c147cd3 at start); fixtures: SalesPro `working-docs/requirements-process/fixtures/`.

| File | Start | Cap |
|---|---|---|
| Guides/Requirements/requirements-authoring.md | 23,012 | 20,500 |
| Guides/Requirements/requirements-baseline.md | 2,630 | 1,700 |
| Guides/DesignSpecs/design-specs-authoring.md | 16,971 | 15,500 |
| Guides/Design/design-authoring.md | 15,189 | 14,400 |
| Templates/skills/skai-requirements-authoring/SKILL.md | 468 | 450 |
| Templates/skills/skai-design-specs-authoring/SKILL.md | 617 | 450 |
| Templates/skills/skai-design-authoring/SKILL.md | 1,068 | 550 |
| Group | 59,955 | 53,550 |

## Dependents inherited from target 2 (`spec-content-findings.md`, working doc § Dependents)

- `requirements-authoring.md:33` package row `change-requests/requirements-<nnn>.md` → folders `change-requests/<nnn>/request.md`.
- `requirements-authoring.md:216-219`, `design-specs-authoring.md:171`: "raised by promotion" → filed by any downstream consumer; triage recorded on the request.
- `design-specs-authoring.md:274`: "changed text inline" → change items carry no inline text.
- `requirements-baseline.md:19`: "§ Root index" → the catalog guide's section is now `### Indexes route`.
- Review-page link at the top of the authoring artifact (new; no current text).

## Pre-review tool facts (2026-10-18, tool md5 4c147cd3)

- `validate catalog package/proposed-product-specs` → 6 files, 0 issues, 2 notes outside the projection (untouched `legacy-note.md`: missing statement, unlinked term), exit 0. Design fixtures: 9 files, 0 issues.
- `check-changes` on the fixture package → 0 issues, exit 0; on `broken-package` → 18 issues naming an unchanged item, an absent item, an absent rule, two operation mismatches (`add` on a modified item, `retire` on an added one) and every unlisted change, exit 1. The declared operation is checked (r4 ruling landed).
- `references STAGE-01` → the bracketed citations of the item and its rules across catalog and drafts, exit 0.
- `render` with `--out` only (no `--authoring`) finds `product-specs-authoring.md` beside the drafts; the page carries justifications. `render-request` on request 002 (no drafts) writes the page, exit 0.
- The docstring: `render` without `--out` writes `product-specs-review.html` / `design-specs-review.html` into the package folder; legacy `requirements-authoring.md` + `proposed-requirements/` accepted until the rename pass; a request's drafts are `proposed-product-specs/` or `proposed-design-specs/`.

## Pre-edit workflow models (gated guides; `gated-workflows.md` § Pre-edit workflow model)

### requirements-authoring.md

Happy path: signal → hosting (first catalog) → read catalog guide + catalog → reopen or create package (change ID or blocked gate) → infer mode (baseline guide) → drafts under `proposed-requirements/` + `## Discussion` seeded → blocked gate while items remain, items resolved one by one → pre-gate pass (`C1`–`C5`) → planned gate "Discussion complete" → Requirement Changes written → Assumptions/Out of scope → 🏁. Artifacts: `requirements-authoring.md`, `proposed-requirements/**`. Markers: `- [ ] D<n>` only, resolved per item on the supervisor's approval of that item; change items carry no checkbox; drafts carry none. Blockers: contradictory inputs, no change ID, prefix naming collision, file split; the generic blocked gate otherwise.
Target model (known deltas): drafting opens with the concept inventory — new or changed concepts are one Discussion item, app behavior waits for its resolution under the standing blocked gate (no new gate); `## Situations` optional after Goal; page link under the title; the change list maintained with the drafts and confirmed by `check-changes` pre-gate; pre-gate pass = `validate`, `C1`–`C5`, `check-changes`, one evidence line each; reference sweep before modify/retire, recorded; `validate` + `render` on every material change; change requests from any consumer, triaged on the request; the planned gate advances to Completion (assumptions, out of scope, final render, 🏁).
Simulations (pre-edit, on the target model): (1) normal — baseline backfill, inventory finds two new concepts → D1 `[Proposal]`, blocked gate "1 open item"; supervisor approves → `- [x] D1` + Decision, app subjects drafted end to end, D2–D4 seeded, blocked gate "3 open items"; all resolved → pre-gate pass with evidence → planned gate "Discussion complete. Say "next" to advance to Completion." → `next` → Completion → 🏁. (2) blocked/tooling — `validate` fails on a held draft (duplicate ID introduced by the package): the pre-gate pass records the failure under `## Verification`, the agent fixes the draft before gating (the gate presents what the supervisor reviews); a tool that cannot run (python missing) is the generic blocked gate. (3) ambiguity — a modify-vs-retire call that could go either way: Discussion item, blocked gate; the sweep runs after the decision. (4) `auto` — baseline with fully specifying inputs and no new concepts: no items, the pre-gate pass runs where the gate would be, the planned gate is bypassed, Completion, 🏁; with a new concept, `auto` stops at the blocked gate on D1.

### design-specs-authoring.md

Happy path: signal → hosting → content rules + specs + requirements + tool guide → reopen or create → infer mode → drafts screen by screen + Discussion → blocked gate while items remain (drawing items stay open until seen) → `V1`–`V10` with evidence → planned gate → Spec Changes → 🏁. Artifacts: `design-specs-authoring.md`, `proposed-design-specs/**`. Markers: `- [ ] D<n>` only. Blockers: contradictory inputs, no change ID, design file unreachable (`V5`), prefix naming call.
Target model: page link; the change list maintained with the drafts; pre-gate pass = `validate`, `V1`–`V10`, `check-changes`; reference sweep recorded; live validate + render; a requirements gap files a change request against the open product spec package or the catalog, held open as a Discussion item until triaged; change requests received are triaged on the request; planned gate advances to Completion.
Simulations: (1) normal — two screens drafted, D1 undrawn state, blocked; drawing made and seen → resolved; pre-gate pass → planned gate → Completion. (2) blocked — design file unreachable: `V5` cannot run, listed blocked gate. (3) ambiguity — a spec that narrows a requirement: change request filed, D item open until triage, blocked gate; `auto` does not pass it. (4) `auto` — fully specified baseline, no gaps: pass runs, gate bypassed, 🏁.

### design-authoring.md

Happy path: signal → tool guide → reopen or create → Discussion phase (items with recommendations, nothing drawn) → blocked gate → all resolved → planned gate → Mockups on the change page → Mockup review gate (non-standard: "approved" advances; feedback applied, decisions parked → Discussion gate) → Design Changes → 🏁. Artifacts: `design-authoring.md`, the change page. Markers: `- [ ] D<n>`; Design Changes no checkbox. Blockers: no change ID, tool cannot do what a draft needs.
Target model: a decision that changes or adds a product spec is filed as a change request (format cited from `requirements-artifacts.md` § Change Requests), never by editing that package; before the Mockup review gate, one trace pass over the change page (every drawn state ↔ a product spec; every package spec served or recorded out of scope), filing requests for gaps, linked under `## Assumptions and TODOs` until triaged; at completion name any request still `Proposed` — promotion waits for its triage.
Simulations: (1) normal — D1 pinned group approved, mockups drawn, trace pass clean, review gate, "approved" → Design Changes → 🏁. (2) blocked — a font the tool cannot load: listed blocked gate, supervisor resolves. (3) ambiguity — feedback at review changes what the product promises (a new sort rule): parked as D3, Discussion gate blocked; its Decision names request 002 filed against the product spec package; mockup updated next phase. (4) `auto` — never bypasses the Mockup review gate; `auto to mockup review` draws and stops there.

## Pre-review pass (known deltas, decided by the supervisor)

Clusters, one per file, each with self-check and sanity scan, then the post-edit flow reflection for the gated guides.

Deltas applied in every cluster: the review-page link under the artifact title; `validate` + `render` on every material change (cited from the artifacts guides, stated at the point of use in Artifact maintenance); the change list maintained with the drafts and confirmed by `check-changes` in the pre-gate pass; change requests from any downstream consumer, triaged on the request; the planned Discussion gate advances to a `## Completion` phase (assumptions, out of scope, final render, 🏁); the standard gate, advance-intent and marker blocks untouched (diffed against the promotion guides' copies: identical apart from the milestone names). Prose says "product specs" for the catalog; file, guide, skill and addendum names stay. The efficiency review the caps were derived from (SalesPro `working-docs/requirements-process/reviews/efficiency-3-authoring.md`) supplied the trim list; its items were applied where they survived the deltas.

### Cluster 1 — requirements-authoring.md (23,012 → 21,040; cap 20,500)

Added: `## Drafting` with *Concept inventory* (checked against the company's vocabulary, `domains/` and the glossary; new or changed concepts are one `[Proposal]` item resolved under the standing blocked gate before app behavior is drafted — no new gate; a clean inventory is recorded under Assumptions and TODOs; ❌/✅ LumenNotes Collaborator), `## Situations` (optional, after Goal), `## Verification` (evidence lines for the pre-gate pass and each reference sweep), the reference sweep in *Working a scoped change* (catalog citations re-pointed by drafting their file into the package; citations in other artifacts by a change request against them), the pre-gate pass as `validate` → `C1`–`C5` → `check-changes`, `## Requirement Changes` maintained from the first draft, `## Completion`, sibling artifacts updating freely, change requests from any consumer triaged on the request (naming the new package a valid request belongs to). The package table is replaced by a citation of the artifacts guide (which owns the tree); *Reopening* gathers the reopen rules; Cross-references dropped (the intro routes to the same guides). Trims from the efficiency review: rationale tails ("what stops one being waved through", "what a raw diff cannot reconstruct", "record of what the drafts take for granted"), the re-read-on-reopen and resolution restatements, the D2 Proposal example (D5 Tradeoff kept: it shows Options, Proposal and Why), skeleton glosses, diff semantics (cited from the artifacts guide), modify-vs-retire summary kept to one clause.

Self-check: no contradiction with adjacent text — the backfill rule now reads "once the concepts are confirmed … never interrupt drafting", which is the standard's two P7 sentences in order; the gate note, Artifact maintenance and Completion agree on when the pass and renders run; no contradiction with siblings — the artifacts guide's lifecycle wording (Incorporated condition, Proposed blocks) is restated only where authoring acts, the catalog guide owns modify-vs-retire and the blocking scope. No stale sentence: greps for `requirements-<nnn>`, "raised by promotion", "Written after the Discussion", "advance to Requirement Changes", "Cross-references" → 0. No rule moved from its point of use: the sweep sits in *Working a scoped change*, triage in *Reopening*, the pass in the gate note. Nothing weakened: "never the catalog file", "never interrupt drafting", "`Proposed` blocks promotion", "`auto` never bypasses the blocked gate" stand.

Sanity scan: Managed-Updated-At 2026-10-18 (header read) → ok; `## Gates` and `## Advance intent` present with the supervisor definition; `\bhuman` → 1, the standard definition (false positive); `Next Command|checkpoint` → 0; `🟡` → 3, all in the frozen progress-tracking block; `- [ ]` outside code → the item-line template and the lifecycle text only, letter-led; no aggregator sections; `⏳ GATE:` lines: the two Discussion lines, both traced to the one planned gate and its blocked form; no planned gate without an artifact (the authoring artifact, Discussion-only marker model); no marker clearing before a gate; `auto` behavior names the hard (blocked) gate; working-doc paths 0; stack terms 0; fences 4 (two blocks); links resolve (catalog, artifacts, promotion, baseline, shape, hosting). Over-long merged lines: checked after the last edit, none outside the frozen blocks and link lines.

### Cluster 2 — requirements-baseline.md (2,630 → 1,698; cap 1,700)

Three rules kept, rationale removed per the efficiency review ("three things go wrong", "nothing downstream catches it", the delegation failure list); "§ Root index" pointer dropped with the sentence that carried it (the catalog guide's section is now *Indexes route*; the rule names `_requirements.md` directly). Self-check: no contradiction (the authoring guide's step 5 still routes here; *Working a backfill*'s clause quoted verbatim); no stale text (grep "Root index", "nowhere else" → 0); nothing weakened — "never a predicted one", "authoring may not [be delegated]", "writes nothing in the package" stand. Sanity scan: Managed-Updated-At 2026-10-18 → ok; no gates (not a workflow); `\bhuman` 0; markers 0; fences 0; links resolve.

### Cluster 3 — design-specs-authoring.md (16,971 → 17,511; cap 15,500)

Added: page link, `## Verification` covering validation and the sweep, pre-gate pass `validate` → `V1`–`V10` → `check-changes`, `## Spec Changes` maintained from the first draft with no inline text, `## Completion`, live validate-and-render in Artifact Maintenance, the reference sweep in *Working a Scoped Change*, *Requirements Gaps* as a change request against the open product spec package or the catalog (format cited from `requirements-artifacts.md` § Change Requests; the gap is a Discussion item held open until triage, so the gate note's open-until bullet names it), change requests from any consumer triaged on the request, siblings updating freely. TOC dropped; skeleton glosses, the modes rationale, the duplicated drawing reminders, the audit restatement in Artifact Maintenance, the incoming-link repair restatement (the artifacts guide owns it) and the Initiation tool-guide gloss trimmed per the efficiency review.

Self-check: no contradiction — Initiation's audit paragraph still owns the audit entry; the gate note and Artifact Maintenance agree on the pass; *Requirements Gaps*, *What Earns an Item* and the gate's open-until bullet say the same thing about a gap item. No stale text: greps "Seed a requirements", "sibling", "changed text inline", "Spec Changes are written", "advance to Spec Changes" → 0. No rule moved: the sweep sits with modify-vs-retire, triage with reopen. Nothing weakened: "never quietly specify", "never edit that package", "stays open until the drawing exists and the agent has seen it" (gate note), "`Proposed` blocks readiness" stand.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; Gates and Advance Intent present with the supervisor definition; `\bhuman` → the standard definition only; terms 0; `🟡` → the frozen block only; `- [ ]` letter-led; no aggregators; gate lines: the two Discussion lines, one planned gate; marker clearing gated; `auto` names the blocked gate as hard; working-doc paths 0; stack: "Figma" as the tool-guide selector only; fences 4; links and anchors resolve (`#the-package`, `#change-requests` in both artifacts guides, `#modify-vs-retire`, `#what-counts-as-a-state`).

### Cluster 4 — design-authoring.md (15,189 → 14,439; cap 14,400)

Added: a decision that changes or adds a product spec is a change request against the change's open product spec package or the catalog, format cited from `requirements-artifacts.md` § Change Requests, never by editing it (Purpose names the boundary, *Resolution* owns the rule; the request is listed under Assumptions and TODOs until triaged); the trace pass before the Mockup review gate (every drawn state ↔ a product spec; every package spec served or recorded under Out of scope; gaps file requests), run again after feedback when nothing was parked; completion names any request still `Proposed` since promotion waits for its triage; sibling types update freely. Trims per the efficiency review: "tool-agnostic" and "every tool has named pages" sentences, the input list, the Phases paragraph that restated the feedback sequence (Mockups owns it; the gate note points at it), the D2 example, the second "changed" inventory line, Cross-references, the "nothing is drawn to make a proposal" restatement (Phases owns "Nothing is drawn"), the aggregator-section sentence.

Self-check: no contradiction — Phases, the gate note and Mockups now describe one feedback sequence with one owner; Purpose's "changes what the product promises" and Resolution's "changes or adds a product spec" name the same event. Design-process requirement 2 holds: the only dependency is the request format, by citation. No stale text (grep "Cross-references", "tool-agnostic", "named pages" → 0). No rule moved: the trace pass sits in Mockups where it runs. Nothing weakened: "Nothing is drawn" in Discussion, "never a workaround", "`auto` never bypasses the Mockup review gate" stand.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; Gates and Advance intent present; `\bhuman` → the standard definition only; terms 0; `🟡` → the frozen block only; `- [ ]` letter-led; no aggregators; gate lines: Discussion blocked/planned and the non-standard Mockup review line, each traced to the two planned gates; the Mockup review gate's `Next` states the exact supervisor response ("approved"); marker clearing gated; `auto` names both hard stops; working-doc paths 0; stack: "Figma" as the selector only; fences 6; links and the `#change-requests` anchor resolve.

### Clusters 5–7 — skill wrappers (468 → 443; 617 → 430; 1,068 → 549; caps 450 / 450 / 550)

Descriptions shortened; the design skill's two substantive bullets (tool-guide routing, hard boundaries) removed as logic the guide owns — the one instruction now says the guide names the tool guide to read before drawing. The multiple-sizes conditional lives in the Figma guide, which the design guide loads. Frontmatter names and guide paths unchanged. Sanity scan: not managed-header files; no gates; links are the guide paths, unchanged.

### Post-edit flow reflection (`gated-workflows.md` § Flow reflection)

requirements-authoring: (normal) inputs → inventory finds a new concept → D1 open → response ends `⏳ GATE: Blocked: 1 open items in Discussion. Resolve them to proceed to Completion.`; supervisor approves D1 → `- [x] D1` + Decision; subjects drafted end to end, `## Requirement Changes` current, page rendered each response; D2–D3 resolved → pre-gate pass (validate, C1–C5, check-changes) with evidence lines → `⏳ GATE: Next: Discussion complete. Say "next" to advance to Completion.` → `next` → Completion → 🏁. Artifact: the authoring artifact; markers: D items only, cleared per item on that item's approval; nothing clears at the planned gate. (blocked) `validate` fails on a held draft: fixed before gating; the tool absent: generic blocked line. (auto) no new concepts, no items: pass runs where the gate would be, gate bypassed, 🏁; with D1 open, `auto` stops at the blocked gate. No issues found in simulation.

design-specs-authoring: (normal) two screens, D1 undrawn state → blocked gate; drawing made and seen → resolved; pass → planned gate → Completion → 🏁. (blocked) design file unreachable → listed blocked gate. (auto) fully specified baseline: pass, bypass, 🏁; a requirements-gap item keeps the blocked gate until the request is triaged. No issues found in simulation.

design-authoring: (normal) D1 resolved → planned gate → mockups drawn → trace pass clean → `⏳ GATE: Next: Review the mockups on <change-id>. Say "approved" to write Design Changes, or give feedback.` → "approved" → Design Changes → 🏁. (blocked) a font the tool cannot load → listed blocked gate. (ambiguity) feedback changes a promise → parked D3, Discussion gate blocked; Decision names request 002; next mockup round applies it; trace pass before the review gate. (auto) stops at the Mockup review gate always. No issues found in simulation.

### Pre-review pass totals

| File | Before | After | Cap | Delta to cap |
|---|---|---|---|---|
| requirements-authoring.md | 23,012 | 21,040 | 20,500 | +540 |
| requirements-baseline.md | 2,630 | 1,698 | 1,700 | −2 |
| design-specs-authoring.md | 16,971 | 17,511 | 15,500 | +2,011 |
| design-authoring.md | 15,189 | 14,439 | 14,400 | +39 |
| skai-requirements-authoring skill | 468 | 443 | 450 | −7 |
| skai-design-specs-authoring skill | 617 | 430 | 450 | −20 |
| skai-design-authoring skill | 1,068 | 549 | 550 | −1 |
| Group | 59,955 | 56,110 | 53,550 | +2,560 |

Three files are over cap after the efficiency review's trims and three compression passes; the residual is the known deltas' growth exceeding the growth the caps allowed. Not cut silently — raised as a supervisor decision (see the report). The frozen standard blocks measure 2,232 (Gates) + 2,620 / 1,495 / 1,474 (Advance intent: requirements long variant; design-specs and design compact variant).

### Maintainer bookkeeping

Managed-Updated-At bumped to 2026-10-18 in the four guides. CHANGELOG `## Unreleased` gains one **Spec authoring guides** entry with migration steps for open packages and the wrapper refresh. README Usage: the three authoring entries' descriptions and phases updated (concept inventory, live change list and renders, request triage, the pre-gate pass, Completion; design: change requests and the trace pass; design specs: gap as a change request); the two Shape rows now say the authoring guides cite the shape guide. `assets.manifest.json` unchanged (no rename). Findings log created and seeded. Not done: no commit.

## Supervisor Rulings After The Pre-Review Pass (2026-10-18)

1. requirements-authoring.md adopts the compact Advance intent variant its siblings carry (the gated-workflows reference allows an explicitly declared compact control model preserving the invariants); design-authoring.md trims 39 rule-free bytes; design-specs-authoring.md applies the three rule-free candidates and its cap is provisionally 17,000 (design-specs-design Size Budgets updated, flagged to the human). Group cap 54,900.
2. `## Verification` approved for the product-spec authoring artifact; requirements-system-design § Authoring artifact lists it.
3. Design-spec change lists are maintained live; design-specs-design decision 9 says so. The two in-pass decisions (concept-inventory item under the blocked gate; design requests listed under Assumptions and TODOs until triaged) stand.

### Ruling cluster — compact block and residual trims

requirements-authoring.md 21,040 → 19,915: the `Progress tracking:` block is now byte-identical to the design-specs sibling's (diffed); the custom-lifecycle bullets and the "Not workflow progress" paragraph went with it, and the workflow-specific lifecycle paragraph below still declares the one marker, its per-item clearing on that item's approval, and that advance intent clears nothing — the persistence, approval and blocked-stop invariants are preserved by the untouched Gates block and the Rules list. design-specs-authoring.md 17,511 → 17,026: worked example replaced by one sentence naming the undrawn-state proposal form; the two `[evidence: …]` formats replaced by "in promotion's evidence form" (the promotion guide owns the bracket); the reopen paragraph replaced by a citation of requirements authoring § Reopening with `C3` for `C7` and the three rules it carries. design-authoring.md 14,439 → 14,394: "never both at once", "or equivalent" and the inventory's "from which promotion knows…" tail dropped.

Self-check: no contradiction — the compact block's four bullets are the invariants the long block stated, with the lifecycle paragraph carrying the custom exception; design-specs' Resolution still says "Follow the item approval/marker lifecycle in *Advance Intent*" and the lifecycle paragraph is unchanged; the reopen citation's anchor `#reopening` resolves to `### Reopening` in requirements-authoring. No stale sentence (grep "Not workflow progress", "custom marker lifecycle", "Reminder Badges", "evidence: V<n>", "UI-NOTES-02" → 0 in the three guides). No rule moved except by the ruling (reopen rules cited from the product spec guide, as design-specs-design's Guide Shape allows). Nothing weakened — markers still clear only on supervisor approval; the three reopen rules are restated in the citing sentence.

Sanity scan (three guides): Managed-Updated-At 2026-10-18 → ok; Gates and Advance intent present, supervisor definition present; `\bhuman` → the standard definition only (1 each); terms 0; `🟡` → 1 line each (the compact block); markers letter-led; aggregators 0; gate lines unchanged (8 / 8 / 9 occurrences incl. the template lines; each workflow line traced to a listed gate); fences 4 / 2 / 6; working-doc paths 0; stack: "Figma" selector only; links resolve incl. the new `#reopening` anchor.

Flow reflection after the control-model change (requirements-authoring): (normal) D1 open → blocked line → approved → `- [x] D1` + Decision under the lifecycle paragraph's per-item rule; all resolved → pre-gate pass → planned line → `next` → Completion; the compact block's "At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers" has nothing to clear, as the lifecycle paragraph says. (blocked) validate fails on a held draft → fixed before gating; tool absent → generic blocked line. (auto) no items → pass, bypass, 🏁; D1 open → stops at the blocked gate. No issues found in simulation.

| File | Now | Cap | Δ |
|---|---|---|---|
| requirements-authoring.md | 19,915 | 20,500 | −585 |
| requirements-baseline.md | 1,698 | 1,700 | −2 |
| design-specs-authoring.md | 16,998 | 17,000 | −2 (Initiation's context clause shortened after the first measure) |
| design-authoring.md | 14,360 | 14,400 | −40 |
| skills | 443 / 430 / 549 | 450 / 450 / 550 | under |

Round 1 commissioned over the current text with the deltas and the rulings in the settled slot. Series A: full cold review, Codex gpt-6-astra, standard charter, the seven files as the binding target, the four standards as the spec, the content, artifacts, shape, promotion, process-flow and Figma guides plus the tool and fixtures as non-normative context. Prompt `scratchpad/r1/prompt.txt`, diffed clean against the template block (slot replacements and the four deleted optional sections only; one drift — the settled-dispositions trailer — caught and restored before launch).

## Round 1 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r1/prompt.txt` (diffed clean), report `scratchpad/r1/review-r1.md`. Four findings, one open question.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 *Working a scoped change* says "copy each file out of the catalog" unconditionally, so a reopened package regenerates a draft from canon and loses earlier approved additions; the design-specs sibling says reuse existing drafts (parallel-structure drift; design-specs p1 r4 closed the same defect there) | accept | req-sys P5; requirements-authoring § What `proposed-requirements/` holds, § Working a scoped change | Initialization rule sharpened in *holds* ("reuse an existing draft; initialize a missing one by copying the catalog file, or fresh"); *scoped change* points at it | Whole-file drafting, carried content, re-read canon and recompute the list on reopen | +75 |
| F2 the sweep sends a stale citation "in another artifact" to "a change request against it", but only the two spec types take requests; a work spec or another package has no request lifecycle | accept | req-sys P8, P10; requirements-authoring § Working a scoped change | Per-citation disposition: catalog → draft the file; design specs → change request; work spec or other package → named in the sweep for its owner | The mandatory sweep; a disposition per citation; never editing another workflow's artifact | +112 |
| F3 the rendered page shows Discussion items as a table of titles, not their bodies or decisions, so the supervisor cannot resolve an item from the page alone (spec-format acceptance 4) | routed — standard / tool | spec-format 12 ("the discussion items as a table"); tool docstring rule 2 | Standard says a table; whether bodies render is the supervisor's call; tool pass if so | Markdown authoritative; the page the primary surface | 0 |
| F4 `check-changes` matches a rule entry to its parent item (`ok = found <= {"modified"}`), so a list naming the wrong rule or operation passes (re-raise of target 2 r1 F2 / r5 confirmation, already with the tool pass) | routed to the tool pass | spec-format 15; tool docstring ("an entry about a rule … names an item that shows as modified") | Tool: compare the typed target and operation | The guides' claim equals spec 15 | 0 |

Open question (neither): design-process-design's live-render sentence applies to "every workflow that writes a package", but no design-package render exists (the drafts are on the change page; request pages are the artifacts guide's) — a standard-level tension for the supervisor; the design guide invents no render.

### Round score

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875 · F3 outside the binding target (standard/tool), neither · F4 routed to the tool pass (re-raise of a routed item), neither

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 3.75 | 2 | 0 | 2 | 0 | 0 |

Who the findings are about: F1 is original wording (the pre-review pass kept the old "copy and edit" sentence); F2 is my pre-review sweep text. Consolidation trigger: not fired.

### Round 1 repair — cluster A (F1, F2; requirements-authoring.md)

19,915 → 20,102. *What `proposed-requirements/` holds*: "Reuse an existing draft; initialize a missing draft by copying the catalog file, or draft it fresh when the catalog lacks it." *Working a scoped change*: "Edit the draft under `proposed-requirements/` (initialized as *What `proposed-requirements/` holds* says), never the catalog file." and the per-citation dispositions: catalog → draft its file into the package; design specs → change request against them; work spec or another package → "not the author's to edit — name it in the sweep for that artifact's owner".

Self-check: no contradiction — *Reopening* still re-derives mode and change list from the catalog (a reused draft is compared afresh); the initialization rule has one home, mirrored by the design-specs sibling's wording (grep "Reuse an existing draft" / "Reuse existing drafts" → one each); no stale sentence (grep "Copy an existing file", "copy out of the catalog", "another artifact by a change" → 0); no rule moved — the sweep stays in *scoped change*; nothing weakened — "never the catalog file", the mandatory sweep and the proposer-never-edits boundary stand (now explicit for work specs too).

Sanity scan: Managed-Updated-At 2026-10-18 → ok; `\bhuman` → the standard definition only; terms 0; `🟡` → the compact block only; markers letter-led; gate lines unchanged (8 occurrences); fences 4; long lines: the artifacts link line and the footer only; links resolve; working-doc paths 0; stack 0.

### Round 1 verification (tool md5 e6180dd8 — the tool pass changed it during the round)

- No guide claim about the tool changed this round. The guides claim: `validate` on the projection with the content guides' blocking scope (verified at pass start: notes outside the projection, exit 0); `render` finds the artifact beside the drafts (verified at pass start); `check-changes` confirms the list matches the projection (verified: fixture package 0 issues, broken package 18 issues naming unchanged, absent, wrong-operation and unlisted entries); `references` lists citing file:line (verified).
- F4 premise confirmed from the tool's own docstring ("an entry about a rule … names an item that shows as modified"), consistent with target 2's reproduction; routed.
- F3: the tool docstring rule 2 and spec-format 12 both specify the discussion items as a table — the behavior matches the standard; whether it should show bodies is a standard question.
- Caps: 20,102 / 1,698 / 16,998 / 14,360 / 443 / 430 / 549 = 54,580 of 54,900 (20,500 / 1,700 / 17,000 / 14,400 / 450 / 450 / 550).

### Round 1 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 scoped change copied canon over existing drafts on reopen | closed | Initialization rule in *holds* mirrors the design-specs sibling; *scoped change* points at it; greps above |
| F2 sweep routed non-spec citations to a nonexistent request lifecycle | closed | Three dispositions by artifact; work specs and other packages named in the sweep for their owner |
| F3 review page shows item titles only | routed — supervisor (standard) / tool pass | spec-format 12 and the docstring agree on a table; acceptance check 4 asks for approval from the page alone |
| F4 `check-changes` rule entries match the parent item | routed to the tool pass | Re-raise of target 2 r1 F2 / r5; docstring confirms |
| Open: live-render sentence vs no design-package render | open question | Standard-level (design-process-design live render); no guide change |

Stop rule not met: round 1 produced live findings and was repaired after. Round 2 to be commissioned over the current text, series A, after the supervisor's rulings.

## Supervisor Rulings After Round 1 (2026-10-18)

Round 1 accepted. spec-format 12 amended: discussion items render in full on the page (tool pass implementing); design-process-design's live-render paragraph: a design package has no render of its own, the rule reaches it through the requests it files; F4 with the tool pass. Round 2 commissioned over the current text, series A, settled slot refreshed with the round-1 dispositions and the rulings (routine refresh). Prompt `scratchpad/r2/prompt.txt`, diffed clean.

## Round 2 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r2/prompt.txt` (diffed clean), report `scratchpad/r2/review-r2.md`. Five findings, three open questions. Mid-round, the human added a delta: the reference sweep applies to a modified or retired glossary entry as well as to an ID (`references <term>` lists every linked occurrence; tool pass implementing) — applied in cluster A as the same repair F2 asks for.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 promotion's worked `C1` bracket greps `^## ` headings while the shape is `###`, so it reports a pass over a dropped ID; authoring routes the operator to that example | routed to target 4 (requirements-promotion.md, read-only here) | req-sys P8; requirements-promotion § Promotion Checks example | Promotion pass: correct or replace the example | Single enumeration in promotion; authoring cites, never duplicates | 0 |
| F2 the sweep trigger named requirements, rules and table rows; P8 (and the new delta) require it before modifying or retiring a glossary entry too | accept | req-sys P8; requirements-authoring § Working a scoped change, § Concept inventory | "Before modifying or retiring an ID or a glossary entry, run `references` (the ID, or the term for every linked occurrence)"; the inventory points at the sweep for a changed entry | One concept Proposal and its blocked gate; per-citation dispositions; the glossary binds nothing | +153 |
| F3 design-specs' sweep delegated incoming-link repair to "draft every file whose links change" with no ownership boundary, while the product spec sibling distinguishes catalog / design specs / other artifacts (r1 F2 not swept across siblings) | accept | design-specs-design 9, Amendments; design-specs-authoring § Working a Scoped Change | The sibling's dispositions: spec citation → draft its file (Touches); product spec, work spec or other package → named in the sweep for its owner; glossary trigger added for parallelism | Scanning active packages; drafting affected canonical spec files in Touches | +~250, funded by five rule-free trims |
| F4 design: "The Decision names the request" assumed a Discussion item, but direct feedback and the trace pass file requests with no item | accept | design-process-design superseded entry; design-authoring § Resolution | "This holds in any phase — a Discussion decision, direct feedback, the trace pass — and every request is listed under Assumptions and TODOs until triaged; a Decision that produced one names it" | No item required for supervisor-directed mockup changes; *What earns an item* unchanged | +~110, funded by two trims |
| F5 `validate` marks cross-file conflicts "always block" (`cross` never gets the `outside` note), so a duplicate ID wholly between untouched canonical files blocks an unrelated package (spec-format 8 says only conflicts the projection introduces block) | routed to the tool pass | spec-format 8; tool `validate()` | Tool: classify a conflict confined to untouched canonical files as a note | Projection-introduced conflicts and held-file faults block | 0 |

Open questions (neither): the three standards still print the 53,550 authoring group cap (the supervisor set 54,900 — standard hygiene); a drawing-dependent item closes when the drawing is seen while `V5` wants an approved drawing (the later check catches it; a close/reopen cycle, not a wrong action); fixtures README historical notation (noise).

### Round score

> F1 outside the binding target (promotion guide), routed · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875 · F4 divergent · off-normal · speculative = 1.875 · F5 routed to the tool pass, neither

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r2 (A) | 5.625 | 3 | 0 | 3 | 0 | 0 |

Who the findings are about: F3 is the round-1 F2 repair not swept to its sibling — the consolidation trigger counts once (class not swept; the class — the sweep's per-citation dispositions — is now stated identically in both spec guides). F2 and F4 are pre-review-pass text (first statements of the sweep trigger and the design request record), not round repairs.

### Round 2 repairs — cluster A (F2 + delta; requirements-authoring.md 20,102 → 20,255)

Self-check: no contradiction — the catalog guide's modify-vs-retire still says "run `references`" for items; this guide widens the trigger per the amended standard, and the inventory's pointer sends a changed entry to the same sweep (one home); no stale sentence (grep "Before either" → 0); rule not moved; nothing weakened — the ID semantics ("retires it and adds a new one") stay on items, rules and rows, as the reviewer's churn guard asks.

### Cluster B (F3 + glossary trigger; design-specs-authoring.md 16,998 → 17,000)

Dispositions mirror the product spec guide word for word in structure; funded by: the inputs list, the branch example, the drawing-location sentence (the content guide's Product Language Only owns it), "production/approved-change" and "(modify, retire, move or add)" glosses, "Preserve original text" (the lifecycle's "appending" carries it), and a shorter reopen citation. Self-check: no contradiction — the artifacts guide's "Draft every file whose links a move or retirement changes" now reads under the ownership boundary stated at the point of use; grep "Before either", "incoming-link drafts ride", "drawing location" → 0; nothing weakened — incoming-link drafts in Touches stand.

### Cluster C (F4; design-authoring.md 14,360 → 14,396)

Self-check: no contradiction — Mockups' "filed as under *Resolution*" now lands on a rule that covers its path; *What earns an item* untouched; funded by the reopen clause, the no-items sentence and "the input's change ID"; grep "The Decision names" → 0.

Sanity scan (three guides): Managed-Updated-At 2026-10-18 → ok; Gates and Advance intent present; `\bhuman` → the standard definition only; terms 0; `🟡` → the compact block only; markers letter-led; aggregators 0; gate lines unchanged (8 / 8 / 9); fences 4 / 2 / 6; over-long lines: link lines and footers only; links resolve; working-doc paths 0; stack: "Figma" selector only.

### Round 2 verification (tool md5 29c50ce5 — changed again mid-round)

- F5 confirmed by implementation read: `cross = []  # whole-projection checks: always block` at `spec-tool.py:573`; the guides' claim ("what blocks is the content guide's") equals spec-format 8, so the tool is the stale side; routed.
- F1 confirmed: promotion's `C1` bracket greps `^## [A-Z-]+-[0-9]+`; the shape guide's items are `###`. Routed to target 4.
- No guide claim about the tool changed this round beyond `references <term>`, which the human's delta assigns to the tool pass (not yet runnable: `references` takes an ID; noted for round close of the tool pass).
- Caps: 20,255 / 1,698 / 17,000 / 14,396 / 443 / 430 / 549 = 54,771 of 54,900.

### Round 2 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 promotion's `C1` example greps `##` | routed to target 4 | Example text vs the shape guide; authoring only cites |
| F2 sweep trigger omitted glossary entries | closed | "an ID or a glossary entry"; inventory points at the sweep |
| F3 design-specs sweep had no ownership boundary | closed | Dispositions now parallel in both spec guides |
| F4 design request record assumed a Decision | closed | Any phase; Assumptions list is the record; a Decision names it when one exists |
| F5 untouched canonical conflicts block | routed to the tool pass | `cross` never noted as outside |
| Open: standards print 53,550 | open question | Standard hygiene for the supervisor |

Stop rule not met: round 2 produced live findings and was repaired after. Consolidation trigger count: one. Round 3 to be commissioned over the current text, series A.

## Supervisor Ruling After Round 2 (2026-10-18)

Round 2 accepted; the standards print the 54,900 authoring group cap; F1 noted for target 4; F5 with the tool pass (cross-file conflicts block only when a draft is one side). Round 3 commissioned over the current text, series A, settled slot refreshed (routine). Prompt `scratchpad/r3/prompt.txt`, diffed clean.

## Round 3 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r3/prompt.txt` (diffed clean), report `scratchpad/r3/review-r3.md`. Two findings, both in design-specs-authoring.md; no open questions beyond noise.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 the design-specs sweep's roots omitted the product catalog and grouped a product-spec citation with "named for its owner", against the settled parallel disposition (other spec type → change request); my round-2 cluster B text | accept | design-specs-design 1 and 9 (amended), req-sys P8; design-specs-authoring § Working a Scoped Change | Roots: the specs, the product catalog, the active packages; dispositions mirrored from the product spec guide, the product-spec case routed through *Requirements Gaps* | Whole-file drafting of affected spec files in Touches; owner-only handling of work specs and other packages; never editing the product spec package | +~130, funded by three rule-free trims |
| F2 "New specs require the root index, glossary and all three folder indexes" read as a per-screen obligation, pulling unchanged index files into the package and its blocking scope; the product spec sibling says "A new catalog needs" | accept | design-specs-design 5 (all three folders from the start); design-specs-authoring § What `proposed-design-specs/` Holds | "A new specs root needs …" | Root creation still carries all three folder indexes; ordinary additions still hold every index or glossary file they change, whole | +9, funded by two trims |

### Round score

> F1 divergent · normal · verified = 5 · F2 divergent · normal · speculative = 2.5

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r2 (A) | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r3 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |

Who the findings are about: F1 is my round-2 repair (the mirrored sweep paragraph) — my fix in one round became the next round's finding. With r1 F2 → r2 F3 counted once, **the consolidation trigger has fired twice**; per the refinement guide the problem is the editing method, so this round's repairs move to the structured tier below. F2 is original wording.

### Structured tier

**Invariants** (properties a repair must not break):
- I1 — The reference sweep is stated once per spec guide with the same four parts: trigger (modify or retire an ID or a glossary entry), roots (own canon, the other spec system, the active packages), dispositions (own canon → draft the file into the package; the other spec type → change request against it; a work spec or another package → named in the sweep for its owner), record (under `## Verification`).
- I2 — Package contents: touched files only, each whole; reuse an existing draft, initialize a missing one from canon, draft fresh what canon lacks; only the package that creates the root carries the root index, glossary and folder indexes as a set.
- I3 — A change request filed by a workflow is recorded in that workflow's artifact until triaged (design: Assumptions and TODOs; design specs: the gap's Discussion item) and never edits the target package.
- I4 — The three guides state a shared mechanic the same way or cite the same owner (parallel structure).

**Canonical ownership** (content → owner → derivative surfaces):
- Sweep rule → requirements-authoring § Working a scoped change → design-specs-authoring § Working a Scoped Change (mirror with the spec types swapped); the content guides' Modify vs. retire say only "run `references` and decide per citation" (consistent, no dispositions); the shape guide's command table (consistent).
- Initialization rule → requirements-authoring § What `proposed-requirements/` holds → design-specs-authoring § What `proposed-design-specs/` Holds; design-specs.md § Layout "Create all three folders and indexes immediately" (consistent).
- Request record → design-authoring § Resolution (any phase; Assumptions and TODOs) → design-specs-authoring § Requirements Gaps (Discussion item linking the request) — different vehicles by design, both satisfy I3.

**Rule impact map:**
- F1 violates I1 (roots, dispositions) and I4. Owner: requirements-authoring (unchanged, already correct). Dependents by grep `references\`\|the sweep` over Guides: design-specs.md:139 (consistent), requirements-catalog.md:149 (consistent), requirements-authoring.md:202/232/236 (owner), design-specs-authoring.md:194–198 (repaired). After the repair the grep returns a consistent set: both authoring guides carry the same three dispositions (grep "by a change request against them" → one hit each; "name it in the sweep for" → one hit each).
- F2 violates I2 and I4. Owner: requirements-authoring:47 "A new catalog needs" (unchanged). Dependents by grep `New specs require\|new catalog needs\|three folder indexes\|all three folders`: design-specs.md:62 (consistent), design-specs-artifacts "Root creation is one entry" (consistent), design-specs-authoring.md:33 (repaired to "A new specs root needs").
- Class sweep: every mechanic the two spec guides share was re-read side by side after the repairs — package rules, skeleton, modes, gate notes, lifecycle, reopen/triage, sweep, Discussion schema, change list, Completion, Artifact maintenance — for a statement present in one and absent or different in the other without a reason. Found none beyond F1 and F2.

### Round 3 repairs — cluster F1 (design-specs-authoring.md 17,000 → 17,002)

Self-check: no contradiction — *Requirements Gaps* already owns the change-request route the sweep now points at; no stale sentence (grep "supervisor assigns", "supervisor-approved", "Questions/Open Items" → 0); rule not moved; nothing weakened — "not the author's to edit" still covers work specs and other packages. Funded by: "the supervisor assigns the work" (the design package route already names who does it), "supervisor-approved" (promotion's own gate says so), "aggregate them into Questions/Open Items sections" → "in aggregator sections" (the sibling's word).

### Cluster F2 (design-specs-authoring.md 17,002 →    16990)

Self-check: no contradiction — "Mirror only touched paths" now governs ordinary additions and the root clause names the one package it binds; grep "New specs require" → 0; nothing weakened — a new root still carries all five files. Funded by "draft both, then revisit the first" (the efficiency review's own wording) and "check its paths and create the artifact".

Sanity scan (design-specs-authoring): Managed-Updated-At 2026-10-18 → ok; Gates and Advance Intent present; `\bhuman` → the standard definition only; terms 0; `🟡` → the compact block only; markers letter-led; aggregators 0; gate lines unchanged (8); fences 2; over-long lines: link lines and the footer only; links and anchors resolve; working-doc paths 0; stack: "Figma" selector only.

### Round 3 verification

- Tool md5 38a60dcc at round close. `references REMIND-04 <design-catalog> <catalog>` over two roots returns the design-spec citation at `screens/notes.md:16`, exit 0 — the guide's "over the specs, the product catalog and the active packages" is a multi-root call the tool accepts (its docstring: `references ID ROOT [ROOT ...]`). `references <term>` is the tool pass's (settled).
- No other guide claim about the tool changed this round.
- Caps: 20,255 / 1,698 /    16990 / 14,396 / 443 / 430 / 549 = 54761 of 54,900.

### Round 3 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 design-specs sweep roots and product-spec disposition | closed | Roots and three dispositions parallel to the product spec guide; multi-root `references` run |
| F2 "New specs require" per-screen reading | closed | "A new specs root needs"; owner wording unchanged |

Stop rule not met: round 3 produced live findings and was repaired after. Consolidation trigger: fired twice; structured tier applied from this round on. Round 4 to be commissioned over the current text, series A.

## Supervisor Ruling After Round 3 (2026-10-18)

Round 3 accepted; the structured tier stays. Round 4 commissioned over the current text, series A, settled slot refreshed (routine). Prompt `scratchpad/r4/prompt.txt`, diffed clean.

## Round 4 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r4/prompt.txt` (diffed clean), report `scratchpad/r4/review-r4.md`. Two findings (one tool, one log-only), two open questions.

### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 the renderer installs the authoring artifact's link definitions, then `set_resolver(new.linkdefs, draft.resolve())` per draft and renders Discussion afterwards without restoring them, so an authoring link such as `[request][request-001]` resolves against the last draft's definitions (unlinked or wrong) | routed to the tool pass | spec-format 12 (amended: items render in full); tool | Preserve the source document's link context per rendered section | Reference-style links; automatic artifact discovery; the page as the primary surface | 0 |
| F2 "Infer mode; read *Working a Baseline* before code" is not conditioned on Baseline in the sentence (the sibling says "Baseline: read …"); the heading carries the condition | log only (reviewer's triage; single observation, no strand) | design-specs-authoring § Initiation step 4 | On recurrence: "Infer mode; if Baseline, read *Working a Baseline* before code" (+13) | Mode inference; root-creation rule | — |

Open questions (neither): the no-delegated-authoring rule lives in the baseline guide, which a scoped product-spec author never loads (settled in the 2026-09-28 baseline pass: relocation priced out; design specs state it directly) — a standards-level placement question; `## Situations` is not parsed or rendered by the tool and the package-page standard (spec-format 12) omits it — how the product manager's confirmation reaches the page is a standard question for the supervisor.

### Round score

> F1 outside the binding target (tool), routed · F2 log-only, noise — no live defect in the seven files

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r2 (A) | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r3 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 (A) | 0 | 0 | 0 | 0 | 0 | 1 |

Who the findings are about: neither is a repair of mine (F1 tool; F2 original wording). No guide text changed this round.

### Round 4 verification

- F1 premise confirmed in the implementation (`set_resolver(new.linkdefs, draft.resolve())` inside the per-draft loop; `render_discussion_item` called after `render_tree`); routed. Tool md5 at close recorded in the findings log.
- `Situations` does not appear in the tool (grep → 0); spec-format 12's page omits it — standard-level, not a guide defect.
- Caps unchanged: 20,255 / 1,698 / 16,990 / 14,396 / 443 / 430 / 549 = 54,761 of 54,900.

### Round 4 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 renderer loses the authoring artifact's link context | routed to the tool pass | Implementation read (reviewer and refiner) |
| F2 baseline dispatch not conditioned in the sentence | logged | Single observation; the heading carries the condition; sharpen on recurrence (+13 bytes) |
| Open: delegation rule's placement; Situations on the page | open questions | Standard-level, for the supervisor |

**Stop rule (a) met:** round 4 is a fresh round over the current text with no new live finding in the binding target (F1 routes to the tool pass; F2 is logged without a guide change), and nothing was repaired after it. Convergence by clean round. Series A: 3.75 → 5.625 → 7.5 → 0. Sizes 59,955 → 54,761 (group cap 54,900). No supervisor-decision finding remains unimplemented. Awaiting closure.

## Pass Closed (supervisor, 2026-10-18)

Closure confirmed: target 3 closed with a clean round 4 at 54,761 bytes (20,255 / 1,698 / 16,990 / 14,396 / 443 / 430 / 549 against 20,500 / 1,700 / 17,000 / 14,400 / 450 / 450 / 550; group 54,900). Round-4 F1 is with the tool pass; Situations rendering is now spec-format decision 12 (tool pass); the no-delegated-authoring sentence goes to the consistency pass. Every finding of the pass carries a disposition with evidence or rationale in the round closure tables above: closed — r1 F1, F2; r2 F2, F3, F4; r3 F1, F2. Routed — r1 F3 (standard, then tool), r1 F4, r2 F5, r4 F1 (tool pass); r2 F1 (target 4). Logged — r4 F2. Open questions resolved by rulings — Discussion bodies on the page, design-package live render, the 54,900 group cap, Situations on the page, the delegation sentence (consistency pass). Net size change 59,955 → 54,761 (−5,194). No further rounds.
