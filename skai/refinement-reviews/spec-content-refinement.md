# Spec Content Guides Refinement

Working document for target 2: the content guides of both spec types, refined together. Standards: `skai/refinement-reviews/requirements-system-design.md` (P2, P4, P5, P8, P10, Artifacts, Decisions and Size Budgets 2026-10-18, live render), `design-specs-design.md` (decisions 1, 6, 7, 9 as amended, Amendments 2026-10-18, Size Budgets, live render), `spec-format-design.md` (decisions 9, 12–16). Shared shape guide cited, never restated, not edited: `Guides/Core/spec-file-shape.md`. Findings log: `skai/refinement-reviews/spec-content-findings.md`. Tool: `Bin/spec-tool.py` (repaired concurrently; not edited here); fixtures: SalesPro `working-docs/requirements-process/fixtures/`.

| File | Start | Cap |
|---|---|---|
| Guides/Requirements/requirements-catalog.md | 18,127 | 10,500 |
| Guides/Requirements/requirements-artifacts.md | 11,674 | 6,500 |
| Guides/DesignSpecs/design-specs.md | 19,554 | 15,000 |
| Guides/DesignSpecs/design-specs-artifacts.md | 9,030 | 5,000 |
| Group | 58,385 | 37,000 |

## Pre-review tool facts (2026-10-18, tool md5 d272290d…, 1,459 lines)

- `validate catalog package/proposed-product-specs` → 5 files, 0 issues, exit 0.
- `check-changes --catalog --drafts --authoring` exists and runs: on the fixture package it reports 12 unlisted changes (the fixture's list is partial), one `path:line: message` per failure, exit 1.
- `render` without `--authoring` writes `product-specs-review.html` into the package folder but carries no card or justifications (0 `class="why"`); `--no-authoring` is not accepted yet. Both are pending in the tool pass (amended spec 9).
- `render-request` with `<request>/proposed-product-specs` writes `request-review.html` beside `request.md`, exit 0.
- A `glossary.md` with `##` sections fails validation: "glossary entry must be a '###' heading, not a section or bold paragraph" and "not in alphabetical order" (alphabetical across the whole file). Design-specs-design decision 5 sections the glossary Global, Shared, then per family. **Architecture contradiction → supervisor decision** (see below).
- An index line ending `(uses: [SYNC-04])` validates.

## Dependents in read-only siblings (targets 3 and 4)

Found by grep; not edited here, listed so the next targets inherit them:
- `requirements-authoring.md:33` and `design-specs-artifacts`-mirroring `design-specs-authoring.md:32`: package table rows `change-requests/requirements-<nnn>.md` → folders `change-requests/<nnn>/request.md`.
- `requirements-authoring.md:216-219`, `design-specs-authoring.md:171`: "raised by promotion" → filed by any downstream consumer; triage outcome recorded on the request.
- `requirements-promotion.md:233-237`, `design-specs-promotion.md:191-193`: "Promotion alone raises these" → promotion is one filer among several.
- `design-specs-authoring.md:274`: "changed text inline" → change items carry no inline text.
- Authoring and promotion artifacts: review-page link at the top (new; no current text).

## Pre-review pass (known deltas, decided by the supervisor)

Clusters, one per file, each with self-check and sanity scan below. Deltas applied in every cluster: file-shape content moves out to a citation of `spec-file-shape.md`; glossary entries are headings and every term occurrence is linked; an app's index lists the feature files it offers; change items hold only ID, type, identity, justification and touched files; the authoring and promotion artifacts link the rendered review page at the top; change requests are folders `change-requests/<nnn>/` with `request.md` and optional drafts, filed by any downstream consumer, triaged by authoring; the live-render rule; prose says "product specs" for the catalog while file, guide, skill and addendum names stay.

### Cluster 1 — requirements-catalog.md (18,127 → 10,468; cap 10,500)

Moved out to a citation of `spec-file-shape.md`: the requirement file shape and its example, the known-difference and retired-requirement forms, link style, ID format and anchors, index-line form, glossary entry form. Prose now says "product specs" for the catalog and "requirement" for the item. Added: an app's index lists the feature files it offers; glossary entries linked at every occurrence (`link-terms`), terms in sentence case; one item per claim with rules and tables for enumerations (❌ nine requirements for seven stages); modify-vs-retire applies to rules and table rows and is preceded by `references`; catalog root from the Integration block, never a literal path. Removed with the shape move: the legacy "match the file's unpadded IDs" clause (the validator requires two digits; logged as superseded). Trims paid for the cap: scope decision tree folded into one sentence; Self-check folded into Required and Nothing that decays; one Forbidden example pair dropped; Cross-references descriptions shortened.

Self-check: no contradiction with adjacent text or the shape guide (grep `.<NN>`, `## <PREFIX>`, bold glossary, unpadded, `skai/requirements/`: 0); no stale sentence teaching the old shape (same greps; "Known difference —" form present only by citation); the rules moved away from their point of use are the shape rules, by the supervisor's decision, each cited where the agent needs it (Requirements, IDs, Indexes, Glossary); no enforced rule weakened — "Cross-references are mandatory" survives as "Cite dependencies inline, where they apply", and the retire-in-place ❌s survive.

Sanity scan: Managed-Updated-At 2026-10-18 = today (header read) → ok; gates n/a (content guide); `grep '\bhuman'` → 0; terms (`Next Command`, `checkpoint`) → 0; markers (`🟡`, `- [ ]`) → 0; stack mismatch (xcode, gradle, swift, ios) → 0; working-doc paths → 0; fences 4 (two blocks, balanced); relative links resolve (shape guide, artifacts, authoring, promotion exist).

### Cluster 2 — requirements-artifacts.md (11,674 → 6,498; cap 6,500)

Change items now hold ID, type, identity, justification and touched files; *Showing the diff* and the **Description** field are gone — the rendered page shows the difference under each justification. The package tree adds `product-specs-review.html`, `change-requests/<nnn>/request.md` with optional drafts beside it, and `request-review.html`; the review-page paragraph carries the live-render rule and the link-at-the-top rule for the authoring, promotion and request artifacts. Change requests: filed by any downstream consumer for any reason against the open package or the catalog, triaged on the request by authoring, proposer never edits the package; `request.md` form shown (status, response, title, Goal, Requested Changes). `check-changes` named as the list-matches-projection check (verified: index line riding in Touches accepted, 0 issues; stray-entry branch to verify at round close with a truly unchanged item). Trims paid for the cap: one two-entry change-item example in place of two four-entry ones; the request example cut to its skeleton after the first entry; C7/C8 note to one sentence; Cross-references section dropped (the intro routes to the same four guides).

Open for the supervisor (recorded, not resolved here): the request's drafts folder is written as `proposed-requirements/**`, mirroring the package, while the tool reads `<request>/proposed-product-specs` or `proposed-design-specs` only; and `render` now looks for `product-specs-authoring.md` in the package folder by default (tool md5 74ce8dad…, 1,485 lines), so a package named per "file names stay" needs `--authoring`.

Self-check: no contradiction with the catalog guide (modify-vs-retire has one home, pointed at from Type) or the shape guide (change-item fields match its Change Items paragraph); stale-text greps (`Description`, `~~`, `struck`, `requirements-<nnn>`, `only raiser`, `promotion raises`, `Showing`): 0; no rule moved from its point of use — the request format sits with the lifecycle, the item format with its field rules; nothing weakened — "Proposed blocks readiness" and "proposer never edits the package" are stated as rules.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0 (the request skeleton's `- R1` is a list item, not a checkbox); stack 0; working-doc paths 0; fences 8 (four blocks, balanced); links resolve (shape guide, catalog, authoring).

### Cluster 3 — design-specs.md (19,554 → 14,987; cap 15,000)

Moved out to a citation of `spec-file-shape.md`: the Spec File Shape section and its example, index naming, sub-ID form, link style, ID format; `.<NN>` → dashes everywhere (`UI-LIST-01-02`, `UI-FORM-01-02`). Items section keeps the design-spec judgment: opening sentence identifying the subject and linking the requirement (one ✅ example), data in tables, contract unit, conditions, known differences, pending references, links to draft requirements, every binding claim has an ID; Citing by Reference unchanged. Glossary: entries linked at every occurrence (`link-terms`), sentence case; the sectioning rule (Global, Shared, per family) retained from design-specs-design decision 5 — **the validator rejects it; supervisor decision below**. Gap routing: a change request against the open product spec package or the catalog (decision 1 as amended) replaces "authoring's gap procedure". Verification Checks lead: the tool's `validate` runs over the projection before the ten checks, a failure blocks; V8 keeps the judgment part (renumbering, reuse, moves, prefixes) now that the validator rejects duplicate IDs. Modify vs. Retire: `references` before either. Trims paid for the cap: TOC removed; ownership table to prose; the index-line and glossary fenced examples replaced by inline ✅ quotes; tree comments dropped; parentheticals and routing tails shortened; "Motion needs words" pointer dropped (the Motion bullet and V10 carry it).

Self-check: no contradiction with the artifacts guide (gap → change request; `move` items; retired rule form) or the shape guide (dashes, `###` entries, tables keyed on first column); stale-text greps (`.<NN>`, `.0N]`, bold glossary entries, "sibling requirements package", "gap procedure", "plain lists", "Sub-IDs", "Index Naming"): 0; rules moved away from point of use are the shape rules only, cited at Items, IDs, Indexes and Glossary; nothing weakened — every V-check keeps its scope, "unavailable access blocks", "a pending global pattern blocks" and "never link into the design tool" survive.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack: "iOS" appears once inside a ❌ example ("a standard iOS tip bubble") → false positive, intentional; working-doc paths 0; fences 2 (one block); links resolve (shape, catalog, artifacts, authoring, promotion, Figma guide). Rewrapped three over-long lines after editing (no byte change).

### Cluster 4 — design-specs-artifacts.md (9,030 → 4,991; cap 5,000)

Parallel to cluster 2: change items hold ID, operation × object, identity, justification, touched files; *Showing the Diff* and **Description** gone; `sub-item` → `rule` to match the shape guide (same thing; design-specs-design 9 says sub-item); `.<NN>` → dashes. Package: `design-specs-review.html`, `change-requests/<nnn>/request.md` with optional `proposed-design-specs/**`, `request-review.html`. Change requests: any downstream consumer, against the open package or the specs, triaged on the request, proposer never edits. Because the cap leaves ~4,350 bytes of content, the guide states the design-spec-specific rules in full (independence, operation × object, move identity and incoming-link drafting, granularity, one `move` example, who files) and cites `requirements-artifacts.md` for the mechanics it mirrors (package tree, review-page render and link rules, Source list, request form and lifecycle), as design-specs-design's Guide Shape allows. Dropped as duplicates of design-specs.md: the frames/nodes sentence (Writing Style owns it) and the verified-cleanup carve-out (Purpose owns it).

Self-check: no contradiction with design-specs.md (Modify vs. Retire anchor resolves; retired form matches Stability) or the product spec guide (same fields, same lifecycle by citation); stale-text greps (`Description`, `~~`, `struck`, `design-specs-<nnn>`, `Only promotion`, `sub-item`, `.0N]`, `Showing`, `frames, nodes`): 0; rules moved: the shared mechanics now live in the product spec guide by citation — a reader of this guide is sent there explicitly in the intro; nothing weakened — "proposer never edits", "Proposed blocks readiness", "files never retire" stand.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack 0; working-doc paths 0; fences 4 (two blocks); links resolve (shape, requirements-artifacts, design-specs and its `#modify-vs-retire` anchor, present at line 132).

### Pre-review pass totals

| File | Before | After | Cap |
|---|---|---|---|
| requirements-catalog.md | 18,127 | 10,468 | 10,500 |
| requirements-artifacts.md | 11,674 | 6,498 | 6,500 |
| design-specs.md | 19,554 | 14,987 | 15,000 |
| design-specs-artifacts.md | 9,030 | 4,991 | 5,000 |
| Group | 58,385 | 36,944 | 37,000 |

### Pre-review verification (tool md5 74ce8dad…, 1,485 lines; the tool changed twice during the pass)

- `validate catalog drafts` on the fixtures: 5 files, 0 issues. Probe catalog + package (index line, glossary, two feature files): 7 files, 0 issues; an index line ending `(uses: [SYNC-04])` validates.
- `check-changes`: index line and new file riding in the file entry's `Touches` → 0 issues; an entry naming an unchanged item → "R3 names item REMIND-02, which is unchanged", exit 1. Both claims in the artifacts guides hold.
- `link-terms` on a scratch copy with one unlinked "pending reminder": validate reports the unlinked use; `link-terms` → "linked 1 term uses"; the occurrence is now `[pending reminder][g-pending-reminder]`.
- `render`: with `product-specs-authoring.md` in the package folder the page carries justifications (`class="why"` > 0) without `--authoring`; `--no-authoring` accepted; default output name `product-specs-review.html` in the package folder. `render-request` with `<request>/proposed-product-specs` writes `request-review.html` beside `request.md`.
- Glossary with `##` sections: rejected (see supervisor decision 1).

### Maintainer retro (pre-review pass)

Inventory: four content guides rewritten to the shared shape and their caps (host-install-visible: guide content; no asset added, moved or renamed). CHANGELOG `## Unreleased` carries one net entry with migration steps for open packages; README rows for the four guides and the shape rows updated (links, not bare paths); `assets.manifest.json` needs no change (ids and paths unchanged, no date field); every edited managed file carries `Managed-Updated-At: 2026-10-18`. Gates: none of the four guides has gates (no `⏳ GATE:` lines, no `## Gates` needed). Terminology: `grep "Next Command"` over both guide folders → 0. Markers: `- [ ]`/`🟡` in the four guides → 0. Working-doc paths: 0. Change-package verification (artifact formats changed): request paths use the type folder (`change-requests/<nnn>/request.md`), no discovery globs; coexistence, reopen, promotion ordering and archival recovery are the authoring/promotion guides' rules and are unchanged by this pass; migration guidance for open packages is in the changelog entry. Guide-addendum contract: footers unchanged in all four guides, lookup names unchanged. Stale references in read-only siblings (for targets 3 and 4): `requirements-authoring.md:33` (`change-requests/requirements-<nnn>.md`), `requirements-baseline.md:19` ("§ Root index" — now `### Indexes route`), plus the dependents listed above. Retro complete; no misses inside the four targets.

## Supervisor Decisions After The Pre-Review Pass (2026-10-18)

1. Glossary sections: option (b). spec-format-design decision 4 now allows optional `##` sections in `glossary.md`, alphabetical within each; design-specs.md keeps its sectioning paragraph; the tool pass makes the validator accept it — verify at round close.
2. Package names: the tool will accept the legacy package names until the rename pass; a change request's drafts folder is `proposed-product-specs/` now (artifacts guide tree line changed, 6,498 → 6,499 bytes); `render` needs no flag once the tool change lands — verify at round close.
3. Hygiene: design-specs-design decision 9 no longer says "changed text inline" and says "rule" for "sub-item".

Round 1 commissioned over the current text with these in the settled slot. Series A: full cold review, Codex gpt-6-astra, standard charter, the four guides as the binding target, the two standards plus the shape standard as the spec.

## Round 1 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r1/prompt.txt` (diffed clean against the template: slot replacements and four deleted slot sections only), report `scratchpad/r1/review-r1.md`. Six findings, three open questions.

### Finding matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 Request filing boundary: "for any reason" against an open package vs "a package defect is not a request"; design artifacts guide's independence rule omits the change-request link (design-specs-design 1, 9; req-sys P10) | accept | requirements-artifacts § Change Requests; design-specs-artifacts § The Package, § Change Requests | Sharpen the exception to promotion's own failed check; add the change request to the permitted cross-package links | Promotion still blocks on its own failures; proposer never edits the package | net 0 (trim consumer lists) |
| F2 `check-changes` keys a rule identity to its parent item, so a nonexistent rule passes (spec-format 15) | routed to the tool pass | tool; design-specs-artifacts § Spec Change Items claim | Tool: compare the typed target; guide unchanged (its claim equals spec 15's item-level check) | Rule entries still attach to the parent | 0 |
| F3 Renderer's retired-item branch shows only statements, dropping the old rules and tables (spec-format 12, 14) | routed to the tool pass | tool | Tool: render the whole removed contract | Canonical retired items carry only the explanation | 0 |
| F4 V9 "no unnumbered binding prose" reads as rejecting the required statement (design-specs-design 7, 10) | accept | design-specs § Verification Checks V9 vs § Items | Clause becomes "orientation prose binds nothing" | Statement and requirement link stay required; prose after rules/tables stays the shape guide's | ≤ 0 |
| F5 Request example omits the `request-review.html` link the package section requires (req-sys rendered page rule) | accept | requirements-artifacts § Change Requests example | Add the link line under the title; trim the field enumeration above | Status and response above the title; metadata-only entries | net 0 |
| F6 Modify vs. retire covers tightening, not relaxation | log only | both content guides § Modify vs. retire | On recurrence: "a changed promise in either direction retires and adds" | Clarifications keep the ID; reference sweep mandatory | — |

Open questions (neither): requests without drafts render as a card alone (standard, spec-format 13); design-specs-design 9 residue "whose description summarizes it" — standard hygiene for the supervisor.

### Round score

> F1 divergent · off-normal · speculative = 1.875 · F2 routed to the tool, neither · F3 routed to the tool, neither · F4 divergent · normal · speculative = 2.5 · F5 divergent · off-normal · speculative = 1.875 · F6 log-only, noise

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 6.25 | 3 | 0 | 3 | 0 | 1 |

### Round 1 repairs — cluster A (F1, F5; both artifacts guides)

requirements-artifacts.md 6,499 → 6,439: the package-defect exception now reads "Promotion's own failed check on the package is not a request: it blocks and the package returns to authoring"; "design authoring" dropped from the consumer list (it files through design specs); the request example gains `[Review page](request-review.html)` directly under its title, funded by dropping the field enumeration the example shows. design-specs-artifacts.md 4,991 → 4,996: the independence sentence adds "and a change request filed against that package"; the same exception sharpening; funded by "(`## Spec Changes`)", "(root index, glossary, three folder indexes)", "`C4` the package archived" and dropping "the UI Map" from the consumer list (it is a downstream consumer; "any downstream consumer" still covers it).

Self-check: no contradiction — "for any reason" and the promotion exception no longer overlap, and the design guide's independence rule now names both permitted cross-package links (design-specs-design 1, 9); no stale sentence (`grep "defect in the package\|package defect"` → 0 in both guides); no rule moved — the exception sits where the filing rule is; nothing weakened — promotion still blocks on its own failure, the proposer never edits the package, independence otherwise holds.

Sanity scan: Managed-Updated-At 2026-10-18 → ok (same day); gates n/a; `\bhuman` 0; terms 0; markers 0; stack 0; working-doc paths 0; fences 8 / 4 (balanced); links unchanged and resolving; long lines: only the print line and addendum footer.

### Round 1 repairs — cluster B (F4; design-specs.md)

design-specs.md 14,987 → 14,991: V9's last clause "no unnumbered binding prose" → "orientation prose binds nothing", matching Items ("A `##` part … may open with one nonbinding orientation line; anything that says what shows or when belongs under an item") and V1 ("Nonbinding orientation and routing are `V9`'s").

Self-check: no contradiction — Items, V1 and V9 now use the same word for the same prose; no stale sentence (`grep unnumbered` → 0); rule not moved; nothing weakened — the statement and requirement link stay required, and prose after rules or tables stays the shape guide's rejection.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack: the one intentional "iOS" ❌ example; working-doc paths 0; fences 2; links unchanged.

### Round 1 verification (tool md5 0eeb87c2…, 1,508 lines)

- Sectioned glossary (`## Global`, `## List Screens`, `###` entries alphabetical within each): `validate` → 5 files, 0 issues. Ruling 1 landed; design-specs.md's sectioning paragraph is accurate.
- `render` with no flag on a package named `requirements-authoring.md` + `proposed-requirements/`: writes `product-specs-review.html`, justifications present. Ruling 2 landed. `render-request` with `proposed-product-specs/` inside that package: `request-review.html` written, 1 modified item.
- F2 probe: `retire requirement: [REMIND-01-99]` (no such rule) → `check-changes` 0 issues. Tool gap confirmed; routed.
- F3 probe: `REMIND-01` retired with its rule removed → the page's retired card carries no old rule text. Tool gap confirmed; routed.
- Caps: 10,468 / 6,439 / 14,991 / 4,996 = 36,894 of 37,000.

### Round 1 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 request boundary and omitted cross-package exception | closed | Exception is promotion's own failed check (both guides); design independence rule names the change request; greps for the old wording → 0 |
| F2 `check-changes` ignores the rule and operation of an entry | routed to the tool pass | Reproduced: nonexistent rule 99 passes; the guides' claim is spec 15's item-level check and stands |
| F3 retired item's old contract missing from the page | routed to the tool pass | Reproduced: old rule text absent from the retired card |
| F4 V9 "no unnumbered binding prose" | closed | "orientation prose binds nothing", same word as Items and V1 |
| F5 request example lacked the review-page link | closed | `[Review page](request-review.html)` under the title; funded by dropping the field enumeration |
| F6 modify vs. retire silent on relaxation | logged | No strand observed; standing blocked route; on recurrence: "a changed promise in either direction retires and adds" |
| Open: requests without drafts render as a card alone | open question | Standard (spec-format 13); the typed list is on `request.md` |
| Open: design-specs-design 9 residue "whose description summarizes it" | open question | Standard hygiene for the supervisor |

Round 2 to be commissioned over the current text (series A continues: same files, standard, scope and charter; the round-1 dispositions join the settled slot as routine refreshes).

## Supervisor Rulings After Round 1 (2026-10-18)

Round 1 accepted. F2 and F3 are with the tool pass. Spec-format decision 13 amended: a request without drafts shows one card per Requested Changes entry (identity, type, justification) after its card — requirements-artifacts.md now says "without drafts the page lists each requested change" (6,439 → 6,484). design-specs-design decision 9's "description summarizes it" phrase is fixed. Round 2 commissioned over the current text; series A continues (routine refresh of the settled slot).

## Round 2 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r2/prompt.txt` (diffed clean: slot replacements and the four deleted slot sections), report `scratchpad/r2/review-r2.md`. Four findings. The reviewer saw the tool mid-repair and reports round-1's F2 and F3 as present in its final read.

### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 Layout's "restructures move, never delete, files" vs Stability's `move` items and the artifacts guide's "only items move" (design-specs-design 6, 9) — a pre-review trim artifact | accept | design-specs § Layout vs § Stability, artifacts § Spec Change Items | Delete the clause; Stability owns the rule | Item IDs, explicit `move` entries, incoming-link repair, files never retire | −40 |
| F2 Request identity when no draft of the target exists | log only | artifacts guides § Change Requests | On a strand: sharpen the Identity rule for requests in the product spec guide | Drafts stay optional | — |
| F3 Changes riding in `Touches` carry no justification on the page (intro, index line) | routed to the tool pass | tool | Carry the `Touches` association into rendering | Granularity; no duplicate entries | 0 |
| F4 Index line retargeted with unchanged text renders as unchanged, so `check-changes` would reject a correct entry | routed to the tool pass | tool | Compare the line's resolved target (spec-format 11) | Path rebasing stays ignored | 0 |

### Round score

> F1 divergent · off-normal · speculative = 1.875 · F2 log-only, noise · F3 routed, neither · F4 routed, neither

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 6.25 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 1.875 | 1 | 0 | 1 | 0 | 1 |

Who the findings are about: the one live finding is damage from the pre-review trim of Layout (not a round-1 repair); the consolidation trigger has not fired.

### Round 2 repair — one cluster (F1; design-specs.md)

design-specs.md 14,991 → 14,951: Layout now ends "Create all three folders and indexes immediately." The move rule has one home (Stability: "Moves never renumber; restructures use `move` items") and the artifacts guide's "Only items move … files never retire".

Self-check: no contradiction (grep "restructure|never delete|move": only Stability, the glossary's "entries move with their items", the motion example and V8 remain); no stale sentence; the rule did not move — it was a duplicate, now deleted; nothing weakened — "files never retire" stays in the artifacts guide.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack: the one intentional "iOS" ❌ example; working-doc paths 0; fences 2.

### Round 2 verification (tool md5 c3fdc8eb…, 1,534 lines)

- F4 reproduced: an index line retargeted from `reminders.md` to `alarms.md` with unchanged text renders `modified: 0`. Routed.
- F3: reviewer-verified in the implementation (`c.keys & keys and c.why`; intro rendering without justification); my page probe was inconclusive (justifications in the region could not be attributed to the index line). Routed on the reviewer's evidence.
- Caps: 10,468 / 6,492 / 14,951 / 4,996 = 36,907 of 37,000.

### Round 2 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 Layout told the operator to move files | closed | Clause deleted; greps above |
| F2 request identity without a draft | logged | No occurrence; standing stop; sharpen the product spec guide's Identity rule on a strand |
| F3 `Touches`-riding changes lose their justification on the page | routed to the tool pass | Reviewer's implementation read |
| F4 index retarget invisible to the renderer and so to `check-changes` | routed to the tool pass | Reproduced |

Stop rule not met: round 2 produced one live finding and was repaired after. Round 3 to be commissioned over the current text, series A.

## Supervisor Ruling After Round 2 (2026-10-18)

Round 2 accepted; F3 and F4 with the tool pass. Round 3 commissioned over the current text, series A, settled slot refreshed with the round-2 dispositions (routine refresh).

## Round 3 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r3/prompt.txt` (diffed clean), report `scratchpad/r3/review-r3.md`. Three findings.

### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 "a failure blocks" (design-specs § Verification Checks lead; shape guide validate row) is unqualified, while the catalog guide exempts pre-existing defects (req-sys P2) and design-specs § Purpose excludes untouched canonical files (design-specs-design 10); the tool reports every root's shape faults, so an untouched malformed canonical file blocks a clean package | supervisor decision (architecture: req-sys P2 and design-specs-design 10 vs spec-format 8 and 10) | both content guides; shape guide; tool; spec-format 8, 10 | Once decided: qualify the blocking clause to the package's review scope (touched files whole plus conflicts the package introduces), tool filters accordingly | Touched files checked whole; cross-file conflicts introduced by the package still block | ~0 (replace the repeated scope wording) |
| F2 design-specs-artifacts § The Package "drawing location is never referenced" (a pre-review trim dropped "by specs") contradicts Writing Style's "package prose may name frames, nodes and code files" | accept | design-specs-artifacts § The Package vs design-specs § Writing Style | Delete the clause; the content guide owns the restriction | The two permitted cross-package links; the ban on design-tool references in spec text | −41 |
| F3 per-folder glossaries (design-specs-design 5) are unseen by `validate`, `link-terms` and `render`, which read the root `glossary.md` only (spec-format 4 names one file) | routed to the tool pass; standard-level note | tool; spec-format 4 vs design-specs-design 5 | Tool discovers projected per-folder glossaries | Sections, ordering, governing-item exemption | 0 |

### Round score

> F1 divergent · normal · verified = 5 (live in the binding target; awaiting the decision) · F2 divergent · normal · speculative = 2.5 · F3 routed to the tool, neither

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 6.25 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 1.875 | 1 | 0 | 1 | 0 | 1 |
| r3 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |

Who the findings are about: F2 is pre-review trim damage (second such finding: r2 F1, r3 F2 — both from the pre-review compression, not from round repairs; consolidation trigger not fired, but noted as a trim-damage class: sweep the four guides for clauses that lost a qualifying phrase before round 4). F1 is original to the standards.

### Round 3 repair — one cluster (F2; design-specs-artifacts.md)

design-specs-artifacts.md 4,996 → 4,954: "and drawing location is never referenced" deleted; the independence sentence names only the two permitted cross-package links.

Self-check: no contradiction (design-specs.md § Product Language Only, § Items "never link into the design tool" and V3 own the restriction on spec text; Writing Style permits package prose to name frames and nodes); no stale sentence (`grep "drawing location"` → 0); no rule moved — it had one home already; nothing weakened — spec-text restrictions untouched.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack 0; working-doc paths 0; fences 4.

Trim-damage sweep (the class behind r2 F1 and r3 F2): re-read every sentence the pre-review pass shortened for a dropped qualifier — requirements-catalog.md (Purpose, Scopes, Layout, Requirements, IDs, Writing style), requirements-artifacts.md (Package, items, requests), design-specs.md (Purpose, Layout, Items, IDs, Writing Style, checks), design-specs-artifacts.md (all). Found none beyond F2 ("only items move" and "never link into the design tool" now stand once each). Recorded as visual review; 0 further occurrences.

### Round 3 verification (tool md5 18b16f6d…)

- F1 reproduced: an untouched canonical `features/broken.md` (item without a statement) fails `validate catalog drafts` with exit 1 while the package's drafts are clean.
- Caps: 10,468 / 6,492 / 14,951 / 4,954 = 36,865 of 37,000.

### Round 3 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 validation blocking vs the package's review scope | supervisor decision — open | Standards conflict (P2, design-specs-design 10 vs spec-format 8, 10); reproduced in the tool; guides unchanged pending the ruling |
| F2 package-wide drawing-location ban | closed | Clause deleted; the content guide owns the restriction |
| F3 per-folder glossaries unseen by the tool | routed to the tool pass | Implementation reads `glossary.md` at the root only (reviewer's read; spec-format 4 names one file) |

Stop rule not met: F1 is live and awaits a ruling; F2 was repaired after the round.

## Supervisor Rulings After Round 3 (2026-10-18)

F1: the scoped reading. spec-format 8 and 10 now say a failure blocks only when it is in a file the package holds or is a conflict the projection introduces; a per-file fault in an untouched canonical file is reported, never blocks, and becomes a change request; the tool pass implements the filter. The shape guide's validate row is left alone (closed target; the consistency pass aligns it). F3: with the tool pass — every `glossary.md` under the root is read as one glossary; design-specs.md keeps the per-folder split.

### Round 3 repair — cluster F1 (both content guides)

design-specs.md § Verification Checks lead: "run `validate` over the drafts projected on canon: a fault in a file the package holds, or a conflict the projection introduces, blocks; a fault in an untouched canonical file is reported and becomes a change request. Then these ten checks, enumerated only here, over the scope in *Purpose*." (the repeated scope wording replaced by the pointer). requirements-catalog.md § Purpose: "a pre-existing defect never blocks a package but becomes a change request". The artifacts guides make no blocking claim. Funded by: "target" dropped from the organize-by list; "(an 8:00 PM cutoff)", "(*Restatement*)" on V1 and "(*Copy*)" on V4 dropped (the check names carry the section names). Sizes: catalog 10,468 → 10,489; design-specs 14,951 → 14,990.

Self-check: no contradiction — Purpose's "only a contradiction that would make the write inconsistent blocks" and the new lead say the same thing; the catalog's exemption now names the route (change request) the artifacts guide defines; no stale sentence (`grep "a failure blocks"` → 0 in the four guides; the shape guide's row is deliberately untouched per the ruling); no rule moved; nothing weakened — touched files are still checked whole, conflicts the package introduces still block.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack: the one intentional "iOS" example; working-doc paths 0; fences 4 / 2. Over-long merged lines rewrapped (no byte change).

Round 4 commissioned over the current text, series A, settled slot refreshed with the round-3 dispositions and the two rulings.

## Round 4 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r4/prompt.txt` (diffed clean), report `scratchpad/r4/review-r4.md`. Two findings, one open question (`check-changes` compares target coverage, not the declared operation — the standard's own description; not a finding).

### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 requirements-catalog § Purpose "a pre-existing defect never blocks a package" is broader than the ruling: a fault inside a file the package holds blocks (spec-format 8 as amended; the tool marks only faults outside the drafts as notes). My round-3 wording — the consolidation trigger has fired once | accept | requirements-catalog § Purpose | "a defect in an untouched canonical file never blocks a package but becomes a change request" | Held files and projection conflicts block; untouched canonical faults never do | +14, funded by "in that order" (−15) |
| F2 design-specs § What Belongs Here "every app named by the requirements root index" — the catalog's root index holds no app inventory; apps are in `apps/_apps.md` | accept (deterministic dangling reference; reviewer logged it) | design-specs § What Belongs Here vs requirements-catalog § Indexes route | "every app in the catalog's `apps/` index" | Rules apply to every app; single-app verification recorded as an assumption | −7 |

### Round score

> F1 divergent · normal · verified = 5 · F2 divergent · normal · speculative = 2.5 (accepted as a dangling reference rather than logged)

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 6.25 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 1.875 | 1 | 0 | 1 | 0 | 1 |
| r3 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |

Who the findings are about: F1 is my round-3 repair (consolidation trigger fired once — the repair was one clause and is now aligned to the ruling's exact words; a second firing moves to the structured tier). F2 predates the pass (the original guide had the same sentence).

### Round 4 repair — cluster 1 (F1; requirements-catalog.md)

10,489 → 10,488: "a defect in an untouched canonical file never blocks a package but becomes a change request; release migrations are separate", funded by "in that order" (the scope list is ordered on the page).

Self-check: no contradiction — matches design-specs § Verification Checks' lead word for word in substance and the ruling; no stale sentence (`grep pre-existing` → 0); no rule moved; nothing weakened — a fault in a held file is no longer exempted.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack 0; working-doc paths 0; fences 4.

### Round 4 repair — cluster 2 (F2; design-specs.md)

14,989 → 14,983: "Specs apply to every app in the catalog's `apps/` index."

Self-check: no contradiction — the catalog guide's Layout tree and Indexes route describe `apps/_apps.md` as the catalog of apps; no stale sentence (`grep "root index"` in design-specs.md → only the specs' own root index at line 66); no rule moved; nothing weakened — "Rules apply to every app" (Mechanism Is the Developer's) stands.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack: the one intentional "iOS" example; working-doc paths 0; fences 2.

### Round 4 verification (tool md5 2427b61f…, 1,572 lines)

- Scoped validation landed: an untouched canonical `features/broken.md` → "note: … BROKEN-01 has no statement; 8 files, 0 issues, 1 notes outside the projection", exit 0. The same fault copied into a held draft → 1 issue, exit 1. Both content guides' wording verified against the tool.
- Caps: 10,488 / 6,492 / 14,983 / 4,954 = 36,917 of 37,000.

### Round 4 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 catalog exemption broader than the ruling | closed | "a defect in an untouched canonical file never blocks"; tool probe: held-file fault blocks, untouched does not |
| F2 "every app named by the requirements root index" | closed | Now "every app in the catalog's `apps/` index"; the catalog guide's Layout names `_apps.md` as the catalog of apps |
| Open: `check-changes` checks coverage, not the declared operation | open question | Spec-format 15 describes coverage; the guides claim no more |

Stop rule not met: both findings were repaired after the round. Round 5 to be commissioned over the current text, series A. Consolidation trigger count: one (r3 F1 → r4 F1).

## Supervisor Ruling After Round 4 (2026-10-18)

Round 4 accepted. The `check-changes` open question goes to the tool pass: it will verify the declared operation as well as coverage; spec-format 15 stands. Round 5 commissioned over the current text, series A, settled slot refreshed (routine).

## Round 5 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r5/prompt.txt` (diffed clean), report `scratchpad/r5/review-r5.md`. One finding; two tool confirmations under open questions, both already with the tool pass.

### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 `platform` opened as "invariants that hold regardless of app or feature", which domain invariants also satisfy, so "choose the first that fits" can route an entity invariant to `platform` (req-sys P3: domain rules are behavioral placement; wording carried over from the original guide) | accept | requirements-catalog § Scopes | Define `platform` by its contracts: "protocol, infrastructure and format contracts, the same for every app and feature" | Scope order; domains own entities and transitions; feature vs. domain test | −2 |
| Tool: unlinked-term occurrences in untouched canon still block (filter downgrades shape issues only) | already routed (r3 F1 tool part) | tool | Tool pass | Guides' scoped rule stands | 0 |
| Tool: `check-changes` special-cases `sub-item|known-difference` while the design vocabulary is `rule` | already routed (r1 F2, r4 ruling) | tool | Tool pass | Guides' operation × object vocabulary stands | 0 |

### Round score

> F1 divergent · normal · speculative = 2.5 · the two tool items are confirmations of work already assigned, neither

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 6.25 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 1.875 | 1 | 0 | 1 | 0 | 1 |
| r3 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r5 (A) | 2.5 | 1 | 0 | 1 | 0 | 0 |

Who the findings are about: F1 is original wording, not a repair. Consolidation trigger count stays at one.

### Round 5 repair — one cluster (F1; requirements-catalog.md)

10,488 → 10,486: the `platform` bullet now reads "protocol, infrastructure and format contracts, the same for every app and feature"; the example is unchanged.

Self-check: no contradiction — the domains bullet keeps entities, invariants and transitions, and the feature-vs-domain test is untouched; no stale sentence (`grep "regardless"` → 0); no rule moved; nothing weakened — the category is now defined by what it contains rather than by a property domain rules share.

Sanity scan: Managed-Updated-At 2026-10-18 → ok; gates n/a; `\bhuman` 0; terms 0; markers 0; stack 0; working-doc paths 0; fences 4.

### Round 5 verification (tool md5 82c8bc7e…)

No tool claim in the guides changed this round; the reviewer's read-only validation of both fixture sets passed with the untouched legacy file reported as a note. Caps: 10,486 / 6,492 / 14,983 / 4,954 = 36,915 of 37,000.

### Round 5 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 `platform` definition overlapping domain invariants | closed | Bullet defines the category by its contracts; scope order and the feature-vs-domain test unchanged |
| Tool: unlinked-term faults in untouched canon block | routed (confirmation) | Reviewer's read of the filter (shape issues only) |
| Tool: `sub-item` special case vs `rule` | routed (confirmation) | Reviewer's read of `check-changes` |

Stop rule not met: F1 was repaired after the round. Round 6 to be commissioned over the current text, series A.

## Supervisor Ruling After Round 5 (2026-10-18)

Round 5 accepted. An unlinked term occurrence in an untouched canonical file is a note, never a block (tool pass); the guides' "a fault in an untouched canonical file is reported and becomes a change request" already covers it — no edit. Round 6 commissioned over the current text, series A, settled slot refreshed (routine).

## Round 6 (series A)

Reviewer: Codex gpt-6-astra, prompt `scratchpad/r6/prompt.txt` (diffed clean), report `scratchpad/r6/review-r6.md`. Two findings, both tool divergences; no guide-text defect; no open questions.

### Finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged | Size |
|---|---|---|---|---|---|
| F1 `references` finds bracketed ID citations only, not a sibling rule's bold-number pointer in a table cell or rule (shape pass r2 F1, logged as a tool enhancement; re-raised) | routed to the tool pass | tool | Resolve local bold-number pointers within the owning item | The sweep instruction; local pointers stay permitted | 0 |
| F2 `check-changes` compares items per file, so a declared `move item` plus `modify item` yields missing/added statuses and the `modify` entry is rejected | routed to the tool pass | tool | Compare a move's source and destination across files, then assess the modify | Move verified before modify; a changed contract still retires and adds | 0 |

### Round score

> F1 outside the binding target, routed to the tool pass (re-raise of a logged tool item) · F2 outside the binding target, routed to the tool pass — no live defect in the four guides

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (A) | 6.25 | 3 | 0 | 3 | 0 | 1 |
| r2 (A) | 1.875 | 1 | 0 | 1 | 0 | 1 |
| r3 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 (A) | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r5 (A) | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r6 (A) | 0 | 0 | 0 | 0 | 0 | 0 |

### Round 6 verification (tool md5 at close recorded in the findings log)

`references STAGE-01-01` over the fixture drafts returns the bracketed citations and omits the `(**01**)` table pointer at `pipeline-stage.md:14` — F1 confirmed. No guide text changed this round. Caps: 10,486 / 6,492 / 14,983 / 4,954 = 36,915 of 37,000.

### Round 6 closure

| Finding | Disposition | Evidence |
|---|---|---|
| F1 `references` misses bold-number pointers | routed to the tool pass | Reproduced on the fixtures; shape pass r2 F1 logged the same gap |
| F2 `check-changes` rejects move plus modify | routed to the tool pass | Reviewer's implementation read (`ok = found == {"added", "missing"}`; modify permits only `{"modified"}`) |

**Stop rule (a) met:** round 6 is a fresh round over the current text with no new live finding in the binding target (both findings route to the tool pass; neither is a re-raise the guides must answer). Convergence by clean round. Series A: 6.25 → 1.875 → 7.5 → 7.5 → 2.5 → 0. Sizes 58,385 → 36,915 (group cap 37,000). No supervisor-decision finding remains unimplemented. Awaiting closure.

## Pass Closed (supervisor, 2026-10-18)

Closure confirmed: target 2 closed with a clean round 6 at 36,915 bytes (10,486 / 6,492 / 14,983 / 4,954 against 10,500 / 6,500 / 15,000 / 5,000; group 37,000). Round-6 F1 and F2 are with the tool pass. Every finding of the pass carries a disposition with evidence or rationale in the round closure tables above: closed — r1 F1, F4, F5; r2 F1; r3 F2; r3 F1 (after the ruling); r4 F1, F2; r5 F1. Routed to the tool pass — r1 F2, F3; r2 F3, F4; r3 F3; r5 confirmations; r6 F1, F2. Logged — r1 F6; r2 F2. Open questions resolved by rulings — requests without drafts (spec-format 13), design-specs-design 9 residue, `check-changes` operation check. Net size change 58,385 → 36,915 (−21,470). No further rounds.
