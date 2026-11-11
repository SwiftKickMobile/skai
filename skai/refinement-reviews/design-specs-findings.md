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
| 2026-10-26 RG r1 | the item definition's exclusion of "what is not shown" rejected legitimate prohibitions; V9 tested form only | closed | Items: show, do or withhold; a sentence binding nothing is not one; V9 tests Items |
| 2026-10-26 RG r3 | design-specs.md assigned requirements "screen-independent promises" while the catalog keeps navigation guarantees | closed | product guarantees and thresholds, navigation included; the authoring trigger follows |
| 2026-11-10 #118 r1 | F1 "glossary entries move" read as re-sectioning within one glossary; the tool sees no change there | closed | "move, and only to another file" |
| 2026-11-10 #118 r1 | F2 root creation's one entry had no type the tool accepts | closed | "one `add spec file` entry, the root index, with the glossary and three folder indexes in `Touches`" |
| 2026-11-10 #118 r1 | F3 Operation's "decides" has no object; rule-parent clause restates `design-specs.md` | rejected | The link's title (Modify vs. Retire) is what decides; the clause is older settled text |
| 2026-11-10 #118 r1 | F4 Initiation "never overwrite or merge destinations" lost its antecedent | closed | "merge into a promoted path" |
| 2026-11-10 #118 r1 | F5 readiness 1 "under it" may read as one level | closed | ", at any depth" here and in `product-specs-promotion.md` |
| 2026-11-10 #118 r1 | F6 layout list omits `evidence/` | closed | Added |
| 2026-11-10 #118 r1 | Initiation forbade touching archived packages while `change-requests.md` rule 6 resolves a promoted request's item there | closed | "reopen or re-promote archived drafts" |
| 2026-11-10 #118 r1 | Readiness-failure gate line says "I am reopening the package" when the open item is in a promoted request | logged | The base's author reopens the base and resolves it there; same wording as the product guide |
| 2026-11-10 #118 r1 | Gate summary omits base items checked off and requests moved by a fold | logged | Adding them is process weight (supervisor call); the page shows both after the base re-render |
| 2026-11-10 #118 r1 | Anchor forms `#d27` vs `#missed-reminders` for a cited item | logged | Routed to `change-requests.md` / `product-specs-artifacts.md` |
| 2026-11-10 #118 r2 | F1 r1's "only to another file" read as a ban on re-sectioning an entry in one glossary | closed | "take `move`, and only to another file (a glossary section change is no entry)" |
| 2026-11-10 #118 r2 | F2 a known-difference note entry had no stated identity | closed | "and a note's item ID" in Identity |
| 2026-11-10 #118 r2 | F3 "never overwrite or merge into a promoted path" vs resuming a partial archive | logged | Recovery's explicit "resume archival only at either path" governs; a blocking reading ends at the designed blocked gate |
| 2026-11-10 #118 r2 | Open: moved open requests keep pages rendered at the old depth; sibling requests on one base file; unparsed entry lines draw no type message | logged | Routed to `change-requests.md`, authoring and the tool respectively; outside the binding surface |
| 2026-11-10 #118 r3 | F1 a retirement's citing files were told to ride in Touches; the tool requires entries for them | closed | "a move changes, in Touches after the `from → to`"; retirement citers fall under Granularity |
| 2026-11-10 #118 r3 | F2 an item added to an existing file needs an entry per rule; a new file's items do not | rejected | Granularity states it and the tool enforces it; the asymmetry is logged as a tool design question |
| 2026-11-10 #118 r4 | F1+F2 `check-changes` rejects a `modify rule` riding a moved item and an `add known-difference note` on a new item, both entries Granularity asks for | logged | Tool is the wrong side; routed to `Bin/spec-tool.py` as a follow-up (code change, supervisor's go) |
| 2026-11-10 #118 r4 | F3 an index-line identity linked to a file the package does not hold fails; only the index-draft link passes | logged | Single observation; the tool error and "linked to drafts" lead to the index draft |
| 2026-11-10 #118 r4 | F4 "resume archival only at either path" lost its referent | closed | "resume archival only, wherever the package now sits" (cap raised to 47,700) |
| 2026-11-10 #118 r4 | F5 move rules spread over three bullets; Identity reads without its verb | logged | Cosmetic; all within 20 lines and the tool enforces the outcome |
| 2026-11-10 #118 r4 | F6 "after promotion" unqualified where a request archives under its base | closed | "after promotion into production", as the product guide |
| 2026-11-10 #118 r5 | F1 "Draft every spec file" read as excluding the glossary and indexes; claimed promotion's repointing is a no-op | closed (part) / rejected (part) | "Draft every file"; `C2` maps draft targets to base destinations, so promotion's repointing stands |
| 2026-11-10 #118 r5 | F2 "Promotion's own failed check … returns the package to authoring" overstated the failure routes | closed | Deleted; promotion's § Gates owns every route |
| 2026-11-10 #118 r5 | F3 a footnote linked to another artifact's closed item passes readiness and surfaces only at `C3`'s post-write `validate` | logged | Tool follow-up: production readiness should fail any footnote in the drafts |
| 2026-11-10 #118 r5 | F4 move example shows no citing file after `from → to` | logged | One example, cosmetic; ~70 bytes |
| 2026-11-10 #118 r5 | F5 Archive step 1 omits `evidence/` | rejected | "Move the package intact" covers it |
| 2026-11-10 #118 r6 | F1 "move plus modify keeps one contract, the move verified first" names no action | closed | "a moved item or entry whose text changes also takes a `modify` entry" |
| 2026-11-10 #118 r6 | F2 "Input citations … are not dependencies" reads against readiness 5 | logged | Condition 5 states the block where it applies; a fix would restate `change-requests.md` rule 8 |
| 2026-11-10 #118 r6 | Open: link definitions of appended entries on a fold; entry order after a fold | logged | Routed to `change-requests.md` 4.1; the base's `check-changes` catches a missing definition |
| 2026-11-10 #118 r7 | F1 an intro- or orientation-line-only change had no stated entry | closed | Touches template: "alone under `modify spec file`"; tested |
| 2026-11-10 #118 r7 | F2 "promotion verifies identical prose" read as absolute before the modify exception | closed | Exception first, "otherwise promotion verifies…" |
| 2026-11-10 #118 r4–r5 tool | `check-changes` rejected `modify rule` on a moved item and `add known-difference note` on a new item; a linked footnote whose owner closed passed | closed | Fixed in `check_changes`, each with a reproducing test (supervisor's go) |
| 2026-11-10 #118 r8 | Tool: a note or retired-rule entry on a moved item still rejected after the r7 patch | closed | `check_changes` judges any part entry riding a move against the item's change; tests added |
| 2026-11-10 #118 r8 | F2 "alone under `modify spec file`" had two readings | closed | "or with no other entry for its file takes `modify spec file`" |
| 2026-11-10 #118 r8 | F3 an item changing section within its file had no stated answer | closed | "(a section change within a file is no entry)" |
| 2026-11-10 #118 r9 | Tool: a moved item's changed parts were not each required; a renumbered gap footnote read as a modified item; `modify spec file` covered its intro only through its own Touches | closed | Fixed in `check_changes` and `diff_key`, each with a test |
| 2026-11-10 | Pass closed | closed | Clean round r9 (stop rule a): no live finding in the binding target. Rounds r1–r9: 13 · 8.125 · 5 · 6.5 · 5.375 · 2.75 · 4.75 · 2.5 · 0. The set 47,459 → 47,694 / 47,700 |
