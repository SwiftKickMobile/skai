Managed-By: skai
Managed-Id: guide.ui-map-implementation
Managed-Source: Guides/UIMap/ui-map-implementation.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-11

# UI Map Implementation

The implementation method for the UI Map system. It executes or specifies the code work needed to conform to an approved map and promotes an approved proposed map when one exists. Use [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md) for the code-change and evidence formats this skill produces, [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md) for the map-change items it consumes and the change requests it raises, and [`ui-map-guide.md`](ui-map-guide.md) for the YAML map.

For platform-specific code conventions, load [`ui-map-swiftui.md`](ui-map-swiftui.md) for iOS/SwiftUI or [`ui-map-compose.md`](ui-map-compose.md) for Android/Compose. For placeholder scaffolding, load [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md) or [`ui-map-compose-placeholders.md`](ui-map-compose-placeholders.md) for the matching stack.

## Purpose

Implementation makes app code conform to an approved UI Map architecture or records the conformance work for a larger effort, then advances the official map when a proposed map exists. The system keeps two map files:

- **Official map** — `skai/ui-map/ui-map.yaml`, the approved architecture authority; frozen while a proposed change is under review.
- **Proposed map** — `skai/changes/<change-id>/proposed-ui-map.yaml`, the architecture the change moves toward.

When a proposed map exists, implementation works against it, then **promotes** it after the Code Changes spec is approved: copy the proposed YAML to the official YAML, then regenerate the official SVG from that official YAML, so the approved architecture advances. The proposed SVG is a preview, not a promotion source. In Build this follows a green conforming build. In Plan the approved map intentionally leads the unchecked implementation work recorded in the artifact. Promotion is the final UI Map implementation step of every run that changes the map; a no-package conformance run works against and leaves the official map unchanged.

**Invariant — the map leads, code follows.** The target map is the architecture authority. Implementation may scaffold, align, move, rename, hand off, block, or raise a **change request** back to architecture — but it never edits map content to justify code. When the map itself is wrong or infeasible, raise a change request; when the skill simply can't do a change mechanically, hand it off or stop at a blocked gate (see *Code Changes*).

**Invariant — structure, not features.** Implementation changes and creates *structure* — scaffolding new scenes, wiring routes, moving, renaming, aligning code to the platform conventions — but never *feature content*: no business logic, no real UI, no data beyond placeholder labels. A scene it scaffolds is a minimal placeholder that compiles, routes correctly, and is visibly identifiable in the running app.

This workflow is one part of a larger agent session, not the system of record for every task in that session. Keep unrelated feature, bug, and product work out of the UI Map implementation artifact, including disclaimers that label it excluded or outside scope; session orchestration or that work's own skill and artifacts own it. If such work appears alongside a UI Map request, complete the separable UI-map-owned work through `🏁` before session orchestration starts the unrelated work, even when both happen in the same overall agent turn. Record `handoff` only when external work directly affects UI Map conformance or reconciliation. Block only when the UI Map work itself cannot proceed without that work or an external decision.

Implementation runs in four stages:

1. **Audit** — compare the codebase to the target map within the run's scope.
2. **Discussion** — resolve the audit findings that genuinely need a decision.
3. **Code Changes** — write the checklisted, disposition-coded code-change items, ending with a terminal promote item when a proposed map exists.
4. **Implement** — execute the items this mode owns and, when applicable, end by promoting the proposed map.

## Run mode

The skill **infers** its run mode from context at initiation and records it in the artifact's `Mode` field, which **travels with the artifact** — so any session that picks up the work knows the intent. The mode is the scope of the job:

- **Plan** — inferred when a larger feature, bug-fix, or refactor workflow will own the **same structural conformance work**. This skill produces the conformance spec only: UI-map-owned code items are unchecked `planned`; directly relevant work owned elsewhere is unchecked `handoff`; when a proposed map exists, it performs and checks the terminal promote, then completes.
- **Build** — inferred when UI Map implementation owns the structural conformance work. The skill implements and checks UI-map-owned `implement` and `placeholder` work — scaffold placeholders, wire routes, move/rename to conform, build green, then promote when a proposed map exists — delivering a reachable, navigable skeleton. Unchecked `handoff` items block Build completion/promotion until the owning workflow resolves them and the run can resume. Build does not imply scaffolding, and unrelated tasks elsewhere in the same session do not turn a Build into Plan.

## Inputs

Required:

- The target map: when an architecture change package exists at `skai/changes/<change-id>/`, its proposed map (`proposed-ui-map.yaml`), render, and architecture artifact (`ui-map-architecture.md`) with `## Map Changes`; otherwise the official map for a no-package conformance run. A package is ready for implementation when its Discussion has no unchecked items, no change request remains `Proposed`, and its current `## Map Changes`, proposed YAML, and nonempty render are present.
- The official map `skai/ui-map/ui-map.yaml`, the frozen baseline the change is measured against. (For a baseline there is none yet.)
- The app codebase.
- The platform convention guide: [`ui-map-swiftui.md`](ui-map-swiftui.md) for iOS/SwiftUI or [`ui-map-compose.md`](ui-map-compose.md) for Android/Compose.
- The matching placeholder guide whenever placeholder work is in scope during Audit, Plan, or Build: [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md) or [`ui-map-compose-placeholders.md`](ui-map-compose-placeholders.md). Omit it only when no placeholder work is in scope.
- The artifact-format references: [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md) (code-change items + evidence this skill writes) and [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md) (map-change items it reads, change requests it raises).
- `skai/integration.md` for build/test commands, render overrides, and evidence paths. Do not invent project-specific commands; for rendering, use the SKAI default from [`ui-map-guide.md`](ui-map-guide.md) when no override exists.
Expected when available:

- The project's `README.md` or equivalent project-conventions doc for overrides such as modal styles, route wrappers, folder layout, or view-model conventions. Standard guide-covered patterns do not require one.
- Scoped architecture/change collateral for the active story, and the active upstream requirement/story/bug scope.

If no change package is present, conform code to the official `skai/ui-map/ui-map.yaml` as the frozen source of truth (the map is unchanged); a missing architecture artifact is not a blocker when the map and codebase are present. If the map (proposed or official) is missing, invalid, or not identifiable, STOP with a blocked gate (see *Gates and control flow*). Multiple plausible change packages with no named target make the map not identifiable; do not choose one. If the app codebase is not present, STOP with a blocked gate.

## Implementation artifact

Create the implementation artifact in the change package, parallel to the architecture artifact: `skai/changes/<change-id>/ui-map-implementation.md`. When a change package is present, use its `<change-id>`. When there is none — a conformance run against the official map — resolve the id the way the architecture skill does: if it is clear from the user's input, use it; if not, do not create the artifact yet — ask inline for the change ID, propose a short kebab-case default when possible (deriving from the current branch, use only its final path component, e.g. `work/billing-ui` → `billing-ui`), and wait.

Skeleton:

```
# UI Map Implementation — <name>
## Goal
## Inputs
## Mode
<Plan | Build>
## Audit
## Discussion
## Code Changes
## Change Requests
## Evidence
```

The stage sections are filled in as the workflow runs. Replace `<Plan | Build>` with exactly one inferred value; a later workflow reads that recorded Mode before acting. Write every section as a record of UI Map conformance within this run's current scope. When the same session also contains separate work, omit that work entirely from Goal, Audit, Discussion, Code Changes, Change Requests, and Evidence — do not mention it to explain exclusions, ownership, or sequencing. `## Code Changes` and `## Evidence` follow the formats in [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md); `## Change Requests` links the change requests this run raised (format in [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md)).

`## Inputs` makes the artifact usable by a later workflow without embedding the UI Map documentation. Record exact paths to the target map, the architecture artifact when one exists, [`ui-map-implementation.md`](ui-map-implementation.md), the selected platform guide, the placeholder guide whenever placeholder work is in scope during Audit, Plan, or Build, and any project-conventions document actually used. A consumer loads those references before acting on the artifact.

## Gates and control flow

Gate lines:

- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

At a planned gate, first reread the implementation artifact and remove any reference to separate-session work from Goal, Audit, Discussion, Code Changes, Change Requests, and Evidence; those sections record only UI Map conformance. Then summarize what you did and what happens next, end with the gate line, STOP and wait.

**Planned gates** — `next` advances:

- Discussion complete — emitted when every `- [ ]` discussion item is resolved (`- [x]`) and no change request is open. Advances to Code Changes.
- Code Changes ready — the human reviews the spec. `next` executes the unchecked items this mode owns (the *Implement* stage): in **Plan**, when a proposed map exists, the only executable item is the terminal promote item, so `next` promotes, checks that item, and completes; without a proposed map, `next` completes with the official map unchanged. In **Build**, `next` runs and checks the `implement` / `placeholder` items — scaffolds and mechanical conformance, the green build, then the promote when one exists — to completion, or a blocked gate if any `handoff` item remains unchecked.

**Completion** — when the run carries a map change, both modes end by performing and checking the terminal promote item, then `🏁` (Plan right after the Code Changes gate; Build once the scaffolds build green). Without a map change, they complete with the official map unchanged. A Build still holding unchecked `handoff` items ends at a blocked gate first (see *Completion*).

**Blocked gates** — emitted when the agent cannot advance. Common reasons:

- Discussion in progress: one or more `- [ ]` items remain unresolved.
- The map (proposed or official) is missing, invalid, or not identifiable; or the codebase is missing.
- A change request is open — the proposed map must change before Code Changes can be written: `⏳ GATE: Blocked: change request <id> is open. Update the map, then say "next" to re-audit.`
- Build/render commands or overrides are missing or broken (for rendering, only when an override is broken or the SKAI default cannot run).
- A build failure points at a map flaw, requirement conflict, or project constraint rather than a clear local fix.
- UI Map conformance cannot proceed without feature content beyond placeholder/navigation work.
- Ambiguity: a finding or task cannot be interpreted without human or architecture input.

The human resolves the cause (resolves items, fixes inputs, updates the package); the agent re-evaluates and emits the appropriate gate on the next response.

**Advance intent** moves past a planned gate. Signals: "next", "continue", "go ahead", "do it"; recognized only after a `⏳ GATE:` line. Deliverables named in the initiating request (e.g. "implement the UI map") are not advance intent and never skip Discussion. "we should..." / "let's..." is discussion, not authorization. `auto` bypasses planned gates only — never a blocked gate. `auto to <milestone>` stops before a named gate (`discussion complete`, `code changes ready`).

## Audit

On initiation, load the required inputs, infer the Mode from context (see *Run mode*), and create the implementation artifact. Then run the scoped audit: compare the codebase to the **target map** — the proposed map when a change package exists, otherwise the official map. The audit is exhaustive within its reach: inspect every applicable scene and route in scope, deriving and checking its expected identity and canonical home before declaring conformance.

The request and change package set the audit's reach. When a package exists, its `## Map Changes` is the spine: a baseline audits the whole codebase against the whole proposed map; a scoped change audits only the affected subset. Architecture `## Deferrals` are context about intentionally postponed map work, not implementation findings or `T#` sources; include work only when the current target-map/code audit independently yields a conformance finding. A no-package conformance request audits the scope named by the request against the official map. Do not expand into a general cleanup audit unless the human explicitly requests it. If you discover a deviation outside that reach, surface it to session orchestration rather than adding it to this artifact; include it only after the human explicitly expands the run's scope.

The audit surfaces two kinds of gap: **code that deviates** from the target map, and **map scenes with no code yet** (scaffolding). Three starting conditions shape what it finds:

1. **New app** — no existing scene or route code to compare; every scene/route finding is new scaffolding. Still inspect project and target metadata required by the loaded guidance before recording setup work.
2. **Existing app already following a supported UI Map implementation guide** — findings are mostly mechanical (moves, renames, route wiring).
3. **Existing app not yet following one (brownfield)** — the extreme of (2): most conformance is real refactoring, not mechanical. Expect a migration backlog (`handoff` items + a mechanical slice + change requests), not a one-pass green build.

### What to compare

Compare code against the target map for:

- Scenes present in scope for the selected app platform (`platform` omitted or matching), including applicable map scenes with no code yet.
- Route kinds and presentation mechanics.
- Modal styles and project-specific presentation overrides.
- Scene/domain identity and code names: derive each in-scope scene's expected code identity from its map ID and the selected platform convention, then compare it to the actual code; labels or equivalent behavior do not substitute for the mapped identity.
- Canonical folder organization and file layout: derive each scene's expected home from the map and the selected platform or project convention, then compare it to the actual files.
- Placeholder-scene boundaries for newly scaffolded map scenes.
- Platform patterns called out by the selected platform convention guide.

Read a route's kind and modal style from the modifier or host it is actually bound to, not from an enum's name. For example, a route enum named `MessageRoute` is still modal if it is bound to `.sheet(item:)`.

Findings are observed deviations only. Inspect the relevant code and project metadata; do not record a guide-required ingredient that is already present or enumerate conforming scenes. Keep each architecture source's stated operation separate from additional deviations observed at the same implementation site: an `M#` or `D#` covers only the operation it states, while any other deviation is an independent audit finding and cannot broaden or reclassify that source.

### Finding disposition

Each finding gets one of three dispositions, in order — do it, else stop, and request a map change only as a last resort:

Before assigning a disposition, confirm that the map plus the loaded platform and project guidance define a concrete, verifiable conforming outcome. If required guidance is missing or a map value has no defined code mapping, STOP in Discussion at a blocked gate before writing Code Changes; ask for the missing decision or mapping. Do not turn an unknown outcome into a `handoff`. If the problem is instead that the target map itself is wrong or infeasible, use **Request change** below.

1. **Implement** — a mechanical fix or a placeholder scaffold the skill does itself; becomes a `T#` code-change item. Mechanical changes default here: placeholder scaffolds for new scenes in scope; file/folder moves that mirror the target map's domains; renames that align scene IDs and code names; route enum or route-host placement that follows the platform convention guide; missing imports or simple local compile fixes caused by these.
2. **Hand off** — a concrete, verifiable non-mechanical change outside UI Map implementation ownership that directly affects conformance: the required outcome is already defined, but another workflow, skill, person, or PR must do the work → an unchecked `handoff` `T#`. In Build this stops the run at a blocked gate; in Plan it is part of the spec. Examples: rewriting existing runtime behavior, refactoring cross-cutting navigation infrastructure, or changing established project conventions to an already-defined pattern. A scene newly added by the active proposed map is UI-map-owned placeholder work in Build or `planned` work in Plan. A pre-existing official-map scene with no code in a shipped or brownfield app is a `handoff` unless the active request explicitly scopes it as new scaffold work. Unrelated feature work elsewhere in the session is not a finding and does not belong in this artifact.
3. **Request change** — only when the target **map itself** must change (a clear flaw, infeasible as specified, a poor decision worth revisiting). The skill never edits the map, so it proposes a change request in Discussion and, only after explicit approval, raises the request and blocks its own Code Changes until the map is updated — the heaviest stop, so prefer a blocked gate or handoff unless the map is genuinely at fault or the human directs it.

The implement/handoff line is the mechanical/non-mechanical line for work that affects UI Map conformance **after the conforming outcome is known**. A brownfield case may produce `handoff` items plus a mechanical slice, so a Build lands that thin slice and then blocks at completion on the unchecked handoff remainder. The audit's mix of dispositions does not reclassify the run: `Mode` remains the ownership scope inferred at initiation.

## Discussion

Findings that need a **decision** are resolved here, mirroring the architecture skill's discussion. A finding whose disposition is already clear needs no discussion item — it goes straight into Code Changes when that stage runs: a UI-map-owned finding as `implement`/`placeholder` in Build or `planned` in Plan, and a **clear-cut handoff as `handoff`** (the human weighs in on handoff work at the completion blocked gate, so a plainly non-mechanical handoff does not also need discussing first). Reserve Discussion for genuine decisions: a `[Question]` with no default, including a missing required guide/project mapping; a `[Tradeoff]`; an ambiguous implement-vs-handoff call; or a finding that the map itself is wrong (decision: raise a change request). A missing mapping remains an open Discussion item and blocks Code Changes until the human or owning authority supplies it. So a new-app baseline, or a run whose only non-mechanical findings are clear-cut handoffs, often leaves Discussion empty.

### Item format

Discussion items are `D#`, whether the decision comes from an audit finding or an implementation choice. Each item line is `- [ ] <id> [Kind] <summary>`, with Kind one of:

- `[Question]` — needs the human's input; the agent has no basis to recommend. Rare: propose a default whenever there is one.
- `[Proposal]` — the agent recommends a course of action; the human accepts, rejects, or modifies.
- `[Tradeoff]` — two or more options plus the agent's recommended pick and why. Never a neutral menu.

A finding that the *map* itself is wrong is not a separate Kind: it is an ordinary `[Proposal]` / `[Tradeoff]` whose recommended action — and `Decision` — is to raise a change request (see *Raising a change request* below).

Sub-bullet labels are **bold** with no separator after: `Concern` always, then either `Proposal` or `Question`; `Options` for a Tradeoff; `Detail` when helpful; `Why` for the rationale; `Decision` added on resolution. On the human's explicit approval, check the box (`- [x]`) and append `- **Decision** <succinct resolution>.`. Keep sibling items tight: no blank lines between `- [ ]` items under one heading.

### Organization and gate

Use topic sections that reflect the code or map area, not aggregator sections. A finding belongs where its reasoning is easiest to review; one whose proposed resolution is a change request stays here until the human explicitly approves it.

### Raising a change request

When the human explicitly approves a Discussion decision to request a map change, check that `D#`, append its Decision, then immediately write one markdown file at `skai/changes/<change-id>/change-requests/ui-map-<nnn>.md` and link it under the implementation artifact's `## Change Requests`. Use the format in [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md): `Change Request Status: Proposed`, a `Reviewer Response`, and the concern and requested map change. Number from `ui-map-001.md`.

Do not create the request while its `D#` is unresolved, and do not enter or populate `## Code Changes` after creating it. Emit the change-request blocked gate immediately; the run resumes and re-audits only after architecture updates the map and no change request remains open.

After drafting, and after each response, STOP at a gate: a blocked gate if any `- [ ]` items remain (or a change request is open), or the discussion-complete planned gate if none do — every item `- [x]`, or the audit raised nothing that needs a decision (an all-mechanical run, or one whose only non-mechanical findings are clear-cut handoffs).

`⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Code Changes.`
`⏳ GATE: Next: Discussion complete. Say "next" to write Code Changes.`

## Code Changes

Only after the discussion-complete gate advances with no open change request, translate the resolved audit into `## Code Changes` (`T#` items). `## Code Changes` is the durable conformance checklist: checkboxes show what is complete, while Disposition shows whether each item is UI Map implementation work (`implement` / `placeholder`), UI-map-owned work reserved for a larger Plan (`planned`), or directly relevant work owned elsewhere (`handoff`). When the run has a proposed map (a change package), the list ends with a terminal **promote** item (below); a conformance run against the official map has no map change to promote, so it has none.

### Code change items

Write `T#` items in the format defined in [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md): an unchecked checkbox, a stable `T#` ID, an identity, **Description**, **Disposition** (`implement` / `placeholder` / `planned` / `handoff`), **Realizes** (what this item carries out), and **Touches**. Build the list from the audit's already-separated sources: create one item for each applicable `M#` or `D#`, then one for each independent audit finding without an ID. Implementation overlap does not merge sources. Keep all operations from one source under the same checkbox; terminal promotion is the whole-change exception. Before the gate, read the sources back against the drafted items: each source has exactly one item, and that item's Description carries every operation from the source. There is no `Status` or `Type` field — the checkbox carries completion and the identity and Description convey the kind. Write items top-down in structural order.

After separating the sources, assign each item's Disposition independently from ownership and mode; it never changes when an item is checked. In **Plan** mode, UI-map-owned code items are `planned` (the larger effort implements them) and directly relevant work owned elsewhere is `handoff`; the terminal promote item is `implement`. In **Build** mode, UI-map-owned mechanical work is `implement`, placeholder scaffolding is `placeholder`, and directly relevant work owned elsewhere is `handoff`. A `planned` or `handoff` item Description must explain what remains, why this run is not doing it, and the relevant UI Map/platform guidance the receiving workflow should preserve. Common change kinds and the disposition the principle yields — a coverage checklist, not a field on each item:

| Change kind | What it covers | Build disposition | Plan disposition |
|---|---|---|---|
| `folder-org` | folders mirror the map's domains | `implement`, or `handoff` if non-mechanical | `planned`, or `handoff` if non-mechanical |
| `file-layout` | a scene's files sit at its canonical home | `implement`, or `handoff` if non-mechanical | `planned`, or `handoff` if non-mechanical |
| `naming` | code names match the map's scene ids / types | `implement`, or `handoff` if non-mechanical | `planned`, or `handoff` if non-mechanical |
| `route-kind` | an existing route's presentation matches the map | `implement`, or `handoff` if non-mechanical | `planned`, or `handoff` if non-mechanical |
| `platform-pattern` | code follows the platform reference's conventions | `implement`, or `handoff` if non-mechanical | `planned`, or `handoff` if non-mechanical |
| `scene-attribute` | a scene attribute changed in the map (e.g. `modal_style`) | `implement`, or `handoff` if non-mechanical | `planned`, or `handoff` if non-mechanical |
| `scaffold-scene` | scaffold a placeholder for a new map scene | `placeholder` | `planned` |
| `wire-route` | wire a new route | `placeholder` | `planned` |
| `remove` | the map dropped an element → delete its code | `implement` | `planned` |

A change not in the table still gets its disposition from the same principle — apply the `implement` / `placeholder` / `planned` / `handoff` definitions in [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md) to the change at hand.

**Routes aren't special.** The skill wires route *structure*, not new feature data. In Build, a **new route** is `placeholder`: a new destination receives no feature inputs, while an existing destination keeps its inspectable input contract when the project already defines the required value sources; if a required source is undefined, stop in Discussion under the platform placeholder guide's missing-input rule. A **mechanical kind change** on an already-wired route (e.g. nav → modal) is `implement`. In Plan, the same UI-map-owned route work is `planned`. A **real route refactor** is `handoff`.

**The terminal promote item.** The last `T#` is the promotion: copy the proposed YAML to `skai/ui-map/ui-map.yaml`, then run the project render override or the SKAI default renderer against that **official YAML**, targeting `skai/ui-map/ui-map.svg`. Do not copy the proposed SVG; it is derived preview output. Require renderer exit 0 and a nonempty official SVG, and record the render command and result in `## Evidence`. Only then check the promote item. Its Disposition is always `implement`, never `planned` or `handoff`, and it runs last: in Build after the scaffolds build green, in Plan right at the Code Changes gate (the spec review is the sign-off). It isn't literally a code change; modeling it as a `T#` folds promotion into the normal execution flow, with no separate promotion step. Author it with **Realizes** = the approved change as a whole (not a single `M#`) and **Touches** = the official map and its render.

This item exists only when there is a proposed map to promote. In a conformance run with **no change package** — code conformed to the official map, which does not change — there is nothing to promote: omit the promote item, leave the official map and its render untouched, and end at green build (Build) or the approved spec (Plan).

### Code Changes gate

When Code Changes is ready, summarize the artifact path, item count by disposition, the change-request links, and the Evidence plan. Then STOP:

`⏳ GATE: Next: Code Changes ready. Review it, then say "next" to implement. Or say what to change.`

On advance intent, proceed to *Implement*. In **Plan** mode the only executable item, when a proposed map exists, is the terminal promote; perform and check it, then complete. Without a proposed map, complete with the official map unchanged. In **Build** mode, execute unchecked `implement` / `placeholder` items and block if any `handoff` item remains unchecked.

## Implement

Execute the unchecked `## Code Changes` items this mode owns, top-down. In **Plan** mode, go straight to *Completion*: execute the terminal promote only when one exists. In **Build** mode, work the `implement` / `placeholder` scaffold and mechanical items below (each a single typed unit of work), then verify and complete. On resume, do not redo checked items unless the audit shows they have regressed.

Per item:

1. Read the item. **Description** is what to do; **Realizes** anchors why; **Touches** lists the files/paths affected.
2. Apply the change. `planned` and `handoff` items are not built here.
3. If a mechanical glitch surfaces, fix it inline when allowed below.
4. If anything else surfaces — map mismatch, structural mismatch, ambiguity, a directly blocking feature dependency, project constraint — STOP at a blocked gate.
5. After verifying that every operation in the item's Description is true in code or artifact state, check the item (`- [x]`) without changing its Disposition and proceed.

On resume, re-audit every unchecked `handoff` item. If external work has made the described code conform, check that same `T#` item and preserve `Disposition: handoff`; if it still does not conform, leave it unchecked and remain blocked. The same completion rule applies when another workflow implements a `planned` item: check it, but preserve `Disposition: planned`.

**Placeholder shape.** The exact placeholder shape is platform-specific — load the matching reference: [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md) for the `SKAISwiftUI` API, per-route-kind scaffold patterns, the NavigationStack-at-the-presentation-boundary rule, dismiss/breadcrumb behavior, the real-screen entry trigger, and the new-scene no-inputs rule; [`ui-map-compose-placeholders.md`](ui-map-compose-placeholders.md) for the placeholder library API and matching patterns.

**Moving files.** When an item relocates tracked files, use `git mv` to preserve history. Use plain `mv` only for untracked files.

**Scaffold markers.** Every scaffold site carries a greppable in-code marker — a `🟡` comment stamped with the change-id (e.g. `// 🟡 UI Map scaffold <change-id>`): one file-level marker on a new placeholder file, one marker per injected block in an existing real file (a real-screen entry trigger, route registration in a real nav host). The `🟡` visually flags placeholder code; the change-id lets a later productionization pass grep all of one change's scaffold sites. This skill does **not** remove these at its own completion — they are the handoff for productionizing the placeholders (invariant: no markers left for a change-id = fully productionized). Exact marker syntax lives in the placeholder reference.

**Reaching a new scene from an existing real screen.** When the selected placeholder guide or project conventions define this mapping, a `wire-route` item registers the destination on the real nav host and adds the defined temporary entry trigger so the skeleton is click-through-able; both injected blocks carry the change-id scaffold marker. If no trigger mapping is available, STOP in Discussion before writing Code Changes under *Finding disposition*; do not hand-roll or omit it.

**Chunk boundaries.** At the end of each domain or natural chunk for large change sets, run the project's build command from `skai/integration.md`. Record the result inline in `## Evidence`:

```
[evidence: <command>; exit <code>; output: <path if persisted>]
```

On success, linked output is optional; still record command + exit code. On failure, persist full output to `skai/changes/<change-id>/evidence/<file>` and link it. If the failure is a fixable local glitch, fix and rebuild; if it points at a needed change request, requirement conflict, or map flaw, STOP at a blocked gate.

### Auto-fixes allowed

These do not require a STOP: obvious typos in identifiers; missing imports; simple compilation errors with a clear, local fix caused by the current item; local formatting required by the project formatter.

### Never auto-fix

STOP at a blocked gate for:

- Anything that requires editing the map (raise a change request instead).
- Removing, weakening, or reordering `T#` items beyond what Code Changes permits.
- Choosing a different route kind, modal style, or scene identity than the target map specifies.
- Adding feature content to a UI-map-owned structural item. Keep separable feature work out of this artifact; block only when the structural work cannot proceed without it.
- Changing project conventions.
- Substituting an undocumented workaround to force a green build.

## Verification

Verification is the agent's automated build — a green build conforming to the target map is the deliverable:

- **Every successful Build run performs a fresh completion build during the current run**, even when the audit finds no changes to make. Append a new evidence bracket for that invocation; do not infer build health from an empty change list or satisfy current-run evidence by relying on, replacing, or overwriting a prior run's evidence.
- **Agent runs additional automated verification** at chunk boundaries as needed: build/compile, platform-specific checks, and any project-specific automated checks from `skai/integration.md`.
- **Agent may render the proposed map** when validating it helps. Promotion **must** render the official YAML directly to the official SVG and record successful evidence. Use a project-specific override when one exists; otherwise use the SKAI default renderer from [`ui-map-guide.md`](ui-map-guide.md). Rendering validates the map target; it does not authorize editing it.

Click-through QA — running the app to confirm navigation behaves as specified — is downstream of this skill, not a gate it waits on; the placeholder boundary keeps each scaffolded scene visibly identifiable so QA can confirm routes later. If a navigation issue surfaces, handle it like any finding: propose the smallest guide-faithful fix, raising a change request if it requires changing the target map.

## Completion

When the run has a proposed map, completing means performing and checking the terminal promote item — copy the proposed YAML to the official YAML, successfully regenerate the official SVG from that official YAML, and record the render evidence, so the change is now the official architecture — then emit `🏁`.

**Plan** completes right after the Code Changes gate (the spec review was the sign-off): when a proposed map exists, perform and check the promote; otherwise leave the official map unchanged. Leave `planned` and `handoff` items unchecked and finish — the spec is the deliverable.

- With a proposed map: `🏁 Complete. The UI Map implementation plan is ready; the official map is promoted.`
- Without a proposed map: `🏁 Complete. The UI Map implementation plan is ready; the official map is unchanged.`

**Build** completes once the fresh completion build is green and no `handoff` item remains unchecked: when a proposed map exists, perform and check the promote; otherwise leave the official map unchanged. Then finish.

- With a proposed map: `🏁 Complete. The UI Map implementation is done; the official map is promoted.`
- Without a proposed map: `🏁 Complete. The app conforms to the official UI Map; no map change to promote.`

**A Build with unchecked `handoff` items does not complete.** It ends at a blocked gate reporting what was checked, what remains unchecked, and why UI Map implementation does not own it, and holds the promote when one exists — the promote is the last item, so the run stops before it. Whoever continues the Build — this session, or a later one reading the artifact's `Mode` — resolves the handoff work, re-audits, checks the same item without changing its Disposition, then the effort completes.

`⏳ GATE: Blocked: <N> item(s) handoff — <reason>. Resolve and say "next" to continue.`

**Conformance (no change package)** has no map to promote; it finishes through the applicable Plan or Build branch above, with the official map left untouched.
