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

## 2026-10-25 — change requests as authoring against a base, spec guides (series CA)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-25 r1 | F1 validate skipped a request's bases | closed — tool | infer_bases in validate |
| 2026-10-25 r1 | F2 base check-changes right after the fold | closed | reconciliation on reopen |
| 2026-10-25 r1 | F3 folded citations re-read as the base's | closed | shared rules 5–6; checker skips `Change request:` entries |
| 2026-10-25 r1 | F4 item moves compared against the catalog | closed — tool | layered baseline |
| 2026-10-25 r1 | F5 rule 9 included the base | closed | "but your base" |
| 2026-10-25 r1 | F6 promotion artifact path hardcoded | closed | beside the authoring artifact |
| 2026-10-25 r1 | F7 base contradiction returned the package | closed | own blocked-gate bullet |
| 2026-10-25 r1 | F8 docstring request page; "unruled"/"statuses" | closed | deleted; reworded |
| 2026-10-25 r1 | F9 migration not discoverable on reopen | logged | release work |
| 2026-10-25 r1 | shipping and canonical-citation rules read as binding folds into packages | closed | scoped "into production" |
| 2026-10-25 r2 | F1 Completion's shipping rule unscoped | closed | points at promotion's rule |
| 2026-10-25 r2 | F2 validate's baseline was the first root only | closed — tool | every root but the last |
| 2026-10-25 r2 | F3 unchanged inherited footnote read as modified | closed — tool | footnote set compared |
| 2026-10-25 r2 | F4 design-spec rule entries checked at item grain | closed — tool | rule-level entries and checks |
| 2026-10-25 r2 | F5 known-gaps rule 8 competed with filing triggers | closed | reworded |
| 2026-10-25 r2 | F6 ancestor-owned gap in a nested request | logged | wait for occurrence |
| 2026-10-25 r3 | F1 design-specs V6 and § IDs assumed production | closed | V6 sentence deleted; IDs from the base |
| 2026-10-25 r3 | F2 link regression compared against the first root only | closed — tool | baseline of every root but the last |
| 2026-10-25 r3 | F3 `base D3` not said to become `D3` on fold | closed | rule 6 |
| 2026-10-25 r3 | F4 redundant parent entry beside rule entries allowed | logged | — |
| 2026-10-25 r4 | F1 untouched-base exemption covered introduced conflicts | closed | "already in" |
| 2026-10-25 r4 | F2 Requirements Gaps waited for upstream promotion unconditionally | closed | clause deleted |
| 2026-10-25 r4 | F3 C1 overclaimed check-changes on missing items | closed | reworded |
| 2026-10-25 r4 | F4 design-specs.md routed to the removed § Change Requests | closed | shared guide |
| 2026-10-25 r5 | F1 link targets compared by file name | closed — tool | normalized relative path |
| 2026-10-25 r5 | F2 concept inventory against the catalog | closed | the base |
| 2026-10-25 r5 | F3 authoring and promotion disagreed on unchanged content | closed | scope owned by design-specs.md |
| 2026-10-25 r6 | F1 Audit blocked on inherited defects | closed | scoped |
| 2026-10-25 r6 | F2 `Base decision: D#` rejected by the checker | closed — tool | stripped before the check |
| 2026-10-25 r6 | F3 file identity by name; moves compared unrebased links | closed — tool | paths; rebased link definitions |
| 2026-10-25 r6 | F4 catalog citation fallback skipped the base; stale routing | closed | reworded |
| 2026-10-25 r7 | F1 index-line identities lost their path | closed — tool | paths kept for index types |
| 2026-10-25 r7 | F2 rule tables compared as raw text | closed — tool | resolved-cell comparison |
| 2026-10-25 r7 | F3 citation fallback one level deep | closed | base chain |
| 2026-10-25 r8 | F1 link identity by spelling; base targets unmatched | closed — tool | rebased and re-rooted link definitions |
| 2026-10-25 r8 | F2 design index lines rode in Touches | closed | own entry unless with the new file |
| 2026-10-25 r9 | F1 links into the catalog normalized differently per layer | closed — tool | layer-aware logical paths |
| 2026-10-25 r9 | F2 validate read a cross-layer link from disk | closed — tool | resolves through the projection |
| 2026-10-25 r9 | F3 index rider needed only a file-typed entry | closed — tool | the described file |
| 2026-10-25 r9 | F4 intro rider renders without a reason | logged | — |
| 2026-10-25 r10 | F1 external URLs identified by fragment | closed — tool | whole destination |
| 2026-10-25 r10 | F2 file links keyed by label collided | closed — tool | place only |
| 2026-10-25 r11 | F1 index rider accepted existing files | closed — tool | added files only |
| 2026-10-25 r11 | request fixture's glossary links | closed — fixture | base's glossary; validate in the test |
| 2026-10-25 r12 | Terminal round: no findings | converged | stop rule (a); series CA: 31.25, 19.375, 11.25, 10, 10, 14.375, 11.875, 10, 11.25, 10, 1.25, 0 |

## 2026-10-25 — plain language in the spec, UI Map and work-spec guides (series PL)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-25 r1 | spec F1: a citation sufficed as a Justification; "entries carry no text"; folded provenance first | accept — verified | both artifacts guides, both promotion guides, shared rule 5, checker |
| 2026-10-25 r1 | spec F2: Tradeoff example taught letter-only proposals; Resolution let a state label stand for the decision | accept | example; process-flow owner sentence swept to five copies |
| 2026-10-25 r1 | spec F3: "package prose may name frames, nodes and files" | accept | narrowed to where the reader must go |
| 2026-10-25 r1 | spec F4: gap footnote names its owner by ID only | noise — settled 2026-10-24, reaffirmed 2026-10-25: the gap item is the source of truth, the footnote states the placeholder for this item, the owner link and tooltip are for more | prompt omitted the disposition |
| 2026-10-25 r1 | spec F5: Restatement examples shrink to a citation | accept | subject kept before the citation |
| 2026-10-25 r1 | spec F6: C4 / V3 check content rules only; C4 failure example names no defect | accept | apply the writing guide; example names the defect |
| 2026-10-25 r1 | spec F7: gate wording in guide vocabulary | accept — cosmetic | reworded in place |
| 2026-10-25 r1 | uimap F1: "the Justification is just the citation"; `Realizes` as explanation | accept | reason then source; Realizes traces only |
| 2026-10-25 r1 | uimap F2: gate says "implement" in Plan mode; scoped audit completes as whole-app conformance | accept | templates say the real next action and scope |
| 2026-10-25 r1 | uimap F3+F4: domain line, Discussion and annotation examples teach shorthand | accept — one defect | examples repaired together |
| 2026-10-25 r1 | uimap F5: evidence bracket as the whole record | accept — cosmetic | a result sentence before the bracket |
| 2026-10-25 r1 | uimap F6: eight guides without the writing-style pointer | accept | pointer added |
| 2026-10-25 r1 | workspec F1: image-loading example without substance in both guides | accept | one example across both |
| 2026-10-25 r1 | workspec F2: no-items sentence and "link or summarize" let the agent point instead of state | accept | both sharpened |
| 2026-10-25 r1 | product-specs-baseline without the pointer (not raised; checked) | log-only | read only from authoring |
| 2026-10-25 r2 | spec F1: the review page dropped the no-items Discussion sentence | closed — tool (both renderers), test | `discussion_note` |
| 2026-10-25 r2 | spec F2: an intro covered through a requirement entry's Touches rendered without its reason (second sighting of CA r9 F4) | closed — tool, test | `why_for` fallback takes every covering entry |
| 2026-10-25 r2 | spec F3: evidence examples led with bookkeeping, not the result | closed | form and seven examples result-first, both promotion guides |
| 2026-10-25 r2 | spec F4: reconciliation kept a justification for a matching ID whatever it still explained | closed | "only while it still explains the current difference", both authoring guides |
| 2026-10-25 r2 | spec F5: product authoring Completion omitted whether promotion can follow | closed | Completion says now or waits on shipping |
| 2026-10-25 r2 | uimap F1: empty-Discussion sentence claimed the inputs determined the map | closed — class swept | sentence, example, gate paragraph; design-authoring's no-items sentence too |
| 2026-10-25 r2 | uimap F2: Code Changes gate summary was path, counts and links | closed | leads with what changes in the app; ❌/✅ pair |
| 2026-10-25 r2 | workspec F1: evidence examples and the requested-stop line carried only metadata | closed | result in words first; stop line names the next task's outcome |
| 2026-10-25 r2 | workspec F2: Why templates and example gave a reason without its source | closed — owner swept | process-flow defines Why as reason then source; four guides' example Whys cite |
| 2026-10-25 r2 | open note: "single screens" in the domain line example | closed | "collapsed to their root screens" |
| 2026-10-25 r3 | work-spec read: no findings | clean read | — |
| 2026-10-25 r3 | UI Map read: no findings; note that architecture's reconciliation kept a justification unconditionally (round 2's spec F4 class) | closed — swept | "only while it still explains why the change is needed"; UI Map family re-read in round 4 |
| 2026-10-25 r3 | spec F1: a product index line covered through Touches rendered without its reason; a justification's source link resolved with the draft's definitions | closed — tool, test | index lines pass their file to `why_for`; justifications render with the authoring artifact's resolver |
| 2026-10-25 r3 | spec F2: the leaked-detail paragraph blamed the requirement from the reason alone | closed | inspect both; fix whichever holds the mechanism |
| 2026-10-25 r3 | note: design-specs-authoring "with no text inline" (r1 F1 class) | closed — swept | "omitting spec text" |
| 2026-10-25 r4 | UI Map read: no findings | converged — stop rule (a) for the UI Map family | — |
| 2026-10-25 r4 | spec F1: the ✅ leaked-detail example described behavior, not a reason (a round-3 trim) | closed | example removed; "a reason says why the requirement changes, not what the app does" |
| 2026-10-25 r4 | spec F2: the page omits Assumptions and TODOs and Out of scope | noise — settled 2026-10-23 (page = card, Discussion, change cards) | reported to the supervisor once |
| 2026-10-25 r5 | spec F1: an added file covered through another entry's Touches rendered its heading without a reason | closed — tool, test | file-heading lookup passes the file |
| 2026-10-25 r6 | spec F1: a new or removed section's orientation text was never diffed; the file could be skipped as unchanged | closed — tool, class fix (every prose comparison × added/modified/removed), tests | `render_spec` section prose; intro removal |
| 2026-10-25 r7 | spec F1: a glossary's intro was never compared (the glossary renderer skipped the shared intro comparison) | closed — tool, test | `render_glossary` calls `intro_entries` |
| 2026-10-25 r8 | spec F1: the renderer chose a reason by name without kind, so a same-named glossary term supplied a section's reason | closed — tool, test | `why_for` filters by kind as the checker does |
| 2026-10-25 r8 | spec F2: a changed prose paragraph and its reason filtered separately on the page | closed — tool, test | one prose card holds text and reason |
| 2026-10-25 r8 | note: a section with orientation text and no items was never visited | closed — tool | sections without items rendered |
| 2026-10-25 r9 | spec F1: rule-level change entries' reasons never rendered | closed — tool, test | each changed rule shows its entry's reason |
| 2026-10-25 r9 | spec F2: a removed table column's cell text dropped from the diff | closed — tool, test | changed rows padded both sides |
| 2026-10-25 r10 | spec F1: a rule's reason shown only with a visual marker (table-only changes and rules in added items lost it) | closed — tool, test | reason looked up whenever an entry names the rule |
| 2026-10-25 r11 | spec F1: retirement examples taught "Superseded by [ID]" | closed — routed to spec-file-shape (its owner) and Stability sharpened in both content guides | successor named in product words, then cited |
| 2026-10-25 r11 | spec F2: a topic-anchor citation in a justification linked nowhere on the page | closed — tool, test | topic headings carry ids; unmatched fragments link to the artifact |
| 2026-10-25 r12 | spec F1: a citation into another document was shortened to a same-named local anchor | closed — tool, test | the anchor shortcut applies only to documents the page represents |
| 2026-10-25 r13 | spec read: no findings; note that the ID and term shortcuts bypassed the document check (round 12 residual) | closed — tool, test | shortcuts respect `on_page` |
| 2026-10-25 r14 | spec F1: the gap tooltip dropped an item's nested bullets (a Tradeoff's alternatives) | closed — tool, test | tooltip renders bullets as the Discussion card does |
| 2026-10-25 r15 | spec F1: popovers resolved citations under the last draft's definitions, losing or misdirecting a source link | closed — tool, test | every popover renders under its own document's definitions |
| 2026-10-25 r16 | spec F1: sources identified by ID or heading alone (shared tooltips, page-local jumps from external hover text, re-pointed citations compared equal) | closed — tool, tests | document-qualified identity, except a spec item's own ID |
| 2026-10-25 r17 | spec read: no findings; residual: a term citation into another glossary showed the local definition on hover | closed — tool, test | local tooltip only for the page's own definition |
| 2026-10-25 r18 | spec F1: deleted text resolved its citations under the draft's definitions and folder | closed — tool, tests | one old-document context for every old-side fragment |
| 2026-10-25 close | Series PL converged: spec family at r13 by stop rule (a), confirmed r17; UI Map at r4; work-spec at r3. Rounds 14–18 reclassified as renderer follow-up work done outside the series; r19 logged on return | converged | supervisor: a zero round stops the series |
| 2026-10-25 r19 (after close) | renderer: a glossary entry moved between files can show as a false change with an incomplete reason (reviewer's probe) | logged — follow-up; the series had closed at r13/r17 | for the renderer-hardening effort, with the rest of rounds 14–18's class |
