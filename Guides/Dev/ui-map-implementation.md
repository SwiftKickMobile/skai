# UI Map Implementation

The implementation method for the UI Map system. Consumes the approved plan document produced by [`ui-map-planning.md`](ui-map-planning.md) and executes its Change list. Companion to the platform references ([`ui-map-swiftui.md`](ui-map-swiftui.md), [`ui-map-compose.md`](ui-map-compose.md)), which carry the placeholder-scene spec.

This guide carries the procedure *and* the skai control flow inline; on another host the control flow is rewritten while the reference docs are reused unchanged.

## Purpose

Implementation executes the approved Change list: code edits, file moves, renames, map edits, and any other typed changes planning produced. The execution is **mechanical** — every decision was made during planning. The agent's job is to apply each entry cleanly, build-verify at stage boundaries, and stop on anything the plan didn't anticipate.

**Invariant — the map leads, code follows.** Implementation does not revise the map or the Change list. If the next step requires changing either, that's an amendment back to planning — STOP, propose, get approval.

## Inputs

- The plan document at `working-docs/<branch-path>/<name>/<name>-plan.md` — produced by `ui-map-planning.md`. The Change list, Deferrals, and Out of scope are authoritative.
- The approved `ui-map.yaml` — the working-tree state, including any Phase-2 map edits. For a pure conformance audit, `ui-map.yaml` is unchanged and stands as the conformance target.
- The relevant platform reference — [`ui-map-swiftui.md`](ui-map-swiftui.md) for iOS/SwiftUI, [`ui-map-compose.md`](ui-map-compose.md) for Android/Compose. Provides the placeholder-scene spec and conformance conventions.
- The project's operational doc — `docs/skai/integration.md` — for build/test/render commands. Do not invent commands.
- The project's `README.md` — for any project-specific overrides (e.g., **Modal Styles**, **View Models**).

## Initiation

Implementation starts on an explicit signal — "implement the plan" or equivalent — against a plan document whose Phase 2 is complete (Change list populated, Deferrals populated if any, and any map edits in place).

On the signal: load the plan doc, the approved `ui-map.yaml`, the platform reference, and the project's `README.md`; then begin execution.

If the plan isn't ready — any `- [ ]` remains unresolved in Discussion, the Change list is empty, or (for plans with map edits) the rendered SVG is missing — STOP with a blocked gate citing the missing piece. Implementation cannot start. (Change-list entries themselves are `- [ ]` at start; the agent checks them to `- [x]` during execution — those are expected, not blockers.)

## Gates and control flow

Gate lines:

- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

**Planned gates** — emitted when ready to advance. `next` moves to the next stage (or, at completion, hands off to the human).

- *Stage gate* (optional, large change sets only) — after each domain's entries complete and build-verify passes, summarize progress and emit a planned gate. `next` continues to the next stage.
- *Completion gate* — every Change list entry `- [x]`, final build green: `⏳ GATE: Next: Implementation complete. Build is green. Please review the diff and click through the new navigation. Say "next" to close out.`
- When the human approves at the completion gate: `🏁 Complete. The UI Map implementation is done.`

**Blocked gates** — emitted when the agent cannot advance. Reasons:

- **Plan deviation** — the next viable step would do not-what-the-Change-list-says.
- **Plan flaw surfaced** — a Change entry can't be executed as specified (referenced file/structure doesn't match), or the approved `ui-map.yaml` is invalid.
- **Codebase drift** — the audit's assumptions don't match the current code state.
- **Build broken in an unexpected way** that points at a plan flaw, not a fixable glitch.
- **Ambiguity** — how to interpret an entry isn't clear; STOP and ask.
- **Required tooling missing or broken** — build script, render script, or any other command from `docs/skai/integration.md`.
- **Constrained resolution** — the correct, guide-faithful change can't be completed within the project's constraints (for example, it requires a module to link a package, or any change gated by Safe Operations / human approval). Do **not** improvise an alternative placement or workaround to force a green build — STOP and state exactly what is needed.

The human resolves the cause (amends plan, fixes input, clarifies); the agent re-evaluates and emits the appropriate gate on the next response.

**Advance intent** — moves past a planned gate. Signals: "next", "continue", "go ahead". Recognized only after a `⏳ GATE: Next:` line.

**No `auto` mode.** Implementation has no per-entry planned gates to bypass; running autonomously between blocked gates is the default flow.

**Bright-line:** if continuing correctly would require changing the approved Change list or `ui-map.yaml`, that is a plan amendment, not a fix — STOP, state it, propose the amendment, get approval. Never silently edit the plan or map after the fact to justify an already-made deviation. Resolution may route back to Phase 1.

## Execution

Work the Change list top-down — structural order is execution order. Each entry is a single, typed unit of mechanical work. The Change list itself is the progress tracker; do not maintain a separate todo list.

**Per entry:**

1. Read the entry. **Description** is what to do; **Justification** anchors why; **Touches** lists the files/paths affected.
2. Apply the change — edits, moves, renames, additions, deletions.
3. If a mechanical glitch surfaces, fix it inline (see Auto-fixes below) and continue.
4. If anything else surfaces — plan deviation, structural mismatch, ambiguity, anything not anticipated — STOP at a blocked gate. Do not silently work around it. If you made a change only to diagnose the blocker (e.g. a trial move to build-verify), revert it to the last-green state before stopping, so the working tree isn't left broken.
5. On success, check the box (`- [x]`) and proceed to the next entry.

**Moving files** — when an entry relocates files (e.g. a `folder-org` change), use `git mv` for tracked files (preserves history); fall back to plain `mv` for untracked files.

**Stage boundaries** — at the end of each domain (or other natural chunk for large change sets), run the project's build command (see `docs/skai/integration.md`). Record the result inline at the stage gate using an evidence bracket:

```
[evidence: <command>; exit <code>; output: <path>]
```

On success: linked output optional; still record command + exit code. On failure: persist full output to `working-docs/<branch-path>/<name>/implementation/evidence/<file>` and link it. If the failure is a fixable glitch, fix and re-build; if it points at a plan flaw, STOP at a blocked gate.

**Auto-fixes allowed** (no STOP):

- Obvious typos in identifiers.
- Missing imports.
- Simple compilation errors with a clear, local fix.

**Never auto-fix — STOP at a blocked gate:**

- Anything that requires editing the Change list or `ui-map.yaml`.
- Removing, weakening, or reordering Change entries beyond what the list permits.
- Architectural changes (e.g., choosing a different route kind than the plan specifies, or substituting a different scene name).

**During implementation** — when the human asks questions, answer them. Do not make changes unless explicitly instructed.

## Verification

Verification is split between agent and human:

- **Agent runs build only** — at stage boundaries and at completion. Plus any project-specific automated checks called out in `docs/skai/integration.md` (e.g., the UI Map render-script's schema and semantic checks, if the plan included map edits).
- **Human performs click-through** — after the completion gate, the human runs the app and verifies the new navigation works as specified. The agent does not run the app interactively.

If the human reports a click-through issue, treat as a new blocked gate: diagnose, propose a fix, and amend the plan if the fix requires changing the Change list or `ui-map.yaml`.

## Placeholder boundary

The implementation skill produces **skeleton + navigation only**, not feature content. Every scene the plan adds gets a minimal placeholder that:

- Compiles and routes correctly.
- Is visibly identifiable in the running app (so click-through can confirm the route reached the right scene).
- Carries no business logic, no real UI, no data.

The exact placeholder shape is platform-specific and lives in the platform reference's **Placeholder scenes** section — the authority for how a scaffolded scene is built:

- iOS/SwiftUI: see [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md) — the `SKAISwiftUI` API, the per-route-kind scaffold patterns, the NavigationStack-at-the-presentation-boundary rule, dismiss/breadcrumb behavior, and the new-scene no-inputs rule.
- Android/Compose: see [`ui-map-compose.md`](ui-map-compose.md) → "Placeholder scenes" (pending; authored when the Compose path is built).

**This boundary is a hard line.** If a Change entry appears to require feature content, the entry is malformed — STOP at a blocked gate. Feature work belongs to a separate work spec (see skai's `work-spec-creation` / `work-spec-implementation` flow), not the UI Map implementation skill.

## Completion

When every Change list entry is `- [x]` and the final build is green:

1. Run the render script if the plan included `ui-map.yaml` edits (per `docs/skai/integration.md`) — confirms the final map is valid and renders.
2. Emit the completion gate.
3. STOP and wait for the human to click through.

If the human approves at the completion gate: `🏁 Complete. The UI Map implementation is done.`

If the human reports a click-through issue: see Verification above — treat as a new blocked gate.
