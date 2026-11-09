# Spec Promotion Guides — Findings Log

Target 4: `Guides/ProductSpecs/product-specs-promotion.md`, `Guides/DesignSpecs/design-specs-promotion.md`, `Guides/Design/design-promotion.md` and the three promotion skill wrappers, refined together for fidelity and parallel structure. Standards: [`product-specs-system-design.md`](product-specs-system-design.md), [`design-specs-design.md`](design-specs-design.md), [`design-process-design.md`](design-process-design.md), [`spec-format-design.md`](spec-format-design.md). Refiner-facing cross-pass record: never shown to a cold reviewer; settled decisions go to the prompt's settled-dispositions slot instead. One row per finding per pass; appended at each round's closure.

## Seeded from earlier passes (promotion-relevant rows)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-08-27 p1 (req) | Content-check list had three drifted homes | closed | Promotion's `C1`–`C5` is the single enumeration; authoring cites |
| 2026-08-27 p1 (req) | Change requests raised but never answered | closed | Reopen answers it; readiness condition on `Proposed`; artifact section |
| 2026-08-29 r5 (req) | Promotion has no listed blocked gate for a missing Integration block | logged | A strand, not a misroute; the generic blocked gate covers it |
| 2026-08-29 r5 (req) | Re-promoting a package that raised a change request is undocumented | logged | The route out is stated; the round trip does not strand |
| 2026-08-29 r6 (req) | `C1`'s widened command false-positived; baseline with no catalog on disk gave a vacuous pass | closed, then superseded | The whole-content `C1` was reverted 2026-08-30; `C1` is `IDs are append-only` |
| 2026-08-29 r7 (req) | "Accounted for" is a substring match; a shell one-liner cannot encode the judgment | open — supervisor, superseded 2026-10-18 | The tool's `check-changes` and `validate` now supply `C1`'s evidence; the shell bracket is gone |
| 2026-08-29 r7 (req) | Readiness screen leaves no trace on the success path | logged | Readiness must not become `C0`; the tool runs at readiness leave their output as the checks' evidence (2026-10-18) |
| 2026-08-29 r7 (req) | `C6` transforms text that exists nowhere; its evidence could only assert intent | closed | Confirmation lives in `C7`, where the written files exist |
| 2026-08-30 (req) | Silent loss of glossary entries or index lines on a whole-file rewrite | accepted risk, stated (P9) | The drafting rule is the obligation; no check backs it; do not re-raise |
| 2026-08-30 r8 (req) | `C7` writes then confirms, but a return to authoring denied the write | closed | Rule bounded to `C1`–`C5`; a post-write fault is repaired in place |
| 2026-08-30 r8 (req) | Nothing distinguished a promoted package from an open one | closed | `## Completion` defines the promoted state; a promoted package is closed |
| 2026-08-30 r9 (req) | Readiness condition 2's "matches" undefined | closed, superseded 2026-10-18 | Now the tool's `check-changes` (spec-format 15) |
| 2026-08-30 r10 (req) | Baseline promotion has no worked example | logged | Priced out by budget; in the ledger |
| 2026-08-30 r11 (req) | `C7`'s confirmation printed nothing and exited 2 on unresolved paths, read as a pass | closed | Silence is never a pass (`## Evidence`); codified on the third sighting |
| 2026-08-30 r11 (req) | No worked example of a passing `C4`; `C5` has no evidence bracket | open — supervisor | Priced out, not declined; in the ledger; do not re-raise |
| 2026-08-30 r12 (req) | `C4`'s scope included index lines, which the Forbidden list bans as paths | closed | Subject narrowed to requirement and glossary prose; index lines are `C5`'s |
| 2026-08-30 r12 (req) | Promotion timing has no stop attached, and `auto` no checkpoint | logged | Every enforcing form adds weight; the standing blocked-gate route covers it |
| 2026-08-30 r15 (req) | `C5` enforces three traversal rules; mandatory inline cross-references has no check | open — supervisor | A proof burden; in the ledger; do not re-raise |
| 2026-08-30 r18 (req) | Authoring reopens a package by judgment where promotion blocks on the same ambiguity | open — supervisor | In the ledger; do not re-raise |
| 2026-08-30 r18 (req) | Under `shared`, an uninitialized submodule reads as an empty catalog | closed | Shape-qualified clause on both blocked gates |
| 2026-08-30 r18 (req) | Change-request lifecycle had no disposition for "valid, not this package's to fix" | closed | `Rejected` names the package it belongs to; no fifth status |
| 2026-10-05 r1-release (req) | Location rebasing creates false diffs; promotion timing; citation style | closed | Readiness compares prose and resolved targets (now the tool's diff); timing keyed to shipping; `C6` rebases destinations, `C7` is the completion identity |
| 2026-10-12 p1–p5 (design) | Authoring-return line scope; `C3` placement vs inventory; unfinished promotion continued, not restarted; component mechanics belong to the tool guide (P1); `C1` script covers only what it tests | closed | Series converged at p5 (6.875 → 0); invariant P1: the process guide says what promotion achieves, the tool guide how designs are arranged |
| 2026-10-12 p1 (design) | Recovery after rejection at production review unspecified | logged | No occurrence; route mechanics to the tool guide when one appears |
| 2026-10-12 p4 (design) | An evidence-only readiness failure fits neither continuation nor new-run wording cleanly | logged | New-run path; no occurrence |
| 2026-10-12 post (design) | Release 11 typed packages; tool-agnostic skills | closed (ruling) | Archive to `skai/promoted/<id>/design/`; the process guide loads the tool guide |
| 2026-10-14 p1 r1 (ds) | Whole-file scope vs "pre-existing defects do not block" | closed | One scope in Purpose and Promotion Checks; untouched canonical files not re-examined |
| 2026-10-14 p1 r1 (ds) | A `Proposed` request both permitted continuation and blocked | closed | Blocks at readiness; the continue-branch ride-through preserved |
| 2026-10-14 p1 r2 (ds) | Move-plus-modify failed readiness; `C2` needed writes outside the package | closed | Move identity verified before the declared modify (now `check-changes`); incoming-link files drafted in Touches |
| 2026-10-14 p1 r2 (ds) | Untouched-file defects both non-blocking and blocking | closed | Unrelated ones do not block; write-invalidating contradictions follow Raising a Change Request |
| 2026-10-14 p1 r4–r5 (ds) | A pending requirement both returned the package and waited; readiness blocked on a draft link after the contract was canonical | closed | Canonical requirements are a prerequisite that waits at the blocked gate; `C2` repoints the link |
| 2026-10-14 p1 r5 (ds) | Reusing a draft against intervening canon has no merge rule | logged | Readiness exposes a mismatch; sharpen reopen if it strands |
| 2026-10-14 p1 r17 (ds) | Incoming-link repair covered moves only; retirement changes anchors | closed | Moves and retired headings in `C2` |
| 2026-10-18 r1 (content) | "Promotion alone raises these"; request file names; inline text | settled (target 2) | Promotion is one filer among several; folders `change-requests/<nnn>/request.md`; dependents repaired here |
| 2026-10-18 r2 (authoring) | Promotion's worked `C1` bracket greps `^## ` while items are `###` | routed here | Repaired in the pre-review pass: the tool's output is `C1`'s evidence |

## Target 4 passes

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-18 pre-review | Post-write re-render would replace the archived page's approved diff with an all-unchanged render | ruling | The page is rendered last before the readiness screen, never after the write; `C7`/`C3` confirm by read-back and `validate` on the catalog (spec-format 15 amended) |
| 2026-10-18 pre-review | Sweep-recorded readiness check in design-specs-promotion beyond the listed delta | ruling | Kept for parallelism |
| 2026-10-18 pre-review | Worked `C1` evidence grepped `^## ` while items are `###` (routed from target 3) | closed | `C1`'s evidence is `check-changes` (missing items) and `validate` (duplicate IDs); verified: a dropped item fails with or without an entry, a reused retired ID is a duplicate |
| 2026-10-18 r1 | First commission aborted: the ruling cluster landed mid-review and the reviewer stopped | — | Not a round; recommissioned over stable text; never edit a guide while a review runs |
| 2026-10-18 r1 | F1 readiness condition 2 filed a request for an untouched-file note, then condition 5 rejected every `Proposed` request | closed | "No request filed before this run remains `Proposed`, whoever filed it" (both spec guides); continue-branch requests ride to completion |
| 2026-10-18 r1 | F2 `check-changes` matches a rule entry against its parent item's status | routed to the tool pass (re-raise) | Already assigned (target 2 r1 F2, r4 ruling, r5; target 3 r1 F4); the guides' wording equals spec-format 15 |
| 2026-10-18 r1 | F3 post-write confirmation attributed a fault by the file it was reported on; the validator reports a cross-file duplicate on the later-visited file | closed | Reproduced; "a fault readiness did not note is `C7`'s/`C3`'s, wherever reported" |
| 2026-10-18 r1 | F4 design-promotion's authoring-return line covered the promoted-path collision (condition 4) | closed | Conditions 1–3 return to authoring; condition 4 waits at the standard blocked gate with condition 5 |
| 2026-10-18 r1 | F5 design-promotion's worked block said `C1`–`C4` checked with `C4` evidence absent, under "Example" | closed | "Excerpt" |
| 2026-10-18 r1 | F6 the standard's "Integration block resolvable" readiness step has no operational line in promotion | logged | Standing blocked gate and the catalog guide's literal-path ban; sharpen Initiation on a strand |
| 2026-10-18 r1 | Open: root-location authority (Integration block vs README hosting) | open question | Standard-level |
| 2026-10-18 r1 | Round score | — | Series A r1 8.125 (3 divergent, 1 noise, 1 routed); sizes 16,986 / 12,796 / 11,500 / 449 / 449 / 500 = 42,680 |
| 2026-10-18 r1 | Supervisor ruling after r1 | ruling | Round accepted; the project README is the root-location authority (`artifact-hosting.md` for a first artifact), the Integration-block wording historical (requirements-system-design § Workflow step 4); no guide edit unless a strand occurs |
| 2026-10-18 r2 | F1 `check-changes` skips the operation check for an entry naming an existing, modified file (`add file` on it passes); a bare-path design identity resolves to the index line | routed to the tool pass | Reproduced on the product fixture (0 issues, exit 0); the guides' wording equals spec-format 15 |
| 2026-10-18 r2 | F2 the `C7` evidence bracket said "0 issues in the written files" after the rule became "wherever reported" (ruling-cluster text) | closed | "validate skai/requirements: nothing beyond readiness's 1 note"; consolidation trigger fired once |
| 2026-10-18 r2 | F3 readiness condition 4 demanded a sweep for every modify or retire while authoring sweeps IDs and glossary entries only | closed | "Every modified or retired ID or glossary entry has its sweep under the authoring artifact's `## Verification`" (both spec guides) |
| 2026-10-18 r2 | Open: a resumed `C7`/`C3` confirmation may lack the identities of readiness's notes | open question | The uncertain-outcome blocked route covers it; no readiness record (settled) |
| 2026-10-18 r2 | Round score | — | Series A r2 5.0 (2 divergent, 0 noise, 1 routed); sizes 17,000 / 12,794 / 11,500 / 449 / 449 / 500 = 42,692 |
| 2026-10-18 r2 | Supervisor ruling after r2 | ruling | Round accepted; F1 with the tool pass; an unfundable round 3 fix is a size-rule supervisor decision |
| 2026-10-18 r3 | F1 Raising a change request's "block if writing would leave canon inconsistent" reversed readiness's "an untouched-file fault never blocks" (a duplicate between two untouched files remains after any write) | closed | "block only if the write itself would contradict canon / the specs" (both spec guides), the gate bullets' own formulation |
| 2026-10-18 r3 | F2 the `C1` bracket concluded "no ID … reused" from `check-changes` and `validate` alone; a retired item revived live under its ID with a `modify` entry passes both | closed | Reproduced; `C1` says "inspect that no retired item is made live" and the bracket records that inspection |
| 2026-10-18 r3 | F3 design rollback after a rejected production review does not say what to restore when unrelated work entered the file meanwhile | logged (second sighting of design-process p1 F4) | The standing blocked route covers it; a third sighting codifies |
| 2026-10-18 r3 | Tool: round 2 F1 (`add file` on a modified file) fixed in build 94407e0b | closed (tool pass) | `R0 declares add but file … is modified`, exit 1 |
| 2026-10-18 r3 | Round score | — | Series A r3 8.75 (2 divergent, 1 noise); sizes 16,997 / 12,797 / 11,500 / 449 / 449 / 500 = 42,692 |
| 2026-10-18 r3 | Supervisor ruling after r3 | ruling | Round accepted; the revived-retired-ID case becomes a validator rejection (tool pass); `C1`'s bracket may cite the tool once it lands if the cap allows, else the inspection wording stays |
| 2026-10-18 r4 | F1 readiness condition 3 restated change-list granularity ("every changed … index line and file has an entry") against the artifacts guides (index lines ride in Touches; a new file is one entry) and the tool | closed | "every change has an entry, or rides in one's Touches, at the artifacts guide's granularity" (both spec guides); the artifacts guides stay the one home |
| 2026-10-18 r4 | F2 `C1`'s bracket (round 3's repair) evidenced the retirement inspection only; two live items exchanging IDs with a `modify` entry pass both commands | closed | `C1` restated whole: tool covers missing, duplicate and (build 144c8081) revived IDs; inspection covers renumbering; bracket records it. Consolidation trigger fired twice → structured tier (invariants P1–P5, ownership table, rule impact maps in the working doc) |
| 2026-10-18 r4 | Tool: the validator rejects a revived retired ID (build 144c8081) | closed (tool pass) | `STAGE-04 revived; … a retired ID is never modified`, exit 1; `C1` cites it |
| 2026-10-18 r4 | Round score | — | Series A r4 10.0 (2 divergent, 0 noise); sizes 16,987 / 12,800 / 11,500 / 449 / 449 / 500 = 42,685 |
| 2026-10-18 r4 | Supervisor ruling after r4 | ruling | Round accepted; tool stable (no open items); a round 5 of compression defects is reported as such with the byte cost of full restatement, for a possible cap adjustment |
| 2026-10-18 r5 | F1 the `C7` evidence bracket's grep tested the legacy inline `(D#)` citation form while citations are reference-style `[D#]` | closed | Regex `\[D[0-9]+\]`, probed; stale original text from before the 2026-10-05 link decision, not a compression defect (cost 0) |
| 2026-10-18 r5 | Open: removing an item's last rule passes both commands and `C1`'s named inspection says items only | logged (first sighting) | `C1`'s opening clause and spec-format 2 cover rules; on recurrence sharpen the inspection to "no item or rule is dropped or renumbered" (+16 bytes) |
| 2026-10-18 r5 | Round score | — | Series A r5 5.0 (1 divergent, 0 noise); sizes 16,987 / 12,800 / 11,500 / 449 / 449 / 500 = 42,685; tool md5 144c8081 stable |
| 2026-10-18 r5 | Supervisor ruling after r5 | ruling | Round accepted; no cap change; round 6 commissioned |
| 2026-10-18 r6 | No live findings in the binding target | closed — clean fresh round | Stop rule (a); series A r1 8.125 → r2 5.0 → r3 8.75 → r4 10.0 → r5 5.0 → r6 0; sizes 47,633 → 42,685 (caps 17,000 / 12,800 / 11,500 / 450 / 450 / 500; group 42,700); tool md5 144c8081 at close |

| 2026-10-18 r6 | Pass closed by the supervisor | closed | Target 4 closed at 42,685 bytes after clean round 6; no further rounds |

Pass converged by a clean round: round 6 (series A) raised no finding in the six files. Net size change 47,633 → 42,685 (−4,948): 16,987 / 12,800 / 11,500 / 449 / 449 / 500. Consolidation trigger fired twice (r2 F2 on the ruling cluster's bracket; r4 F2 on round 3's `C1` repair); the structured tier (invariants P1–P5, canonical-ownership table, rule impact maps in the working document) applied from round 4. Routed during this pass: rule-level `check-changes` (r1 F2, re-raise; by contract), `add file` on a modified file (r2 F1, fixed in the tool), the revived retired ID (r3 F2's tool half, fixed in the tool as a validator rejection). Logged, not codified: no explicit root-resolution step in promotion (r1 F6; the README is the authority by ruling), design rollback scope with intervening work (r3 F3, second sighting), an item's last rule removed passing both commands (r5 open, first sighting). Supervisor rulings recorded above: no render after the write (page rendered last before readiness; `C7`/`C3` confirm by read-back and `validate` on the catalog); the sweep readiness check kept in design-specs-promotion for parallelism; the README as root-location authority; the unfundable-fix size rule; no cap change after round 5.
