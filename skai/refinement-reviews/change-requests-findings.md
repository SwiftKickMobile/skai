# Change Requests Guide Findings

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-11-07 r1 | F1–F4 rules 5–6 too compressed to act on at the fold (folded citations, folded footnotes, moved open requests, `(<nnn>)` placement) | closed | Rules 5–6 rewritten: folding links the request's own `D<n>` in drafts and change items to the archive; moved open requests become the base's; deciding another package's item; `(<nnn>)` on the base-side records |
| 2026-11-07 r1 | F5 "base's contents" reads as copy the base's drafts | closed | Rule 2 "base's layout"; spec requirement 2 sharpened |
| 2026-11-07 r1 | F7 "its page" ambiguous | closed | "the base's page" |
| 2026-11-07 r1 | F6 rule 7's lead is inheritance; "resolved in place" dangles | logged | Cosmetic; the type guides' readiness screens carry the enforced production rule |
| 2026-11-07 r2 | F1–F5 fold steps split between rules 5 and 6; link target and label definition unstated; Gap line on check-off; request must hold the base files it drafts markers out of; moved requests' links | closed | Fold steps moved into rule 5 (relink own citations, check off decided items with no Gap line, move open requests with links repointed); rule 6 names the authoring artifact as link target and the label defined once; rule 2 "only files they change" |
| 2026-11-07 r2 | F3 next free number ambiguous across open and promoted | closed | Rule 2 "numbered across open and promoted"; spec requirement 2 |
| 2026-11-07 r2 | F6 design-tool top bar drops the request chain on archived requests | logged | Tool defect, not the guide; `design-tool.py` `short_title`; fix with #108's path work |
| 2026-11-07 r2 | F7 example label `[base D12]` sits one step from the retired `base D12` shorthand | closed | Supervisor, 2026-11-07: labels name the cited package; the example is `[reminder-expiry D12]` (LumenNotes) |
| 2026-11-07 r3 | F1 a decided base item keeps its markers after the fold (design type) | closed (this guide) | Rule 5 "no Gap line or marker"; design-promotion `C3` routed to the design guides' pass |
| 2026-11-07 r3 | F2 "holds each base file marking it" when the decided item is an ancestor's | logged | Off-normal, no occurrence; rule 9 routes non-base changes to their own requests |
| 2026-11-07 r3 | F3 rule 5 links to "the archive" before naming it | closed | Archive path stated before the relink step |
| 2026-11-07 r3 | F4 who resolves a promoted request's open item | closed | Rule 7 "resolved there by the base's author" |
| 2026-11-07 r3 | F5 moved request's first input; numbering of `<nnn>-<their nnn>` | closed / logged | "links and first input repointed"; numbering already answered by rule 2 |
| 2026-11-07 r3 | F6 tools accept the retired scope-word citations in open packages | closed | Supervisor, 2026-11-07: no; tools do not reject them |
| 2026-11-07 r3 | F7 `<decision> (<nnn>)` names no field | closed | "Decision `<decision> (<nnn>)`" |
| 2026-11-07 r4 | F1 rule 5 "link its `D27` ... there": "its" switches from base to request | closed | "its own `D27` in the base's drafts and change items become links into it" |
| 2026-11-07 r4 | F2 rule 3 reopen test lost "for the same work" (round-3 trim) | closed | "Reopen a request for the same work if named or in context" |
| 2026-11-07 r4 | F3 rule 7 "resolved there" does not say the markers sit in the base's drafts | closed | "its markers in the base's drafts" |
| 2026-11-07 r4 | F4 rule 6 states no label rule; two example shapes | logged | Cosmetic; examples carry it |
| 2026-11-07 r4 | F5 `check_base_decisions` checks markers only for the direct base's items | logged | Tool gap, not the guide; `spec-tool.py` |
| 2026-11-07 r5 | F1 rule 5 links to the archive path before the move; C7 validate fails them | closed | Links point to the request; archiving is rule 5's last step, with the path |
| 2026-11-07 r5 | F2 rule 7 markers clause has no verb (round-4 repair) | closed | "clearing its markers from the base drafts" |
| 2026-11-07 r5 | F3 rule 3 dropped "for it" from the base-defect sentence | closed | "with no open package for it" |
| 2026-11-07 r5 | F4 `design-tool` top bar loses the chain for archived requests | logged | Same as r2 F6; tool |
| 2026-11-07 r6 | F1 rule 5 re-renders the base before archiving; base page links go stale | closed | Archive, then re-render; spec requirement 5 amended; type guides' re-render after archive routed to their passes |
| 2026-11-07 r6 | F2 rule 3 base-defect sentence has no branch for an existing package; type guides state it unconditionally | closed (this guide) | "goes to an open package for it or starts one against the base"; spec requirement 3 amended; type guides routed |
| 2026-11-07 r6 | F3 "first input repointed" names no target | closed | "first input the base" |
| 2026-11-07 r6 | F4 "the base's drafts" read as the base's own drafts, not the folded ones | closed | "in folded drafts and change items" |
| 2026-11-07 r6 | F5 `design-tool` top bar for archived requests | logged | Same as r2 F6; tool |
| 2026-11-07 r6 | F6 reopen rule does not exclude promoted requests | closed | "Reopen an open request"; spec requirement 3 amended |
| 2026-11-07 r6 | F7 "A move changes only link paths" has no stated subject | logged | Cosmetic; no bytes |
| 2026-11-07 r7 | F1 deciding a base item says strip the marker, not draft the decision | closed | "drafted to the decision, minus the marker"; spec amendment item 4 to match |
| 2026-11-07 r7 | F2 check-off log line has no location | closed | "log there" |
| 2026-11-07 r7 | F3 folded change items' links to base items break; fold is not a move | closed | "A move or fold changes only link paths" |
| 2026-11-07 r7 | F4 spec's "a promoted request is never reopened" carried only by "open" | logged | Cosmetic |
| 2026-11-07 r7 | F5 base resolves an item a live request decided; request's check fails with no route | logged | Stranded, not broken; blocked gate escalates |
| 2026-11-07 r8 | F1 rule 6 "a move or fold changes only link paths" contradicts rule 5's fold (round-7 repair) | closed | "Moves and folds keep links; paths follow." |
| 2026-11-07 r8 | F2 base's own bare item references in files a request holds read as the request's items | closed | "even in held base files" |
| 2026-11-07 r8 | F3 deciding a non-base package's item overlaps rule 9 | closed | Supervisor, 2026-11-07: the supervisor picks the route for any input but the base (edit directly or request); rule 6 decides only base items; rule 9 asks |
| 2026-11-07 r9 | F1 rule 1 lets a promoted request read as a base | closed | "an open package of its type or request" |
| 2026-11-07 r9 | F2 `<id>` in the provenance tag unglossed | logged | Type guides give the concrete form |
| 2026-11-07 r9 | F3 managed header date stale | closed | Bumped to 2026-11-07 |
| 2026-11-07 r9 | F4 `design-tool` top bar title-cases the change id | logged | Tool |
| 2026-11-07 r9 | F5 `check-changes` passes a linked footnote whose target item is checked | logged | Tool; mirror the own-item check |
| 2026-11-07 r10 | F1 rule 6 names the link for held base files but not the act (round-8 repair) | closed | "in a held base file, a bare `D<n>` of the base becomes a link" |
| 2026-11-07 r10 | F2 how a request decides a base item (own Discussion item or log line only) | closed, no change | Supervisor, 2026-11-07: every Discussion item waits on the supervisor's ruling (process-flow); the request records that ruling; no duplicate item |
| 2026-11-07 r10 | F3 rule 7 names where a promoted request's open item is resolved, not how | closed | "resolves an item left open in a promoted request there, as that request's own" |
| 2026-11-07 r10 | F4 rule 1 "or request" outside its qualifiers (round-9 repair) | closed | "an open package or request of its type" |
| 2026-11-07 r11 | F1 whether a moved `<nnn>-<their nnn>` request uses up a number | rejected | Supervisor, 2026-11-07: a moved request keeps its own name; nothing collides |
| 2026-11-07 r11 | F2 retired `base D4` form not shown as ❌ | logged | Does not teach a wrong action; supervisor approved leaving it logged to end the pass (2026-11-07) |
| 2026-11-07 r11 | F3 "promoted requests' too" depth for nested promoted requests | rejected | Supervisor, 2026-11-07: the rule is recursive |
| 2026-11-09 | Supervisor: restore content cut to meet caps; compression review (Fable) | applied | Restored "Read for any base or request.", the LumenNotes example's contents, "in filing order", "Any package may hold…", "under the same rules" (3,516); reviewer's wording changes in rules 5, 6, 7 (3,442); five removals rejected (requirement 2 sentence, "against the base", "first input the base", "keep links", "as that request's own"); no further tightening without loss; cap raise to the supervisor |
| 2026-11-09 r12 | F1 rule 3 "an open package for it" read as for the base | rejected | Spec requirement 3: a package for the defect; "for it" restored in r5 F3; the fix would send a defect to any open package |
| 2026-11-09 r12 | F2 rule 5 "link the request's `D<n>` to it" | closed | "folded drafts' and change items' `D<n>` link to the request" |
| 2026-11-09 r12 | F3 rule 2 "Production:" reads as where production lives | closed | "Against production:" |
| 2026-11-09 r12 | F4 rule 9 "your review gate" absent from the spec workflows | routed | Spec authoring guides' passes state where rule 9's question is asked |
| 2026-11-09 | Cap | closed | Supervisor: 3,450 |
| 2026-11-09 r13 | F1 rule 5 relinks every `D<n>`, not the request's own (round-12 repair dropped the qualifier) | closed | "bare `D<n>`"; reviewer's trim rule 6 "repairing paths" |
| 2026-11-09 r13 | F2 rule 7 does not say the answer is drafted in the base | logged | Rare; the chain through known-gaps gives it |
| 2026-11-09 r13 | F3 rule 9 "by" and "missing" soften the spec's words | closed | "Ask before your review gate advances"; "unruled ones block" |
| 2026-11-09 r13 | F4 rule 2's lead does not cover the production path | logged | Cosmetic; the reading lands right |
| 2026-11-09 r14 | F1 rule 9 "unruled ones" refers to outcomes (round-13 repair) | closed | "pending ones block" (0 bytes) |
| 2026-11-09 r14 | F2 rule 5 "items the request decided" broader than base items | closed | "the base items it decided" (0 bytes); a request decides only its base's items |
| 2026-11-09 r14 | F3 "held" not introduced before rule 6 | logged | Rule 2's "hold" and rule 6's "holds" anchor it; no spec-safe trim for a sharpening |
| 2026-11-09 r15 | F1 rule 6 "held base file" misnames the owner for nested requests; reviewer's fix (drop "base") would turn the request's own bare `D<n>` into links | changed | "a held file's bare base `D<n>` become links": restores the spec's "of the base" qualifier lost in compression (0 bytes); nested owners logged |
| 2026-11-09 r15 | F2 rule 5 "the base items it decided" misses a moved request's earlier decisions (round-14 repair) | closed | "the items it decided where they live"; rule 6 still limits decisions to base items |
| 2026-11-09 r15 | F3 rule 9 "every outcome" wider than the type guides' "every request" | logged | Narrowing would hide a pending direct edit |
| 2026-11-09 r15 | F4 linked `reopened` on another package's item has no fold instruction | logged | Spec silent; route to process-flow pass |
| 2026-11-09 r15 | Open: a moved request's earlier decisions on its former base | logged | Spec amendment 5 silent; rule 5's wording now covers the check-off |
| 2026-11-09 r16 | F1 rule 6 held-file clause reads as automatic (round-15 repair) | closed | Folded into the imperative: "Cite … by link, the base's too, a held file's bare base `D<n>` included" |
| 2026-11-09 r16 | F2 rule 5 link step is descriptive | closed | "link folded drafts' and change items' bare `D<n>` to the request" |
| 2026-11-09 r16 | F3 rule 5 "the items it decided" precedes rule 6's definition | changed | "(6)" pointer added; reviewer's "base items" not taken (round 15 F2: a moved request's earlier decisions) |
| 2026-11-09 r16 | F4 provenance tag on a re-fold | logged | Off-normal; spec silent |
| 2026-11-09 r16 | F5 "minus the marker" vs footnote definition | logged | Core-wide vocabulary; tool catches it |
| 2026-11-09 r17 | F1 rule 5 "change items'" reads as the base's whole list | closed | "appended items'" |
| 2026-11-09 r17 | F2 rule 6 held-file clause reads as a term, not an instruction (round-16 repair) | closed | "the base's too, even in files copied from it" |
| 2026-11-09 r17 | F3 type guides say "fold footnotes"; this guide never says "footnote" | routed | The three promotion guides' passes reword the pointer |
| 2026-11-09 r18 | F1 rule 6 copied-file clause gives the act, not why (a bare `D<n>` there is the base's; collides with the request's own IDs unseen) | closed | "a copied base file's bare `D<n>` are the base's: link them" (reviewer's text; spec amendment item 2 kept: the base is another package) |
| 2026-11-09 r18 | F2 after a fold, the base's drafts keep links to its own items | logged | Spec silent; tools accept both forms |
| 2026-11-09 r18 | F3 `check-changes` exempts folded entries' bare `D<n>` | logged | Tool: drop the `Change request:` exemption or flag bare IDs in folded entries |
| 2026-11-09 | Rules 5 and 6 restructured as numbered steps (Fable, cap 3,600) | applied | 3,449 -> 3,598; every meaning earlier rounds fixed carried (checked against the round history); no change outside rules 5 and 6 |
| 2026-11-09 r19 | F1 rule 6.1 copied-file clause too dense where the tool is silent | closed | "in a copied base file, bare `D<n>` are the base's items: link them" |
| 2026-11-09 r19 | F2 rule 6.2 omits copies, the common path-breaking act | closed | "Copies, moves and folds keep links, repairing paths" |
| 2026-11-09 r19 | F3 rule 6.2 restates 5.1; cross-references point at rules, not steps | closed | Restatement dropped (5.1 is the sole statement); "(6.3)" |
| 2026-11-09 r19 | F4 rule 5.1 "in both" | closed | "in drafts and items" |
| 2026-11-09 r19 | F5 rule 5 lead runs two statements together | closed | Full stop before "Into a package:" |
| 2026-11-09 r19 | F6 5.1 links "to the request" before the archive step | logged | Repaired by 6.2 and the type guides' archive step |
| 2026-11-09 r19 | F7 rule 9 "except your base" gives no pointer | logged | Cosmetic |
| 2026-11-09 r20 | F1 rule 5.1 "items" has two referents (round-19 repair) | closed | "in drafts and appended items" (round 17's wording, not "change items": the base's own list is not relinked) |
| 2026-11-09 r20 | F2 rule 4 "may edit anything" lost the spec's "in it" | closed | "may edit anything in it" |
| 2026-11-09 r20 | Trim offered: 5.3 "first input now the base" | declined | States a state, not the act (round 6 F3, round 16); not needed under 3,600 |
| 2026-11-09 r20 | F3 which copy of the drafts 5.1 links | logged | Spec amendment item 3 reads two ways |
| 2026-11-09 r21 | F1 rule 5.1 "drafts become the base's" reads as replacing the base's whole drafts folder | closed | "The request's files overwrite the base's, file by file"; the type guides' "replace its drafts" routed to their passes |
| 2026-11-09 r21 | F2 rule 4's record sentence describes, not instructs | closed | "Record for the originator in Discussion and Decision Log what stayed, changed or dropped and why."; reviewer's trim 6.1 "are the base's" |
| 2026-11-09 r21 | F3 rule 7 "like any input's" has no pointer to known-gaps | logged | The authoring guides link known-gaps |
| 2026-11-09 r22 | F1 rule 5.1 "files" includes the authoring artifact (round-21 repair) | closed | "The request's drafts overwrite the base's, file by file" |
| 2026-11-09 r22 | F2 rule 4's record does not say it is a ruled Discussion item | logged | The tool rejects free-form log lines; sharpening needs bytes the guide lacks |
| 2026-11-09 r23 | F1 rule 4's record names no artifact; spec puts it in the request's | closed | "in its Discussion and Decision Log"; reviewer's trim 5.2 "Check off items"; its rule-2 trim declined (restored text) |
| 2026-11-09 r23 | Open: nothing verifies the fold's check-off (5.2) | logged | Tool |
| 2026-11-09 r24 | F1 rule 4 "Record … what stayed" may invite an item per accepted entry | closed | Supervisor, 2026-11-09: the partial-acceptance sentences are workflow; deleted from rule 4 and the spec amended; existing Discussion, log and change-list rules record every change |
| 2026-11-09 r24 | F2 rule 6's lead does not announce 6.3 | logged | Cosmetic; guide read whole |
| 2026-11-09 r24 | F3 the example's `**` reads as the whole drafts tree | logged | Cosmetic; rule 2 says only files they change; example untouched |
| 2026-11-09 r24 | F4 design tool humanizes the change id in the top bar | logged | Tool |
| 2026-11-09 r25 | F1 rule 5.1's only citing example labels the cited item `001` right after "the base's too": reads as "label with my own request number" | closed | Reviewer's fix: 5.1 example is `[D27][reminder-expiry D27]`; the request-label form moves to 4.1, `[D5][001 D5]`, where the fold writes it |
| 2026-11-09 r25 | F2 rule 6 "resolves any as that request's own" unclear; drop "as that request's own" | rejected | Reverses r10's fix, which says how the item is resolved; "where" and "that request's own" already place it in the request |
| 2026-11-09 r25 | F3 rule 4.1 "overwrite" omits files the request adds; revert to "become" | logged | Cosmetic; reverting reverses r21's fix ("become" read as replacing the whole folder); the type guides' write steps create absent files |
| 2026-11-09 r25 | F4 4.4 re-renders the base, not requests moved in 4.3 | logged | Cosmetic; spec silent; the moved request renders on its next authoring turn |
| 2026-11-09 r26 | F1 rule 4.1's link clause: "in drafts" is the base's whole folder after the overwrite (base's own bare `D<n>` can be relinked); the r25 example has no route to 5.1's definition rule | closed | "in its drafts" (the request's drafts, r22's wording) and "(`[D5][001 D5]`, per 5.1)"; reviewer's pointer, scope reworded to keep the authoring artifact out (r22) |
| 2026-11-09 r26 | F2 rule 5.1's example reads as two labels, not use and definition | logged | Cosmetic |
| 2026-11-09 r26 | F3 labels by change id collide when two types share an id and item number | logged | Rare; any qualifier is a new form rule; for the type guides' passes or the tool |
| 2026-11-09 r27 | F1 rule 5.1 "in a copied base file, bare `D<n>` are the base's" is a standing state; the request's own later markers in that file read as the base's | closed | Reviewer's text: "when copying a base file, link its bare `D<n>` (the base's)" (act at the crossing, keeps r18's why) |
| 2026-11-09 r27 | F2 README's design-promotion summary still says a request's open gaps are carried into the base's Discussion | closed | README: "its open items and gaps staying in the archived request" (#118 consequence; outside the guide, not scored) |
| 2026-11-09 r27 | F3 a folded Decision line copies a `<decision>` that need not name answered / adopted / omitted | logged | Cosmetic; the Decision format is process-flow's |
| 2026-11-09 r28 | F1 pronouns in 4.1 ("its drafts"), 4.2 ("where they live … there"), 5.1 ("its bare `D<n>` (the base's)") resolve by reasoning; every reading gives the same action | logged | Cosmetic; reviewer's own triage log-only |
| 2026-11-09 r28 | Open question: a `decided` log line on a non-base input passes every check and is never folded | logged | Against the tool; the guide gives only the base case (settled) |
| 2026-11-09 r28 | Open question: nested requests both labelled `001` can need two `[001 D<n>]` definitions in one file | logged | Adds a concrete case to the logged nested-label item |
| 2026-11-09 | Pass closed | closed | Supervisor, 2026-11-09, after r28 (score 1, one cosmetic finding logged): end the pass with every logged finding above left unimplemented (stop rule b). `change-requests.md` 3,488 / 3,600 |
| 2026-11-11 #108 C r1 | F1 rule 6's production readiness unscoped (where to look, type qualifier, a part counting against itself) | closed | "no other open request part of its type in the change" |
| 2026-11-11 #108 C r1 | F2 over the 4,220 cap | closed | Wording tightened, nothing dropped |
| 2026-11-11 #108 C r2 | F1 the move-up step sat under "Into a package" | closed | Moved into rule 4's body for any base |
| 2026-11-11 #108 C r2 | F2 rule 3's reopen sentence could override a direct-edit answer | closed | "For a request, reopen an open one …" |
| 2026-11-11 #108 C r2 | F3 rule 6's promoted parts not scoped to the whole change | closed | "any promoted part of its type there" |
| 2026-11-11 #108 C r3 | Type promotion screens said "no open request sub-package", self-blocking a production-based part | closed (routed) | "no other open" in the three screens |
| 2026-11-11 | #108/#129 pass 1 closed | closed | Clean round r3; 4,219 / 4,220 |
