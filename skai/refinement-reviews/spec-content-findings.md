# Spec Content Guides — Findings Log

Target 2: `Guides/ProductSpecs/product-specs-catalog.md`, `product-specs-artifacts.md`, `Guides/DesignSpecs/design-specs.md`, `design-specs-artifacts.md`, refined together for fidelity and parallel structure. Standards: [`product-specs-system-design.md`](product-specs-system-design.md), [`design-specs-design.md`](design-specs-design.md), [`spec-format-design.md`](spec-format-design.md). Refiner-facing cross-pass record: never shown to a cold reviewer; settled decisions go to the prompt's settled-dispositions slot instead. One row per finding per pass; appended at each round's closure.

## Seeded from earlier passes (content-guide-relevant rows)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-27 p1 (req) | `proposed-requirements/` full mirror or subset | closed | Touched files only, each drafted whole (P5) |
| 2026-08-28 r3 (req) | Zero-padding inside a legacy file whose IDs are unpadded | superseded 2026-10-18 | Spec-format decision 6 and the validator require two digits; the legacy-match clause is removed with the shape move |
| 2026-08-29 r7 (req) | `retire glossary entry` means delete, thirty lines after an ❌ forbidding deletion | closed | Only a requirement keeps its heading and `(retired)`; a retired glossary entry is removed |
| 2026-08-30 (req) | Silent loss of glossary entries or index lines on a whole-file rewrite | accepted risk, stated | Drafting rule is the obligation; no check backs it (P9); do not re-raise |
| 2026-08-30 r8 (req) | Modify-vs-retire had no pointer where the type is chosen | closed | Type bullet points at the catalog guide's rule; the rule has one home |
| 2026-08-30 r9 (req) | Digit-bearing prefixes invisible to the ID pattern | closed | Prefix is letters and hyphens only (shape guide) |
| 2026-08-30 r11 (req) | A package whose only change is an index line has no `Type` to ride on | logged | Stranded, not broken; the standing blocked gate covers it |
| 2026-08-30 r15 (req) | Mandatory inline cross-references have no check | open — supervisor | A proof burden; in the unimplemented ledger; do not re-raise |
| 2026-08-30 r15 (req) | Catalog root stated as a literal path | closed | The Integration block names the root; guides say `<catalog root>` |
| 2026-08-30 r17 (req) | Index layer taught by example, never stated; cross-reference field placement | closed | Index obligation stated; `(uses: …)` rides last on the file line |
| 2026-08-30 r18 (req) | Granularity: a baseline's glossary and root index fell through both clauses | closed | Catalog-root package is one item carrying root index and glossary |
| 2026-10-05 r1-release (req) | Known differences, promotion timing, link style, note cleanup | closed | Known-difference blockquote under the item; verified cleanup by work-spec implementation only; reference-style links in stored documents |
| 2026-10-14 p1 r1 (ds) | Never Appearance had no test | closed | Redesign test with ❌/✅ |
| 2026-10-14 p1 r1 (ds) | Glossary purpose/inventory rule; V9 blind | closed | Entry says meaning and purpose, may carry a detail, never inventories; V9 checks it |
| 2026-10-14 p1 r1 (ds) | Overrides: declaration and link direction | closed | Override declares and links the superseded rule; parents never name overrides |
| 2026-10-14 p1 r1 (ds) | Item opening statement and requirement link demonstrated, not required | closed | Required; V9 enforces |
| 2026-10-14 p1 r1 (ds) | Motion and polish had no home; V10 blind | closed | Fourth kind in What Counts as a State; V10 asks the careful-developer question |
| 2026-10-14 p1 r3 (ds) | General permission to restate another spec's rule defeated extraction | closed | Restatement only by a declared override (V7) |
| 2026-10-14 p1 r8 (ds) | New-file entries summarized while the inline-text rule had no exception | superseded 2026-10-18 | No change item carries inline text; the rendered page shows the diff (spec-format 15) |
| 2026-10-14 p1 r9 (ds) | V8 did not check duplicate live IDs across packages | closed | V8 rejects duplicates in projected canon; the validator checks the projection |
| 2026-10-14 p1 r11 (ds) | "clarified or tightened" let a stricter contract keep its ID | closed | Conformance test decides modify vs. retire |
| 2026-10-14 p1 r13 (ds) | Changing a table row bypassed Modify vs. Retire | closed | Data edits follow Modify vs. Retire |
| 2026-10-14 p1 r14 (ds) | Retirement "replaces the body", erasing descendant IDs | closed | Retire in place at every level; form in the shape guide |
| 2026-10-14 p1 r18 (ds) | "A glossary name brings all governing items" readable as inheritance | logged | Glossary never binds; delete the clause if it strands |
| 2026-10-15 backfill (ds) | Required delegated cold check before the Discussion gate | rejected (supervisor) | Review mechanics are not baked into the guide; do not re-raise |
| 2026-10-18 r1 (shape) | Change items named Description as a field; artifacts guides required inline old/new text | routed here, settled | Fields are ID, type, identity, justification, touched files |
| 2026-10-18 r1 (shape) | "Every changed item has a list entry" vs file-level entries for new files | open question, for this pass | `check-changes` accepts an added file named by one entry or in Touches |

## Target 2 passes

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-18 pre-review | Sectioned glossary (design-specs-design 5) rejected by the validator (spec-format 4) | ruling | Spec-format 4 amended: optional `##` sections, alphabetical within each; tool to accept; verify at round close |
| 2026-10-18 pre-review | Request drafts folder name vs tool lookup; `render` default artifact name vs legacy package names | ruling | Request drafts are `proposed-product-specs/` now; tool accepts legacy package names until the rename pass; verify at round close |
| 2026-10-18 pre-review | design-specs-design 9 stale ("changed text inline", "sub-item") | closed (standard) | Amended by the supervisor |
| 2026-10-18 pre-review | Legacy "match the file's unpadded IDs" clause | superseded | Validator requires two digits (spec-format 6); clause removed with the shape move |
| 2026-10-18 r1 | F1 "for any reason" vs "a package defect is not a request"; design artifacts guide's independence rule omitted the change-request link | closed | Exception narrowed to promotion's own failed check in both artifacts guides; design independence rule names the change request |
| 2026-10-18 r1 | F2 `check-changes` keys a rule entry to its parent item; a nonexistent rule or wrong operation passes | routed to the tool pass | Reproduced with `retire requirement: [REMIND-01-99]` → 0 issues; the guides claim only spec 15's item-level check |
| 2026-10-18 r1 | F3 renderer's retired-item branch shows statements only, dropping the old rules and tables | routed to the tool pass | Reproduced: retired card carries no old rule text |
| 2026-10-18 r1 | F4 V9 "no unnumbered binding prose" readable as rejecting the required statement | closed | "orientation prose binds nothing", matching Items and V1 |
| 2026-10-18 r1 | F5 request example omitted the mandatory review-page link | closed | Link line added under the example's title; field enumeration above it dropped |
| 2026-10-18 r1 | F6 modify vs. retire covers tightening, not relaxation | logged | No strand observed; on recurrence sharpen both guides to "a changed promise in either direction retires and adds" |
| 2026-10-18 r1 | Open: a request without drafts renders as a card alone; its typed list is only on `request.md` | open question | Standard (spec-format 13); not a guide defect |
| 2026-10-18 r1 | Open: design-specs-design 9 still says a new file's "description summarizes it" | open question | Standard hygiene |
| 2026-10-18 r1 | Round score | — | Series A r1 6.25 (3 divergent, 1 noise, 2 routed); sizes 10,468 / 6,439 / 14,991 / 4,996 = 36,894 |
| 2026-10-18 r1 | Supervisor rulings after r1 | ruling | F2, F3 to the tool pass; spec-format 13 amended (a request without drafts shows one card per requested change; guide says so); design-specs-design 9 residue fixed |
| 2026-10-18 r2 | F1 design-specs Layout said "restructures move, never delete, files" while Stability and the artifacts guide move only items | closed | Clause deleted (pre-review trim damage); Stability is the one home |
| 2026-10-18 r2 | F2 a request's change-item identity has no stated target when neither the request nor the package holds a draft of the item | logged | No occurrence; the standing stop covers it; on a strand, sharpen the product spec guide's Identity rule for requests, design guide inherits |
| 2026-10-18 r2 | F3 index-line and intro changes riding in `Touches` carry no justification on the rendered page | routed to the tool pass | Reviewer read the renderer (`c.keys & keys and c.why`; intro renders without a justification) |
| 2026-10-18 r2 | F4 an index line whose link is retargeted with unchanged text renders as unchanged, so `check-changes` rejects a correct entry | routed to the tool pass | Reproduced: `modified: 0` after retargeting `[reminders]` to `alarms.md` |
| 2026-10-18 r2 | Round score | — | Series A r2 1.875 (1 divergent, 1 noise, 2 routed); sizes 10,468 / 6,492 / 14,951 / 4,996 = 36,907 |
| 2026-10-18 r3 | F1 "a validation failure blocks" is unqualified while the guides exempt pre-existing and untouched-file defects; the tool reports every root's shape faults | supervisor decision — open | Reproduced: an untouched malformed canonical file fails the projection (exit 1). Standards conflict: req-sys P2 and design-specs-design 10 (scope) vs spec-format 8 and 10 (broad blocking) |
| 2026-10-18 r3 | F2 design-specs-artifacts § The Package banned "drawing location" for the whole package, against Writing Style's permission for package prose | closed | Clause deleted (pre-review trim had dropped "by specs"); the content guide owns the restriction |
| 2026-10-18 r3 | F3 per-folder glossaries sanctioned by design-specs-design 5 are unseen by `validate`, `link-terms` and `render` (root `glossary.md` only; spec-format 4 names one file) | routed to the tool pass | Reviewer's implementation read; standard-level tension noted for the supervisor |
| 2026-10-18 r3 | Trim-damage class (r2 F1, r3 F2: qualifiers dropped by the pre-review compression) | swept | Visual re-read of every shortened sentence in the four guides; no further occurrence |
| 2026-10-18 r3 | Round score | — | Series A r3 7.5 (2 divergent, 0 noise, 1 routed); sizes 10,468 / 6,492 / 14,951 / 4,954 = 36,865 |
| 2026-10-18 r3 | Supervisor rulings after r3 | ruling | F1: scoped reading — spec-format 8 and 10 amended; a fault in a held file or a projection conflict blocks, an untouched canonical fault is reported and becomes a change request; repaired in both content guides, shape guide row left for the consistency pass. F3: tool reads every `glossary.md` under the root as one glossary; per-folder split stays |
| 2026-10-18 r3 | F1 validation blocking vs review scope | closed | design-specs § Verification Checks lead and requirements-catalog § Purpose state the scoped rule; the tool filter is pending in the tool pass (verify at round close) |
| 2026-10-18 r4 | F1 catalog § Purpose exempted every pre-existing defect, including one inside a file the package holds (r3 repair wording) | closed | "a defect in an untouched canonical file never blocks a package but becomes a change request"; tool probe: held-file fault exit 1, untouched fault note + exit 0 |
| 2026-10-18 r4 | F2 design-specs "every app named by the requirements root index" — the root index holds no app inventory | closed | "every app in the catalog's `apps/` index" (a dangling reference, repaired at negative cost although the reviewer logged it) |
| 2026-10-18 r4 | Open: `check-changes` verifies target coverage, not the declared operation | open question | Spec-format 15's own description; the guides claim no more; not a proof burden to add |
| 2026-10-18 r4 | Round score | — | Series A r4 7.5 (2 divergent, 0 noise); sizes 10,488 / 6,492 / 14,983 / 4,954 = 36,917; consolidation trigger fired once (r3 F1 → r4 F1) |
| 2026-10-18 r4 | Supervisor ruling after r4 | ruling | `check-changes` will verify the declared operation as well as coverage (tool pass); spec-format 15 stands |
| 2026-10-18 r5 | F1 `platform` defined as "invariants that hold regardless of app or feature", which domain invariants also satisfy under "choose the first that fits" | closed | "protocol, infrastructure and format contracts, the same for every app and feature"; domains keep entities, invariants, transitions |
| 2026-10-18 r5 | Tool confirmations: unlinked-term faults in untouched canon still block; `check-changes` special-cases `sub-item` while the design vocabulary is `rule` | routed to the tool pass | Already assigned (r3 F1 ruling; r1 F2 / r4 ruling); the guides' wording stands |
| 2026-10-18 r5 | Round score | — | Series A r5 2.5 (1 divergent, 0 noise); sizes 10,486 / 6,492 / 14,983 / 4,954 = 36,915 |
| 2026-10-18 r5 | Supervisor ruling after r5 | ruling | An unlinked term occurrence in an untouched canonical file is a note, never a block (tool pass); guides already say so — no edit |
| 2026-10-18 r6 | F1 `references` finds bracketed citations only, not a sibling rule's bold-number pointer (re-raise of shape pass r2 F1) | routed to the tool pass | Reproduced: `references STAGE-01-01` omits the `(**01**)` table pointer at `pipeline-stage.md:14`; the guides' sweep instruction stands |
| 2026-10-18 r6 | F2 `check-changes` rejects a declared `move item` plus `modify item` (per-file comparison yields missing/added; modify accepts only modified) | routed to the tool pass | Reviewer's implementation read; the artifacts guide's move-plus-modify rule stands |
| 2026-10-18 r6 | No live findings in the binding target | closed — clean fresh round | Stop rule (a); series A r1 6.25 → r2 1.875 → r3 7.5 → r4 7.5 → r5 2.5 → r6 0; sizes 58,385 → 36,915 (caps 10,500 / 6,500 / 15,000 / 5,000; group 37,000); tool md5 785ed314 at close |

Pass converged by a clean round: round 6 (series A) raised no finding in the four guides. Net size change 58,385 → 36,915 (−21,470): 10,486 / 6,492 / 14,983 / 4,954. Consolidation trigger fired once (r3 F1 → r4 F1), not twice. Routed to the tool pass during this pass: rule-level `check-changes` (r1 F2), retired-item render (r1 F3), `Touches` justifications (r2 F3), index retarget diff (r2 F4), per-folder glossaries (r3 F3), unlinked terms in untouched canon (r5), bold-number `references` (r6 F1), move-plus-modify (r6 F2). Logged, not codified: modify-vs-retire on a relaxed contract (r1 F6); request identity without a draft (r2 F2). Dependents in the read-only authoring, promotion and baseline guides are listed in the working document for targets 3 and 4.
| 2026-10-18 r6 | Pass closed by the supervisor | closed | Target 2 closed at 36,915 bytes after clean round 6; r6 F1 and F2 with the tool pass; no further rounds |
