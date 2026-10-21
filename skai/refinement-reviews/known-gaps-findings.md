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
| 2026-10-20 r2→r3 | Supervisor ruling on the no-placeholder form | closed | Gap field description now allows `"none; waiting on <what>"`; mirrored in the template and the amendment; round 3 commissioned over the final text |
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
