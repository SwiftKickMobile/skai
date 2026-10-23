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

