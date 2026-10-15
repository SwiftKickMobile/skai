# Design Specs — Findings Log

Target: `Guides/DesignSpecs/*.md` and the two `skai-design-specs-*` skill wrappers. Standard:
`design-specs-design.md`. One row per finding per pass; appended at closure.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-14 p1 r1 | F1 Never Appearance had no test; V2 said "rule"; promotion example taught a word list | closed | Redesign test + ❌/✅ in Never Appearance; V2 cites it; grep evidence example gone |
| 2026-10-14 p1 r1 | F2 Glossary: one alphabetical list, no purpose/inventory rule, V9 blind | closed | Glossary rewritten per D5 (purpose first, secondary detail, no inventory/position/appearance, sections by governing item's home, entries move with items, split seams); V9 checks it |
| 2026-10-14 p1 r1 | F3 overrides: no required declaration or link direction | closed | Citing by Reference owns it; parent never names overrides; restating allowed; V6 checks both ways |
| 2026-10-14 p1 r1 | F4 item opening statement + requirement link demonstrated, not required; part prose unbounded | closed | Spec File Shape requires it; nonbinding one-line part intro allowed; V9 enforces |
| 2026-10-14 p1 r1 | F5 V8 lacked the prefix-kind rule | closed | IDs and V8 carry it |
| 2026-10-14 p1 r1 | F6 motion/polish had no home; "words mean the design is incomplete" misrouted it; V10 blind | closed | Fourth home in What Counts as a State; V10 asks the careful-developer question; sentence deleted |
| 2026-10-14 p1 r1 | F7 no audit entry; reopen routed to drafting | closed | Audit paragraph in Initiation (checks over every draft before any edit, failures as Discussion items); wrapper trigger; What Earns an Item; Artifact Maintenance |
| 2026-10-14 p1 r1 | F8 whole-file scope vs "pre-existing defects do not block" | closed | One scope in Purpose and Promotion Checks; untouched canonical files not re-examined |
| 2026-10-14 p1 r1 | F9 size 76,459 vs 60,000 | closed | Trims in r1 (−5,900) and the r2 section rewrites: 58,418 at r2 closure. Gate template kept as fixed cost (skai issue #75) |
| 2026-10-14 p1 r1 | A1 V8 "every ID stays in its draft" vs permitted moves | closed | V8 allows a declared move's destination |
| 2026-10-14 p1 r1 | A2 scoped example showed a contract change as `modify` | closed | Example is a clarification of the same promise |
| 2026-10-14 p1 r1 | A3 sub-item `move` vs retire-and-add | closed | `move` applies to items only; parent change is retire-and-add |
| 2026-10-14 p1 r1 | A4 `Proposed` request both permits continuation and blocks | closed | Blocks at readiness; continue-branch ride-through preserved |
| 2026-10-14 p1 r2 | F1 V1 rejected nonbinding glossary/index prose V9 requires | closed | V1 scoped to requirement-citing binding prose |
| 2026-10-14 p1 r2 | F2 examples competed with repaired rules | closed | Glossary example under its family; intro binding claim removed; appearance exceptions named; purpose-led ✅ examples |
| 2026-10-14 p1 r2 | F3 move-plus-modify failed readiness; C2 needed writes outside the package | closed | Move identity verified before the declared modify; incoming-link files drafted and in the move's Touches; C2 works through them |
| 2026-10-14 p1 r2 | F4 untouched-file defects both non-blocking and blocking | closed | Unrelated ones do not block; write-invalidating contradictions follow Raising a Change Request |
| 2026-10-14 p1 r2 | F5 V3 evidence example was a word-list grep (verified by the reviewer) | closed | Sentence-level inspection evidence |
| 2026-10-14 p1 r2 | Open: Global vs Shared wording for every-screen terms; V10 "design and app" with no app; Title Case not stated | logged / Title Case added | Governing-item home decides placement; generic blocked route covers the no-app case until a strand occurs; "Title Case headings." added to Spec File Shape |
| 2026-10-14 p1 r3 | F1 general permission to restate another spec's rule defeated extraction; V7 blind to spec-to-spec copies | closed | Restatement only by a declared override (Layout, Restatement, V7) |
| 2026-10-14 p1 r3 | F2 V9 did not require entry detail to be supported by linked items; V10 started from existing items so omissions escaped | closed | V9 requires supported detail; V10 opens with source-to-spec coverage |
| 2026-10-14 p1 r3 | F3 promotion example lost its evidence lines and fence (round-2 apply defect), swallowing the Evidence section | closed | Example restored; fence-balance check added to the sweep |
| 2026-10-14 p1 r3 | F4 content guide duplicated change-request routing with a different answer | closed | Purpose routes to the artifacts guide § Change Requests |
| 2026-10-14 p1 r4 | F1 reopen's "copy from canon" could replace an existing draft | closed | Reuse existing drafts; initialize missing ones from canon |
| 2026-10-14 p1 r4 | F2 V3 and its evidence inspected "rules" only; example omitted earlier evidence unlabelled | closed | V3 covers all spec text (platform names only in known-difference notes); example labelled Excerpt |
| 2026-10-14 p1 r4 | F3 pending requirement both returned the package and waited | closed | Canonical requirements are a prerequisite that waits at the blocked gate; readiness failures return to authoring |
| 2026-10-14 p1 r5 | F1 readiness blocked on a draft link after the contract was canonical | closed | Prerequisite tests the contract; C2 repoints the link |
| 2026-10-14 p1 r5 | F2 `S` IDs "in document order" vs never-renumber and presentation order | closed | "in document order" deleted |
| 2026-10-14 p1 r5 | F3 Touches let index changes ride while granularity required entries | closed | "index/" deleted from Touches |
| 2026-10-14 p1 r5 | F4 reusing a draft against intervening canon has no merge rule | logged | No occurrence; readiness exposes a mismatch; sharpen Initiation's reopen rule if it strands |
| 2026-10-14 p1 r6 | F1 V10 accepted "confirmed absent from the design and app" as passing motion | closed | Clause deleted; the careful-developer test alone |
| 2026-10-14 p1 r6 | F2 a new file's index line fell under both granularity sentences | closed | Existing-file sentence covers each *other* change |
| 2026-10-14 p1 r7 | F1 V5 "every named state" demanded drawings for app-only states in known-difference notes | closed | V5 checks every *prescribed* state or variant |
| 2026-10-14 p1 r8 | F1 new-file entries summarized while the inline-text rule had no new-file exception | closed | Inline text scoped to changes inside existing files; a new file's entry summarizes and links the draft (spec D9 clarified) |
| 2026-10-14 p1 r8 | F2 V8/V9 rejected the prescribed retirement form | closed | V8 accepts retirement in place; V9's opener applies to live items |
| 2026-10-14 p1 r9 | F1 applicability clause made a known-difference note an exception | closed | Clause deleted; the note records a gap |
| 2026-10-14 p1 r9 | F2 V8 did not check duplicate live IDs across packages | closed | V8 rejects duplicate IDs in projected canon |
| 2026-10-14 p1 r9 | Appendix: README Usage summary drifted (inline text for every item; verification in Spec Changes) | routed → README fixed | Usage defers to the guide on format and timing |

Pass 1 converged by a clean round: round 10 (series B) raised no finding. Rounds: r1 A 28.875 · r2 B 14.375 · r3 B 9.375 · r4 B 6.25 · r5 B 6.25 · r6 B 5 · r7 B 2.5 · r8 B 5 · r9 B 4.375 · r10 B 0. Series changed at r2 when the charter added reviewer-proposed replacement text. Size 76,459 → 59540 (budget 60,000; gate template fixed, issue #75).
| 2026-10-14 p1 eval 1 | Clean audit run missed motion/polish although V10 asks for it; found once hinted | logged (first sighting) | V10 reads as a check on written text; candidate: "look at the design and the app for…". Codify on recurrence in evaluation (2) |
| 2026-10-14 p1 eval 1 → repair | V10 motion clause checked the drafts, not the sources (second sighting: the supervisor's analysis) | closed | V10 says where motion comes from (code in a backfill; the designer's statement otherwise) and that unstated motion is a Discussion item |
| 2026-10-14 p1 r11 | F1 Restatement's enumerated test would cut motion rules V10 requires | closed | "an added screen binding", matching V1 |
| 2026-10-14 p1 r11 | F2 "clarified or tightened" let a stricter contract keep its ID | closed | "or tightened" deleted; the conformance test decides |
| 2026-10-14 p1 eval 1 re-run | Clean audit after the V10 change found motion from the code unprompted (nine items) and every other critique group | closed by observation | One run; a second miss would reopen this |
| 2026-10-14 p1 r12 | F1 move summaries forced `modify` for every text change | closed | Both summaries defer to Modify vs. Retire |
| 2026-10-14 p1 r12 | F2 V1 evidence example demonstrated the old test | closed | "compared with cited contracts; each adds a screen binding" |
| 2026-10-14 p1 r13 | F1 "changing a row modifies the item" bypassed Modify vs. Retire | closed | "data edits follow Modify vs. Retire" |
| 2026-10-14 p1 r14 | F1 retirement "replaces the body", erasing descendant IDs V8 requires | closed | Headings and rule segments kept, marked retired; binding text replaced |
| 2026-10-14 p1 r14 | F2 universal drafting constraints under a baseline-only heading | closed | Relocated into Drafting |
| 2026-10-14 p1 r15 | F1 new-file grouping swallowed a declared move into the new file | closed | Incoming moves listed separately from a new file's own items |

Pass 1 closed by supervisor ruling after round 15 (stop rule b): no unimplemented findings; rounds 11–15 scored 5 · 4.375 · 2.5 · 3.75 · 1.875, each one or two consistency defects adjacent to the prior repair. Final size 59658. Evaluation runs: clean audit (after V10's source clause) caught every critique group unaided; fresh authoring of a new screen conformed.
| 2026-10-14 backfill b1–b2 | Authoring's check pass produced no evidence; agents reported "pass" and a cold conformance review found 10 and 12 defects (two sightings) | closed | Evidence line per check under `## Verification` before the gate; spec D10 amended |
| 2026-10-14 backfill b1–b2 | Five rules missed at drafting in both buckets (cite-not-copy, glossary counts/position, motion as substitution, position words, static copy) | closed | ❌/✅ examples added to the three rules lacking one |
| 2026-10-14 p1 r16 | F1 component-appearance example stated a difference, not a condition→variant mapping (twice) | closed | Example maps condition to named variant; duplicate deleted |
| 2026-10-14 p1 r17 | F1 badge example applied pending variants outside the pending state | closed | "When pending: …" |
| 2026-10-14 p1 r17 | F2 incoming-link repair covered moves only; retirement changes heading anchors | closed | Moves and retired headings, in authoring, artifacts and promotion C2 |
| 2026-10-14 p1 r18 | F1 "a glossary name brings all governing items" readable as implicit inheritance | logged | No occurrence; Glossary's "never binds" governs. If it strands, delete the clause (−44 bytes) |

Pass 1 re-converged by a clean round: round 18 (series B) after the post-backfill repairs (evidence per check, three examples, r16–r17 fixes). Rounds 16–18: 2.5 · 4.375 · 0. Size 59,958.
| 2026-10-15 backfill b1–b3 | Authors' self-checks passed while a cold reviewer found 10–13 defects per bucket; proposed a required delegated cold check before the Discussion gate | rejected (supervisor) | Review mechanics are not baked into the guide; whether and when to run a cold check is a supervisory decision per package. Do not re-raise |
