# Spec File Shape Refinement

Working document for the refinement pass on `Guides/Core/spec-file-shape.md`. Standard: `skai/refinement-reviews/spec-format-design.md` (Size Budgets 2026-10-18: 8,200 bytes whole file by `wc -c`). Findings log: `skai/refinement-reviews/spec-file-shape-findings.md`. Tool: `Bin/spec-tool.py`; fixtures: SalesPro `working-docs/requirements-process/fixtures/` (catalog + package/proposed-product-specs must validate at 0 issues; broken/ must fail with file and line).

Size at start: 9,582 bytes (1,382 over the cap).

Series A: full cold review, Codex gpt-6-astra, standard charter.

## Pre-review tool verification (2026-10-18)

- `validate catalog package/proposed-product-specs` → 5 files, 0 issues, exit 0. `validate broken` → 22 issues, each `path:line: message`, exit 1. `validate package/proposed-product-specs` alone → 3 files, 0 issues.
- `references STAGE-01 …` lists `[STAGE-01]` and `[STAGE-01-01]` citations with file:line, including the authoring artifact and glossary.
- `link-terms` on a scratch copy with one unlinked "terminal stage": validate fails (unlinked use + defined-but-unused), link-terms reports `linked 1 term uses`, validate then passes.
- `render` and `render-request` on the fixtures write HTML pages, exit 0.
- CLI: `--authoring` is optional; the other render flags are required (argparse).

## Rounds

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 19.0 | 7 | 0 | 5 | 2 | 0 |
| r2 (A) | 7.5 | 2 | 0 | 2 | 0 | 1 |
| r3 (A) | 0 | 0 | 0 | 0 | 0 | 2 |

> F1 command schedule omits the spec's live-render rule (spec line 152, added after the guide was drafted): divergent · normal · speculative = 2.5 · F2 size 9,582 vs 8,200: cosmetic · normal · verified = 2 · F3 rejection inventory promises more than the parser checks; guide-side part is the vague "does not match its shape" entries, the lax sentence-case / empty-rule-text / ordering checks are the tool's shortfall against spec 8 and route to the tool: divergent · past-a-rule · verified = 1.25 · F4 glossary linking and checking cover item bodies only — guide and spec 4 agree, the tool lags: routed to the tool, neither · F5 "checks what promotion would produce" overstates the overlay, which spec 8 limits to uniqueness and glossary checks: divergent · off-normal · verified = 3.75 · F6 renderer drops table-under-rule, header, link-target and diffs section text — tool vs docstring/spec 11: routed to the tool, neither (the guide's restated diff table goes under F2) · F7 renderer reads only `R<n>` entries and item identities — tool vs spec 12: routed · F8 render-request reads only `proposed-product-specs` — tool vs spec 13: routed · F9 Change Items names "Description" as a field, which spec 15 excludes (the artifacts guides' inline-diff rules route to their own refinement, settled): divergent · normal · speculative = 2.5 · F10 index example has no title, reminder line or link definitions and the validator rejects it (verified: `file must start with a single '# Title' line`, `[reminders] used but not defined`); reviewer said log-only, accepted as a deterministic example defect: divergent · normal · verified = 5 · F11 (refiner-observed) glossary link name `g-overdue` for anchor `overdue-reminder`; spec 4 says `g-anchor` and `link-terms` writes `g-overdue-reminder`: cosmetic · normal · verified = 2. Open questions (neither): list-matches-diff tool check absent (spec 15); item-vs-file entry granularity (spec 15 vs artifacts guides); the spec's stale "size budget none declared yet" bullet.

## Round 1 Finding Matrix

Size at start 9,582; cap 8,200; fixed cost (managed header + addendum footer) 923; content budget 7,277.

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F2 size 9,582 vs 8,200 | accept | Size Budgets, Guide Shape ("the guide does not restate" the render spec); § How The Renderer Diffs, § What The Validator Rejects, § The Spec Tool | Replace the diff table with a two-sentence pointer to the docstring (keeps what an author needs: what is not a change); dedupe the rejection inventory against Elements; drop the When column (F1 owns timing). Cost: about −1,300 | The example; every element rule; the command list |
| F3 rejection inventory overpromises | accept (guide part); tool part routed | D8; § What The Validator Rejects | Each listed rejection is one the tool makes, verified by the broken/ output; delete "does not match its shape" entries. Cost: inside the F2 rewrite | Spec 8's list stays the tool's standard; nothing is described as accepted syntax |
| F5 overlay sentence overstates | accept | D8; § The Spec Tool validate row | Say what overlays: drafts replace their catalog files for ID uniqueness and glossary checks; every file's own shape is still checked. Cost: about +40 | Later-root-overlays-earlier wording |
| F1 schedule omits live render | accept | Live render (spec line 152), D10; § The Spec Tool | One sentence under the command table: validate then render after every material package change, in every workflow that writes a package; the gate and promotion runs are the last; a validation failure blocks. Cost: about +300, offset by dropping the When column | Workflow guides own gates and approval; no new gate here |
| F9 Change Items lists "Description" | accept (guide part); artifacts guides routed | D15; § Change Items | The pointer names the fields spec 15 keeps (ID, type, identity, justification, touched files) and what the renderer reads; no "Description". Cost: about −40 | Artifacts guides own the list format; the diff source stays the drafts |
| F10 index example fails validation | accept | D5, acceptance 1; § Index File, § Glossary File | Complete index example (title, reminder line, two entries, link definitions); glossary section names the title. Cost: about +170 | File lines carry prefixes, folder lines none |
| F11 glossary link name not `g-anchor` | accept (trivial) | D4; § Link definitions | `g-overdue` → `g-overdue-reminder` (two places). Cost: +18 | — |

Routed to the tool (`Bin/spec-tool.py`, not refined in this pass; for the supervisor): F3 tool part (sentence case only checks the first letter; empty rule text accepted; known differences not required last; glossary entries not held to one paragraph); F4 (link-terms and the unlinked-term check cover item statements, rules and table rows only — not intro, section lines, known differences, table headers; retired items skipped); F6 (table-under-rule edits do not mark the item changed; added/removed tables under a rule dropped; headers and bound row order not compared; link-target identity not compared; section descriptions word-diffed although the spec says sections are not diffed); F7 (only `R<n>` entries parsed; justification looked up by item ID only, none for glossary/index entries); F8 (`render-request` reads `<request>/proposed-product-specs` only).

Routed to the artifacts guides (their own refinement, settled): inline old/new text in change entries vs spec 15.

Repair order: cluster 1 = F2 (+ F6's restated diff table), trims needing no decision; cluster 2 = F3, F5 (tool claims); cluster 3 = F1, F9 (runtime handoff); cluster 4 = F10, F11 (examples).

## Cluster 1 (F2 trims, F6's restated diff table)

Diff table replaced by a four-sentence pointer (keys, word diff, what is not a change, docstring is the render spec); the dash-form rationale, the two "keyed for diffing" sentences and the duplicate docstring pointer deleted. 9,582 → 9,038 (−544).

Self-check: no contradiction with adjacent text (the keys named in the pointer are the ones Elements, Glossary File and Index File define); no stale sentence teaching the old behavior (grep "keyed", "docstring": one mention each, in the diff section); no rule moved from its point of use (what is not a change is a reviewer-side fact, read where diffing is explained); nothing weakened (glossary-link-not-a-change, section-move-not-a-change and link-target-identity rules all kept).

Sanity scan (maintain-skai, guide-authoring): Managed-Updated-At 2026-10-18 = today's edit date → ok; no gates, so the Gates/Advance-intent/process-flow/marker-lifecycle checks do not apply (visual review of the whole file: no `⏳ GATE:`, no `## Gates`); `grep -n '\bhuman'` → 0 occurrences; `grep -n '🟡\|- \[ \]'` → 1 occurrence (line in What The Validator Rejects, naming the markers the validator rejects) → false positive, intentional; no working-doc paths in the guide → n/a; stack-mismatched references → 0 (visual review).

## Cluster 2 (F3, F5: tool claims)

What The Validator Rejects rewritten as one paragraph naming only checks the tool makes (each verified against the broken/ fixture output and the parser: title/heading shape, missing statement, prose after rules, duplicate IDs, rule numbering and nesting, table header/separator/keys, link definitions unused/undefined/duplicated/not at end, progress markers, glossary heading/order/duplicate/capitalization, index bullet shape, unlinked term in an item's statement, rules or table cells) and stating what is not checked (wording; order of tables, rules and known differences) with "the shapes above still bind". The validate row now says what the overlay does (drafts replace catalog files for ID-uniqueness and glossary checks) and that each file's own shape is still checked. 9,038 → 8,896 (−142).

Self-check: no contradiction with adjacent text (Elements still states the full shape, including order; the rejects paragraph claims less, not more); no stale sentence (grep "what promotion would produce": 0; grep "does not match its shape": 0); no rule moved; nothing weakened — the order rule is still stated in Elements and the paragraph says the shapes bind whether or not checked.

Sanity scan: Managed-Updated-At 2026-10-18 = today → ok; gate checks n/a (no gates); `grep -n '\bhuman'` → 0; `grep -n '🟡\|- \[ \]'` → 1 (the markers the validator rejects) → false positive; working-doc paths n/a; stack mismatch 0 (visual).

## Cluster 3 (F1, F9: runtime handoff)

When column dropped; the references and link-terms timing folded into their rows; "A failure blocks" on validate (spec 10); a paragraph under the table carries the spec's live-render rule (validate, then render, after every material package change, in every workflow that writes a package; gate and promotion runs are the last of many). Change Items names the fields spec 15 keeps (ID, type, identity, justification, touched files) and no longer names Description. 8,896 → 9,152 (+256).

Self-check: no contradiction (the table rows no longer say "whenever the supervisor reviews", so the live-render paragraph is the only timing statement; the validate row's "a failure blocks" agrees with it); no stale sentence (grep "Whenever the supervisor", "Description": 0); no rule moved (timing sits with the commands); nothing weakened (the gate and promotion runs are still required, now as the last of many).

Sanity scan: Managed-Updated-At 2026-10-18 = today → ok; gate checks n/a; `grep -n '\bhuman'` → 0; `grep -n '🟡\|- \[ \]'` → 1 (validator rejects) → false positive; working-doc paths n/a; stack mismatch 0 (visual).

## Cluster 4 (F10, F11: examples)

Index example is now a complete file (title, reminder line, two bullets, link definitions); the Glossary File lead names the title; glossary link name `g-overdue` → `g-overdue-reminder` in both places. 9,152 → 9,387 (+235). The three examples, extracted to a scratch root (glossary wrapped with its title and the one link definition the fragment implies), validate at 0 issues.

Self-check: no contradiction (Elements' Title and Link definitions rules now match what the index example shows); no stale sentence (grep "g-overdue`": 0; "holds one reminder line": 0); no rule moved; nothing weakened.

Sanity scan: Managed-Updated-At 2026-10-18 = today → ok; gate checks n/a; `grep '\bhuman'` → 0; marker grep → 1 (validator rejects) → false positive; working-doc paths n/a; stack mismatch 0.

## Cluster 5 (F2: prose trims, no rule changed)

Shorter phrasing throughout (intro, every Elements entry, glossary and index leads, IDs, tool preamble and rows, live-render paragraph's rationale sentence, Change Items, validator and diff paragraphs); example text shortened (intro, rule 01, known difference, issue URL, index bullet's "uses:" tag and its definition). Every rule, element, command and example path survives; the "uses:" tag was not a spec element (spec decision 5 names only name, prefixes and questions). 9,387 → 8199 (−1188). Cap 8,200: 1 bytes of headroom.

Self-check: no contradiction (each trimmed sentence was re-read against its neighbours; the Rule and Table entries still state nesting, citation, append-only, keys, order and bold-number pointers; the validate row still states the overlay limit from cluster 2; the live-render rule still names all four triggers and "the last of many"); no stale sentence (grep "whichever", "navigation.", "immediately under", "Nothing else", "stay indefinitely": 0); no rule moved; nothing weakened (every "never", "required", "unique", "blocks" kept). Examples re-validated: 0 issues. Fixtures: catalog + drafts 0 issues, broken 22 issues exit 1.

Sanity scan: Managed-Updated-At 2026-10-18 = today → ok; gate checks n/a; `grep '\bhuman'` → 0; marker grep → 1 (validator rejects) → false positive; "checkpoint"/"Next Command" → 0; working-doc paths → 0; stack mismatch 0 (visual, whole file). CHANGELOG: the 2026-10-18 Unreleased entry for this new guide still describes it (nothing added or removed at the level it names); manifest and README unchanged.

## Round 1 Closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 live-render schedule | closed | Paragraph under the command table: validate then render after every material change, in every workflow that writes a package; gate and promotion runs the last of many; "a failure blocks" on validate |
| F2 size | closed | 8199 bytes (`wc -c`), cap 8,200; diff table → pointer, rejection inventory → one paragraph, When column folded, prose trims; no rule removed |
| F3 rejection inventory | closed (guide part) / routed (tool part) | Paragraph names only checks the tool makes (each seen in the broken/ output or the parser) and says what is not checked; tool shortfalls vs spec 8 listed for the supervisor |
| F4 glossary coverage | routed to the tool | Guide and spec 4 agree; `link_terms` and the unlinked-term check cover item statements, rules and table rows only |
| F5 overlay overstated | closed | validate row: drafts replace catalog files for the ID-uniqueness and glossary checks; every file's own shape still checked (matches spec 8 and `validate()`) |
| F6 renderer drops edits | routed to the tool | Guide's restated diff table removed under F2; remaining pointer states the keys and what is not a change, per docstring 1 |
| F7 S-entries and rule identities | routed to the tool | Guide's Change Items claim equals spec 12; `CHANGE_RE` parses `R\d+` only |
| F8 render-request product-only | routed to the tool | `cr_drafts = request_dir / "proposed-product-specs"` |
| F9 Change Items fields | closed (guide part) / routed (artifacts guides, settled) | Fields now ID, type, identity, justification, touched files (spec 15); Description gone; inline-diff rules belong to the artifacts guides' own refinement |
| F10 index example | closed | Complete example validates at 0 issues (title, reminder line, bullets, link definitions) |
| F11 g-anchor name | closed | `g-overdue-reminder` matches spec 4 and `link-terms` output |
| Open: list-matches-diff tool check (spec 15) absent | open question | Not claimed by the guide; for the supervisor |
| Open: item-vs-file entry granularity (spec 15 vs artifacts guides) | open question | For the artifacts guides' refinement |
| Open: spec "size budget none declared yet" bullet stale | open question | Spec hygiene; not the target |
| Refiner-observed: committed render file names (spec 15) not in the guide | logged | Single observation; the package folder layout belongs to the artifacts guides' tables; nothing added |

## Supervisor Decisions After Round 1 (2026-10-18)

1. Tool gaps are being fixed by a separate agent against the spec and fixtures; the tool is not touched here. Re-run fixture verification at the close of each round; a guide claim the tool now fulfils is satisfied.
2. The list-matches-diff check will be implemented in the tool; the guide need not claim it until it exists.
3. The spec's stale "no size budget" bullet is deleted.

Round 2 commissioned over the current text (8,199 bytes), series A continued: same scoring model, files, scope and charter; settled dispositions refreshed from the log.

## Round 2

Reviewer: Codex gpt-6-astra, prompt `r2/prompt.txt` (settled dispositions refreshed from the log; recently-revised lists every r1 change). Tool md5 at review time fedcd2a8… (unchanged since r1).

> F1 `references` does not find in-item bold-number pointers (`(**01**)` in a table cell or sibling rule): the guide's claim ("every file and line citing an ID or one of its rules") is accurate — a bold-number pointer names no ID and sits inside the item being edited; valid observation, log only, routed to the tool as a candidate enhancement: noise · F2 `render` without `--authoring` silently drops the card, discussion and justifications (verified: no "Goal" text, zero `class="why"` blocks); reviewer said supervisor-decision, but the minimal fix is one clause on the render row saying what `--authoring` supplies and when to omit it — documentation only, no gate — so accepted; the heavier option (make it required for review renders, spec 9 change) is for the supervisor: divergent · off-normal · verified = 3.75 · F3 Table entry omits the nonempty-key rule (spec 8, enforced by the tool): reviewer said log-only; accepted as a 13-byte sharpening of the existing key rule: divergent · off-normal · verified = 3.75. Open question (neither): the validator paragraph's "in an item's statement, rules or table cells" and "Not checked: …" describe today's tool limits, which supervisor ruling 1 says the guide must not do — repaired under that ruling, not scored.

`| r2 | 7.5 | 2 | 0 | 2 | 0 | 1 |`

### Round 2 Finding Matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| Validator paragraph states tool limits (open question; ruling 1) | accept (ruling) | D8; § What The Validator Rejects | Unlinked-term clause becomes spec 8's ("a glossary term unlinked outside its governing items"); the "Not checked: …" sentence goes; keep "the shapes above still bind" sense. Cost: about −150 | Each named check stays one the spec requires; both spec types alike |
| F2 render row silent on `--authoring` | accept | D9, D12, acceptance 4; § The Spec Tool render row | "`--authoring` supplies the card, discussion and justifications; omit it only for a drafts-only comparison." Cost: about +100, paid by the paragraph trim | `--authoring` stays optional in the CLI; no gate; render look stays in the docstring |
| F3 table key may be empty | accept | D8; § Elements Table | "the key, nonempty and unique within the table". Cost: +13 | Uniqueness, uncited rows, statement-bound order |

Routed to the tool: F1 (bold-number pointers in `references`), as an enhancement candidate.

Repair order: cluster 1 = validator paragraph (frees bytes); cluster 2 = F2, F3.

### Cluster 1 (validator paragraph per ruling 1)

Unlinked-term clause now spec 8's scope ("outside its governing items"); "not capitalized" → "not in sentence case" (spec 8's words); the "Not checked: … order …" sentence replaced by "Wording is never checked." 8,199 → 8,075 (−124).

Self-check: no contradiction (Linking terms still says every occurrence in prose links, which this clause now matches; Elements still states element order, no longer contradicted by a "not checked" note); no stale sentence (grep "table cells", "Not checked": 0); no rule moved; nothing weakened (the clause now claims the spec's full scope). Verification note for round close: the tool's coverage of intro/known-difference terms and sentence-case is pending its separate repair; recorded as a claim the tool is expected to fulfil.

Sanity scan: Managed-Updated-At 2026-10-18 = today → ok; gate checks n/a; `grep '\bhuman'` → 0; marker grep → 1 (validator rejects) → false positive; working-doc paths 0; stack mismatch 0.

### Cluster 2 (F2, F3)

Render row says what `--authoring` supplies (card, discussion, justifications) and when to omit it (a drafts-only comparison); Table entry: key "nonempty and unique"; one glossary sentence shortened to pay. 8,075 → 8187.

Self-check: no contradiction (the live-render paragraph still says validate then render after every material change; the drafts-only comparison is named as the only reason to omit `--authoring`); no stale sentence (grep "review page.": the render row only); no rule moved (the input's meaning sits on the command row); nothing weakened (`--authoring` stays optional in the CLI, as spec 9 has it; the review render's need for it is stated on the row).

Sanity scan: Managed-Updated-At 2026-10-18 = today → ok; gate checks n/a; `grep '\bhuman'` → 0; marker grep → 1 (validator rejects) → false positive; working-doc paths 0; stack mismatch 0.

### Round 2 Verification (tool md5 4004d102…, 1,266 lines — repaired concurrently by the tool pass)

Fixtures: catalog + drafts 5 files, 0 issues (exit 0); broken 22 file:line issues (exit 1); the guide's three examples 0 issues. Probes: the tool now rejects a rule after a known difference ("known differences come last in an item"), a glossary term `Overdue Reminder` as not sentence case, and an unlinked term in an intro paragraph — so the validator paragraph's spec-scope clauses (sentence case; unlinked term outside its governing items) are fulfilled, and the deleted "order is not checked" sentence would have become false. `render` without `--authoring` verified earlier this round to drop the card, discussion and justifications (zero `class="why"` blocks); `references OFFER-04-01` returns nothing for a bold-number pointer (F1, routed).

### Round 2 Closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 `references` misses in-item bold-number pointers | logged (routed to the tool) | Guide claim ("citing an ID or one of its rules") is accurate; pointers name no ID and sit in the item being edited; `references OFFER-04-01` → no output, observed |
| F2 `render` silent on what `--authoring` supplies | closed | Render row names the card, discussion and justifications and the one reason to omit it; verified by rendering with and without the flag |
| F3 table key may be empty | closed | Table entry: "nonempty and unique"; broken/tables.md:16 rejection observed |
| Open: validator paragraph stated tool limits | closed (ruling 1) | Paragraph now carries spec 8's scope; the tool, repaired in parallel, now meets it (probes above) |
| Supervisor option on F2 (heavier) | for the supervisor | Make `--authoring` required for review renders (spec 9 change + tool); not implemented |

Size 8,187 (13 bytes of headroom).

## Supervisor Decision After Round 2 (2026-10-18)

Spec 9 amended: `render` locates the package's authoring artifact itself when the drafts folder sits inside a package folder; `--authoring` only points elsewhere; `--no-authoring` gives a bare drafts-to-catalog comparison that is never the committed page. Tool change pending in the parallel tool pass; the render row may be adjusted to the amended spec if the cap allows.

### Render row to amended spec 9 (one cluster)

Render row now: the page carries the card, discussion and justifications of the authoring artifact it finds in the package; `--authoring` only points elsewhere; `--no-authoring` gives a bare comparison, never the committed page. Paid for by three trims that change no rule: "may link a tracking issue" (the example still shows one), "navigation only", "Wording is never checked" (spec 8 never claimed it), "with text after the number" (spec 2 does not say it; the tool does not check it). 8,187 → 8198.

Self-check: no contradiction (the live-render paragraph and the render row agree that a review render is the full page); no stale sentence (grep "drafts-only", "navigation only", "tracking issue", "Wording is never": 0); no rule moved; nothing weakened. Claim pending the tool: `render` finding the authoring artifact and `--no-authoring` — recorded as a claim the tool is expected to fulfil (ruling 1); verified at round close.

Sanity scan: Managed-Updated-At 2026-10-18 = today → ok; gate checks n/a; `grep '\bhuman'` → 0; marker grep → 1 (validator rejects) → false positive; working-doc paths 0; stack mismatch 0.

Round 3 commissioned over the current text (8198 bytes), series A continued (the spec 9 amendment changes what the `render` row may claim, a routine refresh recorded in the settled slot, not a new series).

## Round 3

Reviewer: Codex gpt-6-astra, prompt `r3/prompt.txt`. Tool at review time mid-repair (md5 c9199611… at close, 1,328 lines).

> F1 `link-terms ROOT...` may rewrite unshadowed catalog files when given `<catalog> <drafts>`: the row already says "rewrites files"; no observed misuse; reviewer and refiner log-only — noise · F2 "A retired item's says what superseded it" assumes a successor; the spec requires only a statement; unobserved branch, the standing stop covers it; log-only (a later sharpening "says why it was retired, naming any successor" costs about 20 bytes against 2 of headroom) — noise. No live findings in the binding target. Open question (neither): a table cell's bold-number pointer `**01**` is ambiguous when a parent rule and a nested rule both carry `01` — a standard-level tension (spec decisions 2–3), for the supervisor; reviewer recommends no notation without a real case.

`| r3 | 0 | 0 | 0 | 0 | 0 | 2 |`

### Round 3 Verification (tool md5 c9199611…)

Catalog + drafts 5 files, 0 issues; broken 22 file:line issues, exit 1; the guide's three examples 0 issues; spec-8 probes (sentence case, intro-term link) rejected; known-difference order rejected. Pending in the tool pass: `render` does not yet find the package's authoring artifact by itself (rendering the fixture package without `--authoring` still yields no card and no justifications) and `--no-authoring` does not yet exist — the render row states amended spec 9 per the supervisor's ruling; a claim the tool is expected to fulfil.

### Round 3 Closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 `link-terms` write scope across roots | logged | "Rewrites files" is on the row; no occurrence; multi-root lookup and in-place rewrite are the spec's design (decision 9) |
| F2 retired statement assumes a successor | logged | Spec requires a statement, not a successor; unobserved; sharpening deferred to recurrence (about +20 bytes) |
| Open: parent/child `**01**` pointer ambiguity | open question | Standard-level (spec 2–3); for the supervisor |

**Stop rule (a) met:** round 3 is a fresh round over the current text with no new live findings in the binding target (two log-only observations, one open question). Convergence by clean round. Series A: r1 19.0 → r2 7.5 → r3 0. Size 9,582 → 8,198 (cap 8,200). No supervisor-decision findings remain unimplemented.

## Pass Closed (supervisor, 2026-10-18)

Closure confirmed at 8,198 bytes after a clean round 3. Every finding of the pass carries a disposition with evidence or rationale above (r1 closure table, r2 closure table, r3 closure table): r1 F1, F2, F3 (guide part), F5, F9 (guide part), F10, F11 closed; r1 F3 (tool part), F4, F6, F7, F8 routed to the tool pass; r1 F9 artifacts-guide part routed to those guides' refinement; r2 F2, F3 closed; r2 F1 logged; r3 F1, F2 logged; open questions recorded. Net size change for the pass: 9,582 → 8,198 (−1,384), cap 8,200.

Supervisor ruling on the bold-number ambiguity: spec-format-design.md decision 3 now settles it — a bare bold number points at a top-level rule; a nested rule is pointed at as `01-01`. The guide picks this up in a later consistency pass (not in this one; no edit made).
