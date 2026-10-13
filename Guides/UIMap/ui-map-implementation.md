Managed-By: skai
Managed-Id: guide.ui-map-implementation
Managed-Source: Guides/UIMap/ui-map-implementation.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-13

# UI Map Implementation

Before using this guide, complete [Project addendum](#project-addendum) loading below.

The implementation method for the UI Map system. It executes or specifies the code work needed to conform to an approved map and promotes an approved proposed map when one exists. Use [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md) for the code-change and evidence formats this skill produces, [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md) for the map-change items it consumes and the change requests it raises, and [`ui-map-guide.md`](ui-map-guide.md) for the YAML map.

For platform-specific code conventions, load [`ui-map-swiftui.md`](ui-map-swiftui.md) for iOS/SwiftUI or [`ui-map-compose.md`](ui-map-compose.md) for Android/Compose. For placeholder scaffolding, load [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md) or [`ui-map-compose-placeholders.md`](ui-map-compose-placeholders.md) for the matching stack.

## Purpose

Implementation makes app code conform to an approved UI Map architecture or records the conformance work for a larger effort, then advances the official map when a proposed map exists. The system keeps two map files:

- **Official map** — `skai/ui-map/ui-map.yaml`, the approved architecture authority; frozen while a proposed change is under review.
- **Proposed map** — `skai/changes/<change-id>/ui-map/proposed-ui-map.yaml`, the architecture the change moves toward.

When a proposed map exists, implementation works against it, then **promotes** it after the Code Changes spec is approved: copy the proposed YAML to the official YAML, then regenerate the official HTML page from that official YAML, so the approved architecture advances. The proposed HTML page is a preview, not a promotion source. In Build this follows a green conforming build. In Plan the approved map intentionally leads the unchecked implementation work recorded in the artifact. Promotion and archival are the final UI Map implementation step of every run that changes the map; a no-package conformance run works against and leaves the official map unchanged.

**Invariant — the map leads, code follows.** The target map is the architecture authority. Implementation may scaffold, align, move, rename, hand off, block, or raise a **change request** back to architecture — but it never edits map content to justify code. When the map itself is wrong or infeasible, raise a change request; when the skill simply can't do a change mechanically, hand it off or stop at a blocked gate (see *Code Changes*).

**Invariant — structure, not features.** Implementation changes and creates *structure* — scaffolding new scenes, wiring routes, moving, renaming, aligning code to the platform conventions — but never *feature content*: no business logic, no real UI, no data beyond placeholder labels. A scene it scaffolds is a minimal placeholder that compiles, routes correctly, and is visibly identifiable in the running app.

This workflow is one part of a larger agent session, not the system of record for every task in that session. Keep unrelated feature, bug, and product work out of the UI Map implementation artifact, including disclaimers that label it excluded or outside scope; session orchestration or that work's own skill and artifacts own it. If such work appears alongside a UI Map request, complete the separable UI-map-owned work through `🏁` before session orchestration starts the unrelated work, even when both happen in the same overall agent turn. Record `handoff` only when external work directly affects UI Map conformance or reconciliation. Block only when the UI Map work itself cannot proceed without that work or an external decision.

Implementation runs in four stages:

1. **Audit** — compare the codebase to the target map within the run's scope.
2. **Discussion** — resolve the audit findings that genuinely need a decision.
3. **Code Changes** — write the checklisted, disposition-coded code-change items, ending with a terminal promote item when a proposed map exists.
4. **Implement** — execute the items this mode owns and, when applicable, end by promoting the proposed map.

## Run mode

For a new artifact the skill **infers** its run mode from context at initiation; a resumed run reads and preserves its recorded Mode and records it in the artifact's `Mode` field, which **travels with the artifact** — so any session that picks up the work knows the intent. The mode is the scope of the job:

- **Plan** — inferred when a larger feature, bug-fix, or refactor workflow will own the **same structural conformance work**. This skill produces the conformance spec only: UI-map-owned code items are unchecked `planned`; directly relevant work owned elsewhere is unchecked `handoff`; when a proposed map exists, it performs and checks the terminal promote, then completes.
- **Build** — inferred when UI Map implementation owns the structural conformance work. The skill implements and checks UI-map-owned `implement` and `placeholder` work — scaffold placeholders, wire routes, move/rename to conform, build green, then promote when a proposed map exists — delivering a reachable, navigable skeleton. Unchecked `handoff` items block Build completion/promotion until the owning workflow resolves them and the run can resume. Build does not imply scaffolding, and unrelated tasks elsewhere in the same session do not turn a Build into Plan.

## Inputs

Required:

Resolve the map repository from the project's README or established map location. `skai/ui-map/` and `skai/changes/`, including this workflow's artifact, are relative to that repository. App-code paths, build/test commands, and `skai/integration.md` remain relative to the app repo. If the map repository is unknown or ambiguous, STOP at a blocked gate before auditing or writing.

- The target map: when an architecture change package exists at `skai/changes/<change-id>/ui-map/`, its proposed map (`proposed-ui-map.yaml`), render, and architecture artifact (`ui-map-architecture.md`) with `## Map Changes`; otherwise the official map for a no-package conformance run. For an unexecuted proposal, a package is ready when Discussion is resolved, no request remains `Proposed`, and the proposed
YAML, nonempty render and Map Changes are present. Recompute the difference against the **current**
official map: every difference must have a matching Map Changes item and every item must still
match. A mismatch returns to architecture's reopen procedure; implementation never merges or edits
the proposal itself.
- The official map `skai/ui-map/ui-map.yaml`, the frozen baseline the change is measured against. (For a baseline there is none yet.)
- The app codebase.
- The platform convention guide: [`ui-map-swiftui.md`](ui-map-swiftui.md) for iOS/SwiftUI or [`ui-map-compose.md`](ui-map-compose.md) for Android/Compose.
- The matching placeholder guide whenever placeholder work is in scope during Audit, Plan, or Build: [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md) or [`ui-map-compose-placeholders.md`](ui-map-compose-placeholders.md). Omit it only when no placeholder work is in scope.
- The artifact-format references: [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md) (code-change items + evidence this skill writes) and [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md) (map-change items it reads, change requests it raises).
- `skai/integration.md` for build/test commands, render overrides, and evidence paths. Do not invent project-specific commands; for rendering, use the SKAI default from [`ui-map-guide.md`](ui-map-guide.md) when no override exists.
Expected when available:

- The project's `README.md` or equivalent project-conventions doc for overrides such as modal styles, route wrappers, folder layout, or view-model conventions. Standard guide-covered patterns do not require one.
- Scoped architecture/change collateral for the active story, and the active upstream requirement/story/bug scope.

If no change package is present, conform code to the official `skai/ui-map/ui-map.yaml` as the frozen source of truth (the map is unchanged); a missing architecture artifact is not a blocker when the map and codebase are present. If the map (proposed or official) is missing, invalid, or not identifiable, STOP with a blocked gate (see *Gates*). Discover proposed maps only under `skai/changes/*/ui-map/`; sibling types and promoted packages
are not active targets. A checked terminal promote item is closed. A recorded successful official
write/render with incomplete archival resumes *Archive the package* only. A recorded YAML write
with an incomplete official render instead follows *Promotion progress and restart* below; do not
apply the unexecuted-proposal diff screen to its own partial write. Fully archived packages are not
promoted again. Multiple plausible change packages
with no named target make the map not identifiable; do not choose one. If the app codebase is not present, STOP with a blocked gate.

## Implementation artifact

For a new change-package run, create the implementation artifact parallel to the architecture
artifact: `skai/changes/<change-id>/ui-map/ui-map-implementation.md`. Use the package's ID. The
`ui-map/` folder owns this artifact, its requests and evidence; related requirements work is separate.
On resume reuse the existing artifact and its Mode, IDs, decisions, Evidence and valid completion states. After promotion the same artifact is at `skai/promoted/<change-id>/ui-map/ui-map-implementation.md`.
Receiving workflows execute and check any pending Plan work there without reopening or re-promoting
the map proposal. When this skill is invoked on an already-promoted Plan, retain the recorded Mode,
items and evidence and hand off that plan at its archived path; do not create another package or
terminal promote item. If resuming such work, verify current code against the current official map rather
than assuming the archived preview remains current canon.

Without a proposed map, create no change package. Put the conformance artifact in the map repository
at `skai/working-docs/<branch-path>/<session-name>/ui-map-implementation.md`, using
[`working-doc-conventions.md`](../Core/working-doc-conventions.md). Determine the branch in that
repository and resolve a short session name from the request; if unclear, propose one and wait at a
blocked gate before creating the artifact. Requests and evidence belong beside that artifact.

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

At a planned gate, first reread the implementation artifact and remove any reference to separate-session work from Goal, Audit, Discussion, Code Changes, Change Requests, and Evidence; those sections record only UI Map conformance. Then summarize what you did and what happens next, end with the gate line, STOP and wait.

**Planned gates** — `next` advances:

- Discussion complete — emitted when every `- [ ]` discussion item is resolved (`- [x]`) and no change request is open. Advances to Code Changes.
- Code Changes ready — the supervisor reviews the spec. `next` executes the unchecked items this mode owns (the *Implement* stage): in **Plan**, when a proposed map exists, the only executable item is the terminal promote item, so `next` promotes, checks that item, and completes; without a proposed map, `next` completes with the official map unchanged. In **Build**, `next` runs and checks the `implement` / `placeholder` items — scaffolds and mechanical conformance, the green build, then the promote when one exists — to completion, or a blocked gate if any `handoff` item remains unchecked.

**Completion** — when the run carries a map change, both modes end by performing and checking the terminal promote item, then `🏁` (Plan right after the Code Changes gate; Build once the scaffolds build green). Without a map change, they complete with the official map unchanged. A Build still holding unchecked `handoff` items ends at a blocked gate first (see *Completion*).

**Blocked gates** — emitted when the agent cannot advance. Common reasons:

- Discussion in progress: one or more `- [ ]` items remain unresolved.
- The map (proposed or official) is missing, invalid, or not identifiable; or the codebase is missing.
- A change request is open — the proposed map must change before Code Changes can be written: `⏳ GATE: Blocked: change request <id> is open. Update the map, then say "next" to re-audit.`
- The archive destination collides, a required reference cannot be accessed/repaired, or archival
  fails after successful official-map write/render. Resume archival only; never repeat that successful
  canonical promotion solely to finish a move.
- Build/render commands or overrides are missing or broken (for rendering, only when an override is broken or the SKAI default cannot run).
- A build failure points at a map flaw, requirement conflict, or project constraint rather than a clear local fix.
- UI Map conformance cannot proceed without feature content beyond placeholder/navigation work.
- Ambiguity: a finding or task cannot be interpreted without supervisor or architecture input.

The supervisor resolves the cause (resolves items, fixes inputs, updates the package); the agent re-evaluates and emits the appropriate gate on the next response.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs: work specs, planning docs, working docs, retro outputs, ticket drafts, etc.). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** (test code, application code) seeded or planned by a skai workflow. Completion is **removal** of the marker — the file's remaining work is read by which `🟡`s remain. Canonical in-code case: `Guides/Test/unit-test-planning-guide.md`.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers (`- [ ]` → `- [x]` in a process artifact; remove `🟡` in code) only after the supervisor gives advance intent.
- If a workflow needs a custom marker lifecycle (for example, inline discussion items resolved during a supervisor-led discussion loop), define that exception explicitly and narrowly below.
- If a workflow uses both gate/phase markers and local working markers, keep them distinct: local approvals clear local working markers; advance intent clears the gate/phase marker.
- For any custom marker lifecycle, specify both:
  - the artifact where the markers live
  - the exact supervisor intent that authorizes clearing them

**Not workflow progress:** the `🟡` convention in `Templates/docs/skai/integration.md` and `Install/integration-doc-install-update.md` (project-specific missing constants needing supervisor input during host install) is a separate concept, scoped to that section's rules. Don't conflate the two.

Workflow-specific advance behavior: the initiating request does not skip Discussion. Bounded-auto
milestones are `discussion complete` and `code changes ready`.

Workflow-specific marker lifecycle: Discussion `D#` items are local working markers, checked with
Decisions only on supervisor approval. Their resolved record remains at the Discussion complete
gate; advance intent approves writing Code Changes. The unchecked `T#` items persist through the
Code Changes ready gate. Advance intent approves execution; check each item only after its owned
operations and evidence succeed. Plan leaves `planned` and `handoff` items unchecked. The terminal
promote item includes archival and is checked only at the promoted location after archival succeeds.

## Audit

On initiation load required inputs. Create an artifact and infer Mode only for new work; otherwise
read its recorded Mode and progress. Recorded terminal-write progress dispatches directly to
*Promotion progress and restart*, without recreating Audit/Code Changes. Otherwise re-audit the
existing artifact, preserving its IDs, decisions, Evidence and still-valid verified completions.
Run the scoped audit: compare the codebase to the **target map** — the proposed map when a change package exists, otherwise the official map. The audit is exhaustive within its reach: inspect every applicable scene and route in scope, deriving and checking its expected identity and canonical home before declaring conformance.

The request and change package set the audit's reach. When a package exists, its `## Map Changes` is the spine: a baseline audits the whole codebase against the whole proposed map; a scoped change audits only the affected subset. Architecture `## Deferrals` are context about intentionally postponed map work, not implementation findings or `T#` sources; include work only when the current target-map/code audit independently yields a conformance finding. A no-package conformance request audits the scope named by the request against the official map. Do not expand into a general cleanup audit unless the supervisor explicitly requests it. If you discover a deviation outside that reach, surface it to session orchestration rather than adding it to this artifact; include it only after the supervisor explicitly expands the run's scope.

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
3. **Request change** — only when the target **map itself** must change (a clear flaw, infeasible as specified, a poor decision worth revisiting). The skill never edits the map, so it proposes a change request in Discussion and, only after explicit approval, raises the request and blocks its own Code Changes until the map is updated — the heaviest stop, so prefer a blocked gate or handoff unless the map is genuinely at fault or the supervisor directs it.

The implement/handoff line is the mechanical/non-mechanical line for work that affects UI Map conformance **after the conforming outcome is known**. A brownfield case may produce `handoff` items plus a mechanical slice, so a Build lands that thin slice and then blocks at completion on the unchecked handoff remainder. The audit's mix of dispositions does not reclassify the run: `Mode` remains the ownership scope inferred at initiation.

## Discussion

Findings that need a **decision** are resolved here, mirroring the architecture skill's discussion. A finding whose disposition is already clear needs no discussion item — it goes straight into Code Changes when that stage runs: a UI-map-owned finding as `implement`/`placeholder` in Build or `planned` in Plan, and a **clear-cut handoff as `handoff`** (the supervisor weighs in on handoff work at the completion blocked gate, so a plainly non-mechanical handoff does not also need discussing first). Reserve Discussion for genuine decisions: a `[Question]` with no default, including a missing required guide/project mapping; a `[Tradeoff]`; an ambiguous implement-vs-handoff call; or a finding that the map itself is wrong (decision: raise a change request). A missing mapping remains an open Discussion item and blocks Code Changes until the supervisor or owning authority supplies it. So a new-app baseline, or a run whose only non-mechanical findings are clear-cut handoffs, often leaves Discussion empty.

### Item format

Discussion items are `D#`, whether the decision comes from an audit finding or an implementation choice. Each item line is `- [ ] <id> [Kind] <summary>`, with Kind one of:

- `[Question]` — needs the supervisor's input; the agent has no basis to recommend. Rare: propose a default whenever there is one.
- `[Proposal]` — the agent recommends a course of action; the supervisor accepts, rejects, or modifies.
- `[Tradeoff]` — two or more options plus the agent's recommended pick and why. Never a neutral menu.

A finding that the *map* itself is wrong is not a separate Kind: it is an ordinary `[Proposal]` / `[Tradeoff]` whose recommended action — and `Decision` — is to raise a change request (see *Raising a change request* below).

Sub-bullet labels are **bold** with no separator after: `Concern` always, then either `Proposal` or `Question`; `Options` for a Tradeoff; `Detail` when helpful; `Why` for the rationale; `Decision` added on resolution. On the supervisor's explicit approval, check the box (`- [x]`) and append `- **Decision** <succinct resolution>.`. Keep sibling items tight: no blank lines between `- [ ]` items under one heading.

### Organization and gate

Use topic sections that reflect the code or map area, not aggregator sections. A finding belongs where its reasoning is easiest to review; one whose proposed resolution is a change request stays here until the supervisor explicitly approves it.

### Raising a change request

When the supervisor explicitly approves a Discussion decision to request a map change, check that
`D#` and append its Decision. In a no-package conformance run, resolve a new change ID using the
architecture guide's rules and check its active/promoted UI Map paths. Seed that type folder and
move the conformance artifact, requests and evidence into it, repairing links and preserving the
review history; a collision blocks rather than overwrites. The run now awaits architecture's proposed
map. Then immediately write one markdown file at `skai/changes/<change-id>/ui-map/change-requests/ui-map-<nnn>.md` and link it under the implementation artifact's `## Change Requests`. Use the format in [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md): `Change Request Status: Proposed`, a `Reviewer Response`, and the concern and requested map change. Number from `ui-map-001.md`.

Do not create the request while its `D#` is unresolved, and do not enter or populate `## Code Changes` after creating it. Emit the change-request blocked gate immediately; the run resumes and re-audits only after architecture updates the map and no change request remains open.

After drafting, and after each response, STOP at a gate: a blocked gate if any `- [ ]` items remain (or a change request is open), or the discussion-complete planned gate if none do — every item `- [x]`, or the audit raised nothing that needs a decision (an all-mechanical run, or one whose only non-mechanical findings are clear-cut handoffs).

`⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to Code Changes.`
`⏳ GATE: Next: Discussion complete. Say "next" to write Code Changes.`

## Code Changes

Only after the discussion-complete gate advances with no open change request, translate the resolved audit into `## Code Changes` (`T#` items). `## Code Changes` is the durable conformance checklist: checkboxes show what is complete, while Disposition shows whether each item is UI Map implementation work (`implement` / `placeholder`), UI-map-owned work reserved for a larger Plan (`planned`), or directly relevant work owned elsewhere (`handoff`). When the run has a proposed map (a change package), the list ends with a terminal **promote** item (below); a conformance run against the official map has no map change to promote, so it has none.

### Code change items

Write new `T#` items unchecked in the format defined in [`ui-map-implementation-artifacts.md`](ui-map-implementation-artifacts.md): an unchecked checkbox, a stable `T#` ID, an identity, **Description**, **Disposition** (`implement` / `placeholder` / `planned` / `handoff`), **Realizes** (what this item carries out), and **Touches**. Build the list from the audit's already-separated sources: create one item for each applicable `M#` or `D#`, then one for each independent audit finding without an ID. Implementation overlap does not merge sources. Keep all operations from one source under the same checkbox; terminal promotion is the whole-change exception. Before the gate, when a proposed map exists, check that `skai/promoted/<change-id>/ui-map/` is
available and identify live references in the map/app repositories and resolved repositories of
linked related packages or callers. A collision or inaccessible
required reference blocks before writing the official map; never merge or overwrite a destination.
On re-audit reconcile existing items instead of resetting them: retain matching IDs, Dispositions,
evidence and completions still verified against the updated target. Changed/new work remains
unchecked until verified under the existing gate approvals.
Before the gate, read the sources back against the drafted items: each source has exactly one item, and that item's Description carries every operation from the source. There is no `Status` or `Type` field — the checkbox carries completion and the identity and Description convey the kind. Write items top-down in structural order.

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

**The terminal promote item.** The last `T#` owns official promotion and archival. Its Disposition
is `implement`, Realizes names the approved change as a whole, and Touches includes official
YAML/HTML, the type folder and repaired references. Build executes it after green conformance and
resolved handoffs; Plan after Code Changes approval. Check it only after all operations below
succeed at the promoted location.

### Promotion progress and restart

Execute the terminal item in order, recording actual progress in existing `## Evidence`:

1. **Before the first write**, repeat Inputs' comparison against current official YAML. A stale
   change list blocks and returns to architecture; retain completed code items and re-audit the
   updated proposal. Implementation never merges map content itself.
2. Copy proposed YAML to `skai/ui-map/ui-map.yaml`. Record the actual write outcome, identifying this
   package's proposed source and official destination, **before rendering**.
3. Run the project override or default SKAI renderer on that official YAML, targeting
   `skai/ui-map/ui-map.html`. Require exit 0 and a nonempty page; record command/result separately.
   Do not copy the proposed page. A failed render leaves the terminal item unchecked and blocks.
4. Perform *Archive the package*, then check the terminal item in the archived artifact.

On restart, locate the package at its active/promoted path and inspect its recorded progress:

- No successful write recorded: use ordinary proposal readiness and the first-write comparison.
- Write recorded, official render incomplete: compare current official YAML with this package's
  recorded proposed source. If they match, resume the official render, **without copying YAML again**,
  then archive. If another package has changed official YAML, block for reconciliation; never
  overwrite that intervening change or redraft merely because this package's own write erased its
  original diff. Preserve original Map Changes, approval and execution records.
- Official write and render verified: resume archival only; do not repeat canonical promotion.

An uncertain unrecorded outcome uses the standing blocked route, not a fabricated success record.

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

On success, linked output is optional; still record command + exit code. On failure, persist full
output under `evidence/` beside the implementation artifact and link it — inside the active or
promoted UI Map type folder, or the working-doc session for a no-package run. If the failure is a fixable local glitch, fix and rebuild; if it points at a needed change request, requirement conflict, or map flaw, STOP at a blocked gate.

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
- **Agent may render the proposed map** when validating it helps. Promotion **must** render the official YAML directly to the official HTML page and record successful evidence. Use a project-specific override when one exists; otherwise use the SKAI default renderer from [`ui-map-guide.md`](ui-map-guide.md). Rendering validates the map target; it does not authorize editing it.

Click-through QA — running the app to confirm navigation behaves as specified — is downstream of this skill, not a gate it waits on; the placeholder boundary keeps each scaffolded scene visibly identifiable so QA can confirm routes later. If a navigation issue surfaces, handle it like any finding: propose the smallest guide-faithful fix, raising a change request if it requires changing the target map.

## Archive the package

After recording successful official-map write/render evidence in the terminal promote item:

1. Move the entire `skai/changes/<change-id>/ui-map/` folder to
   `skai/promoted/<change-id>/ui-map/` in the map repository. Keep architecture, implementation,
   proposed YAML, render, requests and evidence together, including unchecked Plan work. Leave
   `requirements/` and all other siblings untouched; remove the active grouping directory only if empty.
2. Repair live incoming links across those resolved repositories, including work specs and related
   packages. Check relative links inside the moved files and preserve their intended targets. Keep
   decisions, item IDs, YAML and recorded commands/results intact; annotate historical paths with
   their current locations. An inaccessible required reference blocks completion.
3. Re-render the proposed YAML at its promoted location using the project override or default SKAI
   renderer, producing `proposed-ui-map.html` there. Moving a page can invalidate its relative links
   to the viewer. Require exit 0 and a nonempty page whose viewer links resolve; record this command
   and result separately from the official render evidence.
4. Verify the archived artifacts and links, absence of the active type path, and preservation of
   siblings. Record move/link evidence, then check the terminal promote item in the archived artifact.

If the move, link repair or preview render fails after the official write, report the map as promoted
and archival as incomplete, then STOP at the standard blocked gate. Locate the package at its active
or promoted path on retry and verify identity and recorded progress; resume only unfinished archival
operations, without repeating the official write/render. Never overwrite a destination.

**Example** — promote `skai/changes/reminder-expiry/ui-map/` to
`skai/promoted/reminder-expiry/ui-map/` while a related
`skai/changes/reminder-expiry/requirements/` remains active. Repair its incoming links and regenerate
the moved preview before checking the terminal item. In Plan, unchecked code work stays in the
promoted artifact; the receiving workflow continues there.

## Completion

When the run has a proposed map, completion requires a verified official-map write/render and
successful archival. The terminal promote item stays unchecked until both succeed. Then emit `🏁`
and link the artifact at `skai/promoted/<change-id>/ui-map/`.

**Plan** completes right after the Code Changes gate (the spec review was the sign-off): when a proposed map exists, perform and check the promote; otherwise leave the official map unchanged. Leave `planned` and `handoff` items unchecked and finish — the spec is the deliverable.

- With a proposed map: `🏁 Complete. The UI Map implementation plan is ready; the official map is promoted.`
- Without a proposed map: `🏁 Complete. The UI Map implementation plan is ready; the official map is unchanged.`

**Build** completes once the fresh completion build is green and no `handoff` item remains unchecked: when a proposed map exists, perform and check the promote; otherwise leave the official map unchanged. Then finish.

- With a proposed map: `🏁 Complete. The UI Map implementation is done; the official map is promoted.`
- Without a proposed map: `🏁 Complete. The app conforms to the official UI Map; no map change to promote.`

**A Build with unchecked `handoff` items does not complete.** It ends at a blocked gate reporting what was checked, what remains unchecked, and why UI Map implementation does not own it, and holds the promote when one exists — the promote is the last item, so the run stops before it. Whoever continues the Build — this session, or a later one reading the artifact's `Mode` — resolves the handoff work, re-audits, checks the same item without changing its Disposition, then the effort completes.

`⏳ GATE: Blocked: <N> item(s) handoff — <reason>. Resolve and say "next" to continue.`

**Conformance (no change package)** has no map to promote; it finishes through the applicable Plan or Build branch above, with the official map left untouched.

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/ui-map-implementation-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Once the lookup is done
and before work, report `- 📖 SKAI guide: ui-map-implementation`, nesting `- 📎 Addendum loaded` under it only if one
loaded. If the lookup fails, nest `- ⛔ Addendum lookup failed: <what failed>` and stop. Report each guide
once per task; one addendum line covers referenced documents. Not a gate; keep GATE lines last.
