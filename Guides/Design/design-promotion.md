Managed-By: skai
Managed-Id: guide.design-promotion
Managed-Source: Guides/Design/design-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-24

# Design Promotion

Print `📖 SKAI guide: design-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Move a completed package's changes into its **base** ([`design-authoring.md`](design-authoring.md)):
change page to production, or request section to parent package.
After supervisor confirmation, delete drafts and archive the package.

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
- At the non-standard Base review gate, the supervisor reviews the base's drawings, and any
  Design Changes folded in undrawn, before deletion. A requested design change blocks: restore the base from version history and return
  to authoring.
  - `⏳ GATE: Next: Review <production | the base's drawings and Design Changes>. Say "next" to confirm and delete <the change page | the request section> <name>, or what to change.`

Workflow-specific blocked gates:
- A readiness failure (conditions 1–3, or 5 when a ruling invalidates mockups), a `C1` or `C2`
  failure, or a design change the supervisor asks for at either gate: only authoring resolves them; each takes:
  `⏳ GATE: Blocked: <C1 | C2 | readiness condition | requested design change> — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- An existing promoted path (condition 4) or unruled request (condition 5) takes the standard
  blocked gate naming it; use the input's process for rulings.
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
left unchecked and nothing after it runs. `C5` and `C6` run only after the Base review gate
advances. An unfinished promotion (`C6` unchecked) continues from its pending check or gate, never
restarts. **A new run after an authoring return unchecks every check** and starts from `C1`; prior
evidence stays under `### Run <n>`.

**Workflow-specific `auto` behavior.** `auto` bypasses the Promotion Checks gate but never the
Base review gate: the supervisor looks at the base before the drafts are deleted.

## Initiation

Begin only on an explicit signal ("promote the designs"), never automatically after authoring.

Read the tool guide. The package is the one named or already in context; one already holding an
unfinished `design-promotion.md` continues (*Advance intent*), `C3` re-checking condition 5; the
readiness screen is for a new run.

### Readiness screen

Render the page, then verify before writing the checks:

1. All non-gap `- [ ]` items in `## Discussion` are resolved; into production, no open gap items
   or footnotes ([`known-gaps.md`](../Core/known-gaps.md)); into a package, `C3` carries both.
2. `## Design Changes` is current, Review advanced and inputs reconciled (authoring's *Completion*).
3. `add` and `modify` entries link drafts on the change page or request section, unless the
   no-mockups ruling under `## Assumptions and TODOs` leaves them unlinked; unlinked entries never
   enter production. `remove` entries name the base design.
4. The promoted path (*C6*) does not exist.
5. Requests filed against inputs (under `## Assumptions and TODOs`) have rulings from their
   processes. Apply them to the package: invalidation returns it to authoring; otherwise do
   nothing. Unruled requests block now and at the base write.

A failure is a blocked gate, recorded in `## Evidence` instead of a checks section.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

- `C1 Drafts meet the conventions` — with drawings, run and pass the tool guide's structure
  check; drafts follow the guide and, into production, mirror no gap. A script covers what it tests; inspect the rest.
- `C2 Inventory matches the drawings` — per section, each linked `## Design Changes` entry has a
  draft; every screen draft of this package has an entry.
- `C3 The base absorbs the package` — with condition 5 still met by current statuses, per entry:
  update changed screens in the base to match drafts, keeping identities; place new screens or
  states and integrate needed components per the tool guide; delete removed designs. Into
  production, the per-screen sections do not survive: every column is regrouped into
  `Production`'s feature areas.
  Designs outside the inventory change only by the placement and relocation the tool guide's
  rules need to absorb them. Into a package, fold screen sections into same-named base sections
  (create missing ones), and:
  - Append entries with footnotes (`base D04` becomes `D04`) to its `## Design Changes`: next `V`
    numbers, Descriptions kept, Justifications `Change request: <nnn> V<n>; <the entry's own>`. Undrawn entries stay unlinked
    and return the base to Mockups to draw them.
  - Append its own open gap items to the base's `## Discussion`: next `D` numbers, Gap lines and
    mirrors kept; log `gap`.
  - Name the promoted request in its `## Assumptions and TODOs`.
- `C4 Links point at the base` — repoint `add` and `modify` links, including appended entries,
  to the base's drawings; a `remove` entry keeps its name; re-render every page whose
  artifact changed, the promoting package's included.
- `C5 Delete the drafts` — after Base review advances, delete the change page or request section,
  where one exists.
- `C6 Archive the package` — move the folder intact with `working-docs/`, `change-requests/`
  and `promoted-change-requests/` if present: to `skai/promoted/<change-id>/design/` for production,
  leaving siblings and removing an empty `<change-id>` folder; to
  `<base>/promoted-change-requests/<nnn>/` for a package. Repair links into and inside the moved
  files, keeping targets; re-render the moved page, verify the move and check
  `C6` in the archived artifact.

**Excerpt** (at the Base review gate: `C1`–`C4` checked, `C5`–`C6` unchecked):

```markdown
## Evidence

[evidence: C2; inspection — 3 entries, 3 frames on `pinned-notes`, each entry links one frame; none extra]
```

## Evidence

One bracket per check:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Persist and link full failure output. An inspection names its subject precisely enough to repeat
it; silence is not a pass: name what was compared and found.

## Completion

With `C6` checked, the base holds the changes, drafts are gone and the package is archived.
Link its artifact, name what the base owes and gaps carried, and end with
`🏁 Complete. Let me know if anything needs adjustment.`
If archival fails after `C5`, report the base promoted but archival incomplete, use the standard
blocked gate and later resume only the archival.

## Project Addendum

If `<active-project-root>/skai/addenda/design-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
