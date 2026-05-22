# UI Map Planning

The planning method for the UI Map system. Companion to [`ui-map-guide.md`](ui-map-guide.md) (the YAML format) and the platform references. This guide carries the procedure *and* the skai control flow inline; on another host the control flow is rewritten while the reference docs are reused unchanged.

## Purpose

Planning produces a **plan document** for a change to a UI Map app — a new feature, an edit, or an audit-driven conformance pass. The plan document is the reviewable specification: it captures the design decisions and the concrete change list. The implementation skill consumes it.

The plan document carries *decisions* and a *change list* — nothing more. The map is the app's architecture; the rendered map is the review surface. Implementation detail beyond the typed changes does not belong here.

**Invariant — the map leads, code follows.** Between sessions, the map is the source of truth and code conforms to it. An audit's Discussion is the sanctioned exception: the moment when the map itself may be revised, based on what an audit surfaces.

Planning runs in two phases:

1. **Discussion** — resolve the genuine design decisions.
2. **Change list** — the determined, typed changes, plus the proposed `ui-map.yaml` and its render.

## The plan document

One document. Create it as a working document following `Guides/Core/working-doc-conventions.md` — session-name = `<name>`, no subpath; full path `working-docs/<branch-path>/<name>/<name>-plan.md`. Skeleton:

```
# UI Map Plan — <name>
## Goal          one or two sentences; no motivation essay
## Inputs        the sources this plan was built from
## Discussion    phase 1
## Change list   phase 2; fix-code + fix-map findings
## Deferrals     phase 2; approved defer findings with TODO pointers; may be empty
## Out of scope  scope boundaries the plan deliberately doesn't address; may be empty
```

## Gates and control flow

Gate lines:

- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

At a planned gate: summarize what you did, end with the gate line, STOP and wait. When planning finishes: `🏁 Complete. The plan document is ready for implementation. Say "implement the plan" (or invoke the UI Map implementation skill directly) to begin.`

**Planned gates** — emitted when ready to advance. `next` moves to the next phase.

- End of Phase 1 — emitted when every `- [ ]` item in Discussion has been resolved (`- [x]`).
- End of Phase 2 is *not* a planned gate — once the Change list + Deferrals + `ui-map.yaml` diff + render are in place, the agent declares completion directly (see the `🏁 Complete.` line above) and tells the human how to invoke implementation.

**Blocked gates** — emitted when the agent cannot advance. Common reasons:

- Phase 1 in progress: one or more `- [ ]` items remain unresolved.
- Inputs are too contradictory or incomplete to draft a phase.
- A Phase-1 decision proves unworkable when Phase-2 tries to realize it (kicks back to Phase 1) — e.g. the proposed map cannot be made valid without revisiting a decision.

The human resolves the cause (resolves items, fixes inputs, revises decisions); the agent re-evaluates and emits the appropriate gate on the next response.

**Advance intent** — moves past a planned gate. Signals: "next", "continue", "go ahead". Recognized only after a `⏳ GATE: Next:` line. "we should…" / "let's…" is discussion, NOT authorization.

**`auto`** — advance intent that bypasses *planned* gates only. It never bypasses a blocked gate.

Bright-line: if continuing correctly would require changing something already approved, that is an amendment, not a fix — STOP, state it, propose the amendment, get approval. Resolution may route back to a prior phase.

## Initiation

Planning starts on an explicit signal — "write the planning document" or equivalent. Whatever came before (a requirements set, a discussion, an audit or bug request) is context the agent digests; there is no declared mode.

On the signal: digest all available inputs, infer the situation — **new change** or **audit** — and draft Phase 1.

## Phase 1 — Discussion

The Discussion section is topic-organized. New-change drafting uses free-form prose with one section per concern; audits use a fixed structure (see Audit proposal example below). In new-change drafting, do NOT create workflow-shaped sections ("Questions", "Decisions") — each topic carries its own open items inline.

Open items are `- [ ]` lines tagged with a Kind:

- `- [ ] Question — …` — an open-ended ask.
- `- [ ] Proposal — …` — the agent suggests something; accept / reject / modify.
- `- [ ] Tradeoff — …` — two or more options; the human picks. When options have different implications per affected item, expand each option as a sub-list — one bullet per implication — so the human can give per-item feedback (e.g., "approve option B except keep X").

Place a marker on the specific content line that needs input — never on a heading, never as a roll-up on a parent. The marker count equals the number of real decisions.

**Drafting:**

- *New change* — summarize the Goal and Inputs, then seed the Discussion with proposals and open items for the genuine design decisions. The agent MUST seed proposals; the document is never a passive transcript. If the inputs fully specify the change, state "inputs fully specify the change — no open questions" and draft no items.
- *Audit* — run the requested conformance pass (see below), then draft each finding as its own `- [ ]` item under the appropriate `###` subsection: per finding, *concern + discrepancy + recommended resolution + brief why*. Each finding is approved (and checked off) individually. **Findings are deviations only**; conformant scenes are not enumerated. Findings state what changes and why; how to execute belongs to the implementation method. A finding's resolution has three directions: *fix code* (becomes a `conformance / <dimension>` entry in the Change list); *fix map* (a `modify`/`add` entry); or *defer* — for findings whose resolution implies real refactor or feature implementation outside the implementation skill's mechanical scope. A deferred finding ensures the map's `todos:` mechanism records the pending work (an existing TODO that already tracks it, or a new one added in this pass) and produces no Change list entry; approved defers populate the Phase 2 Deferrals section with a pointer to the TODO. **Project-wide topics** that cross-cut many findings (e.g., a repo-wide pattern, a missing project-convention doc section) may be raised as their own Discussion items before the per-scene findings. Use sparingly — only when keeping the decision inline would noise up multiple per-scene findings.

**Audit proposal example.** One finding per resolution direction:

```
### Map fixes

- [ ] A. `Foo` scene missing `implements` annotation
  - **Concern** Map under-models the scene.
  - **Discrepancy** `FooView(mode:)` renders two variants (`.bar`, `.baz`); the map's `foo` scene carries no `implements`.
  - **Resolution** Fix map — add `implements: [bar, baz]` to `foo`.
  - **Why** Brings the map in line with the actual scene contract.

### Code conformance

- [x] B. Route enums in standalone files
  - **Concern** File-layout deviates from the SwiftUI reference.
  - **Discrepancy** Every scene puts its route enums in dedicated `*Route.swift` files instead of at the top of `*ViewModel.swift`.
  - **Resolution** Fix code — inline each route enum into its owning view-model file; delete the standalone `*Route.swift` files.
  - **Why** Guide convention; the enum belongs next to the view model that owns it.
  - **Decision** Fix code as proposed.

### Defers

- [ ] C. `Login → Verify` nav implementation absent
  - **Concern** Map-defined route has no code.
  - **Discrepancy** Map has `login.nav → verify`; code has no `VerifyView`.
  - **Resolution** Defer — tracked by the existing `verify: { todo: true }` entry. Real feature implementation, outside this skill's mechanical scope.
  - **Why** The implementation skill is mechanical; feature work belongs to a separate work spec.
```

Each finding is its own `- [ ]` item under the appropriate `###` subsection. Title is plain text with a letter prefix (`A.`, `B.`, etc.) — no bold on the title itself. Subsections: `Map fixes`, `Code conformance`, `Defers` — in that order; omit any with no findings. Letter prefixes are continuous across subsections (no per-group reset). On approval, check the box and append a `- **Decision** <succinct resolution>.` line as the last sub-bullet (see finding B). Defers cite the existing TODO in the Resolution; approved defers also populate the Phase 2 Deferrals section.

After drafting, STOP with a Blocked gate citing the open items:

`⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to the Change list.`

After each subsequent response, emit a Blocked gate (if `- [ ]` items remain) or a Planned gate (if every item is `- [x]`):

`⏳ GATE: Next: All Discussion items resolved. Say "next" to advance to the Change list.`

**Discussion loop:** the agent proposes, the human refines or redirects. Each `- [ ]` item resolves on the human's explicit approval — check the box (`- [x]`) and append a `- **Decision** <succinct resolution>.` line as the last sub-bullet of the item. Keep the Kind label (`Question` / `Proposal` / `Tradeoff`) in the title so the original shape of the decision stays visible. No separate "Decisions" section — decisions stay inline next to their topic.

**Completeness:** Phase 1 is done when every `- [ ]` item has been checked off (`- [x]`). STOP at the **advancing Phase-1 gate**; `next` here advances to Phase 2 — the Change list.

### Conformance detection

Conformance detection is not a standard step. It runs only when:

- a request asks for it — an audit or a bug; the request sets the scope (full, an area, or whatever the bug implicates); or
- the agent trips over a deviation opportunistically — raise it as a finding under the appropriate `###` subsection. Do not silently expand scope.

A new-feature session runs no detection.

**Performing detection.** Load the relevant platform reference for the codebase under audit — [`ui-map-swiftui.md`](ui-map-swiftui.md) for iOS/SwiftUI, [`ui-map-compose.md`](ui-map-compose.md) for Android/Compose. Also load the project's `README.md` (especially any **Modal Styles** section or other project-conventions content — that is where projects declare overrides and project-specific patterns). Compare code against (a) the current `ui-map.yaml` for route kinds, scenes, modal styles, and other structural facts; (b) the platform reference's standard conventions for the conformance dimensions — `folder-org`, `file-layout`, `naming`, `route-kind` (as realized in code), and `platform-pattern`; and (c) the project's README-declared conventions and overrides. Each detected deviation becomes a finding under the appropriate `###` subsection. If code uses non-standard modifiers or patterns and the README's documentation is missing or stale, propose a README update as a finding.

## Phase 2 — Change list

Once the advancing Phase-1 gate passes, translate the resolved decisions — and, for an audit, the resolved findings — into the typed Change list and, for any approved defers, into the Deferrals section. Produce four things together, before the gate:

1. The typed Change list in the plan document.
2. The Deferrals section in the plan document — one entry per approved defer finding, with TODO pointer and brief rationale (see below). Omit the section if no defers were approved.
3. The proposed `ui-map.yaml` — edit the project's UI Map file in place (see `docs/skai/integration.md` for its location); the working-tree diff is the proposed-map artifact. Consult [`ui-map-guide.md`](ui-map-guide.md) for the YAML format.
4. The render — run the render script (see `docs/skai/integration.md` for the project's invocation) to produce an SVG. The render also validates (schema + semantic checks: dangling refs, duplicate canonical homes, `primary_parent`, modal-style vocabulary). Fix until valid; never present an invalid map. The SVG is the review surface — cite its path at the gate so the human can open it externally.

(*Pure conformance audit* — every finding resolves as a code fix, zero map changes. In that case there is no map diff; the render is the current map, shown as the conformance target.)

Once the package is in place, declare completion directly — no advancing gate. Use the completion line:

`🏁 Complete. The plan document is ready for implementation. Say "implement the plan" (or invoke the UI Map implementation skill directly) to begin.`

### Change entry format

Each entry is a `- [ ]` list item with a bold title, then Description / Justification / Touches as sub-bullets. The checkbox is for the implementation skill to track progress — `- [x]` once executed.

```
- [ ] T<n> <Type>: <identity>
  - **Description** what changes. Single operation: 1–2 lines.
    Multiple operations of the same kind under one identity: a sub-list,
    one bullet per operation. Avoid prose that buries per-operation detail.
  - **Justification** <Source>: <reference or rationale>
  - **Touches** scenes / routes / files affected
```

The title is plain text with a stable task ID, the type word, and identity (e.g., `T1 Add scene: required_update`). Task IDs are `T1`, `T2`, ... — assigned sequentially in document order, and never renumbered or reused (removing a task retires its ID), so cross-references stay stable across plan revisions. The ID identifies, it does not order — entries execute top-down in document order (see Ordering), not by ID. Task IDs are their own namespace, kept distinct from the Phase-1 finding letters (`A`/`B`/`C`); the letter prefix also keeps the checkbox line free of a leading digit, which some Markdown renderers misparse as an ordered-list item (forcing a line break after the checkbox). The leading type word is **capitalized** (`Add`, `Move`, `Modify`, `Conformance`). Sub-bullet field labels are **bold**; no separator (em-dash, colon, etc.) after the label — the bold weight is the separator.

- **Type** — `<operation> <element>` for map changes, or `conformance / <dimension>` for code-vs-map/guide changes.
  - operations: `add` | `remove` | `move` | `modify`
  - map elements: `domain` | `scene` | `route` | `scene-attribute`
  - conformance dimensions: `folder-org` | `file-layout` | `naming` | `route-kind` | `platform-pattern`
- **Source** (the leading token of Justification) — one of: `Upstream requirement` | `Human spec` | `Agent proposal` | `Guide convention` | `Project convention` | `Map` | `Migration mapping`. When the source is a spec or requirement, the Justification is just the citation; when it is `Agent proposal`, give a real rationale. `Project convention` means the project's `README.md` (or equivalent project-conventions doc) is the authority, often for project-specific overrides of the guide. The source is a review-triage signal — a reviewer scans for `Agent proposal`.

**Ordering:** structural, top-down — domain-level changes first, then scenes, then routes — mirroring the map and the rendered diagram. That order also serves as the execution order. Group by domain for audits.

### Deferrals entry format

One bullet per approved defer finding: bold title, TODO pointer, brief rationale.

```
- **<title>** — tracked by `<todo identifier>`. <Brief rationale: the kind of work this is, why it's outside this audit's scope>.
```

The TODO identifier may be a top-level `todos:` scope (e.g. `todos[scope=login]`) or a scene-level marker (e.g. `verify: { todo: true }`). For defers that require adding a new TODO in this pass, cite the new identifier the same way — the new TODO is part of the `ui-map.yaml` diff at Phase 2.
