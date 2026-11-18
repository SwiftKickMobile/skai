Managed-By: skai
Managed-Id: guide.design-promotion
Managed-Source: Guides/Design/design-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-17

# Design Promotion

Print `📖 SKAI guide: design-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Fold the completed package ([`design-authoring.md`](design-authoring.md)) into its **base** per
[`change-requests.md`](../Core/change-requests.md): a change page's or request section's drafts into it.
The fold carries each change to every affected base
frame. The package is archived; its drafts and backups stay in the design file until the
supervisor asks for cleanup ([`design-cleanup.md`](design-cleanup.md)) or deletes them.

Refactor the base to absorb drafts; any redesign returns to authoring. For Figma, load
[`figma-designer-guide.md`](figma-designer-guide.md): it owns pages, sections, production, the component library and design conventions. A package
whose `## Design Changes` lists a style, value or component also follows
[`design-system-changes.md`](design-system-changes.md).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## The promotion artifact

Write `design-promotion.md` beside the authoring artifact:

```
# Design Promotion — <name>
## Inputs               the package being promoted; its base; the design file
## Promotion Checks     - [ ] C<n> items, unchecked until executed
## Evidence             the verification trail
```

## Gates

Whenever you are waiting on the supervisor, end the message with a `⏳ GATE:` line. The one exception is workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion items and reviews its gates; the executing agent does not resolve or approve its own.

**Gate persistence.** After emitting a `⏳ GATE:` line, end every response, discussion and clarifications included, with that line verbatim until the gate moves. Change it only when its content changes (a blocker emerges, or `Next` needs revising), and then emit the new line in full. Never paraphrase, shorten or silently change it.

**No fabricated gates.** Use `⏳ GATE:` only for the gates this section defines. Never invent one for discussion state, partial completion or an intermediate review; a gate this guide lacks is a process improvement to file.

At a planned gate, summarize what you did and what happens next, end with the gate's line, then STOP and wait for the supervisor. This workflow has two:

- **Promotion Checks**, after readiness and before the base is changed. `Next` executes
  `C1`–`C4`; name the base and changes from `## Design Changes`.
  - `⏳ GATE: Next: Promote <N> changes from <package> into <production | its base <base>>. Say "next" or what to change.`
- **Base review**, after `C4`. The supervisor reviews the base's drawings, any Design Changes
  folded in undrawn, `C3`'s audit of what the fold carried beyond them, and any trim or redraw it
  proposes. Name every place `C3` marked as merged and the package whose change it merged. A requested
  design change blocks: restore the base's drawings and design system changes from backup, with
  gap mirrors, and its artifact, pages and links to before `C3`; return to authoring, where the
  next run folds afresh.
  - `⏳ GATE: Next: Review <production | the base's drawings and Design Changes>. Say "next" to confirm and archive the package, or what to change.`

An unexpected blocker takes `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.` and a STOP until the supervisor resolves it. This workflow's own blocked gates:
- A readiness failure (1–3 except an open request part; 5 if an outcome invalidates mockups), `C1` or `C2`
  failure, or a design change requested at either gate returns to authoring:
  `⏳ GATE: Blocked: <C1 | C2 | readiness condition | requested design change> — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- Without a failure, open request parts, existing destinations, pending outcomes, another
  promotion waiting for its review (6) and a conflict (7) take the standard blocked gate naming
  all; otherwise name them at the failure's gate.
- A `C3` (base) or `C4` (links) fault is a promotion mistake repaired in place, never by
  redesigning; one needing access or a library the agent lacks takes the standard blocked line.

## Advance intent

Advance intent moves past the current gate: "next", "continue", "go ahead", "do it". It counts only after you have output a `⏳ GATE:` line; "we should...", "let's..." are discussion, NOT authorization. Outside a gate, never use "begin"/"next"/"continue" to skip a check or a gate.

`auto` bypasses the Promotion Checks gate only. It never bypasses a blocked gate, or Base review: the supervisor looks at the base before the package archives. `auto to <milestone>` stops before the named gate: `promotion checks`, `base review`.

**Markers.** This workflow's markers are the `- [ ] C<n>` items in
`## Promotion Checks`, written unchecked before the first gate. After advance intent, `C1`–`C4`
run in order and are checked as each passes, with evidence; a failing `C1` or `C2` is
left unchecked and nothing after it runs. `C5` runs only after the Base review gate
advances. An unfinished promotion (`C5` unchecked) resumes at its pending check or gate, within `C3` where it stopped, keeping its backups. **A new run after an authoring return unchecks every check** and starts from `C1`; prior
evidence stays under `### Run <n>`.

## Initiation

Begin only on an explicit signal ("promote the designs"), never automatically after authoring. A
request to clean up after a promoted package follows `design-cleanup.md`.

Read the tool guide. The package is the one named or in context; one already holding an
unfinished `design-promotion.md` continues (*Advance intent*), `C3` re-checking 1 and 4–7; the
readiness screen is for a new run.

### Readiness screen

Render the page; verify before writing checks:

1. Into production: no other open `design/` request part in the change; no footnote or open Discussion item or gap
   ([`known-gaps.md`](../Core/known-gaps.md)) in the package, nor, but for closed gaps' footnotes, in the change's promoted `design/` sub-packages, at any depth.
2. `## Design Changes` is current, Review advanced and inputs reconciled (authoring's *Completion*).
3. `add` and `modify` entries link drafts on the change page or request section, unless the
   no-mockups ruling under `## Assumptions and TODOs` leaves them undrawn; undrawn entries never
   enter production. `remove` entries name the base design. A rename (`design-system-changes.md`)
   has no draft, links nothing and is not undrawn.
4. The `design/` destination (*C5*) is absent.
5. Every non-base input this package's decisions changed has its outcome applied ([`change-requests.md`](../Core/change-requests.md) rule 8), now and at the base write.
6. No other package's promotion has changed this base and still waits for its Base review.
7. No change of this package has an unresolved conflict with one another package made first; a
   moved base never sends a package back to be redrawn. From source control
   history, list the packages promoted into this base since this package was first recorded, and
   compare their `## Design Changes` with this package's; a base package's own list holds its
   promoted requests' entries. Name the packages compared in `## Evidence`. For an item both
   changed: where both changes can stand, `C3` merges them; where they cannot, block for the
   supervisor's choice and record it in `## Evidence`.

Record blockers in `## Evidence`, not checks; block.

## Promotion Checks

Write `- [ ] C<n> <identity>` items in execution order.

- `C1 Drafts meet the conventions` — with drawings, run and pass the tool guide's structure
  check; drafts follow the guide and, into production, mirror no gap. Inspect what the script does not test.
- `C2 Inventory matches the drawings` — per section, each linked `## Design Changes` entry has a
  draft; every screen draft of this package has an entry. Design system entries:
  `design-system-changes.md`.
- `C3 The base absorbs the package` — with conditions 1 and 4–7 met:
  1. From `## Design Changes`, list the rules the changes set, each with the entries that set it;
     audit every base frame against them, by rule and by eye, hosts behind overlays
     included; a working document names every base frame, its rules and its change or none, updated as
     applied: `C3`'s evidence, into production too.
  2. Back up the base, then copy the drafts in, never move them (where: the tool guide).
  3. Apply design system entries first, per `design-system-changes.md`. Apply draft changes to existing screens, keeping identities; place new screens or states and
     integrate needed components per the tool guide; delete removed designs; carry every rule to
     every base frame it affects. A removal or redraw beyond the package's changes is only
     proposed, at Base review. Where condition 7 found changes that can both stand,
     apply this package's to the base as it stands, keep the other's, and mark the place in
     the form the tool guide gives. The supervisor's recorded choice replaces any entry it
     overrules, in every step. Where the design file keeps screens at several target sizes,
     keep every size's set complete, as the tool guide says. Purpose notes travel with their frames and are never
     stripped; rewrite one that no longer fits, such as a draft's note on the one change it showed
     that now sits on the approved design of a whole state.
  4. Screenshot every touched frame; check what copying breaks: a pairing (a tab's unread dot needs
     unseen content on screen), a pattern that belongs to one stage, an instance still linked to a
     draft's component. Run authoring's sample-data check on the merged base.

  Into production, the per-screen sections do not survive: every column is regrouped into
  `Production`'s feature areas. Into a package, fold screen sections into same-named sections in
  the Section holding the base's drawings (create missing ones), and:
  - Append entries to the base's `## Design Changes`, each under its screen or design system heading: next `V`
    numbers, or sub-IDs under a frame the base lists, Descriptions kept, bare `D<n>` linked to the request, each Justification or sub-change ending `; Change request: CR-<id> V<n>`. Undrawn entries stay unlinked,
    go only to the base's list, and return it to Mockups to draw them.
  - Record changes carried to the base's own frames on their entries: a sentence on an add, a
    sub-change on a modify, a remove entry for a trim.
  - Fold footnotes (drop any whose gap the base owns or already footnotes) and decisions on base items (each still open) per
    `change-requests.md`, mirrors per the tool guide; name the request in the base's `## Assumptions and TODOs`.
- `C4 Links point at the base` — repoint existing `add` and `modify` links, appended too,
  to where the base shows them; a `remove` entry keeps its name; re-render every page whose
  artifact changed, this package's too.
- `C5 Archive the package` — remove `C3`'s merge marks; move the folder intact with `working-docs/`: to
  `skai/promoted/<change-id>/design/` for a change's own package, with its promoted request parts per `change-requests.md`, leaving siblings and removing
  an empty `<change-id>` folder; a request's sub-package to its destination per `change-requests.md`. Repair links into and inside moved
  files and mirrors' owner paths, keeping targets; re-render moved pages and a request's base, if a package, verify the move and check
  `C5` in the archived artifact.

**Excerpt** (at the Base review gate: `C1`–`C4` checked, `C5` unchecked):

```markdown
## Evidence

[evidence: C3; working-docs/fold-audit.md names all 14 base frames against 3 rules (pinned group, no unread dot, pin glyph gone), each with what changed or no change — 3 drafts copied, 6 more frames updated, 5 unchanged, 1 trim proposed (notes — pinned only, now redundant)]
```

## Evidence

One bracket per check:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Persist and link full failure output. An inspection names its subject precisely enough to repeat
it; silence is not a pass: name what was compared and found.

## Completion

With `C5` checked, link the archived artifact; name what the base owes, the drafts and backups left in the design file (removed on a cleanup request), and each gap open in or under the
package and where it was raised; end with
`🏁 Complete. Let me know if anything needs adjustment.`
If archival fails after Base review, report the base promoted, archival incomplete, use the standard
blocked gate and resume only archival.

## Project Addendum

If `<active-project-root>/skai/addenda/design-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
