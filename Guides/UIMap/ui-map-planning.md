Managed-By: skai
Managed-Id: guide.ui-map-planning
Managed-Source: Guides/UIMap/ui-map-planning.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-05-24

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
## Change list   phase 2; typed changes from the resolved findings
## Deferrals     phase 2; approved defer findings with TODO pointers; may be empty
## Out of scope  scope boundaries the plan deliberately doesn't address; may be empty
```

## Gates and control flow

Gate lines:

- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

At a planned gate: summarize what you did, end with the gate line, STOP and wait. When planning finishes, emit the completion handoff — the `🏁 Complete.` line shown at Phase 2 — Change list.

**Planned gates** — emitted when ready to advance. `next` moves to the next phase.

- End of Phase 1 — emitted when every `- [ ]` item in Discussion has been resolved (`- [x]`).
- End of Phase 2 is *not* a planned gate — once the Change list + Deferrals + `ui-map.yaml` diff + render are in place, the agent declares completion directly (see the `🏁 Complete.` line above) and tells the human how to invoke implementation.

**Blocked gates** — emitted when the agent cannot advance. Common reasons:

- Phase 1 in progress: one or more `- [ ]` items remain unresolved.
- Inputs are too contradictory or incomplete to draft a phase.
- A Phase-1 decision proves unworkable when Phase-2 tries to realize it (kicks back to Phase 1) — e.g. the proposed map cannot be made valid without revisiting a decision.
- Required tooling or commands are missing — e.g. the render/validation command or the `ui-map.yaml` location isn't documented in `docs/skai/integration.md`. STOP and ask rather than improvise a command.

The human resolves the cause (resolves items, fixes inputs, revises decisions); the agent re-evaluates and emits the appropriate gate on the next response.

**Advance intent** — moves past a planned gate. Signals: "next", "continue", "go ahead". Recognized only after a `⏳ GATE: Next:` line. "we should…" / "let's…" is discussion, NOT authorization.

**`auto`** — advance intent that bypasses *planned* gates only. It never bypasses a blocked gate.

Bright-line: if continuing correctly would require changing something already approved, that is an amendment, not a fix — STOP, state it, propose the amendment, get approval. Resolution may route back to a prior phase.

## Initiation

Planning starts on an explicit signal — "write the planning document" or equivalent. Whatever came before (a requirements set, a discussion, an audit or bug request) is context the agent digests; there is no declared mode.

On the signal: digest all available inputs, infer the situation — **new change** or **audit** — and draft Phase 1.

## Phase 1 — Discussion

The Discussion section is topic-organized. New-change drafting uses free-form prose with one section per concern; audits use a fixed structure (see Audit proposal example below). In new-change drafting, do NOT create workflow-shaped sections ("Questions", "Decisions") — each topic carries its own open items inline.

Open items are `- [ ]` lines tagged with a Kind. The same Kinds are used in both new-change discussion and audit findings:

- `- [ ] Question — …` — needs the human's input; the agent has no basis to recommend. Rare — propose a default whenever there is one.
- `- [ ] Proposal — …` — the agent recommends a course of action; the human accepts / rejects / modifies.
- `- [ ] Tradeoff — …` — two or more options **plus the agent's recommended pick and why**; the human confirms or chooses differently. Never a neutral menu.

The agent always takes a position: every item carries a recommendation, and a Tradeoff names which option it recommends. When a finding's resolution differs across the items it affects, expand it into a sub-list **bucketed by proposed resolution** — one bucket per resolution, the affected items under it — so the human can confirm or override per bucket (e.g., "approve the rename-the-map bucket, but keep X"). When all items share one resolution, state it once with a count; do not repeat it per item.

Place a marker on the specific content line that needs input — never on a heading, never as a roll-up on a parent. The marker count equals the number of real decisions.

**Drafting:**

- *New change* — summarize the Goal and Inputs, then seed the Discussion with proposals and open items for the genuine design decisions. The agent MUST seed proposals; the document is never a passive transcript. If the inputs fully specify the change, state "inputs fully specify the change — no open questions" and draft no items.
- *Audit* — first run conformance detection (see the **Conformance detection** section below for what to load and compare against), then draft in **two passes**: pass 1, enumerate every deviation as an atomic *concern* — a one-line working list, not written into the document; pass 2, analyze and dispose each, writing them up as the findings below (the findings are the only persisted artifact). Each finding is its own `- [ ]` item under the appropriate `###` subsection (see the finding format below); each is approved (and checked off) individually. **One finding per concern, high-level**: when all of a concern's instances take the *same* disposition, state it once with a count and leave the itemized list to Phase 2; when the disposition differs across instances, list them bucketed by resolution (per the bucket rule above). **Findings are deviations only**; conformant scenes are not enumerated. Findings state what changes and why; how to execute belongs to the implementation method.

  **Disposing a finding is a two-step call.** (1) *Can the deviation be resolved as a UI-Map change or as a code-conformance fix under the guide's conventions?* If neither — not expressible in the map, and not a convention the guide defines — it is outside the skill's scope; record it under `Out of scope` (it needs separate handling), not as a finding. (2) If yes, *is it low cost/complexity/risk?* Yes → **fix now** (a `fix map` or `fix code` Change-list entry); no → **defer**. Weigh cost/risk by locality (one file vs cross-cutting), behavior risk (structure-only vs touches runtime), new-code volume (templated vs real logic), and reversibility — the agent proposes the call, the human approves it. Mechanical relocations, renames, file-layout moves, and placeholder scaffolds are always **fix now**: moving folders to mirror `domains:` (`git mv`), renaming a scene id or type, inlining a route enum, adding a missing placeholder ViewModel. The thing that **defers** is a *refactor* — rewriting or re-architecting existing code, a design task even when behavior is unchanged; relocating and renaming are not refactors. A map scene with no code, found while auditing an existing app, is a **defer** (tracked by a todo) — placeholder scaffolding is for new work, not back-filling a shipped app.

  A deferred finding ensures the map's `todos:` mechanism records the pending work (an existing TODO, or a new one added this pass) and produces no Change-list entry; approved defers populate the Phase 2 Deferrals section with a pointer to the TODO. **Project-wide topics** that cross-cut many findings (e.g. a repo-wide pattern, a missing project-convention doc section), and any **`Question`** finding (a deviation you cannot dispose without the human's intent), may be raised as their own Discussion items before the disposition-grouped findings. Use sparingly — only when keeping the decision inline would noise up multiple per-scene findings.

**Audit example** (LumenNotes — a Proposal, a Tradeoff with a recommended pick, a bucketed rename, and a defer):

```
### Map fixes

- [ ] F1 [Proposal] The Note screen's variants aren't in the map
  - **Concern** The map doesn't capture that one screen is built more than one way.
  - **Detail** `NoteView` renders two forms — a full note and a quick "peek" — but the map's `note` scene lists no variants.
  - **Proposal** Fix map (now) — add the two variants to `note`.
  - **Why** The map should show that one screen has two forms.

### Code conformance

- [ ] F2 [Tradeoff] Routes are kept in separate files
  - **Concern** All 9 screens keep their navigation routes in a standalone file instead of next to the code that uses them.
  - **Options**
    - A — move each into its ViewModel file and delete the separate file (the convention)
    - B — treat it as a deliberate house style and document it as a project exception in the README
  - **Proposal** A (now) — nothing suggests it's intentional, and keeping routes next to the code that drives them is the convention. 9 files, same fix — itemized in Phase 2.
  - **Why** If it were a real house style we'd expect it documented, and it isn't.
- [ ] F3 [Proposal] Folders don't match how the map groups screens
  - **Concern** The folder layout predates the current grouping and no longer matches the map.
  - **Detail** There are no per-domain folders; screens are scattered (the whole Editor group sits inside Library).
  - **Proposal** Fix code (now) — move the folders to match the map's groups, with `git mv`. ~8 folders, same kind of move — itemized in Phase 2.
  - **Why** Map-matching folders are a core feature, and moving files is mechanical, not a rewrite.
- [ ] F4 [Proposal] Some screen names don't match their code
  - **Concern** A few screens are named one thing in the map and another in the code.
  - **Proposal** Fix now — rename each pair to match, direction per case by least work:
    - rename the map: `note_editor` → `editor` ("note_" is redundant)
    - rename the code: `TrashListView` → `TrashView` — "trash" is the name we want
  - **Why** A screen's map name and its code type name should be the same.

### Deferred

- [ ] F5 [Proposal] The search-results screen is in the map but not the code
  - **Concern** The map defines a screen the app doesn't have yet.
  - **Detail** The map has `search → results`, but there's no `ResultsView`.
  - **Proposal** Defer — track it with a todo on the `results` scene. It's unbuilt feature work, and we don't drop placeholders into a shipped app.
  - **Why** Building the real screen belongs to a separate work spec.
```

Each finding is its own `- [ ]` item under the appropriate `###` subsection. The title is `<id> [Kind] <plain-language summary>` — the id is `F1`, `F2`, … (letter-led so renderers don't misparse it as a list; continuous across subsections, no per-group reset), `[Kind]` is `Proposal` / `Tradeoff` / `Question`, and the title itself carries no bold. Subsections group by disposition: `Map fixes` (fix-map), `Code conformance` (fix-code), `Deferred` — in that order; omit any with no findings. A `Tradeoff` files under its recommended option's disposition; a finding whose buckets span directions (some fix-map, some fix-code) files under `Code conformance`, each direction in its own bucket. A `Question` has no disposition yet, so it isn't filed under a subsection — raise it above them as its own Discussion item (see Project-wide topics above). It's answered in place — check the box and append the `Decision` — and stays where it is; the document is not reorganized. Sub-bullet labels are **bold** with no separator after: `Concern` always, then either a `Proposal` (the recommended action — a `Tradeoff` adds `Options`) or, for a `Question`, a `Question` line (what you need decided and why you can't recommend yet); `Detail` when the concern needs elaboration; `Why` for the rationale. On approval, check the box and append a `- **Decision** <succinct resolution>.` line as the last sub-bullet. Approved defers cite a TODO in the Proposal and also populate the Phase 2 Deferrals section.

**Keep findings tight:** within a subsection, leave no blank line between one finding and the next. A blank line makes the list "loose," which pushes the checkbox onto its own line in some renderers; a tight list keeps the checkbox inline with the title. The same applies to Change-list entries.

After drafting, and after each subsequent response, STOP at a gate: a **Blocked** gate if any `- [ ]` items remain, or the advancing **Planned** gate if none do — every item `- [x]`, or drafting produced no items at all (inputs fully specify the change, or the audit found no deviations).

`⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to the Change list.`
`⏳ GATE: Next: Discussion complete. Say "next" to advance to the Change list.`

**Discussion loop:** the agent proposes, the human refines or redirects. Each `- [ ]` item resolves on the human's explicit approval — check the box (`- [x]`) and append a `- **Decision** <succinct resolution>.` line as the last sub-bullet of the item. Keep the Kind label (`Question` / `Proposal` / `Tradeoff`) in the title so the original shape of the decision stays visible. No separate "Decisions" section — decisions stay inline next to their topic.

**Completeness:** Phase 1 is done when every `- [ ]` item has been checked off (`- [x]`). STOP at the **advancing Phase-1 gate**; `next` here advances to Phase 2 — the Change list.

### Writing style

Findings and discussion items are written in **plain language** — a teammate who doesn't know the schema should understand them. Say what the thing actually is, says, or does; don't describe it by its schema field or by a rule name.

Tells to check before writing:
- Quote or paraphrase the real content — what a stale note actually says, what the code actually does — not `todos[scope=…]` or `primary_parent`.
- Don't cite rule names ("the domain-mirror rule", "the modal-style → enum-suffix convention"); state the situation instead.
- Prefer "screen" / "folder" / "name" over schema jargon where it reads more naturally.

Avoid:
> **Detail** `todos[scope=folder-layout]` targets `Library/` and cites `primary_parent`; both violate the domain-mirror rule.

Instead:
> **Detail** The map has a leftover note telling us to move the Search and Profile screens into the Library folder. That's wrong now — those screens belong in their own group, and the note is chasing a display-only hint that isn't meant to move files.

### Conformance detection

Conformance detection is not a standard step. It runs only when:

- a request asks for it — an audit or a bug; the request sets the scope (full, an area, or whatever the bug implicates); or
- the agent trips over a deviation opportunistically — raise it as its own finding and let the human set the scope; don't silently widen the audit. (In an otherwise free-form new-change Discussion, append such audit-style findings at the end.)

A new-feature session runs no *deliberate* detection — but an incidental trip-over is still raised, with the human setting scope.

**Performing detection.** Load the relevant platform reference for the codebase under audit — [`ui-map-swiftui.md`](ui-map-swiftui.md) for iOS/SwiftUI, [`ui-map-compose.md`](ui-map-compose.md) for Android/Compose. Also load the project's `README.md` (especially any **Modal Styles** section or other project-conventions content — that is where projects declare overrides and project-specific patterns). Compare code against (a) the current `ui-map.yaml` for route kinds, scenes, modal styles, and other structural facts; (b) the platform reference's standard conventions for the conformance dimensions — `folder-org`, `file-layout`, `naming`, `route-kind` (as realized in code), and `platform-pattern`; and (c) the project's README-declared conventions and overrides. Read a route's kind and modal-style from the modifier it is actually bound to, not from the enum's name — e.g. `.modal(item: $vm.messageRoute)` is the `modal` style even though the enum is named `…MessageRoute`. Each detected deviation becomes a finding under the appropriate `###` subsection. If code uses non-standard modifiers or patterns and the README's documentation is missing or stale, propose a README update as a finding.

## Phase 2 — Change list

Once the advancing Phase-1 gate passes, translate the resolved decisions — and, for an audit, the resolved findings — into the typed Change list and, for any approved defers, into the Deferrals section. (A *fix-map* finding becomes an `add` / `remove` / `move` / `modify` map entry; a *fix-code* finding becomes a `conformance / <dimension>` entry.) Produce four things together, before the gate:

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
  - **Description** what changes. Single operation: 1-2 lines.
    Multiple operations of the same kind under one identity: a sub-list,
    one bullet per operation. Avoid prose that buries per-operation detail.
  - **Justification** <Source>: <reference or rationale>
  - **Touches** scenes / routes / files affected
```

The title is plain text with a stable task ID, the type word, and identity (e.g., `T1 Add scene: required_update`). Task IDs are `T1`, `T2`, … — assigned sequentially in document order, and never renumbered or reused (removing a task retires its ID), so cross-references stay stable across plan revisions. The ID identifies, it does not order — entries execute top-down in document order (see Ordering), not by ID. Task IDs are their own namespace, kept distinct from the Phase-1 finding ids (`F1`/`F2`); the letter prefix also keeps the checkbox line free of a leading digit, which some Markdown renderers misparse as an ordered-list item (forcing a line break after the checkbox). The leading type word is **capitalized** (`Add`, `Move`, `Modify`, `Conformance`). Sub-bullet field labels are **bold**; no separator (em-dash, colon, etc.) after the label — the bold weight is the separator.

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
