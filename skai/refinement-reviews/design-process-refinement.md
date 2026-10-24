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

