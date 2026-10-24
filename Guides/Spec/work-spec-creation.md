Managed-By: skai
Managed-Id: guide.work-spec-creation
Managed-Source: Guides/Spec/work-spec-creation.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-24

# Work Spec Design

Print `📖 SKAI guide: work-spec-creation` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Turn open-ended input into an approved technical design for a software change, reviewed mainly
as an API diff with only needed supporting material.

This skill owns the design; [`work-spec-implementation.md`](work-spec-implementation.md) owns
task lists and code changes. Continue there or hand the completed design to another developer.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## Inputs and initiation

Start when the supervisor asks to design or author a work spec. Input may be a conversation, design,
ticket, requirements, another specification, source code, or any combination. There is no intake form
or declared mode.

Digest the supplied material and inspect the repository for the current architecture and conventions.
Read `skai/integration.md` and applicable canonical requirements when they exist. Do not ask the
supervisor to restate facts the inputs or repository answer. Resolve the spec name from context when
possible; if no stable artifact identity can be proposed, stop at a blocked gate before creating it.

Choose a concise `<spec-name>` and create:

```text
skai/working-docs/<spec-name>/<spec-name>-design.md
```

`<spec-name>` is the [working-doc](../Core/working-doc-conventions.md) session folder.
Record durable paths or links in `## Inputs`. Restate facts supplied only in conversation under Goal,
Current Architecture and Constraints, or the relevant `D#`; do not require a transcript. Chat history
is never a hidden dependency.

When the named design already exists—because implementation returned new evidence or a later slice is
starting—reopen it in place using *Returning to Discussion* below.

## Design artifact

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

Goal, Inputs, Discussion, API Sketch, Implementation Design and Decision Log always appear in a completed design
with those exact headings and never carry status text. Before the first gate,
omit `## Implementation Design`; its presence proves the gate advanced. When no detail is
needed, write: `No additional implementation design is needed beyond the
approved API and decisions.` Do not emit other empty boilerplate. A table of contents is optional for
a long document.

Use the smallest reviewable form for each material decision. Supporting prose may cover use cases,
relevant data flow, ownership, dependencies, compatibility, migration, security, risks, or
alternatives. Use a separate artifact only when it has independent structure or another workflow
owns it.

### Readiness for implementation planning

The design is ready when:

- `## Discussion` has no unchecked non-gap items.
- `## API Sketch` is present.
- `## Implementation Design` is present.
- No assumption or TODO blocks implementation planning.
- Every required sibling architecture artifact is ready.

An assumption or TODO blocks when its being wrong would change a resolved `D#` or the API Sketch;
otherwise it is a recorded non-blocking note.

This structural screen is authoritative. Do not add a mutable readiness status.

## Gates

Whenever waiting on the supervisor, end with the active gate line and re-emit it verbatim on every
response until the gate changes. Name the artifact path and what awaits review; for a planned gate,
also state what approval does. Do not invent intermediate gates. Completion is not a gate.

Unexpected blockers use:

`⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

While Discussion has open non-gap items, use:

`⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to approve the API sketch.`

When none remain, use this skill's only planned gate:

`⏳ GATE: Next: Discussion complete<; N open gaps carried>. Review the design decisions and API sketch, then say "next" to approve them and complete the design.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion
items and reviews its gates; the executing agent does not resolve or approve its own. This guide
does not prescribe delegation or escalation.

While an invoked sibling is active, only its gate is active; resume this skill after the sibling's
completion line.

## Advance intent and markers

Advance intent ("next", "continue", "go ahead", "do it") advances a planned gate only after that
gate is emitted. "We should" and "let's" are discussion. There is no `auto` mode.

At a blocked gate, the supervisor resolves the cause; on the next response the agent re-evaluates and
emits the appropriate gate. Bare advance intent while unresolved re-emits the blocked gate.

Discussion uses stable, never-renumbered `D#` checkboxes in tight topic lists. Explicit supervisor
approval checks one item and appends its Decision, not advance intent. The planned gate appears
only after every non-gap item is checked, and advance intent there authorizes `## Implementation Design`.

"Approve all proposals" resolves every open non-gap item at its stated Proposal, including Tradeoffs and
Questions.

## Draft and discuss

On initiation, write everything the first gate must review in one pass: the design through
`## API Sketch` and any additional review section, omitting only `## Implementation Design`. Fill unknowns
with the agent's best proposal (a gap with no placeholder stays out) so the artifact is coherent
and reviewable from the first draft. Update
the artifact before every response during Discussion; do not merely describe intended edits.

### Discussion items

Organize Discussion by design topic, never by workflow category. Use:

```markdown
- [ ] D01 [Proposal] <summary; name the affected API or type when API-specific>
  - **Concern** <what requires review>
  - **Proposal** <recommended resolution>
  - **Why** <rationale>
- [ ] D02 [Tradeoff] <summary>
  - **Concern** <what requires review>
  - **Options**
    - A — <option>
    - B — <option>
  - **Proposal** <recommended option and reason>
  - **Why** <rationale>
```

If drafting produces no items, `## Discussion` contains one sentence: `The listed Inputs determine
the design; review the API Sketch as the proposed contract.` Omit that sentence whenever an item
exists.

Keep gaps unchecked with `- **Gap** <placeholder, or "no placeholder; waiting on <what>">` last. A gap on an input you rely on, or an item of yours that cannot be resolved because something outside this work is not yet known, is handled per [`known-gaps.md`](../Core/known-gaps.md).

`[Question]` is for the rare case with no defensible recommendation. Its item uses a
`**Question**` line to name the needed input and a `**Proposal**` line to state the provisional
resolution used by the API Sketch, or a **Gap** line when none exists. Every other item is a
`[Proposal]` or `[Tradeoff]`.

A choice earns a `D#` only when supervisor review has leverage: it creates a long-lived contract,
has broad blast radius, is costly to reverse, commits to an external system, or materially constrains
future work. Clear implications of the inputs, project conventions, or existing architecture are
encoded directly. Answer a supervisor question directly; make it a `D#` only when the answer is a material choice.

On explicit approval, preserve the item, check it, and append:

```markdown
  - **Decision** <succinct resolution>.
```

Never renumber resolved items or rewrite their Concern, Options or Proposal. Keep resolved items
only while cited by current work or explaining the design. For gaps, remove **Gap**; Decision says
answered, placeholder adopted, or omitted. At most one Decision: replace it and log `decided` on
change; only withdrawal without replacement reopens (remove Decision, uncheck, log `reopened`). End
with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>` per state change; keep
entries after item removal.

If feedback changes the proposal, update the discussion and every affected part of the design
before responding. Add or split an item only when the new decision meets
the same materiality bar. Keep IDs stable.

### Returning to Discussion

Before reopening, read `## Implementation Design`, then remove it so readiness cannot pass before
renewed approval. Preserve resolved items still explaining the design; change an affected item through the transitions under *Discussion items* (a new `D#` only for a new decision),
update the API Sketch, and stop at the Discussion gate. After approval, rewrite Implementation Design,
deriving it from the approved decisions, API Sketch, inputs, and repository.

### Example: dependency choice reflected in API

````markdown
### Image loading

- [ ] D01 [Tradeoff] Implement `ImageProviding` with an image service or existing storage
  - **Concern** The feature needs transformations the current path does not provide.
  - **Options**
    - A — Adopt the service.
    - B — Extend the current path.
  - **Proposal** A, isolated behind an app-owned protocol.
  - **Why** It supplies the required transformation while containing vendor coupling.

## API Sketch

```swift
protocol ImageProviding {
    ~~func image(for asset: ImageAsset) async -> AppImage?~~

    /// Returns a display-ready image for the requested asset.
    func image(for asset: ImageAsset) async throws -> AppImage
}

struct ServiceImageProvider: ImageProviding { }
```
````

Selecting a service or library is in scope when the design depends on it. Procurement, credentials,
contracts, and other external actions may become implementation handoffs.

## API Sketch

API means production-code definitions visible outside their immediate implementation scope. It
includes module-visible definitions, not only definitions exported outside a package or module. It
excludes tests and private or local implementation details. The sketch records models and surfaces
through which types or components interact without exposing implementation bodies.

Apply that boundary directly for the initially supported languages:

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

If no API changes are needed, say so explicitly. Do not turn the sketch into a caller inventory,
impact report, or implementation listing. Put material reasoning in the surrounding design and
mechanical impact in the work spec.

## Complete the design

After the planned gate advances, write `## Implementation Design`. Add only what implementation
planning needs beyond the approved decisions and API: component relationships, data flow, ownership,
dependency boundaries, migration, compatibility, security, or other material constraints as
applicable. Do not restate the API or create line-by-line implementation instructions.

If this work exposes a material API or design problem, follow *Returning to Discussion*. Otherwise
finish the design without another approval.

## Related workflows

Invoke sibling workflows only when their owned artifact is needed:

- When the project has an official UI Map, invoke
  [`../UIMap/ui-map-architecture.md`](../UIMap/ui-map-architecture.md) for a new or changed scene,
  route, or domain. If no official map exists, invoke the sibling only when the supervisor approves a
  material `D#` adopting one; otherwise describe the UI design in this document. Its completed package
  becomes an input.
- When the project has a product specs catalog, invoke
  [`../ProductSpecs/product-specs-authoring.md`](../ProductSpecs/product-specs-authoring.md) if existing
  shipping behavior needed by this work is absent. It owns the backfill package and its gates. The
  backfill runs here only when an open `D#` or the current slice's API Sketch cannot be resolved
  without it. Otherwise record the need for separate supervisor orchestration and continue. If the
  project keeps no catalog, record the missing behavior as an assumption. New behavior being planned
  does not automatically trigger product specs authoring.

Siblings keep their artifacts and gates; link their results instead of duplicating them. Work Spec
Design writes only its design document and treats sibling packages, canonical requirements, and
`skai/integration.md` as read-only.

A required sibling may run after the initial API Sketch is written but before its gate, or later.
After it completes, update the design and emit the appropriate Design gate. Do not create a `D#`
merely to invoke a sibling.

## Optional delivery slices

Omit delivery slicing in the normal case. If scope grows beyond one desirable implementation
iteration, propose the cut as a material `D#`. After approval, add `## Delivery Slices` with one
current slice—its outcome and boundary—and brief bullets for later slices. Do not create empty
mini-plans for future work.

The API Sketch covers the current slice plus only future-facing constraints needed to avoid an
architectural dead end. One design may produce several work specs over time. Name them
`<spec-name>-<slice-name>-impl.md` in the same session folder. When a slice becomes current, declare
its work-spec path in Delivery Slices before implementation planning begins.

## Completion

Complete when the readiness screen passes. If the request was design-only, end with:

`🏁 Complete. The work-spec design is ready for implementation planning.`

If the initiating request also includes a work spec or implementation, load
[`work-spec-implementation.md`](work-spec-implementation.md) immediately and continue there without
waiting at the skill boundary.

## Project Addendum

If `<active-project-root>/skai/addenda/work-spec-creation-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
