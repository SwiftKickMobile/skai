# UI Map System — Findings Log

Target: the UI Map guides under `Guides/UIMap/` (in May 2026 `ui-map-planning.md` and `ui-map-implementation.md`, split 2026-06-03 into `ui-map-architecture.md` and `ui-map-implementation.md` with their artifact guides; the format guide, demo, and the SwiftUI and Compose references and placeholder guides) and the renderer, schema and viewer under `Bin/`. Standard: [`ui-map-system-design.md`](ui-map-system-design.md), backfilled 2026-10-19; the May passes were judged against the lost `docs/ui-map-skill-plan.md`.

Consolidated 2026-10-19 from three records. The May 2026 passes lived in the host checkout's working docs, `skai/working-docs/main/ui-map-planning-refinement/ui-map-planning-refinement.md` (the first pass's finding matrix, clusters, decisions and closure table) and `skai/working-docs/main/ui-map-planning-coverage.md` (the across-pass coverage map, appended at each closure through 2026-05-23). The September 2026 Compose pass was committed as `refinement-reviews/ui-map-compose-findings.md` at `c69a3e0` (2026-09-03) on branch `work/uimap-cmp`, which never merged into `main`. Content is preserved; the coverage map's row groups, which it separated with blank lines, are one table here.

## Pass 1 — 2026-05-19 (planning guide, first cold review)

Carried from `ui-map-planning-refinement.md`. Refinement pass on `Submodules/skai/Guides/Dev/ui-map-planning.md`, based on a cold review of the guide against `docs/ui-map-skill-plan.md`, following `Submodules/skai/Guides/Process/skill-refinement-guide.md`.

**Context**

- Guide under refinement: `Submodules/skai/Guides/Dev/ui-map-planning.md` (125 lines, freshly authored, never used in a real session)
- Design spec (standard): `docs/ui-map-skill-plan.md`
- Cold review: fresh-session review of the guide against the spec
- Reviewer verdict: Needs revision before use. Two blockers (B1, B2), four should-fixes (S1–S4), six minors (M1–M6)

**Finding matrix**

| ID | Finding | Triage | Touches (spec § + guide §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|---|
| B1 | Phase-1 described as two STOPs both labeled "Phase-1 gate"; advance-intent at the after-draft STOP is undefined | accept | spec §"The plan document" (one Phase-1 gate); guide ll. 77, 81, with 38–39 / 45 | Adopt skai's planning-draft-gate framing: the after-draft STOP is a review/handoff where `next` means "start walking through the items"; the *advancing* Phase-1 gate fires only when all `- [ ]` items have resolved. | Single-advancing-gate semantics; `auto`'s unresolved-items rule; the marker protocol |
| B2 | Audit path not runnable from this guide alone — no instructions for performing detection; the conformance dimensions are listed as a closed taxonomy but their conventions live in the platform reference | accept | spec §"Skills" (audit entry situation); guide ll. 75, 83–90 | In "Conformance detection," direct the agent to load the relevant platform reference (`ui-map-swiftui.md` / `ui-map-compose.md`); state that detection compares code against the map *and* against that reference's folder-org / file-layout / naming / route-kind / platform-pattern conventions. Cite `docs/ui-map.audit.md` as a worked-shape example. | Detection-scope rule (request-driven or opportunistic, never a standard step); placeholder spec stays out (build-sequence step 3) |
| S1 | Working-doc path underspecified — session-name, subpath, and full path not stated | accept | guide l. 18 | Mirror `work-spec-creation.md` File Naming Convention: session-name = the plan's `<name>`; subpath: none; full path: `working-docs/<branch-path>/<name>/<name>-plan.md` | Plan-document-as-working-doc convention |
| S2 | Render invocation not specified — no command, script path, or output statement | accept | guide l. 102 | Either give the command path or defer to `docs/skai/integration.md` per skai's "don't invent commands" rule; name the SVG as the review surface | Render performs schema + semantic validation in one pass |
| S3 | "One consolidated, high-level proposal" conflicts with marker-count rule (reads as one `- [ ]` for an audit with many findings) | accept | guide l. 75 vs l. 70 | Clarify: each audit finding gets its *own* `- [ ]` Proposal item; "consolidated" means only that Phase-2-level enumeration (file lists, move tables) is suppressed in Phase 1 | Marker-count = real-decisions rule; individual per-item resolution |
| S4 | Agent never instructed to load `ui-map-guide.md` at the point of editing the map; also doesn't say where to find `ui-map.yaml` | accept | guide ll. 3, 101 | In Phase 2, direct the agent to `ui-map-guide.md` for the YAML format at the point of edit; for `ui-map.yaml` location, defer to the integration doc | Companion-doc framing; in-place YAML edit (working-tree diff is the artifact) |
| M1 | "Map leads, code follows" invariant + "audit's Discussion is the sanctioned exception" never stated in the guide | accept | spec §"Architecture"; guide (not stated) | Add one sentence stating the invariant and the audit-Discussion exception | None — additive |
| M2 | "## Phase 1 → Phase 2" section is one near-empty sentence overlapping Phase 2 intro | accept | guide ll. 92–94 | Fold into Phase 2; remove the separate heading | Phase 2 content |
| M3 | "pure conformance audit" used without definition | accept | guide l. 104 | One clause: an audit where every finding resolves as a code fix, zero map changes | Behavior in that case (no diff; current render shown as conformance target) |
| M4 | Mapping resolved finding → entry type not explicit (code fix → `conformance /`; map fix → `modify`/`add`) | accept | guide l. 75 | One clause spelling the mapping | Audit-findings-as-proposal; typed-entry taxonomy |
| M5 | Skeleton has `## Out of scope` but body never connects the deferral path to it | accept | guide skeleton + l. 88 | Say deferred opportunistic conformance items land in `Out of scope` | Deferral semantics (agent does not silently expand scope) |
| M6 | How the render is "presented" at the gate unspecified (inline Mermaid vs SVG path) | accept | guide l. 106 | State the SVG path is cited at the gate (the human opens it externally) | Render-as-review-aid role |

**Triage summary:** 12 findings, all `accept`. None `human decision` — none of the fixes add process weight (no new gate, mirror field, checklist, proof burden, validation, wrapper, or repeated re-approval). None `reject`. None contradict the design spec; all are content/clarity gaps in the guide.

**Repair clusters** — group order A → B → C → D. A and B touch load-bearing semantics; C and D are localized clean-ups.

- Cluster A — Gate semantics: B1
- Cluster B — Audit runnability: B2, S3, S4, M4
- Cluster C — Phase 2 operational detail: S1, S2, M6
- Cluster D — Tightening clarifications: M1, M2, M3, M5

**Decisions**

- S3 — audit marker count (2026-05-19): one `- [ ]` for the entire consolidated audit proposal; the human approves it as a whole or amends specific findings inline before approval. Rationale: audit is mostly mechanical, so per-finding markers would force rubber-stamping. Revisit if the single-marker model proves insufficient. Plan doc updated to make this explicit. *(Reversed 2026-05-20; see the coverage map below.)*

**Closure table**

| ID | Status | Evidence |
|---|---|---|
| B1 | closed | Cluster A: Gates section disambiguated "Phase-1 gate" into advancing-gate + review/handoff stop; Phase 1 section and `auto` clause updated. |
| B2 | closed | Cluster B: "Performing detection" paragraph added in Conformance detection — directs agent to the platform reference for the conformance dimensions. |
| S1 | closed | Cluster C: working-doc path spelled out per work-spec-creation pattern (`working-docs/<branch-path>/<name>/<name>-plan.md`). |
| S2 | closed | Cluster C: render invocation deferred to `docs/skai/integration.md`; SVG named as the review surface. |
| S3 | closed | Cluster B: audit-findings line now states one `- [ ]` for the consolidated proposal; plan doc updated to match. |
| S4 | closed | Cluster B: Phase 2 step 2 now points to `ui-map-guide.md` for format and to `docs/skai/integration.md` for `ui-map.yaml` location. |
| M1 | closed | Cluster D: invariant ("map leads, code follows" + audit-Discussion exception) stated in Purpose. |
| M2 | closed | Cluster D: "Phase 1 → Phase 2" standalone section folded into the Phase 2 intro. |
| M3 | closed | Cluster D: "pure conformance audit" defined inline at point of use. |
| M4 | closed | Cluster B: finding-resolution → entry-type mapping (`conformance /` vs `modify`/`add`) made explicit. |
| M5 | closed | Cluster D: deferred opportunistic-conformance items now explicitly land in `Out of scope`. |
| M6 | closed | Cluster C: SVG named as review surface; path cited at the gate so the human can open it externally. |

## Coverage map — 2026-05-19 to 2026-05-23 (planning guide, all passes)

Carried from `ui-map-planning-coverage.md`: the across-pass record of findings and their dispositions, consulted at triage time of subsequent passes to prevent relitigation and to operate the recurrence threshold. The cold review itself was not given this map — a cold review must stay fresh; the refining agent consulted it during triage. Entries were appended at the closure step of each refinement pass. "SalesPro" names the host project whose validation runs surfaced the finding.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-05-19 | B1 — Phase-1 described as two STOPs both labeled "Phase-1 gate"; advance intent at after-draft STOP undefined | closed | Gates section disambiguated into advancing-gate + review/handoff stop |
| 2026-05-19 | B2 — Audit path not runnable from guide alone; conformance dimensions defined only in platform reference | closed | "Performing detection" paragraph added with platform-reference pointer |
| 2026-05-19 | S1 — Working-doc path underspecified | closed | Full path spelled out per work-spec-creation pattern |
| 2026-05-19 | S2 — Render invocation not specified | closed | Deferred to `docs/skai/integration.md`; SVG named as review surface |
| 2026-05-19 | S3 — "Consolidated, high-level proposal" conflicts with marker-count rule | closed | Single `- [ ]` per audit made explicit; plan doc updated to match |
| 2026-05-19 | S4 — `ui-map-guide.md` not loaded at Phase 2 edit; `ui-map.yaml` location not stated | closed | Phase 2 step 2 points to guide for format and integration doc for location |
| 2026-05-19 | M1 — "Map leads, code follows" invariant never stated | closed | Stated in Purpose, with audit-Discussion exception |
| 2026-05-19 | M2 — "Phase 1 → Phase 2" section near-empty, overlaps Phase 2 intro | closed | Folded into Phase 2 intro |
| 2026-05-19 | M3 — "Pure conformance audit" used without definition | closed | Defined inline at point of use |
| 2026-05-19 | M4 — Mapping from resolved finding to entry type not explicit | closed | Explicit mapping added to audit-findings line |
| 2026-05-19 | M5 — Skeleton has "Out of scope" but body never connects deferrals | closed | Deferred opportunistic-conformance items now land in `Out of scope` |
| 2026-05-19 | M6 — Render presentation at the gate unspecified | closed | SVG path cited at the gate for external opening |
| 2026-05-19 | Planning method lacks a "defer" resolution direction for findings implying real refactor/feature implementation — surfaced by SalesPro audit validation run (findings 4, 5) | closed | Added **defer to map todos** as a third resolution direction in `docs/ui-map-skill-plan.md` (Planning method §) and `Submodules/skai/Guides/Dev/ui-map-planning.md` (Phase 1 audit-findings line). |
| 2026-05-19 | `- [ ]` resolution rule was wrong — both planning-method guides instructed "replace inline, no `[x]`"; the correct rule is standard markdown check-off (`- [x]`). Surfaced by SalesPro audit validation run (agent removed marker instead of checking it). | closed | Plan doc and planning guide updated to "check the box (`- [x]`); item text may also be edited to read as the resolved decision." Stale "no `- [ ]` items remain" phrasing in the Completeness sentence fixed for clarity. |
| 2026-05-19 | Change-entry format under-specified for bundled operations — multi-operation entries were written as prose, burying per-operation detail. Surfaced by SalesPro audit Phase 2. | closed | Plan doc and planning guide updated: one identity per entry; multiple operations of the same kind under one identity become a sub-list under Description, one bullet per operation; avoid burying prose. |
| 2026-05-19 | Change-entry header capitalization and sub-bullet separator unspecified — entry headers began with lowercase and sub-bullets used `**Label** — value` em-dashes redundant with the bold label. Surfaced by SalesPro audit Phase 2. | closed | Planning guide template now specifies: capitalize the leading type word in the header (`Add`, `Modify`, `Conformance`); sub-bullet field labels are bold with no separator after the label. |
| 2026-05-20 | SwiftUI reference carried project-specific content — `.modal` and `.swiftMessage` rows in the modal-routing table belong to SalesPro overlay patterns, not standard SwiftUI. Surfaced by SalesPro audit dry-run when Phase 2 produced a "tighten the SwiftUI guide" Out-of-scope item. | closed | Dropped non-standard rows from `ui-map-swiftui.md`; updated code example to standard modifiers only; added paragraph directing projects to declare non-standard styles in their own `modal_styles` vocabulary and document them in `README.md` under a **Modal Styles** section. |
| 2026-05-20 | Audit method had no mechanism for project-declared conventions and overrides — input set didn't include the project's `README.md`, and the Source taxonomy had no value for project-authoritative rules. The skill couldn't represent "this project's README defines style X" as either an audit input or a justification. Surfaced alongside the SwiftUI cleanup. | closed | Added `Project convention` to the Source taxonomy in `ui-map-planning.md` and `docs/ui-map-skill-plan.md` (authority = project `README.md` or equivalent); extended "Performing detection" to load the project README and compare code against (c) README-declared conventions and overrides; a missing or stale README section for a non-standard pattern in code becomes its own finding. |
| 2026-05-20 | Phase-1 audit findings contained execution detail — fresh-session audit's finding D wrote "Split into one PR per domain to keep diffs reviewable; bundle each domain's pbxproj updates with that domain's moves" inside the Resolution field. | closed | Added rule to the Audit drafting bullet: "Findings state what changes and why; how to execute belongs to the implementation method." Stated as a principle, not an enumeration of forbidden examples. |
| 2026-05-20 | Audit proposal enumerated a conformant scene as a "positive baseline" finding (fresh-session finding I) — doesn't fit the approve-as-whole / amend-inline model since there is nothing to amend, and adds noise. | closed | Added rule to the Audit drafting bullet: "Findings are deviations only; conformant scenes are not enumerated." |
| 2026-05-20 | Audit proposal internal structure unspecified — fresh-session agent improvised letter prefixes, italic field labels with periods, and resolution-category subsections (workflow-shaped grouping the guide warns against in Phase 1). | closed | Added an inline "Audit proposal example" to `ui-map-planning.md` directly under the Audit drafting bullet: letter prefixes (`A`, `B`, …), bold field labels with no separator (matching the Change-list convention), one-line titles, flat ordering by resolution direction (map fixes → code conformance → defers), defer pointer in both the finding and `Out of scope`. |
| 2026-05-20 | Agent unilaterally expanded the input set — pulled `docs/ui-map.audit.md` (a pre-skill prose audit not listed in the invocation) into the audit as a load-bearing source. Caused 8/9 findings to be inherited rather than re-derived, and propagated a stale recommendation (skai-guide tightening for `MessageRoute`) that the prior cleanup had already obsoleted. Undermined cold validation of the skill. | mitigated | Hard-deleted `docs/ui-map.audit.md` and the prior dry-run plan to remove the crutch. Skill-side codification (rule on handling unsolicited files / scope expansion) intentionally deferred — re-evaluate after the next cold rerun: if the agent scope-expands into a different file under cold conditions, the behavior generalizes and warrants a rule; if not, the deletion was sufficient. |
| 2026-05-20 | Code-organization rule for `common:` scenes lived in `ui-map-guide.md` (platform-agnostic) — it specifies a `Scenes/` folder/package convention, which is platform-specific. Surfaced by the cold-rerun audit (finding C3 cited the rule correctly but the rule belonged in the platform refs). | closed | Removed the line from `ui-map-guide.md`'s Common scenes section; added the equivalent paragraph to both `ui-map-swiftui.md` (`Scenes/` folder) and `ui-map-compose.md` (`Scenes/` package) in their Scene file layout sections. |
| 2026-05-20 | `Out of scope` section duplicated defer findings — defers appeared as full findings in Discussion AND as one-line pointers in Out of scope. Surfaced by the cold-rerun audit (Out of scope was only a restatement of D1, D2; no other content). | closed | Defers now live in Discussion only as findings with resolution = defer. Removed "lands in `Out of scope`" from the defer description; narrowed Out of scope to "scope boundaries the plan deliberately doesn't address; may be empty"; updated the audit-example trailing sentence to drop the duplication. |
| 2026-05-20 | Audit proposal grouped findings by resolution category in subsection headers (`### Map fixes`, `### Code conformance`, `### Defers`) despite the structural decision being flat. The example's trailing "ordered map fixes → code conformance → defers" was interpreted as license to make those headers. | closed | Strengthened the example's trailing sentence: "Flat list of findings under the single Proposal item — no resolution-category subsection headers. Soft ordering: map fixes → code conformance → defers." |
| 2026-05-20 | File enumeration leaked into Discrepancy fields — cold-rerun audit's C1 listed 11 file paths verbatim in its Discrepancy, C2 listed 4. The "no enumeration" rule was scoped to the proposal as a whole but not per-finding. | closed | Tightened the audit-bullet rule: "Findings describe each discrepancy in summary; file paths, move tables, and per-instance enumeration are Phase-2 detail." |
| 2026-05-20 | Agent invented "project-wide decisions before consolidated audit proposal" structure — cold-rerun-2 had a separate Discussion section for route-enum file layout and missing Modal Styles README section, distinct from the consolidated audit findings. Useful pattern (surfaces cross-cutting decisions cleanly) but unstated in the rules. | closed | Added one sentence to the audit drafting bullet: "**Project-wide topics** that cross-cut many findings (e.g., a repo-wide pattern, a missing project-convention doc section) may be raised as their own Discussion topics before the consolidated audit proposal. Use sparingly — only when keeping the decision inline would noise up multiple per-scene findings." Permission, not requirement; "sparingly" clause guards against proliferation. |
| 2026-05-20 | Positive baseline finding returned (cold-rerun-2 finding O: "demo_mode_loading … Resolution: None (conformant). Listed for completeness"). Same defect as a prior fresh-session finding; the deviations-only rule was in the guide but too quiet. | closed | Bolded "**Findings are deviations only**" inline for visual emphasis. Rule content unchanged. |
| 2026-05-20 | File enumeration leaked into the new project-wide Discussion section — cold-rerun-2's "Project-wide conventions and overrides" listed 12 standalone `*Route.swift` files inline. The no-enumeration rule was scoped to "Findings", which the agent read as not applying to project-wide topics. | closed | Extended the rule's scope: "Findings **and project-wide Discussion topics** describe each discrepancy in summary; file paths, move tables, and per-instance enumeration are Phase-2 detail." |
| 2026-05-20 | Defers vanished after approval — Phase 1 captured them as findings; Phase 2 had no place for them, so the plan-doc record of audit deferrals lived only in the map's `todos:`. Surfaced when reviewing the defer mechanic's adequacy to track audit decisions, and reinforced by the agent over-deferring folder reorgs (cold-rerun-2's L/M/N) under the misconception that Xcode requires manual project edits — when the project uses synchronized folders, making folder moves mechanical. | closed | Added a Phase 2 **Deferrals** section to the plan-doc skeleton. Phase 2 now produces four artifacts (Change list + Deferrals + YAML diff + render). Added a Deferrals entry format subsection. Updated the defer mechanic: "approved defers populate the Phase 2 Deferrals section with a pointer to the TODO." Aligned the Conformance detection opportunistic-deviation rule with the new model ("raise it as a finding in the consolidated audit proposal"). The Xcode-folders slip is project-specific, not a skill issue — no rule change. |
| 2026-05-20 | "No resolution-category grouping" rule was fighting a strong agent instinct — four runs (dry-run + three cold reruns) all reached for resolution-direction groupings (`### Map fixes` / `### Code conformance` / `### Defers`, or the same labels as bold paragraph dividers). The rule's value was aesthetic; the agent's grouping was natural organization that aided review. Successive tightenings of the rule (banning `###` headers, then banning bold labels) escalated the fight without changing the agent's preference. | closed | Reversed direction: codified the grouping as *required* structure. Audit findings are now organized under three `###` subsections by resolution direction — `Map fixes`, `Code conformance`, `Defers` — in that order; omit empty subsections; letter prefixes continuous across subsections. Example updated to show the three headers. Trailing block rewritten as a positive rule. Stops the cycle of escalating prohibitions. |
| 2026-05-20 | Per-instance enumeration leaked into project-wide Discussion topics — cold-rerun-3's route-enum topic used a 9-row table with file-path links despite the just-added "summary, not enumeration" rule. The wording "describe in summary" was interpretable; the agent read a table as a summary. | closed | Tightened to principle-based wording: "Findings and project-wide Discussion topics describe each discrepancy in a sentence or two; per-instance evidence is Phase-2 detail." The "sentence or two" length constraint and "per-instance evidence" framing close the loophole without enumerating failure cases. |
| 2026-05-20 | "No per-instance enumeration in Phase 1" rule failed to stick across four cold reruns — the agent listed all 12 standalone `*Route.swift` files in the route-enum finding every time, despite three successive tightenings of the rule's wording. Same dynamic as the resolution-direction grouping issue (a few rounds earlier): the rule was fighting a strong, consistent agent instinct (prove the project-wide claim by enumerating instances). | closed | Same call as the grouping reversal: stop fighting it. Removed the rule "Findings and project-wide Discussion topics describe each discrepancy in a sentence or two; per-instance evidence is Phase-2 detail" from the audit drafting bullet. Per-finding enumeration is now accepted as evidence that the agent did the audit work; the human can scan past it. |
| 2026-05-20 | Discussion structure was hard to read at-a-glance — with the single-consolidated-proposal model, individual findings had no checkmarks, so it wasn't visible from the markers alone what had been resolved vs. pending. The original "one marker for the whole audit" decision (made early to avoid 10+ markers) didn't survive contact with a real 16-finding audit. | closed | Reversed: each finding now gets its own `- [ ]` item; the wrapping consolidated Proposal is gone. Findings sit directly under the `### Map fixes` / `### Code conformance` / `### Defers` subsections. Audit example updated to show individual markers with one finding in approved state. |
| 2026-05-20 | Resolved items lost their Kind label (`Tradeoff` / `Proposal`) when the agent edited item text to read as the resolution — making it harder to remember what kind of decision was originally being made. The "item text may be edited" allowance was too permissive. | closed | Added a `- **Decision** <succinct resolution>.` bullet appended to each item upon approval; the title (with its Kind label) stays untouched. Updated the Discussion loop description accordingly. |
| 2026-05-20 | Walk-through framing in the post-draft gate line was an extra construct that didn't add value. Human-driven discussion is the natural mode; the agent-driven walk-through option just adds confusion. | closed | Dropped the walk-through framing. Gate line simplified to "Respond to any open item to drive resolution. Phase 1 advances when all items are resolved." Gates section's "review/handoff STOP" reworded to "draft-complete STOP" with no walk-through language. |
| 2026-05-20 | Phase 2 Change list entries had no progress markers. The implementation skill needs a way to track which entries it has executed. | closed | Change-list entry format changed from `### N. <Type>: <identity>` heading to `- [ ] **N. <Type>: <identity>**` list item with checkbox. Sub-bullets unchanged. Implementation checks off `- [x]` as each entry completes. Deferrals and Out of scope stay as plain bullets (not actionable here). |
| 2026-05-20 | Tradeoff items with options that varied per affected item were presented as prose (commas separating implications) — making per-item feedback hard. The "Map naming alignment" Tradeoff in cold-rerun-4 had three options whose specifics only became clear at the policy level, not per-scene. | closed | Codified in the Tradeoff Kind description: "When options have different implications per affected item, expand each option as a sub-list — one bullet per implication — so the human can give per-item feedback (e.g., 'approve option B except keep X')." |
| 2026-05-20 | Gate model treated "blocked" as only an unexpected condition, so unresolved Phase-1 items had no explicit gate state — and the post-draft gate text was ambiguous about auto-advancing. | closed | Reframed: Blocked gates emitted whenever the agent cannot advance (including the normal Phase-1 in-progress state with unresolved `- [ ]` items); Planned gates emitted when ready to advance. Post-draft gate is now a Blocked gate citing open-item count; flips to Planned when all items are `- [x]`. No auto-advance to Phase 2 — explicit `next` required. |
| 2026-05-20 | Gate line text used internal phase numbers ("Phase 1", "Phase 2") that the user doesn't see in the plan doc. | closed | Plain section names in user-facing gate lines: "Discussion" and "Change list" (and "complete planning" at the Phase 2 gate). Internal prose in the guide keeps "Phase 1" / "Phase 2" as agent-facing shorthand. Added explicit Phase 2 completion gate line text. |
| 2026-05-20 | Audit example used `- [ ] A. **Title**` — letter prefix outside the bold. GFM-style renderers parse `A.` after a checkbox as an ordered-list start, breaking the layout. | closed | Letter prefix moved inside the bold: `- [ ] **A. Title**`. Audit example updated; the trailing block now explains the rule. Matches the Phase 2 entry format already in place (`- [ ] **N. <Type>: ...**`). |
| 2026-05-20 | Phase 1 intro rule "Do NOT create workflow-shaped sections" contradicted the required `### Map fixes / Code conformance / Defers` audit structure. | closed | Rule scoped to new-change drafting only. Audits use a fixed structure (per the Audit proposal example); the contradiction is resolved by separating new-change and audit guidance. |
| 2026-05-20 | Conformance detection section still referenced "consolidated audit proposal" — stale after the per-finding `- [ ]` refactor. | closed | Two references updated: "raise it as a finding under the appropriate `###` subsection" / "Each detected deviation becomes a finding under the appropriate `###` subsection." |
| 2026-05-20 | Decision-line format inconsistency between Discussion-loop prose and the audit example — prose called for "append a `**Decision** <text>.` bullet" but the example shown was `- **Decision** Fix code as proposed.` (with leading `-`). | closed | Prose updated to match the example: "append a `- **Decision** <succinct resolution>.` line as the last sub-bullet." |
| 2026-05-20 | Letter-prefix-inside-bold fix didn't address the actual rendering issue — markdown task-list items with bold-spanning-the-title still rendered the checkbox on its own line above the title in the user's renderer. Original diagnosis (ordered-list parsing) was incomplete; the bold span itself was the trigger. | closed | Verified via test file at `working-docs/main/checkbox-format-test.md` (host checkout). Adopted variation 2: `- [ ] A. Title text` — letter prefix outside, plain title (no bold). Updated audit example, Change entry format, and the trailing-block explanation accordingly. |
| 2026-05-20 | Phase 2 advancing gate ("Say 'next' to complete planning") was a no-op — saying "next" on a finished plan doc didn't do anything actionable. And the `🏁 Complete.` line didn't tell the human how to start implementation. | closed | Eliminated the Phase 2 advancing gate entirely. Agent now declares completion directly with: `🏁 Complete. The plan document is ready for implementation. Say "implement the plan" (or invoke the UI Map implementation skill directly) to begin.` Natural-language invocation is the primary path; the explicit skill name is the fallback. Updated three places in `ui-map-planning.md`: the gate-line description (line 39), the Gates section's Phase-2 bullet (line 44), and the Phase 2 section's closing (line 148). |
| 2026-05-23 | #1 — Conformance changes: spec line 65 ("never a Discussion topic") contradicts the per-finding-approval model (spec line 74 + guide route conformance deviations through Phase-1). Cold review of the codified guide. | closed | Architecture decision — chose model A (all conformance deviations are Phase-1 findings). Reworded `docs/ui-map-skill-plan.md` line 65: "surfaced as audit findings in Phase-1 Discussion, disposition approved per finding; not design-question topics; resulting Change-list entries are mechanical and not re-debated." Guide already matched A; no guide change. |
| 2026-05-23 | #2 — After-drafting gate emitted an unconditional Blocked gate ("<N> open items"), nonsensical for a fully-specified change or fully-conformant audit (zero items). | closed | Merged the after-drafting and subsequent-response gate logic: Blocked if any `- [ ]` remain, advancing Planned gate if none (including zero items drafted). |
| 2026-05-23 | #3 — `Detail` field listed as standard but omitted in example F2/F4; `Options` not marked Tradeoff-only. | closed | Sub-bullet-labels line reworded: `Concern`/`Proposal` always, `Detail` when the concern needs elaboration, `Options` only for a Tradeoff, `Why` for rationale. |
| 2026-05-23 | #4 — Finding-format spec stated three times (drafting bullet, example, format paragraph) with verbatim overlap. | closed | Trimmed the drafting bullet to a pointer ("see the finding format below"); authoritative format stays in the post-example paragraph. |
| 2026-05-23 | #5 — fix-map/fix-code → typed-entry mapping never stated. | closed | Added a sentence at the Phase-1→2 transition: fix-map finding → `add`/`move`/`modify` entry; fix-code finding → `conformance / <dimension>` entry. |
| 2026-05-23 | #6 — Plan-skeleton comment called Change-list contents "findings"; the list holds typed entries, findings live in Discussion. | closed | Skeleton comment reworded to "typed changes from the resolved findings." |
| 2026-05-23 | #7 — Generic blocked-gate template ("Resolve and say 'next' to continue") clashes with the Phase-1 blocked gate ("Resolve them to proceed"). | rejected | The generic gate line is the house-standard template; the concrete Phase-1 blocked gate already specializes it correctly. The mismatch is cosmetic with no workflow break, and editing the standardized template to chase it isn't worth the churn. Re-raises expected — refer back here. |
| 2026-05-23 | #8 — Verbatim duplications (long `🏁 Complete.` sentence at Gates and Phase-2; decision-line, ID-rationale, "no Decisions section" repeats). | closed | Deduped the long completion sentence: canonical kept at the Phase-2 point of use; Gates section now references it. The short "rule at point of need" repeats left as-is per the refinement guide's tolerance. |
| 2026-05-23 | #9 — Spec's "auto never auto-decides architecture" (spec line 121) is not restated in the guide. | logged | Already enforced implicitly: `auto` cannot pass a blocked gate, unresolved items force a blocked gate, and items resolve only on explicit human approval — so auto cannot advance past an open architectural decision. Restating adds no enforcement; per default-to-no-rule, not codified. Re-raises — refer back here. |
| 2026-05-23 | H1 (cold review 2) — `Question` audit kind self-contradictory: required a Proposal it can't have, and had no disposition subsection. | closed | Field rule now takes a `Question` line instead of a Proposal; Questions ride the existing raised-first slot (extended line 87) and are answered in place — no reorg (per human). No new subsection added. |
| 2026-05-23 | H2 — scope gate "schema and conventions" misreads as *both*; the spec's bare "schema" is too narrow (folders/naming are conventions, not schema). | closed | Reworded guide + spec to "resolvable as a UI-Map change OR a code-conformance fix under the conventions." |
| 2026-05-23 | H3 — Out-of-scope determinations bypass the per-finding approval that even a defer requires (gameable). | deferred | The human reviews the audit and can redirect a bad out-of-scope call; a formal approval gate is premature. Revisit if it proves a problem in practice. |
| 2026-05-23 | H4 — Phase-2 render/validate points at integration-doc sections that don't exist, and planning had no blocked-gate for missing tooling. | closed | Added "required tooling/commands missing" to planning's blocked-gate reasons (STOP, don't improvise). The empty `integration.md` UI-Map section is the known step-7 deferral, not a guide bug. |
| 2026-05-23 | M1 — "opportunistic detection" vs "new-feature runs no detection" read as a contradiction. | closed | Reconciled: no *deliberate* detection in new-feature; a trip-over is still raised and the human sets scope. |
| 2026-05-23 | M2 — two-pass pass-1 ("enumerate concerns") had no defined output. | closed | Pass-1 is a non-persisted working list; the findings are the only persisted artifact. |
| 2026-05-23 | M3 — "no enumeration in Phase 1" collided with "bucket by resolution," ~50 lines apart. | closed | Reconciled at point of use: same disposition → count; differs → bucket (per the bucket rule). Dropped the absolute "no enumeration." See supersession note. |
| 2026-05-23 | M4 — Phase-1 blocked-gate line differs from the generic template. | rejected | Re-raise of last pass's #7. The generic gate line is the house-standard template; the Phase-1 gate specializes it correctly; cosmetic, no workflow break. Refer back here. |
| 2026-05-23 | M5 — detection method stated after the audit-drafting step that consumes it. | closed | Lighter fix instead of moving the section: audit bullet now says "first run conformance detection (see below) ... then draft" — explicit dependency + pointer. Rationale: an LLM reads the whole guide; a pointer is navigable and avoids churn. Move the section if a future review still trips here. |
| 2026-05-23 | M6 — placement of project-wide / opportunistic items in audit Discussion undefined. | closed | Project-wide topics + Questions sit above the disposition subsections; opportunistic findings in a free-form new-change Discussion are appended at the end. |
| 2026-05-23 | L1 — two Kind-tag syntaxes (`Proposal —` new-change vs `F1 [Proposal]` audit). | logged | Matches the spec's own context split; minor, no mixing observed. Codify only if mixed forms appear. |
| 2026-05-23 | L2 — `remove` dropped from the fix-map → entry mapping. | closed | Added `remove`. |
| 2026-05-23 | L3 — scene vs scene-attribute granularity undefined; "taxonomy derived from schema" note absent from guide. | logged | Rare; the schema is consultable. Avoid bloat; codify a one-line schema pointer on recurrence. |
| 2026-05-23 | L4 — a defer adds a `todos:` yaml edit with no Change entry, not explicitly stated. | logged | Already covered: line 87 instructs adding the TODO ("or a new one added this pass") and states "produces no Change-list entry." Edge is minor; no change. |
| 2026-05-23 | L5 — zero-item planned-gate read "All Discussion items resolved" when there were none. | closed | Reworded to "Discussion complete." |
| 2026-05-23 | L6 — no worked example of a resolved item. | logged | The `- [x]` + `Decision` shape is specified; an example is nice-to-have. Default-to-no-rule; add if confusion arises. |
| 2026-05-23 | Supersession note — an earlier pass removed "no enumeration in Phase 1" (it fought a strong agent instinct); this session's codification re-added a high-level/count model at the user's direction, now reconciled (count for uniform, bucket for divergent). | noted | Recorded so a future review doesn't flag the count model as a flip-flop: enumeration is allowed where it serves a decision (buckets) or proves the audit; uniform concerns use a count. |
| 2026-05-23 | Checkboxes wrapped *inconsistently* in a rendered cold audit — single-finding subsections rendered inline, multi-finding subsections wrapped (checkbox on its own line above the title). ROOT CAUSE (finally): a "loose" markdown list (blank lines between findings) puts the checkbox on its own line in the user's renderer; a "tight" list (no blank lines between items) keeps it inline. Confirmed empirically: test Block A (loose) wrapped, Block B (tight) inline. | closed | Added a "Keep findings tight" rule (no blank line between consecutive findings; same for Change-list entries) and tightened the audit example to demonstrate it. **Supersedes every prior checkbox closure** (2026-05-20 bold-span "fix"; letter-prefix-inside-bold; the move to `F#`/`T#` letter-led IDs) — those chased the wrong cause (bold spans, ordered-list parsing of `A.`/`5.`) and did not hold. List looseness is the only variable that matters. The `F#` IDs and plain titles remain fine but were never the fix. Spec not updated — markdown-whitespace rendering is below the spec's design level. |
| 2026-05-23 | F8 (cold-audit critique) — agent inferred modal-style from the enum *name* (`*MessageRoute` → "SwiftMessages") instead of the modifier actually bound; produced a wrong implementation description and missed the real `…MessageRoute`→`…ModalRoute` misnaming (three enums drive `.modal()`, verified). | closed | Existing rule already covered it ("route-kind **as realized in code**") — the agent failed to apply it, not a missing rule. Per the codification check, **sharpened the existing detection rule with a concrete example** (`.modal(item: $vm.messageRoute)` is the `modal` style despite the `…MessageRoute` name) rather than adding a new rule. The audit doc was throwaway — not corrected. Considered and rejected a new detection rule (process-bloat) and rejected log-only (a significant error with an existing-rule-missed warrants the example, per "prefer examples over rules"). |

## Compose library — 2026-09-02

Restored from `refinement-reviews/ui-map-compose-findings.md` at skai commit `c69a3e0` ("UI map compose library", 2026-09-03, branch `work/uimap-cmp`; also on `work/skai-v6-uimap-integration`). The commit added `Dev/Compose` (the `skai-compose-android` placeholder and routing library) and revised `ui-map-compose.md` and `ui-map-compose-placeholders.md`; neither the library nor those revisions reached `main`, whose Compose placeholder guide still describes project-vendored libraries. The design spec's Open section carries that.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-09-02 | R1 F1 — guide falsely required project-vendored libraries | closed | Official SKAI Compose dependency selection and mechanical attachment now live in `ui-map-compose.md`. |
| 2026-09-02 | R1 F2 — Android-only Hilt conventions were mandatory for shared KMP | closed | Guide now branches on the consuming source set and makes Hilt an established Android-only option. |
| 2026-09-02 | R1 F3 — modal examples named nonexistent APIs and defaults | closed | Canonical modal table and examples match `ModalNavHost`, `bottomSheet`, `bottomSheetFullScreenModal`, and `dialog`; both artifacts compile. |
| 2026-09-02 | R1 F4 — indexed domain-color API was missing | closed | `PlaceholderColors.domain(index)` implements all nine renderer slots, wraps, and compiles in both artifacts. |
| 2026-09-02 | R1 F5 — destination helpers lost presenter route menus/ancestry | closed | Push and modal helpers append inherited crumbs with the shared presenter route list; examples reuse one list. |
| 2026-09-02 | R1 F6 — root placeholders rendered as embedded composites | closed | `LocalPlaceholderIsEmbedded` is supplied only around composite children; root/start scenes are full-bleed. |
| 2026-09-02 | R1 F7 — long breadcrumbs opened on the ancestor end | closed | Breadcrumb scroll state moves to its maximum when the path or measured range changes. |
| 2026-09-02 | R1 F8 — production cleanup could remove routing still in use | closed | Cleanup now retains the combined dependency while either routing or placeholder symbols remain. |
| 2026-09-02 | R1 F9 — state-file rule contradicted the stateless exemption | closed | State/event/effect files are required only for scenes with state-management responsibility. |
| 2026-09-02 | R2 F1 — tabbed modal destination lost dismiss context | closed | Tab scaffolding now inherits the presentation context; embedded and pushed boundaries preserve their distinct resets. |
| 2026-09-02 | R2 F2 — dependency placement was ambiguous in a mixed KMP module | closed | Paired Gradle examples place the KMP artifact in `commonMain`, prohibit an additional Android artifact, and show the plain-Android alternative. |
| 2026-09-02 | R2 F3 — pushed helper allowed omission of its back action | closed | `onBack` is required and non-null; no external workspace caller required migration. |
| 2026-09-02 | R3 F1 — tab-plus-composite placeholders silently omitted composite children | closed by owner ruling | The current renderer's combined shape is documented as unsupported and blocks in Discussion; real app architecture remains unrestricted. |
| 2026-09-02 | R3 F2 — setup omitted the consuming module's serialization compiler prerequisite | closed | Setup now inspects/adds the project-compatible plugin mechanically and blocks on incompatible constraints. |
| 2026-09-02 | R3 F3 — worked placeholder scaffolds omitted file-level markers | closed | Every Kotlin scaffold example now begins with the exact change-id marker; leaf view-model and screen examples are separate files. |

## Change-request triage — 2026-10-19

The pass that aligned `ui-map-architecture.md` and `ui-map-architecture-artifacts.md` with the shared triage decision (the supervisor rules on a change request; the agent applies) is logged with the other spec types in [`change-request-triage-findings.md`](change-request-triage-findings.md): see r1 F3 (the "on its own" qualifier in § Initiation) and r5 F1 (the proposed map is seeded only when none exists).

## Route files and tab bars — 2026-11-07 (skai#81, skai#57)

Draft-then-cap per skai#90: inventory and caps in the design spec's § Decisions — 2026-11-07; compression review on the additions; then cold review with the compressed edits and the caps.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-11-07 r1 | F1 Nav routing examples declared the route enum beside the view model | closed | Enum declarations removed from both guides' Nav routing examples; *Route enums* keeps the definition |
| 2026-11-07 r1 | F2 "The tab bar is production code" misread against the package rendering the bar | closed | Tab sections say tab titles and icons are final, and that the package's bar is the bar |
| 2026-11-07 r1 | F3 The spec's "records nothing about them" was dropped | closed | Restored in both tab sections |
| 2026-11-07 r1 | F4 SwiftUI API list omitted the tab icon parameter | closed | `PlaceholderTab(label:systemImage:)` |
| 2026-11-07 r1 | F5 SwiftUI library doc comment calls a tab's label the child scene's name | logged | Outside the guides; routed to the placeholder library in `Dev/Swift/` |
| 2026-11-07 r1 | F6 Nothing lists tab titles, icons and sources for review | rejected | Supervisor ruling: the result is checked in the running app, so change entries don't list them |
| 2026-11-07 r1 | F7 Tab sections didn't point to the designs input | closed | "(an implementation input)" in both tab sections |
| 2026-11-07 r1 | A1 Stale `@Published` | closed | Removed; doubles as a cap trim |
| 2026-11-07 r1 | A2 Client app names in the Compose placeholder guide | closed | Removed; doubles as a cap trim |
| 2026-11-07 r1 | A3 "Modal-style enums" illustrated with a nav enum | logged | Cosmetic, single observation |
| 2026-11-07 r1 | Trim of the implementation guide's custom-marker-lifecycle lines | rejected | Shared progress-tracking template text, also in the architecture guide; the Gates **Completion** paragraph became a pointer instead |

Sizes after round 1 repairs, against caps: swiftui 9,990 / 10,050; compose 10,792 / 10,850; swiftui-placeholders 14,965 / 15,050; compose-placeholders 15,949 / 16,000; implementation 51,351 / 51,500.
| 2026-11-07 r2 | F1 Child, tab and Compose modal examples still declared their route enums beside the view model (round 1's F1 fix was partial) | closed | Enum declarations removed from every route-kind example in both platform guides; *Route enums* is their one home |
| 2026-11-07 r2 | F2 SwiftUI *Route enums* gave modal enums the conformances a nav enum shows (re-raises r1 A3) | closed | Conformance sentence now covers enums bound with `item:` and tab enums |
| 2026-11-07 r2 | F3 Tab fallback reachable without looking for designs | closed | Fallback applies to tabs the designs don't show or when none were supplied; Inputs say what the designs feed; the artifact's Inputs record the designs used or that none were supplied (supervisor) |
| 2026-11-07 r2 | F4 Spec and guides differed on an app's existing tab bar | closed | Supervisor: the existing bar is used. Guides add that a tab added to the app's own bar uses it as set up, through *Reaching a scene from a real screen*; the spec is unchanged |
| 2026-11-07 r2 | F5 Tab examples used labels equal to scene names | closed | One tab per example shows a label from the designs |
| 2026-11-07 r2 | F6 Placeholder titles' source unstated | closed | `title` is the scene's name from its map ID, at each API list |
| 2026-11-07 r2 | F7 "Expected when available" joined the previous bullet | closed | Blank line |
| 2026-11-07 r2 | F8 Gates quotes one fixed completion line | logged | Shared template text; routed to the template's owner |
| 2026-11-07 r2 | F9 Compose placeholder route pointer named the whole file layout | closed | "route file layout" |
| 2026-11-07 r2 | Trim of the implementation guide's planned-gate steps | rejected | Shared template text |

Round 2 repairs leave `ui-map-swiftui-placeholders.md` 9 bytes and `ui-map-compose-placeholders.md` 80 bytes over their caps, after the reviewer's two recommended trims; round 3 is asked for the rest.
| 2026-11-07 r3 | F1 "final" asked to go back to "production code" | rejected | r1 F2 closed "production code" as an undefined label that misled; "final" states what it means |
| 2026-11-07 r3 | F2 Compose tab section said "package" | closed | "library" |
| 2026-11-07 r3 | F3 Both placeholder guides cited an unreachable "rebuild-plan D12" | closed | Removed; the work is skai#127 |
| 2026-11-07 r3 | F4 Designs input buried in a hard-to-parse bullet | closed | Its own bullet in Inputs |
| 2026-11-07 r3 | F5 Placeholder tab bars had no way to use the tab route enum | closed | Supervisor: match production. The SwiftUI placeholder library takes `selection:` and `route:`; the guide binds `currentTabRoute` |
| 2026-11-07 r3 | F6 API lists gave no pointer to the tab rules | closed | Each `PlaceholderTab` entry points to *tab* |
| 2026-11-07 r3 | F7 Modal examples' `routes` no longer explained beside them | logged | The rule stays at *Destination markers*; the nav example shows it |
| 2026-11-07 r3 | Appendix: stale `item:` kind list; child enum conformances; Compose companion pointer omits *Modal routing* | logged | Cosmetic, outside the charter |
| 2026-11-07 r4 | F1 SwiftUI tab example's `route: .notes` didn't type-check against the generic initializer | closed | Cases written as `LibraryTabRoute.notes` |
| 2026-11-07 r4 | F2 API list omitted `selection:` | closed | `PlaceholderScene(title:domainColor:routes:tabs:selection:)` |
| 2026-11-07 r4 | F3 SwiftUI placeholder guide over cap | closed | Trims: the one-rule worked example (stated again in *child*), the speculative modifier sentence (skai#127 holds it), the "throwaway" sentence |
| 2026-11-07 r4 | F4 Initiation loaded only required inputs, so designs were never gathered | closed | Initiation loads the expected inputs that are available; the Gates "Code Changes ready" bullet now points to *Code Changes gate* (it restated it) |
| 2026-11-07 r4 | F5 Code Changes gate summary didn't say whether designs were used for a tab bar | rejected | Supervisor: gates announce no other inputs; the artifact's Inputs records them |
| 2026-11-07 r4 | Q1 `selection:` with tabs lacking `route:` silently desyncs the bar | closed | Supervisor: library debug assertion in `PlaceholderScene` |
| 2026-11-07 r4 | F6 Stale `item:` modifier list | closed | (nav, sheet, cover, popover) |
| 2026-11-07 r4 | F7 Compose layout comment read as one file per route | closed | "route kind" |
| 2026-11-07 r5 | F1 Implementation Inputs gave no way to tell whether designs were available | closed | Designs are available wherever the request, the architecture artifact's `## Inputs` or the scope collateral names them |
| 2026-11-07 r5 | F2 Real-screen block didn't say it covers a tab added to the app's own bar | closed | Supervisor ruling (existing bar via the real-screen route, skai#127): both placeholder guides' block names that case |
| 2026-11-07 r5 | F3 Implementation guide restated the tab-title rule without its fallback | closed | Reduced to a pointer to the placeholder guides |
| 2026-11-07 r5 | F4 SwiftUI API list offered `selection:` only without embedded content | closed | Listed as one form, optionally with `{ embedded }` |
| 2026-11-07 r5 | F5 Real-screen STOP sits under Implement, not Audit | logged | Placeholder guides carry the STOP at the point of use |
| 2026-11-07 r5 | F6 Four hand-kept lists of what the placeholder guides cover | logged | None stale; shorten when next edited |
| 2026-11-07 r6 | F1 Tab sections read as permission to add a tab to the app's own bar | closed | Tab sections now say it is a real-screen route, not a `tabs:` entry |
| 2026-11-07 r6 | F2 Real-screen wiring assumed a trigger overlay even for a tab bar | closed | SwiftUI block: registration on the nav host or tab bar, trigger unless the host is its own entry; implementation § Implement matches |
| 2026-11-07 r6 | F3 "Final" is shorthand for production code | logged | Action is carried by the rest of the sentence |
| 2026-11-07 r6 | F4 API list shows only the `selection:` form | logged | Rule and example pair `tabs:` with `selection:` |
| 2026-11-07 r7 | F1 "Adding to it" read as adding tabs | closed | Both tab sections: "adding components or customizations to it", the spec's wording |
| 2026-11-07 r7 | F2 Real-screen registration on a tab bar pointed back to the tab section | closed | Piece 1 also cites *Tab routing* in the platform guide |
| 2026-11-07 r7 | F3 Implementation said the placeholder guide defines the trigger; Compose defines none | closed | "the entry trigger that mapping defines" |
| 2026-11-07 r7 | F4 Audit file-layout check compared only the scene's folder | closed | Audit and the `file-layout` row compare the scene's file set too |
| 2026-11-07 r7 | F5 Code blocks show several files together | logged | Route enums sections state the file; codify on recurrence |
| 2026-11-07 r7 | A1 Compose `isCurrent` expressions differ without comment | logged | Outside charter |
| 2026-11-07 r7 | Q SwiftUI real-screen TODO said "no defined mapping" then defined one | closed | TODO says the whole route is deferred, the own-bar tab included |
| 2026-11-07 r8 | F1 Structure-not-features invariant read against design-sourced tab titles | closed | Invariant names the tab-bar carve-out and points to the placeholder guide's *tab* |
| 2026-11-07 r8 | F2 "Styling it" drops the spec's "bars the app hasn't styled" | logged | Matches the spec for the only bar a scaffold sets up today |
| 2026-11-07 r8 | F3 "You declare only …" list omitted `selection` | closed | Added |
| 2026-11-07 r8 | F4 Deferred real-screen section carried a buildable trigger recipe | closed | `safeAreaInset` detail removed; skai#127 holds the design |
| 2026-11-07 r8 | A1 Circular "missing-input rule" pointers | closed | Placeholder guides just STOP; implementation cites *Finding disposition* |
| 2026-11-07 r8 | Q Compose placeholder tab route file with no selection binding | logged | Compose library work, skai#128 |
| 2026-11-07 r9 | F1 "Routes live on the view model" read as file placement | closed | "Route state lives on the view model"; both *Route enums* say "not inside it" |
| 2026-11-07 r9 | F2 Placeholder guides stop in two idioms (blocked gate vs Discussion) | logged | Pre-existing text outside this change |
| 2026-11-07 r9 | F3 Override location stated under *Modal routing* only | closed | Moved to each platform guide's intro, covering every pattern |
| 2026-11-07 r9 | F4 Design icons that aren't SF Symbols have no instruction | closed | Supervisor: falls back to a fitting icon, as for an unshown tab |
| 2026-11-07 r9 | F5 *Routes aren't special* restates table rows | logged | Pre-existing; agrees with the table |
| 2026-11-07 r9 | F6 "are production" shorthand | closed | "production code, not placeholder labels" |
| 2026-11-07 r9 | A1–A3 Section order, pre-read list, override-document naming | logged | Outside charter |
| 2026-11-07 r10 | F1 "Established project conventions" let undeclared code habits outrank the guide | closed | Handoff example and never-auto-fix name a declared convention; an undeclared pattern is a deviation |
| 2026-11-07 r10 | F2 Override list didn't name file layout | closed | "folder organization and file layout"; "route wrappers" dropped |
| 2026-11-07 r10 | F3 Icon fallback replaced the designs' title too | closed | Title and icon fall back independently |
| 2026-11-07 r10 | F4 SwiftUI placeholders set route state from the view without saying it's placeholder-only | closed | Intro states it, as the Compose guide does |
| 2026-11-07 r10 | F5 Unresolved symbol builds as a square | logged | Supervisor checks icons in the running app |
| 2026-11-07 r11 | F1 Handoff example read a declared convention as handoff work | closed | Moved to the Audit file-layout bullet: a convention counts only when declared |
| 2026-11-07 r11 | F2 "view-model conventions" is a coined label | closed | Dropped |
| 2026-11-07 r11 | F3 SwiftUI tab example doesn't show the fallback branch | logged | Prose is unambiguous |
| 2026-11-07 r11 | F4 "One enum per route kind" reads wrong for modals until the next sentence | logged | Recovered two sentences later |
| 2026-11-07 r11 | A1 Compose stateless leaf vs every scene exposes three sealed types | logged | Older text |
| 2026-11-07 81-r1 | F1 Compose guide named the override location with an undefined label | closed | Both platform guides say `README.md` |
| 2026-11-07 81-r1 | F2 Compose "Routes are owned by … not the view model" | closed | "Route state is owned by" |
| 2026-11-07 81-r1 | Appendix: modal sentence order, Inputs record of a checked README, T# granularity, spec P9 wording | logged | Outside scope |
| 2026-11-07 81-r2 | F1 Platform guides said README only; implementation also accepts a conventions doc | closed | Each platform intro defines the override document once; README below means either |
| 2026-11-07 81-r2 | F2 SwiftUI file rule stated before its modal exception | closed | Exception moved into the rule's sentence |
| 2026-11-07 81-r2 | F3 *Finding disposition* placement named only the platform convention | closed | "platform or declared project convention" |
| 2026-11-07 81-r3 | F1 "README below means either" didn't reach the placeholder guides | closed | "README here and in the placeholder guide means either" |
| 2026-11-07 81-r3 | F2 "One enum per route kind" vs per-style modal enums | closed | "or per modal style" |
| 2026-11-07 81-r3 | F3 "route-host placement" defaults to Implement | logged | Predates this change (f8ec8a5) |
| 2026-11-07 81-r3 | F4 Undeclared-pattern clause unqualified | logged | Preceding sentence and Inputs resolve it |
| 2026-11-07 81-r3 | F5 "Route-type contract" label in Compose placeholder pointer | logged | Cosmetic |
| 2026-11-07 81-r3 | F6 Override definition sits in the routing intro | logged | No proportionate fix under caps |
| 2026-11-07 81-r4 | F1 SwiftUI *Route enums* opening takes three corrections to reach the modal file name | logged | Readable; no misroute |
| 2026-11-07 81-r4 | F2 Intro forward-references the placeholder guide | logged | Reached by reading the guide fully |
| 2026-11-07 81-r4 | F3 "lives" used for enum file and route state | logged | "not inside it" governs |
| 2026-11-07 81-r4 | F4 Nothing says how to establish that no declaration exists | logged | Gate and Inputs record make it auditable; record "none found" if it recurs |
| 2026-11-07 81-r4 | F5 Override-document rule restated in five places | logged | Owner: platform intro (definition), implementation (audit consequence); placeholder guides point |
| 2026-11-07 81-r4 | Series 81 (route files) converged: a round with no live findings | closed | — |
| 2026-11-07 57-r1 | F1 Designs lookup was a location, not a step; "none supplied" recordable without looking | closed | Inputs say to check the three places; the record says that check found none |
| 2026-11-07 57-r1 | F2 Tab titles could also come from requirement/story sources | closed | Rejected at first on a misread ruling; supervisor later widened sources to any input |
| 2026-11-07 57-r1 | F3 "missing-mapping rule" label has no owner heading | closed | Cites *Finding disposition* |
| 2026-11-07 57-r1 | A1–A4 Selection-less library inits, Tab routing pre-read, *Boundary* carve-out, example annotations | logged | Outside scope or cosmetic |
| 2026-11-07 57-r2 | F1 Inputs record's "that check" had no anchor | closed | Names the designs check in the guide's *Inputs* |
| 2026-11-07 57-r2 | F2 Designs found but unreadable could read as "don't show" | logged | Standing ambiguity stop covers it; fix at the Inputs bullet if it occurs |
| 2026-11-07 57-r2 | A1–A5 Debug stop unmentioned, marker examples, ImageVector shorthand, duplicated Inputs clause, CLI symbol oddity | logged | Cosmetic |
| 2026-11-07 57-r3 | F1 Inputs record said "designs used" (nothing uses them in Plan) and coined "designs check" | closed | "the designs found in the places *Inputs* lists, or that none were found there" |
| 2026-11-07 57-r3 | F2 Invariant classified tab titles instead of saying the scaffold writes them | closed | "the scaffold writes a tab bar's titles and icons as production code" |
| 2026-11-07 57-r3 | F3 "The app's own bar" didn't exclude an earlier scaffold's placeholder bar | closed | "a real screen's bar" in both guides |
| 2026-11-07 57-r3 | F4 README bar convention vs "the package's bar is the bar" | logged | Not yet seen; ❌/✅ example if it occurs |
| 2026-11-07 57-r4 | F1 "Tab titles" collides with the scene `title:` | closed | "Tab labels", matching `label:` |
| 2026-11-07 57-r4 | F2 Inputs record says designs "found", spec says "used" | rejected | Reverses 57-r3 F1: a Plan run uses no designs; the *tab* rule makes the scaffold follow them |
| 2026-11-07 57-r5 | F1 *tab* pointed to "an implementation input", not the record | closed | "the designs the artifact's Inputs record" |
| 2026-11-07 57-r5 | F2 Designs lookup used "scope collateral" and never said what designs are | closed | "(the design file or drawings)"; "the story's linked documents" |
| 2026-11-07 57-r5 | F3 Spec says tab "title", guides say "label" | closed | Spec aligned to "label" |
| 2026-11-07 57-r5 | F4 No pairing rule when designs' tabs and map tabs disagree | logged | Standing ambiguity stop |
| 2026-11-07 57-r6 | F1 "the artifact's Inputs" could mean the architecture or implementation artifact | closed | "the implementation artifact's `## Inputs`" |
| 2026-11-07 57-r6 | F2 Project-convention path to a real tab bar never meets the label rule | logged | Future text behind the deferred route; lands with skai#127 |
| 2026-11-07 57-r6 | F3 Resume doesn't say to refresh the designs record | logged | Standing ambiguity stop; record shows what was searched |
| 2026-11-07 57-r7 | F1 A missing or stale designs record reads like "none found" at *tab* | closed | Moot: supervisor widened label sources to any input; *tab* no longer reads a designs record |
| 2026-11-07 57-r7 | A1, A2 Inputs bullet phrasing; dense relative clause in *tab* | logged | Cosmetic |
| 2026-11-07 57b-r1 | F1/F2 Product specs named as a label source but not loaded or recorded | closed | Inputs bullet and record name designs and product specs; spec matches |
| 2026-11-07 57b-r1 | F3 Examples marked only one tab as from the inputs | closed | Comment on the tab list |
| 2026-11-07 57b-r1 | F4 *Tab routing* not in the SwiftUI read-first list | logged | Platform guide is read in full |
| 2026-11-07 57b-r2 | F1 "Available" undefined when loading expected inputs | closed | Initiation loads "the expected ones found where *Inputs* says to look"; the bullet says where |
| 2026-11-07 57b-r2 | F2 Where-to-look list omitted the change package | closed | Named |
| 2026-11-07 57b-r2 | F3 Route-menu label source unstated | logged | Examples consistent; no recurrence |
| 2026-11-07 57b-r2 | F4 Compose icon-fallback clause hard to parse | closed | "or that has no `ImageVector`" |
| 2026-11-07 57b-r2 | A1 `PlaceholderTab.label` doc comment said designs only | closed | Doc comment updated |
| 2026-11-07 57b-r3 | F1 Expected inputs could go unloaded | rejected | Supervisor: low-risk like any coding slip; lookup and record wording removed instead |
| 2026-11-07 57b-r3 | F2 Compose "has no `ImageVector`" names a type, not a test | closed | "that no existing `ImageVector` provides" |
| 2026-11-09 57b | Series 57 (tab bars) converged by supervisor ruling | closed | — |
| 2026-11-09 | Cap trims deleted worked examples and explanations instead of tightening wording | closed | Supervisor ruling: all cap trims restored, examples labeled with their files; caps met by a compression review's rewording (102 changes, verified); its proposal to delete the Compose type bullets was rejected. Template wording that invited it drafted as a skai ticket |
| 2026-11-09 caps-r1 | F1 SwiftUI placeholder child section told a child coordinator under a sheet, cover or tab to add a second stack | closed | Parenthetical names the root or a popover as the boundary; sheet, cover, tab and nav push already supply one |
| 2026-11-09 caps-r1 | F2/F3 Multi-file code blocks without file labels (SwiftUI Modal routing; both leaf examples) | closed | Each file labeled; Modal routing shows the shared `DashboardModalRoute.swift` |
| 2026-11-09 caps-r1 | F4 Compose "screen never reads the current route" vs. tab route in view state | logged | Tab routing governs at its point of use |
| 2026-11-09 caps-r1 | F5 Change-request step said the run awaits the map before the request file is written | closed | Wait sentence removed; "In either run, immediately write…" |
| 2026-11-09 caps-r1 | F6 `DomainColors` has no stated home for `common:` scenes in a shared module | logged | Standing escalation catches it; one clause in *Domain colors* if it recurs |
| 2026-11-09 caps-r1 | A1–A11 Duplicate `DashboardNavRoute` cases, "three sealed types", routeless crumb color, `SlideNavHost` call shapes, unlabeled single-file fragments, marker syntax pointer, real-screen STOP restated under *Implement*, third completion copy, invariant pointer | logged | Cosmetic |
| 2026-11-09 caps-r2 | F1/F2 SwiftUI library's tabbed branch draws only the tabs: tabs plus composite drops the composite, a tabbed modal had no ✕, and a sheet wrapped tabbed content in a second stack | closed | Guides carry the spec's tabs-plus-composite STOP; library passes the ✕ to tabs; a tabbed destination's tabs own their stacks |
| 2026-11-09 caps-r2 | F3 Compose "every scene exposes three sealed types" vs. the stateless-scene exemption | closed | "Every scene with a view model" |
| 2026-11-09 caps-r2 | F4 No-package rule lacked its change-request exception | closed | Pointer to *Raising a change request* |
| 2026-11-09 caps-r2 | F5 "Type folder" undefined | closed | Defined at the `ui-map/` folder |
| 2026-11-09 caps-r2 | F6 Compose modal API names differ from the spec | logged | Reconcile when the Compose library lands |
| 2026-11-09 caps-r2 | A1–A6 Assert unmentioned, nav-bar overclaim for popovers, "sub-domain", gate-line location rule, archive shorthand, palette wrap | logged | Cosmetic |
| 2026-11-09 caps-r3 | F1 Tab stacks stated unconditionally; a pushed tabbed scene got two answers | closed | **Tab** bullet owns the tabbed-scene boundary; modal and child point to it |
| 2026-11-09 caps-r3 | F2/F3 Compose guide lost the `scenes/` root and the README bar for non-standard modal styles | closed | Both restated in Compose, parallel to SwiftUI |
| 2026-11-09 caps-r3 | F4 SwiftUI nav example's scene wrapped itself in a `NavigationStack` | closed | Wrapper removed; matches the modal example |
| 2026-11-09 caps-r3 | A1–A5 Library accepts tabs plus embedded; resume "records" Mode; `Route`/`NavStart` not in the library list; unnamed linkage rule; Compose modal crumb reset | logged | Cosmetic |
| 2026-11-09 caps-r4 | F1 Decision question and modal bullet told a sheet to wrap a tabbed destination | closed | The decision question asks whether the presented scene is tabbed; modal bullet points to **tab**; nav-bar sentence covers tabbed scenes |
| 2026-11-09 caps-r4 | F2 Leaf examples lacked the scaffold marker | closed | Marker line on each file |
| 2026-11-09 caps-r4 | F3 Compose tab section named one widget | closed | "the tab container in use" |
| 2026-11-09 caps-r4 | A1 `note.text` example has no `.fill` variant | closed | `text.document` |
| 2026-11-09 caps-r4 | A3–A6 Library-link stop phrasing differs, Compose icon clause, `DomainColors` location, mixed-destination modal example | logged | Cosmetic |
| 2026-11-09 caps-r5 | F1 Declared-convention rule sat inside one audit bullet | closed | Moved below the *What to compare* list |
| 2026-11-09 caps-r5 | F2 Compose tabbed placeholder's tab route file | rejected | Deferred to the Compose library; missing from the prompt's settled list |
| 2026-11-09 caps-r5 | F3 Library doc comment said tabs never show the ✕ | closed | Tab content inherits the scene's value |
| 2026-11-09 caps-r5 | F4 Compressed phrases lost their noun: "route" (layout), "final" (tab), Compose icon clause | closed | "route kind"; Compose icon clause reworded; "final" left as logged earlier |
| 2026-11-09 caps-r5 | F5 "One nav bar per tab" overgeneralized | closed | "a tabbed scene at a boundary" |
| 2026-11-09 caps-r5 | F6 New-scene-inputs STOP without a section pointer; appendix (tab fragment's `@Bindable`, Compose README-only modal styles) | logged | Cosmetic or out of scope |
| 2026-11-09 caps-r6 | F1 "Boundary" used in two senses in the one rule | closed | Conditions carry the meaning; "boundary" dropped from the tab and child bullets |
| 2026-11-09 caps-r6 | F2 Library default list said tabs have nothing to dismiss | closed | "tabs of a non-modal scene" |
| 2026-11-09 caps-r6 | F3 Scaffold-marker examples named only a nav host | closed | "or tab bar" |
| 2026-11-09 caps-r6 | F4/F5 Read-first list omits *Tab routing*; declared-convention sentence literally over-broad | logged | Cosmetic |
| 2026-11-09 caps-r7 | F1 Given non-symbol icon replaced by a fitting one | rejected | Supervisor ruling, missing from the prompt's settled list |
| 2026-11-09 caps-r7 | F2 "Load it only when…" pointed at the wrong guide | closed | "Load this guide" |
| 2026-11-09 caps-r7 | F3 Nav-bar parenthetical overclaimed | closed | Baseline sentence restored |
| 2026-11-09 caps-r7 | F4 Library comment used process wording | closed | Library's own terms |
| 2026-11-09 caps-r8 | F1 Nav-bar sentence untrue for tabbed scenes | closed | Tabbed scene's title rides in its tabs' breadcrumbs |
| 2026-11-09 caps-r8 | F2 SwiftUI intro load rule lost its mandate half | closed | Matches the Compose intro |
| 2026-11-09 caps-r8 | F3/F4 Deferral reason vs. tab bars; library label comment's input list | logged | Cosmetic |
| 2026-11-09 caps-r9 | F1 One rule's closing sentence put its guarantee after the tabbed exception | closed | Guarantee first, exception last |
| 2026-11-09 caps-r9 | F2 Tab examples' `// from the inputs` comments | logged | Cosmetic |
| 2026-11-09 caps | Series caps (size pass) converged by supervisor ruling | closed | — |
| 2026-11-09 compose-r1 | F1 Library declares Navigation Compose and Material as `implementation`; guide's setup list reads as complete | closed | Supervisor chose the library fix: both builds expose their public-signature dependencies as `api`; a consumer declaring only the SKAI artifact compiles, and fails with 28 unresolved references under the old `implementation` scope |
| 2026-11-09 compose-r1 | F2 Production *Modal routing* didn't place `ModalNavHost`; only the placeholder guide said `Box` | closed | *Modal routing* owns the `Box` placement; placeholder bullets point to it |
| 2026-11-09 compose-r1 | F3 View-model provider rule and STOP in both guides | closed | Owned by *Scene state, events, and effects*, now in the placeholder read-first list |
| 2026-11-09 compose-r1 | F4 Production tab host kind unstated | closed | "plain tab `NavHost` (tabs swap in place, not `SlideNavHost`)" |
| 2026-11-09 compose-r1 | F5 Spec's September table names `bottomSheet` for `sheet` | closed | Spec 2026-11-09 records `bottomSheetModal`; guide unchanged |
| 2026-11-09 compose-r1 | F6 Breadcrumb "opens on the current segment" | closed | "pinned to the current (trailing) segment", per `PlaceholderScene.kt` scroll |
| 2026-11-09 compose-r1 | F7 SwiftUI aside in the Layout bullet; siblings in older text | closed / logged | Layout aside deleted; older siblings outside the change |
| 2026-11-09 compose-r1 | F8 Tab example shows no `Box`/`ModalNavHost` | logged | The *tab* prose says modals ride in the same `Box`; a copy fails to compile, not silently |
| 2026-11-09 compose-r1 | F9 `ModalStyles` "property name, keeping its exact map ID" | logged | Example shows camelCase name with exact `id` |
| 2026-11-09 compose-r1 | F10 Hilt API list | closed | Parenthetical deleted |
| 2026-11-09 compose-r1 | F11 Library pointer twice in the placeholder intro | closed | Folded into the read-first list |
| 2026-11-09 compose-r1 | Q Production tab taps through the view model; no pop effect for pushed routes; "Android-only scenes" wording; `common:` STOP parity; literal include path | logged | Open questions, no defect shown |
| 2026-11-09 compose-r2 | F1 Modal `Box` placement undefined for a scene that also pushes; production example drew no `Box` | closed | *Modal routing*: over the `SlideNavHost` when the scene pushes; example draws the `Box` |
| 2026-11-09 compose-r2 | F2 "the same `Box`" in *tab* has no referent | closed | "the scene's modal `Box`" |
| 2026-11-09 compose-r2 | F3 Tabbed-only "no host" while the library hosts a tab `NavHost` | logged | The operator writes no host; supervisor asked for less library internals |
| 2026-11-09 compose-r2 | F4 Placeholder-only view model with no SwiftUI counterpart | logged | Older text, outside the change; touches the logged production-leaf item |
| 2026-11-09 compose-r2 | F5 "plain `NavHost` swaps in place" (default fades) | closed | Claim removed: "plain tab `NavHost` (not `SlideNavHost`)" |
| 2026-11-09 compose-r2 | F6 `common:` scenes lack SwiftUI's no-shared-module STOP | logged | Stranded; the blocked-gate route catches it |
| 2026-11-09 compose-r2 | F7 Read-first entry for *Scene state, events, and effects* | closed | Removed; the point-of-use pointer stays |
| 2026-11-09 compose-r2 | Q `viewModel()` not supplied by the library | logged | Verified by consumer build: `ViewModel` and `collectAsStateWithLifecycle` resolve, `viewModel()` doesn't; the guide leaves the provider to the project with a STOP |
| 2026-11-09 compose-r2 | Q Child start destination in view state; `rememberBottomSheetNavigator` name collision; tab order source | logged | No defect shown |
| 2026-11-09 compose-r3 | F1 Placeholder "never add Hilt wiring" contradicts production Hilt-by-convention | closed | Clause deleted; production *Scene state, events, and effects* owns DI |
| 2026-11-09 compose-r3 | F2 Nav + modal scene can paste two `viewEffects` collectors; a `receiveAsFlow` channel splits between them | closed | `FooViewEffect` bullet: collected by a single `LaunchedEffect` that handles every effect |
| 2026-11-09 compose-r3 | F3 Placeholder nav example passes `navController` positionally into `modifier` | closed | Named argument, per `SlideNavHost.kt` signature |
| 2026-11-09 compose-r3 | F4 `ModalStyles` removal rule restated with a different "what stays" list | closed | "Like `DomainColors`, `ModalStyles` is temporary." |
| 2026-11-09 compose-r3 | F5 Compose doesn't name the README's Modal Styles section | logged | Older text, off-normal |
| 2026-11-09 compose-r3 | F6 Dismissal bullet under "Effects come from" | logged | Older text, cosmetic |
| 2026-11-09 compose-r3 | F7 Setup STOP doesn't name the SDK floor | logged | Closed setup list and the convention-change rule already stop it |
| 2026-11-09 compose-r3 | F8 "the scene's modal `Box`" coined label | closed | "the `Box` with the scene's `ModalNavHost`" |
| 2026-11-09 compose-r3 | Q `ModalNavHost(isComposite)` undocumented; `CloseModal` on an idle host; no debug route check in the Compose library | logged | Library-level, no guide defect shown |
| 2026-11-09 compose-r4 | F1 One-collector rule not visible at the routing examples (r3 F2 reproduced at the copy point) | closed | Comment on the *Modal routing* example's `LaunchedEffect`; the `FooViewEffect` bullet stays the owner |
| 2026-11-09 compose-r4 | F2 Missing-modal-style STOP restated in *Modal routing* | closed | Clause deleted; *Build philosophy* and *Finding disposition* own it |
| 2026-11-09 compose-r4 | F3 Library behavior restated: modal Behavior column; Layout bullet's equal share; crumb-less root | closed / logged | Behavior column cut; equal share is older text; crumb-less root is the 2026-09-02 full-bleed decision |
| 2026-11-09 compose-r4 | F4 Route-files and marker sentences under *View models and DI* | logged | Older text |
| 2026-11-09 compose-r4 | F5 No rule for shared vs Android-only scene placement | logged | Stranded; project convention and *Finding disposition* cover it |
| 2026-11-09 compose-r4 | F6 `ModalStyles` "readable title" has no source | logged | The example shows Title Case of the ID |
| 2026-11-09 compose-r4 | Q Child start destination in view state; `DomainColors`/`ModalStyles` package unstated on both platforms; setup STOP routed via *Finding disposition* | logged | No defect shown |
| 2026-11-09 compose-r5 | F1 Audit status of existing M2 `bottomSheet` destinations undecided | closed | Follows the spec's "`bottomSheet` stays for legacy code": "existing `bottomSheet` destinations stay" |
| 2026-11-09 compose-r5 | F2 "recorded in Plan and done in Build" reads two ways | closed | SwiftUI shape: "mechanical setup this skill owns in Build" |
| 2026-11-09 compose-r5 | F3 `PlaceholderColors.domain(index)` stated twice | logged | Older text |
| 2026-11-09 compose-r5 | F4 Tab icon clause doesn't reject the library's default star | logged | Older #57 text; the clause already requires a fitting icon |
| 2026-11-09 compose-r5 | F5 "at the `NavHost` declaration site" names no host | logged | Older text; the example and table place every standard builder in `ModalNavHost` |
| 2026-11-09 compose-r5 | Q Placeholder view model × DI STOP on a greenfield shared module; `navigatePush` same-class no-op | logged | Settled / library behavior |
| 2026-11-09 compose-r6 | F1 Setup STOP routed through *Finding disposition* instead of a blocked gate | closed | "STOP at a blocked gate", as on SwiftUI |
| 2026-11-09 compose-r6 | F2 "this skill … in Build" without an antecedent | closed | "the implementation skill owns in Build" |
| 2026-11-09 compose-r6 | F3 Placeholder *Route enums* section restates the route-file rule | logged | Older text |
| 2026-11-09 compose-r6 | F4 *tab* restates "in its own file" and `@Serializable` | closed | "(one case per tab)" |
| 2026-11-09 compose-r6 | F5 *Child routing* start destination in view state vs *State ownership* | logged | Older text outside the change; raised as an open question in r1, r2, r4 |
| 2026-11-09 compose-r6 | F6 Tab example uses `Icons.Default.Menu` for Folders | logged | Older #57 example |
| 2026-11-09 compose-r6 | F7 Three names for one library | logged | Resolved by the intro's parenthesis |
| 2026-11-09 compose-r6 | Q Android-only module in a KMP project with both artifacts on one classpath; `collectAsStateWithLifecycle` vs project convention; `Sample.kt` builds a style inline | logged | No occurrence; settled; non-normative |
| 2026-11-09 compose-r7 | F1 Setup "inspect the consuming module" misses the settings include | closed | "Inspect the Gradle settings and the consuming module first" |
| 2026-11-09 compose-r7 | F2 Builder-source rule stated three times in the placeholder guide | closed | *Modal style descriptors* sentence deleted; the API bullet and *modal* keep it |
| 2026-11-09 compose-r7 | F3 "Never copy the library sources or hand-roll substitutes" has no SwiftUI counterpart | logged | Guards the vendoring failure mode; one sentence |
| 2026-11-09 compose-r7 | F4 *Placeholder scenes* pointer before *State ownership* | logged | Older text, reading order only |
| 2026-11-09 compose-r7 | F5 `DomainColors`/`ModalStyles` package unstated | logged | Same on SwiftUI; a wrong source set fails the build |
| 2026-11-09 compose-r7 | Q KMP project with an Android-only scene module gets both artifacts (duplicate classes); README omits the Kotlin Gradle plugin floor | logged | Raised r6 and r7; no occurrence; library/README scope |
| 2026-11-10 compose-r1 | F1 reopened by supervisor ruling (skai#133): the app owns its dependencies | closed | `api` reverted to `implementation` at the oldest versions the sources build with (each floor fails one release lower); unused AppCompat, Core KTX, Material Components, extended icons and BOM dropped; core icons and kotlinx-serialization-core, which the sources import, declared; guide's "exactly one artifact" and serialization-plugin sentences cut |
| 2026-11-10 compose series | Stopped by supervisor ruling after r7 | closed | r7's two cosmetic findings fixed; F3–F5 and the both-artifacts question stay logged |
| 2026-11-10 131-r1 | F1 production *Tab routing* doesn't say the container selects by `id`; equality tagging breaks value-carrying tab routes | closed | Closing sentence: "matching tabs by `id`, not `==`"; superseded by the route-identity ruling, which makes `==` correct |
| 2026-11-10 131-r1 | F2 ui-map-swiftui.md 16 bytes over its 10,050 cap | closed | Reviewer's tightenings in *Route enums* and *Tab routing*; 10,050 |
| 2026-11-10 131-r1 | F3 a tab enum's `id` has no production use at its point of use | logged | Compile error at `PlaceholderTab` catches a dropped conformance; F1's sentence gives `id` its use |
| 2026-11-10 131-r1 | F4 placeholder guide doesn't say a tap writes the tab's declared `route:` value | logged | Stranded, not broken: *New-scene inputs — none* sends unsourced values to STOP; codify on recurrence |
| 2026-11-10 131-r2 | F1 *Tab routing* says to match tabs by `id` with no mechanism shown | closed | Supervisor ruling: a route's identity is its whole value (`var id: Self { self }`), so plain `.tag(route)` matching is correct; sentence restored to its pre-series text |
| 2026-11-10 131-r2 | F2 "keeping navigation out of the view model's file" reads against route state on the view model | closed | Pre-series wording restored |
| 2026-11-10 131-r2 | F3 `DashboardNavRoute` declared twice with different shapes (*Route enums*, *Nav routing*) | logged | Older text outside the change; the compiler and destination initializer catch a dropped value |
| 2026-11-10 131-r2 | F4 placeholder read-first list omits *Tab routing* | logged | Older text outside the change; a wrong `currentTabRoute` shape fails to compile |
| 2026-11-10 131-r2 | Q per-case `id` on `item:`-bound routes vs *State ownership*'s "a new value moves to a different destination" | closed | Same ruling: whole-value identity; per-case `id` switches removed from every example |
| 2026-11-10 131-r3 | F1 "a new associated value is a new destination" hides that the same case with a new value is a new screen | closed | "new screen" in *Route enums* and *State ownership* |
| 2026-11-10 131-r3 | F2 whole-value identity alone doesn't give nav or child destinations a new screen on a new value (simulator-verified; `.id(route)` on the destination does) | closed | Supervisor ruling: `.id(route)` on nav and child destination content, clause in *Route enums*; cap 10,170 |
| 2026-11-10 131-r3 | F3 *Route enums* admits any construction value; spec's event clause not in the guide | logged | The event clause is rationale; a non-identity value in a route shows itself as a re-presented screen |
| 2026-11-10 131-r3 | F4 *Tab routing* doesn't say how tabs are matched to the route | closed | "tagging each tab with its route case" |
| 2026-11-10 131-r3 | Q library offers a tabs-plus-embedded initializer the guide forbids | logged | Library shape outside route identity |
| 2026-11-10 131-r4 | F1 placeholder nav and child examples omit `.id(route)` | closed | Supervisor ruling: `.id` on the placeholder nav and child destinations (the wrapped child's `NavigationStack` included); cap 15,160 |
| 2026-11-10 131-r4 | F2 `.id(route)` clause introduced an example it doesn't illustrate | closed | Clause moved after the *Route enums* example |
| 2026-11-10 131-r4 | F3 whole-value identity needs `Hashable` associated values; guide silent | logged | STOP route covers it; codify on recurrence |
| 2026-11-10 131-r4 | F4 *Modal routing* enum bodies elided | logged | *Route enums* rule is unambiguous; no cap room |
| 2026-11-11 131-r5 | F1 wrapped-child `.id` placement rests on one uncommented example | closed | Comment: "`.id` on the stack" |
| 2026-11-11 131-r5 | Q whether a UI Map audit flags existing nav or child destinations missing `.id(route)` | logged | Implementation guide's audit scope; outside this change |
| 2026-11-11 compose caps | Efficiency review against the SwiftUI guides: `ui-map-compose.md` efficient (extra size is the library and state/event/effect sections plus Compose example code); placeholder guide had SwiftUI comparisons and restatements | closed | Fixed the stale serialization-plugin pointer and cut the modal Behavior column (compose-r4 F3's cut had not held); cut *The one rule*'s SwiftUI comparison, the duplicate `PlaceholderColors.domain` API entry, the top-app-bar SwiftUI clause and three restatements in *View models and DI*; scaffold-marker sentence kept (point of use, regression-tested). 13,312 → 13,135; 17,013 → 16,481. Caps 13,150 and 16,500 |
| 2026-11-11 compose-trim | F1 production `full_screen` content draws under the status bar; guide silent | logged | Not caused by the trim (the removed column said only "full-height Material 3 sheet"); content insets are feature work (D7) |
| 2026-11-11 compose-trim | F2 *View models and DI* points at *Scene state, events, and effects* without naming its file; read-first list omitted it, so the DI rule and STOP never reach the placeholder operator | closed | Section added to the read-first list; reviewer tightenings "Placeholder-only:" lead and "(examples use plain `viewModel()`)"; 16,499 |
| 2026-11-11 compose trim | Stopped by supervisor ruling after r1 | closed | F2 fixed; F1 logged |
| 2026-11-11 131 series | Stopped by supervisor ruling after r5 | closed | r5 F1 fixed; logged items stay logged |
| 2026-11-11 57-backout-r1 | F1 neither placeholder guide says a tab's label is its scene's name after the #57 rule's removal | closed | *tab* sentence in both guides: "Label each tab with its scene's name, as `title` is" |
| 2026-11-11 57-backout-r1 | F2 implementation invariant lacks P6's designs-and-specs sentence | logged | Lines 28 and 238 already keep feature work out of `handoff`; restating would duplicate them |
| 2026-11-11 57-backout-r1 | F3 SwiftUI "Tabbed + embedded" preview labels differ from their scene titles | logged | Previews aren't operator inputs; library file outside the change |
| 2026-11-11 57-backout-r1 | F4 Compose tab icon source (icon sets the app links) unstated | logged | One unobserved case; a red build stops at the standing blocked gate |
| 2026-11-11 57-backout-r2 | F1 "its scene's name, as `title` is" could be read as the tabbed scene's own title | logged | Cosmetic; example and library comment resolve it |
| 2026-11-11 57-backout-r2 | F2 SwiftUI real-screen deferral names a missing trigger API, which a tab bar doesn't need | logged | Default path stops in Discussion as intended; Compose and implementation guides say "mapping" |
| 2026-11-11 57-backout-r2 | F3 scene-name label rule doesn't reach a tab on a real bar | logged | Behind the real-screen deferral; sharpen when the mapping lands |
| 2026-11-11 57-backout-r2 | F4 SwiftUI library previews omit `systemImage` | logged | Library previews, not operator inputs; guide rule is clear |
| 2026-11-11 57-backout | Series stop | closed | r2 scored 0 over the current text |
| 2026-11-11 67-r1 | F1 map guide taught two scene forms, one modal style and multiple-inbound → `primary_parent` as exhaustive | closed | *Scenes*, *Modal styles*, *Reused scenes* and the authoring rule admit the form-factor cases |
| 2026-11-11 67-r1 | F2 form-factors guide example wasn't a valid map | closed | Full envelope; renders |
| 2026-11-11 67-r1 | F3 "naming what to declare" overstated the renderer errors | closed | Errors name the conflict; resolve against intended screens and routes |
| 2026-11-11 67-r1 | F4 code stop missed an unmarked screen with a modal-style map; audit and Inputs didn't carry form factors | closed | Stop covers anything that differs; per-form-factor comparison; Inputs records addenda and documents |
| 2026-11-11 67-r1 | F5 architecture artifacts over its cap | closed | 5,913 / 5,920 |
| 2026-11-11 67-r2 | F1 missing form-factor pattern had two homes | closed | Form-factors guide: add it "there, not to the implementation addendum" |
| 2026-11-11 67-r2 | F2 single-parent nesting rule would flatten a domain root | closed | "unless it roots its own domain" |
| 2026-11-11 67-r2 | F3 `platform` comparison asserted a codebase count | closed | Deleted |
| 2026-11-11 67-r2 | F4 Compose modal-style descriptor naming vs its example | closed | camelCase property, exact map ID as `id` |
| 2026-11-11 67-r3 | F1 reused-scene rule excluded a domain root | closed | "as a domain root, in a domain's `scenes:` list, or in `common:`" |
| 2026-11-11 67-r3 | F2 valid IDs can convert to reserved words (`class`) | logged | Hypothetical; a failed build stops at the standing blocked gate; first sighting |
| 2026-11-11 67-r3 | F3 renderer sentence read as rejecting root screens | closed | "non-root screens" |
| 2026-11-11 67-r4 | F1 reused-scene home list vs "define it under the route you want it drawn in" for a two-parent scene | logged | Older text both sides; the visual-home section falls back when the scene is defined elsewhere; first sighting |
| 2026-11-11 67-r4 | F2 implementation gates don't show the render or why there is none | logged | Outside #67; candidate for the next implementation-guide pass |
| 2026-11-11 67 | Series stop | closed | r4 scored 0 over the current text |
