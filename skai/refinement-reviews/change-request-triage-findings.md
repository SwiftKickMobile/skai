# Change-Request Triage — Findings Log

Target: the change-request passages of `Guides/ProductSpecs/product-specs-{authoring,artifacts}.md`, `Guides/DesignSpecs/design-specs-{authoring,artifacts}.md`, `Guides/UIMap/ui-map-architecture{,-artifacts}.md`, `Guides/Design/design-promotion.md`; promotion guides for their dependence on request status. Standard: `product-specs-system-design.md` § Decisions — 2026-10-19 (change request triage); adopted by `design-specs-design.md`. Reviewer: Codex `gpt-6-astra`, cold, template verbatim.

## Round 1 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | Both authoring guides describe resolution only as approval of an existing item; a supervisor decision supplied without an item has no recording path | divergent · off-normal · speculative | accept — one sentence in § Resolution / § What earns an item: recorded as a checked item with its Decision line |
| F2 | design-specs-authoring § Requirements Gaps still makes opening a package a precursor to filing a request; Gates note assumes every gap has a request status | divergent · off-normal · speculative | accept — two routes (request against an open package; input for product specs authoring when none); Gates note aligned |
| F3 | "never reject or supersede one" lost the standard's "on its own" in product-specs-authoring § Reopening and ui-map-architecture § Initiation | divergent · off-normal · speculative | accept — qualifier restored |

Collapse: F1+F2 one defect (reviewer's root cause: decision 2 not carried into the operational text), heaviest F1 = 5 × 0.75 × 0.5 = 1.875; F3 = 1.875.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 3.75 | 2 | 0 | 2 | 0 | 0 |

Open question (reviewer): a reopen performed only because requests exist can reach authoring completion with them still `Proposed`; promotion blocks, authoring does not. Left as designed.

## Round 2 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | product-specs-authoring § Working a scoped change routes a broken design-spec citation to "a change request against them" with no open-package condition | divergent · off-normal · speculative | accept — against the open design-spec package, else input for design specs authoring |
| F2 | design-specs-authoring § Requirements Gaps closes the gap on any ruling; a rejection leaves draft behavior that assumed the contract | divergent · off-normal · speculative | accept — resolves when the outcome is applied to the draft; Gates note aligned |
| F3 | Both promotion guides' readiness 5 exempt requests by filing time, not by provenance | divergent · off-normal · speculative | accept — only a request this run filed under Raising a change request is exempt |

Collapse: one defect (reviewer's root cause: lifecycle not reconciled with its callers), heaviest F1 = 1.875. Log-only (no row): the observed failure's request-conversion path is now past-a-rule under the revised text.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r2 | 1.875 | 1 | 0 | 1 | 0 | 0 |

## Round 3 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | Both promotion guides check readiness 5 once before the gate; a request filed while the gate waits is not seen at the write | divergent · off-normal · speculative | accept — condition 5 still holds when the write begins; referenced at C7 / C3 |
| F2 | design-specs-artifacts § Change Requests and design-specs-authoring § Requirements Gaps select the open package "for the screen" / "for the change" instead of by subject | divergent · off-normal · speculative | accept — "for the subject" |

Two rows (distinct causes): 1.875 + 1.875.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r3 | 3.75 | 2 | 0 | 2 | 0 | 0 |

## Round 4 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | Requirements Gaps turns Rejected/Superseded into "reworked or removed, never kept" (a repair of r2-F2's repair) | divergent · off-normal · speculative | accept — the supervisor's reason and resulting coverage decide; gap resolves when reflected in the draft |
| F2 | Promotion guides delegate the request's destination to the subject rule; the settled destination (the package being promoted) is unstated | divergent · off-normal · speculative | accept — destination stated at the filing step |
| F3 | spec-file-shape `validate` row says an untouched canonical fault "becomes a change request" | divergent · off-normal · speculative | accept — clause deleted; the workflow disposes |
| F4 | Concept inventory forces a [Proposal] for a concept the supervisor already decided | divergent · normal · speculative | accept — open item only where a decision is still needed |

Clusters: F2+F3 (routing has more than one owner), heaviest F2 = 1.875; F1+F4 (action from status, not ruling), heaviest F4 = 2.5. Consolidation trigger: F1 is a repair of a repair (1 of 2).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r4 | 4.375 | 2 | 0 | 2 | 0 | 0 |

## Round 5 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | ui-map-architecture § Provisional preview's seed sentence reads as a restart on reopen | divergent · off-normal · speculative | accept — seed only when no proposed map exists; reopen starts from the existing one |
| F2 | design-specs-artifacts "never link another package" forbids citing a request redirected from another design-spec package | divergent · off-normal · speculative | accept — depending on a package (never) vs citing where input came from (allowed) |

Two rows: 1.875 + 1.875. Both adjacent to the target (reached through the reopen path), neither about who rules.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r5 | 3.75 | 2 | 0 | 2 | 0 | 0 |

## Round 6 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | design-promotion readiness 5 accepts a terminal status without the ruling's effect on the approved mockups being applied | divergent · off-normal · speculative | accept — a ruling that invalidates assumed behavior returns to design authoring; one that leaves the drawings valid needs nothing |
| F2 | design-promotion's readiness is "for a new run"; C3 does not re-establish condition 5 at the production write | divergent · off-normal · speculative | accept — condition 5 still holds at the write, referenced at C3; "new run" sentence qualified |

One cluster (design promotion's readiness 5), heaviest F1 = 1.875. Receiving workflows reported clean.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r6 | 1.875 | 1 | 0 | 1 | 0 | 0 |

## Round 7 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | Concept inventory's "waits for that item's resolution … blocked gate" still follows the checked-item qualifier (repair of r4-F4's repair; consolidation trigger fired a second time) | divergent · normal · speculative | accept — sentence restructured: undecided blocks, settled is recorded and drafting continues |
| F2 | design-authoring lists filed requests only "until ruled on", so design-promotion readiness 5 can miss a terminal ruling's effect | divergent · normal · speculative | accept — the list keeps every request with its status through promotion |

Two rows: 2.5 + 2.5. Consolidation trigger count: 2 (r4-F1, r7-F1), both in product-specs-authoring's supervisor-decision text; a third occurrence stops patching and restructures that passage.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r7 | 5.0 | 2 | 0 | 2 | 0 | 0 |

## Round 8 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | The package review page's status says "ready for promotion" from Discussion state alone, ignoring `Proposed` requests (`Bin/spec-tool.py` render) | divergent · normal · verified | accept — routed to the tool (outside the binding target): drop the readiness claim, label only the Discussion state; awaiting supervisor's go for the tool change |
| F2 | The decision-vs-request distinction lives in the artifacts guide, the recording instruction in authoring; the observed failure is now past-a-rule | divergent · past-a-rule · speculative | log-only — a ❌/✅ example if it recurs |
| F3 | design-promotion's Gates routing list omits readiness 5's authoring-return outcome | divergent · off-normal · speculative | log-only — the generic blocked route covers it |

No live finding in the guides: terminal by clean round (stop rule a). F1 routed; F2, F3 logged.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r8 | 0 (guides); 5.0 routed to the tool | 0 | 0 | 0 | 0 | 2 |

## Round 9 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | product-specs-catalog.md Purpose: an untouched canonical defect "becomes a change request", unconditionally | divergent · off-normal · speculative | accept — routed to the artifacts guide's § Change Requests; class swept across all guides (design-specs.md requirements-gap sentence too) |
| F2 | design-specs.md § What Belongs Here gives only the open-package route for a requirements gap | divergent · off-normal · speculative | log-only by the reviewer; fixed in the class sweep (routes to authoring § Requirements Gaps) |
| F3 | design-promotion's authoring-return gate bullet omits readiness 5's invalidating ruling (recurs from r8) | divergent · off-normal · speculative | log-only by the reviewer; recurrence → fixed (bullet extended) |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r9 | 1.875 | 1 | 0 | 1 | 0 | 2 |

## Round 10 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | design-authoring § Resolution's "(a ruled one blocks nothing)" (added in r7) contradicts design-promotion's readiness 5 | divergent · off-normal · speculative | accept — phrase deleted |
| F2 | "this run" undefined for a promotion resumed before its first write | divergent · off-normal · speculative | log-only — sharpen Initiation's restart distinction if it recurs |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r10 | 1.875 | 1 | 0 | 1 | 0 | 1 |

## Round 11 — 2026-10-19

| # | Finding | Labels | Disposition |
|---|---|---|---|
| F1 | Both authoring guides' Resolution / drafting passages do not say that recording a supervisor decision as checked settles only what the decision settled; remaining placement or scope choices still earn Discussion items | divergent · off-normal · speculative | supervisor decision — fourth re-framing of the same boundary (r1-F1, r4-F4, r7-F1, r11-F1); loop stopped, ledger presented |

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r11 | 1.875 | 1 | 0 | 1 | 0 | 0 |

## Unimplemented ledger — 2026-10-19 (for the supervisor)

- r11-F1 (above). What the reviewer wants: one sentence in each authoring guide's Resolution that a checked decision settles only what it settled, and a qualifier on "draft under the recommended reading" that provisional drafting stays within authorized scope. What already covers it: § What earns an item lists "genuine placement or scope choices" as Discussion items, and the Discussion blocked gate holds them. Smallest fix: the two sentences. Heavier fix: none proposed. Recommendation: rule it settled (the existing item rule covers it; a fifth wording of the same boundary is the thrash the consolidation trigger warns about), or accept the two sentences and run one more round.
- r8-F1: the package page's "ready for promotion" label ignores `Proposed` requests (`Bin/spec-tool.py` render). Tool change; needs the supervisor's go.
- r8-F2, r8-F3, r9-F2, r9-F3, r10-F2: logged (r9-F2 and r9-F3 fixed in the class sweep anyway).

## Supervisor ruling — 2026-10-19

- r11-F1: settled by ruling — "reviewer is over-engineering; don't add more rules". The existing item rule covers it. Convergence by ruling (stop rule b).
- r8-F1: fix approved — the package card's state reads "discussion complete" instead of "ready for promotion".

## Closure — 2026-10-19

Accepted and applied: r1 F1–F3, r2 F1–F3, r3 F1–F2, r4 F1–F4, r5 F1–F2, r6 F1–F2, r7 F1–F2. Routed: r8 F1 (tool). Logged: r8 F2, F3. Consolidation trigger fired twice (r4-F1, r7-F1), both in product-specs-authoring's supervisor-decision text; the r7 restructure held in r8.
