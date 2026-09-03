# Findings log — `process-refinement-guide.md` + `cold-review-prompt-template.md`

Cross-pass record of every cold-review finding against these two guides and what was decided.
Consulted at triage; never shown to a cold reviewer. Extract settled decisions into the prompt's
`{{SETTLED_DISPOSITIONS}}` slot instead.

**Path note (closed 2026-09-03).** Collateral now resolves from the binding target's owning Git root,
not the caller's working directory. Findings live at `<target-repo-root>/refinement-reviews/`; working
documents live at `<target-repo-root>/skai/working-docs/` and use that repository's branch. This works
when SKAI is opened directly or nested as a submodule. The separate standing observation remains:
this process cannot commission a conforming cold review of itself because the template forbids the
reviewer from reading `process-refinement-guide.md`, which is unavoidable when that guide is the target.

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
