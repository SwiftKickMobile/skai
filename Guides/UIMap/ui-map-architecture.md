Managed-By: skai
Managed-Id: guide.ui-map-architecture
Managed-Source: Guides/UIMap/ui-map-architecture.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# UI Map Architecture

The architecture method for the UI Map system. Use [`ui-map-guide.md`](ui-map-guide.md) for the YAML map format and [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md) for the change-package artifact formats (map change items, change requests).

## Purpose

The **official map** (`skai/ui-map/ui-map.yaml`) is the frozen architecture authority a change is proposed against, and this guide does not change it. Code should conform to it; any approved gap is tracked by the implementation artifact's unchecked Code Changes items. This guide produces a **change package** at `skai/changes/<change-id>/`: the **proposed map** (`proposed-ui-map.yaml`), its render (`proposed-ui-map.svg`), and the change artifact (decisions + change list).

Two things are the source of truth for the change. The **proposed map** is the architecture the change moves toward. The **change list** (`## Map Changes`) describes exactly the differences between the official map and the proposed map — downstream implementation scopes its work and its audit from it, so a missing, stale, or wrong map change item is a failure, not polish.

This guide produces map artifacts only — no app-code tasks, file moves, build steps, or sequencing. The rendered proposed map is the review surface; until Map Changes is complete, the proposed map, its render, and the change list are provisional.

The workflow runs in two stages:

1. **Discussion** — resolve the genuine map decisions.
2. **Map Changes** — the determined map change items, plus the proposed map and its render.

## The architecture change artifact

One document. Create it at `skai/changes/<change-id>/ui-map-architecture.md`.

If the change ID is clear from the operator's input, use it. If not, do not create the artifact yet. Ask inline for the change ID, propose a short kebab-case default when possible, and wait. When deriving a proposal from the current branch, use only the final path component, not the full branch path; for example, `work/billing-ui` proposes `billing-ui`. Once the change ID is resolved, create the artifact at its final path.

Skeleton:

```
# UI Map Architecture - <name>
## Goal                 one or two sentences; no motivation essay
## Inputs               the sources this architecture artifact was built from
## Mode                 Baseline map | Scoped map change
## Provisional preview  the proposed map and render; maintained through Discussion
## Discussion           the design decisions and open items
## Map Changes          typed map change items from resolved decisions
## Deferrals            approved map deferrals with TODO pointers; may be empty
## Assumptions and TODOs map assumptions, unresolved design gaps, and map TODOs
## Out of scope         scope boundaries the artifact deliberately doesn't address; may be empty
```

## Modes

**Baseline map.** Create a complete first map from designs, product intent, or screen inventory. There is no existing map to pattern-match, so apply *Authoring a UI Map* in [`ui-map-guide.md`](ui-map-guide.md) deliberately, with [`ui-map-demo.md`](ui-map-demo.md) as the worked example.

**Scoped map change.** Update an existing approved map for a story, feature slice, design change, or other map-scoped request. State the active scope and avoid revisiting unrelated map areas unless the requested change cannot be represented without doing so.

A **change request** from downstream implementation is not a separate mode. It arrives as new input on a package that already has a kind; handle it on reopen within that kind (see Initiation). The package keeps its Baseline map or Scoped map change kind, and the request's status lives on the change-request artifact.

If no map change is needed, do not create architecture collateral just to say the map is unchanged.

## Gates and control flow

Gate lines:

- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

At a planned gate: summarize what you did, include the current map-preview status when Discussion has a preview, end with the gate line, STOP and wait. When the architecture package is finished, emit the completion line shown in Map Changes.

**Planned gates** — emitted when ready to advance. `next` moves to the next stage.

- Discussion complete — emitted when every `- [ ]` item in Discussion has been resolved (`- [x]`).

**Completion** — Map Changes has no planned gate. Once the map change items, Deferrals, proposed map, render, and Assumptions and TODOs are in place, declare completion directly.

**Blocked gates** — emitted when the agent cannot advance. Common reasons:

- Discussion in progress: one or more `- [ ]` items remain unresolved.
- Inputs are too contradictory or incomplete to draft a stage.
- A Discussion decision proves unworkable when realized in Map Changes; for example, the proposed map cannot be made valid without revisiting a decision.
- Required tooling is unavailable; for example, the SKAI renderer, its runtime, the SVG dependency, or a project-specific render override cannot produce a valid render.
- The rendered map is invalid or cannot be produced.
- The request requires app-code tasks, file moves, build steps, or implementation sequencing rather than a map artifact.

The operator resolves the cause (resolves items, fixes inputs, revises decisions); the agent re-evaluates and emits the appropriate gate on the next response.

**Advance intent** — moves past a planned gate. Signals: "next", "continue", "go ahead", "do it". Recognized only after this guide has emitted a `⏳ GATE: Next:` line. Expected deliverables named in the initiating request are not advance intent and never skip Discussion. "we should..." / "let's..." is discussion, NOT authorization.

**`auto`** — advance intent that bypasses planned gates only. It never bypasses a blocked gate. `auto to discussion complete` runs until the discussion items are resolved, then STOPs before Map Changes.

## Initiation

The workflow starts on an explicit signal — "write the UI Map architecture document", "create the baseline map", "update the UI Map", or equivalent. Whatever came before (designs, requirements, a discussion, a story, a change request, or a bug request) is context the agent digests; there is no declared mode.

On the signal: digest all available inputs, infer the mode — **baseline map** or **scoped map change** — and draft Discussion.

If new map-relevant input arrives after the architecture package has completed — including a **change request** raised by downstream implementation — reopen the same architecture artifact in Discussion. Treat the new input as additional context and continue the normal Discussion loop, keeping the package's existing kind. Do not create a separate response artifact or replace the existing architecture artifact with a narrow response artifact. Proceed to Map Changes only after the discussion-complete gate advances.

When the new input is a change request artifact in the input set, either incorporate the requested map adjustment, reject it, or supersede it with a different map decision, and record the outcome on the artifact: update its `Reviewer Response` and set its `Change Request Status` (values per [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md)) — use `Incorporated` only once the adjustment is applied in the proposed map in Map Changes, and leave it `Proposed` until then.

## Discussion

The Discussion section is topic-organized. Do NOT create workflow-shaped sections ("Questions", "Decisions", "Tradeoffs", "Open Items") — each topic carries its own open items inline.

Open items use one format:

`- [ ] D<n> [Kind] <summary>` — a letter-led id, a bracketed Kind, and a plain-language summary. The id is `D1`, `D2`, ... across the whole Discussion section; IDs are continuous and never renumbered, so each decision has a stable handle the Map Changes section can cite. The Kind is one of:

- `[Question]` — needs the operator's input; the agent has no basis to recommend. Rare — propose a default whenever there is one.
- `[Proposal]` — the agent recommends a course of action; the operator accepts / rejects / modifies.
- `[Tradeoff]` — two or more options **plus the agent's recommended pick and why**; the operator confirms or chooses differently. Never a neutral menu.

The agent always takes a position: every item carries a recommendation, and a Tradeoff names which option it recommends. When a decision's resolution differs across the items it affects, expand it into a sub-list **bucketed by proposed resolution** — one bucket per resolution, the affected items under it — so the operator can confirm or override per bucket. When all items share one resolution, state it once with a count; do not repeat it per item.

**When a choice becomes a discussion item.** The agent always takes a position, so "discussion needed" is not "I can't decide" — it is "the operator should consciously confirm this one." Raise a choice as a `D#` item only when it is **both**:

- **Unforced** — the design, a UI Map convention, or clear ownership doesn't settle it; your pick is a genuine judgment call among options that each fit, not a reading of what's shown. (Tell: an honest justification of "A fits, though B would too" is unforced; "the design shows a sheet" or "a transient overlay is conventionally a sheet" is forced.)
- **Material** — picking differently reshapes the map: a different route container (nav vs. modal), different nesting, or a different domain — not a cosmetic attribute (a sheet's style, a note, a name).

Otherwise, decide and let the rendered preview be the review surface: a *forced* choice you encode however structural it is; an *unforced but immaterial* one you settle with a sensible default. When you do raise an item, still bring your recommendation (`[Proposal]` / `[Tradeoff]`); a bare `[Question]` is only for the rare case you can't even lean.

Keep each discussion item scoped to one map decision. If expressing the map surfaces another choice that meets that bar, make it its own discussion item rather than bundling it. Do not combine ownership, route kind, presentation style, naming, or reuse into one option unless the input explicitly couples them.

Place a marker on the specific content line that needs input — never on a heading, never as a roll-up on a parent. The marker count equals the number of real decisions.

Use `###` subsections only for actual Discussion topics: one or more `D#` items, or retained resolved items that still explain the current map. Do not create `###` headings merely to restate fully specified input. Capture fully specified input in `## Inputs`, `## Provisional preview`, `## Assumptions and TODOs`, and `## Map Changes` instead.

**Empty Discussion state:** If drafting or updating produces no `D#` items, and there are no retained resolved items that still explain the current map, leave `## Discussion` as one plain paragraph: "The listed Inputs determine the proposed map; review the provisional preview before it is finalized in Map Changes." This is the empty state for the section; omit it whenever `## Discussion` contains any `D#` items.

**Drafting:**

- *Baseline map* — summarize the Goal and Inputs, then encode the map the inputs describe, seeding Discussion only for the choices that meet the bar above. If the input directly names the app structure, feature areas, screens, and route relationships, encode that structure without asking the operator to approve the straightforward translation; the rendered preview is the review surface for feedback.
- *Scoped map change* — summarize the active scope and current map context, then seed Discussion only for decisions needed to express that map change.
- *Reopen (including a change request)* — summarize the new input and its evidence in Goal/Inputs. If the requested adjustment is coherent and fully specified, update the provisional preview and draft no *new* discussion items — but retain the artifact's existing resolved items that still explain the current map. Never replace `## Discussion` with the empty state on a reopened artifact, especially when map change items still cite those decisions (`D#`). Seed Discussion only when incorporation, rejection, supersession, or map representation requires a real decision.
- If the inputs fully specify the map, draft no new items. Use the empty Discussion state only when the section has no retained resolved items.
- If the request drifts into app-code tasks, file moves, build steps, or implementation sequencing, record only the map fact that matters; leave execution details out of this artifact.

**Route kind.** Read it from how the destination is actually presented when the design shows that — never from vague wording (see *Authoring a UI Map* in [`ui-map-guide.md`](ui-map-guide.md)). When the design doesn't show it, apply the bar above: pick the conventional default and surface it in the preview, and raise a discussion item only when the choice is also material — it changes the route container or the map's shape, not just the presentation style.

**Display/data states are not structure.** Empty, populated, loading, and error are scene states, not separate scenes or `implements` variants — see *Authoring a UI Map* in [`ui-map-guide.md`](ui-map-guide.md). Capture them as notes, assumptions, or map TODOs when they matter to the discussion.

### Provisional preview

During Discussion, once there is enough concrete structure to propose a map, maintain the proposed map and its render in the change package:

```text
skai/changes/<change-id>/proposed-ui-map.yaml
skai/changes/<change-id>/proposed-ui-map.svg
```

Seed the proposed map from the current official map (`skai/ui-map/ui-map.yaml`); for a baseline, where no official map exists yet, start from empty. Edit the proposed map here — the official map stays frozen.

Add or update `## Provisional preview` in `ui-map-architecture.md` with paths to the proposed map and render and a status line saying they are provisional until Discussion resolves and Map Changes completes.

The proposed map reflects the agent's current proposals and any resolved decisions. It is a discussion aid, not approval. Open discussion items remain the source of truth for unresolved decisions. When the operator changes direction, update the proposed map to match the current proposal state before the next gate when tooling allows.

The proposed map is YAML-first. Do not investigate render tooling before the artifact exists. If there is not enough concrete structure to produce a useful render, say so in `## Provisional preview`. Before a gate, check the proposed map for map-validity choices the renderer cannot infer: reused scenes with more than one inbound route need a visual home, and every modal destination needs an agreed `modal_style` from the declared vocabulary. Resolve such choices by the bar above: default when the map is obvious, raise a discussion item only when the choice is unforced and material. Once `proposed-ui-map.yaml` exists and has enough structure to review, attempt to render it before the next gate: use any project-specific override first; otherwise use the default SKAI renderer from [`ui-map-guide.md`](ui-map-guide.md). If the render is not produced, the artifact and gate response must state the concrete reason — missing SKAI root, missing runtime dependency, renderer failure, invalid YAML, not useful yet, or another specific blocker. Do not leave render status as merely pending, and do not invent a non-SKAI render command.

**Structural self-check before gating.** The renderer validates schema and semantics but not the authoring conventions — a non-collapsed single-root domain or a flattened scene renders fine. Before each gate, check the provisional against *Authoring a UI Map* in [`ui-map-guide.md`](ui-map-guide.md): single-root domains collapsed, non-root scenes nested under the route that reaches them, reused scenes with one home and a `primary_parent`, `common:` only for domain-agnostic scenes, and every section the operator reads consistent with the current proposed map — notes and assumptions describe nothing superseded, no now-resolved decision is still called `pending`, `open`, or `unresolved`, and on a reopen the inherited `## Map Changes` and `## Deferrals` — which describe the prior pass — are marked pending re-derivation rather than left reading as current. Fix the artifact before gating — the gate presents what the operator reviews.

**Domain structure line.** In `## Provisional preview`, record and keep current a one-line domain summary: name every domain, and for each non-collapsed (`scenes:`) domain list its root scenes. Collapsed domains are named only; a bucket lists its roots:

```text
Domains: shell, tickets, billing (collapsed); reports (bucket — roots: ticket_report, billing_report)
```

Writing this forces the single-root check into the open — a bucket whose root list has one entry must be collapsed (rename the domain to that scene), not left as a `scenes:` wrapper. Keep the line current whenever the domain set changes; the operator reviews it alongside the render.

Before every gate line, include a short map-preview status:

```text
🗺️ Updated provisional map render: skai/changes/<change-id>/proposed-ui-map.svg
```

or, when unavailable:

```text
🗺️ Provisional map render not updated: <reason>.
```

**Example** (LumenNotes — a Tradeoff with a recommended pick, and a Proposal):

```
## Discussion

### Sharing a note

A note needs a way to share its contents. Today it has no outgoing share route.

- [ ] D1 [Tradeoff] How is share presented from a note?
  - **Concern** Share can be a modal sheet over the note or a pushed screen.
  - **Options**
    - A — `modal` sheet over the note
    - B — `nav` push onto the note's stack
  - **Proposal** A (modal) — sharing is a transient side-task, not a destination in the note's flow.
  - **Why** A sheet dismisses back to where you were; a push implies a place in the navigation.

### Scene name

- [ ] D2 [Proposal] Name for the share scene
  - **Concern** The new scene needs a scene id.
  - **Proposal** `share_sheet`.
  - **Why** Matches the modal's role and reads clearly in the map.
```

**Example** (empty Discussion state):

```
## Discussion

The listed Inputs determine the proposed map; review the provisional preview before it is finalized in Map Changes.
```

Each discussion item is its own `- [ ]` item under the appropriate `###` subsection. The title is `<id> [Kind] <plain-language summary>` — the id is `D1`, `D2`, ... (letter-led so renderers don't misparse it as a list; continuous across subsections, no per-group reset), `[Kind]` is `Proposal` / `Tradeoff` / `Question`, and the title itself carries no bold. Sub-bullet labels are **bold** with no separator after: `Concern` always, then either a `Proposal` (the recommended action — a `Tradeoff` adds `Options`) or, for a `Question`, a `Question` line (what you need decided and why you can't recommend yet); `Detail` when the concern needs elaboration; `Why` for the rationale. On approval, check the box and append a `- **Decision** <succinct resolution>.` line as the last sub-bullet.

**Keep discussion items tight:** where two or more `- [ ]` items sit under the same heading, leave no blank line between them. A blank line makes the list "loose," which pushes the checkbox onto its own line in some renderers; a tight list keeps the checkbox inline with the title. This applies to discussion items and map change items alike.

After drafting, and after each subsequent response, update the artifact before speaking: revise `ui-map-architecture.md`, update the provisional preview to match it, then STOP at a gate. Emit a **Blocked** gate if any `- [ ]` items remain, or the advancing **Planned** gate if none do — every item `- [x]`, or drafting produced no items at all because the inputs fully specify the map. Do not describe intended artifact changes without applying them.

`⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Map Changes.`
`⏳ GATE: Next: Discussion complete. Say "next" to write Map Changes.`

**Discussion loop:** the agent proposes, the operator refines or redirects. Discussion items are live working topics until resolved, not a frozen first draft.

As the conversation evolves:
- Revise an unresolved item when the operator clarifies or redirects its proposal.
- Split an unresolved item when one topic becomes multiple map decisions. Keep the original ID on the first resulting item and assign new IDs to the others.
- Add a follow-up item when a decision exposes a new map decision that was not visible before.
- Remove an unresolved item when the direction changes so it no longer applies. The architecture artifact should stay focused on the current map, not preserve every abandoned branch.
- Do not add follow-up items for unknowns that can be represented as assumptions, TODOs, or non-blocking notes without changing scene/route architecture.

Keep IDs stable and never renumber existing items. Each `- [ ]` item resolves on the operator's explicit approval — check the box (`- [x]`) and append a `- **Decision** <succinct resolution>.` line as the last sub-bullet of the item. Keep resolved decisions only when they still explain the current map. If a later direction subsumes, contradicts, or makes a resolved item misleading, collapse the topic around the current decision: revise the surviving item and remove stale items rather than carrying redundant history forward. Resolved items are not meeting minutes, but they must not erase why the decision existed: when the operator changes or rejects a recommendation, keep enough of the original options, proposal, and rationale to show what was changed, then use the Decision line for the current outcome. Keep the Kind label (`Question` / `Proposal` / `Tradeoff`) in the title so the original shape of the decision stays visible. No separate "Decisions" section — decisions stay inline next to their topic.

**Completeness:** Discussion is done when every `- [ ]` item has been checked off (`- [x]`). STOP at the advancing gate; `next` here advances to Map Changes.

### Writing style

Map decisions and notes are written in **plain language** — a teammate who doesn't know the schema should understand them. Say what the thing actually is, says, or does; don't describe it by its schema field or by a rule name.

Tells to check before writing:
- Quote or paraphrase the real content — what a design actually shows, what a stale note actually says, what the map actually does — not `todos[scope=...]` or `primary_parent`.
- Don't cite rule names ("the modal-style convention", "the canonical-home rule"); state the situation instead.
- Prefer "screen" / "route" / "name" over schema jargon where it reads more naturally.

Avoid:
> **Detail** `billing.modal_style` violates the modal-style convention.

Instead:
> **Detail** The map says Billing opens as a full-screen destination, but the design shows it as a temporary sheet over Settings.

## Map Changes

Once the advancing gate passes, produce the typed map change items by **diffing the frozen official map against the proposed map** — one item per real difference (for a baseline there is no official map, so the whole proposed map is the difference). The resolved decisions supply each item's justification, not the set of items — the diff is what makes the section complete, so an attribute-level difference (a note, a `modal_style`) is its own item even when no decision singled it out. Also write the Deferrals section for any approved map deferrals.

Map change items are written and updated only in Map Changes, never during Discussion.

**The final map is the reviewed provisional.** Write the structure the operator approved at the gate; do not silently re-derive or restructure it here. If realizing the map exposes a needed correction — the provisional cannot be made valid without one — make the minimal fix, record it in Map Changes / Assumptions, and re-render. A structural change beyond a validity fix is a new decision: return to Discussion and re-gate rather than changing the shape after approval.

`## Map Changes` describes exactly the differences between the frozen official map and the proposed map. Since the official map does not move, that diff is recomputable at any time: when the artifact is reopened for new work and already holds map change items from earlier passes, recompute the diff and reconcile the existing items against it — never reset or regenerate the section. An item that still matches a difference keeps its `M#` id and justification; a new difference gets a new item; a difference that no longer holds (the proposed map moved back) loses its item. The ids and rationale are the part a raw diff cannot reconstruct.

Produce these together before completing:

1. The typed map change items in `skai/changes/<change-id>/ui-map-architecture.md`.
2. The Deferrals section in `skai/changes/<change-id>/ui-map-architecture.md` — one entry per approved map deferral, with TODO pointer and brief rationale. Omit the section if no deferrals were approved.
3. The proposed map — `skai/changes/<change-id>/proposed-ui-map.yaml`. The official map stays frozen. Consult [`ui-map-guide.md`](ui-map-guide.md) for the YAML format and its *Authoring a UI Map* conventions.
4. The render — run the project-specific render override when one exists; otherwise use the default SKAI renderer from [`ui-map-guide.md`](ui-map-guide.md) to produce `skai/changes/<change-id>/proposed-ui-map.svg`. The render also validates schema and semantic checks: dangling refs, duplicate canonical homes, `primary_parent`, required modal styles and their vocabulary, and related map constraints. Fix until valid; never present an invalid map. The SVG is the review surface.
5. The Assumptions and TODOs section — map assumptions, unresolved design gaps that do not block the map, and any map TODOs added or updated.

Before completion, update `## Provisional preview` so it no longer reads as an active Discussion status: the proposed map and render in the package are now the finished change package, pending review.

If a project-specific render override is missing required values, is broken, or contradicts the SKAI renderer contract, STOP with a blocked gate. If no override exists, use the default SKAI renderer. STOP only when the SKAI root, renderer script, runtime dependency, SVG dependency, or validation result prevents a valid render.

If every resolved decision produces zero map changes, state that in `## Map Changes`, render the proposed map when a renderer is available, and complete.

Once the package is in place, declare completion directly — no final planned gate. Use the completion line:

`🏁 Complete. The UI Map architecture artifact is ready.`

### Map change item format

Map change items follow the format defined in [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md): a stable `M#` ID, a `Type` (`<operation> <element>`), an identity, and **Description** / **Justification** (`<Source>: ...`) / **Touches** sub-bullets. Do not use a checkbox — the map change is realized by the accompanying proposed map and render. Write items top-down in structural order (domain-level changes first, then scenes, then routes), mirroring the map and the rendered diagram; the `M#` ID identifies, it does not order.

### Deferrals entry format

One bullet per approved map deferral: bold title, TODO pointer, brief rationale.

```
- **<title>** — tracked by `<todo identifier>`. <Brief rationale: the kind of map work this is, why it is outside this artifact's scope>.
```

The TODO identifier may be a top-level `todos:` scope (e.g. `todos[scope=login]`) or a scene-level marker (e.g. `verify: { todo: true }`). For deferrals that require adding a new TODO in this pass, cite the new identifier the same way — the new TODO is part of the proposed map in Map Changes.
