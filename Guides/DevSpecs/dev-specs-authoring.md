Managed-By: skai
Managed-Id: guide.dev-specs-authoring
Managed-Source: Guides/DevSpecs/dev-specs-authoring.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-31

# Dev Specs Authoring

Print `📖 SKAI guide: dev-specs-authoring` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Turn open-ended input into an approved technical design for a software change, reviewed mainly as
an API diff with only needed supporting material.

This skill owns the design; [`dev-specs-implementation.md`](dev-specs-implementation.md) owns task lists and code changes. Continue there or hand the completed design to another developer.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## Inputs and initiation

Start when the supervisor asks to design or author a dev spec. Input may be conversation, design,
tickets, requirements, specifications, source code, or any combination. There is no intake form or declared mode.

Read the supplied material and inspect the repository for current architecture and conventions.
Read `skai/integration.md` and applicable canonical requirements when present. Do not ask the
supervisor for facts the inputs or repository provide. Infer the spec name from context when possible;
if no stable artifact identity can be proposed, stop at a blocked gate before creating it.

Choose a concise `<spec-name>` and create:

```text
skai/working-docs/<spec-name>/<spec-name>-design.md
```

`<spec-name>` is the [working-doc](../Core/working-doc-conventions.md) session folder.
Record durable paths or links in `## Inputs`. Restate conversation-only facts under Goal, Current
Architecture and Constraints, or the relevant `D#`; do not require a transcript or depend on hidden chat history.

Reopen an existing named design in place—including for new implementation evidence or a later slice—
following *Returning to Discussion*.

## Authoring artifact

Use this order:

```text
# <Change> Design
## Goal
## Inputs
## Current Architecture and Constraints     when useful
## Discussion
## API Sketch
## <additional review sections>             only when useful
## Implementation Design                    written after API approval
## Assumptions and TODOs                     when present
## Non-goals                                 when present
## Delivery Slices                           only when activated
## Decision Log
```

Completed designs always include Goal, Inputs, Discussion, API Sketch, Implementation Design and
Decision Log with those exact headings and no status text. Omit `## Implementation Design` before
the first gate; its presence proves the gate advanced. When no detail is needed, write:
`No additional implementation design is needed beyond the
approved API and decisions.` Omit other empty boilerplate. A long document may have a table of contents.

Use the smallest reviewable form for each material decision. Supporting prose may cover use cases,
relevant data flow, ownership, dependencies, compatibility, migration, security, risks, or alternatives.
Separate artifacts require independent structure or ownership by another workflow.

### Readiness for implementation planning

The design is ready when:

- `## Discussion` has no unchecked non-gap items.
- `## API Sketch` is present.
- `## Implementation Design` is present.
- No assumption or TODO blocks implementation planning.
- Every required sibling architecture artifact is ready.

An assumption or TODO blocks if being wrong would change a resolved discussion decision (`D#`) or
the API Sketch; otherwise record a non-blocking note.

This structural screen is authoritative; do not add a mutable readiness status.

## Gates

While waiting on the supervisor, end every response with the active gate line verbatim until it
changes. Name the artifact path and what awaits review; for planned gates, state what approval does.
Do not invent intermediate gates. Completion is not a gate.

Unexpected blockers use:

`⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

While Discussion has open non-gap items, use:

`⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to approve the API sketch.`

When none remain, use this skill's only planned gate:

`⏳ GATE: Next: Discussion complete<; N open gaps carried>. Review the design decisions and API sketch, then say "next" to approve them and complete the design.`

The supervisor is an outside human or authorized agent who resolves this workflow's discussion items
and reviews its gates. The executing agent cannot resolve or approve its own. This guide prescribes
neither delegation nor escalation.

While an invoked sibling is active, only its gate is active; resume this skill after the sibling's
completion line.

## Advance intent and markers

Advance intent ("next", "continue", "go ahead", "do it") advances a planned gate only after that
gate is emitted. "We should" and "let's" are discussion. There is no `auto` mode.

At a blocked gate, the supervisor resolves the cause; the agent re-evaluates and emits the appropriate
gate on its next response. Bare advance intent while unresolved re-emits the blocked gate.

Discussion uses stable, never-renumbered `D#` checkboxes in tight topic lists. Only explicit supervisor
approval checks an item and appends its Decision. Advance intent at the planned gate authorizes
`## Implementation Design`.

"Approve all proposals" resolves every open non-gap item at its stated Proposal, including Tradeoffs and
Questions.

## Draft and discuss

Draft the first gate's review in one pass on initiation: the design through `## API Sketch` and any
additional review section, omitting only `## Implementation Design`. Fill unknowns with your best
proposal (exclude gaps with no placeholder) for a coherent, reviewable first draft. Update the
artifact before every Discussion response; do not merely describe intended edits.

### Discussion items

Organize Discussion by design topic, never by workflow category. Use:

```markdown
- [ ] D01 [Proposal] <summary; name the affected API or type when API-specific>
  - **Concern** <what requires review>
    - **Proposal** <recommended resolution>
  - **Why** <reason, then its source>
- [ ] D02 [Tradeoff] <summary>
  - **Concern** <what requires review>
  - **Options**
    - A — <option>
    - B — <option>
    - **Proposal** <recommended option and reason>
  - **Why** <reason, then its source>
```

If there are no items, `## Discussion` holds one sentence stating the change and the input fact that settles it; omit it when an item exists.

Keep gaps unchecked with `- **Gap** <the placeholder alone, or "no placeholder">` last.
A gap on an input you rely on, or an item of yours that cannot be resolved because something outside this work is not yet known, is handled per [`known-gaps.md`](../Core/known-gaps.md).

Use `[Question]` for the rare case with no defensible recommendation. Its `**Question**` names the needed input;
its `**Proposal**` states the provisional resolution used by the API Sketch, when there is one.
All other items are `[Proposal]` or `[Tradeoff]`.

Give a choice a discussion ID (`D#`) only when supervisor review has leverage: it creates a long-lived
contract, has broad impact, is costly to reverse, commits to an external system, or materially constrains
future work. Encode clear implications of inputs, project conventions, or existing architecture directly.
Answer supervisor questions directly; create a discussion item only for a material choice.

On explicit approval, preserve the item, check it, and append:

```markdown
  - **Decision** <succinct resolution>.
```

Never rewrite resolved items' Concern, Options or Proposal. Keep them only while
cited by current work or explaining the design. For gaps, remove **Gap**; Decision states the outcome in words and which it was: answered, placeholder adopted, or omitted. Keep
at most one Decision: replace it and log `decided` when it changes. Only withdrawal without replacement
reopens an item: remove Decision, uncheck, and log `reopened`. End with append-only `## Decision Log`:
`- <ID> decided|gap|reopened — <one line>` per state change. Retain entries after item removal.

If feedback changes the proposal, update the discussion and all affected design content before
responding. Add or split an item only when the new decision meets the same materiality bar.

### Returning to Discussion

Before reopening, read `## Implementation Design`, then remove it so readiness requires renewed approval.
Preserve resolved items still explaining the design. Change affected items through the transitions
under *Discussion items* (a new `D#` only for a new decision), update the API Sketch, and stop at the
Discussion gate. After approval, rewrite Implementation Design from approved decisions, API Sketch,
inputs, and repository.

### Example: dependency choice reflected in API

````markdown
### Image loading

- [ ] D01 [Tradeoff] Load note images through an image service or the app's own storage
  - **Concern** Note images need resizing and cropping before display, which the app's storage path
    cannot do; the designs show a thumbnail and a full-size view of the same image.
  - **Options**
    - A — Adopt the image service, behind an app-owned `ImageProviding` protocol.
    - B — Extend the app's storage path to resize and crop.
  - **Proposal** I recommend the image service: it already resizes and crops, and the protocol keeps the rest of
    the app from depending on it.
  - **Why** Writing resizing ourselves repeats what the service does well, and behind the protocol a later
    swap touches one type; its documentation (Inputs) lists both.

## API Sketch

```swift
protocol ImageProviding {
    ~~func image(for asset: ImageAsset) async -> AppImage?~~

    /// The asset's image, sized for display. Throws when it cannot be loaded; callers used to get nil.
    func image(for asset: ImageAsset) async throws -> AppImage
}

struct ServiceImageProvider: ImageProviding { }
```
````

Selecting a service or library is in scope when the design depends on it. Procurement, credentials,
contracts, and other external actions may become implementation handoffs.

## API Sketch

API means production-code definitions visible outside their immediate implementation scope, including
module-visible definitions and those exported outside a package or module. It excludes tests and
private or local implementation details. The sketch shows models and interaction surfaces between
types or components, without implementation bodies.

Apply this boundary to the initially supported languages:

- Swift and Kotlin: include non-private production declarations, including module-visible `internal`
  API.
- JavaScript and TypeScript: include exported module definitions and externally visible type or
  object members; omit file-local helpers.

Do not grow the guide into a universal language taxonomy.

Show every new, modified, or removed API implied by the design:

- Show members inside their enclosing type.
- Omit unchanged definitions.
- Show removed declarations with strikethrough.
- Show a modified declaration as the struck old declaration followed by the proposed declaration.
- Add documentation to new and modified API.
- Use language-tagged code fences.
- When a protocol or interface defines an API, show it once. On a conforming type, show conformance
  only; do not repeat the requirements. Show independently changed API on that type normally.

Explicitly state when no API changes are needed. Keep caller inventories, impact reports, and
implementation listings out of the sketch. Put material reasoning in the surrounding design and
mechanical impact in the implementation artifact.

## Complete the design

After the planned gate advances, write `## Implementation Design` with only what implementation
planning needs beyond approved decisions and API: component relationships, data flow, ownership,
dependency boundaries, migration, compatibility, security, or other material constraints as applicable.
Do not restate the API or give line-by-line implementation instructions.

If this exposes a material API or design problem, follow *Returning to Discussion*. Otherwise finish
without another approval.

## Related workflows

Invoke sibling workflows only when their owned artifact is needed:

- If the project has an official UI Map, invoke [`../UIMap/ui-map-architecture.md`](../UIMap/ui-map-architecture.md) for a new or changed scene, route, or domain. Without an official map, invoke it only after the supervisor approves a material discussion item (`D#`) adopting one; otherwise
  describe the UI design here. Its completed package becomes an input.
- If a product specs catalog omits existing shipping behavior this work needs, invoke [`../ProductSpecs/product-specs-authoring.md`](../ProductSpecs/product-specs-authoring.md). It owns the
  backfill package and gates. Run the backfill here only if an open discussion item (`D#`) or the current
  slice's API Sketch cannot be resolved without it. Otherwise record the need for separate supervisor
  orchestration and continue. Without a catalog, record missing behavior as an assumption. Planning
  new behavior does not automatically trigger product specs authoring.

Siblings own their artifacts and gates; link their results without duplicating them. Dev Specs Authoring
writes only its authoring artifact. Sibling packages, canonical requirements, and `skai/integration.md`
are read-only.

A required sibling may run after the initial API Sketch but before its gate, or later. On completion,
update the design and emit the appropriate Design gate. Do not create a discussion item (`D#`) merely
to invoke a sibling.

## Optional delivery slices

Normally omit delivery slicing. If scope exceeds one desirable implementation iteration, propose
the cut as a material discussion item (`D#`). After approval, add `## Delivery Slices` with one current slice
(its outcome and boundary) and brief bullets for later slices. Do not create empty future mini-plans.

The API Sketch covers the current slice and only future constraints needed to avoid an architectural
dead end. One design may produce several task lists over time, named `<spec-name>-<slice-name>-impl.md`
in the same session folder. Declare each slice's `-impl.md` path in Delivery Slices when it becomes
current, before implementation planning.

## Completion

Complete when the readiness screen passes. If the request was design-only, end with:

`🏁 Complete. The design is ready for implementation planning.`

If the request also asks for planning or implementation, immediately load [`dev-specs-implementation.md`](dev-specs-implementation.md) and continue without waiting at the skill boundary.

## Project Addendum

If `<active-project-root>/skai/addenda/dev-specs-authoring-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
