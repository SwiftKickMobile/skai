# Figma designer guide — findings log

Target: `Guides/Design/figma-designer-guide.md` (+ `figma-designer-guide-multiple-sizes.md`). Standard: [`figma-designer-guide-design.md`](figma-designer-guide-design.md).

## 2026-10-10 — round 1

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-10 r1 | F1: general rules contradict the multiple-form-factor and draw-intent rules (Production "no other place", frame-name uniqueness, `type/` only, "what the app does today") | closed | Pages 2 points to form-factor pages; canvas table and Screen pages scope include them; frame names unique per page; Styles 3 / Dimensions 2 say "a dimension variable"; "the current design" |
| 2026-10-10 r1 | F2: "start new screens from an existing screen" impossible for the first screen | closed | Components 5: the first screen builds its shell from the kit (rule 6) |
| 2026-10-10 r1 | F3: platform-specific mandates (partial-height sheet, Apple renderer) and off-theme examples | closed | Overlay rules merged, size and dimming follow the platform; target platform's render for PDFs; LumenNotes examples |
| 2026-10-10 r1 | F4: custom-font layout prerequisite stranded in Agent tooling 8 | closed | Folded into Custom fonts 2; practice 8 deleted |
| 2026-10-10 r1 | F5: guide over the 17,500-byte cap (19,899) | closed | 17,413 bytes after compression; no rule removed |
| 2026-10-10 r1 | Open question: zero spacing / square corners not on a scale starting at 1 | logged | 0 is the absence of a value, not a step; single observation, no operator has hit it |

## 2026-10-10 — round 2

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-10 r2 | F1: component-state crops and "interactions that reveal more UI" conflict with control states in component sets and overlays as screen states | closed | Screen pages 2 says interactions *within a component*; Frames 4 component-crop naming deleted; Screen pages 1 "crops of them" |
| 2026-10-10 r2 | F2: Frames device size and `screen — state` naming read as applying to documentation and asset frames | closed | Frames 1 and 5 scoped to screen frames; per-page uniqueness still applies to every frame |
| 2026-10-10 r2 | F3: form-factor instances all at device size, against taller and cropped frames | closed | Multiple form factors 3: instances sized by Frames |
| 2026-10-10 r2 | F4: shell reuse assumes a compatible screen exists (r1 F2 repair) | closed | Components 5: copy a screen with the same shell, otherwise build from the kit |

## 2026-10-10 — round 3

Consolidation trigger fired a second time (F1 and F2 were about round-2 repairs), so F1 and F2 went
to the supervisor under stop rule (b); both dispositions below are supervisor rulings, not refiner
triage.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-10 r3 | F1: a component that opens a popover fits both Screen pages 2 (reference frame) and 5 (screen state) | closed (supervisor ruling) | Ruled: an overlay the screen presents is a screen state, even one a component opens; a Reference frame is for changes inside the component. Screen pages 2 gains "(a keyboard key's highlight)"; the spec's settled decision updated to match |
| 2026-10-10 r3 | F2: "no two frames on a page share a name" read as covering nested layers inside copied screens | rejected (supervisor ruling) | Renaming nested layers is a hypothetical literal misreading, not normal use; the wording predates this pass and no operator has hit it |
| 2026-10-10 r3 | F3: Multiple form factors 3 "the mode alone changes their dimensions" read as resizing the frame | closed | Now "the mode changes their spacing and type"; instance sizing stays with Frames |

## 2026-10-10 — round 4

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-10 r4 | F1: dormant whole screens carry no marker, yet everything else on `Production` is called current | closed | Screen pages 6: dormant designs stay on `Production` with `legacy` in the frame name, before the whole-screen / crop branch (the guide's existing marker, relocated) |
| 2026-10-10 r4 | F2: "every fill and stroke binds a color variable" read as covering image fills | rejected | Hypothetical literal misreading: the rule is "Colors are variables" and bans hard-coded hex/RGB; Components 4 mandates image components; same class as the r3 F2 ruling |

## 2026-10-10 — round 5 and series close

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-10 r5 | F1: dormant designs "stay on `Production`" read as excluding a form-factor page's own designs | rejected | Hypothetical literal misreading: Screen pages is scoped to `Production` and its form-factor pages, Pages 2 makes them part of `Production`, and "stay" keeps a design where it is |
| 2026-10-10 r5 | F2: Dimensions 2 "one mode per form factor" restates Multiple form factors 1 | logged | Cosmetic; the two agree and one mode burdens no single-form-factor file. Ready trim for a later pass: delete the sentence (−48 bytes) |

Series summary: scores r1 10.125 → r2 9.375 → r3 3.75 (6.25 before the supervisor rulings made r3
F2 noise) → r4 1.875 → r5 0. Round 3 hit the consolidation trigger a second time and R3-F1/F2 were
settled by supervisor ruling (convergence-by-ruling); round 5 then came back with no live findings
over the repaired text (convergence-by-clean-round, stop rule a). Net guide size 19,899 → 17,297
bytes (−2,602), under the 17,500-byte budget.

## 2026-10-11 — scope change (new series)

Tim widened the scope: the guide is platform-agnostic (web included) and carries no implementation
details of any codebase; it is renamed `figma-designer-guide.md`, multiple-target-size rules move to
the linked `figma-designer-guide-multiple-sizes.md`, the custom-font fallback becomes a stop-and-ask,
and a Working a backfill section is added. The spec was rewritten. Scores before this entry belong
to the previous series and are not comparable with later rounds.

## 2026-10-12 — series 2 (platform-agnostic guides)

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-12 s2r1 | F1: overlay rule and shell fallback required kit parts even where no kit supplies them | closed | Both defer to Components 6 ("where a kit supplies one") |
| 2026-10-12 s2r1 | F2: "tall enough to show all possible content" distorted layouts with an inner scrolling region; Copy 3 duplicated it | closed | Frames 3: whole-screen scroll shows representative content, inner region keeps the frame |
| 2026-10-12 s2r1 | F3: device and size examples remained (landscape tablet, 360px, phone and tablet) | closed | Deleted; grep for device names clean |
| 2026-10-12 s2r2 | F1: "Text is never clipped" conflicted with scrolling regions and crops | closed (superseded by s2r3 F1) | Restated at s2r3 |
| 2026-10-12 s2r2 | F2: Pages 2 prescribed frame replacement (a promotion step) | closed | Sentence deleted |
| 2026-10-12 s2r2 | F3: "set reflows as variants change" contradicted explicit grid placement | closed | Clause deleted |
| 2026-10-12 s2r3 | F1: "a container grows with its text" forbade intentional truncation (third round on Copy 3) | closed | Restated by principle: text shown as the design handles it (wrapped, truncated, scrolled), never cut off by a too-small container. Invariant P1: copy rules say what is depicted, not how layout responds |
| 2026-10-12 s2r3 | F2: Dimensions 2 mentioned modes without routing to `-adapt` | closed | Routes to the multiple-sizes guide; modes defined only there |
| 2026-10-12 s2r3 | F3: drafting several target sizes of one screen on a change page | logged | Belongs to the authoring process guide (unwritten); no strand observed |
| 2026-10-12 s2r4 | F1: Components 2 read as requiring exactly two variant properties | closed | "arranges its variant properties along the axes (… a single property runs across)" |
| 2026-10-12 s2r5 | F1: "every fill binds a color variable" read as covering image fills | rejected | Re-raise of series-1 r4 F2: a literal misreading no operator hits; image content is not a colour |
| 2026-10-12 s2r5 | F2: only "a new variable's" Dark value followed the mirror rule | closed | "A variable's Dark value mirrors…"; copy from Light "to start" |
| 2026-10-12 s2r5 | Three or more variant properties on two axes | logged | Reviewer's own call; no strand; replace the example if it recurs |
| 2026-10-12 s2r6 | F1: "nothing is rebound" when adding dark mode conflicted with deviant colours needing a rebinding | closed — by ruling | Tim: edge cases are expected; sentence deleted |
| 2026-10-12 s2r6 | F2: frame-name uniqueness read as covering nested frames | rejected | Same as series-1 r3 F2, rejected by ruling |

Series 2: s2r1 5.375 → s2r2 7.5 → s2r3 4.375 → s2r4 2.5 → s2r5 1.875 → s2r6 1.875. Tim stopped
the series after round 6 ("good enough territory"); convergence is by ruling on the one open
item (s2r6 F1, applied), not by a clean round. Size: 16,003 → 16,053 bytes for both guides against
the 17,500 cap (series 1 took the single guide from 19,899 to 17,297 before the scope change).
| 2026-10-12 post | Tim: how Dark colours are chosen (adding the mode, mirroring lightness) is methodology, not a file convention | closed — by ruling | Both bullets deleted from Styles 1; deviant naming, Light pins and the both-mode check remain |
| 2026-10-12 routed | From design-authoring r1 F5: a new component a draft needs had no placement satisfying both the authoring boundary and Components 1 / Screen pages 7 | closed | Both rules now allow a change page to hold a draft's new components until promotion moves them |
| 2026-10-12 post | SKAI Release 11 Project addendum boilerplate added to both guides (cue after the title, footer with the lookup names `figma-designer-guide` and `figma-designer-guide-multiple-sizes`) | closed — by ruling | Combined cap raised 17,500 → 19,000 for the ~750 bytes per guide of mandatory boilerplate; no rule changed. Not re-reviewed |

## 2026-10-14 — series 3 (scoped: chrome content lost on size pages)

Scoped review on an observed failure: following rule 5, chrome content set through properties in
each screen component showed component defaults on every instance on a second size's page; setting
the properties inside those instances held.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-14 s3r1 | F1: rule 5 implied component properties set in the screen component survive the variant switch | closed | Rule 5 now has the chrome's properties set again inside each size-page instance; the draft's "drops whatever" and case examples dropped as broader than the evidence |
| 2026-10-14 s3r2 | F1: "set on each screen instance" left unclear whether the values go on the screen instance or the chrome inside it | closed | "Inside each screen instance on a size page, the chrome's properties are set again to the screen component's values" |
| 2026-10-14 s3r3 | No findings | — | Clean round over the current text |

Series 3: s3r1 2.5 → s3r2 2.5 → s3r3 0; converged by a clean round. Size 17,872 → 18,007 bytes
for both guides against the 19,000 cap; 16,674 after merging the shorter Project Addendum footer.
