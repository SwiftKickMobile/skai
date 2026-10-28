Managed-By: skai
Managed-Id: guide.design-authoring
Managed-Source: Guides/Design/design-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-28

# Design Authoring

Print `📖 SKAI guide: design-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Settle decisions with the supervisor; draw and list a **change package** against a **base** per
[`change-requests.md`](../Core/change-requests.md), ready for [`design-promotion.md`](design-promotion.md).

Edit only the package and drawings; carry input changes at *Completion*. For Figma, load [`figma-designer-guide.md`](figma-designer-guide.md).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## The change package

Against production: `skai/changes/<change-id>/design/`. Contents:

| Path | What it is |
| --- | --- |
| `design-authoring.md` | this workflow's artifact |
| `design-review.html` | supervisor's rendered page |
| `design-promotion.md` | promotion's artifact; may be absent |
| `evidence/` | promotion's check output; may be absent |
| `working-docs/` | working documents |

Draw against production on the **change page** the tool guide names; requests use a **request section**
`CR-<nnn> — <name>` on the base's page for additions and changes only. Change screens on copies of
base frames, never in place. Other types for the same change share its `<change-id>` and
update freely; promotion archives each type independently.

Use the input's change ID; otherwise propose a short kebab-case default and block before creation.

### Artifact skeleton

```
# Design — <name>
[Review page](design-review.html)
## Goal                   one or two sentences; no motivation essay
## Inputs                 draft sources; base first for requests
## Discussion             open questions and decisions
## Design Changes         live typed change list
## Assumptions and TODOs  what the designs assume; notes needing no decision; filed requests
## Out of scope           excluded work; may be empty
## Decision Log
```

## Phases

Authoring alternates between two phases, never both at once:

1. **Discussion.** Items are raised and resolved. Nothing is drawn.
2. **Mockups.** The agent draws or adjusts in the design file; the supervisor reviews the designs.
   If the supervisor, asked at the tool-access blocked gate, rules no mockups can be drawn,
   record it under `## Assumptions and TODOs`; nothing is drawn, and the Design Changes list
   stands in for the drawings below.

The phases alternate until the supervisor advances the
Review gate.

## Gates

Core rule: every time the agent is waiting on the supervisor, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion items and reviews its gates; the executing agent does not resolve or approve its own.

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

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
  for Mockups (Design Changes with no mockups).
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Mockups.`
  - Planned: `⏳ GATE: Next: Discussion complete<; N open gaps carried>. Say "next" to draw the mockups on <page or section> (with no mockups: to write Design Changes).`
- After the trace pass, Review covers drawings and rendered Design Changes (list alone with no
  mockups). Feedback follows *Mockups*; the supervisor's `next` approves and runs *Completion*.
  - `⏳ GATE: Next: Reconcile the inputs and complete <package>. Say "next" or what to change.`

Planned gates for this workflow:
- After every non-gap Discussion item is resolved, before anything is drawn.
- After each drawing round (or Design Changes with no mockups), before reconciling inputs.

Workflow-specific blocked gates:
- The change ID cannot be determined from the input, so the package has no path yet.
- The tool cannot do what a draft needs (a font it cannot load, a library it is not subscribed to,
  no write access). The tool guide names these; the resolution is the supervisor's, never a workaround.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestones in this workflow: `discussion complete`, `review`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the supervisor gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns the `- [ ] D<n>` items
in `## Discussion`. Each is resolved individually, on the supervisor's explicit approval of *that
item*, by checking its box and appending `- **Decision** <resolution>.` Advance intent at the
Discussion gate does not clear them; by the time that gate is reached they are already clear. Gap items stay unchecked; all open gaps block promotion into production.
`## Design Changes` has no checkboxes; the drawings, or the list with no mockups, are the change.

**Workflow-specific `auto` behavior.** `auto` never bypasses the Discussion blocked gate (unresolved
items are supervisor decisions) or Review: the supervisor inspects the drawings or list.

## Initiation

The workflow starts on an explicit signal — "design X", "mock up X", "backfill the designs",
"request a design change to <package>".

On the signal:

1. Read the tool guide.
2. Reopen a named or contextual package for this work if it has no `design-promotion.md` or was
   returned to authoring; promotion holds its packages, closed ones need new packages.
   A request signal follows the shared guide: reopen or create `<base>/change-requests/<nnn>/`.
3. Otherwise resolve the path, create the artifact, and record `## Goal` and `## Inputs`.
4. Open the first Discussion phase.

On reopen, a resolved `- [x] D<n>` keeps its number, Concern, Options and
Proposal; *Resolution* governs its state; new items continue the numbering.

**A backfill** (designs drawn from an existing app) is a change like any other; its items are the
deviations from the app and the suspected defects the agent finds, and the tool guide's *Working a
backfill* says what to draw.

## Discussion

`## Discussion` holds the decisions this package needs from the supervisor, grouped under `###`
topics, never in aggregator sections.

Item line: `- [ ] D<n> [Kind] <summary>`, where `[Kind]` is `[Question]`, `[Proposal]`, or
`[Tradeoff]`. Sub-bullet labels are bold with no separator: **Concern** (always), **Proposal**,
**Question**, **Options**, **Detail**, **Why**, **Gap** last for unchecked gaps (the placeholder alone, or "no placeholder"), and **Decision** on resolution.

A gap on an input you rely on, or an item of yours that cannot be resolved because something outside this work is not yet known, is handled per [`known-gaps.md`](../Core/known-gaps.md).
Mirror all gaps in the design file per the tool guide once placeholders are drawn; remove
mirrors when owning items close.

**Every item carries a recommendation**, in words. An item that can only be judged visually says
so, and the supervisor resolves it by approving the recommended option as a trial
(`- **Decision** Try it; judge in the mockup.`); the mockup then shows it, and feedback settles it.

### What earns an item

An item is a decision the agent needs from the supervisor: a departure from the base or an
existing design that the agent proposes, behavior that looks like a defect, a product question the inputs leave open, a scope
call that could go either way. Design iteration (layout, spacing, copy, the look) and changes the supervisor asks for at a review
need no new item; the design is the record. One that changes an existing decision replaces it and logs the change.

With no items, Discussion is one sentence saying which input settled the designs and where to review
them (`design-review.html` without mockups); omit it when items exist.

**Example** (LumenNotes):

```markdown
### Pinned notes

- [ ] D01 [Proposal] Pinned notes sit in their own group above the list
  - **Concern** The brief says "pinned notes are easy to find" but not where they go. The current
    app sorts them first with a pin glyph, which is easy to miss.
  - **Proposal** A `Pinned` group with its own header above the rest of the list.
  - **Why** It matches other notes apps, and the header shows the state without a glyph; the brief wants pinned notes easy to find.
```

### Resolution

On the supervisor's explicit approval of an item: check the box and append
`- **Decision** <resolution>.` as the last sub-bullet; the original is kept. Remove a resolved item nothing current cites or needs. For gaps, remove **Gap**; Decision states the outcome in words and which it was: answered, placeholder adopted, or omitted. At most one Decision: replace it and log `decided` on change; only withdrawal without replacement reopens (remove Decision, uncheck, log `reopened`). End with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>` per state change; keep entries after item removal.

A Decision that changes an input says so; *Completion* carries it.

## Mockups

When the Discussion gate advances, draw the whole change on its page or section: everything the
Goal and Inputs call for, as the decisions and any later feedback currently stand. A decision feedback has
changed is updated through *Resolution*, its old outcome in the log; Discussion holds decisions,
not the scope.

Before Review, with drawings, run the tool guide's structure check on the page or section and
fix findings; then run the **trace pass**: every drawn state traces to an input; everything inputs
ask of this change is drawn, or under `## Out of scope`. Mismatches become Discussion items or
input-changing Decisions for *Completion*; then end at the gate *Gates* prescribes.

On feedback, in this order: apply everything that needs no further decision; park what does, as
new Discussion items, together with any drawing that depends on their answers; then run the trace
pass and end at the gate *Gates* prescribes.

## Design Changes

Under `### <screen>` in canvas order (down a column, then across), one entry per frame: `- V<n> <add|modify|remove> <screen|state|component>: <identity>`.
Current from the first drawing; with no mockups, from decisions at the Discussion gate.

One sequence per package: `V01`, `V02`, …, never renumber or reuse. New frames take the next `V`
under their screen; new changes take their frame's next sub-ID. Identity: `add` and `modify` use
the frame name linked to its draft (`[name](<link>)`), or the intended name unlinked without mockups;
`remove` uses the base design's name, unlinked. Each entry has:
- **Description** the screen, state or component change in product words, never a visual diff or sample data; about a sentence with mockups; without them, enough to design from.
- **Justification** a reason sentence, then an input citation, `Resolved decision: D<n>` (this package), `Base decision: D<n>` (its base), or `Supervisor input`.

Inherited gaps get one footnote each, not items, on the first entry or sub-change whose change rests on its placeholder, never on what a frame merely keeps from the base; Placeholder is the provisional answer, not the frame ([`spec-file-gaps.md`](../Core/spec-file-gaps.md)).

Several changes: sub-IDs:

```markdown
### Notes

- V03 modify screen: [notes](<link>)
  - **01** A `Pinned` group with its own header above the list — pinned notes were easy to miss; Resolved decision: D01
  - **02** The unread dot on each row goes — unread notes come first, so the dot adds nothing; [NOTES-07]
```

## Completion

On Review's `next`, reconcile drawings against every input but the base; file against each the
decisions changed, with drafts, per the shared guide. Update
`## Assumptions and TODOs` and `## Out of scope`; name requests or needs, outcomes and downstream
work owed (design specs, say). End with
`🏁 Complete. Let me know if anything needs adjustment.` Invoke promotion separately.

## Artifact maintenance

Through every phase, update `design-authoring.md` before speaking. Apply changes, never merely
describe them. On every material change and before every gate, render `design-review.html`
beside it.

```
python3 <skai>/Bin/design-tool.py render --authoring <package>/design-authoring.md [--specs ROOT ...]
```

## Project Addendum

If `<active-project-root>/skai/addenda/design-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
