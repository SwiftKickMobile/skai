Managed-By: skai
Managed-Id: guide.design-promotion
Managed-Source: Guides/Design/design-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-11

# Design Promotion

Print `📖 SKAI guide: design-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Fold the completed package ([`design-authoring.md`](design-authoring.md)) into its **base** per
[`change-requests.md`](../Core/change-requests.md): a change page's or request section's drafts into it.
Drafts show each change in as few frames as needed; the fold carries it to every affected base
frame. The supervisor deletes drafts and backup; the package is archived.

Refactor the base to absorb drafts; any redesign returns to authoring. For Figma, load
[`figma-designer-guide.md`](figma-designer-guide.md): it owns pages, sections, production, the component library and design conventions.

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

Core rule: every time the agent is waiting on the supervisor, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion items and reviews its gates; the executing agent does not resolve or approve its own.

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the supervisor.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the supervisor gives advance intent. If the gate is non-standard, make it describe the exact supervisor response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the supervisor resolves it.

Workflow-specific gate notes:
- At the Promotion Checks gate — after readiness, before changing the base — `Next` executes
  `C1`–`C4`; name the base and changes from `## Design Changes`.
  - `⏳ GATE: Next: Promote <N> changes from <package> into <production | its base <base>>. Say "next" or what to change.`
- At the non-standard Base review gate, the supervisor reviews the base's drawings, any Design
  Changes folded in undrawn, and `C3`'s audit of what the fold carried beyond them and any trim or
  redraw it proposes. A requested design change blocks: restore the base's drawings from backup,
  with gap mirrors, and its artifact, pages and links to before `C3`; return to authoring, where the
  next run folds afresh.
  - `⏳ GATE: Next: Review <production | the base's drawings and Design Changes>. Say "next" to confirm and archive the package, or what to change.`

Workflow-specific blocked gates:
- A readiness failure (1–3 except an open request part; 5 if an outcome invalidates mockups), `C1` or `C2`
  failure, or a design change requested at either gate returns to authoring:
  `⏳ GATE: Blocked: <C1 | C2 | readiness condition | requested design change> — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- Without a failure, open request parts, existing destinations and pending outcomes take the
  standard blocked gate naming all; otherwise name them at the failure's gate.
- A `C3` (base) or `C4` (links) fault is a promotion mistake repaired in place, never by
  redesigning; one needing access or a library the agent lacks takes the standard blocked line.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestones in this workflow: `promotion checks`, `base review`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the supervisor gives advance intent.

**Workflow-specific marker lifecycle.** This workflow's markers are the `- [ ] C<n>` items in
`## Promotion Checks`, written unchecked before the first gate. After advance intent, `C1`–`C4`
run in order and are checked as each passes, with evidence; a failing `C1` or `C2` is
left unchecked and nothing after it runs. `C5` runs only after the Base review gate
advances. An unfinished promotion (`C5` unchecked) continues from its pending check or gate, never
restarts. **A new run after an authoring return unchecks every check** and starts from `C1`; prior
evidence stays under `### Run <n>`.

**Workflow-specific `auto` behavior.** `auto` bypasses the Promotion Checks gate but never the
Base review gate: the supervisor looks at the base before the package archives.

## Initiation

Begin only on an explicit signal ("promote the designs"), never automatically after authoring.

Read the tool guide. The package is the one named or already in context; one already holding an
unfinished `design-promotion.md` continues (*Advance intent*), `C3` re-checking 1, 4 and 5; the
readiness screen is for a new run.

### Readiness screen

Render the page, then verify before writing the checks:

1. Into production: no other open `design/` request part in the change; no footnote or open Discussion item or gap
   ([`known-gaps.md`](../Core/known-gaps.md)) in the package, nor, but for closed gaps' footnotes, in the change's promoted `design/` sub-packages, at any depth.
2. `## Design Changes` is current, Review advanced and inputs reconciled (authoring's *Completion*).
3. `add` and `modify` entries link drafts on the change page or request section, unless the
   no-mockups ruling under `## Assumptions and TODOs` leaves them unlinked; unlinked entries never
   enter production. `remove` entries name the base design.
4. The `design/` destination (*C5*) is absent.
5. Every non-base input this package's decisions changed has its outcome applied ([`change-requests.md`](../Core/change-requests.md) rule 8), now and at the base write.

Record blockers in `## Evidence`, not checks; block.

## Promotion Checks

Write `- [ ] C<n> <identity>` items in execution order.

- `C1 Drafts meet the conventions` — with drawings, run and pass the tool guide's structure
  check; drafts follow the guide and, into production, mirror no gap. Inspect what the script does not test.
- `C2 Inventory matches the drawings` — per section, each linked `## Design Changes` entry has a
  draft; every screen draft of this package has an entry.
- `C3 The base absorbs the package` — with conditions 1, 4 and 5 met:
  1. From `## Design Changes`, list the rules the changes set, each with the entries that set it;
     audit every base frame against them, by rule and by eye, hosts behind overlays
     included; a working document names every base frame, its rules and its change or none, updated as
     applied: `C3`'s evidence, into production too.
  2. Back up the base, then copy the drafts in, never move them (where: the tool guide).
  3. Apply draft changes to existing screens, keeping identities; place new screens or states and
     integrate needed components per the tool guide; delete removed designs; carry every rule to
     every base frame it affects. A removal or redraw beyond the package's changes is only
     proposed, at Base review.
  4. Screenshot every touched frame; check what copying breaks: a pairing (a tab's unread dot needs
     unseen content on screen), a pattern that belongs to one stage, an instance still linked to a
     draft's component.

  Into production, the per-screen sections do not survive: every column is regrouped into
  `Production`'s feature areas. Into a package, fold screen sections into same-named sections in
  the Section holding the base's drawings (create missing ones), and:
  - Append entries to the base's `## Design Changes`, each under its screen: next `V`
    numbers, or sub-IDs under a frame the base lists, Descriptions kept, bare `D<n>` linked to the request, each Justification or sub-change ending `; Change request: CR-<id> V<n>`. Undrawn entries stay unlinked
    and return the base to Mockups to draw them.
  - Record changes carried to the base's own frames on their entries: a sentence on an add, a
    sub-change on a modify, a remove entry for a trim.
  - Fold footnotes (drop any whose gap the base owns or already footnotes) and decisions on base items (each still open) per
    `change-requests.md`, mirrors per the tool guide; name the request in the base's `## Assumptions and TODOs`.
- `C4 Links point at the base` — repoint existing `add` and `modify` links, appended too,
  to the base's drawings; a `remove` entry keeps its name; re-render every page whose
  artifact changed, this package's too.
- `C5 Archive the package` — move the folder intact with `working-docs/`: to
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

With `C5` checked, link the archived artifact; name what the base owes, drafts and backup for the supervisor to delete, and each gap open in or under the
package and where it was raised; end with
`🏁 Complete. Let me know if anything needs adjustment.`
If archival fails after Base review, report the base promoted, archival incomplete, use the standard
blocked gate and resume only archival.

## Project Addendum

If `<active-project-root>/skai/addenda/design-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
