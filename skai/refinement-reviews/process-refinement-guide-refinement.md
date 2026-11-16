# Process Refinement Guide — Refinement

Target: `Guides/Process/process-refinement-guide.md` (26,556 bytes at start) and `Guides/Process/cold-review-prompt-template.md` (18,489 bytes at start); no caps yet. Standard: `skai/refinement-reviews/process-refinement-guide-design.md`. Issues: skai#90, #130, #135, #136. Plan: [refinement-plan.md](refinement-plan.md). Tier: lightweight. Reviewer: Codex `gpt-6.1-terra`, reasoning high, read-only. Round 1 uses the starting template; from round 2 the prompt is built from the updated template and the updated guide is followed.

## Proposal (2026-11-13)

Drafted in `proposal-g/Guides/Process/`, diff in `refinement-g-proposal.diff`. Sizes: guide 26,556 → 29,384; template 18,489 → 19,842.

Self-check against the design spec: every requirement in *Refinement Guide Requirements* and *Review Prompt Template Requirements* that differs from the starting guides is drafted, and the drive-by blank line before *Scaling the ceremony* is fixed. Not drafted: the findings log's stale path note, which is outside both guides.

## Round 1 — Proposal Review

Prompt: `reviews-g/g-r1-prompt.md`. Output: `reviews-g/g-r1-out.md`. Not scored (proposal round).

Verdict: directionally sound; amend before applying. 7 findings, all speculative, none rejected.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Matrix's "score the round here" fires on the proposal round; working doc omits the score table | accept | Guide § Finding matrix, § working document | Score only rounds on applied text; list the score table |
| F2 Cap set after applying conflicts with an old cap binding every repair; cap step not conditional | accept (sequencing follows from the cap binding every repair; design spec updated) | Guide § Size budgets; spec § Decisions | Propose the cap after triage, before applying, from the settled shape measured on a temporary copy; only when a change sets or revises one |
| F3 Stop rule says "no new live findings", not "nothing to apply"; tier line says "clean round" | accept | Guide § Iterated review, § Scaling the ceremony, § Closing the pass; spec § Rounds | "Triaged findings leave nothing to apply"; tiers point to the stop rule; closure hands the change to the supervisor |
| F4 Settled dispositions can hide a failed closure | accept (drive-by, outside the change; small) | Template slot note, § Settled dispositions | Decisions only, never a claim a defect was fixed; a failure to carry one out is a finding |
| F5 Measuring instructions can leave out the proposed change; opening no-edit line lacks the exception | accept | Template § Size caps, opening | Measure the complete result; exception named at the opening |
| F6 First-round charge is per finding, not whole-change | accept | Template § Proposed edits | Assess as a whole and hunk by hunk, including moving, refactoring or removing existing text, with wording |
| F7 Supervisor-decision presentation assumes a process-weight tradeoff | accept | Guide § supervisor decision rule | For dropping content: why it adds no value and what tightening was tried |
| Open question: how a review-only pass enters a proposal-first flow | accept | Guide § When to use; spec § Process Flow | A pass with no proposed change starts with a round over the current text |

Settled shape (amended proposal): guide 29,923 bytes, template 20,174 bytes. Caps pending supervisor approval before applying.

## Rework (2026-11-13)

The first draft appended the change beside the old text (+3,367 / +1,685). Reworked by rewriting: the guide's sections are reordered to follow a pass (records, commissioning, triage, matrix, repairing, verifying, rounds, closing), the cap rules merged into one paragraph, supervisor decisions and design contradictions folded into triage, and the template's refiner-facing notes tightened. Sizes: guide 26,556 → 23,619; template 18,489 → 19,196.

### Cuts For Supervisor Approval

Already left out of the reworked draft; approved by the supervisor 2026-11-13:

| # | Guide | Cut | Why |
|---|---|---|---|
| C1 | Guide § Verify | "If the guide says a tool enforces something, confirm it still does." | Restates the line before it |
| C2 | Guide § Verify | "the guide keeps promising what the tool stopped doing" | Explanation; the rule stands without it |
| C3 | Guide § Verify | "resolving to be more careful has a poor track record against it" | Explanation |
| C4 | Guide § Verify | "and it crowds out the judgment work only a fresh reader can do" | Explanation |
| C5 | Guide § Full apparatus | "weight calibrated for a large, in-use, multi-doc workflow" | Restates the when-to-use clause that follows |
| C6 | Guide § Round score | "A low score is not convergence; the stop rule above decides that." | Restates "a monitor, never the stop criterion" |
| C7 | Guide § Findings log | "Keeping those two distinct is what lets the review stay fresh while still not relitigating." | Explanation |
| C8 | Guide § Lightweight tier | The list "triage, finding matrix, cluster-at-a-time repair with the self-check, closure list, findings log" | Replaced by "Everything above" |
| C9 | Template § Legacy | "not whether old files conform" | Restates the sentence's first half |

Proposed for cutting; approved by the supervisor 2026-11-13 and removed:

| # | Guide | Cut | Why |
|---|---|---|---|
| C10 | Guide § Records | "This is the same working-doc convention used by the dev specs and UI Map workflows: process artifacts are kept out of the target's own committed files." | Points at other workflows; the location rule is the working-doc guide's |
| C11 | Guide § Closing | "Closing on intent is how a bug survives its own repair: three closures in one refinement effort were recorded against fixes that did not work, and each one then suppressed the finding when a later round raised it again." | An incident story; the rule before it stands alone |
| C12 | Guide § Stop rule | "The old convergence shape — all in scope, all sharpen-level, no bloat flags — is an approach signal, never the stop." | Refers to a stop rule the guide no longer has |
| C13 | Guide § Verify | "It is minutes of expensive reasoning; a script is a second and never forgets a case." | Explanation |

After cuts: guide 23,041 bytes, template 19,196 bytes. Proposed caps: guide 22,800; template 18,489 (its starting size).

Caps approved 2026-11-13 (guide 22,800; template 18,489) and recorded in the design spec. Settled change applied to both guides; slot names consistent between the template's notes and its prompt; section references resolve; no live document cites the old section names (only historical release notes).

## Round 2 — Applied Text (Updated Template)

Prompt: `reviews-g/g-r2-prompt.md`, built from the updated template. Output: `reviews-g/g-r2-out.md`. Series S2 (own series; prompt and guide change each round under self-application).

Verdict: usable with care. 2 findings plus measured trims (reviewer's copy: guide 22,759, template 18,195).

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Self-review can omit one of the two guides | accept | Guide § Commissioning; template intro | A review of either one has both as its target |
| F2 Cleanup bans compete with tightening to meet a cap | accept | Guide § Repairing; template § Editing discipline | Cleanup ban excepts tightening to meet a cap |

Trims: departed from the reviewer's wording where it dropped content without supervisor approval — template trims 1, 3, 4, 5 dropped examples or the reviewer's motivation sentence, guide trims 1 and 2 dropped reasons, guide trim 4 changed meaning. Instead tightened wording elsewhere and removed duplicated text (verified/speculative defined twice, Style restating the opening, "where each fix belongs" stated twice, the triage paragraph restating that the review is aggressive). Guide trim 3 and template trim 2 taken in reworded form.

After repair: guide 22,794 (cap 22,800); template 18,384 (cap 18,489).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r2 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875

## Round 3 — Applied Text (Updated Template)

Prompt: `reviews-g/g-r3-prompt.md`, built from the template as repaired after round 2. Output: `reviews-g/g-r3-out.md`. Own series.

Supervisor (2026-11-13): converge on the change first, with the change charter; a whole-guide audit against the design spec follows as its own pass.

Verdict: usable on the main path. 2 findings, both accepted; reviewer measured guide 22,741, template 18,384.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 "Trivial copy edits skip it" overrides the supervisor's choice (the design spec's Entry had the same line, from the backfill) | accept | Guide § When to use; spec § Entry | Line removed from both |
| F2 Log consultation reopens a closure only "with the same surface" | accept | Guide § Records | "and still reproduces" |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r3 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875

## Round 4

Verdict: usable; 2 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 "At least two rounds" vs a stop rule a review-only round 1 can meet | accept, different fix: the two-round minimum follows from applying a change; a review-only pass whose first round leaves nothing to apply rightly ends there | Guide § When to use; spec § Process Flow | "A pass that applies a change has at least two rounds" |
| F2 The prompt's codification check lacks the guide's exceptions, and "reserve accept" over-restricts | accept; kept the three examples the reviewer's wording dropped | Template § Editing discipline | Exceptions restored; wrong-action text is a defect whatever its likelihood |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r4 | 5.0 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · normal · speculative = 2.5

## Round 5

Verdict: usable; 1 finding.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 `reject`'s example "treats a hypothetical misuse as a normal-use failure" can discard a real defect whose reachability was mislabeled | accept, different fix: deleting the example would drop content without approval; reworded so it rejects only a finding resting on a hypothetical misuse | Guide § Triage | "or rests on a hypothetical misuse rather than on what the text says" |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5

## Round 6

Verdict: usable; 2 findings. The consolidation trigger fired once: round 5's `reject` fix became this round's F1, so the category was rewritten whole against the design spec ("doesn't establish a live defect; reasoning from the documents alone is not grounds to reject").

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 `reject` could discard a text-grounded hypothetical misuse | accept; rewritten whole | Guide § Triage | "or posits a misuse the text doesn't support" |
| F2 Pre-round check doesn't name failure branches | accept; kept the "does it parse" contrast | Guide § Verify | "failure branches included" |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r6 | 5.0 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · normal · speculative = 2.5

## Round 7

Verdict: usable for the principal workflow; 1 finding, outside the change.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The reviewer may read only the prompt and named files, yet must read the implementation behind every tool claim; the design spec states both | supervisor decision: a design contradiction, predating this change (the starting template had the same boundary). Proposed: defer to the whole-guide audit pass | Spec § Commissioning, § Tool claims; guide § Commissioning; template intro and opening | — |

Trims proposed by the reviewer drop an explanation and an example; not taken (nothing to fit).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r7 | 1.875 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 (pre-existing; outside the change)

Supervisor (2026-11-13): round 7's F1 fixed in this pass, not deferred. The reviewer may read the code behind any tool claim it checks, never an excluded file; an excluded implementation leaves the claim reported as unchecked. Applied to the design spec (§ Commissioning, § The task), the guide (§ Commissioning a round) and the template (intro, prompt opening, § Verify claims about tooling). Template tightened to fit (excluded-files, report-charter and observed-failures sentences reworded). Sizes: guide 22,800 (cap 22,800); template 18,485 (cap 18,489).

## Round 8

Prompt: `reviews-g/g-r8-prompt.md`. Output: `reviews-g/g-r8-out.md`.

Verdict: usable; 1 finding.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The refiner-facing handoff lines give the reviewer tool code without the excluded-file boundary | accept; superseded by the supervisor's broader ruling below, whose wording carries the boundary into every handoff line | Guide § Commissioning; template intro | "never a file it excludes" |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r8 | 1.875 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875

Supervisor (2026-11-13): the reviewer reads the named files and everything they reference, never an excluded file; referenced content counts as part of the guide that cites it. Replaces the tool-code rule, which becomes a case of it. Applied to the design spec and both guides; tightened to fit (guide 22,792, cap 22,800; template 18,478, cap 18,489).

## Round 9

Prompt: `reviews-g/g-r9-prompt.md`. Output: `reviews-g/g-r9-out.md`.

Verdict: usable on the principal path; 1 finding.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Reading what the guides reference can lead the reviewer into the findings log or the refinement guides; the exclusion slot was optional and didn't name them | accept | Template § How to fill it, prompt opening, intro; guide § Commissioning; spec § For the refiner | `{{EXCLUDED_SURFACES}}` made required, always naming the findings log and, unless targeted, both refinement guides; "referenced content counts as part of its citing guide" |

Reviewer trims dropped meaning (the prose-drift premise, the "highest-yield check" guidance); not taken. Fit by removing the settled-decisions note's restatement of why the log is withheld and other rewording. Sizes: guide 22,784 (cap 22,800); template 18,488 (cap 18,489).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r9 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5

**Consolidation trigger, second firing** (round 5 → 6, then round 8 → 9): moving to the structured tier for the rest of the pass.

Invariants:
- **P1** The reviewer reads every named file and everything it references, tool code included.
- **P2** The reviewer never reads an excluded file; the findings log is always excluded, and the two refinement guides are unless they are the target.
- **P3** The prompt's fixed wording, used verbatim, carries every reading rule the reviewer must follow.

Ownership:

| Content | Canonical owner | Derivative surfaces |
|---|---|---|
| Reading set and exclusions | Template prompt: opening line and § Files you must not read; `{{EXCLUDED_SURFACES}}` note | Guide § Commissioning a round; template intro; spec § Commissioning, § For the refiner, § The task |
| Tool-claim checks | Template prompt § Verify claims about tooling | Guide § Verify (the refiner's own runs); spec § Tool claims |

Impact map for F1: owner edited first (the slot note and prompt opening), then every dependent found by searching both guides and the spec for "findings log", "must not read", "excluded" and "files it names"; all consistent.

## Round 10

Prompt: `reviews-g/g-r10-prompt.md`. Output: `reviews-g/g-r10-out.md`. Structured tier.

Verdict: usable for the main sequence; 2 findings, both in the cap workflow.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Cap formulas overlap: "new content" can also be an addition to an existing guide | accept; the spec had the same overlap and is corrected too | Guide § Size caps; spec § Decisions | "for a new guide … ; for an existing guide …" |
| F2 The measuring copy can leave out the reviewer's own recommended fixes | accept | Template § Size caps | "apply all your recommended fixes, any proposed change as amended, and your trims" |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r10 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · normal · speculative = 2.5
## Round 11

Prompt: `reviews-g/g-r11-prompt.md`. Output: `reviews-g/g-r11-out.md`.

Verdict: usable for the ordinary path; 2 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Triage says "codify on recurrence" while *Across passes* says the third sighting codifies | accept; threshold moved to the decision point, *Across passes* now points at it | Guide § Triage, § Across passes | "a first sighting … `log only`, a second in a different case is considered, a third codified" |
| F2 The existing-guide cap formula needs an old cap an uncapped guide doesn't have | accept as the refiner's call, not a supervisor decision: the D2 ruling already used the guide's size before the change as the old cap | Guide § Size caps; spec § Decisions | "the old cap (else its size before the change)" |

Reviewer's self-check trim dropped "that break adjacent behavior"; not taken (not needed). Sizes: guide 22,795 (cap 22,800); template 18,478 (cap 18,489).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r11 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875

## Closing (2026-11-13)

Supervisor: end the change pass here, by ruling; move to a whole-guide audit. Dispositions appended to `skai/refinement-reviews/process-refinement-guide-findings.md` § Pass 2. Net size: guide 26,556 → 22,795; template 18,489 → 18,478.

# Pass 3 — Whole-Guide Audit

Review-only: no proposed change, so round 1 reviews both guides as they stand, scored. Charter: the whole of both guides against the design spec. Settled list: the design decisions only.

## Audit Round 1

Prompt: `reviews-g/a-r1-prompt.md`. Verdict: usable by a careful fresh agent; 2 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The repair step doesn't send the refiner back to the next round | accept | Guide § Verify | "After the clusters, before each next round until the stop rule" |
| F2 Scoring excludes "settled" rows, which can exclude a closed defect that reproduces | accept; spec had the same tension and is corrected | Guide § Round score; spec § Round score | Score live rows with no earlier disposition still holding |

Reviewer's trim ("This prevents premature and redundant rules") dropped two distinctions; not taken. Fit by rewording. Sizes: guide 22,794; template 18,478.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a1 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875

## Audit Round 2

Prompt: `reviews-g/a-r2-prompt.md`. Verdict: usable; 2 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The label-correction example treats a command-run `verified` as failing; "one step apart is fine" reads as overriding plain failures | accept; kept the one-step tolerance (pass 1's method note: it ended rounds of rounding rules), now scoped by "Otherwise" | Guide § Round score | "no command run or implementation read"; "Otherwise, one step apart either way is fine" |
| F2 The whole-read instruction sat in the optional report-charter section | accept | Template § Review target, § Report charter | "Read every binding surface in full"; moved, not duplicated |

Sizes: guide 22,798; template 18,392.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a2 | 11.875 | 2 | 1 | 1 | 0 | 0 |

> F1 irreversible · normal · speculative = 10 · F2 divergent · off-normal · speculative = 1.875

## Audit Round 3

Prompt: `reviews-g/a-r3-prompt.md`. Verdict: the ordinary workflow is reliable; 2 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 A new guide can't be the first round's target: nothing says how to represent it | accept | Guide § When to use; template § How to fill it, § Review target | A new guide is proposed in full; its proposed text is round 1's target |
| F2 "A third codified" reads as an automatic rule, bypassing the existing-rule check and the supervisor's say on process weight; the spec says the same | supervisor decision (design contradiction). Reviewer proposes "a third can be codified" | Guide § Triage; spec § Across passes | pending |

Reviewer's trims cut an explanation and a "not a working document" clause; not taken. Sizes: guide 22,796; template 18,487.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a3 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875

F2 resolved (2026-11-13): "a third can be codified" in the guide and spec; follows from the existing rules (sharpen first, process weight to the supervisor), applied as the refiner's call with the supervisor's go. Guide 22,799.

## Audit Round 4

Prompt: `reviews-g/a-r4-prompt.md`.
Verdict: usable with care; 2 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The guides say what the reviewer may read, not that it must read every reference | accept | Guide § Commissioning; template prompt opening | "it reads every named file and everything they reference, except excluded files" |
| F2 The prompt's codification test said only "codify on recurrence" | accept | Template § Editing discipline | "Log the first sighting; consider a second in another case; a third can be codified" |

Reviewer's three trims kept the meaning; taken. Sizes: guide 22,770; template 18,461.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a4 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875

## Audit Round 5

Prompt: `reviews-g/a-r5-prompt.md`.
Verdict: core sequence usable; 2 findings; the reviewer also could not exhaust references of references.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Context files: "read every named file" vs "read as needed" | accept | Template § How to fill it, § Context surfaces | Context files are read in full; still non-normative |
| F2 "One step apart either way is fine" reads as license to adjust a defensible label | accept; removing it is an ordinary fix: it duplicated "a label stands unless it plainly fails its test" and conflicted with it. Consolidation trigger fired again (audit r2 → r5 on this sentence); resolved by removal | Guide § Round score | Sentence removed |
| Coverage note: "everything they reference" read as transitive | refiner's call, from the supervisor's reason for the rule (a guide's references are part of the guide) | Guide § Commissioning; template prompt opening; spec | "everything they reference directly" |

Sizes: guide 22,734; template 18,466.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a5 | 5.0 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · normal · speculative = 2.5

## Audit Round 6

Prompt: `reviews-g/a-r6-prompt.md`.
Verdict: usable for the main path; 1 finding.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The prompt let the reviewer drop out-of-charter findings that "don't seem important", which the refiner must triage | accept | Template § Report charter | "list them briefly in an appendix after the Verdict, with the same finding fields" |

Sizes: guide 22,734; template 18,414.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a6 | 1.875 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875

## Audit Round 7

Prompt: `reviews-g/a-r7-prompt.md`.
Verdict: usable for the principal workflow; 1 finding plus 1 in the appendix.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 A failed accepted fix could count as noise, since its `accept` disposition "still stands" | accept | Guide § Finding matrix, § Round score | Noise only for a non-fix disposition; an unresolved accepted fix is live, a failed closure included |
| A1 The guide fixed a session-folder location that conflicts with the working-doc guide for package work | accept (in the binding target, so scored) | Guide § Records | Location deferred to `working-doc-conventions.md` |

Sizes: guide 22,690; template 18,414.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a7 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · A1 divergent · off-normal · speculative = 1.875

## Audit Round 8 — Thoroughness Comparison

Same text, two reviewers. A: high, prompt as usual (`a-r8a-*`). B: xhigh, with "Report every defect you find, however many, not only the most important; completeness matters more than brevity." in the report-charter slot (`a-r8b-*`).

| Run | Findings | Notes |
|---|---|---|
| A | 1 | Observed-failure prompt asserts a cause ("executing as documented") |
| B | 5 + 1 open question | Endorsed proposal not carried into repair; own-repairs count doesn't trigger the tier where it's counted; "every other surface points to it" vs the standalone prompt; appendix instruction lost when the charter is omitted; "exit codes" excluded even when they contradict a guarantee; open: old cap binding round 1 when a cap is being revised |

No overlap: B found five defects A didn't, and A found one B didn't. Reviewers are under-reporting. The two changes in B (effort and instruction) are confounded.

Supervisor (2026-11-13): make both standard — the template's fixed wording asks for every defect, and reviews run at xhigh. All six round 8 findings accepted (A's observed-failure premise; B's F1–F5; B's open question on cap revision resolved as current sizes only in round 1). Recorded in the design spec § Decisions From The Audit Pass. Sizes: guide 22,797; template 18,476.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a8 (A + B merged) | 12.5 | 6 | 0 | 6 | 0 | 0 |

> A F1 divergent · off-normal · speculative = 1.875 · B F1 divergent · normal · speculative = 2.5 · B F2 divergent · normal · speculative = 2.5 · B F3 divergent · off-normal · speculative = 1.875 · B F4 divergent · off-normal · speculative = 1.875 · B F5 divergent · off-normal · speculative = 1.875 · open question: neither

## Audit Round 9 (xhigh)

Prompt: `reviews-g/a-r9-prompt.md`.

Verdict: usable with risk; 4 findings (xhigh, completeness line in the template).

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Commissioning doesn't say to use the highest reasoning effort | accept | Guide § Commissioning | "on the supervisor's model at its highest effort" |
| F2 A cap-revision round 1 is still told to "meet each cap" | accept | Template § Size caps | Round 1 of a cap revision measures but doesn't enforce the old cap |
| F3 The recurrence bar also gated sharpening an existing rule | accept | Guide § Codification check | Scoped to minting new rules |
| F4 Commissioning's report scope omitted review-only passes | accept | Guide § Commissioning | "the change, or the whole target if none" |

Trims taken where they kept meaning; the template trim dropping the "this is intentional" example not taken. Sizes: guide 22,795; template 18,476.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a9 | 8.75 | 4 | 0 | 4 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875 · F4 divergent · normal · speculative = 2.5

## Audit Round 10 (xhigh)

Prompt: `reviews-g/a-r10-prompt.md`.

Verdict: usable for the ordinary loop; 6 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F01 "the supervisor's model" can read as the supervisor's own model | accept | Guide § Commissioning | "the supervisor's chosen model" |
| F02 Entry requires a latest report that a first pass doesn't have | accept | Guide intro | "if any" |
| F03 The stranded-case rule sat inside the new-rule check | accept | Guide § Triage | Moved to its own paragraph after the check; `log only` = "warrants no guide change" |
| F04 The reviewer can't count sightings without the log | accept | Template § Codification check | Flag unestablished recurrence for the refiner |
| F05 A finding matching no invariant was sent through the new-rule bar | accept | Guide § Structured tier | "If none fits, add one grounded in the design spec" |
| F06 "Tiers change record-keeping only" vs higher tiers' added checks; full-tier stop conditions vs the stop rule | refiner's call, consistent with the supervisor's intent for goal 9 (diligence never drops); spec goal 9 reworded to "the core checks never drop", higher tiers add safeguards | Guide § Scaling the ceremony; spec goal 9 and § Record-keeping levels | Core checks at every tier, higher tiers add safeguards; stop conditions consistent with the stop rule |

Template trim kept the example; taken. Sizes: guide 22,793; template 18,409.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a10 | 12.5 | 6 | 0 | 6 | 0 | 0 |

> F01 divergent · normal · speculative = 2.5 · F02 divergent · normal · speculative = 2.5 · F03–F06 divergent · off-normal · speculative = 1.875 each

## Audit Round 11 (xhigh)

Prompt: `reviews-g/a-r11-prompt.md`.

Verdict: usable with care; 3 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 No handoff when the reviewer rejects or amends the proposal | accept | Guide § When to use | "you triage its verdict with the findings and apply the shape you settle" |
| F2 The stranded-case rule lost the rare-path condition the spec and prompt have | accept | Guide § Triage | "A gap on a rare path …" |
| F3 A cap-revision commission didn't say it was one | accept | Template slot note; guide § Size caps | "say so and give current size only"; fill the slot "as directed there" |

Reviewer's trim deleted "This prevents premature rules…" (an explanation); not taken. Fit by rewording the *Size caps* paragraph. Sizes: guide 22,790; template 18,411.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a11 | 5.625 | 3 | 0 | 3 | 0 | 0 |

> F1–F3 divergent · off-normal · speculative = 1.875 each

## Audit Round 12 (xhigh)

Prompt: `reviews-g/a-r12-prompt.md`.

Verdict: usable for the ordinary path; 2 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 A newly approved cap can be smaller than the settled shape, with no instruction to tighten again before applying | accept | Guide § Size caps | "tighten the settled shape to fit, or escalate, before applying" |
| F2 The series exception can read as moving the round already scored | accept | Guide § Round score | Repairs stay in the running round's series; a changed series input starts a new series for later rounds |

Trims taken (meaning kept). Sizes: guide 22,797; template 18,411.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a12 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F1, F2 divergent · off-normal · speculative = 1.875 each

## Audit Round 13 (xhigh)

Prompt: `reviews-g/a-r13-prompt.md`.

Verdict: usable for the ordinary path; 3 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 A logged observation could be skipped before its recurrence was considered | accept | Guide § Finding matrix, § Closing | Noise only "after considering recurrence"; rationale lets later passes "assess re-raises and recurrence" |
| F2 "A disposition returning round after round" could treat a failed fix as a prompt defect | accept | Guide § Commissioning | "a settled decision returning … calls for checking" the settled slot |
| F3 Measuring applied even a rejected proposal | accept | Template § Size caps | "your recommended shape, including any endorsed or amended proposal" |

Sizes: guide 22,782; template 18,436.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a13 | 6.25 | 3 | 0 | 3 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2, F3 divergent · off-normal · speculative = 1.875 each

## Audit Round 14 (xhigh)

Prompt: `reviews-g/a-r14-prompt.md`.

Ran about 11 hours (others took well under one), measuring several restructures. Verdict: usable for the ordinary path; 3 findings.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F01 The findings-log step skips a restated rejection before recurrence is considered | accept; spec line reconciled | Guide § Records; spec § Records | "skip a non-fix only if it still stands after considering recurrence" |
| F02 The repeat-finding and own-repairs triggers come after the repair step they govern | accept | Guide § Finding matrix → § Repairing | Both bullets moved, unchanged, under "Before repairing:" |
| F03 The prompt orders the reviewer to meet every cap, with no route for a fix that can't fit | accept | Template § Size caps | Report the measured over-cap shape for supervisor decision |

Sizes: guide 22,764; template 18,488 (both match the reviewer's measurement).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a14 | 5.625 | 3 | 0 | 3 | 0 | 0 |

> F01–F03 divergent · off-normal · speculative = 1.875 each

## Audit Round 15 (xhigh)

Prompt: `reviews-g/a-r15-prompt.md`.

Verdict: usable with a careful refiner; 3 findings, two on the normal path.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 Label correction came after the matrix was already collapsed | accept | Guide § Finding matrix, § Round score | Label correction moved to the start of *Collapse before you count*; the *Round score* paragraph removed (moved, not cut) |
| F2 "No facts asserted about the target" forbids what the slots must contain | accept | Guide § Commissioning | "no rephrasing, preamble or target claims outside the slots" |
| F3 The reviewer's `supervisor-decision` label didn't cover cap-related decisions | accept | Template § Output | Label covers dropping valid content and a fix that can't fit |

Trims taken (meaning kept). Sizes: guide 22,675; template 18,489 (at cap).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a15 | 6.875 | 3 | 0 | 3 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · normal · speculative = 2.5 · F3 divergent · off-normal · speculative = 1.875

## Audit Round 16 (xhigh)

Prompt: `reviews-g/a-r16-prompt.md`.

Verdict: "A fresh LLM can follow the main refinement path today"; 2 findings, both off-path.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 A copied fix both stays in series and, as a change to the files under review, starts a new one | accept | Guide § Round score | Copied fix that adds a sibling guide stays in series; other series inputs start a new series |
| F2 The supervisor-decision category and handoff didn't carry the can't-fit-a-cap case | accept | Guide § Triage, § Supervisor decisions | Category includes it; handoff presents measured size, cap and options |

Sizes: guide 22,737; template 18,489.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a16 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F1, F2 divergent · off-normal · speculative = 1.875 each

## Caps Raised And Squeezed Wording Restored (2026-11-14)

Supervisor: the compression done to fit the caps made the guides denser and harder to read; the refiner should have proposed raising the caps instead of squeezing. Caps approved: guide 24,000 (was 22,800); template 19,500 (was 18,489); recorded in the design spec. Restored the readable wording of every sentence compressed only to fit a cap during this pass (about 20 in the guide, 16 in the template), leaving the fixes themselves as they were. Sizes: guide 23,263 (cap 24,000); template 19,211 (cap 19,500).

## Audit Round 17 (xhigh)

Prompt: `reviews-g/a-r17-prompt.md`. First review of the restored wording under the raised caps.

Verdict: "usable by a fresh LLM from scratch" once F01 is fixed; 1 finding.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F01 The supervisor-decision handoff's "or" lets a cap or content-drop escalation omit the heavier alternative the spec requires | accept; round 16's fix to this sentence became this finding (consolidation trigger), so the sentence was rewritten whole against spec § Supervisor Decisions | Guide § Supervisor decisions | Both fixes always shown; content-drop and can't-fit cases "also show" their extra evidence |

Sizes: guide 23,278 (cap 24,000); template 19,211 (cap 19,500); matches the reviewer's measurement.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a17 | 1.875 | 1 | 0 | 1 | 0 | 0 |

> F01 divergent · off-normal · speculative = 1.875

## Audit Round 18 (xhigh)

Prompt: `reviews-g/a-r18-prompt.md`. Verdict: usable on the main path, not yet reliable as a whole; 3 findings, none on round 17's repair.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The recurrence bar and the stranded rule could defer a requirement of the design spec the text misses | accept; reviewer's "any new rule" change not taken (every rule a reviewer recommends is its own, and the proposed change is already exempt); examples kept where its wording dropped them | Guide § Codification check, § Stranded; template § Editing discipline; spec § Triage | Deterministic defect includes "a design-spec requirement the text misses"; stranded applies only to a gap that "violates no design-spec requirement" |
| F2 A copied fix could make the whole sibling scoreable | accept | Guide § Repairing, § Round score; template `{{GUIDES}}` note, § Review target; spec § Repairing | Later prompts name the joined passage; reviewer reads the whole sibling; only the passage is binding |
| F3 The report had no place for the proposal assessment | accept, different home: *Verdict*, since the guide triages "its verdict on the proposal" | Template § Output; spec § Output | "If edits were proposed, your assessment of them, endorsements included." |
| Open question: the handoff's heavier alternative may be artificial for a fix that only can't fit a cap | not a finding; for a cap case the heavier alternative is raising the cap | — | — |

Sizes: guide 23,510 (cap 24,000); template 19,452 (cap 19,500); own new line tightened to fit.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a18 | 6.875 | 3 | 0 | 3 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · normal · speculative = 2.5

## Audit Round 19 (xhigh)

Prompt: `reviews-g/a-r19-prompt.md`. Verdict: usable for the main path; 2 findings, one on round 18's repair.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 The prompt didn't tell the reviewer that only a named sibling passage is binding | accept; round 18's repair became this finding: consolidation trigger, second firing this pass, so the pass moves to the structured tier; the target line rewritten whole against spec § Repairing | Template § Review target | "Read each existing guide named below in full …; where only a passage of a guide is named, that passage alone is binding" |
| F2 A proposal's own references and tool claims weren't read or checked | accept, different fix: the reading rule's owner (the prompt opening) covers the proposal, not a new refiner duty to list its files | Template opening, intro, § Verify claims about tooling; guide § Commissioning; spec § Commissioning, § The task, § Tool claims | "everything they or the proposed edits reference directly"; "the guide or a proposed edit asserts" |

Reviewer's two trims drop the goal-4 explanation and the "highest-yield check" reason; not taken. Template over its cap: supervisor decision pending.

Structured tier, impact map: the reading rule's owner (template prompt opening) edited first; dependents found by searching for "reference directly" and "they reference": template intro, guide § Commissioning, spec § Commissioning and § The task, all updated. The binding-boundary owner (template § Review target) edited; dependents (guide § Repairing, § Round score, template `GUIDES` note, spec § Repairing) already consistent.

Sizes: guide 23,532 (cap 24,000); template 19,575 (cap 19,500, over by 75).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a19 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · normal · speculative = 2.5

## Audit Round 20 (xhigh)

Prompt: `reviews-g/a-r20-prompt.md` (template cap 19,600, approved 2026-11-15). Verdict: largely usable; 2 findings, one an extension of round 19's repair.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F1 A named sibling passage didn't say whether the sibling's references bind, and the refiner's scoring rule didn't count referenced content | accept, amended to fit the cap: the narrowing goes in the target line, not the prompt opening; third finding on the copied-fix boundary, already at the structured tier | Template § Review target; guide § Round score *What counts*, § Repairing; spec § Repairing | "only that passage and what it references bind"; "a sibling passage a copied fix joined, with what they reference" |
| F2 Setting a first cap drops the size section in round 1 | reject (noise): the spec gives the reviewer size instructions only when a cap is set (§ Commissioning, § Decisions); a first cap is set after round 1 triage, and the refiner measures the settled shape | — | — |

Reviewer's two trims (goal-4 explanation, "highest-yield check" reason) declined again; the amended fix fits without them.

Structured tier, impact map: binding-boundary owner (template § Review target) edited first; dependents found by searching "is binding", "binding review target", "counts as part": guide § Repairing and § Round score, spec § Repairing updated; template prompt opening ("counts as part of its citing guide") consistent, since the target line narrows it for a passage; spec § Commissioning already says referenced content counts as part of the citing guide.

Sizes: guide 23,582 (cap 24,000); template 19,591 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a20 | 2.5 | 1 | 0 | 1 | 0 | 1 |

> F1 divergent · normal · speculative = 2.5 · F2 noise

## Audit Round 21 (xhigh)

Prompt: `reviews-g/a-r21-prompt.md`. Verdict: usable for the ordinary path; 2 findings, neither about round 20's repair.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F01 Stalled rounds were read as proof of a prompt defect; spec ties the prompt diagnosis to findings that misfire | accept, amended: the heading already names the condition, so the conditional is dropped | Guide § When the findings are wrong, suspect the prompt | "the other failure is an *under-specified* one, and its symptom names the slot:" |
| F02 Stranded-gap rule didn't require the workflow to already say stop and escalate | accept, amended: keeps "whatever its severity" | Guide § Stranded is not broken | "merely strands the operator, where the workflow already says to stop and escalate when the guide doesn't answer, is `log only`" |

Impact map: searched "stop converging" and "escalation route"; template § Stranded already conditional on the route; spec § Triage already matches.

Sizes: guide 23,544 (cap 24,000); template 19,591 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a21 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F01 divergent · off-normal · speculative = 1.875 · F02 divergent · off-normal · speculative = 1.875

## Audit Round 22 (xhigh)

Prompt: `reviews-g/a-r22-prompt.md`. Verdict: usable for the main loop; 2 findings, neither about round 21's repairs; round 21's two fixes not re-raised.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| 1 After a repeat finding, any outstanding findings across steps forced a restructure; spec restructures only when the findings span steps | accept, amended: keeps the spec's "only when" | Guide § Finding matrix, consolidation trigger | "restructure only when the repeated findings span more than one step, grouping them by root cause" |
| 2 A fix that applied to a sibling had to be copied there; spec only says what happens when one is copied | accept, amended to avoid a doubled "joins" | Guide § Repairing | "A fix copied into a sibling guide joins the same round: the sibling's changed passage becomes part of the binding target," |

Open question (not counted): findings that ignore a clear scope boundary, with no slot defect to repair. Logged.

Impact map: searched "outstanding findings", "also applies to a sibling"; spec § Repairing and § Decisions already conditional; template `GUIDES` note already conditional.

Sizes: guide 23,525 (cap 24,000); template 19,591 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a22 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> 1 divergent · off-normal · speculative = 1.875 · 2 divergent · off-normal · speculative = 1.875

## Audit Round 23 (xhigh)

Prompt: `reviews-g/a-r23-prompt.md`. Verdict: usable; 4 findings. 1 of 4 on my own earlier repair (the copied-fix sentence, again).

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| 1 The prompt carries neither the supervisor's problem nor, after round 2, the original change; spec goal 4 has the reviewer take the problem statement, but the spec's prompt section list has no place for it | supervisor decision: contradiction in the design. Ruled 2026-11-15: smallest fix; fitted the 19,600 cap by tightening the template intro, so no cap raise | Template `RECENTLY_REVISED` note and heading, intro; spec § Refinement Guide Requirements, prompt sections | "the supervisor's problem and wanted change, facts only, then what changed since the last round"; heading "The change, then recent changes (look hardest at these)"; intro "Each round the refiner fills it anew for a **fresh, no-context session**" |
| 2 Copying a fix into a sibling already under full review could narrow it to a passage | accept, amended to two words | Guide § Repairing | "A fix copied into a sibling guide outside the target joins the same round" |
| 3 An uncapped pass had no instruction to measure size (spec step 5) | accept, different fix: the tier line that lists every round's checks | Guide § Tiers | "checks mechanically, measures size and reviews" |
| 4 The refiner lacked the editing preference order the reviewer is told binds both | accept, amended: keeps why examples beat rules | Guide § Triage | "**Prefer, in this order:** remove wrong or duplicated text, or move a misplaced rule … · last, a new rule, gate or required field." |

Reviewer's template trims (prompt-fidelity paragraph) cut the "scaffolding" and "opposite of what the review is for" reasons; not taken.

Open question (not counted): the "span more than one step" threshold. Logged.

Impact map: copied-fix owner (guide § Repairing) edited; template `GUIDES` note and spec § Repairing already speak of a sibling joining. Preference order: spec § In The Prompt and template already carry it; spec § Repairing "Prefer examples over rules" consistent; no other surface named the old paragraph.

Sizes: guide 23,706 (cap 24,000); template 19,591 (cap 19,600). Finding 1's smallest fix measured on a temporary copy: template 19,671.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a23 | 7.625 | 4 | 0 | 3 | 1 | 0 |

> 1 divergent · normal · speculative = 2.5 · 2 divergent · off-normal · speculative = 1.875 · 3 cosmetic · off-normal · speculative = 0.75 · 4 divergent · normal · speculative = 2.5

After the finding 1 ruling: guide 23,706 (cap 24,000); template 19,596 (cap 19,600).

## Audit Round 24 (xhigh)

Prompt: `reviews-g/a-r24-prompt.md`. Verdict: usable for ordinary refinement; 2 findings, neither on round 23's repairs; round 23's fixes not re-raised.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| 1 "Run everything the guide tells an operator to run" could run a destructive command (reviewer: spec looks wrong) | first rejected (Safe Operations covers it); supervisor ruled 2026-11-15 that it is a real defect with a different fix: tools are not tested, their maintainers do that; the check is that the guide's claims match the tool's current code or documentation | Guide § Checking before the next round, § Closing the pass; spec § Checking Before The Next Round, § Closing A Pass | "Check every command and tool claim against the tool's current code or documentation … Don't test the tool itself; its maintainers do."; a tool finding "closes only when the guide's claim matches the tool's current code or documentation, failure handling included" |
| 2 The answer-baking ban could suppress a general fix that also covers the observed failure | reject (noise): the sentence contrasts a listed case with the general mechanism, the spec's line; the rewrite drops the paraphrase guard. Supervisor agreed 2026-11-15 | — | — |

Impact map: searched "run everything", "observed run", "re-read the implementation" across Guides, Templates, Policies and the refinement records; only the guide and spec carried the rule. The separate "Re-read the implementation" bullet folded into the new check. Template's reviewer side already reads code and never runs mutating tools; unchanged.

Sizes: guide 23,791 (cap 24,000); template 19,596 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a24 | 2.5 | 1 | 0 | 1 | 0 | 1 |

> 1 divergent · normal · speculative = 2.5 · 2 noise

Pass reopened; the earlier closure is withdrawn.

## Audit Round 25 (xhigh)

Prompt: `reviews-g/a-r25-prompt.md`. Verdict: usable; 1 finding, on round 24's repair. The tool-check ruling was confirmed to match the spec.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| 1 The pre-round check step no longer said to run every applicable mechanical check (spec step 5); a24's repair removed the "run everything" bullet that carried it | accept; a fix became the finding, so the step's opening sentence is rewritten whole; already at the structured tier | Guide § Checking before the next round | "After the clusters, run every applicable mechanical check before each next round until the stop rule:" |

Impact map: spec step 5 and § Checking Before The Next Round already require it; the tier line ("checks mechanically") is consistent.

Sizes: guide 23,829 (cap 24,000); template 19,596 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a25 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> 1 divergent · normal · speculative = 2.5

## Audit Round 26 (xhigh)

Prompt: `reviews-g/a-r26-prompt.md`. Verdict: usable with one scoring ambiguity; round 25's repair and the tool-check ruling confirmed sound.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F01 "other labels stand" could be read as protecting any label outside the two examples, though the spec corrects any label that plainly fails its test | accept | Guide § Finding matrix, *Collapse before you count* | "noting each in the arithmetic line; otherwise the reviewer's labels stand." |

Impact map: spec § Round score already says "otherwise the reviewer's labels stand"; template § Output unchanged.

Sizes: guide 23,848 (cap 24,000); template 19,596 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a26 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F01 divergent · normal · speculative = 2.5

## Audit Round 27 (xhigh)

Prompt: `reviews-g/a-r27-prompt.md`. Verdict: usable; 2 findings, neither on round 26's repair.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F01 The prompt's `supervisor-decision` listed any new rule as process weight; the guide's category and codification check let the refiner accept one | accept, different fix: the spec (goal 5, § Triage categories and new-rules bar) leaves new rules to the codification check and lists process weight without them, so the prompt is the side that's wrong; the reviewer's fix would have made the guide contradict the spec | Template § Output, Triage field | "(the fix adds process weight -- a new gate, checklist, or proof burden --" |
| F02 The structured-tier trigger said "previous repairs" / "own repairs"; spec § Scoring says the refiner's own last repairs | accept | Guide § Finding matrix, § Tiers; spec § Tiers, § Decisions | "your own last repairs" |

Impact map: searched "gate, rule", "own repairs", "previous repairs"; spec § Tiers and § Decisions said "own repairs" and were aligned; template has no other supervisor threshold for rules.

Sizes: guide 23,849 (cap 24,000); template 19,590 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a27 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F01 divergent · off-normal · speculative = 1.875 · F02 divergent · normal · speculative = 2.5

## Audit Round 28 (xhigh)

Prompt: `reviews-g/a-r28-prompt.md`. Verdict: usable; 1 finding, on round 23's measuring repair; round 27's fixes not re-raised.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| F01 Measuring size sat in the tier summary and the caps paragraph, not at the pre-round check where spec step 5 puts it | accept, amended: keeps "whatever the reviewer measured"; a fix became the finding, so the check's opening sentence is rewritten whole; already at the structured tier | Guide § Checking before the next round, § Size caps | "After the clusters, measure each guide with `wc -c`, capped or not and whatever the reviewer measured, and run every applicable mechanical check before the next round, until the stop rule:"; caps paragraph: "Record the net size change at closure." |

Open question (not counted): the spec's opening says it isn't read at runtime, yet the refiner reads it. Logged.

Impact map: searched "wc -c" and "measure" in the guide; the tier line ("measures size") stays as the summary; spec step 5 and § Size Caps consistent.

Sizes: guide 23,860 (cap 24,000); template 19,590 (cap 19,600).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a28 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F01 divergent · normal · speculative = 2.5

## Audit Round 29 (xhigh)

Prompt: `reviews-g/a-r29-prompt.md`. Verdict: usable for the ordinary path; 1 finding; round 28's repair confirmed consistent.

| Defect | Triage | Touches | Fix |
|---|---|---|---|
| 1 A proposal rejected in round 1 with nothing applied had no explicit route to the required fresh round | reject (noise): not reachable in practice: round 1's verdict on a proposal is triaged like any finding, so the refiner overrules it or proposes a different change, and either is applied and reviewed; only the supervisor dropping the change applies nothing, and that ends the pass with nothing left to review | — | — |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| a29 | 0 | 0 | 0 | 0 | 0 | 1 |

Stop rule (a) met: a fresh round over the current text whose triaged findings leave nothing to apply.

# Pass 3 Closure

| Item | Status |
|---|---|
| Rounds | a1–a29; a17 onward a new series after the cap raise |
| Findings | every row in the findings log's Pass 3 table is closed, rejected or logged with its evidence; none still open or deferred |
| Supervisor rulings | caps 24,000 / 19,500 (2026-11-14); template cap 19,600 (2026-11-15); round 23 finding 1, smallest fix (2026-11-15); a24: tools are not tested, claims are checked against code or docs; answer-baking ban stands (2026-11-15) |
| Tool findings | a24 only; closed against the guide text, no tool involved |
| Net size | guide 22,795 → 23,860 (+1,065, cap 24,000); template 18,478 → 19,590 (+1,112, cap 19,600) |
| Committed | nothing |

Handed to the supervisor for review.
