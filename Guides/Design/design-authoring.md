Managed-By: skai
Managed-Id: guide.design-authoring
Managed-Source: Guides/Design/design-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-18

# Design Authoring

Print `📖 SKAI guide: design-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Settle decisions with the supervisor; draw and list a **change package** against a **base** per
[`change-requests.md`](../Core/change-requests.md), ready for [`design-promotion.md`](design-promotion.md).

Edit only the package and drawings; carry input changes at *Completion*. For Figma, load [`figma-designer-guide.md`](figma-designer-guide.md).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## The change package

A change's own package, `skai/changes/<change-id>/design/`, uses a supplied change ID; else propose a
short kebab-case one and block before creation. Contents:

| Path | What it is |
| --- | --- |
| `design-authoring.md` | this workflow's artifact |
| `design-review.html` | supervisor's rendered page |
| `design-promotion.md` | promotion's artifact; may be absent |
| `evidence/` | promotion's check output; may be absent |
| `working-docs/` | working documents |

Draw against production on the **change page** the tool guide names; requests use the **request section**
it names, for additions and changes only. Change screens on copies of
base frames, never in place. A package that adds, changes, renames or removes a style, value or
component also follows [`design-system-changes.md`](design-system-changes.md). Other types for the same change share its `<change-id>` and
update freely; promotion archives each type independently.

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

Authoring alternates between two phases until Review advances. Before the first drawing round
they never overlap; after it, a decision is drawn as it is made (*Resolution*):

1. **Discussion.** Items are raised and resolved. No new frame is drawn.
2. **Mockups.** The agent draws or adjusts in the design file; the supervisor reviews the designs.
   If the supervisor, asked at the tool-access blocked gate, rules no mockups can be drawn,
   record it under `## Assumptions and TODOs`; nothing is drawn, and the Design Changes list
   stands in for the drawings below.

## Gates

Whenever you are waiting on the supervisor, end the message with a `⏳ GATE:` line. The one exception is workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion items and reviews its gates; the executing agent does not resolve or approve its own.

**Gate persistence.** After emitting a `⏳ GATE:` line, end every response, discussion and clarifications included, with that line verbatim until the gate moves. Change it only when its content changes (a blocker emerges, or `Next` needs revising), and then emit the new line in full. Never paraphrase, shorten or silently change it.

**No fabricated gates.** Use `⏳ GATE:` only for the gates this section defines. Never invent one for discussion state, partial completion or an intermediate review; a gate this guide lacks is a process improvement to file.

At a planned gate, summarize what you did and what happens next, end with the gate's line, then STOP and wait for the supervisor. This workflow has two:

- **Discussion**, before each Mockups round. While any non-gap `- [ ]` item remains in
  `## Discussion`, every response ends with the blocked line citing the remaining count; the
  moment every non-gap item is resolved, or the phase produced none, emit the planned line for
  Mockups (Design Changes with no mockups).
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Mockups.`
  - Planned: `⏳ GATE: Next: Discussion complete<; N open gaps carried>. Say "next" to draw the mockups on <page or section> (with no mockups: to write Design Changes).`
- **Review**, after each drawing round and its package check (or Design Changes with no mockups),
  before reconciling inputs. It covers drawings and rendered Design Changes (the list alone with
  no mockups); there, ask each changed input's route. Feedback follows *Mockups*; the supervisor's
  `next` approves and runs *Completion*.
  - `⏳ GATE: Next: Reconcile the inputs and complete <package>. Say "next" or what to change.`

An unexpected blocker takes `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.` and a STOP until the supervisor resolves it. This workflow's own blocked gates:
- The change ID cannot be determined from the input, so the package has no path yet.
- The tool cannot do what a draft needs (a font it cannot load, a library it is not subscribed to,
  no write access). The tool guide names these; the resolution is the supervisor's, never a workaround.

## Advance intent

Advance intent moves past the current gate: "next", "continue", "go ahead", "do it". It counts only after you have output a `⏳ GATE:` line; "we should...", "let's..." are discussion, NOT authorization. Outside a gate, read "begin"/"next"/"continue" by the active phase's rules below, and never use them to skip a phase.

`auto` bypasses planned gates only, and here never Review, where the supervisor inspects the drawings or list. It never bypasses a blocked gate, the Discussion one included: unresolved items are supervisor decisions. `auto to <milestone>` stops before the named gate: `discussion complete`, `review`.

**Markers.** This workflow owns the `- [ ] D<n>` items
in `## Discussion`. Each is resolved individually, on the supervisor's explicit approval of *that
item*, by checking its box and appending `- **Decision** <resolution>.` Advance intent at the
Discussion gate does not clear them; by the time that gate is reached they are already clear. Gap items stay unchecked; all open gaps block promotion into production.
`## Design Changes` has no checkboxes; the drawings, or the list with no mockups, are the change.

## Initiation

The workflow starts on an explicit signal — "design X", "mock up X", "backfill the designs" or
"request a design change to <package>". A fix that changes nothing visible needs no package: follow
`design-system-changes.md`.

On the signal:

1. Read the tool guide. Then read, from the design file, its recorded conventions, its app-wide
   designs, and what its component library and design system already hold (the tool guide says
   where each is); and any specs among the inputs, or linked by the project, that say how the
   app-wide designs apply. No such spec is required.
2. Per `change-requests.md`, settle whether work is a request; for one, reopen or create its `design/`
   sub-package, else reopen a named or contextual `design/` package or create one. Reopen only without
   `design-promotion.md` or when returned to authoring; promotion holds its packages, closed ones need
   new packages.
3. For any new package, resolve the path, create the artifact and record `## Goal` and `## Inputs`.
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

Once the package has mockups of its own,
apply each Decision to the affected frames, `## Design Changes` and gap mirrors before anything
else, in the same turn, and re-render.

## Design Practices

Follow these in everything drawn, a scratch Section included: what the supervisor keeps becomes
production. IDs are stable, never reused, and a retired practice keeps its line, marked retired,
so a review or a Description can cite one.

- **DP-01 Look before drawing.** Before drawing anything, check the component library, the styles
  and the values for something that fits. Where something nearly fits, add a variant or a property
  to it as a drafted change; never draw a lookalike.
- **DP-02 What recurs is defined once.** An element that recurs across screens (a card, a row, a
  header) is a component and each use an instance; a look that recurs (a separator, a field shape)
  lives in one component or value that screens inherit. Ordinary content that happens to repeat is
  not meant. The definition exists by Review. A fix is made to the definition, so every use gets it.
- **DP-03 A change to something shared is checked everywhere it is used.** Before changing a shared
  component, style or value, see where it is used; afterward, look for the old look surviving
  anywhere, the component library's own examples and other features' screens included.
- **DP-04 Content goes in through component properties.** A component has a property for what
  varies from one use to the next (a label, an icon, an optional part); screens set properties and
  never detach or restructure an instance.
- **DP-05 States live in the component; screens choose them.** A control's states and a recurring
  overlay's forms are variants in the library; a screen picks one and does not draw its own.

## Mockups

When the Discussion gate advances, draw each distinct change the Goal and Inputs call for, as
decisions and feedback currently stand, in the package's Section on its page, or its
request section. Draw each in as few frames as show it, normally one, cropped where the tool
guide's crop rule applies; its Description says where else it applies, and promotion carries it
there. Not every affected frame needs a drawing. Which states earn a frame, and
what is also drawn at each form factor, are the tool guide's rules.

A case an app-wide design already covers is not drawn again and needs no Discussion item: the
entry that relies on it, or `## Out of scope`, cites that design by name, and the case counts as
covered. A screen that departs from an app-wide design is an ordinary change, drawn and listed.
If coverage is unclear, raise a Discussion item.

A screen frame carries a purpose note where the tool guide calls for one, in the form it gives:
written when the frame is drawn and rewritten when what the frame is for changes. A Description says what changed;
the note says what the frame is for; the two never disagree.

Requested
exploration goes in a scratch Section (the tool guide's), outside the list and structure check; in
the same session, carry what the supervisor keeps into every affected package frame and list every
change. A decision feedback has
changed is updated through *Resolution*, its old outcome in the log; Discussion holds decisions,
not the scope.

Before Review, with drawings, run the tool guide's structure check on the page or section. Fix
each breach; look at each signal and judge it, and never fix one by rote. Then run the
**package check**:

- **Coverage.** Every drawn state traces to an input. Everything the inputs ask of this change is
  drawn once as above, covered by a cited app-wide design, or under `## Out of scope`. A repeated
  change drawn once and a case a cited app-wide design covers are not missing drawings.
- **Reuse.** The practices hold across the package's frames, and every design system change is
  listed, and drafted where it needs a draft.
- **Sample data.** Within a frame, what is shown could occur together (states, dates, counts,
  statuses, indicators). Across related frames, the same sample people and records agree. Against
  the inputs, what is shown follows them (ordering, grouping, what a state requires), and every
  indicator has what it indicates on screen. An edge case is drawn once, on the frame that is
  about it; frames showing the main case do not also show it. Each frame shows what its purpose
  note says it is for.

Fix each finding; where the inputs and a drawing disagree and the call is the supervisor's,
raise a Discussion item. If a non-gap item is open, return to Discussion; otherwise end at Review.

On feedback, in this order: apply everything that needs no further decision; park what does, as
new Discussion items, together with any drawing that depends on their answers; then run the
checks above again and route as above.

## Design Changes

Under `### <screen>` in canvas order (down a column, then across), one entry per frame: `- V<n> <add|modify|remove> <screen|state|component|style>: <identity>`. A design system change's entry follows `design-system-changes.md`.
Current from the first drawing; with no mockups, from decisions at the Discussion gate.

One sequence per package: `V01`, `V02`, …, never renumber or reuse. New frames take the next `V`
under their screen; new changes take their frame's next sub-ID. Identity: `add` and `modify` use
the frame name linked to its draft (`[name](<link>)`), or the intended name unlinked without mockups;
`remove` uses the base design's name, unlinked. Use these fields, or sub-IDs as below:
- **Description** what changed, in a reader's words, about a sentence with mockups (without them, enough to design from): name anything new without describing how it looks; no measurements, style names or sample data. State each change precisely so promotion finds and updates every affected frame. Added ✅ "An empty state for a notebook with no notes." Changed ❌ "The label is subordinate to the price." ✅ "On every offer card the label is smaller and gray, under the price." Removed ✅ "The unread-only notes state goes."
- **Justification** a reason sentence, then an input citation, `Resolved decision: D<n>` (another package's linked), or `Supervisor input`.

Only inherited gaps get footnotes, one each, not items, on the first entry or sub-change whose change rests on its placeholder, never on what a frame merely keeps from the base; Placeholder is the provisional answer, not the frame ([`spec-file-gaps.md`](../Core/spec-file-gaps.md)).

Several changes: sub-IDs:

```markdown
### Notes

- V03 modify screen: [notes](<link>)
  - **01** Pinned notes move into a group with its own header, above the list — pinned notes were easy to miss; Resolved decision: D01
  - **02** The unread dot goes from every row — unread notes come first, so the dot adds nothing; [NOTES-07]
```

## Completion

On Review's `next`, reconcile drawings against every input but the base; route each input the
decisions changed as the supervisor picked, with drafts, per `change-requests.md`. Update
`## Assumptions and TODOs` and `## Out of scope`; name requests or needs, outcomes and downstream
work owed (design specs, say). End with
`🏁 Complete. Let me know if anything needs adjustment.` Invoke promotion separately.

## Artifact maintenance

Once created, update `design-authoring.md` before speaking. Apply changes, never merely
describe them. On every material change and before every gate, render `design-review.html`
beside it.

```
python3 <skai>/Bin/design-tool.py render --authoring <package>/design-authoring.md [--specs ROOT ...]
```

## Project Addendum

If `<active-project-root>/skai/addenda/design-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
