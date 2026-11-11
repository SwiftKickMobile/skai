# Known Gaps — Findings Log

Target: `Guides/Core/known-gaps.md` and `Guides/Core/process-flow.md` § Structured discussion items. Design specs: `known-gaps-design.md`; `product-specs-system-design.md` § Decisions — 2026-10-20.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-20 r1 | F1 pointer sentence's `known-gaps.md` link dangles when copied outside Core | closed | destination now `../Core/known-gaps.md`; resolves from every Guides subdirectory |
| 2026-10-20 r1 | F2 gap resolution recipe left the Gap line beside Decision on a checked item | closed | process-flow Resolution step 2 removes the Gap line; guide rule 4 names the artifact's marker |
| 2026-10-20 r1 | F3 gate subsection's closing summary omits the gap-only planned-gate case | logged | operative rule two lines above is explicit; the summary is pre-existing prose; qualify only if misuse is observed |
| 2026-10-20 r1 | Open question: how an item records a gap with no placeholder | open | raised to the supervisor |
| 2026-10-20 r2 | F1 Gap field describes only a placeholder; no stated form for a gap without one (restates r1 open question) | logged | escalation route exists; sharpen the field description only on the supervisor's ruling |
| 2026-10-20 r2 | Open question: a revised placeholder with state unchanged gets no log entry | logged | consistent with the decision that the log records state changes only |
| 2026-10-20 r2 | Terminal round: no new live findings | converged | stop rule (a), clean round over the current text |
| 2026-10-20 r2→r3 | Supervisor ruling on the no-placeholder form | closed | Gap field description now allows `"no placeholder; waiting on <what>"`; mirrored in the template and the amendment; round 3 commissioned over the final text |
| 2026-10-20 r3 | Clean round over the final text | converged | no findings; stop rule (a) |
| 2026-10-20 post-r3 (supervisor) | Schema does not say what a changed decision is (new `decided` line, Decision line replaced) nor that `reopened` is only for a withdrawn decision with no replacement | accept | spec hole: the amendment listed states, not transitions; fix folded into slice 2 (process-flow Resolution rule, template, every inlined copy) |
| 2026-10-20 slice 2 r1 | F1 reopening paragraphs froze decisions; implementation's return path mandated a new D# | closed | preservation now means stable IDs and untouched originals, state per Resolution; the return path reopens or adds |
| 2026-10-20 slice 2 r1 | F2 planned-gate inventories and UI Map implementation's after-drafting line counted carried gaps | closed | non-gap in all four places |
| 2026-10-20 slice 2 r1 | F3 promotion guides (readiness failure, blocked gate) and known-gaps rule 6 (planned gate, "next") disagree on how a gap-bearing package returns to authoring; the standards disagree too | supervisor decision | pending ruling |
| 2026-10-20 slice 2 r1 | Open: a UI Map gap holds a composed work spec at the sibling's promotion boundary | logged | consequence of per-type promotion; skai#91 |
| 2026-10-20 slice 2 r1 | F3 ruled (G10): blocked gate; rule 6 and design spec requirement 3 now say readiness failure, package returns to authoring | closed | one sentence in known-gaps.md; promotion guides unchanged |
| 2026-10-20 slice 2 r2 | F1 three operational stops (concept inventory, requirements-gap gate note, mockup feedback branch) still blocked on gap items | closed | non-gap / placeholder-carried wording; "(blocked)" dropped |
| 2026-10-20 slice 2 r2 | F2 design specs promotion's canonical-contract prerequisite preceded the gap readiness check | closed | moved after the readiness list |
| 2026-10-20 slice 2 r2 | F3 artifact reference implied a placeholder-vs-draft tool check | closed | comparison and page outputs named |
| 2026-10-20 slice 2 r2 | F4 work spec creation's mandatory-heading list omitted Decision Log | closed | added |
| 2026-10-20 slice 2 r3 | F1 drafting instructions assumed a proposal always exists (product specs, design specs, work spec creation; "fill gaps" wording; approve-all) | closed | draft under the reading or the placeholder; a bare gap leaves the behavior out; non-gap for approve-all |
| 2026-10-20 slice 2 r3 | F2 UI Map's remove-unresolved-item rule and design authoring's feedback wording bypassed the lifecycle | closed | non-gap removal, gap omitted first; feedback changing a decision goes through Resolution |
| 2026-10-20 slice 2 r3 | F3 UI Map justification source has no label for an agent-proposed placeholder under an open gap | logged | sharpen `Agent proposal` if it recurs |
| 2026-10-20 slice 2 r4 | F1 design specs made a placeholder the condition for carrying a requirements-gap item (an r2 repair) | closed | "unless it carries a Gap line"; drafting per the Drafting rule |
| 2026-10-20 slice 2 r4 | F2 work spec re-entry's "reopen or add a D#" (a G06 repair) mishandled a replaced decision | closed | re-entry uses the Discussion-items transitions; new D# only for a new decision |
| 2026-10-20 slice 2 r5 | F1 UI Map architecture's Reopen bullet forbade the empty Discussion state, contradicting lean retention | closed | bullet retains items that still explain the map or that a map change cites |
| 2026-10-20 slice 2 r6 | F1 artifact skeletons routed "gaps needing no decision" / "unresolved design gaps" into Assumptions and TODOs | closed | "notes"; sweep of the word "gap" in pre-existing text repaired four more; "requirements gap" kept deliberately |
| 2026-10-20 slice 2 r7 | F1 a UI Map gap stops work spec planning through the sibling invocation's "after it completes" | supervisor decision | G11: recommended to leave to slice 7 (G05 removes the invocation); ruling pending |
| 2026-10-20 slice 2 r7 | G11 ruled: the sibling-invocation dependency is slice 7's (G05 removes the invocation) | converged by ruling | stop rule (b); slice 2's unimplemented ledger is this one item |
| 2026-10-20 slice 3 r1 | F1 parser swallowed a gap definition in intro/section prose and allowed a rule after a footnote, against the validator's stated rejections | closed | parser fixed; probes and fixture verify |
| 2026-10-20 slice 3 r1 | F2 drafting sentence could attach the footnote to any open item | closed (sharpened) | "or, for a gap, its placeholder footnoted …" |
| 2026-10-20 slice 3 r1 | F3 `validate` and `check-changes` rows lack a companion link | logged | item-order and render-row links route the reader; revisit if an operator misses them |
| 2026-10-20 slice 3 r2 | F1 "(none: leave it out)" read as omitting the gap's representation when no placeholder exists | closed | footnote applies regardless; the dependent text is what is left out |
| 2026-10-20 slice 3 r2 | F2 Gaps list linked a retired item's non-retired anchor | closed | list uses the item's real anchor; probed |
| 2026-10-20 slice 3 r3 | Old-side superscripts under `--base` link into the current item's footnote namespace (relabeled footnote leaves a dead historical link) | logged | renderer maintenance; current markers, Gap lines and the Gaps list are correct |
| 2026-10-20 slice 3 r3 | Clean round over the final text | converged | stop rule (a) |
| 2026-10-21 Offers test | Gap-state Discussion cards rendered at 13px with a dashed top border: the slice 3 footnote block's class `gap` collided with the slice 2 card state class | closed | footnote block renamed `gapnote`; test passes; release entry; a renderer change sweeps class names across the stylesheet (skai#90 note) |
| 2026-10-26 RG r1 | the authority test for a gap admitted ordinary supervisor decisions (rule 1 vs the workflow guides' blocked gate) | closed | rule 1 reconciled: nobody in the work can decide yet; a decision the supervisor can make now is a Discussion item |
| 2026-10-26 RG r1 | a gap with no placeholder and no legitimate host item has nowhere to put its marker-less note | logged — the unexpected-blocker route covers it; no observed strand | known-gaps 5, spec-file-gaps |
| 2026-10-26 RG r2 | the gap example showed an outstanding product decision, not an unavailable answer; design authoring's "Gap to carry it" and process-flow's example reinforced it | closed | example reworded; shortcut deleted; process-flow example routed and corrected |
| 2026-10-26 RG r2 | the authoring guides' drafting clauses footnoted ordinary recommendations, which check-changes rejects | closed | footnotes only for a gap's placeholder or omitted text (product and design specs authoring) |
| 2026-10-26 RG r5 | the page's owner chip drops a scoped upstream owner to a bare D# when its artifact does not resolve | logged — renderer, skai#102 class | gap_owner_chip fallback |
| 2026-10-26 RG r5 | process-flow's gap example waited on an outside answer without saying why it constrained the choice | closed (routed) | example's Concern and Proposal reworded |
| 2026-10-26 RG | Series RG converged: clean round over the binding target at r5 | converged | stop rule (a) |
| 2026-10-26 GL r1 | the Gap line's no-placeholder deletion left the boundary unstated: rule 8 forbade only a field; the Gap definition and process-flow's example still admitted an awaited-answer clause | closed | rule 8 "no line names who is to answer; Concern states what is not yet known"; Gap line "the placeholder alone, or no placeholder" in the owner, the maintainer reference and the six copies; example's Gap line `PDF.` |
| 2026-10-26 GL r2 | process-flow's example Concern named the print partner as the one to answer | closed | Concern states the unknown as a fact: "until the print partner's format is known" |
| 2026-10-26 GL r2 | work-spec-creation's Question rule offered a Gap line as the alternative to a Proposal | closed | "when there is one"; the pointer sentence decides what is a gap |
| 2026-10-26 GL r2 | process-flow's Question kind ("no basis to recommend") against "every item carries a recommendation" | logged | pre-existing taxonomy tension, outside this amendment; for process-flow's next pass (skai#89) |
| 2026-10-26 GL r3 | process-flow's gate recap said the planned gate comes "when the draft produced zero items", contradicting the non-gap rule for a gap-only draft | closed | parenthetical deleted |
| 2026-10-26 GL r3 | the Decision line's boundary ("the outcome, in words") is less explicit than the Gap line's "placeholder alone" | logged | no recurrence under the amended text; outside the series' scope (Gap line and rule 8); sharpen to "the outcome alone" on the supervisor's say |
| 2026-10-26 GL r4 | the standard's decision 3 said `render` shows the Decision Log, which left the page 2026-10-21 | closed (standard) | decision 3 records the 2026-10-21 change |
| 2026-10-26 GL r4 | the six inlined Decision Log sentences omit the owner's "no dates" | logged | pre-existing propagation drift, outside the series' scope; one clause in the six copies on the supervisor's say |
| 2026-10-26 GL | Series GL converged: clean round over the binding target at r4 | converged | stop rule (a) |
| 2026-11-07 r1 | F1 rule 6 "there" and "the base's author" unanchored; restates change-requests' who and where | closed | "a promoted request's as change-requests.md says" |
| 2026-11-07 r1 | F2 rule 6 dropped the spec's "or renumbers" | closed | "never moves, renumbers or resolves a gap" |
| 2026-11-07 r1 | F3 rule 6 said promotion resolves a gap by folding a ruling | closed | "a fold only records a ruling the request already holds" |
| 2026-11-07 r1 | F4 rule 7 names an input catch-up rule no guide contains | closed | "your workflow's input-change and Discussion rules"; spec requirement 6 corrected |
| 2026-11-07 r1 | F5 where a promoted request's gap is edited | rejected | Rules 5 and 7 cover the base's inherited marker |
| 2026-11-07 r1 | F6 rule 3 "mark them" read as inherited only | logged | Tool stops with a clear message |
| 2026-11-07 r2 | F1 rule 7 points at input-change rules most workflows lack (round-1 repair) | closed | "Use your workflow's Discussion rules"; a differing answer is a Discussion item |
| 2026-11-07 r2 | F2 rules 2, 5, 8 hard-code "file a change request" | routed | #129: the supervisor picks the route |
| 2026-11-07 r2 | F3 rule 3 names artifacts, not the guide owning the marker form | closed | Footnotes per `spec-file-gaps.md`; UI Map and Figma mirrors per their guides |
| 2026-11-07 r2 | F4 no ❌ for a question the supervisor can rule now | closed | Supervisor, 2026-11-07: the agent raises Discussion items; only the supervisor declares one a gap, when they cannot answer it. Rule 1 and process-flow's **Gap** label now say so; design specs amended |
| 2026-11-07 r2 | F5 rule 6 hands off how as well as who and where | logged | Cosmetic; change-requests' "as that request's own" routes back to rule 4 |
| 2026-11-07 r2 | F6 mark/marks/marker mixed; rule 7 restates rule 5's clearing | closed | "marker" throughout; rule 7's clause removed |
| 2026-11-07 r3 | F1 rule 7 has no trigger; "nothing changes" on adoption reads as contradicting rule 5's marker clearing; spec correction still said "input-change" | closed | Lead "When an upstream gap closes"; "Adopted as written: only the marker clears"; spec correction aligned to round 2 F1 (Discussion rules only) |
| 2026-11-07 r3 | F2 rule 3's lead "Keep gaps open" reads as forbidding resolution before completion | closed | "Open gaps never block authoring's completion" (spec requirement 3) |
| 2026-11-07 r3 | F3 rule 2 has the agent record a placeholder; the supervisor's ruling sets it | closed | "propose one whenever you can" |
| 2026-11-07 r3 | Trims for the above | applied | Rule 4 "the Decision Log"; rule 6 colon list. Rule 8 trim declined: "The supervisor starts promotion" drops the imperative |
| 2026-11-07 r4 | F1 rule 7's "Omitted upstream: remove the dependent part" is not in the spec and skips the Discussion bar | closed | Omission joins the differing-answer case: a Discussion item; spec requirement 6 notes it |
| 2026-11-07 r4 | F2 rule 4 makes the agent the one who resolves a gap | closed | "The supervisor closes your own gaps one of three ways" |
| 2026-11-07 r4 | F3 rule 3's lead does not head its body | closed | Lead joined to the formats sentence |
| 2026-11-07 r4 | F4 "decide and record it for review" names no record | logged | Spec does not name it either; workflow guides own the record |
| 2026-11-07 r4 | F5 own gap with no placeholder: rule 2 does not say nothing proceeds | closed (2026-11-09) | Stranded, not broken; spec-file-gaps and the authoring guides cover it |
| 2026-11-07 r4 | F6 nothing detects that an inherited marker's owner closed | logged | Stranded, not broken; blocked gate escalates; tooling territory |
| 2026-11-07 r5 | F1 rule 3's lead puts inherited gaps under Discussion and Decision Log formats (round-4 repair) | closed | Rule 3 keeps own gaps and the marker forms; inherited clause moved to rule 5's lead |
| 2026-11-07 r5 | F2 rule 7 leaves the marker unstated for a differing answer; "its omission" has no fixed referent | closed | Lead "clear the marker and use your workflow's Discussion rules"; "the dependent part omitted upstream" |
| 2026-11-07 r5 | F3 rule 5's lead is a label | closed | "Inherit upstream gaps as markers, not items, on what stands on the placeholder" |
| 2026-11-07 r5 | F4 "Out of scope" names a section dev specs and UI Map implementation lack | logged | Spec requirement 4 names it; stranded, not broken |
| 2026-11-07 r5 | F5 item state after "request a placeholder upstream" unstated | logged | The supervisor's ruling says it |
| 2026-11-07 r6 | F1 rule 6 drops the spec's "one of rule 4's three ways" for a promoted request's gap | closed | "a promoted request's by (4), where `change-requests.md` says" |
| 2026-11-07 r6 | F2 rules 5 and 7 both state marker clearing (round-5 repair) | closed | Rule 5 "proceed without a decision until the owning item closes (7)"; rule 7 owns clearing |
| 2026-11-07 r6 | F3 managed header date stale | closed | 2026-11-07 |
| 2026-11-07 r6 | F4 rule 3's lead does not announce the representation list | logged | Cosmetic; guide read whole |
| 2026-11-07 r6 | F5 "fold" unglossed | logged | Cosmetic; the link beside it defines it |
| 2026-11-07 r6 | Open question: which of the three ways a request's base-gap decision records | routed | `change-requests.md` / process-flow; design-guides pass |
| 2026-11-07 r7 | F1 rule 7 names no act on the drafts; its tail "a Discussion item" overrides the Discussion bar (round-2 repair) | closed | "clear the marker, build on the outcome and use your workflow's Discussion rules"; tail removed (spec requirement 6: normal Discussion bar) |
| 2026-11-07 r7 | F2 rule 6's promoted-request clause verb-less; pointer floats | closed | "a promoted request's too, where `change-requests.md` says; inherited markers…" |
| 2026-11-07 r7 | F3 a bare "gap" ruling: does the item's proposed placeholder stand? | closed | Supervisor, 2026-11-09: no; the supervisor supplies placeholders. Rule 2 "the supervisor's to supply" (my round-3 "propose one" was wrong) |
| 2026-11-07 r7 | F4 rule 1 dropped the spec's "yet" | logged | Cosmetic; the sentence's earlier "yet" carries it |
| 2026-11-09 r8 | F1 rule 7 "build on the outcome and use" sequences redraft before the Discussion bar (round-7 repair) | closed | "under your workflow's Discussion rules" (spec requirement 6's word) |
| 2026-11-09 r8 | F2 rule 6 "where change-requests.md says" reads two ways | closed | "as" |
| 2026-11-09 r8 | F3 rule 6 "owners" reads as people | closed | "owning items" |
| 2026-11-09 r8 | F4 "the marker" singular where a gap has several marks (footnote and Figma mirror) | closed | "markers" in rules 4 and 7 |
| 2026-11-09 r8 | F5 rule 4's record list omits removing the Gap line | logged | process-flow and every authoring guide state it; spec enumerates the same list |
| 2026-11-09 | Supervisor ruling: rule 5's "request a placeholder upstream" route | closed | Removed; a bare upstream gap is intentional; the agent omits the dependent part, or waits at a blocked gate if its absence blocks progress; spec amended |
| 2026-11-09 r9 | F1 rule 3 "never block" contradicts rule 5's wait (2026-11-09 ruling's application) | closed | "except as rule 5 says"; spec requirement 3 noted |
| 2026-11-09 r9 | F2 bare upstream gap: is the omitted part marked? | closed | Unmarked: a marker blocks production, which the omission avoids; follows from the ruling |
| 2026-11-09 r9 | F3 rule 4 "the artifact's markers" unbound | closed | "remove its markers" |
| 2026-11-09 r9 | F4 rule 7 clears markers before building on the outcome | closed | Reordered |
| 2026-11-09 r9 | F5 managed header date | closed | 2026-11-09 |
| 2026-11-09 r9 | O1–O4 (request into base with open gaps implied; rule 2 / rule 5 no-placeholder overlap; blocked gate as a push; rule 6 density) | logged | Stranded or cosmetic |
| 2026-11-09 r10 | F1 rule 7's tail dropped the spec's "is a change" | closed | "is a change that may undercut an approved decision" (spec requirement 6 wording; reviewer's "revisit decisions" not taken: it reads as the agent re-deciding) |
| 2026-11-09 r10 | F2 rule 5 omits before judging; "(Out of scope)" reads as a label | closed | Reviewer's text: judge first, wait or omit, "recorded under Out of scope" |
| 2026-11-09 r10 | F3 the Out of scope record need not name the owning item | logged | Adds a required field; not occurred |
| 2026-11-09 | Supervisor: restore content cut to meet caps | applied | Rule 1 "blocking", rule 4 "artifact's", rule 8 "No owner field;"; size met by reviewer tightening |
| 2026-11-09 | Compression review (Fable) after the restore | applied | 3,405 -> 3,350; seven wording changes in rules 2, 4, 6, 8, each checked against the spec; two rejected (rule 3 "logged", rule 4 "one of") and replaced by the reviewer |
| 2026-11-09 r11 | F1 rule 6: "inherited markers wait" reads as the package waiting in promotion | closed | Reviewer's text: returns to authoring for all three kinds; trim rule 5 "proceed, no decision, until" (spec wording) |
| 2026-11-09 r11 | F2 rule 5's wait for a bare upstream gap leaves no record in the package | closed, no change | Supervisor, 2026-11-09: the block determination is not documented |
| 2026-11-09 r12 | F1 rule 3 "Mark own and inherited gaps" contradicts rule 5's unmarked omission | closed | "Mark own gaps and inherited placeholders"; reviewer's trim in rule 6 "records the request's ruling" (spec amendment item 4 kept) |
| 2026-11-09 r12 | F2 rule 7 "dependent part omitted upstream" flips the term's owner | closed | "the gap closed upstream as omitted" |
| 2026-11-09 r12 | F3 rule 5 "missing part … omit it" referents | logged | Cosmetic; the reviewer's "cannot proceed" would change "blocks progress", which is the supervisor's test |
| 2026-11-09 r13 | F1 rule 6's fold clause omits the check-off the spec requires (amendment item 4) | closed | "a fold's check-off records the request's ruling"; reviewer's trim rule 4 "not the artifact's concern" (spec wording); its rule-7 trim declined ("the gap omitted upstream" loosens round 12's fix) |
| 2026-11-09 r13 | F2 rule 2's "file a change request upstream" could be stretched to a bare upstream gap | logged | Rule 5's if/else closes it; wording tracked under the separate route issue |
| 2026-11-09 r13 | F3 promotion gate templates do not require listing gaps | logged | Promotion guides' boundary |
| 2026-11-09 r14 | F1 rule 6 "a fold's check-off" names no object; reads as checking off the request's own gaps (round-13 repair) | closed | Reviewer's text "a fold checks off base items already ruled in the request"; trim rule 7 "or an upstream omission" (spec wording); its rule-4 trim declined (restored word) |
| 2026-11-09 r14 | F2 "markers … in promoted requests too" sends a literal reader to archived drafts | logged | Tool and promotion guides resolve it; spec line could be tightened at its next amendment |
| 2026-11-09 r15 | F1 rule 7: the differing-answer sentence names the hazard, not the act; the Discussion-rules clause sits in the lead | logged | Reviewer's fix would re-open round 8's build-before-ruling order; supervisor approved ending the pass with it logged (2026-11-09) |
| 2026-11-09 | Pass closed | closed | Stop rule (b): supervisor approved the logged ledger after round 15 (1.875). Size 3,346 / 3,350 |
| 2026-11-09 | Supervisor: drop "recorded under Out of scope" from rule 5's bare-upstream case | closed | No placeholder means no upstream rule; nothing to call out. Spec amendment added; own-gap Omitted closure unchanged |
| 2026-11-11 | Drive-by from design pass 6 r1: rule 3 said design change lists footnote own gaps; design guides keep own gaps as items | closed | "inherited only in design change lists" (3,332 / 3,350) |
