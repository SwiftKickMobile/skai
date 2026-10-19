Managed-By: skai
Managed-Id: guide.update-installation
Managed-Source: Guides/Core/update-installation-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-18

# Update Installation Guide

Print `📖 SKAI guide: update-installation-guide` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Updates the `skai` submodule and re-runs installed adapter runbooks.

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

Planned gates for this workflow:
- Release-documents gate: after reporting what the release documents require (or the `git log` fallback), but before running the adapter install/update runbooks.
- New components gate: when the host has a project config and the target adds optional components it
  has never seen (`newComponents` from the resolver), after the release-documents gate and before the
  runbooks. `Next` opens the configure app; an inline answer naming what to enable or skip is recorded
  through the configuration tool instead.
  - `⏳ GATE: Next: Open the configure app to choose among <N> new components (<labels>). Or say which to enable or skip.`

Stops owned by active inputs (an adapter runbook's confirm step, a stop a release document names) are that input's gates, not fabricated ones: emit its line, or the blocked line if it has none; `auto` never bypasses them.

Workflow-specific blocked gates:
- Every install-state path step 1 names is missing, so the workflow does not know what was installed.
- The default (latest release) target is requested but the submodule has no `v<N>` release tag.
- The target predates the first release that carries `Releases/` (step 5).

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-step rules below. Do not use them to skip required prerequisite checks.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking:
- No work document; state is inline.
- State: the conversation plus the install-state file (adapters write their resolved project or local path).
- At the release-documents gate, STOP after reporting what the documents require and wait for approval before step 5b and the runbooks.

Workflow-specific advance behavior:
- `auto` may bypass the release-documents gate; step 5b still runs before the runbooks.
- `auto` bypasses the new-components gate by enabling every new component (through the
  configuration tool) and naming them in the completion message. A default host (no project config)
  has no such gate: additions install as defaults, and are named at completion the same way.
- `auto` does not bypass the blocked cases.
- `auto to runbooks` = STOP at the release-documents gate.

## Prerequisites

- Install state must exist (created by the initial install). If every path step 1 names is missing, that is the blocked gate above: the supervisor runs the initial install/update runbook per adapter first.

## Procedure

### 1. Read the install state file

Read `skai/install-state.local.json` when present; otherwise `skai/install-state.json`, otherwise
legacy `docs/skai/install-state.json` and record its canonical path migration. Malformed/unreadable
state blocks rather than implying absence. Extract:
- `submodulePath` (default: `Submodules/skai`)
- `lastSHA`
- `lastRelease` (the `v<N>` the host is on; absent or null on older installs — step 5 derives it)
- `lastUpdatedAt`
- `installedAdapters` (list of adapter entries with `runbook` paths)

### 2. Choose the update target

Default to the **latest release** -- the highest `v<N>` tag. Use a different target only when the supervisor names one:

| Supervisor says | Target |
|---|---|
| (nothing) | latest `v<N>` release tag -- the default |
| "head of current branch" | HEAD of the submodule's checked-out branch |
| "head of main" | `origin/main` HEAD |
| "commit <hash>" | that commit |

```
cd <submodulePath>
git fetch --tags
```

Resolve the target to a SHA. The latest release tag is:

```
git tag --list 'v[0-9]*' --sort=-v:refname | head -1
```

If the default is requested but no `v<N>` tag exists, STOP with a blocked gate (the supervisor can name a branch head or commit).

### 3. Check whether an update is needed

Recorded `lastSHA` is the prior migration baseline, not proof of the checkout's version. Read the
actual HEAD:

```sh
git -C "<submodulePath>" rev-parse HEAD
```

Compare that HEAD to the target SHA. Skip only step 4's checkout when they match. A failed update may
have moved HEAD without advancing state, so migration checks use the recorded version. Continue
actual component reconciliation regardless of SHA equality. Use `Install/component-history.md` on every reconciliation; component baselines may
be older than the recorded adapter/global SHA. Never advance install state merely from a checkout.

### 4. Update the submodule

Check out the target in the submodule:

```
git -C <submodulePath> checkout <target-sha>
```

The supervisor commits the host's submodule pointer change as usual.

### 5. Read the release documents

`<submodulePath>/Releases/release-<n>.md` is the technical document of release `n`;
`Releases/unreleased.md` stages the next release. Both are read from the target checkout; a target
older than the first release that carries `Releases/` is a blocked gate. This step is hard, not a suggestion:
reading only the latest document when the host is several releases behind is the failure it
exists to prevent.

1. **Host release.** `lastRelease` from state. If absent or null, derive it from `lastSHA` with the
   tag command below. If that resolves nothing (`lastSHA` absent or unknown to the checkout), the
   host's release is none and every release document applies.
2. **Target release.** For a release target, its `<N>`. For a branch-head or commit target, the
   latest tag that is an ancestor of the target SHA:
   ```
   git -C <submodulePath> tag --list 'v[0-9]*' --merged <sha> --sort=-v:refname | head -1
   ```
3. **Read in order.** Read `Releases/release-<n>.md` for every `n` after the host's release up to
   the target's, ascending. For a branch-head or commit target, also read `Releases/unreleased.md`
   and take the entries dated on or after `lastUpdatedAt`.
4. **Report.** State what the documents require, in document order: asset moves, additions and
   removals, managed-content changes, re-runs, existing-artifact transformations, and any stop a
   document asks the supervisor to review. Record the list of documents read, in order, as
   evidence in this report; the completion message repeats it. If no document or entry applies,
   show `git log --oneline <oldSHA>..<newSHA>` instead.
5. Gate: STOP after reporting and end with `⏳ GATE: Next: Offer any new components, then run the installed adapter update runbooks. Say "next" or what to change.`

### 5b. Offer new components

Resolve each installed adapter's effective selection with the current checkout
(`Install/component-selection.md`) and collect `newComponents`. If the host has a project config and
the list is not empty, STOP at the new-components gate above. On `next`, launch the configure app in
agent mode and verify its result as `Guides/Core/configure-skai.md` § Reconcile after Save says: a
verified Save returns here, and step 6 reconciles once (not that guide's own);
`cancelled` or an unresolved outcome keeps that guide's stop. On an inline answer, write the choices
with the configuration tool's `--enable` / `--decline` flags. Under `auto`, enable them all. Then
continue; the runbooks install whatever the config now selects.

### 6. Run adapter install/update runbooks

For each entry in `installedAdapters`, one adapter at a time:
- Read `Install/component-selection.md` from that checkout, resolve the host's current config, then read and execute the runbook at `<submodulePath>/<runbook>`, including actual inventory/reconciliation.
- Each runbook's migration-capable algorithm applies the scope step 5 reported: each release document whole, in order, then the selected unreleased entries (skills, policies, deprecated artifacts, transformations, the stops a document names).
- A runbook records its own adapter entry and component history as it completes; the top-level `lastSHA`, `lastRelease` and `lastUpdatedAt` advance only at step 7, after every adapter, so a retry after a partial update reports the same range.
- Migration steps are safe to re-run: a host that already applied part of a release from the unreleased document before the cut applies the release document again, and a move of an already-moved path or a conversion of an already-converted file is a no-op. Honor any guard a document states for a step that is not re-runnable.

### 7. Update install state

Update the resolver's active `historyStatePath` with:
- The new submodule HEAD SHA
- `lastRelease`: the `v<N>` tag updated to; for a branch-head or commit target, the latest `v<N>` tag that is an ancestor of the new HEAD (step 5's tag command). Never null.
- Today's date (run `date +%Y-%m-%d` -- see `Install/managed-header.md`)
- Per-adapter `lastRunAt` timestamps and `lastSHA` provenance
- Verified config fingerprint and component history under `Install/component-history.md` when
  tracking applies; retain disabled components' last applied versions. Keep local effective
  history in gitignored local state, preserving shared state and other adapter entries.

Before the completion line, name every optional component this update installed that was not
installed before (new or newly enabled) and any the supervisor declined. Then complete the workflow.

## Project Addendum

If `<active-project-root>/skai/addenda/update-installation-guide-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
