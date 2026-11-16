# Findings log — `process-refinement-guide.md` + `cold-review-prompt-template.md`

Cross-pass record of every cold-review finding against these two guides and what was decided.
Consulted at triage; never shown to a cold reviewer. Extract settled decisions into the prompt's
`{{SETTLED_DISPOSITIONS}}` slot instead.

**Path note (logged, not fixed).** The guide specifies `skai/refinement-reviews/<target>-findings.md`,
which assumes a host project. The skai repo has no `skai/` folder, so refining skai's own guides has
no defined home for this log. Placed at the repo root by analogy. Same family as the standing
observation that this process cannot commission a conforming cold review of itself — the template
forbids the reviewer from reading `process-refinement-guide.md`, which is unavoidable when that guide is the
target.

## Pass 1 — 2026-08-28/29 · round scoring

Sixteen cold-review rounds (`gpt-5.6-sol`/xhigh, read-only) over the *Round score* mechanism and the
two per-finding fields it consumes. **Closed by ruling (Tim, 2026-08-29), not by a clean round** —
the last two repairs are unverified by a fresh review.

Scores ran as two series; the boundary is the 2026-08-29 sharpening of the label tests, which the
guide's own series rule makes a new series.

| Series | Rounds | Scores |
|---|---|---|
| 1 | r1–r13 | 23.4 · 22.9 · 23.5 · 20.0 · 22.5 · 7.5 · 25.0 · 22.5 · 18.2 · 10.0 · 17.5 · 10.0 · 27.5 |
| 2 | r1–r2 | 27.5 · 4.4 |

Series 1 is recorded under the pre-collapse counting rule and is not comparable to series 2.

### Dispositions

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-28 | Re-raises collapsed into noise, hiding failed closures | closed | Noise rule rewritten; a closure that did not hold returns to triage and scores |
| 2026-08-28 | `verified`/`speculative` defined three different ways across the two files | closed | One definition, byte-identical in both template locations |
| 2026-08-28 | Consequence/reachability categories overlap | closed | First-match-wins test order added to both |
| 2026-08-28 | Guide still promised a per-finding `severity` the template no longer collects | closed | "a severity and" deleted from the cold-review description |
| 2026-08-28 | `Total findings` undefined; arithmetic labels unassigned | closed | Defined as the sum of the three consequence columns; findings numbered by report order |
| 2026-08-28 | Section too long (558 words, 14.5%) | closed | Cut to 353 by deleting rationale; verdicts from r7 onward call the share earned |
| 2026-08-28 | "ordered by severity" / "Top findings first" still require computing a grade | closed | Both removed from the Output instruction |
| 2026-08-28 | "one irreversible outweighs ten cosmetic" is false — 20 = 10×2 | closed | Sentence deleted |
| 2026-08-28 | Score had no defined starting round when an effort escalated tier | closed | Tier condition removed entirely (Tim's ruling); every round is scored |
| 2026-08-28 | A deterministic wrong action every operator hits scored `cosmetic` | closed | `divergent` extended to cover every operator sent to the same wrong outcome |
| 2026-08-28 | Worked example implied an unstated rounding rule | closed | Example totals exactly; no rounding implied |
| 2026-08-28 | Charter placement vs target scope not distinguished | closed | Report placement does not decide eligibility; appendix findings score if in target scope |
| 2026-08-28 | Findings log lived under git-ignored `working-docs/` | closed | Moved to a committed per-target path; renamed from "coverage map" |
| 2026-08-28 | Log dispositions appended only at pass close, but noise reads them per round | closed | Append required before commissioning the next review |
| 2026-08-28 | `reject` said "speculative", colliding with the evidence label | closed | `reject` now means fails to establish a live defect; document-only reasoning explicitly not grounds |
| 2026-08-28 | "this document" wrong when a review targets several guides | closed | Scoping boundary is the binding review target |
| 2026-08-29 | "already settled" ambiguous after a mid-round human ruling | closed | Means settled before the round was commissioned |
| 2026-08-29 | Ownership of a plainly wrong reviewer label unstated | closed | Labels stand unless one fails its own test; corrections go in the arithmetic line, before collapsing |
| 2026-08-29 | Series rule read as "every repair starts a new series" | closed | Series fixed by the scoring model, files, spec/scope, charter, and supplied evidence; repair is the measured event, unless the repaired text *is* one of those inputs |
| 2026-08-29 | Score counted reported findings, so it tracked how finely a reviewer chopped its report | closed | Matrix is one row per defect (Tim's design) |
| 2026-08-29 | Collapse took the strongest value on each axis, inventing rows worth more than any constituent | closed | Row copies the whole label set of its heaviest constituent; never mix axes |
| 2026-08-29 | Unit vocabulary half-swept — noise still counted findings, not rows | closed | Swept; noise counts rows |
| 2026-08-29 | Turning "What counts" into a branch-by-branch partition of triage labels | rejected | The governing rule answers the cases on its own; enumeration was deliberately deleted and should not return |
| 2026-08-29 | Worked example for labelling a series boundary after a factor change | rejected | Fires only on a factor-table change; the governing sentence is sufficient |
| 2026-08-29 | Rename `verified`/`speculative`, which read oddly for documentary findings | rejected | Known and accepted; renaming ripples through unrelated text |
| 2026-08-29 | Extract the scoring procedure into its own document | rejected | Tim's ruling: extraction is for off-happy-path material, and scoring is required every round |
| 2026-08-29 | Repair loop does not route to `maintain-skai.md`'s after-every-edit sanity scan | logged | Out of charter across five rounds; not addressed in this pass |
| 2026-08-29 | Guide has human-decision STOPs but no `## Gates` / advance-intent mechanics | logged | Out of charter; adds runtime process weight — a human decision, not a refiner's call |
| 2026-08-29 | `EXCLUDED_SURFACES` described as blindness protection but only offered to scoped reviews | logged | Out of charter; raised once, first sighting |

### Rulings by the project owner

| Date | Ruling |
|---|---|
| 2026-08-29 | The metric is a **round score**; "burden" was inherited agent jargon and is retired |
| 2026-08-29 | Scoring is required for every round — the "structured tier and above" condition was never his and is removed |
| 2026-08-29 | Keep the formula. Replacing it with bare consequence counts was proposed twice and refused |
| 2026-08-29 | Score distinct defects, not reported findings — his design, after the same text scored 10.0 and 27.5 |
| 2026-08-29 | Rename the skill: it refines processes, not skills. `guide.skill-refinement` → `guide.process-refinement` |
| 2026-08-29 | The findings log is committed and belongs outside `working-docs/`; "coverage" was too abstract a name |
| 2026-08-29 | Close by ruling without a confirming round |

### Method notes for the next pass

- **Interview the reviewers when labels disagree.** Two reviewers scored identical text 10.0 and 27.5.
  Interviewing both traced the whole gap to two under-specified phrases — "invalidates the effort's own
  measurements" and "the path every run takes". After sharpening, both re-classified identically and
  called the boundaries forced. This is the single highest-yield move in the effort.
- **Prompt calibration moved the score more than any repair.** A failure-mode slot asking the reviewer
  to hunt "numeric machinery whose inputs are too vague" produced five rounds of rounding rules and edge
  cases. Removing it, and stating that the score is a best estimate where one step apart is tolerated,
  dropped the round from three findings to one.
- **Prefer a governing rule to a list of cases.** Three consecutive rounds were spent patching a list of
  counting cases, each patch colliding with a neighbour. One sentence naming the principle ended it.
- **Verify a repair landed before commissioning the next round.** One round was spent reviewing unchanged
  text because an edit failed silently and the review launched anyway.

## Pass 2 — 2026-11-13 · proposal-first refinement (skai#90, #130, #135, #136)

Eleven rounds (`gpt-6.1-terra`/high), the first on a proposal and unscored; from round 2 each prompt was built from the guides as just repaired, so every round is its own series. Standard: `process-refinement-guide-design.md`, backfilled this pass. Includes a cleanup with 13 supervisor-approved cuts. **Closed by ruling (supervisor, 2026-11-13), not by a clean round**: the rounds had reached into text older than the change, which goes to a whole-guide audit pass; round 11's two fixes are unverified by a fresh review. Sizes: guide 26,556 → 22,795 (cap 22,800); template 18,489 → 18,478 (cap 18,489).

Scores (r2–r11): 3.75 · 3.75 · 5.0 · 2.5 · 5.0 · 1.875 · 1.875 · 2.5 · 4.375 · 3.75.

### Dispositions

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-11-13 | r1: the proposal's scoring, cap timing, stop rule, settled-decision, measuring, whole-change and escalation gaps (7) | closed | Amended before applying; see the pass's working document |
| 2026-11-13 | Self-review could omit one of the two guides | closed | A review of either one has both as its target |
| 2026-11-13 | Cleanup bans competed with tightening to meet a cap | closed | Both bans except tightening to meet a cap |
| 2026-11-13 | "Trivial copy edits skip it" overrode the supervisor's choice | closed | Removed from guide and spec |
| 2026-11-13 | A closure reopened only "with the same surface" | closed | "and still reproduces" |
| 2026-11-13 | Two-round minimum vs a review-only first round | closed | Minimum applies to a pass that applies a change |
| 2026-11-13 | The prompt's codification check lacked the guide's exceptions; "reserve accept" over-restricted | closed | Exceptions restored; examples kept |
| 2026-11-13 | `reject` could discard a real defect (fired twice) | closed | Rewritten whole: "posits a misuse the text doesn't support" |
| 2026-11-13 | Pre-round check didn't name failure branches | closed | "failure branches included" |
| 2026-11-13 | Reviewer may not read the code behind tool claims | closed | Supervisor ruling: the reviewer reads the named files and everything they reference, never an excluded file |
| 2026-11-13 | Following references could reach the findings log or the refinement guides | closed | Exclusion slot required; always names the log and, unless targeted, both guides |
| 2026-11-13 | Cap formulas overlapped; measuring left out recommended fixes | closed | Formula by new vs existing guide; measuring includes all recommended fixes |
| 2026-11-13 | Codification threshold split between triage and *Across passes* | closed (unverified) | Threshold at triage; *Across passes* points to it |
| 2026-11-13 | No old cap for an existing, never-capped guide | closed (unverified) | Its size before the change, per the supervisor's cap ruling this pass |

### Method notes for the next pass

- **Draft by rewriting.** The first draft appended the change (+3,367 / +1,685 bytes); the rewrite came in under the starting sizes.
- **A rewritten guide makes the whole guide the change.** After a reorganization, "defects in the change" reaches old text, and scores stop falling; charter a whole-guide audit instead.

## Pass 3 — 2026-11-13/14 · whole-guide audit

Review-only, against `process-refinement-guide-design.md`; the charter is the whole of both guides. Rounds a1–a7 at `gpt-6.1-terra`/high. a8 was a same-text comparison (high vs xhigh with an every-defect line), after which the supervisor made both standard; a9 onward run at xhigh. Caps raised by the supervisor 2026-11-14 (guide 24,000, template 19,500), and wording compressed to fit the old caps was restored. Open: no clean round yet.

Scores (a1–a29): 4.375 · 11.875 · 3.75 · 4.375 · 5.0 · 1.875 · 4.375 · 12.5 · 8.75 · 12.5 · 5.625 · 3.75 · 6.25 · 5.625 · 6.875 · 3.75 · 1.875 · 6.875 · 4.375 · 2.5 · 3.75 · 3.75 · 7.625 · 2.5 · 2.5 · 2.5 · 4.375 · 2.5 · 0.

### Dispositions

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-11-13 | a1: repair step didn't send the refiner back to the next round | closed | "before each next round until the stop rule" |
| 2026-11-13 | a1: scoring excluded "settled" rows, hiding a reproducing closed defect | closed | Live rows with no earlier disposition still holding; spec corrected |
| 2026-11-13 | a2: label-correction example treated a command-run `verified` as failing | closed | "no command run or implementation read" |
| 2026-11-13 | a2: whole-read instruction sat in the optional report-charter section | closed | Moved to *Review target* |
| 2026-11-13 | a3: a new guide couldn't be round 1's target | closed | A new guide is proposed in full; its text is round 1's target |
| 2026-11-13 | a3: "a third codified" read as automatic | closed | "a third can be codified" in guide and spec |
| 2026-11-13 | a4: reading set said what the reviewer may read, not must | closed | "reads every named file and everything they reference" |
| 2026-11-13 | a4: prompt's codification test said only "codify on recurrence" | closed | Three-step sighting count in the prompt |
| 2026-11-13 | a5: context files "read every named file" vs "as needed" | closed | Context files read in full |
| 2026-11-13 | a5: "one step apart is fine" licensed adjusting a defensible label (trigger fired) | closed | Sentence removed; it duplicated "labels stand unless plainly failing" |
| 2026-11-13 | a5: "everything they reference" read as transitive | closed | "directly" |
| 2026-11-13 | a6: out-of-charter findings could be dropped | closed | Appendix after the Verdict, same fields |
| 2026-11-13 | a7: a failed accepted fix could count as noise | closed | Noise only for a non-fix disposition |
| 2026-11-13 | a7: guide fixed a working-doc location conflicting with the working-doc guide | closed | Location deferred to `working-doc-conventions.md` |
| 2026-11-13 | a8: observed-failure prompt asserted a cause; endorsed proposal not carried into repair; own-repairs count didn't trigger the tier; ownership vs standalone prompt; appendix lost without a charter; exit codes excluded even when wrong; cap-revision round 1 | closed | Supervisor accepted all six plus the open question; spec § Decisions From The Audit Pass |
| 2026-11-13 | a9: no highest-effort instruction; cap-revision round 1 told to meet caps; recurrence bar gated sharpening; report scope omitted review-only passes | closed | Each sharpened at its point of use |
| 2026-11-13 | a10: "supervisor's model"; entry required a report a first pass lacks; stranded rule inside the new-rule check; reviewer can't count sightings; no-invariant findings; tier wording vs goal 9 | closed | Spec goal 9 reworded ("core checks never drop") |
| 2026-11-13 | a11: no handoff for a rejected or amended proposal; stranded rule lost its rare-path condition; cap-revision commission didn't say so | closed | Each sharpened at its point of use |
| 2026-11-13 | a12: approved cap below the settled shape; series exception timing | closed | Tighten before applying, or escalate; later rounds start the new series |
| 2026-11-13 | a13: logged observation skipped before recurrence; disposition-returning diagnosis; measuring applied a rejected proposal | closed | "after considering recurrence"; "a settled decision returning"; "your recommended shape" |
| 2026-11-14 | a14: log step skipped restated rejection; triggers after the repair step; no route for a fix that can't fit | closed | Spec reconciled; triggers under "Before repairing"; over-cap shape to the supervisor |
| 2026-11-14 | a15: label correction after collapse; "no facts asserted" vs slot fills; `supervisor-decision` label missed cap cases | closed | Correction first in *Collapse*; "outside the slots"; label widened |
| 2026-11-14 | a16: copied fix both in and out of series; can't-fit case missing from the category and handoff | closed | Copied fix stays in series; can't-fit is a supervisor decision |
| 2026-11-14 | a17: handoff's "or" let a cap or content-drop escalation omit the heavier fix (repeat of a16's repair) | closed | Sentence rewritten whole: both fixes always, case evidence "also" |
| 2026-11-14 | a18: recurrence bar and stranded rule could defer a design-spec requirement the text misses | closed | Deterministic defect includes a missed spec requirement; stranded only when no spec requirement is violated |
| 2026-11-14 | a18: copied fix could make the whole sibling scoreable | closed | Prompt names the joined passage; only it is binding |
| 2026-11-14 | a18: report had no place for the proposal assessment | closed | Verdict carries it, endorsements included |
| 2026-11-14 | a18 open question: heavier alternative artificial for a cap-only escalation | logged | For a cap case the heavier alternative is raising the cap; spec requires both fixes for every supervisor decision |
| 2026-11-14 | a18: copied fix could make the whole sibling scoreable | closed | Superseded by the a19 rewrite of the prompt's target line |
| 2026-11-14 | a19: the prompt didn't tell the reviewer only a named sibling passage is binding (repeat of a18's repair) | closed; extended by a20 | Target line rewritten whole: guides read in full; a named passage alone is binding |
| 2026-11-14 | a19: a proposal's own references and tool claims weren't read or checked | closed | Reading rule and tool check include the proposed edits |
| 2026-11-15 | a20: a named sibling passage didn't say whether its references bind, and scoring didn't count referenced content (third repeat on the copied-fix boundary) | closed | Only the passage and what it references bind; scoring counts what the guides and passage reference |
| 2026-11-15 | a20: setting a first cap drops the reviewer's size instructions in round 1 | rejected | Spec gives the reviewer size instructions only when a cap is set; a first cap is set after round 1 triage and the refiner measures the settled shape |
| 2026-11-15 | a21: stalled rounds treated as proof of a prompt defect | closed | The prompt-slot diagnosis is tied to wrong findings, not to non-convergence |
| 2026-11-15 | a21: stranded-gap rule didn't require the workflow to have an escalation route | closed | Log-only applies only where the workflow already says to stop and escalate |
| 2026-11-15 | a22: a repeat finding forced a restructure for unrelated findings | closed | Restructure only when the repeated findings span more than one step |
| 2026-11-15 | a22: a fix that applied to a sibling had to be copied there | closed; extended by a23 | Copying is the refiner's call; the rule covers what happens once a fix is copied |
| 2026-11-15 | a22 open question: findings that ignore a clear scope boundary, with no slot defect to repair | logged | Not raised as a defect; such findings are triaged as noise |
| 2026-11-15 | a23: the prompt carries neither the supervisor's problem nor, after round 2, the original change | closed | Supervisor ruled the smallest fix (2026-11-15): the recently-changed section carries the problem and change wanted, then the latest changes; spec section list matches |
| 2026-11-15 | a23: copying a fix into a sibling already under full review could narrow it to a passage | closed | The passage rule applies to a sibling outside the target |
| 2026-11-15 | a23: an uncapped pass had no size measurement | closed | Every tier measures size |
| 2026-11-15 | a23: the refiner lacked the editing preference order the reviewer follows | closed | Guide gives the full order; the example rationale kept |
| 2026-11-15 | a23 open question: "repeated findings span more than one step" threshold | logged | Settled; example only if the log shows confusion |
| 2026-11-15 | a24: "run everything the guide tells an operator to run" could execute a destructive command | closed | Supervisor ruled 2026-11-15: tools are not tested; the refiner checks each command and tool claim against the tool's current code or documentation, and a tool finding closes when the claim matches |
| 2026-11-15 | a24: the answer-baking ban could suppress a general fix that also covers an observed failure | rejected | The sentence already contrasts a listed case with the general mechanism, the spec's line; the suggested rewrite drops the paraphrase guard; supervisor agreed 2026-11-15 |
| 2026-11-15 | a25: the pre-round check step didn't say to run every applicable mechanical check (spec step 5), after a24's repair narrowed it | closed | The step's opening sentence now requires it |
| 2026-11-15 | a26: "other labels stand" could protect a plainly wrong label outside the two examples | closed | Wording matches the spec: otherwise the reviewer's labels stand |
| 2026-11-15 | a27: the prompt counted any new rule as process weight; the guide and spec don't | closed | Different fix from the reviewer's: the prompt aligned to the spec, where a new rule passes the codification check and process weight is gates, fields, checklists and the like |
| 2026-11-15 | a27: the structured-tier trigger didn't say which repairs to count | closed | The refiner's own last repairs, in guide and spec |
| 2026-11-15 | a28: measuring size sat in the tier summary and the caps paragraph, not at the pre-round check (repeat of a23's repair) | closed | Moved to the pre-round check, capped or not; caps paragraph keeps the closure record |
| 2026-11-15 | a28 open question: spec opening says it isn't read at runtime, yet the refiner reads it | logged | The spec's runtime reader is the target's operator; the refiner reads it as the standard. Not a guide defect |
| 2026-11-15 | a29: a proposal rejected with nothing applied had no route to the fresh round | rejected | Not reachable in practice: round 1's verdict on a proposal is triaged like any finding, so the refiner overrules it or proposes a different change, and either is applied and reviewed; only the supervisor dropping the change applies nothing, and that ends the pass with nothing left to review |

Reopened 2026-11-15: the supervisor ruled a24's first finding a real defect (different fix).

Closed 2026-11-15 by stop rule (a): fresh round a29 over the current text left nothing to apply (1 finding, rejected; noise 1). Net size over the pass: guide 22,795 → 23,860 (+1,065); template 18,478 → 19,590 (+1,112); caps 24,000 / 19,600.
