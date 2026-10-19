# Spec File Shape — Findings Log

Target: `Guides/Core/spec-file-shape.md`. Standard: [`spec-format-design.md`](spec-format-design.md). Refiner-facing cross-pass record: never shown to a cold reviewer; settled decisions go to the prompt's settled-dispositions slot instead. One row per finding per pass; appended at each round's closure.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-18 r1 | F1 Command schedule omitted the spec's live-render rule (validate and render after every material package change) | closed | Paragraph under the command table; "a failure blocks" on validate |
| 2026-10-18 r1 | F2 Guide 9,582 bytes vs 8,200 cap | closed | 8,199 bytes: diff table → pointer, rejection inventory → one paragraph, When column folded into rows, prose trims; no rule removed |
| 2026-10-18 r1 | F3 Rejection inventory promised checks the parser does not make | closed (guide) / routed (tool) | Paragraph names only checks the tool makes and says what is not checked; tool lags spec 8 on sentence case (first letter only), empty rule text, element order, one-paragraph entries |
| 2026-10-18 r1 | F4 Glossary linking and the unlinked-term check cover item bodies only (not intro, section lines, known differences, table headers; retired items skipped) | routed to the tool | Guide and spec 4 agree; `link_terms` and `validate` iterate item bodies |
| 2026-10-18 r1 | F5 validate row said the overlay "checks what promotion would produce" | closed | Row states the overlay covers ID-uniqueness and glossary checks and every file's own shape is still checked (spec 8) |
| 2026-10-18 r1 | F6 Renderer misses table-under-rule edits, header and bound-order changes, link-target identity; word-diffs section text | routed to the tool | Guide's restated diff table removed; pointer keeps keys and what is not a change (docstring 1) |
| 2026-10-18 r1 | F7 Renderer parses only `R<n>` entries and item identities; glossary/index get no justification | routed to the tool | `CHANGE_RE` is `R\d+`; guide's claim equals spec 12 |
| 2026-10-18 r1 | F8 render-request reads `<request>/proposed-product-specs` only | routed to the tool | Spec 13 covers both types |
| 2026-10-18 r1 | F9 Change Items named Description as a field; artifacts guides require inline old/new text, against spec 15 | closed (guide) / routed (artifacts guides' refinement, settled) | Fields now ID, type, identity, justification, touched files |
| 2026-10-18 r1 | F10 Index example had no title, reminder line or link definitions; validator rejects it | closed | Complete example validates at 0 issues; glossary lead names the title |
| 2026-10-18 r1 | F11 (refiner) glossary link name `g-overdue` for anchor `overdue-reminder` | closed | `g-overdue-reminder`, as spec 4's `g-anchor` and `link-terms` write it |
| 2026-10-18 r1 | Open: spec 15's list-matches-diff tool check does not exist in the tool | open question | Guide does not claim it; for the supervisor |
| 2026-10-18 r1 | Open: spec 15 "every changed item has a list entry" vs artifacts guides' file-level entries for new files | open question | For the artifacts guides' refinement |
| 2026-10-18 r1 | Open: spec's "size budget none declared yet" bullet contradicts its Size Budgets section | open question | Spec hygiene |
| 2026-10-18 r1 | (refiner) Committed render file names and locations (spec 15) not in the guide | logged | Single observation; package layout belongs to the artifacts guides |
| 2026-10-18 r1 | Supervisor rulings after r1 | ruling | Tool gaps (F3 tool part, F4, F6–F8) fixed in the tool by a separate pass; list-matches-diff check deferred to the tool, guide silent until it exists; spec's stale "no size budget" bullet deleted |
| 2026-10-18 r2 | F1 `references` does not find in-item bold-number pointers (`(**01**)` in a table cell or sibling rule) | logged (routed to the tool) | Guide claim is accurate: a pointer names no ID and lives in the item being edited; enhancement candidate for the tool |
| 2026-10-18 r2 | F2 `render` row silent on what `--authoring` supplies; omitting it drops the card, discussion and justifications | closed | Row names what the flag supplies and the one reason to omit it; verified with and without the flag. Heavier option (require it for review renders; spec 9) left to the supervisor |
| 2026-10-18 r2 | F3 Table entry omitted the nonempty-key rule (spec 8) | closed | "nonempty and unique"; rejection observed on broken/tables.md:16 |
| 2026-10-18 r2 | Open: validator paragraph described today's tool limits (unlinked-term scope, "not checked" order) | closed (ruling 1) | Paragraph now states spec 8's scope; the repaired tool meets it (probes: known-difference order, sentence case, intro-term link all rejected) |
| 2026-10-18 r2 | Supervisor ruling after r2 | ruling | Spec 9 amended: `render` finds the package's authoring artifact itself; `--authoring` only points elsewhere; `--no-authoring` is a bare comparison, never the committed page. Render row adjusted; tool change pending in the tool pass |
| 2026-10-18 r3 | F1 `link-terms ROOT...` rewrites unshadowed files of every root given, so `<catalog> <drafts>` touches canon | logged | The row says "rewrites files"; no occurrence; multi-root lookup and in-place rewrite are spec 9's design; sharpen the row if an operator is caught by it |
| 2026-10-18 r3 | F2 "A retired item's says what superseded it" assumes a successor exists | logged | Spec 1 requires a statement, not a successor; unobserved branch covered by the standing stop; on recurrence: "says why it was retired, naming any successor" (about +20 bytes) |
| 2026-10-18 r3 | Open: a table cell's `**01**` pointer is ambiguous when a parent rule and its nested rule both carry `01` | open question | Standard-level tension (spec 2–3); no notation added without a real case |
| 2026-10-18 r3 | No live findings | closed — clean fresh round | Convergence by clean round; series A r1 19.0 → r2 7.5 → r3 0; size 9,582 → 8,198 (cap 8,200). Pending in the tool pass at close: `render` locating the authoring artifact itself and `--no-authoring` (amended spec 9) |
| 2026-10-18 r3 | Supervisor ruling at closure: bold-number pointer ambiguity | ruling | Spec decision 3: a bare bold number points at a top-level rule; a nested rule is pointed at as `01-01`. Guide to pick it up in a later consistency pass (open question above resolved) |
| 2026-10-18 r3 | Pass closed by the supervisor | closed | Target 1 closed at 8,198 bytes (from 9,582; cap 8,200) after clean round 3; series A r1 19.0 → r2 7.5 → r3 0 |
