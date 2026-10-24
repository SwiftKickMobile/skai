# Design process — findings log

Targets: `Guides/Design/design-authoring.md`, `Guides/Design/design-promotion.md`. Standard: [`design-process-design.md`](design-process-design.md).

## 2026-10-12 — design-authoring.md, series 1

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-12 r1 | F1: "draw every resolved item" read as the drawing scope, though Discussion holds only decisions | closed (superseded by r2 F1) | Restated at r2 |
| 2026-10-12 r1 | F2: a visually-judged item stayed unchecked, blocking the mockup phase it needed | closed | The supervisor resolves it by approving the recommended option as a trial; the mockup shows it, feedback settles it |
| 2026-10-12 r1 | F3: gate note and Mockups gave different feedback transitions | closed | One sequence in Mockups (apply what needs no decision; park the rest with dependent drawing; review gate or Discussion gate); Phases and the gate note point to it |
| 2026-10-12 r1 | F4: reopening an approved, unpromoted package left Design Changes standing as approval evidence | closed | A reopen that changes the designs removes Design Changes; rewritten after the next approval |
| 2026-10-12 r1 | F5: a draft's new component had no placement satisfying both the authoring boundary and the tool guide | routed | Fixed in `figma-designer-guide.md` (Components 1, Screen pages 7): a change page holds a draft's new components until promotion |
| 2026-10-12 r1 | F6: example proposal assigned defect logging, outside scope | closed | Clause deleted |
| 2026-10-12 r1 | F7: intervening production changes on reopen unspecified | logged | No occurrence; the general blocked gate covers a conflict that stops work |
| 2026-10-12 r2 | F1: "each resolved decision applied" reinstated a decision later feedback changed | closed | Mockups: draw the whole change as the decisions and any later feedback currently stand; a changed decision is history |
| 2026-10-12 r2 | F2: a decision discovered while drawing has only the generic blocked gate | logged | No occurrence; the generic gate is a safe stop |
| 2026-10-12 r3 | No live findings | closed — clean fresh round | Reviewer confirmed the r1–r2 repairs; one open tension (judging what needs a decision) left to the existing criterion |

Series 1 (authoring): r1 10.625 → r2 2.5 → r3 0. Converged by a clean fresh round. Size 14,441 →
14,790 bytes against the 16,000 cap. `design-promotion.md` not yet reviewed.

## 2026-10-12 — design-promotion.md, series 1

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-12 p1 | F1: the authoring-return gate line covered any failed check, though C3/C4 faults are repaired in place; "C4 changes production" was wrong | closed | Line limited to readiness, C1, C2, requested design change; C3/C4 mistakes repaired in place, never by redesign; missing access takes the standard line |
| 2026-10-12 p1 | F2: C3 "nothing outside the inventory changes" forbade the placement it also required | closed (superseded by p2/p3) | Restated twice; final wording at p3 |
| 2026-10-12 p1 | F3: production review gate line said "Production reviewed" before the review | closed | Line now asks for the review and names the change page to delete |
| 2026-10-12 p1 | F4: recovery after rejection at production review unspecified (restore target; links already repointed) | logged | No occurrence; route mechanics to the tool guide when one appears |
| 2026-10-12 p2 | F1: "on re-run every check is unchecked" plus readiness sent an unfinished promotion to authoring | closed | Unfinished promotion continues from its pending check or gate; reset applies to a new run after an authoring return; readiness is for a new run |
| 2026-10-12 p2 | F2: C3 "new components move to the library" overrode the tool guide's placement exceptions | closed (superseded by p3 F1) | Restated at p3 |
| 2026-10-12 p3 | F1: C2 "extra drafts" rejected a draft's supporting components; C3's component clause had no referent (third round on that clause) | closed — class fix | No component mechanics in the process guide: C2 inventories screen drafts, C3 integrates components "as the tool guide says". Invariant P1: the process guide says what promotion must achieve; how designs are arranged is the tool guide's |
| 2026-10-12 p3 | F2: the artifact alone cannot show whether a gate was advanced when resuming without the conversation | logged | No occurrence; the standard blocked gate covers missing authorisation |
| 2026-10-12 p4 | F1: C1 read as "a script, if any, is the whole check" | closed | A script covers the rules it tests; inspect the rest; evidence example shows both |
| 2026-10-12 p4 | F2: an evidence-only readiness failure fits neither continuation nor new-run wording cleanly | logged | New-run path; no occurrence |
| 2026-10-12 p5 | No live findings | closed — clean fresh round | Reviewer confirmed all repairs; residual risks are operator diligence, not wording |

Series 1 (promotion): p1 6.875 → p2 4.375 → p3 2.5 → p4 2.5 → p5 0. Converged by a clean fresh
round. Size 11,264 → 11,812 bytes against the 12,000 cap.
| 2026-10-12 post | Tim: per-tool skills were inconsistent with UI Map implementation, which is one skill whose guide loads the stack guide | closed — by ruling | Skills renamed `skai-design-authoring` / `skai-design-promotion`, tool-agnostic; each process guide's Purpose now loads the tool guide for the project's design tool (Figma → `figma-designer-guide.md`), told from the README's design-file link. Sizes 14,860 / 11,872 bytes, under their caps |
| 2026-10-12 post | SKAI Release 11 merged after both series: typed packages (`skai/changes/<id>/design/`, archived to `skai/promoted/<id>/design/`), Project addendum boilerplate, configure metadata | closed — by ruling (Tim: revisit the skills for addenda and configuration) | Authoring: package path, scan path, promoted = closed. Promotion: artifact path, readiness item 4, `C6 Archive the package`, Completion. Both guides carry the addendum cue and footer; skills read the guide "in full, including its Project addendum instructions"; manifest gains a Design category with labels. Caps raised to 16,500 / 13,500 for the boilerplate. Not re-reviewed |
| 2026-10-21 gaps r1–r2 | The mirror sentence in authoring § Discussion and promotion `C1`'s "none still mirrors a gap" reviewed with the Figma guide's § Gaps | converged | no finding against either sentence; simulations of first placeholder, change, closure, leftover annotation and no-placeholder gap all routed; see `design-process-refinement.md` § Slice 5 |

## 2026-10-23 — change requests: authoring against a base (series CR)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-23 r1 | F1: "request a design change to <package>" let Initiation reopen the named base instead of creating the request | closed | Initiation 2: a request signal names the base; create the request unless an existing request for this work is named or in context |
| 2026-10-23 r1 | F2+F4: drawing-dependent instructions (trace pass, feedback, Base review, identity, readiness 3, C2, C4, C5) after the model allowed undrawn entries and removals; spec promotion items 2 and 4 universal | closed — spec clarified first | Spec § Clarification — 2026-10-23; the list stands in for the drawings under the ruling; identity, readiness 3 and C4 by operation (`remove` names the base design, unlinked); Base review covers the base's list for undrawn entries; C5 deletes drafts where one exists |
| 2026-10-23 r1 | F3: the Design Changes form omitted the `- ` list marker the renderer requires; unbulleted entries vanish from the page | closed — verified | Test artifact: unbulleted entry not rendered, bulleted one rendered; the guide shows the full `- V<n> …` line |
| 2026-10-23 r1 | F5: both process guides over their caps (110 / 106) | closed | Duplicated text trimmed; 16,080 / 12,088 after the round |
| 2026-10-23 r1 | Open question (a): the base is a request's first input while Completion files requests per changed input | closed — folded into F2 | Completion reconciles "every input but the base" |
| 2026-10-23 r1 | Open question (b): a request modifying a screen the base lists as an addition appends a second entry for that screen | logged | Entries are per change with provenance; the base's author merges on its next round if wanted; no occurrence |
| 2026-10-23 r2 | F1: the trace pass and the feedback path routed unconditionally to Review, competing with the Discussion blocked gate when the pass raised an item | closed | Both end "at the gate *Gates* prescribes" |
| 2026-10-23 r2 | F2: C2 inventoried every draft on the shared change page, counting an unpromoted sibling request's section against the base | closed | C2: every screen draft of this package |
| 2026-10-23 r2 | Open question: status of open child requests once the base promotes (page deleted, folder archived intact) | logged | No occurrence; no readiness rule inferred |
| 2026-10-23 r3 | F1: C4 "including appended entries" can read as demanding a drawing for undrawn entries; C3 states they stay unlinked | logged | No occurrence; the exception sits in C3 at its point of use; sharpen C4's scope if it recurs |
| 2026-10-23 r3 | Terminal round: no live findings | converged | stop rule (a); series CR: r1 11.375, r2 4.375, r3 0 |

## 2026-10-23 — change list mirrors the page (series CL)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-23 r1 | F1: structure check mandated on the no-mockups path | closed | "with drawings" in Mockups and C1 |
| 2026-10-23 r1 | F2: C1 evidence excerpt claimed a bindings check the script does not do | closed | line deleted |
| 2026-10-23 r1 | F3: C4 re-rendered only the base's page | closed | every page whose artifact changed |
| 2026-10-23 r1 | F4: per-section V numbering ambiguity | closed | one sequence per package, in guide and spec |
| 2026-10-23 r2 | F1: Figma Screen pages 7 and Components 1 contradicted the request hierarchy | closed | content rule scoped to screen Sections; components in the package's own Components Section |
| 2026-10-23 r2 | F2: C2 forbade an entry for a component that is a change | closed | sentence deleted |
| 2026-10-23 r2 | F3: a base's structure check also checks its open child requests' sections | logged | no occurrence; the edit boundary and the blocked gate cover it; a package filter in the script if it recurs |
| 2026-10-23 r3 | F1: known-gaps rule 6's universal zero-gap requirement vs promotion into a package | routed — fixed in `Guides/Core/known-gaps.md` | "into production"; a workflow promoting into another open package carries them |
| 2026-10-23 r3 | F2: Figma pair 22 bytes over cap after the r2 repair | closed | tooling 7 shortened; pair 17,895 |
| 2026-10-23 r4 | F1: tooling 7 overstated the structure check's coverage | closed | "reports the breaches its header lists" |
| 2026-10-23 r4 | F2: authoring named the change page `<change-id>` against the tool guide's page-name convention | closed | the tool guide names the page |
| 2026-10-23 r4 | Open question: a request's removal of a frame the base's list links | logged | no occurrence; blocked route |
| 2026-10-23 r5 | Terminal round: no findings | converged | stop rule (a); series CL: 18.75, 3.75, 2, 7.5, 0 |

## 2026-10-24 — inherited gaps as footnotes (series GF)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-24 r1 | F1: known-gaps rule 6 told authoring to resolve inherited marks locally | closed | own gaps resolved (4), inherited marks wait on their owners (5, 7) |
| 2026-10-24 r1 | F2: the card state hid inherited gaps when no Discussion item existed | closed — tool | state "no discussion items; N gaps carried"; test |
| 2026-10-24 r1 | Open question: "the page's Sections" vs the base's for nested requests | logged | no misroute; C3 is operational |
| 2026-10-24 r2 | F1: no named input catch-up route in design authoring for an upstream answer differing from the placeholder | logged | Discussion, reopen and Mockups cover it; blocked gate for a strand |
| 2026-10-24 r2 | Terminal round: no live findings | converged | stop rule (a); series GF: 3.875, 0 |
| 2026-10-24 in use | The agent labelled footnotes with the owning item's ID (`[^d15]`); the guide said only "labels unique per artifact" | closed | "numbered by first use"; observed on CR-001 |
| 2026-10-24 in use | One gap spans several entries; the agent defined its footnote once and marked the rest, so marks linked to notes under another card | closed — by ruling | a render issue: the artifact defines a gap once, the renderer shows the note under every entry that marks it; guide sentence says so |

## 2026-10-24 — one gap footnote for every artifact (series FN)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-24 r1 | F1: scoped owners unlinked on spec pages; inherited-only packages no gaps tile; base lost after archive | closed — tools | shared owner resolver, tooltips, count; tests |
| 2026-10-24 r1 | F2: validate did not enforce numbering by first use | closed — tool | check added; Offers drafts renumbered |
| 2026-10-24 r2 | F1: the shared guide let a designer take rendering for validation and a spec author read a marked open gap as a failure | closed | tooling paragraphs scoped to spec drafts; pairing spelled out; design pages only render |
| 2026-10-24 r3 | F1: the shared guide claimed footnoted items count as modified; the renderers keep the entry's operation | closed | claim deleted |
| 2026-10-24 r4 | Terminal round: no findings; open question on the spec tool's modified class for footnoted existing requirements | converged; question closed, by design | stop rule (a); series FN: 5.5, 3.75, 2, 0 |

## 2026-10-24 — writing style guide and design change prose (series WS)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-24 r1 | F1: the sub-change example taught a citation-only justification (reason before the separator) | closed | example rows rewritten |
| 2026-10-24 r1 | F2: unqualified first person conflicted with requirement voice | closed | rule 5 scoped to the agent's own actions, recommendations, questions |
| 2026-10-24 r1 | F3: spec-tool help and diagnostic kept the old Placeholder wording | closed — tool | strings replaced |
| 2026-10-24 r1 | "contract phrasing" readable as banning normative language; ❌/✅ pair weak on the outside-reader test | logged | wait for recurrence |
| 2026-10-24 r2 | Terminal round: no findings; vacuous reason sentences and the generic ❌/✅ pair logged | converged | stop rule (a); series WS: 10, 0 |

## 2026-10-24 — footnote owner is where the question was raised (series GO)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-24 r1 | F1: spec tool counts a footnoted existing requirement as modified | noise — by design; prompt disposition misquoted the FN r3 ruling a second time | `spec-format-design.md` convention; FN r4 record |
| 2026-10-24 r1 | F2: numbering rule read as spec-only from its place in the validate sentence | closed | relocated into the form sentence |
| 2026-10-24 r1 | F3: owner link resolves immediate base and linked specs only | logged | wait for recurrence |
| 2026-10-24 process | A paraphrased disposition in a cold-review prompt produced the same noise twice | closed — practice | prompts quote dispositions from the refinement record verbatim |
| 2026-10-24 r2 | F1: pairing sentence keyed on the footnote's location, not its owner | closed | sentence sharpened |
| 2026-10-24 r2 | F2: package page's gaps tile skipped requirements footnoting local owners | closed — tool | count every footnoted requirement |
| 2026-10-24 r2 | F3: request page rendered footnotes without owner links or a gaps tile | closed — tool | request owners from its package; fixture, test |
| 2026-10-24 r3 | Terminal round: no accepted findings; a resolved chip is not proof of ownership (past-a-rule) | converged; logged | stop rule (a); series GO: 2.5, 8.25, 0 |

