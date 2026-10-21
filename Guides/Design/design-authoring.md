Managed-By: skai
Managed-Id: guide.design-authoring
Managed-Source: Guides/Design/design-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-20

# Design Authoring

Print `📖 SKAI guide: design-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Take a design change from an idea to approved mockups in a **change package**: settle the decisions
it raises with the supervisor, draw it on a change page in the design file, and leave the package
ready to promote.

Authoring edits the change page and the package; the production designs stay unchanged, and so does
the change's product spec package: a decision that changes what the product promises is filed as a
change request against it (*Resolution*). The conventions the designs must meet live in the design
tool's own guide: load [`figma-designer-guide.md`](figma-designer-guide.md) for Figma.

## The change package

A package lives at `skai/changes/<change-id>/design/` and holds:

| Path | What it is |
| --- | --- |
| `design-authoring.md` | this workflow's artifact |
| `design-promotion.md` | promotion's artifact; may be absent |
| `evidence/` | check output promotion persisted; may be absent |

The drafts themselves live in the design file, on a **change page** named `<change-id>`; the tool
guide says what a page is in its tool. Other types for the same change share its `<change-id>` and
update freely while the change is open; promotion archives each type independently to
`skai/promoted/<change-id>/<type>/`.

Use the input's change ID; otherwise propose a short kebab-case default and block before
creating the artifact. Once the ID is resolved, create the artifact, then write `## Goal` and
`## Inputs` before anything else.

### Artifact skeleton

```
# Design — <name>
## Goal                   one or two sentences; no motivation essay
## Inputs                 draft sources
## Discussion             open questions and decisions
## Design Changes         the inventory of screens, written after approval
## Assumptions and TODOs  what the designs assume; notes needing no decision; filed requests
## Out of scope           excluded work; may be empty
## Decision Log
```

## Phases

Authoring alternates between two phases, never both at once:

1. **Discussion.** Items are raised and resolved. Nothing is drawn.
2. **Mockups.** The agent draws or adjusts on the change page; the supervisor reviews the designs.

Feedback on mockups follows the sequence under *Mockups*: into the designs, or parked as the next
discussion phase. The phases alternate until the supervisor approves the mockups.

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
- The Discussion gate uses the canonical discussion-phase behavior: while any non-gap `- [ ]` item remains
  in `## Discussion`, every response ends with the blocked gate citing the remaining count; the
  moment every non-gap item is resolved — or the phase produced none — the agent emits the planned gate
  that advances to Mockups.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Mockups.`
  - Planned: `⏳ GATE: Next: Discussion complete<; N open gaps carried>. Say "next" to draw the mockups on <change-id>.`
- The Mockup review gate is non-standard. The supervisor reviews the change page, not the artifact;
  the trace pass under *Mockups* runs before the gate is emitted. Feedback follows the sequence
  under *Mockups*; the word "approved" advances to Design Changes.
  - `⏳ GATE: Next: Review the mockups on <change-id>. Say "approved" to write Design Changes, or give feedback.`

Planned gates for this workflow:
- After every non-gap Discussion item is resolved, before anything is drawn.
- After each mockup round, before Design Changes are written.

Workflow-specific blocked gates:
- The change ID cannot be determined from the input, so the package has no path yet.
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
Discussion gate does not clear them; by the time that gate is reached they are already clear. Gaps stay unchecked; they block promotion.
`## Design Changes` entries carry no checkbox; the designs on the change page are the change.

**Workflow-specific `auto` behavior.** `auto` never bypasses the Discussion blocked gate (unresolved
items are supervisor decisions) and never bypasses the Mockup review gate: mockups are reviewed by
looking at them.

## Initiation

The workflow starts on an explicit signal — "design X", "mock up X", "backfill the designs".
Whatever came before is context the agent digests.

On the signal:

1. Read the tool guide.
2. If a package for this work is named or in context and promotion has not taken it up — no
   `design-promotion.md`, or one that returned it to authoring — reopen it rather than creating a
   second. A package promotion holds is promotion's; a closed one opens a new package.
3. Otherwise resolve the change ID, create the artifact, and record `## Goal` and `## Inputs`.
4. Open the first Discussion phase.

On reopen, a resolved `- [x] D<n>` keeps its number, Concern, Options and Proposal; *Resolution*
governs its state; new items continue the numbering. A reopen that changes the designs
removes `## Design Changes` (its approval no longer covers them); it is rewritten after the next
approval.

**A backfill** (designs drawn from an existing app) is a change like any other; its items are the
deviations from the app and the suspected defects the agent finds, and the tool guide's *Working a
backfill* says what to draw.

## Discussion

`## Discussion` holds the decisions this package needs from the supervisor, grouped under `###`
topics, never in aggregator sections.

Item line: `- [ ] D<n> [Kind] <summary>`, where `[Kind]` is `[Question]`, `[Proposal]`, or
`[Tradeoff]`. Sub-bullet labels are bold with no separator: **Concern** (always), **Proposal**,
**Question**, **Options**, **Detail**, **Why**, **Gap** last for unchecked gaps (placeholder or "none; waiting on <what>"), and **Decision** on resolution.

A gap on an input you rely on, or an item of yours that cannot be resolved because something outside this work is not yet known, is handled per [`known-gaps.md`](../Core/known-gaps.md).

**Every item carries a recommendation**, in words. An item that can only be judged visually says
so, and the supervisor resolves it by approving the recommended option as a trial
(`- **Decision** Try it; judge in the mockup.`); the mockup then shows it, and feedback settles it.

### What earns an item

An item is a decision the agent needs from the supervisor: a departure from the current app or an
existing design that the agent proposes, behavior that looks like a defect, a product question the inputs leave open, a scope
call that could go either way. Design iteration (layout, spacing, copy, the look) earns no
items; a change the supervisor asks for during a mockup review needs no new item (one that changes
an existing decision updates it through *Resolution*); the design is the record.

With no items, leave `## Discussion` as: "The listed Inputs determine the designs; review them on
`<change-id>`." Omit it when items exist.

**Example** (LumenNotes):

```markdown
### Pinned notes

- [ ] D01 [Proposal] Pinned notes sit in their own group above the list
  - **Concern** The brief says "pinned notes are easy to find" but not where they go. The current
    app sorts them first with a pin glyph, which is easy to miss.
  - **Proposal** A `Pinned` group with its own header above the rest of the list.
  - **Why** It matches other notes apps, and the header makes the state visible without a glyph.
```

### Resolution

On the supervisor's explicit approval of an item: check the box and append
`- **Decision** <resolution>.` as the last sub-bullet; the original is kept. Remove a resolved item nothing current cites or needs. For gaps, remove **Gap**; Decision says answered, placeholder adopted, or omitted. At most one Decision: replace it and log `decided` on change; only withdrawal without replacement reopens (remove Decision, uncheck, log `reopened`). End with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>` per state change; keep entries after item removal.

A decision that changes or adds a product spec is filed as a **change request** against the
change's open product spec package (with none, one is opened through its authoring), in the form of
[`product-specs-artifacts.md` § Change Requests](../ProductSpecs/product-specs-artifacts.md#change-requests),
with drafts as that section says; the designer never edits that package. This holds in any phase,
and every request the package filed stays listed under `## Assumptions and TODOs`, with its
status, through promotion; a Decision that produced one names it.

## Mockups

When the Discussion gate advances, draw the whole change on the change page: everything the Goal
and Inputs call for, as the decisions and any later feedback currently stand. A decision feedback has
changed is updated through *Resolution*, its old outcome in the log; Discussion holds decisions,
not the scope. Follow the tool guide's conventions throughout.

Before the Mockup review gate, run the **trace pass** over the change page: every drawn state
traces to a product spec, in the catalog or the change's package, and every spec in that package is
served by a drawing or recorded under `## Out of scope`. A mismatch either way is a change request, filed
as under *Resolution*. Then stop at the Mockup review gate.

On feedback, in this order: apply everything that needs no further decision; park what does, as
new Discussion items, together with any drawing that depends on their answers; then, if nothing was
parked, run the trace pass and re-emit the Mockup review gate, otherwise end at the Discussion gate. On
"approved", write Design Changes.

## Design Changes

Written after approval, and it records that approval: promotion takes its presence as evidence
the mockups were approved. An inventory, not a specification: one line per screen the package adds
or changes, linking its draft on the change page.

```markdown
## Design Changes

- `notes` — changed: pinned group above the list ([draft](<link>))
- `note editor — pin menu` — new ([draft](<link>))
```

Then bring `## Assumptions and TODOs` and `## Out of scope` up to date and end with
`🏁 Complete. Let me know if anything needs adjustment.` Promotion is invoked separately; name any
change request still `Proposed`.

## Artifact maintenance

Through every phase, update `design-authoring.md` before speaking and end the response at
whichever gate *Gates* prescribes. Apply changes, never merely describe them.

## Project Addendum

If `<active-project-root>/skai/addenda/design-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
