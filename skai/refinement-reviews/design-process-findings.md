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
| 2026-10-25 r19 (after close) | renderer: a glossary entry moved between files can show as a false change with an incomplete reason (reviewer's probe) | logged — follow-up; the series had closed at r13/r17 | skai#102 (renderer hardening with a test matrix), with the rest of rounds 14–18's class |
| 2026-10-28 GA r3 | F1 the Design Changes list rule ("columns left to right, frames top to bottom") could order a spilled screen's frames against canvas order | closed | the rule says canvas order (down a column, then across), one entry per frame |
| 2026-10-28 GA r4 | F1 the Discussion gate's "N open gaps carried" is ambiguous before the first drawing | logged | no occurrence; blocked gate covers it; settle the count's meaning before sharpening the gate wording |
| 2026-10-28 GA r5 | F1 with no mockups, entries resting on one placeholder have no canvas order, so the footnote's entry is undefined | logged | no occurrence; blocked gate covers it |
| 2026-11-11 #118 r1 | F1 Completion filed requests itself against rule 8 | closed | "route each the decisions changed as the supervisor picks" |
| 2026-11-11 #118 r1 | F2 `C3` sent mirrors to `change-requests.md` | closed | "mirrors per the tool guide"; spec item 3 corrected |
| 2026-11-11 #118 r1 | F3 readiness 1 "footnote" would block on archived history | closed | "open gap's footnote"; spec item 2 |
| 2026-11-11 #118 r1 | F4 two "its" in `C3` | closed | "the base's" |
| 2026-11-11 #118 r1 | F5 appended entries not placed under their screen | closed | "each under its screen" |
| 2026-11-11 #118 r1 | F6 Completion lost "where raised" | closed | "each open gap, where raised" |
| 2026-11-11 #118 r1 | F7 own gaps footnoted in design change lists per `known-gaps.md` rule 3, against the design spec | closed | "Only inherited gaps get footnotes"; `known-gaps.md` "inherited only in design change lists" |
| 2026-11-11 #118 r1 | F8 a request deciding a base item: no design translation of "holds each base file marking it" | logged | The decision implies redrawing; mirrors follow the tool guide |
| 2026-11-11 #118 r1 | F9 "(each still open)" reads as verify or skip | logged | Standing blocked gate catches a stop; sharpen on recurrence |
| 2026-11-11 #118 r1 | F10 archived request page title dropped the change id | closed | `design-tool.py` `short_title`; test added |
| 2026-11-11 #118 r1 | F11 Base review rejection has no undo for `C3`'s artifact writes | logged | Predates the change; no occurrence |
| 2026-11-11 #118 r2 | F1 `C3` dropped `change-requests.md`'s link step for the request's bare `D<n>` | closed | "Link bare `D<n>` to the request" |
| 2026-11-11 #118 r2 | F2 `C6` moved an owner's path without updating gap mirrors | closed | "and mirror owner paths" |
| 2026-11-11 #118 r2 | F3 Completion's "each open gap" unscoped; "its artifact" unclear | closed | "link the archived artifact … each gap the package leaves open, where raised" |
| 2026-11-11 #118 r2 | F4 nothing asked the supervisor's route before Completion needed it | closed | Review gate note "there, ask each changed input's route"; Completion "as the supervisor picked" |
| 2026-11-11 #118 r2 | F5 footnotes after a fold: a base-owned gap's footnote lands in the base; two footnotes for one shared upstream gap | logged | Needs a spec ruling on what "fold footnotes" does for design; standing blocked gate |
| 2026-11-11 #118 r2 | F6 a re-filed open request keeps its old section name | logged | Section naming is `figma-designer-guide.md`'s; pass 7 |
| 2026-11-11 #118 r2 | F7 `C6` re-rendered only the moved page | closed | "re-render moved pages" |
| 2026-11-11 #118 r2 | F8 Initiation step 3's "Otherwise" reads as excluding a new request | logged | Cosmetic; the operator still creates the artifact |
| 2026-11-11 #118 r3 | F1 `C3` "Link bare `D<n>` to the request" had no scope; could retarget the base's own citations | closed | Moved into the append bullet: "bare `D<n>` linked to the request" |
| 2026-11-11 #118 r3 | F2 `C6` "mirror owner paths" parsed as a verb | closed | "mirrors' owner paths" |
| 2026-11-11 #118 r3 | F3 Completion ", where raised," read as a condition | closed | "and where it was raised" |
| 2026-11-11 #118 r3 | F4 readiness 1 list attached "request" to the gap | closed | "item, request, gap or open gap's footnote" |
| 2026-11-11 #118 r3 | F5 `C6` does not re-render pages it repaired but did not move | logged | Self-heals on next render; widening would drop the base's unconditional re-render |
| 2026-11-11 #118 r3 | F6 Completion has no path when Review advanced without a route | logged | Standard blocked gate covers it |
| 2026-11-11 #118 r4 | F1 `C3`'s provenance suffix had no target on entries with sub-changes | closed | "each Justification or sub-change ending …" |
| 2026-11-11 #118 r4 | F2 Completion's "gap the package leaves open" unscoped | closed | "each gap open in or under the package" |
| 2026-11-11 #118 r4 | F3 a still-open request written before 2026-11-07 folds scope-word citations that change meaning in the base | logged | Convert by hand once; no guide branch for legacy |
| 2026-11-11 #118 r4 | F4 `C6` "keeping targets" reads against "Repair links" | logged | Cosmetic; no bytes |
| 2026-11-11 #118 r4 | F5 readiness 1 "open `- [ ]` item" not scoped to Discussion | logged | Cosmetic; off-normal |
| 2026-11-11 #118 r5 | F1 a request's change to a frame the base lists appended as a second `V` against one entry per frame | closed | Sub-IDs under the base's entry; spec item 3 supersedes 2026-10-23's "next `V`" for that case (supervisor's cap; Offers CR-001 precedent) |
| 2026-11-11 #118 r5 | F2 r1's "open gap's footnote" let a stale footnote in the live package pass | closed | Any footnote in the package blocks; a closed gap's footnote in a promoted request is history |
| 2026-11-11 #118 r2/r5 | Footnotes after a fold: a base-owned gap's footnote, or a duplicate of one the base carries | closed | Dropped at the fold ("not one for a gap the base owns or footnotes") |
| 2026-11-11 #118 r5 | F3 Completion's gap scope (items only or inherited too) | logged | Report only; production readiness re-checks |
| 2026-11-11 #118 r5 | F4 authoring footnote sentence chains four modifiers | logged | Both readings act the same |
| 2026-11-11 #118 r6 | F1 the fold's footnote exception parsed "footnotes" as a noun, losing the duplicate case | closed | "(none whose gap the base owns or already footnotes)" |
| 2026-11-11 #118 r6 | F2 Completion does not say the input change is made in the input's own workflow | logged | `change-requests.md` rule 8 carries "in its workflow"; no proportionate fix fits |
| 2026-11-11 #118 r6 | F3 the Justification line gives no link form at point of use | logged | Purpose routes to `change-requests.md`; restating its forms is settled against |
| 2026-11-11 #118 r6 | Open: a request removing a frame the base added leaves the base's `add` entry dead after a sub-ID fold | logged | Caught at the base's next production readiness (`C2`); authoring's own rule (drop the entry) applies on reopen |
| 2026-11-11 #118 r7 | F1 readiness 1's leading "open" could qualify "footnote", letting a stale footnote in the live package pass | closed | "no footnote or open `- [ ]` item, request or gap" |
| 2026-11-11 #118 r7 | Open: an open request under the package gets "returns to authoring" gate wording; `C5` and a nested request section | logged | Same family as the logged gate wording; section placement is the Figma guide's (pass 7) |
| 2026-11-11 #118 r8 | F1 "(none whose gap …)" read as a description, not a drop instruction | closed | "(drop any whose gap the base owns or already footnotes)" |
| 2026-11-11 #118 r8 | F2 promotion says "mirrors"; the Figma guide never names its gap annotation a mirror | logged | Routed to `figma-designer-guide.md` § Gaps (pass 7) |
| 2026-11-11 | Pass closed | closed | Supervisor approved ending after r8 with F1 applied (stop rule b). Rounds r1–r8: 26 · 16.75 · 18.875 · 10.5 · 9.75 · 8.875 · 1.875 · 4.5. Authoring 15,985 / 16,000; promotion 12,098 / 12,100 |
| 2026-11-11 #108 D r1 | `C6` "for production" and the README's promotion paragraph sent a production-based request part to the change's own destination | closed | `C6` "for a change's own package"; README "a change's own package into production …, or a change request's sub-package into its base, production included (… archived per `change-requests.md`)" |
| 2026-11-11 #108 D r1 | README Completion filed a request or told the supervisor, skipping the supervisor's route choice | closed | "routes each input the decisions changed as the supervisor picked, an edit in that input's own process or a change request, with drafts" |
| 2026-11-11 #108 D r1 | `change-packages.md` said each type owns its change requests and forbade sharing requests at the grouping level, against the request layout | closed | "Do not share evidence at the grouping-directory level; change requests are the exception, below." |
| 2026-11-11 #108 D r1 | `design-promotion.md` 12,200 / 12,160 and the Figma pair 18,152 / 18,140 | closed | Reviewer's trims plus readiness 1 "request part"; 12,158 and 18,131 |
| 2026-11-11 #108 D r2 | README and `change-packages.md` summaries gave a production-based request part the package-base fold and archive path; README prerequisite counted a ruled request as ready | closed | `change-packages.md` points at `change-requests.md` for base, promotion and archive path instead of restating them; README "appended to a base package's Design Changes", prerequisite "the outcome applied for every input its decisions changed, by the route the supervisor picked" |
| 2026-11-11 #108 D r2 | Readiness 1's closed-footnote exemption read as covering the live package (design spec: archived requests only) | closed | "nor, but for closed gaps' footnotes, in the change's promoted `design/` sub-packages" |
| 2026-11-11 #108 D r2 | `C3` tag `; Change request: CR-01 V<n>` reads as a literal ID | closed | `CR-<id> V<n>`; swept to `product-specs-artifacts.md` (`CR-<id> R<n>`) |
| 2026-11-11 #108 D r2 | r1's "change requests are the exception" clause attached to evidence sharing | closed | Clause deleted |
| 2026-11-11 #108 D r3 | README prerequisite (my r2 wording) dropped rule 8's base exception | closed | "every non-base input its decisions changed" |
| 2026-11-11 #108 D r3 | `C6` "any request's base package" (my r1 trim) dropped "if any", so a production-based part re-rendered a base page that does not exist | closed | "a request's base, if a package" |
| 2026-11-11 #108 D r3 | Open question: a wrong-seeming placeholder owned by the base goes to rule 8, which excludes the base | logged | The base's item is decided by the request itself (rule 5.3) or escalated at a blocked gate; no wrong action shown |
| 2026-11-11 #108 D r4 | Initiation reopened a "package or request" with no `design-promotion.md`, so a request with no `design/` part skipped creating one | closed | "reopen a named or contextual `design/` package for this work" |
| 2026-11-11 #108 D r4 | README prerequisite "non-gap items resolved" called stricter than readiness for a package fold | rejected | Authoring's Discussion gate already requires every non-gap item resolved before Mockups, so a completed package has none |
| 2026-11-11 #108 D r5 | Initiation (my r4 wording) could reopen the named base after settling that the work is a request | closed | "settle whether the work is a request; for one, reopen or create its `design/` sub-package. Otherwise reopen …"; step 3 "For a new package, a request's too, …" |
| 2026-11-11 #108 D r5 | Another open request part blocking production was sent back to authoring with the promoting package | closed | "conditions 1–3 but an open request part"; "An open request part, existing destination or pending outcome takes the standard blocked gate"; swept to both spec promotion guides ("another open request part (1)") |
| 2026-11-11 #108 D r6 | Readiness: a wait condition (open request part, pending outcome) beside a failure that returns to authoring had no defined gate | closed | Design: "… alone takes the standard blocked gate naming it; else the failure's gate names it too."; spec promotion guides: "alone, it waits at the standard blocked gate naming it" |
| 2026-11-11 #108 D r6 | Change-ID sentence left "blocking before creation" applying to a supplied ID too (third sighting: DS r1 and DS-b r10 open questions) | closed | "uses the input's change ID; else propose a short kebab-case one and block before creation"; swept to both spec authoring guides ("; else propose") |
| 2026-11-11 #108 D r7 | Two or more wait conditions with no failure had no defined gate ("alone") | closed | All three promotion guides: name them at the failure's gate, or the standard blocked gate if none |
| 2026-11-11 #108 D r7 | Design promotion, design specs set and product specs promotion over cap | closed | Reviewer's exact trims; 12,152 / 12,160; 47,800 / 47,800; 15,619 / 15,620 |
| 2026-11-11 #108 D r8 | Change-ID sentence said "the input's change ID", narrower than a supplied ID (pre-existing wording) | closed | "uses a supplied change ID" |
| 2026-11-11 #108 D r8 | Readiness 1 "open `- [ ]` item" caught any unchecked box in the package, the promotion artifact's own checks included (pre-existing wording) | closed | "open Discussion item or gap", as `change-requests.md` rule 6 |
| 2026-11-11 #108 D r8 | README prerequisite "non-gap items resolved" stricter than a package fold | rejected | As D r4: authoring's Discussion gate requires every non-gap item resolved before Mockups |
| 2026-11-11 #108 D r9 | Readiness recorded only failures in Evidence, not the blockers that wait (my r7 wording) | closed | "Record blockers in `## Evidence`, not checks; block." |
| 2026-11-11 #108 D r10 | README named the change page `<change-id>`; the Figma guide names it for the package with its concept letter (pre-existing) | closed | "drafted on its change page in the project's design file (named per the design tool's conventions guide)" |
| 2026-11-11 #108 D r10 | Open question: design authoring does not check active and promoted paths at creation as the spec guides do | logged | Promotion readiness catches an existing destination; no wrong action shown |
| 2026-11-11 #108 D r11 | Artifact maintenance required updating and rendering the artifact before every gate, including the pre-creation gates (pre-existing) | closed | "Once created, update `design-authoring.md` before speaking." |
| 2026-11-11 #108 D r11 | The promotion hold applied only on the non-request branch of step 2 (my r5 restructure) | closed | "… otherwise reopen a named or contextual `design/` package. Reopen only one with no `design-promotion.md` or returned to authoring; …" |
| 2026-11-11 #108 D r12 | Step 2's non-request branch only reopened, so fresh direct work had no creation action (my r5/r11 restructure) | closed | "otherwise reopen a named or contextual `design/` package or create one. Reopen only without `design-promotion.md` or when returned to authoring; …" |
| 2026-11-11 #108 D r13 | `C3` and resumption rechecked only condition 5, so condition 1 (another open request part, an open gap) could go stale before the production write | closed | "`C3` re-checking 1 and 5"; "with conditions 1 and 5 met" (as the spec promotion guides) |
| 2026-11-11 #108 D r13 | Design authoring 16,007 / 16,000 after r12's fix | closed | Step 2 rewritten whole and tighter: "settle whether work is a request; for one, reopen or create its `design/` sub-package, else reopen … or create one. …" 15,998 |
| 2026-11-11 #108 D r14 | Destination absence (condition 4) not rechecked before the base write | closed | "`C3` re-checking 1, 4 and 5"; "with conditions 1, 4 and 5 met". Supervisor: apply without review |
| 2026-11-11 | #108/#129 pass 4 closed | closed | Supervisor ruling after r14 (stop rule b). Rounds r1–r14: 7.25 · 9.375 · 4.375 · 3.75 · 4.375 · 4.375 · 3.875 · 5 · 1.875 · 2.5 · 3.75 · 2.5 · 3.875 · 1.875 |
| 2026-11-11 #111 D2 r1 | A Base review restore covered only the `Production` page, not the target-size pages or `Components` a production fold changes | closed | Supervisor: smallest fix. Every page a production fold changes is backed up as `<page> — Pre <change-id>`; restore "from backup" |
| 2026-11-11 #111 D2 r1 | Three guides over their caps | still open | Reviewer's trims taken except two (the writing-style pointer sentence is verbatim from process-flow; "Absorb drafts" lost "refactor"); 8 and 7 bytes over remain for round 2 |
| 2026-11-11 #111 D2 r2 | A Base review restore left the base without its gap mirrors (the backup strips them) | closed | "restore the base's drawings from backup, with gap mirrors, and its artifact, pages and links to before `C3`" |
| 2026-11-11 #111 D2 r2 | Promotion and the Figma pair over cap | closed | Reviewer's trims plus Base review and audit wording |
| 2026-11-11 #111 D2 r2 | Open question: a second fold after a Base review return meets the first backup still standing | logged | Supervisor owns deletion; a blocked gate catches it; log until it happens |
| 2026-11-11 #111 D2 r3 | The removal example ("the unread dot goes from every note row") described removing an element from kept screens, which is a modify, not a `remove` entry | closed | "Removed ✅ \"The unread-only notes state goes.\"" |
| 2026-11-11 #111 D2 r3 | The Description rule omits "no lists of element kinds" | rejected | Misread of the spec: the ruling is that the rule itself names no element kinds, not that authors may not name elements; spec item 10 reworded |
| 2026-11-11 #111 D2 r3 | Open question: no execution path when the supervisor accepts a proposed trim or redraw at Base review | logged | A requested design change already returns to authoring; log until it happens |
| 2026-11-11 #111 D2 r4 | "Each entry has" Description and Justification, but the sub-ID example carries change and reason per sub-ID (pre-existing) | closed | "Use these fields, or sub-IDs as below:" |
| 2026-11-11 #111 D2 r4 | The Description rule lacks "what visibly changed" | rejected | The supervisor's one-line rule is "what changed"; the spec's leftover "visibly" clause is removed |
| 2026-11-11 #111 D2 r4 | A Base review restore names no baseline for the artifact, pages and links | logged | They are tracked files; a blocked gate catches a strand; log until it happens |
| 2026-11-11 #111 D2 r5 | `C4` repointed `add` and `modify` links, appended entries' too, though `C3` keeps undrawn entries unlinked (pre-existing) | closed | "repoint existing `add` and `modify` links, appended too" |
| 2026-11-11 #111 D2 r6 | `C3` copied drafts in before the audit and said "update changed screens to match drafts", blurring the base being audited with the drafts | closed | Audit first, then back up and copy; "Apply draft changes to existing screens" |
| 2026-11-11 #111 D2 r6 | Tool: a backup Section checked on its own always failed placement | closed | `figma-page-check.js` checks backup placement only on a page target; test added |
| 2026-11-11 #111 D2 r7 | With the audit moved before the fold (r6), it recorded the plan, not what was applied | closed | "a working document names every base frame, its rules and its change or none, updated as applied"; "A removal or redraw beyond the package's changes is only proposed, at Base review." |
| 2026-11-11 #111 D2 r8 | No finding; open question: the page check accepts a backup under any Section, the guide says under the request (manual inspection covers it) | logged | — |
| 2026-11-11 | #111/#106/#100 pass closed | closed | Clean round r8 (stop rule a). Rounds r1–r8: 3.875 · 3.875 · 2.5 · 6.875 · 1.875 · 6.25 · 2.5 · 0 |
