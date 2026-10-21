# Design Process — Refinement Working Document

Targets: `Guides/Design/design-authoring.md`, `Guides/Design/design-promotion.md` and the Figma
designer guide they load. Design specs: [`design-process-design.md`](design-process-design.md),
[`figma-designer-guide-design.md`](figma-designer-guide-design.md).

## Slice 5 — Gaps On Figma Change Pages — 2026-10-21

Known gaps (skai#82) slice 5, decision G01 (2026-10-20): the design package's artifact is the
source; the change page mirrors each open gap with one Dev Mode annotation on the placeholder node;
the convention lives in the Figma designer guide; the tool-agnostic guides carry one sentence each.

### Pre-edit workflow model (gated-workflows § Pre-edit workflow model)

**Design authoring.**

- Happy path: signal → read tool guide → resolve change ID, create artifact, Goal and Inputs →
  Discussion (items raised and resolved; nothing drawn) → Discussion planned gate (gaps carried) →
  Mockups (draw on the change page; trace pass) → Mockup review gate → "approved" → Design Changes →
  `🏁 Complete.`
- Artifacts: `design-authoring.md` (Discussion, Design Changes, Decision Log); the change page.
- Markers: `- [ ] D<n>` items only, each checked on the supervisor's approval of that item; gap
  items stay unchecked with a **Gap** line and block promotion, not the Discussion gate.
- Blockers: no change ID; the tool cannot do what a draft needs; non-gap items open.
- Where the change lands: a gap item is raised in Discussion (nothing is drawn yet) or parked from
  mockup feedback (its placeholder may already be drawn). Its placeholder is a drawn state, so the
  mirror can exist only once that state is on the page: on the next Mockups pass for a new item, at
  once for one raised against an existing drawing. It closes through *Resolution* in any phase.
- Simulations before the edit:
  - Normal: D01 decided, D02 a gap → `⏳ GATE: Next: Discussion complete; 1 open gaps carried. Say "next" to draw the mockups on pinned-notes.` → Mockups draw D02's placeholder state; today nothing marks it on the page, so the reviewer at the Mockup review gate cannot tell it is provisional (the defect this slice fixes).
  - Blocked / tooling failure: a font will not load → workflow-specific blocked gate; unaffected.
  - Ambiguity: feedback at the Mockup review gate asks for a state whose rule nobody can decide yet → parked as D03 with a **Gap** line; ends at the Discussion gate (planned, D03 carried) since nothing else is open; the page again shows no sign the drawing is provisional.
  - `auto`: bypasses the Discussion planned gate, never the Mockup review gate; unaffected.

**Design promotion.**

- Happy path: signal → readiness screen (1: zero open items, gaps included) → Promotion Checks
  written → Promotion Checks gate → C1–C4 → Production review gate → C5 delete page → C6 archive →
  `🏁 Complete.`
- Artifacts: `design-promotion.md` (checks, evidence); the change page; production.
- Markers: `- [ ] C<n>`, checked as each passes; a failing C1/C2 returns to authoring.
- Blockers: readiness 1–3 (and 5 invalidating), C1/C2 failure, requested design change → authoring;
  condition 4 / `Proposed` request → standard blocked gate; C3/C4 repaired in place.
- Simulations before the edit:
  - Normal: zero open items, C1–C4 pass; any gap mark left on a draft (an item closed without its mark removed) is copied into production by C3 — no check looks for it.
  - Blocked: D02 still a gap → readiness 1 fails; blocked line, package returns to authoring.
  - Ambiguity: a stale mark on a draft whose item is closed — C1 "follows the tool guide" would catch it only if the tool guide's conventions say the mark goes; today they do not mention it.
  - `auto`: bypasses the Promotion Checks gate, never Production review; unaffected.

Conclusion: the authoring sentence belongs beside the gap pointer in *Discussion* and must allow
for the placeholder being drawn later than the item is raised; the promotion check belongs in C1
(an authoring defect, so a failure returns the package to authoring, where the mirror is removed).
No gate, marker or `auto` behavior changes in either guide.

### Edits

- `figma-designer-guide.md`: new § Gaps between *Copy and sample data* and *Working a backfill* (three
  rules: one Dev Mode annotation per open gap on the placeholder node, text = the gap line; added
  once the Gap line exists and the placeholder is drawn, updated with the placeholder, removed when
  the item closes, never on `Production`; written through the node's `annotations` in the Plugin
  API, keeping other annotations). `Managed-Updated-At` 2026-10-14 → 2026-10-21.
- `design-authoring.md` § Discussion, after the gap pointer: "Once a gap's placeholder is drawn,
  mirror the gap on the change page as the tool guide says; remove the mirror when the item closes."
  Trims paying for it:
  1. § Mockups: dropped "Follow the tool guide's conventions throughout." (Purpose already says the
     designs must meet the tool guide's conventions; Initiation step 1 loads it.)
  2. § Design Changes: "Written after approval, and it records that approval: promotion takes its
     presence as evidence the mockups were approved." → "Written after approval; promotion takes its
     presence as evidence of that approval."
  3. § Artifact maintenance: dropped "and end the response at whichever gate *Gates* prescribes"
     (the Gates core rule already requires every waiting message to end at a gate line).
- `design-promotion.md` `C1`: "…follows the tool guide, and none still mirrors a gap." Trim paying
  for it: § Completion dropped "An archived package is not promoted again." (readiness condition 4
  already blocks a package whose promoted path exists).
- README § Figma designs: the Figma guide's content list gains "gaps on change pages".

### Sizes (`wc -c`)

| File | Cap | Before | After |
| --- | --- | --- | --- |
| `design-authoring.md` | 15,100 | 15,084 | 15,072 |
| `design-promotion.md` | 11,500 | 11,497 | 11,484 |
| `figma-designer-guide.md` | pair 19,000 with multiple-sizes (2,698) | 13,976 (pair 16,674) | 14,730 (pair 17,428), +754 |

### Sanity scan after the Figma guide edit

- `Managed-Updated-At`: 2026-10-21 (header read after the edit).
- Gates / Advance intent sections: not a gated guide (conventions; design spec § Authority) — n/a; `grep -c "^## Gates"` → 0, as before.
- "human", "Next Command", "checkpoint": `grep -nw` → 0 occurrences.
- Runtime reference to process-flow: `grep -n process-flow` → 0.
- Stack-mismatched references: `grep -n "Xcode\|iOS\|SwiftUI\|Android"` → 0 (requirement 1, platform-agnostic).
- Markers: `grep -n 🟡` → 0; no `- [ ]` items added (visual review of § Gaps).
- Working-doc paths: none added (`grep -n working-docs` → 0 in this guide).
- Gap workflow inlined: § Gaps states only the mirror (no resolutions, inheritance or catch-up) — visual review; the gap itself is defined by reference to the artifact's item.
- Design spec requirements: 2 no implementation details (the Plugin API names the editing tool, as § Agent tooling already does); 5 rules, not a log; 7 numbered rules with bold leads — visual review, ok.

### Sanity scan after the design-authoring edit

- `Managed-Updated-At`: 2026-10-21 (already today's; header read).
- `## Gates` and `## Advance intent` present (`grep -c` → 2); supervisor sentence present (line 68, the template's "human or authorized agent" definition — false positive for the "human" check, intentional per the template).
- Gate lines: `git diff | grep GATE` → 0 changed; planned/blocked lines unchanged.
- Pointer sentence verbatim against `process-flow.md` (link path aside): `grep` both, compared → identical.
- Gap workflow inlined: the new sentence names only the mirror and defers its form to the tool guide; no resolution, inheritance or catch-up text — visual review.
- Marker lifecycle: unchanged; the sentence changes no checkbox — visual review.
- Runtime process-flow references: 0. "Next Command"/"checkpoint": 0. `🟡`: one hit, the inlined template's source-file convention (false positive).
- Artifact skeleton still ends with `## Decision Log` — visual.

### Sanity scan after the design-promotion edit

- `Managed-Updated-At`: 2026-10-21 (header read).
- `## Gates` / `## Advance intent` present (2); "human" hit is the supervisor definition (false positive); gate lines unchanged (`git diff | grep GATE` → 0).
- `C1` failure path unchanged: a failing `C1` is already a blocked gate returning the package to authoring (§ Gates), which is where the mirror is removed.
- Readiness item 1 (zero open items, gaps included) unchanged.
- Process-flow references 0; `🟡` one template hit (false positive); working-doc paths unchanged (C6 line only).

### Post-edit simulations (gated-workflows § Flow reflection)

**Design authoring.**

- Normal: D01 decided, D02 `[Question]` with `- **Gap** share sheet offers link sharing only` →
  `⏳ GATE: Next: Discussion complete; 1 open gaps carried. Say "next" to draw the mockups on pinned-notes.`
  → "next" → Mockups draws `share sheet`; the placeholder is now drawn, so the agent adds the
  annotation `D02 — share sheet offers link sharing only` on that node (Figma § Gaps rules 1 and 3) →
  trace pass → `⏳ GATE: Next: Review the mockups on pinned-notes. Say "approved" to write Design Changes, or give feedback.`
  The reviewer sees the provisional state marked. "approved" → Design Changes → `🏁 Complete.`, D02
  still open. Later reopen: the supervisor answers D02 → Decision appended, Gap removed, log
  `decided`; the agent redraws if the answer differs and removes the annotation. No issues found in simulation.
- Blocked: a font will not load during Mockups → `⏳ GATE: Blocked: …` per the tool guide; the mirror
  is untouched. No issues found in simulation.
- Ambiguity: at the Mockup review gate feedback raises an undecidable rule for an already drawn
  state → parked as D03 with a Gap line; its placeholder is already drawn, so the annotation goes on
  now; response ends at the Discussion planned gate naming the carried gap. Placeholder later
  changes (gap stays open, log silent) → annotation text updated (Figma § Gaps rule 2). No issues found in simulation.
- `auto`: bypasses the Discussion planned gate; Mockups draws and annotates; stops at the Mockup
  review gate (never bypassed). No issues found in simulation.

**Design promotion.**

- Normal: zero open items; `C1` inspects the drafts — every draft follows the Figma guide and no
  draft carries a gap annotation (an item closed earlier had its annotation removed) → `C1` checked
  with `[evidence: C1; …; no gap annotation on the 3 frames]`; C2–C4; Production review gate;
  production carries none. No issues found in simulation.
- Blocked: D02 still a gap → readiness 1 fails →
  `⏳ GATE: Blocked: readiness condition 1 — D02 is an open gap. The package returns to authoring; re-run promotion once it is resolved.`
  No issues found in simulation.
- Ambiguity: D02 closed but its annotation was left on the draft → `C1` fails →
  `⏳ GATE: Blocked: C1 — draft share sheet still mirrors gap D02. The package returns to authoring; re-run promotion once it is resolved.`;
  authoring removes it; the new run unchecks every check. No issues found in simulation.
- `auto`: bypasses the Promotion Checks gate; `C1` still runs and blocks as above; never bypasses
  Production review. No issues found in simulation.

## Maintenance retro — slice 5 — 2026-10-21

Maintenance retro: DONE

1. Inventory: the gap mirror convention in the Figma designer guide; one sentence each in design
   authoring and design promotion (`C1`); README content line; design-spec amendments. Host-install
   visible (three managed guides).
2. Bookkeeping: `Releases/unreleased.md` entry under **Known gaps** with migration "none" and why;
   `CHANGELOG.md` "Known gaps, part four" line; both agree (`grep` → 1 each). Manifest unchanged (no
   asset added or moved; `json.load` ok). `Managed-Updated-At` 2026-10-21 on the three edited guides
   (headers read). README updated (Figma guide's content list). `internal/maintain-skai.md`: no new
   invariant.
3. Integration doc: untouched. 4. Installer: untouched.
5. Consistency: `known-gaps.md` rule 3 already sends the Figma case to "their guides" — now true,
   no edit. Stale "later slice" mentions: `grep -rni "later slice\|figma mirror" Guides README.md internal`
   → 2 hits in `work-spec-creation.md` (unrelated meaning, false positives); the 2026-10-20 Adopts line
   in `design-process-design.md` naming the mirror as a later slice is dated history, left as is.
   Gated guides: `## Gates` intact, gate lines unchanged. Change-package verification (promotion
   check changed): a leftover annotation fails `C1` before any production write; the blocked line
   returns the package to authoring; coexistence, independent promotion and archival recovery are
   untouched (only `C1`'s criterion grew). Guide addendum contract: entry and footer lines unchanged
   in all three guides (`grep "Project Addendum\|addenda/"` → 9 lines, three per guide, as before). README links: the edited line keeps its links.
6. Process reflection:
   - (a) The routing table's design spec for the Figma pair and the pair's cap live in a different
     file from the guide being edited; the brief named it, but nothing in `guide-authoring.md`
     tells a maintainer to look up a guide's cap before editing. Suggest one line in its sanity
     scan: "the edited guide is at or under its design spec's size cap (`wc -c`), with any trims
     listed."
   - (b) A gap item can be raised before anything is drawn (Discussion phase), so "added when the
     gap is raised" could not hold literally; the convention became "once the item has its Gap line
     and the placeholder is drawn". Worth noting in `known-gaps-planning.md` slice 6 (the UI Map
     mirror) in case the same timing applies there.

Follow-up (not fixed; outside this slice): README design authoring Usage, Mockups phase, says
"filing change requests for the gaps" for trace mismatches; "gap" is now a defined term, so that
wording reads wrong. Suggest "for the mismatches".

### Slice 5 — compression and cold review — 2026-10-21 (reviewing session)

Compression review (Astra) of § Gaps: 754 drafted → 512 proposed → 599 applied with plain sentences; pair 17,274 of a proposed 17,300 cap (awaiting the supervisor).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F1 ("verbatim" points at the Gap sub-bullet, which carries no item ID; the compressed text lost the `D<n> — <placeholder>` format) divergent · normal · speculative = 2.5

- F1 closed: the section now says the text is `D<n> — <placeholder>`, the item's ID then its Gap line's value unchanged. Self-check: the amendment's format matches; authoring's sentence and promotion's `C1` unchanged.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r2 | 0 | 0 | 0 | 0 | 0 | 1 |

> r2: F1 (which drawing hosts the annotation when one placeholder appears in several) log-only, noise · no open questions · terminal by clean round (stop rule (a)), 2026-10-21

- F1 logged — rationale: no occurrence yet; the blocked-gate route covers an operator who cannot choose; a worked example on the placement sentence if it recurs, in the guide and the amendment together.
- Retro after the review repair: the one-sentence fix and the README "mismatches" fix need no bookkeeping beyond the existing entries; the Figma guide's header is 2026-10-21; pair 17,292 bytes, proposed cap 17,300 pending the supervisor.
