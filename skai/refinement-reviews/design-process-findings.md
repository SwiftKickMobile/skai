# Design process — findings log

Targets: `Guides/Design/design-authoring.md`, `Guides/Design/design-promotion.md`. Standard: [`design-process-design.md`](design-process-design.md).

## 2026-10-12 — design-authoring.md, series 1

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-12 r1 | F1: "draw every resolved item" read as the drawing scope, though Discussion holds only decisions | closed (superseded by r2 F1) | Restated at r2 |
| 2026-10-12 r1 | F2: a visually-judged item stayed unchecked, blocking the mockup phase it needed | closed | The supervisor resolves it by approving the recommended option as a trial; the mockup shows it, feedback settles it |
| 2026-10-12 r1 | F3: gate note and Mockups gave different feedback transitions | closed | One sequence in Mockups (apply what needs no decision; park the rest with dependent drawing; review gate or Discussion gate); Phases and the gate note point to it |
| 2026-10-12 r1 | F4: reopening an approved, unpromoted package left Design Changes standing as approval evidence | closed | A reopen that changes the designs removes Design Changes; rewritten after the next approval |
| 2026-10-12 r1 | F5: a draft's new component had no placement satisfying both the authoring boundary and the tool guide | routed | Fixed in `figma-designer-guide.md` (Components 1, Screen pages 7): a change page holds a draft's new components until promotion |
| 2026-10-12 r1 | F6: example proposal assigned defect logging, outside scope | closed | Clause deleted |
| 2026-10-12 r1 | F7: intervening production changes on reopen unspecified | logged | No occurrence; the general blocked gate covers a conflict that stops work |
| 2026-10-12 r2 | F1: "each resolved decision applied" reinstated a decision later feedback changed | closed | Mockups: draw the whole change as the decisions and any later feedback currently stand; a changed decision is history |
| 2026-10-12 r2 | F2: a decision discovered while drawing has only the generic blocked gate | logged | No occurrence; the generic gate is a safe stop |
| 2026-10-12 r3 | No live findings | closed — clean fresh round | Reviewer confirmed the r1–r2 repairs; one open tension (judging what needs a decision) left to the existing criterion |

Series 1 (authoring): r1 10.625 → r2 2.5 → r3 0. Converged by a clean fresh round. Size 14,441 →
14,790 bytes against the 16,000 cap. `design-promotion.md` not yet reviewed.

## 2026-10-12 — design-promotion.md, series 1

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-12 p1 | F1: the authoring-return gate line covered any failed check, though C3/C4 faults are repaired in place; "C4 changes production" was wrong | closed | Line limited to readiness, C1, C2, requested design change; C3/C4 mistakes repaired in place, never by redesign; missing access takes the standard line |
| 2026-10-12 p1 | F2: C3 "nothing outside the inventory changes" forbade the placement it also required | closed (superseded by p2/p3) | Restated twice; final wording at p3 |
| 2026-10-12 p1 | F3: production review gate line said "Production reviewed" before the review | closed | Line now asks for the review and names the change page to delete |
| 2026-10-12 p1 | F4: recovery after rejection at production review unspecified (restore target; links already repointed) | logged | No occurrence; route mechanics to the tool guide when one appears |
| 2026-10-12 p2 | F1: "on re-run every check is unchecked" plus readiness sent an unfinished promotion to authoring | closed | Unfinished promotion continues from its pending check or gate; reset applies to a new run after an authoring return; readiness is for a new run |
| 2026-10-12 p2 | F2: C3 "new components move to the library" overrode the tool guide's placement exceptions | closed (superseded by p3 F1) | Restated at p3 |
| 2026-10-12 p3 | F1: C2 "extra drafts" rejected a draft's supporting components; C3's component clause had no referent (third round on that clause) | closed — class fix | No component mechanics in the process guide: C2 inventories screen drafts, C3 integrates components "as the tool guide says". Invariant P1: the process guide says what promotion must achieve; how designs are arranged is the tool guide's |
| 2026-10-12 p3 | F2: the artifact alone cannot show whether a gate was advanced when resuming without the conversation | logged | No occurrence; the standard blocked gate covers missing authorisation |
| 2026-10-12 p4 | F1: C1 read as "a script, if any, is the whole check" | closed | A script covers the rules it tests; inspect the rest; evidence example shows both |
| 2026-10-12 p4 | F2: an evidence-only readiness failure fits neither continuation nor new-run wording cleanly | logged | New-run path; no occurrence |
| 2026-10-12 p5 | No live findings | closed — clean fresh round | Reviewer confirmed all repairs; residual risks are operator diligence, not wording |

Series 1 (promotion): p1 6.875 → p2 4.375 → p3 2.5 → p4 2.5 → p5 0. Converged by a clean fresh
round. Size 11,264 → 11,812 bytes against the 12,000 cap.
| 2026-10-12 post | Tim: per-tool skills were inconsistent with UI Map implementation, which is one skill whose guide loads the stack guide | closed — by ruling | Skills renamed `skai-design-authoring` / `skai-design-promotion`, tool-agnostic; each process guide's Purpose now loads the tool guide for the project's design tool (Figma → `figma-designer-guide.md`), told from the README's design-file link. Sizes 14,860 / 11,872 bytes, under their caps |
| 2026-10-12 post | SKAI Release 11 merged after both series: typed packages (`skai/changes/<id>/design/`, archived to `skai/promoted/<id>/design/`), Project addendum boilerplate, configure metadata | closed — by ruling (Tim: revisit the skills for addenda and configuration) | Authoring: package path, scan path, promoted = closed. Promotion: artifact path, readiness item 4, `C6 Archive the package`, Completion. Both guides carry the addendum cue and footer; skills read the guide "in full, including its Project addendum instructions"; manifest gains a Design category with labels. Caps raised to 16,500 / 13,500 for the boilerplate. Not re-reviewed |
