# Requirements system — coverage map

Cross-pass record of every finding and its disposition. Refiner-facing: never shown to a cold
reviewer. The settled decisions extracted from it go into the review prompt's settled-dispositions
slot instead.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-27 p1 | `(D#)` strip verified but never performed | closed | `C6` performs the strip; `## Purpose` scopes "never rewrites" to wording |
| 2026-08-27 p1 | No change-id resolution, no artifact creation step | closed | UI Map's change-id paragraph adopted into `## The change package` |
| 2026-08-27 p1 | `proposed-requirements/` full mirror or subset | closed | Human decision: touched files only; diff baseline reworded to match |
| 2026-08-27 p1 | Baseline path has no worked example | closed | Three-item file-granular example added to artifacts |
| 2026-08-27 p1 | Blocked gates promise a resumption the workflow forbids | closed | Stop line added where the failure is described, not as a new gate section |
| 2026-08-27 p1 | Change requests raised but never answered | closed | UI Map's three pieces ported: reopen answers it, readiness condition 3, artifact section |
| 2026-08-27 p1 | `(deprecated)` contradicts "no status fields" | closed | Exception carved into the same sentence; `deprecate` → `retire` throughout |
| 2026-08-27 p1 | Evidence example contradicts its format; brackets unidentifiable | closed | Check ID first token; example conformed; re-run appends below history |
| 2026-08-27 p1 | Content-check list has three drifted homes | closed | Promotion's `C1`–`C6` is the single enumeration; tradeoff recorded |
| 2026-08-27 p1 | Integration block unfillable for a greenfield project | closed | `local` covers intent; `none` framed as opt-out; blocked gate names its resolution |
| 2026-08-27 p1 | Stale requirements routing in work-spec skill + README | closed | Clauses deleted; the "promotes" sentence rewritten to the handoff |
| 2026-08-27 p1 | Grandfathering policy only in CHANGELOG; check scoping unstated | closed | Policy moved into the catalog guide; `C5` scoped to what the package writes |
| 2026-08-27 p1 | Redundant `auto` milestone; `auto` defeats the `shared` announcement | closed | Milestone deleted; announcement made explicit under `auto`. Hard-gate variant **declined** — process weight not justified for a case the clause already covers |
| 2026-08-27 p1 | Work-spec creation has no way back after its handoff | closed | One sentence in `work-spec-creation.md`; nothing in the requirements guides changed |
| 2026-08-27 p1 | Read-only claim names debugging and unit testing | logged | The sentence overstates reach but instructs nothing, so no agent acts wrongly on it. Wiring those workflows to the catalog is real work that a passing clause should not imply is done. Fold the trim in only if that paragraph is touched for another reason |

## Round-1 self-check catches (not from the review)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-27 p1 | `C4` rationale said "here, rather than during drafting" after authoring began running the same checks | closed | Reworded to draft-runs-it / promotion-enforces-it |
| 2026-08-27 p1 | `working-doc-conventions.md` cross-reference implied working-doc paths govern the change package | closed | Dropped from the catalog guide's cross-references |
| 2026-08-27 p1 | "Do not promote as a continuation" contradicted "reached directly after authoring completes" | closed | Promotion reworded: the signal often comes right after, but it is still a signal |

## Rounds 5 and 7 (series A r3, r5)

Reconstructed from the refinement working document at round 8. Rounds 4 and 6 dispositions were not
appended to this log at the time and their reviewer reports are not retained, so they cannot be
reconstructed; recorded here as a gap rather than invented.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-28 r3 | `C1` bracket resolved neither path from any cwd — grep failed to stderr, stdout stayed empty, and "a passing command prints nothing" read that as a pass | closed | Bracket rebuilt to resolve both paths from the host repo root; fixture in `verify-documented-commands.sh` pins both so the regression cannot recur silently |
| 2026-08-28 r3 | Promotion outcome slot did not state what the check found | closed | Outcome slot states the finding; the contradicting rule deleted |
| 2026-08-28 r3 | Type vocabulary named pairings with no execution path | closed (half) | Vocabulary narrowed to executable pairings; "removes" → "retires". The `move` half is in the unimplemented ledger |
| 2026-08-28 r3 | A promotion finding was seeded as a Discussion item rather than fixed in the drafts | closed | Reopen paragraph routes a promotion finding to the drafts unless the fix is itself a decision |
| 2026-08-28 r3 | Zero-padding inside a legacy file whose IDs are unpadded | logged | Genuine convention call, not a wording slip. Padding new IDs yields `MODE-07` beneath `MODE-6`; matching the file preserves in-file consistency but permits cross-file drift. Either answer is defensible, so it is the human's call, not a defect to repair silently. In the unimplemented ledger |
| 2026-08-29 r5 | A package touching `glossary.md` or a scope index destroys the rest of the file with every check green | **reopened at round 8 — see below** | The r5 repair reworded the "drafted whole" rule from *requirements* to *content*. That is an instruction to the drafter; nothing verified it |
| 2026-08-29 r5 | `C1` bracket compared one file pair for a check spanning every rewritten file | closed | `## Evidence` prose requires the comparison once per rewritten file; both branches run in the verify script |
| 2026-08-29 r5 | `C2` did not catch a prefix collision inside the package | closed | `C2` scoped to the catalog *and* this package |
| 2026-08-29 r5 | `C4` flagged the `(D#)` scaffolding that `C6` removes | closed | `C4` excludes the citations `C6` strips |
| 2026-08-29 r5 | Blocked list did not name the current failure kinds | closed | List rewritten to the failures the checks actually produce |
| 2026-08-29 r5 | Promotion has no listed blocked gate for a missing Integration block | logged | A strand, not a misroute — the generic blocked gate is available, and "stranded is not broken" holds until the strand actually occurs. In the unimplemented ledger |
| 2026-08-29 r5 | Re-promoting a package that raised a change request is undocumented | logged | Readiness condition 2 necessarily fails on the second run because the catalog now *is* what the package proposed. The route out is stated; the round trip is undocumented but does not strand. In the unimplemented ledger |

## Round 8 — pre-commission (architecture repair, no review round)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-29 r8 | **Reopened:** promotion pairs a destructive whole-file write (`C7`) with ID-only verification (`C1`–`C6`), so any non-ID content — glossary entries, index routing lines — is invisible to every check and destroyed by the write | closed | Re-reproduced in a fixture first: 3 glossary entries → 1, `C1`/`C3`/`C5` all green. Its r5 `closed` was recorded on intent and is corrected to `still open` in the working doc. Resolved as an architecture decision, not a prose patch: the design spec's *Promotion is a transformation* now requires verification to span everything the write can destroy, and `C1` was widened from `IDs are append-only` to `A rewrite loses nothing`. Human chose the sharpen over a new `C8`. Five dependent sites swept by grep; `## Purpose` and the blocked-gate list updated to match. Verify script extended with glossary, index, dropped-ID and reused-ID fixtures — 7/7, both branches each |
| 2026-08-29 r8 | Size budget of 9,500 words was derived from nothing and priced out the only correct fix | closed | Provenance recorded in the spec; raised to 10,500 on the human's approval. The per-repair cost discipline is unchanged |

## Round 8 (series A r6) — score 26.875, 9 defects, 0 irreversible, 1 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-29 r6 | `C1`'s widened command false-positives on a correct package: a retire transition, rewrapped prose, and a baseline package with no catalog on disk (stderr warning, empty stdout, exit 0 — a vacuous pass) | closed | Reviewer verified by execution; I reproduced all three before accepting. Replaced with an identity-line comparison; baseline routed to an inspection. 11 assertions, both branches |
| 2026-08-29 r6 | "Accounted for" was undefined for index lines and file headers, which the change-item `Type` list cannot express | closed | Defined in the same qualifying paragraph: they ride on the `Touches` of the item changing the file. `Type` stays a closed list |
| 2026-08-29 r6 | Authoring runs `C1` before `## Requirement Changes` exists, so its change-item clause has nothing to resolve against | closed | One clause on the pre-gate sentence; the single-home rule for the check list is untouched |
| 2026-08-29 r6 | Verifying checks specified against post-transform text but ordered before `C6` | closed | One rule for all five; `C4`'s local disclaimer deleted as redundant |
| 2026-08-29 r6 | Promotion's only worked example is a scoped change; baseline had none | closed | Derived rather than duplicated: one sentence making `C1` an inspection on baseline, per house style's "illustrate the base set, derive the rest" |
| 2026-08-29 r6 | Promotion timing keyed on mode, stranding every retro-seeded backfill | closed | Keyed to whether the behavior already ships, in both guides and the spec |
| 2026-08-29 r6 | `Touches` used two path conventions inside one example | closed | Convention stated at the field definition; outlier aligned |
| 2026-08-29 r6 | `C7` named a literal `requirements/**`, wrong under `shared`; no promotion stop for an unfillable Integration block | closed | `C7` names the Integration block's root; blocked gate added. Closes ledger item LO-1 |
| 2026-08-29 r6 | `## Artifact maintenance` read the `C1`–`C5` pass as every-response | closed | Attached to the advancing planned gate only |
| 2026-08-29 r6 | "any `- [ ]` items" unscoped against two scoped statements | closed | Scoped to `## Discussion` |
| 2026-08-29 r6 | File-split stop declared in a concept section, missing from the gate list | closed | Restated at the point of use; reasoning stays single-homed |
| 2026-08-29 r6 | Nothing said a *drafted* ID is stable, yet work specs cite `(pending)` IDs | closed | Append-only now starts at drafting |
| 2026-08-29 r6 | A package seeded by another workflow is never completed to the skeleton | closed | Reopening completes `## Goal`/`## Inputs`/`## Mode` |
| 2026-08-29 r6 | Off-normal promotion bookkeeping: readiness-failure bracket shape, retroactive `### Run 1`, gate release on return to authoring | logged | All three sit behind the standing blocked-gate route and none teaches a wrong action, so the codification bar is not met. Second sighting of the readiness-bracket half; a third codifies it. Counted as noise, not scored |

## Round 9 (series A r7) — score 56.25, 6 defects, 2 irreversible, 2 noise, 1 routed

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-29 r7 | `C1`/`C7` keyed on the package's mode, but mode is per-scope — a package "baseline for one scope" inside a live catalog rewrites the real glossary and root index with `C1` waived | closed | Introduced by round 8's own baseline fix. Re-keyed on whether the catalog already holds the file; two mode bullets collapsed into one file-keyed rule |
| 2026-08-29 r7 | The `C1` ID glob classified `MODE-1`…`MODE-9` and `NOTE-104` as filterable, so a lost requirement was suppressed by any mention in the artifact | closed | Introduced by round 8. Verified against a real catalog holding `MODE-1`…`MODE-11`. Glob widened; three assertions added |
| 2026-08-29 r7 | "Accounted for" is a substring match anywhere in the artifact; silence over an unread path reads as a pass | **open — human decision** | Third consecutive round in which the `C1` bracket is the defect. The command is being asked to encode a judgement a shell one-liner cannot make. Escalated as an architecture topic rather than patched again |
| 2026-08-29 r7 | Three sections harvested from `ui-map-architecture.md` without their defining prose | closed | `## Provisional preview` deleted; `## Assumptions and TODOs`' dropped qualifier restored; `## Artifact maintenance` bounded to its phase |
| 2026-08-29 r7 | `C6` transforms text that exists nowhere, so its evidence can only assert intent | closed | Confirmation relocated into `C7`, where the written files exist |
| 2026-08-29 r7 | `retire glossary entry` means delete, thirty lines after an ❌ forbidding deletion | closed | One clause: only a requirement keeps its heading |
| 2026-08-29 r7 | Package inventory omitted `requirements-promotion.md` and `evidence/` | closed | Two rows added |
| 2026-08-29 r7 | `README.md` still taught the superseded mode-keyed promotion timing | closed | Re-keyed. Routed out of the binding target, so not scored |
| 2026-08-29 r7 | Readiness screen leaves no trace on the success path | logged | Companion to the deferred failure-path bookkeeping item; readiness must not become `C0`. To be ruled on with it |
| 2026-08-29 r7 | `none`-shape blocked gate invites the `next` its prose refuses | logged | The blocked-gate line is inlined verbatim by house style and out of scope to vary; the prose already tells the operator the truth |

## Reversal — 2026-08-30

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 | `C1`'s widening to a whole-content check | **reverted** | Premise never held: no observed run has dropped content, the drafting rule already instructs it, and the `irreversible` label that justified the work is doubtful since any real catalog is in version control. Three successive encodings each shipped a fresh defect. `C1` is `IDs are append-only` again; identity pipeline, glob, filter, "accounted for" definition and the spec's spanning requirement all deleted; `P9` withdrawn. −137 words |
| 2026-08-30 | Silent loss of glossary entries or index lines on a whole-file rewrite | **accepted risk, stated** | The drafting rule is the obligation; no check backs it, deliberately. One sentence in `C1` names the boundary so later rounds do not re-raise it as a gap. Revisit only if an observed run actually drops content |

## Round 10 (series A r8) — score 31.875, 9 defects, 0 irreversible, 1 noise, 1 routed

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r8 | Three sites still described the deleted whole-content `C1`; one told the operator to record a lost ID as a change item rather than repair the draft | closed | Residue from the reversal — swept two members of the class and called it done. All three deleted; the full class now greps clean |
| 2026-08-30 r8 | `C7` writes then confirms, but the lifecycle rule leaves it unchecked and returns the package to authoring, so the artifact denies a write that happened | closed | Rule bounded to `C1`–`C5`; a post-write fault is repaired in place. Generalizes a principle the guide already stated for the change-request continue branch |
| 2026-08-30 r8 | Nothing distinguished a promoted package from an open one — "open" undefined, re-promotion misrouted, a `Proposed` request orphaned | closed | `## Completion` defines the promoted state; *Initiation* scopes "open" to packages holding `requirements-authoring.md` |
| 2026-08-30 r8 | Whether `auto` runs authoring's `C1`–`C5` pass was ambiguous | closed | Runs once where the gate would be; `auto` bypasses the gate, not the pass |
| 2026-08-30 r8 | `C6` and `C7` — the only mutating checks — had no worked evidence bracket | closed | Both added at the format definition; `C7`'s confirmation runs in the verify script, both branches |
| 2026-08-30 r8 | Modify-vs-retire had no pointer where the type is chosen | closed | Cross-reference clause on the `Type` bullet; rule stays in the catalog guide |
| 2026-08-30 r8 | "cannot be fixed by returning it to authoring" contradicted the change-request lifecycle and the gate line | closed | Narrowed to "by editing the package's drafts alone" |
| 2026-08-30 r8 | `Promote <N> requirements` undefined for a rewrite | closed | `N` is what the write puts into canon |
| 2026-08-30 r8 | A package populating a new scope left the root index's scope list stale | closed | Enumeration extended |
| 2026-08-30 r8 | Both handoff guides named a literal `/requirements/**` and ignored repository shape | closed | The two operational sites in `dev-retro.md` routed through the Integration block; `none` seeds nothing. Generic notation left alone. Routed out of the binding target, not scored |
| 2026-08-30 r8 | The terminal `none` gate emits the house-style line saying `next` resolves it | logged | The blocked-gate template is inlined verbatim and out of scope to vary; the prose already tells the operator the truth. A terminal-stop line would be a `process-flow.md` change and new weight for a rare path |

## Round 11 (series A r9) — score 28.375, 9 defects, 0 irreversible, 1 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r9 | "Which text does a check cover" answered three incompatible ways; the blanket phrase pulls a whole-file rewrite's untouched content into conformance | closed | Per-check scope stated, with `C1`'s and `C2`'s widenings named |
| 2026-08-30 r9 | Drafting guidance exists only for the baseline path; the scoped-change path has no assembling step | closed | *Working a scoped change* added; every rule pointed at rather than restated |
| 2026-08-30 r9 | `C4` says "run the self-check" then "do not work from a summary" — the self-check is that summary | closed | `C4` names `## Writing style` and its three lists; the four-question screen named as a drafting aid |
| 2026-08-30 r9 | The real blocked-gate line for a failed check was defined in `## Advance intent`, while `## Gates` taught the standard line that invites a forbidden `next` | closed | Line moved to `## Gates`; semantics stayed put; one definition |
| 2026-08-30 r9 | Artifacts' change-request lifecycle contradicted promotion's new `## Completion` | closed | Condition carried into artifacts; the spec corrected as the stale side |
| 2026-08-30 r9 | `## Assumptions and TODOs` and `## Out of scope` named in the skeleton, owned by no step | closed | Made operative at `## Requirement Changes` |
| 2026-08-30 r9 | Readiness condition 2's "matches" undefined; a literal text match fails on the guide's own example | closed | Names the recompute-and-reconcile operation. Accepted against the reviewer's `log-only` |
| 2026-08-30 r9 | `[A-Z-]+-[0-9]+` cannot see a digit-bearing prefix — `A11Y-03` invisible, bracket reports a green pass over a lost ID | closed | Prefix constrained to letters and hyphens: six words, correct by construction. Accepted against `log-only` |
| 2026-08-30 r9 | Both skill wrappers state the boundary as a literal path, wrong under `shared` | closed | Both say "the catalog". Accepted against `log-only` |
| 2026-08-30 r9 | The read-only claim names debugging and unit testing, which have no catalog integration | noise (re-raise), trimmed | Second sighting of the pass-1 disposition, which still stands — so it scored as noise. Trimmed anyway at five words rather than logged a third time |

## Round 12 (series A r10) — score 15, 4 defects, 0 irreversible, 2 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r10 | Four instances of one failure: a rule re-cut on its own line while every other sentence describing it stayed behind — `C4`'s rename, the per-check scope preamble, the moved gate line, the literal catalog paths | closed | All propagated across the seven surfaces. Net −9 words. The class now has a check in `verify-documented-commands.sh` rather than a resolution to sweep harder |
| 2026-08-30 r10 | `### Working a scoped change` opened "edit it in place", readable as editing the canonical catalog | closed | Names the destination: copy out of the catalog, edit the copy, never the catalog file |
| 2026-08-30 r10 | `C7`'s lead verb described patching where the model is a whole-file write | closed | The write is the operation; `## Requirement Changes` is the manifest it realizes |
| 2026-08-30 r10 | The backfill rhythm and the blocked-gate mechanic could not both be obeyed — one seeded item forced a stop, defeating spec Goal 1 | closed | The gate comes once, after the last subject in scope |
| 2026-08-30 r10 | `Touches` defined as files while the granularity rule rides a folder in it | logged | The worked example already teaches the right thing; the fix buys precision, not behavior |
| 2026-08-30 r10 | Baseline promotion has no worked example | logged | Second sighting. 60–120 words against 88 of headroom — now a budget decision, and in the ledger |

## Round 12 (series B — one-round excursion, not comparable to series A)

Prompt-fidelity failure: the prompt was built and fidelity-checked as a file, then a different prompt
was sent inline, adding a Budget paragraph naming the word count and headroom plus an instruction to
price every fix. That changed the report charter, which fixes a series. Findings were real and were
independently verified before repair; the score (15) is not comparable. Measurable distortion: the
budget appears in one triage rationale, worth 1 point.

## Round 13 (series A r10) — score 19.125, 7 defects, 0 irreversible, 0 noise, 1 routed

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r10 | `C7` named `requirements/` as the `local` root eleven lines after "Never fall back to a literal path" — a non-default root would get a stray second catalog tree | closed | Clause deleted; *Initiation* keeps the `shared` warning |
| 2026-08-30 r10 | Promotion's blocked-gate list over-enumerated `C1`–`C5`'s contents (already drifted) and under-listed the wording-change case its own routing sentence names | closed | Names the case, not its contents; missing bullet added |
| 2026-08-30 r10 | "It goes back to authoring" was orphaned behind the post-write repair rule, so "it" read as the fault that must *not* go back | closed | Deleted; `## Gates` already carries the reasoning |
| 2026-08-30 r10 | `C7`'s worked grep swept the whole catalog, failing on a pre-existing marker in an untouched file and routing the operator to edit a file the package does not hold | closed | Rescoped to the written files; both branches asserted in the verify script |
| 2026-08-30 r10 | Authoring said reopen an existing package; promotion says a promoted package is closed and invisible — the second change to a promoted subject produced a package nothing could promote | closed | Unpromoted packages reopen; a completed one is closed |
| 2026-08-30 r10 | Promotion's `none` bullet omitted the terminal clause and then claimed the filled block resolves it | closed | Clause restated at promotion's point of use; the standard-line sentence narrowed |
| 2026-08-30 r10 | The change-request trigger had two homes that drifted in scope | closed | Promotion carries artifacts' qualifier |
| 2026-08-30 r10 | "The drafting rule" was a coined term appearing nowhere in the guide it pointed at | closed | Dropped; the rule is described instead |
| 2026-08-30 r10 | The three consuming guides still hard-coded `/requirements/**`; `dev-retro.md` contradicted itself | closed (routed) | Two live contradictions fixed; prose about other subjects left |

## Round 14 (series A r11) — score 18.75, 5 defects, 0 irreversible, 2 noise, 1 routed

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r11 | Authoring's Initiation step 1 carried neither the literal-path guard nor the resolutions, and the unfilled Integration block is the default post-install state — so mode is inferred from a catalog that is not this project's | closed | Step 1 points at the blocked gate and inlines "never fall back to a literal path" |
| 2026-08-30 r11 | `C7`'s confirmation prints nothing and exits 2 when its paths do not resolve, which the guide's rule reads as a pass — on the only post-write verification | closed | Reproduced (`stdout=[] exit=2`). **Third sighting** of silence-as-proof, so codified as a rule in `## Evidence` rather than patched in the command; script asserts the rule is present |
| 2026-08-30 r11 | No worked example of a passing `C4`; `C5` has no evidence bracket anywhere | **open — human decision** | Both real, both ~40 words, guide set at exactly 10,500/10,500. Priced out, not declined. In the ledger |
| 2026-08-30 r11 | `## Assumptions and TODOs` is an unguarded bypass around the Discussion gate | closed | The test stated at *What earns an item*, where the call is made |
| 2026-08-30 r11 | "on each response … then STOP at a gate" read as ending work per subject, defeating the backfill continuity rule | closed | "end the response at a gate" |
| 2026-08-30 r11 | Promotion claimed a `next` or filled block resolves the Integration blocker ten lines after calling the `none` stop terminal | closed | Introduced by round 13's own narrowing; now names what the human supplies and defers to the bullet |
| 2026-08-30 r11 | `(pending)` ID notation named once, defined nowhere | logged | Cosmetic; the correct fix lands in `work-spec-creation.md`, outside the target |
| 2026-08-30 r11 | A package whose only change is an index line has no `Type` to ride on | logged | Stranded, not broken — the standing blocked gate covers it |
| 2026-08-30 r11 | `work-spec-creation.md` missed by the literal-path sweep | closed (routed) | Both sites now say "the requirements catalog" |

## Round 15 (series A r12) — score 15, 4 defects, 0 irreversible, 2 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r12 | `C4`'s scope included index lines while the *Forbidden* list it enforces bans file paths — and an index line is a path by construction, so `C4` failed on every package touching an index, twice per package, with no fixable exit | closed | Subject narrowed to requirement and glossary prose; index lines named as `C5`'s business. Original defect, present since the scope sentence landed in round 11 |
| 2026-08-30 r12 | The worked brackets had drifted below the checks they illustrate: `C7` confirmed 3 of 4 clauses and the dropped one is the only check for "no status fields"; `<N>`'s meaning was settled by a bracket rather than prose; `C4`/`C5` carried an undefined fourth field | closed | One re-derivation pass over both bracket blocks rather than per-bracket patches |
| 2026-08-30 r12 | A check whose subject is legitimately empty had no recordable pass — the silence rule added the previous round made baseline `C1` unrecordable, and no "empty subject" vocabulary existed in any guide | closed | Rule gained its complement, pointing at `C2`'s existing bracket as the shape. Self-inflicted, one round old |
| 2026-08-30 r12 | The "reopen, don't create a second package" rule sat after the step that creates the artifact, on the retro handoff path | closed | Relocated into the numbered list ahead of creation; list renumbered and swept |
| 2026-08-30 r12 | Worked commands hardcode `requirements/` as the catalog root | logged | The stderr warning covers the common case; parameterizing would make the examples non-runnable and unverifiable |
| 2026-08-30 r12 | Promotion timing has no stop attached, and `auto` no checkpoint | logged | Every enforcing form adds process weight; the standing blocked-gate route covers a noticing operator. Escalate to human decision only if enforcement is wanted |

## Round 16 (series A r13) — score 11.375, 5 defects, 0 irreversible, 0 noise, 2 routed

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r13 | The text moves drafts → as-it-will-be-written → catalog, and the middle state had no name, producer or home; `C7` pointed at the unstripped drafts, and authoring's "no marker of any kind" contradicted the `(D#)` it mandates | closed | State named where its vocabulary already existed; `C7` writes "that text"; authoring narrowed to *progress* marker |
| 2026-08-30 r13 | File-header prose was outside every check's stated subject, though it is written on every new file by an agent that has just read source | closed | Resolved as exclusion: a header is orientation, so it is `C5`'s business alongside index lines — consistent with the catalog guide's own rule, so no widening of an enforced check |
| 2026-08-30 r13 | The blocked-gate bullet omitted the catalog-caused branch, discarding a change request promotion is the only workflow able to raise | closed | "fails on the package", plus routing to *Raising a change request* |
| 2026-08-30 r13 | Authoring said reopen an *unpromoted* package without giving the test | closed | Restated as a pointer; promotion keeps the definition |
| 2026-08-30 r13 | "as `C2`'s bracket below" pointed 35 lines the wrong way, into another section | closed | Self-inflicted one round earlier; now names the *Promotion Checks* example |
| 2026-08-30 r13 | Spec claimed `requirements/` is created by hand, and that the gate templates are inlined verbatim and untrimmable — both false | closed (routed) | Exclusion narrowed to install time; the trim claim corrected so it stops mispricing repairs |

## Round 17 (series A r14) — score 15, 4 defects, 1 irreversible, 1 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r14 | The persisted failure output path was keyed on the check, not the run — a second failure of the same check overwrites run 1's output while run 1's bracket, deliberately retained "as history", still cites it | closed | Path now carries the run; worked example updated; script assertion added. Original defect, present since the evidence format was written and missed by thirteen rounds of reviewers |
| 2026-08-30 r14 | Three over-claiming clauses: `C4` routed header prose to a check with no prose-style clause; "baseline is the all-new case" contradicted the file-keyed granularity rule; the preamble counted two wide checks when `C7` is a third | closed | Narrowed, deleted, and counted. The precise rule was correct and adjacent in all three |
| 2026-08-30 r14 | Authoring's reopen step gave no way to find the package | closed | Names the glob `dev-retro.md` already uses |
| 2026-08-30 r14 | A backfill spanning more than one response had two contradictory instructions about ending a response | closed | States the principle and what a mid-backfill response carries |
| 2026-08-30 r14 | The change-request path is taught in three places and worked in none | logged | 60–90 words on an off-normal path; fields already enumerated. In the ledger |

## Round 18 (series A r15) — score 8.25, 5 defects, 0 irreversible, 0 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r15 | Three sites decided how a response ends; with zero items seeded one mandated the planned gate (advancing past drafting) and another the blocked gate, whose only line reads "0 open items. Resolve them" | closed | Third sighting of this class. Resolved by **deletion** of the round-17 sentence that created it, plus a drafting-complete conjunct on the advance condition and de-duplication of the resolution rule. Declined the reviewer's new blocked-gate bullet: a state the workflow need never enter does not need a gate |
| 2026-08-30 r15 | `## Raising a change request` gated the only record promotion can create on a check failure, but no listed check can detect a semantic contradiction — narrower than the spec | closed | Entry condition widened to match the spec |
| 2026-08-30 r15 | `C5` enforces three of the catalog's four traversal rules; mandatory inline cross-references has no check anywhere | **open — human decision** | A proof burden on an existing inspection. In the ledger |
| 2026-08-30 r15 | `requirements-catalog.md` still defined the catalog root as literal `requirements/` in three places, two of which collided with its own index-naming rule | closed | Literals deleted from the definitional sites; operational sites were already swept in earlier rounds |
| 2026-08-30 r15 | `Implementation` and `Agent inference` — the sources that dominate a backfill — appeared in no worked item, and `Implementation:` only as a ❌ | closed | ✅ counterpart added beside the ❌ |

## Round 19 (series A r16) — score 11.25, 5 defects, 0 irreversible, 1 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r16 | The drafting-complete conjunct added in round 18 was not propagated to the blocked-gate line, the planned-gates list, or `## Artifact maintenance`; and "in scope" collided with the catalog's defined `scope` term | **split: F1b/F1d closed, F1a/F1c open — human decision** | Fourth sighting of this class, each sighting caused by the previous round's fix. Propagation halves repaired; the substantive question — what a response ending mid-drafting emits — escalated rather than patched a fourth time |
| 2026-08-30 r16 | The index-line template works a file line only; `apps/_apps.md` consists entirely of folder lines | closed | Folder line added to the template with its rule, and the pre-existing prose statement deleted so the rule keeps one home |
| 2026-08-30 r16 | "The glossary starts empty and grows as requirements are written" is read while the catalog is being created, and the baseline example seeds an empty glossary that `C5` then fails | closed | Re-cut to growth by package |
| 2026-08-30 r16 | "promotion reads it while writing" opened the block branch during `C7`, contradicting the post-write repair rule | closed | "while preparing the write" |
| 2026-08-30 r16 | The human-request route named only "a requirement's wording", leaving other draft text unclaimed at the gate | closed | The blocked bullet names the class |
| 2026-08-30 r16 | Authoring's Discussion gate does not specify what the human is shown | logged | Presentation quality, not correctness; the artifact is the standing review surface |

## Round 20 (series A r17) — score 7.5, 3 defects, 0 irreversible, 1 noise, 1 routed

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r17 | "Every baseline package is here" placed every baseline under *behavior that already ships*, but baseline is structural — a greenfield first feature is baseline and unshipped, so the guide told the operator to promote untrue claims into canon | closed | My wording from round 11. Corrected in guide and spec; the governing test above it was already right |
| 2026-08-30 r17 | The index/folder layer was taught by diagram and example but never stated as an obligation, so four downstream references each under-specified it differently; `C4` delegated index-line style to a `C5` clause that does not exist | closed | Obligation stated at `### Index naming`; `C4`'s boundary made honest; folder rides in `Touches`; cross-reference field moved to the file line |
| 2026-08-30 r17 | The first `C4` bracket an operator meets omitted the "against Required, Forbidden and Nothing that decays in full" clause that is `C4`'s chosen enforcement | closed | Clause appended |
| 2026-08-30 r17 | The `Incorporated` precondition has two verbatim homes | logged | Both defensible under the two documents' stated contracts; no proportionate fix. Edit both together if either changes |
| 2026-08-30 r17 | `work-spec-creation.md` handed off unconditionally and asserted the handoff is "not terminal", while authoring's `none` stop is terminal — zero shape handling, where `dev-retro.md` has it | closed (routed) | Clause added; costs nothing against the four-guide cap |

## Round 21 (series A r18) — score 8.75, 4 defects, 0 irreversible, 2 noise

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-30 r18 | The catalog guide stated legacy conformance at file granularity while promotion stated it at changed-text granularity; the operator reads the catalog guide first, so a one-requirement change became an eleven-item mass rewrite | closed | "what a package writes, not what it carries forward" |
| 2026-08-30 r18 | Under `shared`, an uninitialized submodule is indistinguishable from an empty catalog — mode infers Baseline, readiness passes, and `C7` writes a bogus catalog into another repo | closed | Shape-qualified clause on both blocked gates; the `local` missing-root case deliberately untouched |
| 2026-08-30 r18 | Authoring reopens a package by judgment where promotion blocks on the same ambiguity | **open — human decision** | Adds a stop condition; whether authoring carries promotion's strictness is the owner's call. In the ledger |
| 2026-08-30 r18 | The change-request lifecycle had no disposition for "valid, but not this package's to fix", deadlocking any re-run against readiness condition 3 | closed (half) | `Rejected` extended per the reviewer's own advice; no fifth status, which UI Map shares verbatim |
| 2026-08-30 r18 | The granularity rule covered new subject files only; a baseline's glossary and root index fell through both clauses — 1 item vs 30 | closed | Rule names the catalog-root package, making R1 derivable rather than the only source |
| 2026-08-30 r18 | `## Assumptions and TODOs` is an ungated second parking lot; `C6`'s summary line invites editing the drafts | logged | No proportionate fix for the first; the second is `past-a-rule` against a bold adjacent rule |
| 2026-08-30 r18 | **Compression artifacts:** the `## Raising a change request` opening was grammatically broken by three rounds of successive edits, and `requirements-authoring.md:64-67` carried orphaned indentation from a collapsed bullet | closed | Both self-inflicted; both repaired. Paid for with a compensating trim to stay under the cap |
