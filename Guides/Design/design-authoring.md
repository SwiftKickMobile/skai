Managed-By: skai
Managed-Id: guide.design-authoring
Managed-Source: Guides/Design/design-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-12

# Design Authoring

Before using this guide, complete [Project addendum](#project-addendum) loading below.

## Purpose

Take a design change from an idea to approved mockups in a **change package**: settle the decisions
it raises with the supervisor, draw it on a change page in the design file, and leave the package
ready to promote.

Authoring edits the change page and the package; the production designs stay unchanged. This guide
is tool-agnostic. The conventions the designs must meet live in the design tool's own guide: load
[`figma-designer-guide.md`](figma-designer-guide.md) for Figma. The project README's link to the
design file says which tool it is. Read the tool guide before drawing anything.

The input is whatever the supervisor brings: an idea, sketches, a product brief, a requirements
package, screenshots of an existing app. Nothing else is required.

## The change package

A package lives at `skai/changes/<change-id>/design/` and holds:

| Path | What it is |
| --- | --- |
| `design-authoring.md` | this workflow's artifact |
| `design-promotion.md` | promotion's artifact; may be absent |

The drafts themselves live in the design file, on a **change page** named `<change-id>`. Every
design tool SKAI supports has named pages; the tool guide says what a page is in its tool. Other
types for the same change (`requirements/`, `ui-map/`) sit beside `design/` under the same
`<change-id>`; promotion archives each type independently to `skai/promoted/<change-id>/<type>/`.

If the change ID is clear from the input, use it. If not, do not create the artifact yet: propose a
short kebab-case default and stop at the blocked gate rather than guessing. Once the ID is resolved,
create the artifact, then write `## Goal` and `## Inputs` before anything else.

### Artifact skeleton

```
# Design — <name>
## Goal                   one or two sentences; no motivation essay
## Inputs                 the sources this artifact was drafted from
## Discussion             the open questions and resolved decisions
## Design Changes         the inventory of screens, written after approval
## Assumptions and TODOs  what the designs assume; gaps that need no decision; may be empty
## Out of scope           boundaries this package deliberately doesn't address; may be empty
```

## Phases

Authoring alternates between two phases and never runs both at once:

1. **Discussion.** Items are raised and resolved. Nothing is drawn.
2. **Mockups.** The agent draws or adjusts on the change page; the supervisor reviews the designs.

The mockup is new work to review, so it arrives only once the supervisor has finished considering
proposals. Feedback on mockups goes into the designs, except what needs a recorded decision, which
is parked and opens the next discussion phase (the sequence is under *Mockups*). The phases
alternate until the supervisor approves the mockups.

Don't mock up to answer what discussion can settle; don't discuss what a mockup settles faster.

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
- The Discussion gate uses the canonical discussion-phase behavior: while any `- [ ]` item remains
  in `## Discussion`, every response ends with the blocked gate citing the remaining count; the
  moment every item is resolved — or the phase produced none — the agent emits the planned gate
  that advances to Mockups.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Mockups.`
  - Planned: `⏳ GATE: Next: Discussion complete. Say "next" to draw the mockups on <change-id>.`
- The Mockup review gate is non-standard. The supervisor reviews the change page, not the artifact.
  Feedback is handled in the sequence under *Mockups*: the round ends either back at this gate or
  at the Discussion gate with the parked items; the word "approved" advances to Design Changes.
  - `⏳ GATE: Next: Review the mockups on <change-id>. Say "approved" to write Design Changes, or give feedback.`

Planned gates for this workflow:
- After every Discussion item is resolved, before anything is drawn.
- After each mockup round, before Design Changes are written.

Workflow-specific blocked gates:
- The change ID cannot be determined from the input, so the package has no path yet.
- The design file cannot be found: the project README's resources table does not link it (see the
  tool guide, *Where the file is listed*).
- The tool cannot do what a draft needs (a font it cannot load, a library it is not subscribed to).
  The tool guide names these; the resolution is the supervisor's, never a workaround.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestones in this workflow: `discussion complete`, `mockup review`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the supervisor gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns exactly one marker: the `- [ ] D<n>` items
in `## Discussion`. Each is resolved individually, on the supervisor's explicit approval of *that
item*, by checking its box and appending `- **Decision** <resolution>.` Advance intent at the
Discussion gate does not clear them; by the time that gate is reached they are already clear.
`## Design Changes` entries carry no checkbox; the designs on the change page are the change.

**Workflow-specific `auto` behavior.** `auto` never bypasses the Discussion blocked gate (unresolved
items are supervisor decisions) and never bypasses the Mockup review gate: mockups are reviewed by
looking at them, and nothing substitutes for that.

## Initiation

The workflow starts on an explicit signal — "design X", "mock up X", "backfill the designs", or
equivalent. Whatever came before is context the agent digests.

On the signal:

1. Read the tool guide and find the design file through the project README.
2. Scan `skai/changes/*/design/design-authoring.md`. If an unpromoted package for this work exists,
   reopen it rather than creating a second; a package under `skai/promoted/` is closed.
3. Otherwise resolve the change ID, create the artifact, and record `## Goal` and `## Inputs`.
4. Open the first Discussion phase.

A package whose promotion completed (see `design-promotion.md`) is closed; new work on the same
subject opens a new package. On reopen, resolved decisions are never disturbed: a resolved
`- [x] D<n>` is not removed, rewritten, or renumbered; new items continue the numbering. A reopen
that changes the designs removes `## Design Changes`, since it recorded an approval that no longer
covers them; it is rewritten after the next approval.

**A backfill** (designs drawn from an existing app) is a change like any other: it goes through a
change page, and its items are the deviations from the app and the suspected defects the agent
finds. The tool guide's *Working a backfill* says what to draw.

## Discussion

`## Discussion` holds the decisions this package needs from the supervisor. Topics are `###`
subsections with their items inline. Do not create aggregator sections (`## Questions`,
`## Open Items`) that pull items out of their topics.

Item line: `- [ ] D<n> [Kind] <summary>`, where `[Kind]` is `[Question]`, `[Proposal]`, or
`[Tradeoff]`. Sub-bullet labels are bold with no separator: **Concern** (always), **Proposal**,
**Question**, **Options**, **Detail**, **Why**, and **Decision** on resolution.

**Every item carries a recommendation**, in words. Nothing is drawn to make a proposal; the mockup
phase applies the decisions. An item that can only be judged visually says so, and the supervisor
resolves it by approving the recommended option as a trial (`- **Decision** Try it; judge in the
mockup.`); the mockup then shows it, and feedback on the mockup settles it.

### What earns an item

An item is a decision the agent needs from the supervisor: a departure from the current app or an
existing design that the agent proposes, behavior that looks like a defect ("the app does X, which
looks like a defect; the design will show Y"), a product question the inputs leave open, a scope
call that could go either way. Design iteration itself (layout, spacing, copy, the look) is
informal, in the file and in conversation, and earns no items. A change the supervisor asks for
during a mockup review needs no item; the design is the record.

If a phase produces no items, leave `## Discussion` as one plain paragraph: "The listed Inputs
determine the designs; review them on `<change-id>`." Omit that sentence whenever the section holds
any item.

**Example** (LumenNotes):

```markdown
### Pinned notes

- [ ] D1 [Proposal] Pinned notes sit in their own group above the list
  - **Concern** The brief says "pinned notes are easy to find" but not where they go. The current
    app sorts them first with a pin glyph, which is easy to miss.
  - **Proposal** A `Pinned` group with its own header above the rest of the list.
  - **Why** It matches how notes apps users already know do it, and the header makes the state
    visible without a glyph.

- [ ] D2 [Proposal] The empty-list illustration is cut off at the top — a defect, not a design
  - **Concern** On the current app the illustration's top 12px are clipped by the header.
  - **Proposal** Draw it whole.
  - **Why** The source illustration is complete; nothing suggests the crop is intended.
```

### Resolution

On the supervisor's explicit approval of an item: check the box and append
`- **Decision** <resolution>.` as the last sub-bullet. The original stays visible — the decision is
appended, never substituted.

## Mockups

When the Discussion gate advances, draw the whole change on the change page: everything the Goal
and Inputs call for, as the decisions and any later feedback currently stand. A decision that
feedback has since changed is history, not an instruction; Discussion holds decisions, not the
scope. Follow the tool guide's conventions throughout, then stop at the Mockup review gate.

On feedback, in this order: apply everything that needs no further decision; park what does, as
new Discussion items, together with any drawing that depends on their answers; then, if nothing was
parked, re-emit the Mockup review gate, otherwise end at the Discussion gate (blocked). On
"approved", write Design Changes.

## Design Changes

Written after approval, and it records that approval: promotion takes its presence as evidence
the mockups were approved. An inventory, not a specification: one line per screen the package adds
or changes, with a link to its draft on the change page, from which promotion knows what
production must absorb.

```markdown
## Design Changes

- `notes` — changed: pinned group above the list ([draft](<link>))
- `notes — empty` — changed: illustration drawn whole ([draft](<link>))
- `note editor — pin menu` — new ([draft](<link>))
```

After writing the section, bring `## Assumptions and TODOs` and `## Out of scope` up to date, and
the package is ready to promote. End with `🏁 Complete. Let me know if anything needs adjustment.`
Promotion is invoked separately.

## Artifact maintenance

Through every phase, update the artifact before speaking: revise `design-authoring.md`, then end
the response at whichever gate *Gates* prescribes. Do not describe intended changes without applying
them.

## Cross-references

- The tool guide for the project's design tool ([`figma-designer-guide.md`](figma-designer-guide.md)
  for Figma) — the conventions the designs must meet
- [`design-promotion.md`](design-promotion.md) — promoting an approved package

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/%s-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Before work, report
`📎 ADDENDUM: <project-entry filename> — loaded` or `No project addendum found: <project-entry filename>.`
Report only the project entry, not each referenced document. Receipt is not a gate; keep GATE lines last.
