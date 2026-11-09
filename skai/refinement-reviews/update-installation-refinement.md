# Update installation guide — refinement working document

Target: `Guides/Core/update-installation-guide.md` (12,427 bytes at start; cap 12,500 whole file) and `Templates/skills/skai-update-installation/SKILL.md` (thin dispatcher). Standard: `skai/refinement-reviews/maintainer-migration-design.md` § Release Documents — 2026-10-18. Tier: lightweight. Reviewer: Codex `gpt-6-astra`, read-only, prompt filled from `Guides/Process/cold-review-prompt-template.md` verbatim.

Series 1 inputs: scoring model as of 2026-10-14 template; files under review as above; spec as amended 2026-10-18 (on-or-after, runbooks in Scope); no report charter.

## Round score

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 11.25 | 4 | 0 | 4 | 0 | 0 |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r4 | 0 | 0 | 0 | 0 | 0 | 0 |

## Round 1 (2026-10-18, Codex gpt-6-astra, report `scratchpad/review-r1.md`, 16,643 bytes)

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 Target checkout may lack `Releases/` (v13, today's latest tag, predates them); the guide reads documents from the target checkout | supervisor decision | spec § updater reads every intervening release; guide step 4–5 | (a) none in the guide: transitional until v14 is cut, a target older than the documents is a downgrade caught by the generic blocked gate — plus a transitional note in `Releases/unreleased.md` for hosts ≤13 running the old guide; or (b) one line in step 5 naming the source and the blocked case (~110 bytes, over cap without a trim) | target selection, ascending range, target-specific unreleased selection |
| F2 Gate line `Next: Run the runbooks` and `auto` "directly into the runbooks" skip step 5b | accept | spec § invariants (gate as today); guide Gates/Advance intent/step 5.5 | sharpen the three transition sentences to one sequence (gate → 5b → runbooks); net +20 bytes | the two planned gates; inline/app handoff; auto enables all; blocked cases |
| F3 Step 6 "each document applied whole" would re-include unreleased entries the date cutoff excluded (+ open question: "no document applies" vs empty selection) | accept | spec § updater step (release docs whole; unreleased by date); guide step 6, step 5.4 | step 6 consumes "the scope step 5 reported: release documents whole, then the selected unreleased entries"; 5.4 "no document or entry applies"; net +3 bytes | whole-release catch-up, re-run no-ops, guards |
| F4 Configuration tool/app decline and New-section newness are host-wide while the guide collects `newComponents` per adapter | routed (outside the binding target: `Bin/skai-configuration.py`, `internal/apps/ConfigureSKAI`) | component-selection contract | tooling fix, owner: configuration tool; not this pass | guide text unchanged |
| F5 Commit target with no `lastUpdatedAt` has no cutoff | log only | guide step 1/5.3 | none now (strands at the generic blocked gate; single observation) | inclusive cutoff |

### Round score

F1 supervisor decision, live today: divergent · normal · verified = 5 · F2 divergent · normal · speculative = 2.5 · F3 (+ the open-question wording, same scope-handoff defect) divergent · off-normal · speculative = 1.875 · F4 outside the binding target, routed to the configuration tool · F5 log only, live gap: divergent · off-normal · speculative = 1.875

`| r1 | 11.25 | 4 | 0 | 4 | 0 | 0 |`

### Repairs

- Cluster A (F2): step 5.5 gate line now `⏳ GATE: Next: Offer any new components, then run the installed adapter update runbooks. Say "next" or what to change.`; Advance intent: "`auto` may bypass the release-documents gate; step 5b still runs before the runbooks."; Progress tracking: "wait for approval before step 5b and the runbooks". Self-check: Gates section already orders new-components after release-documents and before runbooks (no contradiction); README phase text ("before any runbooks are re-run") still true; no stale sentence; rule stays at the gate; no weakening. 12,427 → 12,447 bytes.
- Cluster B (F3 + empty-selection wording): step 6 first bullet "applies the scope step 5 reported: each release document whole, in order, then the selected unreleased entries (…)"; step 5.4 "If no document or entry applies". Self-check: re-run bullet still says the release document is applied again whole (consistent); step 5.3 selection unchanged; no stale text. → 12,450 bytes.
- Sanity scan after both edits: `grep -i 'changelog\|Next Command\|checkpoint\|process-flow.md\|🟡\|- \[ \]\|directly into'` → 0 occurrences; `\bhuman\b` → 1 (supervisor definition, intentional); gate lines: template (15–25), 43, 54, 164, each traces to `## Gates`; header date 2026-10-18 (edited today); size 12,450 ≤ 12,500. Post-edit simulations re-run for Host A/B/D on the changed transition: gate → 5b → runbooks in every case; under `auto` 5b enables all then runbooks. No issues found in simulation.

### Closure (round 1)

| Finding | Status | Evidence |
|---|---|---|
| F1 | still open — supervisor decision | presented in the report; no guide edit |
| F2 | closed | the three transition sentences name the same sequence (lines 64, 67, 164) |
| F3 | closed | step 6 consumes the reported scope; 5.4 covers the empty selection |
| F4 | routed | configuration tool/app; follow-up for the supervisor |
| F5 | logged | strands at the generic blocked gate; single observation; codify on recurrence |

## Command verification (before round 1)

- `git tag --list 'v*' --sort=-v:refname | head -1` → `v13` (highest tag).
- `git tag --list 'v*' --merged HEAD --sort=-v:refname | head -1` → `v13`; for the v12 commit → `v12`; for the first-parent commit after v11 → `v11`; for a side-branch commit that forked before v11 (`a5771a3`) → `v10`, correct (v11 is not its ancestor, `merge-base --is-ancestor` confirms).
- Unknown SHA → `error: option 'merged' must point to a commit` on stderr, empty stdout: "resolves nothing" in step 5.1 reads as the empty result; the guide should not rely on an exit code (pipeline exit is `head`'s).

### F1 ruling applied (supervisor, 2026-10-18: both (a) and (b))

- (b) Step 5 intro: "Both are read from the target checkout; a target older than the first release that carries `Releases/` is a blocked gate." Blocked case listed under workflow-specific blocked gates ("The target predates the first release that carries `Releases/` (step 5)"). Funded by trims: step 7 "visible in the transcript" → "visible"; step 6 "sequentially (one adapter at a time)" → "one adapter at a time"; step 5.1 parenthetical shortened; `auto` hard-case bullet generalized to "the blocked cases"; step 4 pointer sentence shortened. 12,450 → 12,484 bytes.
- (a) The CHANGELOG bridge line was added by the supervisor (Unreleased opens with the bold instruction); not edited by me.
- Self-check: the new blocked case is in `## Gates` and referenced at step 5 (no fabricated gate); `auto` wording still excludes every blocked case (the generalization covers the new one); no stale sentence; nothing moved away from its point of use. Sanity greps: 0 occurrences for the stale-term set; gate lines unchanged in count. Simulation: Host A targeting v13 under the new guide → blocked gate at step 5 with the reason; default target v14+ → documents present, normal path. No issues found in simulation.

## Round 2 (2026-10-18, report `scratchpad/review-r2.md`, 12,924 bytes; same series — the spec change between rounds recorded a settled disposition only)

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 "No fabricated gates" + broad `auto` leave delegated stops (runbook confirm, release-document stops) without authority | accept | spec § two documents (stops the agent makes); guide Gates/Advance intent/step 6 | one sentence in `## Gates`: delegated stops are that input's gates, emit its line or the blocked line, `auto` never bypasses them; +205 bytes, funded by trims | the two planned gates; adapter approval; blocked-gate rule |
| F2 Step 5b "launch as configure-skai.md describes … then continue" leaves the return undefined (double reconcile, premature completion, continue after cancel) | accept | guide step 5b; configure-skai.md § Reconcile after Save | sharpen 5b: verify the result per that section; verified Save returns here, step 6 reconciles once; cancelled/unresolved keeps that guide's stop; +~200 bytes | Save-and-Apply approval scope; inline route; `auto` route |
| F3 `auto to runbooks` names no planned gate | accept (reviewer: log-only; deterministic ambiguity, negative cost) | guide Advance intent | "`auto to runbooks` = STOP at the release-documents gate" (−8 bytes) | ordinary `auto`; both gate positions |
| Open question: first report is not the final inventory (component-history catch-up) | neither (open question, not pre-settled) | — | none | — |

### Round score

F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875 · open question neither. Findings about my own r1 repairs: 0 of 3.

`| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |`

### Repairs

- Cluster C (F1): sentence before "Workflow-specific blocked gates". Trims: Prerequisites to one line (points at the blocked gate), step 3 baseline/HEAD wording, new-components gate description, step 2 no-tag sentence. 12,484 → 12,417. Self-check: consistent with "No fabricated gates" (delegated gates are defined by their input); `auto` bullet still excludes blocked cases; Prerequisites still says what to run; nothing moved or weakened.
- Cluster D (F2): step 5b return path. → 12,623 (over cap). Self-check: verification stays delegated to the configure guide; reconciliation happens once at step 6; inline and `auto` routes untouched.
- Cluster E (F3) + trims: `auto to runbooks` alias; "(not that guide's own)"; progress bullet "No work document; state is inline."; step 1 drops "Preserve the chosen state path" (step 7 names the resolver's path); step 7 completion sentence; step 6 first bullet. → 12,409 bytes. Self-check: step 7 still names `historyStatePath`, so the dropped sentence loses nothing; the alias names an existing gate; no stale text.
- Sanity scan: stale-term grep → 0; `\bhuman\b` → 1 (supervisor definition); gate lines 15–25, 42, 56, 165 each trace to `## Gates`; header date 2026-10-18; size 12,409 ≤ 12,500. Simulations: Host B with new components via the app → Save → back to step 6 once; Cancel → configure guide's stop; `auto to runbooks` → stops at the release-documents gate; runbook confirm step under `auto` → still a gate (delegated). No issues found in simulation.

### Closure (round 2)

| Finding | Status | Evidence |
|---|---|---|
| F1 | closed | Gates sentence on delegated stops (line before "Workflow-specific blocked gates") |
| F2 | closed | step 5b: verified Save returns here, step 6 reconciles once; cancelled/unresolved keeps the configure guide's stop |
| F3 | closed | `auto to runbooks` = STOP at the release-documents gate |

## Round 3 (2026-10-18, report `scratchpad/review-r3.md`, 12,577 bytes; same series)

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 Each adapter runbook advances top-level `lastSHA`/`lastRelease`/`lastUpdatedAt` (runbook state rules, verified by the reviewer at Codex:193, Claude:195, Cursor:217); a retry after a partial multi-adapter update reports a shorter range at the release-documents gate | accept | spec § invariants (never nulled; range from `lastRelease`); guide steps 6–7 | one bullet at step 6: runbooks record their adapter entry and component history; the top-level fields advance only at step 7 after every adapter; +~230 bytes, funded by trims | pre-removal baseline capture; per-adapter provenance; component history; local/shared ownership; standalone runbook behaviour; `lastRelease` calculation |
| Open question: tag commands match `v*`, broader than `v<N>` | open question (not a finding; conditional on tags that do not exist) | — | none | — |
| Note: "repeat the document list at completion" lives in step 5, not step 7 | not raised as a finding by the reviewer | — | none | — |

### Round score

F1 divergent · off-normal · speculative = 1.875 · the tag-vocabulary item is an open question, neither. Findings about my own repairs: 0 of 1 (the handoff wording made it visible; the per-adapter top-level write predates this series).

`| r3 | 1.875 | 1 | 0 | 1 | 0 | 0 |`

### Repairs

- Cluster F (F1): step 6 loop header "one adapter at a time" (separate bullet removed); new bullet: "A runbook records its own adapter entry and component history as it completes; the top-level `lastSHA`, `lastRelease` and `lastUpdatedAt` advance only at step 7, after every adapter, so a retry after a partial update reports the same range." Trims: progress-tracking state bullet; first workflow-specific blocked gate; guard sentence reworded. 12,409 → 12,509 → ≤ 12,500 after the guard trim (size printed by the launch command).
- Self-check: step 7 still owns the top-level write (unchanged list); runbooks' own standalone behaviour is not edited (the exception is stated at the delegation point, as the reviewer recommended); Prerequisites still points at "the blocked gate above", whose wording changed but not its meaning; no stale sentence; nothing weakened.
- Sanity scan: stale-term grep → 0; `\bhuman\b` → 1 (supervisor definition); gate lines 15–25, 42, 56, 165 trace to `## Gates`; header 2026-10-18. Simulation: two-adapter host, first runbook succeeds, second blocks → top-level fields unchanged → retry reports the same range → second runbook completes → step 7 advances. No issues found in simulation.

### Closure (round 3)

| Finding | Status | Evidence |
|---|---|---|
| F1 | closed | step 6 bullet defers the top-level checkpoint to step 7 |
| tag vocabulary | logged (open question) | conditional; no `v`-tag outside `v1`–`v13` exists |

## Round 4 (2026-10-18, report `scratchpad/review-r4.md`, 9,257 bytes; same series)

No findings in the binding surfaces; the reviewer confirmed the runbook/guide state-write contract agrees (Codex:193, Claude, Cursor), the tooling claims by source inspection, the wrapper thin, and the size within cap. Open questions: none new (the v13 transition blocker is settled; the newness tooling item is the routed follow-up).

`| r4 | 0 | 0 | 0 | 0 | 0 | 0 |` — no live rows, no noise.

**Stop rule:** terminal by (a) — a fresh round over the current text produced no new live findings in the binding target. Convergence by clean round, not by ruling.

### Post-round ruled edit (supervisor, tag pattern)

After the clean round the two tag commands were narrowed to `'v[0-9]*'` per the supervisor's ruling (the runbooks were narrowed during round 4), funded by trimming "For the default, " in step 2. Commands re-verified: highest tag → v13; ancestor of HEAD → v13; ancestor of the side-branch commit → v10. Sanity scan: stale-term grep → 0; gate-line count unchanged (8); header 2026-10-18. Size: 12487 bytes ≤ 12,500. This is a mechanical change to two command patterns, not a repair of a finding; it is reported to the supervisor as a post-terminal edit.

## Closing the pass

| Finding | Status | Evidence |
|---|---|---|
| r1 F1 source of documents | closed (ruling) | step 5 source line + blocked case; CHANGELOG bridge line (supervisor) |
| r1 F2 gate transition | closed | three sentences name gate → 5b → runbooks |
| r1 F3 scope handoff | closed | step 6 consumes the reported scope; 5.4 "no document or entry" |
| r1 F4 newness tooling | routed | configuration tool follow-up for the supervisor to file |
| r1 F5 missing `lastUpdatedAt` | logged | strands at the generic blocked gate; single observation |
| r2 F1 delegated gate authority | closed | Gates sentence on active-input stops |
| r2 F2 configure return | closed | step 5b verified-Save return; cancelled keeps the configure guide's stop |
| r2 F3 `auto to runbooks` | closed | alias for the release-documents gate |
| r3 F1 per-adapter top-level writes | closed | step 6 bullet; runbooks' merge rule aligned (maintenance) |
| r3 tag vocabulary | closed (ruling) | `v[0-9]*` in guide and runbooks |

Net size change of the guide set: `update-installation-guide.md` 10,889 (before the maintenance pass) → 12,427 (pre-refinement) → 12487 bytes; wrapper unchanged (thin dispatcher). Cap 12,500 held at every handoff.

## Supervisor closure (2026-10-18)

Pass closed at 12,487 bytes after clean round 4; the post-terminal tag-pattern edit stands without a confirming round. Findings log updated with the closure row.
