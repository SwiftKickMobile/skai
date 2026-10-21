# Spec Format — Refinement Record

Refinement record for the spec file shape guide and `Bin/spec-tool.py`, judged against [`spec-format-design.md`](spec-format-design.md); findings and their dispositions in [`spec-file-shape-findings.md`](spec-file-shape-findings.md).

## Slice 6 — Glossary Alternate Terms (skai#93), 2026-10-21

Scope: the glossary entry's Also called note (design decision 22). Touched: `Guides/Core/spec-file-shape.md` § Glossary File, its validator clause and diff keys; `Bin/spec-tool.py` parser, validation, render callout, diff, docstring; `internal/tests/tools/spec-tool/` fixtures (catalog and package glossaries carry the note; the package changes one alternate; `broken/glossary.md` holds a second note, an off-form note, prose after a note, and a definition that merely says "Also called") and assertions; the committed fixture page `package/product-specs-review.html` re-rendered. `ProductSpecs/product-specs-catalog.md` left unchanged: its "every entry ends by pointing at the requirements" reads against a final note, but the file is at 10,498 of its 10,500 cap and the shape guide, which owns layout, says the paragraph ends with the pointer; reported to the supervisor.

### Compression review (Astra, draft then cap)

Inventory given to the reviewer: optional, at most one; last, after the definition paragraph; the blockquote form; purpose (agents reading inputs); never linked or used in spec prose; validator clause; diff-key clause; the example shows the note. Proposed −46 bytes over five passages; applied −41 with plain sentences: "an optional final Also called note"; shorter example attributions; the form carried by the example ("in the example's form") instead of restated; "spec prose never links or uses them" (the reviewer's flag: "specs never use them" took in the glossary itself); "malformed" for "off its form"; "(its note keyed separately)" (kept "its" so the note is the entry's). Flag not acted on: an alternate that is also a glossary term would meet "Linking terms" — glossary files are not spec prose, so no conflict in the tool; left for the cold review.

| Old cap | Before | Drafted | Compressed | Addition | Proposed cap |
|---|---|---|---|---|---|
| 8,350 | 8,349 | 8,718 | 8,677 | +328 | 8,700 |

### Sanity scan — `Guides/Core/spec-file-shape.md` (after the compressed edit)

- `Managed-Updated-At` earlier than the edit: 0 occurrences (header reads 2026-10-21).
- `\bhuman` (grep -i): 0 occurrences.
- Gates / advance intent / `⏳ GATE:`: guide has no gates; `gate` (grep -i) 1 hit, line 122 "the gate and promotion renders", pre-existing, descriptive — false positive.
- Markers (`🟡`, `- [ ]`): 1 hit, line 130, the validator list naming them as rejected — false positive.
- Working-doc paths, `evidence/`: 0 occurrences.
- Process-flow template, Discussion, gap pointer checks: not applicable (no Discussion phase; gap material lives in `spec-file-gaps.md`).

### Cold review — round 1 (Astra)

Prompt: `cold-review-prompt-template.md` verbatim, slots filled; Legacy, Observed failures, Proposed edits and Report charter sections deleted; diff against the template shows only slot fills and deleted sections. No guide finding; three tool findings, all `accept`, each its own row (the reviewer named one cluster, F1's parser gaps, already one finding).

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 note-like line with leading space, blank attribution | accept | decision 22 form; `_parse_glossary`, `ALSO_*` | widen recognition, require nonblank fields | definition prose saying "Also called"; `>` continuation lines |
| F2 popover drops the note | accept | render conventions 6, 8; `prepare`, `render_popovers` | carry the note into the popover | no lookup or popover by alternate; note text unlinked |
| F3 move check ignores `--base` | accept | decision 17, 22; `moved_entry_status` | compare against the layered baseline | a relocation stays one move |

Repairs, one cluster each, test run after each: all pass. Self-checks: no guide text changed (size 8,677); docstring's check-changes paragraph sharpened for F3 ("the definition or Also called note … compared with the catalog under any --base"); no stale sentence found (grep "Also called" over the docstring). Re-rendered the committed fixture pages; the design request page was stale from earlier slices and is now current too.

F1 divergent · past-a-rule · verified = 1.25 · F2 divergent · normal · verified = 5 · F3 divergent · off-normal · verified = 3.75 · catalog "entry ends" and design-specs V3 platform names: open questions, outside the binding target

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10.0 | 3 | 0 | 3 | 0 | 0 |

### Cold review — round 2 (Astra)

Same prompt, What-recently-changed slot noting the round-1 repairs (a routine refresh; same series).

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 malformed notes fall back to the definition; note with no definition; autolink | accept (consolidated) | decision 22; `_parse_glossary`, `BLOCKQUOTE_RE`, `ALSO_LABEL_RE`, `ALSO_ALT` | every blockquote in an entry is its note | definition prose saying "Also called"; wrapped notes |
| F2a catalog "every entry ends" | accept (outside target, routed) | `product-specs-catalog.md` § Glossary | "each entry's paragraph ends by linking …", net −5 bytes | the second-index rule; governing routing |
| F2b design-specs V3, V9 | supervisor decision (outside target) | `design-specs.md` checks V3, V9 | scope note: the Also called note's attribution and alternates are outside both checks | no platform requirements elsewhere |
| F3 cap pending | log only | Size Budgets | none | — |

Consolidation trigger fired once (r1 F1's repair became r2 F1): the class fix replaced per-variant recognition. Self-check: the guide's "malformed, repeated or not last" and "one paragraph and an optional final … note" still hold; docstring GLOSSARY TERMS updated in the same edit; no stale sentence (grep "Also called"). Tool test passes.

F1 divergent · past-a-rule · verified = 1.25 · F2 outside the binding target, routed (catalog part repaired; design-specs part for the supervisor) · F3 log-only, noise

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10.0 | 3 | 0 | 3 | 0 | 0 |
| r2 | 1.25 | 1 | 0 | 1 | 0 | 1 |

### Cold review — round 3 (Astra)

Prompt as round 2, What-recently-changed noting the round-2 repairs, Settled dispositions adding the two scheduled supervisor deferrals (the cap, design-specs V3/V9). Fidelity diff against the template: slot fills and deleted sections only.

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 note outside any entry becomes intro | accept | decision 22; `_parse_glossary` | reject a blockquote outside an entry | glossary intro and section orientation paragraphs |
| F2 moved entry hides its note change | accept | render convention 1; `render_glossary`, `render_tree` | diff a moved-in entry against its old home | move pairing in `check-changes`; a pure move adds no content change |

F1 is the r2 class again at the file level (the second time a parser repair was followed by a sibling): this time the rule is stated for the whole file, so no position is left unjudged. F2 was pre-existing for definitions; repaired for both. A first F2 render diffed the old definition with the destination's link definitions and marked an unchanged citation; caught on the committed design fixture page before handoff and fixed. Docstring render convention 1 and GLOSSARY TERMS updated in the same edits. Tool test passes (18 tests).

F1 divergent · past-a-rule · verified = 1.25 · F2 divergent · off-normal · verified = 3.75

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10.0 | 3 | 0 | 3 | 0 | 0 |
| r2 | 1.25 | 1 | 0 | 1 | 0 | 1 |
| r3 | 5.0 | 2 | 0 | 2 | 0 | 0 |

### Cold review — round 4 (Astra)

Prompt as round 3, What-recently-changed noting the round-3 repairs.

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 bare-address check narrower than claimed | accept | docstring GLOSSARY TERMS; `_parse_glossary` | one case-insensitive address check; docstring names what it covers | ordinary attribution punctuation (colons, times) |
| F2 markup in a note rendered inconsistently | log only | `also_called` | — | — |

Open question (leading space) answered: my round-2 prompt summary was loose; reworded for round 5 ("a note-like line with a leading space is judged by the form and rejected"). Tool test passes.

F1 divergent · past-a-rule · verified = 1.25 · F2 cosmetic, log-only, noise · open question: prompt wording, neither

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10.0 | 3 | 0 | 3 | 0 | 0 |
| r2 | 1.25 | 1 | 0 | 1 | 0 | 1 |
| r3 | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r4 | 1.25 | 1 | 0 | 1 | 0 | 1 |

### Cold review — round 5 (Astra)

Prompt as round 4, What-recently-changed noting the round-4 repair and rewording the leading-space summary.

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 address claim wider than the check | accept | docstring GLOSSARY TERMS; `BARE_ADDRESS_RE` | bound the claim to what Markdown links on its own | attribution text; case-insensitive check |
| F2 markup rendering (re-raise of r4 F2) | log only | — | — | — |

**Structured tier.** The consolidation trigger has now fired three times on one class (r1→r2, r2→r3, r4→r5: each repair of the note's validation drew a sibling), so the editing method changes:

- Invariants. **P1** every statement of what `validate` rejects about the note names a bounded set that the code checks entirely. **P2** no line of a glossary file escapes judgment: each is a heading, a definition line, a note line, or rejected. **P3** the note never changes how the definition is read, linked or diffed.
- Canonical ownership. The note's checks: owner the tool docstring GLOSSARY TERMS; dependents the guide's validator clause ("malformed, repeated or not last" — bounded by the shape above it, P1 holds), design decision 22 ("no link" — the bounded set is how the tool reads it), the release entry, the fixtures.
- Rule impact map for r5 F1: violates P1; owner GLOSSARY TERMS; dependents found by `grep -n "bare\|link in it\|no link"` over the tool, release documents, design spec and guide: the tool's two code comments, the release entry; all updated; the guide and decision 22 make no address claim.
- Sweep of P1 over every other note claim: "at most one" (second note, any label variant, `ALSO_LABEL_RE`), "last" (any non-note line after it), "after a definition" (empty paragraph), "on the form" (`ALSO_RE` over the joined lines), "outside an entry" (`term is None`): each is a finite check, fixture-tested. P2: `_parse_glossary`'s branches cover blank, `###`, `##`, bold paragraph, blockquote (inside or outside an entry), and paragraph lines; a paragraph line after a note is rejected; nothing else reaches the definition.

F1 divergent · past-a-rule · verified = 1.25 · F2 re-raise of a logged finding, noise

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10.0 | 3 | 0 | 3 | 0 | 0 |
| r2 | 1.25 | 1 | 0 | 1 | 0 | 1 |
| r3 | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r4 | 1.25 | 1 | 0 | 1 | 0 | 1 |
| r5 | 1.25 | 1 | 0 | 1 | 0 | 1 |

### Cold review — round 6 (Astra)

Prompt as round 5, What-recently-changed noting the bounded address claim. One finding, the r4 F2 cosmetic re-raise (log-only, disposition stands): noise. No new live finding in the binding target: stop rule (a), convergence by clean round.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10.0 | 3 | 0 | 3 | 0 | 0 |
| r2 | 1.25 | 1 | 0 | 1 | 0 | 1 |
| r3 | 5.0 | 2 | 0 | 2 | 0 | 0 |
| r4 | 1.25 | 1 | 0 | 1 | 0 | 1 |
| r5 | 1.25 | 1 | 0 | 1 | 0 | 1 |
| r6 | 0 | 0 | 0 | 0 | 0 | 1 |

Findings about my own previous repairs: r2 1 of 1, r3 1 of 2, r4 1 of 1, r5 1 of 1; every one in the note's validation, none in the guide text. Size at closure: guide 8,349 → 8,677 (+328; proposed cap 8,700); `product-specs-catalog.md` 10,498 → 10,493.

Unimplemented, for the supervisor: `design-specs.md` checks V3 (platform names only in known-difference notes) and V9 (glossary detail supported by linked items) read literally against a note's attribution and alternates; smallest fix a scope clause in each ("the Also called note excepted"); not in this slice's touch list. Follow-up outside the slice: `moved_item_status` compares a moved item against the catalog alone, ignoring `--base` (the glossary counterpart was fixed in r1).

### Sanity scan — `Guides/ProductSpecs/product-specs-catalog.md` (one-sentence edit, r2)

- `Managed-Updated-At`: 2026-10-21, not earlier than the edit.
- `\bhuman`, `🟡`, `- [ ]` (grep): 0 occurrences.
- No gates, Discussion or working-doc paths in the edited section; size 10,493 of 10,500.

### Maintenance retro — slice 6

Maintenance retro: DONE

1. Inventory: the glossary Also called note across the shape guide, one sentence of the catalog guide, the spec tool and its test; host-install-visible (managed guides and `tool.spec-tool`).
2. Bookkeeping: `Releases/unreleased.md` § Glossary alternate terms (skai#93), two entries, migration re-runnable (a `validate` run, a stop on any reported glossary blockquote); `CHANGELOG.md` one line under Unreleased, same change. `Managed-Updated-At` 2026-10-21 on both edited guides; the tool carries no managed header. Manifest: no asset added, moved or renamed (the new fixture folder `glossary-move/` is test material). README: lists what the shape guide covers only in general terms; no change. `internal/maintain-skai.md`: no new invariant.
3–4. Integration and installer: not touched.
5. Consistency: stale paths — none introduced (`git diff --stat` reviewed); every edited guide keeps its managed header; no gates in either guide; `grep -n "Also called"` over the docstring, guide, design spec and release entry agrees on form, placement and the no-link set; tool test 18 tests OK; SalesPro `product-specs/` validates at 0 issues.
6. Process suggestions:
   - `internal/maintain-skai.md` § Tool tests: "every rejection a tool's docstring names has a broken-fixture case, and a claim names a bounded set." Four of six rounds here were spent on validation claims wider than the code; a fixture per claimed case would have shown each before review.
   - The slice plan's "touch the catalog guide only if needed" left content-guide rules (catalog "entry ends", design-specs V3/V9) to be found by the reviewer; slice planning should list every guide whose glossary rules mention how an entry is built, so the touch list is decided before drafting.
   - When refreshing a cold-review prompt's What-recently-changed slot, name where the change is, not how it behaves: my loose summary ("accepts a leading space") came back as an open question in round 4.
