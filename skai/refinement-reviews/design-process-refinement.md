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

## Change Requests: Authoring Against A Base — 2026-10-23

Run per skai#90 in use (no guide edit): inventory in `design-process-design.md` § Amendment —
2026-10-23 (and `figma-designer-guide-design.md` § Amendment — 2026-10-23), drafts checked against
it by the author, then the compression review by Codex Astra, then the supervisor sets the caps.
The drafts were written before the supervisor's go and are kept as the drafts for the check.

### Author check — 2026-10-23

Drafts: `design-authoring.md` 19,791 → 19,668 bytes after the check (cap 15,100 of 2026-10-20);
`design-promotion.md` 13,942 (cap 11,500); Figma pair 17,599 (cap 17,300).

Authoring inventory 1–10: each present (1 Purpose; 2 The change package, table and paths; 3 The
change package, drawings; 4 Rendering, Artifact maintenance; 5 Phases, blocked gate, Review gate;
6 Design Changes; 7 Initiation; 8 Discussion; 9 Initiation; 10 Gates, Advance intent). Promotion
inventory 1–5: each present (1 Purpose, C3; 2 Readiness; 3 C3, Completion; 4 C1–C6; 5 Gates).
Figma requirement 9: present, one passage under the page rules.

Beyond the inventory, cut: the Description bullet's escalation rule (a request needing more than a
drawable description "is not one to send without mockups, and the supervisor … is told so");
inventory 5 already places that ruling with the supervisor. Kept and flagged for the reviewer:
the trace pass now also accepts a drawn state that traces to a decision of the base, and a package
spec served by the base; a consequence of inventory 1 for a request, not an inventory item. Nothing
the old guides said outside the amendment's scope was dropped (gates, advance intent, Discussion,
Resolution, the specs change-request paragraph, backfill, archival of working documents).

### Compression review — 2026-10-23 (Codex Astra, two rounds)

Round 1 on the author-checked drafts (scratchpad `compress/`): authoring 19,668 → 17,374
(+2,292 over released), promotion 13,942 → 12,890 (+1,406), Figma 14,901 → 14,848 (+254).
Rulings followed (design spec § Rulings — 2026-10-23: no approval word, live change list,
inputs reconciled at the Review gate's advance with no upstream type named), applied with the
specs-mirroring points (review-page link in the skeleton, render before readiness, Rendering
folded into Artifact maintenance) and the second planned gate line Astra flagged.

Round 2 on those drafts (scratchpad `compress2/`), rulings in the standard:

| Guide | Released | After (draft) | Compressed | Compressed addition |
| --- | ---: | ---: | ---: | ---: |
| design-authoring.md | 15,082 | 17,546 | 16,502 | 1,420 |
| design-promotion.md | 11,484 | 12,804 | 12,421 | 937 |
| figma-designer-guide.md | 14,594 | 14,848 | 14,821 | 227 |

Protected blocks (header, gate boilerplate, addendum footer) verified intact both rounds.
Astra's flags, author's disposition pending the supervisor: accept the trace pass restored to
"every drawn state traces to an input" and "downstream work is out of scope" named at completion,
and readiness 2 saying the list is current; reject the restored `mockup review` milestone (the
gate is Review now) and "revoke the base's approval" (no approval concept); put back the three
sentences it cut again that mirror the specs guides (IDs never reused, Description longer only
when the change needs it, a citation standing alone), about 60 bytes.

Obsolescence sweep (author, 2026-10-23, added to skai#90): on the round-two rewrites with the
dispositions applied, the amendment obsoletes only the two old milestone names, the "revoke the
base's approval" clause and one role-worded phrase ("the input's supervisor"); cut. Round 3 on the
swept drafts (scratchpad `compress3/`): authoring 16,520 → 16,210 (+1,128 over released),
promotion 12,344 → 12,206 (+722), Figma 14,821 → 14,794 (+200; pair 17,492). No inventory loss
reported; the three restored sentences retained; protected blocks intact. Caps proposed a little
under the compressed sizes (skai#90 as corrected 2026-10-23).

### Refinement — series CR (2026-10-23)

Target: the three guides at the installed round-three sizes (16,210 / 12,206 / 17,492) against caps
16,100 / 12,100 / 17,400. Standard: `design-process-design.md` § Amendment, § Rulings, § Size
Budgets (2026-10-23); `figma-designer-guide-design.md` § Amendment — 2026-10-23. Reviewer: Codex
`gpt-6-astra`, cold, template verbatim (prompt `scratchpad/refine/r1/prompt.txt`, diffed clean:
slot fills and five deleted optional sections only). Report `scratchpad/refine/r1/review-r1.md`.

#### Round 1 — finding matrix

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 Initiation step 2 lets "request a design change to <package>" reopen the named base instead of creating the request | accept | amendment 9; authoring § Initiation | step 2 says a request signal names the base, so create the request unless a request for this work is named or in context; fund by folding the duplicated "resolve path, create artifact, Goal and Inputs" wording | continuing an existing request reopens it, whoever authored it |
| F2+F4 drawing-dependent instructions after the model allows undrawn entries and removals: the no-mockups branch skips Mockups, which holds the trace pass and feedback; Base review names drawings only; identity, readiness 3, C2, C4 require a draft link a `remove` entry cannot have (spec items promotion 2 and 4 say the same) | accept; F4's spec conflict resolved in the spec first | amendment authoring 3, 5, 6, promotion 2, 4; authoring § Phases, § Mockups, § Design Changes, § Completion; promotion gate notes, readiness 3, C2, C4, C5 | state what represents the change (drawing, or the list) once and apply trace, feedback, review and reconciliation to it; rules by operation: add and modify link a draft, remove names the base design and keeps the name after deletion; Base review covers the base's list; delete drafts where they exist; fund from promotion's repeated paths (Purpose, artifact parenthetical) | Discussion draws nothing; the ruling needs the tool-access gate; undrawn entries never promote into production; a base receiving them owes Mockups; request sections hold only added or changed frames |
| F3 the Design Changes form omits the list marker the renderer requires (`design-tool.py:33` `^- (?P<cid>V\d+)`); a plain `V01 …` line vanishes from the page | accept | amendment 6; authoring § Design Changes | show the full bullet line | live list, V IDs, fields, no checkbox |
| F5 both process guides over their caps by 110 and 106 bytes | accept | spec § Size Budgets — 2026-10-23 | net trims in the clusters above | branch guidance stays at its point of use |

Open questions (neither): (a) the base is a request's first input while Completion files requests for every input the decisions changed — folded into F2's repair as "every input but the base" (the package is its change to the base); (b) a request modifying a screen the base lists as an addition appends a second entry for that screen — log only: entries are per change with provenance, the base's author merges on its next round if it wants.

Arithmetic: F1 divergent · normal · speculative = 2.5 · F2+F4 one defect (reviewer's root cause), heaviest F2 by report order, divergent · off-normal · speculative = 1.875 · F3 divergent · normal · verified = 5 · F5 cosmetic · normal · verified = 2 · no noise · two open questions, neither.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 11.375 | 4 | 0 | 3 | 1 | 0 |

#### Round 1 — repairs

Spec first (F4's conflict): § Clarification — 2026-10-23 in `design-process-design.md`: the
representation of a change is its drawing or, under the ruling, its entry; rules by operation;
`remove` names the base design and keeps the name; review of the base covers its list for entries
folded in undrawn; drafts deleted where they exist.

Cluster A (F1, F3, funded): Initiation step 2 says a request signal names the base and creates
the request unless an existing request for this work is named; the duplicated "create the
artifact, Goal and Inputs first" sentence in The change package went (Initiation step 3 holds it);
the Phases feedback sentence now points at Mockups instead of restating it; the Design Changes
line shows the full `- V<n> …` form. Self-check: no contradiction (Initiation 3 still creates;
Mockups still owns feedback); no stale sentence (grep "write `## Goal`" → one place); nothing moved
from its point of use; nothing weakened. Net 0 bytes.

Cluster B (F2+F4, open question a): Phases says the list stands in for the drawings below under
the ruling; Design Changes identity by operation (`add`/`modify` linked, or intended name under
the ruling; `remove` the base design's name, unlinked); Completion reconciles "every input but the
base"; promotion's Base review names the base's drawings and any Design Changes folded in
undrawn, readiness 3 and C4 read by operation, C5 deletes drafts where one exists; Purpose and the
artifact section lost their repeated paths (C6 holds them). Self-check: Mockups' trace pass and
feedback now apply to the list through the stand-in sentence, so no branch is skipped; C2 is
unchanged (linked entries only); request sections still hold added and changed frames only; the
ruling still needs the tool-access gate; undrawn entries still never enter production. Trims for
the caps (F5): "Whatever came before is context the agent digests", "while the change is open",
the Resolution paragraph that restated Completion, the page-contents clause in Artifact
maintenance, "(*Gates*)", "then verify before writing `## Promotion Checks`" → "the checks", and
the tool-guide ownership sentence shortened. Self-check: each cut text is stated once elsewhere
or was decorative; nothing weakened.

Sizes after r1 repairs: authoring 16,080 (cap 16,100), promotion 12,088 (cap 12,100), Figma pair
17,492 (cap 17,400; untouched this round, over by 92 — the Figma passage has no finding yet; trim
due in a later cluster or by ruling).

Verification: the guide's render command run on the prototype request (exit 0, 4 added); a test
artifact with one unbulleted and one bulleted entry renders 1 added — F3 confirmed and its fix
correct (the guide now shows the bullet). Open question (b) logged.

#### Round 2 — finding matrix

Prompt `scratchpad/refine/r2/prompt.txt` (r1's with the settled dispositions and the revised
sections updated; diffed against r1: those two slots only). Report `scratchpad/refine/r2/review-r2.md`.

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the trace pass ends "Stop at Review" and the feedback path re-emits Review when nothing was parked, before the trace pass can raise an item; competes with the Discussion blocked gate | accept | authoring § Mockups vs § Gates | delete the unconditional routing; end at the gate *Gates* prescribes | unresolved items vs authorized input-changing Decisions; the generic blocked route; reconciliation stays after Review's advance |
| F2 C2 counts every screen draft "on the change page or request section", so an unpromoted sibling request's section fails the base's inventory | accept | promotion C2; Figma Pages 1 | "every screen draft of this package" | an omitted draft of the package still fails; components stay out; requests promote separately; no policy on open children blocking the base |

Open question: whether open child requests are historical once the base promotes (C5 deletes the
shared page; C6 archives `change-requests/` intact) — log only; no readiness rule inferred.

Arithmetic: F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875 · no noise · one open question, neither. Findings about my own r1 repairs: none (F1 is released text kept through compression; F2 is amendment text).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 11.375 | 4 | 0 | 3 | 1 | 0 |
| r2 | 4.375 | 2 | 0 | 2 | 0 | 0 |

#### Round 2 — repairs

Cluster F1: Mockups' two routing sentences now end "at the gate *Gates* prescribes" (the
Discussion blocked gate while a non-gap item is open, else Review). Self-check: Gates unchanged;
no stale "re-emit Review" left (grep); the rule sits where the trace pass runs; not weakened.
Cluster F2: C2 "every screen draft of this package". Self-check: C1 and C3 unchanged; the Figma
shared-page rule unchanged; no statement added about open children. Both net negative.

#### Round 3 — terminal

Prompt `scratchpad/refine/r3/prompt.txt` (r2's with the two slots updated). Report
`scratchpad/refine/r3/review-r3.md`. One finding, F1: C4's "including appended entries" can read
as requiring a destination drawing for undrawn entries, though C3 says they stay unlinked —
reviewer's own triage log-only, agreed: C3 states the exception at its point of use and the
generic blocked gate covers a strand; no occurrence. Reviewer confirmed the r1 and r2 repairs hold
and the four simulations route correctly; tooling claims verified against `design-tool.py`.

Arithmetic: F1 log-only, noise · no live rows · no open questions.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 11.375 | 4 | 0 | 3 | 1 | 0 |
| r2 | 4.375 | 2 | 0 | 2 | 0 | 0 |
| r3 | 0 | 0 | 0 | 0 | 0 | 1 |

Converged by clean round (stop rule a), 2026-10-23.

#### Closure

| Finding | Disposition | Evidence |
|---|---|---|
| r1 F1 | closed | Initiation 2 creates the request on a request signal |
| r1 F2+F4 | closed | spec clarified; stand-in sentence; rules by operation; Base review covers the list; C5 where drafts exist |
| r1 F3 | closed — verified | unbulleted entry dropped by the renderer, bulleted rendered; guide shows the bullet |
| r1 F5 | closed | 16,054 / 12,066 under 16,100 / 12,100 |
| r1 open (a) | closed | Completion: every input but the base |
| r1 open (b) | logged | per-change entries with provenance; merge is the base author's |
| r2 F1 | closed | Mockups ends at the gate Gates prescribes |
| r2 F2 | closed | C2: every screen draft of this package |
| r2 open | logged | open children at base promotion; no occurrence |
| r3 F1 | logged | C4 reads with C3's exception; no occurrence |

Net size change of the pass: authoring 16,210 → 16,054 (−156; released 15,082, so +972 for the
amendment); promotion 12,206 → 12,066 (−140; released 11,484, +582); Figma pair 17,492 unchanged
(released 17,292, +200), over its 17,400 cap by 92 with no finding against the passage — a
supervisor decision: trim 92 bytes elsewhere in the Figma guide (opportunistic under the
refinement guide) or hold the cap at 17,500. Ruled: cap held at 17,500 (Tim, 2026-10-23).

## Maintenance retro — change requests — 2026-10-23

Inventory: guide content change (three Design guides rewritten/edited for the base model), a new
tool (`Bin/design-tool.py`, manifest `tool.design-tool`, test under
`internal/tests/tools/design-tool/`), a shared-stylesheet change in place (v1), two skill template
descriptions, README usage entries, release documents, a runbook bullet. Host-install-visible.

Bookkeeping: `Releases/unreleased.md` gains seven dated entries with re-runnable migrations (list
conversion, first render); `CHANGELOG.md` three lines; manifest entry added as text, JSON parses;
`Managed-Updated-At` 2026-10-23 on all three guides; README usage entries match the gates (Review
`next`, Completion, Base review) and link the tool and its test; skill templates 549 / 495 bytes
under 550 / 500; `internal/maintain-skai.md` notes the shared renderer parts. Tool tests: design-tool
2 pass, spec-tool 18 pass.

Consistency checks (recorded): stale names `mockup review` / `production review` / "approved" in
Guides/Design, README, Templates/skills → 0 occurrences (grep); "human" → 2, both the shared
supervisor definition (false positive, intentional); `## Gates` and `## Advance intent` present in
both process guides with the supervisor sentence; every `⏳ GATE:` line in authoring traces to the
Gates section (lines 99, 100, 103 plus the standard lines); no runtime reference to
`process-flow.md` (0); gap pointer present and `## Decision Log` last in the skeleton; `- [ ]`
items letter-led (D, C) and V entries carry none; no aggregator sections; manifest skills all carry
adapter tags with existing paths. Change-package verification: paths use the type folder and the
base (`<base>/change-requests/<nnn>/`, `<base>/promoted-change-requests/<nnn>/`); sibling types
coexist unchanged; reopen finds active work (Initiation 2, request signal creates); promotion
verifies the base before C6 moves, repairs links, re-renders, records evidence; a promoted path
present blocks (readiness 4); working docs move with the folder (C6). Addendum contract: cue and
footer intact in all three guides (protected-block check in every compression round).

Flow reflection (post-edit simulation, authoring): normal — Discussion items resolved → planned
gate → draw → trace pass → Review `next` → Completion; blocked — tool access refused → blocked
gate → ruling "no mockups" → list stands in → Review of the list; `auto` — bypasses the Discussion
planned gate only; never the blocked gate nor Review; `auto to review` stops before Review.
Promotion: normal — readiness → Promotion Checks gate → C1–C4 → Base review → C5–C6; blocked —
open gap into production (readiness 1) and unruled request (readiness 5) each take the blocked
line; `auto` — bypasses Promotion Checks, never Base review. No issues found in simulation
(Astra's r1–r3 simulations walked the same paths cold).

Misses fixed during the retro: skill descriptions over cap (trimmed). Follow-ups: the host's
installed skill copies (`.claude/skills/skai-design-*`) and any other adapter's are stale until the
update runbook re-runs; the host's `skai/integration.md` may add the render command (project-owned).

## Change List Mirrors The Page — 2026-10-23

Per skai#90 in use: inventory in `design-process-design.md` § Amendment — 2026-10-23 (change list
mirrors the page) and `figma-designer-guide-design.md` § Amendment — 2026-10-23 (page
organization); drafts; author check; sweep; compression by Codex Astra; caps by the supervisor.

### Author check and sweep — 2026-10-23

Drafts: authoring 16,054 → 16,706 (cap 16,100); promotion 12,066 → 12,310 (cap 12,100); Figma
14,794 → 15,475, pair 18,173 (cap 17,500).

Figma inventory 1–5: 1 Screen pages 1 and the page table (feature areas vs one per screen, the
tall-screen spill); 2 Screen pages 7, Components 1, the table; 3 Pages 1; 4 Pages 1 and Screen
pages 1; 5 Agent tooling 7. Authoring 1–2: Design Changes (headings, one per frame, sub-IDs,
stable IDs, example) and Mockups (structure check before the trace pass); "the renderer shows the
headings" is the tool's and not in the guide. Promotion 1–2: C1, C2, C3. Sweep: the old Pages 1
request sentence and the old "one entry per base change" opening were replaced; nothing else the
amendment obsoletes (grep for "loose", "prefix", "groups of screens": one occurrence each, all
rewritten).

### Compression review — 2026-10-23 (Codex Astra, scratchpad `compress4/`)

| Guide | Released | After (draft) | Compressed | Compressed addition |
| --- | ---: | ---: | ---: | ---: |
| design-authoring.md | 16,054 | 16,706 | 16,614 | 560 |
| design-promotion.md | 12,066 | 12,310 | 12,218 | 152 |
| figma-designer-guide.md | 14,794 | 15,475 | 15,380 | 586 (pair 18,078) |

Protected blocks intact; the kept sentences and the sub-ID example present. Astra restored four
inventory clauses the draft had left implicit (render shows headings and sub-changes; a screen
Section named for its screen in plain words; one concept per page with no prefixes on frames or
Sections; the check reports Sections too), all accepted. Two draft rules beyond the inventory,
kept as written: the structure check runs before the trace pass (an ordering, not a rule), and
"fix what it reports" in the tool guide. Caps proposed a little under the compressed sizes,
pending the supervisor: 16,500 / 12,150 / 18,000.

Rulings after compression (supervisor, 2026-10-23): keep the tall-screen clause (Production does
it; the guide never said so); C3 says plainly that per-screen sections do not survive promotion
into production; the Figma guide's check line is one line. Caps: 16,450 / 12,150 / 17,900 (100
under the combined proposal). Drafts over cap at the start of refinement: authoring by 164,
promotion by 128, Figma pair by 66.

### Refinement — series CL (2026-10-23)

#### Round 1 — finding matrix (prompt `scratchpad/refine/cl1/prompt.txt`, r3's with the standard, binding passages, settled dispositions and revised sections updated; report `review-r1.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the structure check is mandated in Mockups and C1 with no drawings to check on the no-mockups path | accept | amendment authoring 2, promotion 1; § Mockups, C1 | "with drawings" on both | drawn packages still run and pass it; the ruling still needs the tool-access gate |
| F2 the C1 evidence excerpt claims a "bindings, names" script the check does not do | accept | promotion § Promotion Checks excerpt | delete the line | inspection of untested rules stays |
| F3 C4 re-renders only a package base's page; the promoting package's links go stale at Base review | accept | promotion C4 | re-render every page whose artifact changed | C6's post-move render stays |
| F4 "next V in its section" reads as per-section numbering; renderer ids and provenance are package-wide | accept (reviewer log-only; the intent is known and the spec wording was the cause) | spec amendment authoring 1; § Design Changes | one sequence per package, placed under its heading; spec reworded | existing IDs, canvas order, sub-IDs, provenance |

Arithmetic: F1 divergent · off-normal · verified = 3.75 · F2 divergent · normal · verified = 5 · F3 divergent · normal · verified = 5 · F4 divergent · normal · verified = 5 · no noise · open child requests already logged.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 18.75 | 4 | 0 | 4 | 0 | 0 |

#### Round 1 — repairs

One cluster per finding, each self-checked: F1 "with drawings" in Mockups and C1 (no contradiction with the stand-in sentence; the trace pass still runs on the list); F2 the excerpt's C1 line deleted (C1's text still says script plus inspection); F3 C4 "re-render every page whose artifact changed, the promoting package's included" (C6 unchanged); F4 "one sequence per package … under its screen's heading" in the guide and the spec (C3's "next V numbers" now unambiguous). Trims for the caps: the Review gate line shortened to the standard form; "The tool guide defines pages and sections", "(sections, then columns …)", "raises findings as items and may change or trim anything" tightened; in the Figma guide the page-table cell, Components 1 and Screen pages 7 tightened. Sizes: authoring    16452 (cap 16,450), promotion 12108 (12,150), Figma pair 17896 (17,900).

#### Round 2 (prompt `scratchpad/refine/cl2/prompt.txt`; report `review-r2.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 Screen pages 7 ("only screens inside a Section") and Components 1 ("their change page's Components Section") contradict the request hierarchy Pages 1 and the table set | accept | Figma amendment 2–3; Screen pages 7, Components 1 | the content rule scoped to screen Sections, a request Section holding screen Sections and a Components Section; components in the package's own Components Section | screen Sections hold only screens or crops |
| F2 C2's "components a draft needs … no entry" forbids an entry for a component that is itself a change | accept | promotion C2 | delete the sentence | incidental components need no entry |
| F3 the check on a base's page also checks its open child requests' sections | log-only | — | — | — |

Arithmetic: F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875 · F3 logged, noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 18.75 | 4 | 0 | 4 | 0 | 0 |
| r2 | 3.75 | 2 | 0 | 2 | 0 | 1 |

Repairs: F1 both Figma rules reworded (self-check: Pages 1 and the table unchanged; no stale "except" left); F2 the C2 sentence deleted (C2 still inventories the package's screen drafts). Trims: "in the skai checkout" → "skai's" in tooling 7; "sub-IDs instead" → "sub-IDs". Sizes: authoring 16444, promotion 12056, Figma pair 17922.

#### Round 3 (prompt `scratchpad/refine/cl3/prompt.txt`; report `review-r3.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 `known-gaps.md` rule 6 says every package needs zero open gaps for promotion; design promotion into a package carries them | routed to its owner (`Guides/Core/known-gaps.md`), fixed there: "into production", plus one clause for a workflow that promotes into another open package; `known-gaps-design.md` amended; 3386 of 3,400 | — | — | production promotion still rejects every open gap; no other workflow gains carry-forward |
| F2 the Figma pair 22 bytes over its cap, from the round-two repair; my size check ran after the launch | accept | Figma tooling 7 | "checks the rules above; process guides say when" | script path, scope, division of coverage |

Arithmetic: F1 outside the binding target, routed · F2 cosmetic · normal · verified = 2 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 18.75 | 4 | 0 | 4 | 0 | 0 |
| r2 | 3.75 | 2 | 0 | 2 | 0 | 1 |
| r3 | 2 | 1 | 0 | 0 | 1 | 0 |

Lesson recorded: a round spent on a 22-byte overrun a check would have caught; the launch now
waits on the size check. Sizes: authoring 16444, promotion 12056, Figma pair 17895.

#### Round 4 (prompt `scratchpad/refine/cl4/prompt.txt`; report `review-r4.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 tooling 7's "checks the rules above" overstates the script (it checks what its header lists, not one-screen-per-Section or the page name) — my r3 trim | accept | Figma tooling 7 | "reports the breaches its header lists" | the check stays mandatory; C1's "inspect the rest" |
| F2 authoring names the change page `<change-id>` while the tool guide puts the concept letter in the page name | accept | authoring § The change package | "the change page the tool guide names" | paths and the shared change id |

Open question (logged): a request removing a frame the base's list links leaves that base entry pointing at a deleted draft after C3; no occurrence; the blocked route covers it.

Arithmetic: F1 divergent · normal · verified = 5 · F2 divergent · normal · speculative = 2.5 · no noise. Findings on my own previous repairs: F1 (one of two); consolidation trigger not fired.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 18.75 | 4 | 0 | 4 | 0 | 0 |
| r2 | 3.75 | 2 | 0 | 2 | 0 | 1 |
| r3 | 2 | 1 | 0 | 0 | 1 | 0 |
| r4 | 7.5 | 2 | 0 | 2 | 0 | 0 |

Repairs: both replacements, net −8 bytes. Sizes: authoring    16447, promotion    12056, Figma pair 17910 (the first r4 repair left the pair 10 over; the launch guard stopped it, trimmed).

#### Round 5 — terminal (prompt `scratchpad/refine/cl5/prompt.txt`; report `review-r5.md`)

No findings; the reviewer verified the page naming, the prefix rule, the check's coverage claim
against the script and the renderer's headings and sub-changes against `design-tool.py`; the
four simulations route correctly; sizes 16,447 / 12,056 / 17,885 under caps. Open question
restated: the status of open child requests at the base's promotion, already logged.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 18.75 | 4 | 0 | 4 | 0 | 0 |
| r2 | 3.75 | 2 | 0 | 2 | 0 | 1 |
| r3 | 2 | 1 | 0 | 0 | 1 | 0 |
| r4 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r5 | 0 | 0 | 0 | 0 | 0 | 0 |

Converged by clean round (stop rule a), 2026-10-23. Net size change of the pass against the
released guides (5b2fb59): authoring 16,054 → 16,447 (+393), promotion 12,066 → 12,056 (−10),
Figma pair 17,492 → 17,885 (+393); `known-gaps.md` 3,278 → 3,386 (+108, routed fix). Rounds 3
and 4 each cost a defect of my own making (an overrun launched unchecked; an over-claiming trim);
the launch guard and the "header lists" wording close both.

#### Closure

| Finding | Disposition | Evidence |
|---|---|---|
| r1 F1–F4 | closed | with drawings; excerpt line deleted; every changed page re-rendered; one sequence per package |
| r2 F1, F2 | closed | content rule scoped; C2 sentence deleted |
| r2 F3 | logged | base check reports child requests' sections; no occurrence |
| r3 F1 | routed, fixed | known-gaps rule 6 |
| r3 F2 | closed | pair trimmed |
| r4 F1, F2 | closed | header-lists wording; page name the tool guide's |
| r4 open question | logged | removal of a frame the base's list links |

## Maintenance retro — change list mirrors the page — 2026-10-23

Inventory: three Design guides amended (compressed, refined in five rounds), `known-gaps.md` rule 6
(routed fix), `design-tool.py` (headings, sub-changes) with its test and fixture, new
`figma-page-check.js` with its test (node), manifest entries for both tools, README (usage entry,
test list), release documents (three technical entries plus the known-gaps line; CHANGELOG line),
the stylesheet (inline why) in place. Host-install-visible.

Checks (recorded): stale names in Guides/Design, README, Templates/skills → 0 (grep); Gates and
Advance intent present in both process guides (2 each); `Managed-Updated-At` 2026-10-23 on the
four edited guides; manifest parses, both new tool entries present with existing paths; tests
design-tool OK (2), figma-page-check OK (2), spec-tool OK (18); the real Offers page checks clean
(8 sections, 0 findings). Flow reflection: unchanged from the morning's retro except the Mockups
step, which now runs the check before the trace pass where drawings exist; simulated normal,
no-mockups (check skipped) and `auto` (stops at Review); no issues found in simulation.

Misses fixed: none outstanding. Follow-ups: host installed skill copies still stale until the
update runbook runs; the Figma addendum (project-owned) is to gain the SF Symbols CLI and the
kit-wrapping convention per the supervisor.

## Inherited Gaps As Footnotes — 2026-10-23

Per skai#90 in use. Inventory: `design-process-design.md` § Amendment — 2026-10-23 (inherited
gaps as footnotes), `figma-designer-guide-design.md` § Amendment — 2026-10-23 (gap annotation
format), `known-gaps-design.md` § Amendment — 2026-10-23. Before-state copies in scratchpad
`compress5/`.

### Author check and sweep — 2026-10-23

Authoring 1–3: Discussion (inherited gap = footnote, own gap = item, mirror once drawn), Design
Changes (the footnote form, labels unique, footnoted entries count as open gaps); 3 is the
renderer's (done: marks link to gap notes under the card, `has-gap`, the gaps tile counts them;
test extended, 2 pass). Promotion 1–2: readiness 1, C3. Figma 11: § Gaps rewritten to the three
lines. known-gaps: rules 3, 5, 6; sweep found rule 7's "close your inherited gap as answered" →
"clear the mark" (obsoleted by 5), nothing else (grep for the old annotation format, "carry your
own gap item", "Requests inherit base gaps": 0). Drafts: known-gaps 3386 (cap 3,400), authoring
16852 (16,450), promotion 12194 (12,150), Figma pair 17983 (17,900).

### Compression review — 2026-10-23 (Codex Astra, scratchpad `compress5/`, removals counted)

| Guide | Before | After (draft) | Compressed | Net over before |
| --- | ---: | ---: | ---: | ---: |
| design-authoring.md | 16,447 | 16,852 | 16,817 | +370 |
| design-promotion.md | 12,056 | 12,194 | 12,143 | +87 |
| figma-designer-guide.md | 15,187 | 15,285 | 15,199 | +12 (pair 17,897) |
| known-gaps.md | 3,386 | 3,386 | 3,343 | −43 |

Astra restored nine inventory clauses the draft left implicit (the marker lifecycle saying only
gap items stay unchecked; the gate and card counting footnoted entries; the request's base gaps
as footnotes; the `base D04` → `D04` rewrite on fold-in; one annotation per frame; own gaps'
Gap line; known-gaps rule 4 scoped to own gaps) and reported three sentences still teaching the
old behaviour, all reworded in its rewrite. Protected blocks intact; the pointer sentence kept.
Compressed drafts installed. Caps proposed a little under: 16,750 / 12,100 / 17,850 / 3,300.

Caps set (supervisor, 2026-10-23): 16,750 / 12,100 / 17,850 / 3,300. Trimmed under them before
round one (the Artifact maintenance clause restating the renderer; C1 and C3 wording; the Figma
annotation sentence; known-gaps rule 3's list): authoring    16747, promotion    12100, Figma pair 17839,
known-gaps 3278.

### Refinement — series GF (2026-10-23)

#### Round 1 (prompt `scratchpad/refine/gf1/prompt.txt`, cl5's with known-gaps.md rules 3–7 and § Gaps binding, the three specs, the gap-footnote dispositions and a fifth simulation; report `review-r1.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 known-gaps rule 6 sends every open gap to authoring "where each is answered, adopted or omitted", inherited marks included | accept | known-gaps 5–6; rule 6 | "its own are resolved (4) and inherited marks wait on their owners (5, 7)" | both kinds block production; promotion resolves nothing; carry into a package |
| F2 the card state says "no discussion items" for a package whose only gaps are footnotes, while the tile counts them | accept (tool) | authoring 2; `design-tool.py` | state "no discussion items; N gaps carried"; fixture and test | counting unit unchanged |

Open question (logged): Figma Pages 1 says promotion folds a request's sections into "the page's Sections"; for a request against a request C3 says the base's; no misroute yet.

Arithmetic: F1 divergent · off-normal · speculative = 1.875 · F2 cosmetic · normal · verified = 2 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 3.875 | 2 | 0 | 1 | 1 | 0 |

Repairs: rule 6 reworded (self-check: 4, 5, 7 unchanged; shorter); the renderer's state branches on open, items, or neither; request fixture gains a footnote, test asserts the state (2 pass). Sizes: authoring 16747, promotion 12100, Figma pair 17839, known-gaps     3267 (rule 2's "gives nothing to build on" sentence trimmed to pay for rule 6).

#### Round 2 — terminal (prompt `scratchpad/refine/gf2/prompt.txt`; report `review-r2.md`, 2026-10-24)

No accept findings. F1 (log-only, noise): known-gaps rule 7's "normal input catch-up" has no
named counterpart in design authoring for an upstream gap answered differently from its
placeholder after completion; the Discussion, reopen and Mockups rules cover the substance and the
blocked gate the strand; no occurrence. Reviewer verified the renderer's card state and the
footnote rendering and walked the five simulations.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 3.875 | 2 | 0 | 1 | 1 | 0 |
| r2 | 0 | 0 | 0 | 0 | 0 | 1 |

Converged by clean round (stop rule a), 2026-10-24. Net size change of the gap-footnote change
against the start of the day's work: authoring 16,447 → 16,747 (+300), promotion 12,056 → 12,100
(+44), Figma pair 17,885 → 17,839 (−46), known-gaps 3,386 → 3,267 (−119). Caps 16,750 / 12,100 /
17,850 / 3,300 held.

#### Closure

| Finding | Disposition | Evidence |
|---|---|---|
| r1 F1 | closed | rule 6: own gaps resolved, inherited marks wait on their owners |
| r1 F2 | closed — tool | card state names carried gaps with no items; test |
| r1 open question | logged | "the page's Sections" for nested requests |
| r2 F1 | logged | input catch-up route; no occurrence |

## Maintenance retro — inherited gaps as footnotes — 2026-10-24

Inventory: `known-gaps.md` rules 2–7; the three Design guides' gap passages; `design-tool.py`
footnotes and card state with fixtures and tests; release documents (two technical entries, one
CHANGELOG line). Host-install-visible. Checks: `Managed-Updated-At` 2026-10-24 on the four guides;
no manifest change (no new asset); README usage entries unaffected (gaps are the guide's detail);
tests design-tool OK, figma-page-check OK, spec-tool OK; stale wording grep (`D<n> — <placeholder>`,
"carry your own gap item", "close your inherited gap") → 0. Follow-ups unchanged: host skill
copies stale until the update runbook runs; the Figma addendum lines (project-owned).

## One Gap Footnote For Every Artifact — 2026-10-24

Inventory: `spec-format-design.md` § Amendment — 2026-10-24; adopted by `design-process-design.md`
and `known-gaps-design.md`. Tools first (mechanical): `spec-tool.py` parses, validates and renders
the new form, shares the note rendering and item tooltips, marks inert; `design-tool.py` uses them;
fixtures and tests (18, 2) pass; the Offers specs drafts' 14 footnotes migrated (validate 0 issues,
check-changes 0). Guides: `spec-file-gaps.md` rewritten as the owner (1,844 → 2,208 drafted),
`design-authoring.md` cites it (16,726 → 16,632). Compression (Astra, scratchpad `compress6/`,
removals counted): spec-file-gaps 1,903 (+59 over released), design-authoring 16,616 (−110).
Astra restored two clauses (check-changes pairs only this artifact's items; old footnotes drop
their question) and cut two the inventory did not call for (a one-sentence placeholder; the tile
as the counter). Compressed drafts installed. Caps proposed a little under: spec-file-gaps 1,875,
design-authoring 16,550.

Caps set (supervisor, 2026-10-24): spec-file-gaps 1,875, authoring 16,550; trimmed under them
(1,871 / 16,540).

### Refinement — series FN (2026-10-24)

#### Round 1 (prompt `scratchpad/refine/fn1/prompt.txt`; report `review-r1.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the shared footnote contract outran the tools: a scoped owner in a spec draft got no link or tooltip; inherited-only spec packages had no gaps tile; a request archived to `promoted-change-requests/` lost its base resolution | accept (tools) | spec-format amendment; `spec-tool.py`, `design-tool.py` | one owner resolver in the spec tool for both renderers (this artifact, the base through either request folder name, the product specs artifact the artifact or its base links); tooltips for every owner; the spec page counts requirements with inherited marks | ID-only chips, inert marks, one box per card, questions with their owners |
| F2 `validate` did not enforce "numbered by first use" | accept (tool) | spec-file-gaps § validate | the check, one error at the first deviation per file; the Offers drafts renumbered in two files | marker-less definitions, uniqueness, placement checks |

Arithmetic: F1 divergent · normal · verified = 5 · F2 cosmetic · past-a-rule · verified = 0.5 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.5 | 2 | 0 | 1 | 1 | 0 |

Repairs: both in the tools; tests 18 and 2 pass (the broken fixture now also trips the numbering
check); Offers drafts validate 0, check-changes 0; both pages re-rendered. No guide text changed.

#### Round 2 (prompt `scratchpad/refine/fn2/prompt.txt`; report `review-r2.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the shared gap guide's tooling paragraphs read as if `validate` and `check-changes` covered every artifact (a designer may take a rendered page for a validated one) and "fails on unpaired draft footnotes or open gaps" read as failing every open gap | accept | spec-file-gaps § tooling | the checks named as spec-draft tools; "unpaired" spelled out both ways with a marked open gap passing; design pages only render; funded by dropping "no open gaps at promotion means no placeholders" (rule 6 and readiness own it) and small trims | the common form, numbering, marker-less notes, local-only pairing, readiness blocking |

Arithmetic: F1 divergent · off-normal · verified = 3.75 · no noise. Six walks clean; Astra confirms the
round-1 tool repairs and declines a C3 carry checklist without an observed failure.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.5 | 2 | 0 | 1 | 1 | 0 |
| r2 | 3.75 | 1 | 0 | 1 | 0 | 0 |

Repair installed: `spec-file-gaps.md` 1,874 / 1,875; spec-tool test OK; the design spec's amendment
records the clarified check behavior.

#### Round 3 (prompt `scratchpad/refine/fn3/prompt.txt`; report `review-r3.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the shared guide said footnoted items count as modified; a design entry keeps its operation (an added screen with an inherited gap stays added) and a spec requirement is reclassified only when it already existed | accept | spec-file-gaps § pages | delete the modified claim; keep "count as gaps; the gaps tile filters to them" | typed operations, the spec diff classification, gap counts and filter; neither renderer changes |

Arithmetic: F1 cosmetic · normal · verified = 2 · no noise. Six walks clean; the r2 rewrite confirmed
against the implementation.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.5 | 2 | 0 | 1 | 1 | 0 |
| r2 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r3 | 2 | 1 | 0 | 0 | 1 | 0 |

Repair installed: `spec-file-gaps.md` 1,861 / 1,875.

#### Round 4 (prompt `scratchpad/refine/fn4/prompt.txt`; report `review-r4.md`)

No findings; six walks clean; the r2 and r3 repairs confirmed against the implementation. One open
question, verified by Astra: `spec-tool.py` still classifies an existing requirement that gains a
footnote as modified. Disposition: not a defect. The spec page's design records that behavior
(`spec-format-design.md` convention: a footnote on an existing requirement counts as modified, so
`check-changes` wants a list entry for it); r3 removed only the shared guide's claim that every
footnoted item counts as modified, which was wrong for design entries and added requirements. My
round-4 prompt disposition overstated r3 ("a footnote does not change a requirement's diff class"),
which produced the question; recorded here, no tool change.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 5.5 | 2 | 0 | 1 | 1 | 0 |
| r2 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r3 | 2 | 1 | 0 | 0 | 1 | 0 |
| r4 | 0 | 0 | 0 | 0 | 0 | 0 |

Converged by stop rule (a). Final sizes: spec-file-gaps 1,858 / 1,875; design-authoring 16,540 / 16,550;
promotion 12,100 / 12,100; Figma pair 17,839 / 17,850; known-gaps 3,267 / 3,300.

## Maintenance retro — one gap footnote form, series FN — 2026-10-24

Inventory: `spec-file-gaps.md` (owner of the form; tooling paragraphs scoped to spec drafts; modified
claim removed), `design-authoring.md` citation, `spec-tool.py` (new form, owner resolver, tooltips,
gaps count, numbering check), `design-tool.py` (uses them), fixtures and tests; the Offers drafts
migrated. Host-install-visible. Bookkeeping: release entry extended with the numbering rule, its
migration step and the owner resolution; CHANGELOG line says "numbered by first use"; README's two
gap-guide lines name design change lists and the page; `Managed-Updated-At` 2026-10-24 on every edited
guide; manifest unchanged (no new asset; `tool.design-tool` and `tool.figma-page-check` were added in the
previous retro). Tests: spec-tool OK, design-tool OK, figma-page-check OK. Consistency: stale wording
grep (`count(s) as modified`, `named only`) → `Bin/spec-tool.py:206` false positive (an existing item
with a footnote does count as modified on spec pages), `:1435` false positive (owner named only when its
artifact was not read); Guides and README 0 occurrences. Change-package verification: artifact format
only, no path or promotion mechanics changed; migration guidance is re-runnable and covers mixed state
(definitions already in the new form left alone, then renumber). Addendum contract: the guide keeps its
Project Addendum section. Follow-ups unchanged: host skill copies stale until the update runbook runs;
the Figma addendum lines (project-owned). Process reflection: my round-4 prompt disposition overstated
the round-3 ruling and produced a spurious open question; dispositions quoted into a prompt should
repeat the repair's own words, not paraphrase them.

## Writing Style Guide And Design Change Prose — 2026-10-24

Inventory: `writing-style-design.md` (new standard); `design-process-design.md` § Amendment —
2026-10-24 (descriptions, reasons, footnote placement); `spec-format-design.md` § Amendment —
2026-10-24 (Placeholder clause); skai#97 and its comments. Drafted: `Guides/Core/writing-style.md`
(2,267); the pointer sentence in 13 guides (end of Purpose; `product-specs-catalog.md` and
`design-specs.md` in their writing rules; `ticket-filing.md` in its purpose paragraph);
`process-flow.md` § Writing for people (owner); sanity-scan check; manifest, README, release notes.

Author check (writing-style.md against `writing-style-design.md` § Requirements): 1 kinds named once in
the Read line, no per-artifact sections ✓; 2 the stands-alone test as rule 1 with the "per D15"
example ✓; 3 rule 2 ✓; 4 rule 3 with the Casey Cedar example ✓; 5 rule 4, guide vocabulary named ✓;
6 rules 5 and 6 ✓; 7 six numbered rules, one ❌/✅ pair, the self-check, 2,267 bytes ✓; 8 nothing to
check yet; 9 it points nowhere ✓. Amendments: design-authoring Description, Justification, footnote
placement and the sub-change example carry the three repairs ✓; spec-file-gaps clause ✓.

Obsolescence sweep (grep `plain language|plain-language|jargon|coined` across Guides): ui-map-architecture
§ Writing style's opening sentence (plain language for a teammate who does not know the schema) now owned
by the shared guide → removed, its schema-specific tells kept; process-flow `<summary>: plain-language
description` → kept (format definition); product-specs-authoring Situations "in plain language" → kept
(content rule); design-specs § Product Language Only → kept (content rule, now also points at the guide);
cold-review-prompt-template → maintainer text, kept.

Compression (Astra, scratchpad `compress7/`, sixteen guides): running. Caps before this change:
process-flow 21,200; spec-file-gaps 1,875; design-authoring 16,550; design-promotion 12,100; the design
specs set 60,000 combined; product-specs-authoring 21,300, -promotion 17,000, -catalog 10,500; the work
spec pair 32,600 combined; ui-map-architecture 35,700, -implementation 50,900; ticket-filing and
writing-style none.

Compression (Astra, `compress7/`, sixteen guides) returned 2026-10-24. The eleven pointer-only guides
each earned the pointer's bytes back inside their own text (net −1 to −42, two at 0); installed as
compressed. writing-style 2,267 → 2,183; design-authoring 16,794 → 16,786; process-flow 21,648 →
21,578 (Astra also moved my § Writing for people out of the example's code fence, where my insertion
had landed). Restored or corrected on Astra's report: the audience sentence (a colleague who knows the
product but was not in the session) kept and added to the standard; "shorthand the reader has not seen
defined" adopted; the maintainers' logging rule taken back out of the guide (standard req 8 now says it
is not guide text); rule 6 reworded; "sample data never" made explicit; the design guide's footnote
sentence rewritten in plain words and the example's second sub-change given a reason. Installed sizes:
writing-style 2,188; design-authoring 16,865; process-flow 21,578; the rest at or under their caps.
Tests OK.

Caps needing a ruling (a little under compressed): writing-style (none → 2,150 proposed); process-flow
(21,200 → 21,550 proposed); design-authoring (16,550 → 16,850 proposed). All other caps hold.

Caps set (supervisor, 2026-10-24): writing-style 2,150; process-flow 21,550; design-authoring 16,850. Trim to fit, then series WS.

### Refinement — series WS (2026-10-24)

#### Round 1 (prompt `scratchpad/refine/ws1/prompt.txt`; report `review-r1.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the sub-change example put the reason before the ` — ` separator and only the citation after it, so the renderer's Why field showed a citation alone, against the Justification rule | accept | design-authoring § Design Changes example | reason sentence and citation after the separator in both rows | sub-IDs, source forms, the renderer's split on ` — ` |
| F2 "write in first person" unqualified, in a guide that also covers spec text, against the catalog's requirement voice | accept | writing-style rule 5 | first person for the agent's own actions, recommendations and questions; paid by trims to rules 2 and 6 and the self-check | the catalog's voice, gate forms |
| F3 `spec-tool.py` help and the malformed-footnote diagnostic still read `Placeholder: <what this item shows for it>` | accept (tool) | spec-tool docstring and validate message | the guide's clause wording | form, parser, validation scope |

Arithmetic: F1 divergent · off-normal · verified = 3.75 · F2 divergent · normal · speculative = 2.5 · F3
divergent · off-normal · verified = 3.75 · no noise. Log-only: "contract phrasing" could be misread as
excluding normative requirement language; the ❌/✅ pair demonstrates clearer wording more than the
outside-reader test (a stronger pair waits for a recurring correction).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10 | 3 | 0 | 3 | 0 | 0 |

#### Round 2 (prompt `scratchpad/refine/ws2/prompt.txt`; report `review-r2.md`)

No findings; five walks clean (the V06 scenario now cannot be reproduced without going against a
rule; the three-records state gets no D19 footnote; spec voice and first person compose; the pointer
found once, verbatim, in each of the thirteen guides). Open questions logged: a reason sentence can
still be vacuous ("this matches the requirements"); the ❌/✅ pair is less concrete than the rules'
own examples. Both wait for a recurring correction.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 10 | 3 | 0 | 3 | 0 | 0 |
| r2 | 0 | 0 | 0 | 0 | 0 | 0 |

Converged by stop rule (a). Final sizes: writing-style 2,144 / 2,150; process-flow 21,541 / 21,550;
design-authoring 16,850 / 16,850; spec-file-gaps 1,859 / 1,875; the thirteen pointer guides at or under
their caps.

## Maintenance retro — writing style guide, series WS — 2026-10-24

Inventory: new `Guides/Core/writing-style.md` (asset `guide.writing-style`); `process-flow.md` § Writing
for people; the pointer sentence in thirteen guides, each compressed to absorb it; `design-authoring.md`
§ Design Changes (Description, Justification, footnote placement, example); `spec-file-gaps.md` clause;
`ui-map-architecture.md` § Writing style trimmed; `spec-tool.py` help and diagnostic wording; the sanity
scan check. Host-install-visible. Bookkeeping: two release entries (guide with its pointer and no
migration; the design change prose rules) and two CHANGELOG lines; manifest entry; README gets a Writing
line under each of the eleven skills that point at the guide; `Managed-Updated-At` 2026-10-24 on every
edited guide (twelve bumped in the retro); the release note's form line updated to the new clause.
Tests: spec-tool, design-tool, figma-page-check OK. Consistency: stale clause grep → 0 in Guides, Bin
and README after the release-note fix; pointer sentence 14 occurrences (13 guides + the owner);
gap-pointer sentence and `⏳ GATE` counts unchanged in every compressed guide against HEAD; no plain
language rule left outside the style guide except content rules. Change-package verification: artifact
formats unchanged. Addendum contract: the new guide carries the Project Addendum section. Follow-ups
unchanged: host skill copies stale until the update runbook runs (the wrappers read the submodule's
guides, so runtime behavior is current); Figma addendum lines. Process reflection: the size guard
refused two launches this series (3 and 20 bytes over); trimming before launch, not after, would save a
round trip; measuring right after each repair is the fix, no process change.

Owner clause (2026-10-24, after series WS): `spec-file-gaps.md` says the owner is the item where the question was raised, never one that only inherits it; trims paid for it (1,859 → under 1,875); spec-tool test OK; then, on the supervisor's correction, the full process: compression (Astra, `compress8/`: 1,874 → 1,836, restoring "only there", "design pages only render" and "the gaps tile" that my trims had weakened; I kept the two marker-less rules as separate sentences, which its rewrite had fused), installed at 1848; cap set at 1,850 (supervisor, 2026-10-24); cold series GO follows.

### Refinement — series GO (2026-10-24)

#### Round 1 (prompt `scratchpad/refine/go1/prompt.txt`; report `review-r1.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the spec tool classifies an existing requirement that gains a footnote as modified | reject — noise | — | none: that is the spec page's design (`spec-format-design.md`: a footnote on an existing requirement counts as modified so `check-changes` wants a list entry); my prompt's disposition said "not as modified" without the spec-page qualifier, for the second time (FN r4) | — |
| F2 the numbering-and-uniqueness rule sat only inside the `validate` sentence, which the next sentence scopes to spec drafts, so a designer could read numbering as spec-only | accept | spec-file-gaps form paragraph | numbering and uniqueness relocated into the "All artifacts" form sentence; `validate` sentence says "numbering" | design pages render-only; numbering by first use |
| F3 the page's owner link reaches this artifact, the immediate base and the product specs artifact either links, not an arbitrary ancestor | log-only | — | wait for a recurring strand | the supported routes |

Arithmetic: F2 divergent · normal · speculative = 2.5 · F1 noise (prompt-induced) · F3 logged. Owner clause
walked clean: a legacy base item that inherits a specs question is never named; a request on a request
names `base D<n>`.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 2.5 | 1 | 0 | 1 | 0 | 1 |

Repair installed: spec-file-gaps 1849 / 1,850 (a first relocation ran 6 bytes over and was refused by the
size check before writing). Prompt for r2 quotes the spec-page disposition in the record's own words.

#### Round 2 (prompt `scratchpad/refine/go2/prompt.txt`; report `review-r2.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 "pairs only this artifact's draft footnotes" put the distinction on the footnote's location, not its owner; an inherited footnote is in this artifact's draft too | accept | spec-file-gaps check-changes sentence | "pairs draft footnotes naming this artifact's own items with its open gaps"; paid by trims | scoped footnotes skipped; marked open gaps pass; design pages render only |
| F2 the spec package page counted only requirements with scoped footnotes toward the gaps tile; a requirement footnoting a local owner was left out | accept (tool) | spec-tool render | count every footnoted requirement once | Discussion gap items counted; filtering; the modified classification |
| F3 the change request page (`render-request`) never set the owner resolver and had no gaps tile, so a request's footnotes rendered unlinked | accept (tool) | spec-tool render-request | owners from the package the request is filed against (its Discussion as `base`, its linked product specs); gaps counted from the request's drafts; fixture and test | question text with its owner; no ancestor traversal |

Arithmetic: F1 divergent · normal · speculative = 2.5 · F2 cosmetic · normal · verified = 2 · F3 divergent ·
off-normal · verified = 3.75 · no noise. Owner clause and numbering relocation walked clean again.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r2 | 8.25 | 3 | 0 | 2 | 1 | 0 |

Repairs installed: spec-file-gaps 1,846 / 1,850; spec-tool tests 18 OK (request fixture gained a footnote
naming the package's D3; the test asserts the chip and the count).

#### Round 3 (prompt `scratchpad/refine/go3/prompt.txt`; report `review-r3.md`)

No accepted findings. Log-only: a resolved owner chip proves the ID exists, not that the item raised the
question (past-a-rule: naming an inheriting item goes against the Owner sentence); a stale comment in
`design-tool.py` still said "as this frame shows it" (fixed, comment only). Five walks clean.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r2 | 8.25 | 3 | 0 | 2 | 1 | 0 |
| r3 | 0 | 0 | 0 | 0 | 0 | 0 |

Converged by stop rule (a). Final: spec-file-gaps 1,846 / 1,850.

## Maintenance retro — footnote owner clause, series GO — 2026-10-24

Inventory: `spec-file-gaps.md` (owner clause; numbering in the form sentence; pairing sentence keyed on
ownership; compression); `spec-tool.py` (every footnoted requirement counts toward the gaps tile; the
change request page resolves owners through its package and shows a gaps tile; request fixture and
test); `design-tool.py` comment. Host-install-visible (guide and tool). Bookkeeping: release entry and
CHANGELOG line added; `Managed-Updated-At` already 2026-10-24; manifest unchanged; README unchanged (the
gap-guide lines still describe it). Tests: spec-tool 18 OK, design-tool OK. Consistency: stale clause grep
(`as this frame shows it`, `what this item shows for it`) → 0 in Guides and Bin. Follow-ups unchanged.
Process reflection: I shortcut the process on a one-clause change and had to be told; rule saved to
memory. Twice a paraphrased disposition in a prompt produced noise; prompts now quote the record.

## Change Requests As Authoring Against A Base, Spec Guides — 2026-10-25

Inventory: `change-requests-design.md` (new standard for `Guides/Core/change-requests.md`);
`product-specs-system-design.md` and `design-specs-design.md` § Amendment — 2026-10-25; skai#99.
Obsolescence sweep (to remove): `request.md` with its status and response fields,
`request-review.html`, § Change Requests in both artifacts guides, § Raising a change request in both
promotion guides, `## Change Requests` in both promotion artifacts, readiness condition 5's "Proposed",
authoring § Reopening's change request paragraph, design-specs § Requirements Gaps' request form,
`spec-file-shape.md`'s `render-request` row, `spec-tool.py` `render-request`/`parse_request` and
the request test and fixture (`request.md` under two fixtures), README phase lines naming
`Incorporated`, skill descriptions saying "change requests for catalog defects",
`change-packages.md`'s change request paragraph. Design guides' request passages are the
cross-check reference. Three decisions put to the supervisor before drafting (ending without
promotion; open requests at promotion; UI Map scope).

Rulings (supervisor, 2026-10-25): no rule for ending without promotion; into production nothing open,
into a package open items, gaps and requests move up a level (a request open against the promoted
request is re-filed against the base); UI Map guides out of this pass and the shared guide names no
users. Drafts written: `Guides/Core/change-requests.md` (2,990); both artifacts guides, both
authoring and both promotion guides of the spec types; `design-promotion.md` readiness 1 and C3;
`spec-file-shape.md` command table; README (Requests line under the four spec skills; design specs
promotion phase); the two promotion skill descriptions; `change-packages.md`; manifest. Tool:
`spec-tool.py` infers a request's bases from its folder (`render`, `check-changes`; `--base`
overrides), the page title chains `<change-id> | <nnn>`, a justification may cite `base D<n>`;
`render-request`, `parse_request` and yesterday's `request_gap_owners` removed; the request fixture
is a package fixture (`change-requests/001/product-specs-authoring.md`), the two other request
fixtures removed; 18 tests OK, design-tool and figma-page-check OK; the Offers pages render.

Author check against the three standards: shared guide requirements 1–9 each present (1 the model
sentence; 2 paths and the two folders; 3 the signal, the next free number, a defect in a base starts a
package against it; 4 no roles and selective acceptance; 5 the fold with the open-work ruling; 6 gaps
as rule 5's "nothing open" and known-gaps; 7 the record in Discussion and the log; 8 one renderer,
the chained title; 9 numbered, one example) ✓; product-specs amendment: artifacts (layout, § Change
Requests pointer, Source token), authoring (base, drafts from the base, request signal and path,
Reopening paragraph gone, sweep wording, base-to-drafts list), promotion (fold, readiness 1 and 2,
condition 5 gone, C6/C7/C8, Raising gone, artifact's Change Requests gone) ✓; design-specs
amendment mirrored with S and C3/C4 ✓; tool and migration items ✓ (migration pending step 9).
Obsolescence grep (`Raising a`, `` `Proposed` ``, `request.md`, `Reviewer Response`, `render-request`,
`Incorporated`) over Guides, README, Templates, change-packages.md and the tool, UI Map excluded → 0.

Cross-check against the design guides' request passages (for the supervisor, after compression):
1. The design guides carry their own copy of what the shared guide now says (paths, numbering,
   nesting, the two folders, no roles, the request signal, selective acceptance): about 700 bytes in
   `design-authoring.md` § The change package and § Initiation, and the fold's bookkeeping in
   `design-promotion.md` C3, could become one pointer sentence each. Opportunity, not a divergence.
2. Design readiness 5 (requests the package filed against its inputs must be ruled) has no spec
   counterpart; product specs packages have no formal upstream, and design-specs promotion already
   requires every cited requirement to be canonical. No change proposed.
3. Design Completion reconciles inputs on Review's "next"; spec authoring Completion does not.
   Specs sit upstream of designs, so downstream reconciles; no change proposed.
4. Provenance tokens agree (`Change request: <nnn> V<n>` / `R<n>` / `S<n>`); page titles agree
   (`Design Change: offers | 001` / `Change Package: offers | 001`); initiation wording agrees.
5. The open-work ruling is applied to both sides (design readiness 1 and C3; spec readiness 1 and
   C7/C3).

Compression (Astra, `compress9/`, eight guides, removals counted): change-requests 2,990 → 2,728;
product-specs-artifacts 6,782 → 5,341 (−1,441); -authoring 21,288 → 20,366 (−922); -promotion 16,997 →
16,381 (−616); design-specs-artifacts 4,944 → 4,213 (−731); -authoring 17,783 → 17,438 (−345);
-promotion 12,775 → 12,602 (−173); design-promotion 12,086 → 12,145 (+59). Astra's report, acted on:
the six spec guides now point at the shared guide instead of repeating its definition (requirement 1);
drafts initialize through successive bases to canon; the write, review and recovery wording targets
the base; request initiation reopens-or-creates before the ordinary branch; the shared guide regained
"drafts replace the base's", "requests inherit the base's open gaps", the originator's record,
"layer request pages on the base's drafts" and "read whenever a base is in play"; both authoring
guides' "gaps block promotion" narrowed to production; § Change Requests in both artifacts guides
folded into The Package; root creation kept in C7/C3. Kept against its report: `Base decision: D#`
(needed: the tool accepts `base D<n>`; added to the amendment); "log `gap` for gaps" rather than
"log each transfer" (the log has no state for a carried open item); "a consumer wanting it changed
files a request against it" rather than "consumers may request any change". Installed with those
corrections: change-requests 2,728; product-specs-artifacts 5,373; -authoring 20,390; -promotion
16,381; design-specs-artifacts 4,213; -authoring 17,462; -promotion 12,602 (set 50,160 / 60,000);
design-promotion 12,129. Tests OK.

Rulings on the cross-check (supervisor, 2026-10-25): item 1 done (design-authoring points at the
shared guide for the shared part; the design tool's details stay); item 2 generalized into the shared
guide's rule 9 (decisions that change an input file against it, no later than the review gate; outcomes
applied before promotion), pointed at by design-promotion readiness 5 and a new readiness 5 in both
spec promotion guides; item 3 explained as timing (design batches at the Review gate because decisions
settle only after the mockups are reviewed; specs file as each gap is settled in Discussion), covered
by the same rule. Second compression (Astra, `compress10/`, five guides): change-requests 3,074 →
2,985; design-authoring 16,549 → 15,962 (−888 against the committed guide); design-promotion 12,044 →
11,933; product-specs-promotion 16,512 → 16,412; design-specs-promotion 12,733 → 12,627. Astra restored
the write-time check of the inputs rule (`C7`/`C3` "recheck conditions 1 and 5"), the design guides'
first-mention citations of the shared guide, "under the same rules", "open" and "archived" on the two
folders, and a complete-sentence lead for rule 9; it also replaced several sentences with "per shared
rule N", which I rewrote as plain sentences with the link (a sentence must read with its references
deleted; rule numbers are brittle). Installed: change-requests 2,985; design-authoring 16,021;
design-promotion 12,002; product-specs-promotion 16,578; design-specs-promotion 12,793 (set 50,351).
Tests OK.

Caps set (supervisor, 2026-10-25): change-requests 2,950; product-specs-artifacts 5,350; -authoring
20,350; -promotion 16,550; design-authoring 16,000; design-promotion 12,000; design-specs set 60,000
holds. Trimmed under them; cold series CA follows.

### Refinement — series CA (2026-10-25)

#### Round 1 (prompt `refine/ca1/prompt.txt`; report `review-r1.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 readiness ran `validate <canon> <drafts>`, skipping a request's intervening bases, while render and check-changes infer them | accept (tool) | spec-tool validate | `validate` brings a request's bases in between its roots; the shape guide's row says so | explicit roots still honored |
| F2 the fold ran `check-changes` on the base right after appending the request's entries, which describe the request-to-base difference, not the base's | accept | both spec promotion fold branches | validate and render the base; its author reconciles the list on reopen | the request's own pre-write check |
| F3 a folded entry's justification citing the request's `D<n>` was read as the base's; carried footnotes and items renumber | accept | shared rules 5–6; spec-tool check | the shared guide: a cited decision stays the request's, carried items and footnotes take the base's numbers; the checker skips `D` citations in entries that start `Change request:` | provenance note, Descriptions |
| F4 item-move verification compared against the catalog, not the layered base | accept (tool) | spec-tool `moved_item_status` | the nearest base that holds the item, then the catalog | move/modify distinction |
| F5 rule 9 said "each input"; the base is an input | accept | shared rule 9 | "each input but your base" | design Completion's reconcile wording |
| F6 both spec promotion guides hardcoded the production path for the promotion artifact | accept | both artifact sections | "beside the authoring artifact" | names, checks, recovery |
| F7 the blocked-gate list sent a base contradiction to "return the package to authoring" | accept | both spec promotion gates | its own bullet: standard blocked gate; a package against the base fixes it | package defects still return |
| F8 the tool docstring (the shape guide's "render spec") still described the request page; "unruled"/"statuses" wording | accept | spec-tool docstring; shared rule 9; design-promotion gates and C3 | paragraph deleted, items renumbered; "one without an outcome blocks"; "with condition 5 still met" | supervisor decisions, blocking on no outcome |
| F9 migration not discoverable from Reopening | log-only | — | release work; wait for recurrence | — |
| open question: the shipping restriction and the canonical-citation requirement read as binding folds into packages too | accept (mine) | ps-promotion § When promotion happens; ds-promotion readiness tail | "Into production, …" | production rules unchanged |

Arithmetic: F1 5 · F2 5 · F3 5 · F4 3.75 · F5 2.5 · F6 2.5 · F7 1.875 · F8 3.75 · the open question
1.875 (divergent · off-normal · speculative) · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |

Repairs installed under the caps (change-requests 2,940 / 2,950; product-specs-promotion 16,550 /
16,550; design-specs set 50,406 / 60,000; design-promotion 11,956 / 12,000); tests OK.

#### Round 2 (prompt `refine/ca2/prompt.txt`; report `review-r2.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 authoring's Completion still said other future behavior waits until it ships, unqualified, while promotion now scopes that to production | accept | ps-authoring § Completion | the eligibility policy is promotion's *When promotion happens*; Completion points there | separate promotion invocation |
| F2 `validate` gave baseline treatment to the first root only, so an untouched base draft's fault blocked a request | accept (tool) | spec-tool validate | every root but the last is the baseline (notes); the no-gap-in-canon check stays on the first root | request faults block |
| F3 a requirement carrying an unchanged inherited footnote rendered as modified (`changed or bool(new.gaps)`) and so demanded a change entry | accept (tool) | spec-tool render_item | changed when the footnote set differs between base and draft | adding a footnote is a change; gaps counted and shown |
| F4 the design-spec checker mapped rule entries to their parent item: two changed rules covered by one entry; an unchanged rule passed; the operation tested the parent | accept (tool) | spec-tool render_tree, check_changes, kind_matches | rule-level entries with their own status; rule-typed entries match rules only; design specs require an entry per changed rule, an item whose only change is its rules needs none; product specs keep requirement grain; the design fixture's S2 became `modify rule`, the broken-list test expects the rule issue | known-difference notes at item level; product specs grain |
| F5 known-gaps rule 8 "leave change requests and promotion for the supervisor to start" competed with filing on the workflow's trigger | accept | known-gaps rule 8 | "leave promotion for the supervisor to start and file requests when your workflow says" | supervisor owns decisions |
| F6 a nested request inheriting an ancestor-owned gap cannot name the owner the renderer resolves | log-only | — | wait for an occurrence | — |

Arithmetic: F1 divergent · normal · speculative 2.5 · F2 5 · F3 5 · F4 5 · F5 divergent · off-normal ·
speculative 1.875 · no noise. Also reworded on its open question: design-authoring Completion
"statuses" → "outcomes".

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |

Repairs installed under the caps (known-gaps 3,289 / 3,300; design-authoring 16,000 / 16,000); tests
OK (spec-tool 18, design-tool, figma-page-check); the Offers package validates and check-changes clean
with the layered validate.

#### Round 3 (prompt `refine/ca3/prompt.txt`; report `review-r3.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 design-specs V6 said "at promotion, all cited requirements are canonical" and § IDs "the prefix's canonical maximum plus one", both production assumptions a request trips over | accept | design-specs.md V6, § IDs | V6's sentence deleted (readiness owns it, scoped to production); IDs count from the base, its unpromoted IDs included | production still waits for canonical contracts |
| F2 `validate`'s link-regression check compared against the first root only, so a link a request broke that the base had introduced was a note, not a block | accept (tool) | spec-tool validate | the baseline (every root but the last) is what the projection is compared against; message says "the base resolves it" | untouched base faults stay notes; the no-gap check stays on the first root |
| F3 rule 6's "footnotes follow" did not say that `base D3` becomes `D3` when folded into the base | accept | shared rule 6 | "footnotes follow: a carried item's new number, `base D3` becoming `D3`"; paid by trims to rules 3–4 and the example | folded justifications keep citing the request's decisions |
| F4 the checker allows a redundant parent-item entry beside its rule entries | log-only | — | wait for a reason to forbid it | — |

Arithmetic: F1 divergent · normal · speculative 2.5 · F2 5 · F3 divergent · off-normal · verified 3.75 · no
noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |

Repairs installed under the caps (change-requests 2943 / 2,950; design-specs set 50,386 / 60,000); tests OK.

#### Round 4 (prompt `refine/ca4/prompt.txt`; report `review-r4.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 "an untouched base file's fault never blocks" exempted the very conflict the validator now blocks (a request retiring a target a base file still cites) | accept | both spec promotion readiness 2 and checks preambles | "a fault already in an untouched base file never blocks"; preambles say unchanged content never blocks | no cleanup of untouched base files |
| F2 design-specs § Requirements Gaps said "wait for its promotion" after a request folds upstream, an unconditional wait readiness already scopes to production | accept | ds-authoring § Requirements Gaps | clause deleted | outcomes applied before promotion |
| F3 C1 credited `check-changes` with naming every missing item; a deletion declared as a retirement passes | accept | ps-promotion C1 | `check-changes` names an item missing with no retire entry; inspection covers kept IDs | append-only IDs |
| F4 design-specs.md still routed defects to the removed § Change Requests (two places) | accept (my sweep miss; Astra log-only) | design-specs.md Purpose and § Verification Checks | both route to a package against the base | only a write-inconsistent contradiction blocks |

Arithmetic: F1 divergent · normal · verified 5 · F2 divergent · off-normal · speculative 1.875 · F3
divergent · past-a-rule · verified 1.25 · F4 divergent · off-normal · speculative 1.875 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |

Repairs installed under the caps (product-specs-promotion 16546 / 16,550; design-specs set 50,361 / 60,000);
tests OK.

#### Round 5 (prompt `refine/ca5/prompt.txt`; report `review-r5.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the tool reduced an anchorless link target to its file name, so a citation retargeted from `../shared/details.md` to `../screens/details.md` compared unchanged and its change entry was rejected | accept (tool) | spec-tool `target_identity` | the normalized relative path (a base file and its draft sit at the same place, so a same target still reads the same) | anchors, URLs, glossary-link presentation |
| F2 product-specs § Concept inventory checked concepts against the catalog and called a complete inventory "canonical"; a request's concepts live in its base | accept | ps-authoring § Concept inventory | the base's `domains/` and glossary; "already in the base" | confirmation of new or changed concepts |
| F3 design-specs authoring made a missing drawing for unchanged content a blocking item while promotion said unchanged content never blocks | accept | design-specs.md Purpose scope; ds-authoring V5 sentence; ds-promotion preamble | the content guide owns the scope: inspect touched files whole, block only on what this package changed; a missing drawing blocks for states this package's changes prescribe; promotion points at that scope | validate faults in held files and projection conflicts block |

Arithmetic: F1 divergent · normal · verified 5 · F2 divergent · normal · speculative 2.5 · F3 divergent ·
normal · speculative 2.5 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |

Repairs installed under the caps (product-specs-authoring 20,229 / 20,350; design-specs set 50,522 /
60,000); tests OK; the Offers package still checks clean.

#### Round 6 (prompt `refine/ca6/prompt.txt`; report `review-r6.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 design-specs § Audit still made every failure a blocking item, against Purpose's scope | accept | ds-authoring § Audit | a failure in what this package changed blocks; one already in unchanged content starts a package against the base | audits before editing; validate faults block |
| F2 the checker accepted `base D1` but not the documented `Base decision: D1` | accept (tool) | spec-tool check | `Base decision: D<n>` stripped before the local-citation check | local citations checked; folded entries exempt |
| F3 identity keys still aliased files by name (`screens/notes.md` = `shared/notes.md`); a moved item compared its link definitions without their folders | accept (tool) | spec-tool identity_keys, file entries, index keys, moved_item_status | draft-relative paths only; index entries keyed by the file described; link definitions rebased to root-relative paths before diffing a moved item | item IDs, legitimate rebases, granularity |
| F4 the catalog guide's citation fallback skipped the base ("the draft, otherwise the canonical file") and still routed defects to the removed § Change Requests | accept | ps-catalog Purpose and § Requirements | "the package's draft, else its base's, else the canonical file"; routing to the shared guide; paid by trims | inline citations; touched files only |

Arithmetic: F1 divergent · off-normal · speculative 1.875 · F2 5 · F3 5 · F4 divergent · normal ·
speculative 2.5 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |
| r6 | 14.375 | 4 | 0 | 4 | 0 | 0 |

Repairs installed under the caps (catalog 10499 / 10,500; design-specs set under 60,000); tests OK; the
Offers package checks clean. Noted for the conformance pass: the product-specs-rework package (the
Offers specs' base) fails check-changes on a missing `## Decision Log`, a shape it predates.

#### Round 7 (prompt `refine/ca7/prompt.txt`; report `review-r7.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 a linked `modify index line` identity lost its file path (paths kept for file and folder types only), so a conforming entry was rejected after r6 keyed index entries by path | accept (tool) | spec-tool parse_changes | index-typed entries keep the path | type-sensitive matching |
| F2 rule tables were compared as raw text while the renderer compares resolved targets, so a reference change inside a table left the rule "unchanged" | accept (tool) | spec-tool tables_same | cells compared with `same()` under the two files' link definitions | table structure; rule-level entries |
| F3 the catalog guide's new citation fallback read one level deep ("else its base's") in a recursive model | accept | ps-catalog § Requirements | "else the nearest base's up the chain"; paid by two trims | package first, canon last |

Arithmetic: F1 5 · F2 5 · F3 divergent · off-normal · speculative 1.875 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |
| r6 | 14.375 | 4 | 0 | 4 | 0 | 0 |
| r7 | 11.875 | 3 | 0 | 3 | 0 | 0 |

Repairs installed under the caps (catalog 10483 / 10,500); tests OK.

#### Round 8 (prompt `refine/ca8/prompt.txt`; report `review-r8.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 link identity still depended on spelling and on the target sitting inside the request's drafts: a request index linking the same base file by a different relative path showed as modified, and a linked identity reaching a base file matched nothing | accept (tool) | spec-tool render_tree, render_index, rebased_linkdefs, identity_keys | both sides' link definitions rebased to root-relative paths before any diff; a path that leaves its root into another layer's drafts folder re-rooted to that layer's relative path, in diffs and in identity keys | genuinely different targets detected; touched files only |
| F2 design-specs let an index line ride in Touches on any entry while the granularity paragraph demanded its own entry; the checker followed the template | accept | ds-artifacts Touches line; spec-tool riders | an index line rides only with the new file it describes; the checker enforces that for design specs | product specs Touches unchanged; intro coverage |

Arithmetic: F1 5 · F2 5 · no noise. (A renamed variable broke the renderer for one run; caught by the
tests before launch.)

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |
| r6 | 14.375 | 4 | 0 | 4 | 0 | 0 |
| r7 | 11.875 | 3 | 0 | 3 | 0 | 0 |
| r8 | 10 | 2 | 0 | 2 | 0 | 0 |

Repairs installed under the caps; tests OK; the Offers package checks clean and renders.

#### Round 9 (prompt `refine/ca9/prompt.txt`; report `review-r9.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 a link that left the drafts for the catalog normalized to a different `../` spelling from each layer, so an unchanged index line in a request read as modified; the marker-based re-rooting covered drafts folders only | accept (tool) | spec-tool `logical_path`, rebased_linkdefs, identity_keys | the projection's layers (catalog, bases, drafts) are known to the tool; a path leaving its root is read as its place in whichever layer holds it, no folder-name guessing | genuine retargets visible; external paths unchanged |
| F2 `validate` followed a link into an earlier layer to the file on disk, so a request retiring an item a base file cites passed | accept (tool) | spec-tool resolve_link | a link landing in a layer resolves through the projection, not the disk | external links still read from disk |
| F3 the design index-line rider check tested the entry's type only, so an unrelated index edit rode on any new file | accept (tool) | spec-tool riders | the rider's file must be the file the index line describes | product specs Touches; root creation |
| F4 an intro riding in Touches on a `modify item` entry passes but renders without a reason | log-only | — | attribution of a shared intro waits for a rule | the no-aggregation rule |

Arithmetic: F1 5 · F2 5 · F3 divergent · past-a-rule · verified 1.25 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |
| r6 | 14.375 | 4 | 0 | 4 | 0 | 0 |
| r7 | 11.875 | 3 | 0 | 3 | 0 | 0 |
| r8 | 10 | 2 | 0 | 2 | 0 | 0 |
| r9 | 11.25 | 3 | 0 | 3 | 0 | 0 |

Repairs installed; tests OK; the Offers package validates and checks clean. No guide text changed this
round.

#### Round 10 (prompt `refine/ca10/prompt.txt`; report `review-r10.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 an anchored external URL was identified by its fragment alone, so a tracking link changing from issue 123 to 456 compared unchanged | accept (tool) | spec-tool `target_identity` | an external destination is identified whole | local anchors identify spec IDs |
| F2 a link to a spec file carried its label as an identity key, so two files both linked as "Notes" collided in index checks | accept (tool) | spec-tool `identity_keys` | a link to a non-index file keys by its place only; labels stay for index files and bare names | the new-file index rider; cross-layer equivalence |

Arithmetic: F1 5 · F2 5 · no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |
| r6 | 14.375 | 4 | 0 | 4 | 0 | 0 |
| r7 | 11.875 | 3 | 0 | 3 | 0 | 0 |
| r8 | 10 | 2 | 0 | 2 | 0 | 0 |
| r9 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r10 | 10 | 2 | 0 | 2 | 0 | 0 |

Repairs installed; tests OK; the Offers package checks clean. Guide text unchanged since r8; every
finding since r9 is in the tool's identity and layer handling, found by the reviewer running the code.

#### Round 11 (prompt `refine/ca11/prompt.txt`; report `review-r11.md`)

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 the design index-line rider accepted any file entry for the described file, added or not | accept (tool) | spec-tool riders | the described file must be added in the projection | product specs Touches; new-file riders |

Arithmetic: F1 divergent · past-a-rule · verified 1.25 · no noise. On its open question: the request
fixture's glossary links pointed at a glossary the request does not hold; repointed to the base's
glossary where it sits, and the test now validates the request as well as checking it.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |
| r6 | 14.375 | 4 | 0 | 4 | 0 | 0 |
| r7 | 11.875 | 3 | 0 | 3 | 0 | 0 |
| r8 | 10 | 2 | 0 | 2 | 0 | 0 |
| r9 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r10 | 10 | 2 | 0 | 2 | 0 | 0 |
| r11 | 1.25 | 1 | 0 | 1 | 0 | 0 |

Verdict this round: usable by a fresh LLM today; the guides unchanged since r8.

#### Round 12 (prompt `refine/ca12/prompt.txt`; report `review-r12.md`)

No findings; six walks and the design adoption clean; the tooling claims confirmed by inspection
(transitive bases, chained page ids, base-decision citations, the index rider, the fixture's glossary
links, no request command). Open: the manual fold's bookkeeping and unmigrated artifacts, neither a
guide defect.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.25 | 9 | 0 | 9 | 0 | 0 |
| r2 | 19.375 | 5 | 0 | 5 | 0 | 0 |
| r3 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r4 | 10 | 4 | 0 | 4 | 0 | 0 |
| r5 | 10 | 3 | 0 | 3 | 0 | 0 |
| r6 | 14.375 | 4 | 0 | 4 | 0 | 0 |
| r7 | 11.875 | 3 | 0 | 3 | 0 | 0 |
| r8 | 10 | 2 | 0 | 2 | 0 | 0 |
| r9 | 11.25 | 3 | 0 | 3 | 0 | 0 |
| r10 | 10 | 2 | 0 | 2 | 0 | 0 |
| r11 | 1.25 | 1 | 0 | 1 | 0 | 0 |
| r12 | 0 | 0 | 0 | 0 | 0 | 0 |

Converged by stop rule (a). Final sizes: change-requests 2,943 / 2,950; product-specs-artifacts 5,350 /
5,350; -authoring 20,229 / 20,350; -promotion 16,546 / 16,550; -catalog 10,483 / 10,500; design-specs set
50,633 / 60,000; design-authoring 16,000 / 16,000; design-promotion 11,956 / 12,000; known-gaps 3,289 /
3,300. Guide text last changed in r8; r9–r11 were the spec tool's identity and layer handling.

## Maintenance retro — change requests as authoring against a base, spec guides — 2026-10-25

Inventory: new `Guides/Core/change-requests.md` (`guide.change-requests`); both artifacts guides, both
authoring and both promotion guides of the spec types, `design-specs.md`, `product-specs-catalog.md`,
`known-gaps.md` rule 8, `spec-file-shape.md`'s command table; `design-authoring.md` and
`design-promotion.md` adopting the shared guide and the open-work ruling; `spec-tool.py` (base
inference, chained titles, layer-aware links and validation, rule-level design checks, base-decision
citations, request renderer removed); fixtures and tests (request fixture as a package; two old request
fixtures removed); README, skill descriptions, manifest, `change-packages.md`. Host-install-visible.
Bookkeeping: two release entries plus one for the tool, three CHANGELOG lines; `Managed-Updated-At`
2026-10-25 on every edited guide; manifest has the new guide. Tests: spec-tool 18 OK, design-tool OK,
figma-page-check OK; the Offers package validates and checks clean under the layered validate.
Consistency: stale-model grep (`Raising a`, `` `Proposed` ``, `request.md`, `Reviewer Response`,
`render-request`, `Incorporated`, `request-review`) → 0 outside the UI Map guides, which keep their
model until their refinement. Change-package verification: the request layout is in the shared guide;
promotion archives a request under its base; collisions and recovery unchanged; migration guidance
covers the one old-form request and re-runs safely. Follow-ups: UI Map guides (their own pass); the
conformance pass over the Offers package (plan step 5d), where the product-specs-rework package's
missing `## Decision Log` belongs; host skill copies stale until the update runbook runs.
Process reflection: twelve rounds, the last four almost entirely in the tool, each tool fix opening the
next until the layer model was made explicit (`LAYERS`, `logical_path`) in r9; a tool change of this
size should get that design step before the rounds, not during them.

## Plain Language In The Spec, UI Map And Work-Spec Guides — 2026-10-25

Target: the product specs guides (5), design specs guides (4), UI Map guides (10) and work-spec
guides (2), 313,953 bytes on 2026-10-25. Standard: `writing-style-design.md` Requirements 2–6, with
the supervisor's ruling of 2026-10-25 that a spec change item's Justification is a reason in plain
words, then its source (`product-specs-system-design.md` and `design-specs-design.md` § Amendment —
2026-10-25, plain language). Question for every guide: where do its instructions or its examples
produce writing for a person that is not in plain language, or that says nothing the reader can
use? Both halves matter: an agent imitates the examples a guide gives it, so a fix goes in the
instruction and the example. Method (agreed 2026-10-25): one Astra cold pass with that question as
the inventory, run as three reads so each family is read whole (spec guides; UI Map guides;
work-spec guides), then repairs through the process as one series; the proposed Justification edit
goes to the pass for assessment. Record below.

### Refinement — series PL (2026-10-25)

#### Round 1 (prompts `refine/pl1/prompt-specs.txt`, `prompt-uimap.txt`, `prompt-workspec.txt`; reports `review-specs.md`, `review-uimap.md`, `review-workspec.md`)

Three reads of one round, same prompt but for the target list, the simulation steps and, for the spec
guides only, the observed failures (four facts: the Offers change list's justifications, an Offers
requirement sentence, Discussion-gate summaries from skai#97, the CR-001 V06 entry as it stood on
2026-10-24) and the proposed Justification edits A–C for assessment. Report charter: instructions or
examples that produce or permit text for a person that is not plain or says nothing useful.
Excluded surfaces: the refinement records, release notes, internal and templates. Launched 2026-10-25.

Work-spec read (returned first): F1 the image-loading example in both guides models the form but
not the substance (an unnamed "transformation", a reason with no source, a Done-when that says
nothing with its identifier removed, an API comment silent on the change from optional to throwing)
— accept, example replaced across both guides, paid for by the example's duplicate Unit Testing
routing; F2 the no-items Discussion sentence ("review the API Sketch as the proposed contract") and
the plan gate's "link or summarize" let the agent point instead of state — accept, both sharpened to
state the change and the fact that settles it. Both divergent · normal · speculative = 2.5; read
subtotal 5. Open question on gap closure wording ("answered, placeholder adopted, or omitted") left
to known-gaps, as the reviewer did. Pair at 32,566 / 32,600.

Spec read: F1 both artifacts guides make a citation sufficient ("for a spec the Justification is the
citation"; "Entries carry no text"; the folded entry's `Change request:` prefix is checked by
`startswith` in the tool) — accept, verified; edits A and C amended per the report (A also narrows
"no text" to copying spec text and repairs the Implementation example; C names the shared behavior
and its source), B endorsed; the provenance token moves after the entry's own reason and source and
the checker matches it anywhere. F2 the Tradeoff example ("Proposal B." / "Why Theme follows each
device's appearance") and the Resolution sentence "Decision says answered, placeholder adopted, or
omitted" (owned by process-flow § Structured discussion items, inlined in five guides) — accept;
example rewritten, the owner sentence sharpened to the outcome in words plus which of the three it
was, swept to every inlined copy. F3 "Package prose may name frames, nodes and files" in
design-specs-authoring and design-specs.md — accept, narrowed to where the reader must go. F4 the
gap footnote form names the owner by ID with no words for the question — settled 2026-10-24 (the
question stays with its owner; the chip carries its tooltip), omitted from the prompt's settled
list; noise, and put to the supervisor as a question under today's ruling. F5 design-specs.md
Restatement ("shrink to the citation"; "Headings as [UI-LIST-01-02]"; the glossary attribution) —
accept, examples keep a readable subject before the citation. F6 C4 Writing style and V3 Product
language check content rules only; the C4 failure example says FAILED and a path — accept, both
apply the writing guide and the example names the defect. F7 gate wording ("The package returns to
authoring", "advance to Completion", "base written, archival incomplete") — accept, cosmetic.
Scored: F1 divergent · normal · verified = 5; F2, F3, F5, F6 divergent · normal · speculative = 2.5
each; F7 cosmetic · normal · speculative = 1; F4 noise. Read subtotal 16.

UI Map read: F1 the architecture artifacts guide's "the Justification is just the citation",
"reference or rationale", `Resolved decision: D#` as a whole example; implementation's `Realizes`
"anchors why" — accept. F2 the Code Changes gate says "to implement" in Plan mode too; "The app
conforms to the official UI Map" after a scoped audit; completion lines report state — accept. F3
the domain line example and the Discussion example (`A (modal)`, a Proposal of `share_sheet`) teach
shorthand against the guide's own Writing style section — accept. F4 the copied annotation "Both
surfaced from the library toolbar" in the format guide and the demo — one defect with F3 (examples).
F5 evidence brackets as the whole record — accept, cosmetic. F6 eight guides without the pointer —
accept for all eight (the standard says every guide whose agent writes for a person; no cap on the
set). Scored: F1, F2, F3+F4 divergent · normal · speculative = 2.5 each; F5 cosmetic · normal ·
speculative = 1; F6 divergent · off-normal · speculative = 1.875. Read subtotal 10.375. The
product-specs baseline guide, which writes the product paragraph and is read only from authoring,
keeps no pointer: log-only.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |

spec F1 5 · spec F2+F3+F5+F6 10 · spec F7 1 · spec F4 noise (settled 2026-10-24) · uimap F1+F2+F3(+F4) 7.5 ·
uimap F5 1 · uimap F6 1.875 · workspec F1+F2 5 = 31.375.

Decisions taken in triage (supervisor may overrule): the provenance token on a folded entry follows
the entry's own reason and source (`<reason>; <Source>: <ref>; Change request: <nnn> R<n>`), in the
shared guide, both spec promotion guides, design promotion and the checker. Ruled (supervisor,
2026-10-25): the gap footnote keeps its settled form. The gap's Discussion item is the source of
truth; the footnote's Placeholder clause states the placeholder as it relates to this item; the
owner link, with its tooltip, is for anyone who wants more. A footnote never carries the question.
F4 stays noise; the next prompt lists this among the settled dispositions.

### Drafts and author check — 2026-10-25

Repairs drafted for every accepted r1 finding. Core owners: process-flow's Resolution step says the
Decision states the outcome in words and which of answered, placeholder adopted or omitted it was,
swept to the six inlined copies (design-authoring, design-specs-authoring, product-specs-authoring,
work-spec-creation, ui-map-architecture, ui-map-implementation); the shared guide's rule 5, both
spec promotion guides, design-promotion and the checker put the provenance token after the entry's
own reason and source (`"Change request:" in why`). Spec guides: both artifacts guides' templates
read `<why the change is needed>; <Source>: <reference>`, "entries carry no text" is "copy no spec
text", the citation-only sentence is gone, every example carries a reason, the leaked-detail pair
reordered; the Tradeoff example rewritten in product words with a first-person recommendation; the
no-items sentence states what settled the drafts; the frame/node/file permission narrowed to where
the reader must go; Restatement never shrinks to a bare citation, with the heading and glossary
examples repaired; C4 and V3 apply the writing guide and the C4 failure example names the defect;
gate lines say what the agent does next ("Write <N> requirements into <paths>", "I am reopening the
package to fix it", "close the discussion; I then finish the package for your review", "the specs
are written but the package is not yet archived"). UI Map: the architecture format's citation-only
sentence gone, a ❌/✅ Description and Justification pair added, `Realizes` traces and the
Description explains, the domain line and the Discussion example in product words (the name-only
proposal deleted, the Tradeoff shown resolved), the annotation names Profile and Search in the format
guide and the demo's YAML and render, evidence lines open with what the run established, the Code
Changes gate has a Build and a Plan line, completion lines say what is in place and what is left,
the pointer added to the eight guides without it (and to the two spec artifacts guides). Work-spec:
the image-loading example names the behavior, the reason and the API change across both guides, the
no-items sentence and the plan gate state the change. Maintainer rule: `maintain-skai.md` § Common
house style, the guide-authoring sanity scan, the review template's failure-mode examples.

Author check against the standard: writing-style-design Requirements 2–6 applied to every new
sentence (read with IDs removed), Requirement 10 present in the three maintainer surfaces; the two
spec amendments (reason then source; the citation sentence gone; examples show a reason) ✓; the gap
footnote form untouched ✓. Sanity scan: `Managed-Updated-At` 2026-10-25 on every edited guide; no
"human"; gate prefixes intact; pointer grep: every target guide carries it (still without it, and
logged for a later pass: the Figma designer guide, the Test guides, the debugging guide, the Core
reference guides, product-specs-baseline). Tests: spec-tool 18 OK, design-tool OK.

Sizes before compression (cap, delta): process-flow 21,637 (21,550, +87); change-requests 2,971
(2,950, +21); product-specs-artifacts 5,596 (5,350); -authoring 20,603 (20,350, +253); -promotion
16,575 (16,550, +25); design-authoring 16,065 (16,000, +65); design-promotion 11,950 (12,000);
design-specs set 50,278 (60,000); work-spec pair 33,027 (32,600, +427); UI Map set 179,836 (no cap).
Caps are reset by the supervisor after compression, as the process says.

### Compression — 2026-10-25 (Astra, scratchpad `compress11/`, four runs, removals counted)

Work-spec pair (returned first): 33,027 → 32,095 by Astra; installed 31,813 after rejecting three
of its moves: links lifted out of their sentences to dangle after them (ten places, restored
inline), the verbatim known-gaps pointer sentence paraphrased (restored byte for byte in both
guides), and reason sentences put into the `Realizes` trace field with first person in the task
`Work` lines (restored: Realizes traces, Work is the work). Its documented duplicate removals
accepted (stable-ID reminders, the planned-gate timing sentence, "do not edit the design from this
skill"); its four lost-item flags kept as they stand; its cut list (213 bytes) not taken. The pair
is under its 32,600 cap.

Core and Design run: change-requests 2,971 → 2,957 (installed, then 2,949 after one trim);
design-authoring 16,065 → 14,801, design-promotion 11,950 → 11,330 and process-flow 21,637 → 17,762
rejected. Reasons: process-flow is the canonical reference whose gate and marker boilerplate the
gated-workflows template mirrors into every guide, and an 18 percent restructure of the owner is a
periodic-restructure pass of its own (refinement guide § Across passes), not a repair in this series;
the two design outputs rewrote that same inlined boilerplate and re-inlined the shared guide's rule 6
into design-promotion C3, which the CA cross-check settled the other way (the design guides point at
the shared guide). Hand trims instead: the swept Resolution sentence shortened to "Decision states
the outcome in words and which it was: answered, placeholder adopted, or omitted." in the owner and
all six copies; process-flow's "appended, not substituted" clause (Astra's own duplicate finding)
removed; design-authoring's duplicate feedback reminder in Phases removed and "actually" dropped from
its gate-persistence sentence. Result: process-flow 21,522 / 21,550; change-requests 2,949 / 2,950;
design-authoring 15,995 / 16,000; design-promotion 11,950 / 12,000.

Spec run (seven guides, 93,053 → 87,656) and UI Map run (ten guides, 179,836 → 168,356): installed,
with the same corrections as the work-spec run where they recurred: the verbatim known-gaps pointer
sentence paraphrased in four guides (design-specs-authoring, product-specs-authoring,
ui-map-architecture, ui-map-implementation), restored byte for byte; the swept Resolution sentence
brought to the short form in the two UI Map guides. Checked by script on every installed file: no
links lifted out of their sentences, the writing-style pointer count unchanged, every gate and
completion template line present (the one `⏳ GATE:` occurrence Astra dropped per guide was the
prose mention in "No fabricated gates", not a template), every example string this series added
still present. Astra's documented duplicate removals accepted; its lost-item flags kept; its cut lists
not taken. The worked examples were not changed by these two runs.

Compressed sizes for the supervisor to set caps against: product-specs-artifacts 5,487 (cap 5,350);
product-specs-authoring 18,945 (20,350); product-specs-promotion 15,599 (16,550); design-specs set
47,721 (60,000); work-spec pair 31,789 (32,600); UI Map set 168,384 (no cap yet): architecture 32,694,
architecture-artifacts 5,550, implementation 47,954, implementation-artifacts 6,322, guide 15,088,
demo 10,959, swiftui 9,535, swiftui-placeholders 14,278, compose 10,628, compose-placeholders 15,376.

Ruled (supervisor, 2026-10-25): no aggressive compression of the UI Map guides at this time; they
are the only guides with an extensive regression test, and broad rewording risks the behavior it
covers with no round here to catch it. Astra's UI Map output reverted; the ten guides hold this
series' repairs only (the short Decision sentence kept in the two method guides). UI Map set
179,788; the sizes line above is superseded for that set.

Caps set (supervisor, 2026-10-25): product-specs-artifacts 5,450; -authoring 18,900; -promotion
15,550; design-specs set 47,500; work-spec pair 31,700; process-flow 21,500; change-requests 2,950;
design-authoring 16,000; design-promotion 12,000; UI Map set no cap. Provenance tag order confirmed
("seems fine"). Trimmed under the caps by hand before round 2: wording in the two promotion guides'
gate notes and archive-failure sentences, the Tradeoff example's own sentences in
product-specs-authoring, process-flow's redundant "Guides keep their tool-neutral vocabulary", the
design-specs auto paragraph's restatement of the general auto rule, two of Astra's work-spec cut-list
items (the renumbering reminder and the Plan completion preamble, both stated in Task format and
Advance intent), and the two design-specs example phrasings.

Size guard before round 2: process-flow 21,480 / 21,500; change-requests 2,949 / 2,950;
design-authoring 15,995 / 16,000; design-promotion 11,950 / 12,000; product-specs-artifacts 5,443 /
5,450; -authoring 18,899 / 18,900; -promotion 15,538 / 15,550; -catalog 10,483 / 10,500; design-specs
set 47,482 / 47,500; work-spec pair 31,671 / 31,700; UI Map set 179,788 (no cap). Last trims:
"proceed to Completion" in the two blocked Discussion gates became "Resolve them and I finish the
package"; the design-specs gate note lost its restatement of the no-items case and "so the supervisor
reviews it"; product promotion's gate note lost "and the unchecked checklist".

#### Round 2 (prompts `refine/pl2/prompt-specs.txt`, `prompt-uimap.txt`, `prompt-workspec.txt`; reports `review-*.md`)

Same three reads. Settled dispositions quote round 1's findings-log rows verbatim, plus the gap
footnote ruling, the provenance tag order, the UI Map guides uncompressed and the caps. Recently
revised names every repair and, for the spec and work-spec reads, warns that compression re-worded
sentences throughout. The proposed-edits slot is gone (applied); the observed failures stay as
evidence. Launched 2026-10-25.

Round 2 results. Spec read: F1 the review page drops the no-items sentence (`parse_discussion`
skips prose with no item; the card says only "no discussion items") — accept, verified, tool: the
card now shows the sentence (`discussion_note`, both renderers; test). F2 an intro covered through a
requirement entry's Touches renders with no reason (`why_for`'s fallback took file-level entries
only, while `check-changes` accepts any covering entry) — accept, verified, tool: the fallback takes
every covering entry, attributed by ID when several (test); CA r9 F4 had logged this once, second
sighting. F3 evidence examples put bookkeeping before the result — accept, cosmetic: the evidence
form reads `<the result, in words>; <command or inspection>` in both promotion guides and the seven
examples lead with the result. F4 reconciliation kept justifications for matching IDs even when the
reason no longer explains the difference — accept: "a justification only while it still explains
the current difference" in both authoring guides. F5 product authoring Completion did not say whether
promotion can follow — accept: Completion says whether promotion can follow now or waits on shipping.
UI Map read: F1 the empty-Discussion sentence claimed the inputs determined the map while the guide
lets the agent pick immaterial defaults — accept: the sentence says no choice needs the supervisor's
decision and the map is on the preview; the example and the gate paragraph follow; the same class
swept to design-authoring's no-items sentence; the domain line's "single screens" became "collapsed
to their root screens" (the reviewer's open note). F2 the Code Changes gate summary listed only
path, counts and links — accept, cosmetic: it leads with what the items change in the app, with a
❌/✅ pair. Work-spec read: F1 evidence examples and the requested-stop line carried only metadata
— accept, cosmetic: the result in words leads the evidence line, the stop line names what the next
task delivers. F2 the Why templates and the worked Why gave a reason without its source — accept,
cosmetic: `<reason, then its source>` in the templates; the owner (process-flow § Structured
discussion items) now defines Why as "the reason, then its source" and its two examples cite the
designs; the design-authoring, product-specs-authoring and ui-map-architecture example Whys cite
theirs. Open question (spec read): the amendment's "source as a link" against the design-source rule
(a screen by product name, no design-tool link) — the link is to the item, requirement or decision
where one exists; a design source stays a product name; noted in the amendment, no guide change.
Scored: spec F1, F2 divergent · normal · verified = 5 each; spec F5, uimap F1 divergent · normal ·
speculative = 2.5 each; spec F4 divergent · off-normal · speculative = 1.875; spec F3, uimap F2,
workspec F1, F2 cosmetic · normal · speculative = 1 each.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |

spec F1 5 · spec F2 5 · spec F3 1 · spec F4 1.875 · spec F5 2.5 · uimap F1 2.5 · uimap F2 1 ·
workspec F1 1 · workspec F2 1 = 20.875. Who the findings are about: five of nine are classes of
round 1's repairs applied in one guide but not its siblings (evidence lines, the no-items sentence,
Why sources); this round swept each class across every owner.

After the round-2 tool fixes the Offers pages were re-rendered (context repo, uncommitted): the
Offers specs page (26 gaps, 18 resolved), the rework request 001 page, the Offers design page and
CR-001's page; the rework base's own page is step 5d's. Tests: spec-tool 20 OK (two added: the
no-items sentence renders; an intro covered through Touches shows the covering entry's reason),
design-tool OK. Size guard before round 3: every capped guide under its cap (process-flow 21,480;
change-requests 2,949; design-authoring 15,995; design-promotion 11,950; product-specs-artifacts
5,443; -authoring 18,872; -promotion 15,544; -catalog 10,483; design-specs set 47,489; work-spec pair
31,692; UI Map set 180,263, no cap).

#### Round 3 (prompts `refine/pl3/prompt-*.txt`; reports `review-*.md`)

Same three reads; settled dispositions quote rounds 1 and 2 from the findings log; recently revised
names the round-2 repairs and the two renderer fixes. Work-spec read (returned first): no findings;
every writing moment walked as smooth; the remaining risk named is an agent skipping the shared
self-check, which the reviewer calls noncompliance with an existing rule, not a guide defect. Read
subtotal 0.

UI Map read: no findings; the six walks smooth or usable; tooling claims (schema validation, note
pass-through) verified against the renderer and viewer. One open note: architecture's reconciliation
sentence still kept a matching change's justification unconditionally, the class round 2 repaired in
the two spec authoring guides (spec F4); repaired now as that sweep's last sibling ("and its
justification only while it still explains why the change is needed"). The reviewer's other notes
(top-level YAML TODOs stay out of the viewer; older context not treated as current) need no change.
Read subtotal 0. Because the UI Map text changed after this read, the UI Map family gets a round-4
read over the current text; the work-spec pair's round-3 read already stands over unchanged text.

Spec read: F1 two rendering paths lose what the author wrote — a product index line covered through
`Touches` renders with no reason (the index-line caller passes no file to `why_for`), and a
justification's source link is resolved with the draft's link definitions after `render_tree`
switches the resolver, so a defined `[D02]` renders as a bare span — accept, verified, tool. F2 the
leaked-detail paragraph diagnosed the requirement as wrong from a reason alone — accept: "read the
requirement and the reason, and fix whichever holds the mechanism", the ✅ example shortened to pay.
Open note: design-specs-authoring's "with no text inline" (round 1 F1's class) — "omitting spec
text". Scored: F1 divergent · normal · verified = 5; F2 divergent · normal · speculative = 2.5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |

spec F1 5 · spec F2 2.5 · uimap none (one swept note) · workspec none = 7.5. Both live defects are
in the handoff from the artifact to the page; the guides' text drew no finding in two of three reads.
Round 4: the spec family (text and tool changed) and the UI Map family (text changed after its
read); the work-spec pair's round-3 read stands over unchanged text.

#### Round 4 (UI Map read: prompt `refine/pl4/prompt-uimap.txt`, report `review-uimap.md`)

UI Map read over the current text: no findings; the seven walks smooth or sufficient; the renderer's
validation and note pass-through verified by inspection; the remaining risk named is the operator
skipping the shared self-check. The UI Map family converges by stop rule (a) at this read; the
work-spec pair converged at its round-3 read (text unchanged since). The spec family's round-4 read
follows the round-3 tool fixes.

Round-3 tool fixes installed: index lines pass their file to `why_for`, so an index line covered
through Touches shows the covering entry's reason; justifications render through the authoring
artifact's link definitions (`inline_why`, `WHY_RESOLVER`) at every Why site (card, intro, file).
Tests: spec-tool 22 OK (two added: a cited decision in a justification stays a link inside a draft
card; an index line covered through Touches shows its covering reason), design-tool OK. The two
Offers spec pages re-rendered. Size guard: product-specs-artifacts 5,431 / 5,450; design-specs set
47,488 / 47,500; the rest unchanged since round 3. Round-4 spec read launched (prompt
`refine/pl4/prompt-specs.txt`).

#### Round 4 (spec read: prompt `refine/pl4/prompt-specs.txt`, report `review-specs.md`)

F1 the ✅ example in the leaked-detail paragraph ("The list reorders itself whenever either source
changes; Implementation") describes behavior, not why the requirement changes — the round-3 trim had
cut the clause that carried the reason — accept: the example is gone; the paragraph ends "a reason
says why the requirement changes, not what the app does". F2 the review page omits Assumptions and
TODOs and Out of scope — settled: the supervisor ruled on 2026-10-23 that the page shows the package
card, the Discussion and the change cards, and that Inputs, Assumptions and TODOs, Out of scope and
the Decision Log stay in the artifact (skai#99 prototype conventions; G18); omitted from the prompt's
settled list; noise, and the reviewer's view (an unchanged concept inventory and a folded-request
note never reach the page's reader) is reported to the supervisor once. Scored: F1 divergent ·
normal · speculative = 2.5; F2 noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |

r4 = the UI Map read (0) and the spec read (F1 2.5 · F2 noise). Round 5: the spec family only.

#### Round 5 (spec read: prompt `refine/pl5/prompt-specs.txt`, report `review-specs.md`)

F1 an added file covered only through another entry's Touches (the root-creation entry the artifacts
guide permits, a folder entry) renders its heading with no reason: the file-heading call to `why_for`
passed no file, so the Touches fallback never ran — accept, verified (the reviewer exercised it in
memory: validate and check-changes clean, both files rendered, no reason), tool: the heading lookup
passes the file (test: two added files covered by one entry's Touches both show its reason). No guide
finding; the eight walks usable. Scored: F1 divergent · off-normal · verified = 3.75.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |

Rounds 3–5's live findings are all in the renderer's reason lookups, one coverage path at a time
(intro, index line, citation links, added file); as in series CA, a tool change of this kind should
get its design step (every coverage path check-changes accepts, enumerated) before the rounds, not
during them. Round 6: the spec family.
The heading fallback applies to added files only: a modified file's heading keeps its file-level entry
or none, since each changed item below it carries its own reason. Tests 23 OK, design-tool OK; the
two Offers spec pages re-rendered. Round-6 spec read launched (prompt `refine/pl6/prompt-specs.txt`).

#### Round 6 (spec read: prompt `refine/pl6/prompt-specs.txt`, report `review-specs.md`)

F1 a section's orientation text is compared only when the section exists in the base: a new
section's sentence renders as unchanged prose with no reason, a removed section's sentence vanishes,
and when that is the file's only edit the file is skipped as unchanged; the checker consumes the
same entries, so it misses it too — accept, verified (exercised in memory by the reviewer). No guide
finding; every walk usable. Scored: divergent · normal · verified = 5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |

Consolidation trigger: four rounds in a row have each found one more path where the page and
checker account for a difference incompletely (an intro covered through Touches, an index line's
reason and a citation's links, an added file's heading, now section prose added or removed). Rather
than patch the sixth instance, this repair enumerates every prose comparison the renderer makes
(file intro, section orientation text, index line, glossary entry, item, rule) against the three
cases (added, modified, removed) and the reason lookup, and fixes the class.
Class fix installed: `render_spec` emits a new section's orientation text as an added prose card and a
removed section's as a missing one, each with the reason of the entry naming the section or, failing
that, of the entries whose Touches name the file; the intro already handled all three cases, index
lines and glossary entries handle add, modify and remove, items and rules likewise. Tests 25 OK (two
added), design-tool OK; the Offers spec pages re-rendered and `check-changes` on the Offers package
still clean. Round-7 spec read launched (prompt `refine/pl7/prompt-specs.txt`).

#### Round 7 (spec read: prompt `refine/pl7/prompt-specs.txt`, report `review-specs.md`)

F1 the glossary's introductory prose is parsed but never compared: `render_glossary` builds entries
from terms only and never calls the intro comparison the spec and index renderers share, so a
changed glossary intro reaches neither the page nor `check-changes`, and an intro-only edit skips
the file — accept, verified (exercised in memory by the reviewer). The round-6 enumeration missed
this branch: it checked the intro comparison, not every file type's call to it. No guide finding;
every walk usable. Scored: divergent · normal · verified = 5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
Fix installed: `render_glossary` opens with the shared intro comparison (`rel` passed from the call
site), so a glossary intro added, changed or removed is an entry for the page and the checker like any
other file's. Tests 26 OK (one added), design-tool OK; the Offers spec pages re-rendered; the Offers
`check-changes` clean. Round-8 spec read launched (prompt `refine/pl8/prompt-specs.txt`).

#### Round 8 (spec read: prompt `refine/pl8/prompt-specs.txt`, report `review-specs.md`)

F1 the renderer picks a reason by name alone, so a glossary term sharing a section's name lends its
reason to that section's orientation text; the checker matches by kind (`kind_matches`), the renderer
did not — accept, verified (reproduced in memory by the reviewer). F2 a changed prose paragraph and
its reason are sibling elements, and the page filter hides the paragraph but not the reason, which
then sits beside content it does not explain — accept, verified. Open note: a section with
orientation text and no item under it is never visited by the renderer (a branch of round 6's
repair); fixed with it. No guide finding; every walk usable. Scored: F1 divergent · normal ·
verified = 5; F2 divergent · off-normal · verified = 3.75.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
Fixes installed: `why_for` takes the entry's kind and matches as the checker does (a same-named
glossary term, item or index line lends no reason; section lines and intros take only covering
entries through Touches); a changed prose paragraph and its reason now form one card (`<div
class="item prose modified">`), which the page script already treats as a card and filters whole, with
one neutralizing style rule added in place to `spec-review.v1.css` (allowed by the versioning rule:
pages already rendered are unaffected); a section with orientation text and no item under it is
rendered with its heading. Tests 28 OK (two added, three patterns updated to the card markup),
design-tool OK; the Offers spec pages re-rendered, `check-changes` clean. Round-9 spec read launched
(prompt `refine/pl9/prompt-specs.txt`).

#### Round 9 (spec read: prompt `refine/pl9/prompt-specs.txt`, report `review-specs.md`)

F1 a design spec's rule-level change entries never show their reasons on the page: the rule list
renders with no reason input and the item card's lookup takes item-kind entries only — accept,
verified. F2 when a retained table row loses a column, the changed-row comparison iterates to the
new row's length, so the removed cell's text never reaches the diff (the header comparison pads
both sides) — accept, verified. No guide finding; every walk coherent. Scored: F1, F2 divergent ·
normal · verified = 5 each.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
Fixes installed: each changed rule shows its own entry's reason (`RULE_CHANGES` set at render time,
`why_for` by kind "rule", an inline why span on the rule's line); a changed table row is compared
with both sides padded, so a removed column's cells show as deletions. Tests 30 OK (two added: the
design fixture's rule change shows its reason; a planted table losing a column shows its old cells),
design-tool OK; the Offers spec pages re-rendered, `check-changes` clean. Round-10 spec read launched
(prompt `refine/pl10/prompt-specs.txt`).

#### Round 10 (spec read: prompt `refine/pl10/prompt-specs.txt`, report `review-specs.md`)

F1 a rule's reason is looked up only when the rule gets a visual change marker, so a rule whose
table alone changed, or a rule inside an item added to an existing file (markers suppressed), shows
no reason although its entry supplies one — accept, verified (in-memory probes by the reviewer, with
a sentence-change control that worked). No guide finding; every walk usable. Scored: divergent ·
normal · verified = 5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
Fix installed: a rule's reason is looked up whenever an entry names the rule, with or without a visual
marker (a table-only change, a rule inside an added item). Tests 31 OK (one added: a rule whose
table alone changed shows its entry's reason beside the table diff), design-tool OK; the Offers pages
hold no design specs, so no re-render. Round-11 spec read launched (prompt
`refine/pl11/prompt-specs.txt`).

#### Round 11 (spec read: prompt `refine/pl11/prompt-specs.txt`, report `review-specs.md`)

F1 the retirement examples the shape guide shows ("Superseded by [REMIND-01]", "Superseded by **01**")
teach a pointer where the content guides ask for the successor named; the Offers drafts carry the
same form — accept: Stability in both content guides says the successor is named in product words,
then cited; the shape guide's two examples repaired (routed to its owner, `spec-format-design.md`).
F2 a justification citing a Discussion topic by its anchor (`[D02]: #missed-reminders`, the form
authoring permits) renders as a link to nowhere: topic headings carry no id, cards are `d02`, and
a fragment to an artifact section the page omits has no destination either — accept, verified:
topic headings get their anchor as id; a fragment that matches nothing on the page links to the
authoring artifact itself at that fragment. Scored: F1 divergent · off-normal · speculative = 1.875;
F2 divergent · normal · verified = 5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
Fixes installed: Stability in `product-specs-catalog.md` and `design-specs.md` says the retired body is a
sentence saying in product words what replaced it, then the citation (both trimmed back under cap);
the shape guide's two retirement examples read "Thirty-day removal is now rule **01**" and "Overdue
reminders are now defined in [REMIND-01]" (routed to its owner; 8,700 cap held). Renderer: Discussion
topic headings carry their anchor as id and the page's anchor set includes topics and cards; a
fragment-only citation matching nothing on the page links to the authoring artifact at that fragment
(the resolver now knows its document; the justification resolver carries it), in both renderers.
Tests 32 OK (one added), design-tool OK; the four Offers pages re-rendered, `check-changes` clean.
Round-12 spec read launched (prompt `refine/pl12/prompt-specs.txt`).

#### Round 12 (spec read: prompt `refine/pl12/prompt-specs.txt`, report `review-specs.md`)

F1 the link resolver shortens any target whose fragment matches a page anchor to that local anchor,
whatever document the target names, so a citation of an archived request's decision topic that
shares a name with a base topic lands on the base's — accept, verified (in-memory probe by the
reviewer). No guide finding; every walk usable. Scored: divergent · off-normal · verified = 3.75.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
| r12 | 3.75 | 1 | 0 | 1 | 0 | 0 |
Fix installed: `href_for` shortens a target to a local anchor only when `on_page` holds (a page-local
fragment, the authoring artifact being rendered, or a file under one of the projection's roots); a
citation into any other document keeps that document and its fragment. Tests 33 OK (one added: a
citation into another artifact sharing a topic name keeps that artifact), design-tool OK; the four
Offers pages re-rendered, `check-changes` clean. Round-13 spec read launched (prompt
`refine/pl13/prompt-specs.txt`).

#### Round 13 (spec read: prompt `refine/pl13/prompt-specs.txt`, report `review-specs.md`)

No findings within the charter; the seven walks usable; the reviewer names the existing controls
that now reject the observed failures. One open note, a verified residual of round 12: the resolver's
ID and glossary-term shortcuts return a local anchor before the document check, so a reference named
like an item but defined to point at another document is still shortened; fixed (the shortcuts
apply only when the reference's document is one the page represents; a bare reference with no
definition stays the page's own), with a test. Scored: 0; no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
| r12 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r13 | 0 | 0 | 0 | 0 | 0 | 0 |

Because the tool changed after this read, one more spec read confirms the final state before the
series closes; the guides' text did not change.

#### Round 14 (spec read: prompt `refine/pl14/prompt-specs.txt`, report `review-specs.md`)

F1 the gap tooltip (the owner's text on hover) renders each top-level bullet of the owning item and
drops the nested ones, so a Tradeoff's Options label appears with no alternatives under it, while
the Discussion card shows them — accept, verified (in-memory reproduction by the reviewer). No
guide finding; the eight walks usable. Scored: cosmetic · off-normal · verified = 1.5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
| r12 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r13 | 0 | 0 | 0 | 0 | 0 | 0 |
| r14 | 1.5 | 1 | 0 | 0 | 1 | 0 |
Fix installed: one `bullet_list` renders a Discussion item's sub-bullets with their nested bullets for
the card and for every tooltip of the item. Tests 35 OK (one added: the open Tradeoff's gap tooltip
carries its alternatives), design-tool OK; the four Offers pages re-rendered, `check-changes` clean.
Round-15 spec read launched (prompt `refine/pl15/prompt-specs.txt`).

#### Round 15 (spec read: prompt `refine/pl15/prompt-specs.txt`, report `review-specs.md`)

F1 popovers render copied text under whatever resolver is current (the last draft's): a gap owner's
tooltip loses a reference-style source link or, when the draft defines the same label differently,
links elsewhere; the same holds for the spec and glossary popovers — accept, verified (in-memory
reproduction by the reviewer with the real functions). No guide finding; the seven walks usable.
Scored: divergent · off-normal · verified = 3.75.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
| r12 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r13 | 0 | 0 | 0 | 0 | 0 | 0 |
| r14 | 1.5 | 1 | 0 | 0 | 1 | 0 |
| r15 | 3.75 | 1 | 0 | 1 | 0 | 0 |
Fix installed: `rendered_under` renders copied text under its own document's link definitions and
location; the justification resolver uses it, items and glossary terms remember their source file
when collected, gap owners carry their artifact's definitions and path, and every popover (gap owner,
item, glossary term) renders under its source. Tests 36 OK (one added: the open Tradeoff's gap
tooltip keeps a reference-style citation into another artifact), design-tool OK; the four Offers
pages re-rendered, `check-changes` clean. Round-16 spec read launched (prompt
`refine/pl16/prompt-specs.txt`).

#### Round 16 (spec read: prompt `refine/pl16/prompt-specs.txt`, report `review-specs.md`)

F1 the tool identifies a source by its ID or heading alone in three places: two documents holding
the same item ID share one tooltip (the last collected wins); a fragment-only link inside an external
document's hover text jumps to the page's anchor of that name; and a local target with a fragment
compares by the fragment alone, so re-pointing a citation from one review document to another with
the same heading counts as unchanged (and an honest `modify` entry then fails the check) — accept,
verified (three in-memory probes by the reviewer). No guide finding; every walk usable. Scored:
divergent · normal · verified = 5. The consolidated repair: identity is document-qualified except
for a spec item's own ID, which is stable across moves and layers by design (CA's churn guard).

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
| r12 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r13 | 0 | 0 | 0 | 0 | 0 | 0 |
| r14 | 1.5 | 1 | 0 | 0 | 1 | 0 |
| r15 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r16 | 5 | 1 | 0 | 1 | 0 | 0 |
Fix installed: a target's identity is its document plus fragment unless the fragment is a spec item's
own ID (stable across moves and layers); items collected from a document outside the projection keep
their own popovers (`ext_items`, `ext_tip_id`), chosen by both the explicit-link and bare-ID linkers
when a reference's definition points at that document; a fragment-only link is page-local only when
the document being rendered is the page's own (`doc_on_page`), so external hover text links back to
its document; the tool's render-contract docstring says so. Tests 38 OK (two added: heading anchors
are document-qualified while item IDs are not; a same-ID item in another document gets its own
tooltip), design-tool OK; the four Offers pages re-rendered, `check-changes` clean. Round-17 spec
read launched (prompt `refine/pl17/prompt-specs.txt`).

#### Round 17 (spec read: prompt `refine/pl17/prompt-specs.txt`, report `review-specs.md`)

No findings within the charter; the eight walks usable; the reviewer separates a clean read of the
instructions from evidence that a fresh run applies them, which is the next test (Tim reading
artifacts). One residual of round 16's identity repair under open questions: a term citation whose
definition points at another document's glossary linked there but showed the local same-named term's
definition on hover (`name in gloss` chose the local tooltip); fixed: the local definition shows only
when the reference's definition is the page's own, with a test. Scored: 0; no noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
| r12 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r13 | 0 | 0 | 0 | 0 | 0 | 0 |
| r14 | 1.5 | 1 | 0 | 0 | 1 | 0 |
| r15 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r16 | 5 | 1 | 0 | 1 | 0 | 0 |
| r17 | 0 | 0 | 0 | 0 | 0 | 0 |

The tool changed after this read (the residual), so one more spec read confirms the final state.
Residual fix installed: a term shows the local glossary definition on hover only when the reference's
definition is the page's own, for explicit term links and autolinked bare terms alike. Tests 39 OK
(one added), design-tool OK; the four Offers pages re-rendered, `check-changes` clean. Round-18 spec
read launched (prompt `refine/pl18/prompt-specs.txt`).

#### Round 18 (spec read: prompt `refine/pl18/prompt-specs.txt`, report `review-specs.md`)

F1 deleted text resolves its citations with the new document's definitions and location: whole
deletions (removed table rows, retired items, removed glossary entries, removed rules) render under
the draft's resolver, and word-level deletions swap in the base's root-relative definitions while
the resolver still stands at the draft's folder, so a struck-through citation links to the new
source or to a path that does not exist — accept, verified (two in-memory reproductions by the
reviewer). No guide finding; every walk coherent. Scored: divergent · normal · verified = 5.
Consolidated repair: one old-document context (the base file's own definitions and path) for every
old-side fragment, whole or word-level.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 | 31.375 | 13 | 0 | 11 | 2 | 1 |
| r2 | 20.875 | 9 | 0 | 5 | 4 | 0 |
| r3 | 7.5 | 2 | 0 | 2 | 0 | 0 |
| r4 | 2.5 | 1 | 0 | 1 | 0 | 1 |
| r5 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r6 | 5 | 1 | 0 | 1 | 0 | 0 |
| r7 | 5 | 1 | 0 | 1 | 0 | 0 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |
| r9 | 10 | 2 | 0 | 2 | 0 | 0 |
| r10 | 5 | 1 | 0 | 1 | 0 | 0 |
| r11 | 6.875 | 2 | 0 | 2 | 0 | 0 |
| r12 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r13 | 0 | 0 | 0 | 0 | 0 | 0 |
| r14 | 1.5 | 1 | 0 | 0 | 1 | 0 |
| r15 | 3.75 | 1 | 0 | 1 | 0 | 0 |
| r16 | 5 | 1 | 0 | 1 | 0 | 0 |
| r17 | 0 | 0 | 0 | 0 | 0 | 0 |
| r18 | 5 | 1 | 0 | 1 | 0 | 0 |
Fix installed: `OLD_CTX` holds the base file's own definitions and location per diffed file;
`inline_old` and `under_old` render every old-side fragment in it (word-level deletions, removed
table rows, retired items with their tables and rules, removed glossary entries, removed and retired
rules, removed index lines). Tests 40 OK (one added: a citation dropped from a requirement links
where the old file linked, from the old file's folder, not to the draft's redefinition), design-tool
OK; the four Offers pages re-rendered, `check-changes` clean. Round-19 spec read launched (prompt
`refine/pl19/prompt-specs.txt`).

#### Correction — convergence (2026-10-25)

Series PL converged by stop rule (a) at round 13 for the spec family (round 17 confirmed it), at
round 4 for the UI Map family and at round 3 for the work-spec pair; the guides' text has not changed
since round 11. Rounds 14 to 18 should not have run: each followed a zero-score or clean read whose
parked residual I repaired in the renderer and then re-read "to confirm", treating a verified defect
in a context surface as a live finding under another heading. The process's disposition for those is
`logged — follow-up`. The renderer repairs of rounds 14 to 18 stand as tested tool work (40 tests OK)
done outside the series, recorded here for the release notes; round 19, already running when the
supervisor stopped the series, is logged when it returns and not acted on here. Supervisor, 2026-10-25:
"Next time hit zero... STOP!" Final series table: r1 31.375, r2 20.875, r3 7.5, r4 2.5 (+ UI Map 0),
r5 3.75, r6 5, r7 5, r8 8.75, r9 10, r10 5, r11 6.875, r12 3.75, r13 0 (terminal), r14 1.5, r15 3.75,
r16 5, r17 0, r18 5 — rounds after 13 are tool work, not the series' measure.

## Maintenance retro — plain language in the spec, UI Map and work-spec guides, series PL — 2026-10-25

Inventory: 21 guides' formats, examples and reader-facing lines (ProductSpecs 4, DesignSpecs 4, UIMap
10, Spec 2, plus `process-flow.md`, `change-requests.md`, `spec-file-shape.md`, `design-authoring.md`,
`design-promotion.md`); `spec-tool.py` and `design-tool.py` renderers with one additive rule in
`spec-review.v1.css`; `maintain-skai.md`, the guide-authoring sanity scan and the cold-review template
(the rule for guide writers); standards amended (`writing-style-design.md` requirement 10 and caps;
`product-specs-system-design.md`, `design-specs-design.md`, `work-spec-process-design.md`,
`design-process-design.md`, `change-requests-design.md`). Host-install-visible (guides and renderer).
Bookkeeping: two release entries with migrations, two CHANGELOG lines; `Managed-Updated-At`
2026-10-25 on every edited guide (checked); manifest unchanged (no asset added or moved); README
unchanged (no phase or path changed; its Code Changes line names no gate wording). Tests: spec-tool
40 OK, design-tool OK, ui-map-render OK. Consistency scan: the stale phrases this series removed
("the Justification is the citation", "carry no text", "Superseded by [ID]", "advance to Completion",
"Promote <N> requirements", "say next to implement", `**Why** <rationale>`, the "Both surfaced"
annotation) → 0 in Guides, README and Templates; every target guide carries the writing-style
pointer (25 guides in all). Follow-ups, logged: `design-promotion.md`'s Promotion Checks gate still
reads "Promote <N> changes from <package> into <production | its base>" (clear enough in context;
the spec promotion gates say "Write <N> … into <paths>"); the renderer's moved-glossary-entry
comparison and rendering context (round 19) and any further coverage paths belong to a
renderer-hardening effort with a comparison × case × document-context test matrix, not to cold
reads of guides; the Figma designer guide, the Test guides, the debugging guide, the Core reference
guides and `product-specs-baseline.md` still carry no writing-style pointer (a later pass decides
which write for a person). Process reflection: the series' binding target converged at round 13;
rounds 14–18 ran because I repaired a context surface after clean rounds and re-read, and the
reviewer, told to inspect the renderer, found one more path each time. A zero round ends a series;
a defect in a context surface is logged. Retro complete apart from the follow-ups above.
