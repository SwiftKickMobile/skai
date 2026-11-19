Managed-By: skai
Managed-Id: guide.configure-skai
Managed-Source: Guides/Core/configure-skai.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-18

# Configure SKAI

Print `📖 SKAI guide: configure-skai` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Launch the bundled Mac app to choose optional skills and policies for the active host project, and
where its artifacts live. The app saves the project-owned `skai/config.json`; an existing gitignored
`skai/config.local.json` still overrides its component selection for one working copy. The installer applies the effective
selection and checks retained component migration history.
The configure skill and app remain available even when every optional component is disabled.
If the request explicitly asks to apply an already saved configuration, skip Launch and the UI gates;
use the explicit-request case under Reconcile after Save. Otherwise open the picker.

## Gates

The supervisor is the human or authorized agent outside this workflow who chooses components;
the executing agent never approves its own selection. Every response while waiting on the supervisor
ends with the same applicable `⏳ GATE:` line, verbatim, until the state changes. Do not invent gates.

The planned gate is a **hard UI choice gate**:
`⏳ GATE: Next: Choose components and locations in the Mac app, then Save and Apply or Cancel.`

Here Next describes the supervisor's UI action, not a chat command. The app's drafts are the
review artifact: agent-mode `ready` means pending choice, final `saved` means config committed
and app closed, and `cancelled` means abandoned before Save. These states replace process TODO
markers. Save and Apply commits the selection and
authorizes component reconciliation; no additional confirmation or acknowledgement is required.

When a Save changes a location, the **location gate** comes before reconciliation (*Location changes*):
`⏳ GATE: Next: Approve the location changes above, decline them, or say what to change.`
Here Next is the supervisor's approval in chat; it does not cover anything the proposal does not name.

Blocked conditions use `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`
Stop until resolved; preserve separate installer gates for unmanaged conflicts and unrelated cleanup.
Completion uses `🏁 Complete. Let me know if anything needs adjustment.` after reconciliation succeeds
and the location gate, if any, is resolved, or after an explicit Cancel (state clearly that configuration and installation are unchanged).

## Advance intent

Chat `next`, `continue`, `go ahead`, `auto` or `auto to` cannot select components or bypass the hard
UI choice gate. `auto` may continue authorized installer work after Save; blockers still require
resolution. While the app is open, keep the command session alive and wait for its final JSON event
using bounded tool waits. Stay in the active agent turn so Save and Apply automatically resumes installation (after the location gate, when a location changed);
show the UI gate line in waiting updates. If the harness interrupts or ends the turn, report that
resumption is needed rather than claiming automatic completion.

## Launch

Resolve the active host root and SKAI checkout from project context and install state using
[`component-history.md`](../../Install/component-history.md) discovery: local, shared, then legacy
`docs/skai/install-state.json`. Malformed/unreadable state blocks; it is not an absent installation.
Do not configure the dependency checkout merely because this guide lives there. Read
[`component-selection.md`](../../Install/component-selection.md) for selection and ownership rules.
Before launch, ensure `/skai/config.local.json` and `/skai/install-state.local.json` are ignored in
this host's SKAI-managed `.gitignore` block, preserving all surrounding text. This configuration
request authorizes that minimal ignore setup. If a local file is already tracked, obtain an explicit
untracking decision; never remove it from Git silently. The app refuses local Save in a Git repo if
these local paths are not ignored. Read local settings normally; do not put them in agent-ignore files.

This prototype requires macOS 13+ on Apple Silicon and the bundled app.
An unavailable app/platform or
invalid/unreadable configuration blocks; never reset config or silently install everything.

Launch the executable directly through the harness's local command tool, with resolved paths:

```sh
"<skai-root>/Bin/SKAIConfigure.app/Contents/MacOS/SKAIConfigure" --project-root "<host-project-root>" --skai-root "<skai-root>" --agent-session
```

The explicit `--agent-session` flag declares the agent launch contract; do not infer it from
parent process names. Verify the `ready` event has `launchMode: agent`. Without that flag the app
uses standalone mode, even when invoked from a terminal. An unexpected mode is a launch error;
resolve it rather than treating a standalone save as the automatic installer handoff.

Use a persistent command session (or equivalent) to capture output and exit status; do not launch
via `open`, detach the process, or infer completion from the window disappearing. Direct execution
opens the native window, prints a `ready` JSON event, and remains running while the supervisor chooses.
No browser, web server, custom URL scheme, Playwright, or runtime Xcode installation is needed.

The app saves the component selection and the project's two locations in `skai/config.json`, each
location a path from the host root, blank or absent meaning the host's `skai/` folder: `productionArtifactsRoot`,
the folder holding the production artifacts, and `changePackagesFolder`, the folder named `skai` that
holds `changes/` and `promoted/`. The agent-mode button is **Save and Apply**; standalone mode uses **Save**.

In agent mode, Save and Apply closes immediately and returns final `saved` with `launchMode: agent`
and `reconcile: true`. Cancel, window close and Quit before Save discard drafts without config/install
changes. No confirmation follows a successful agent-mode Save.

In standalone mode, Save writes the config and tells the user to ask an agent to apply it.
Standalone saved events have `launchMode: standalone` and `reconcile: false`; they are not an
automatic installation handoff.

## Reconcile after Save

An agent-mode final `saved` event names the project/config and has `reconcile: true`. Verify it
matches the launched host, has `launchMode: agent`, and read both actual config layers. A local-only
Save may leave project config absent: that means all project defaults with explicit local overrides.
Do not treat `ready`, a standalone saved event, process interruption, a nonzero exit or window
disappearance as an agent-mode Save. On `cancelled`, stop without running the installer. An
interruption with no final event is unresolved; obtain supervisor resolution before applying.

After a standalone Save, wait for an explicit request to apply it. When the supervisor asks to apply an already saved configuration,
resolve the host and checkout as in Launch, read the current config and history, handle *Location changes* (below), then
execute the same reconciliation.
That explicit request approves the component changes; don't reopen the picker or invoke the
version-update skill merely to apply the saved choices.

For an existing installation, run every adapter in the state discovered above sequentially,
using its runbook from the **current checkout**, in full. Do not invoke the version-update skill,
fetch releases, switch the SKAI checkout or stop because SHA/selections are unchanged. Read
[`component-history.md`](../../Install/component-history.md) for per-component versions, pre-removal
baselines and migration checks on re-enablement, including at the same global SHA. Ordinary installation updates also reconcile actual collateral when config is unchanged. Without install state, use
[`install-update.md`](../../Install/install-update.md) to choose initial adapters.

Save and Apply supplies approval for selected/deselected SKAI-managed component reconciliation.
Report the concrete plan and proceed without another approval for that work; unrelated migrations,
unmanaged conflicts and custom-file cleanup retain their separate gates. The app does not own
installed collateral. If installation fails, retain saved desired state, report incomplete work,
and rerun reconciliation after resolution. Do not record successful state for a failed adapter.

Report the saved path, adapters reconciled and any remaining conflicts. Complete only after actual
inventory and required component migrations match effective config, and the location gate (below),
if any, is resolved. If the supervisor declined a proposed change, the report says that the saved
location and the files now differ. User overrides can enable
migrations of shared collateral under the ordinary ownership/collision rules; no extra approval
is needed solely because the selection came from a local override. No commit, push or release is implied.

### Location changes

A Save that changes a location reports it in `locationChanges`: each changed location's folder
before and after, as paths from the host root. When the supervisor asks to apply an already saved
configuration, compare the last committed `skai/config.json` in source control with the current one
instead, reading blank or absent as `skai`; if the before folders cannot be determined that way,
stop at a blocked gate.

When a location changed, before reconciling propose what it needs: moving what the setting covers (the production
artifacts' folders `product-specs/`, `design-specs/` and `ui-map/`, or `changes/` and `promoted/`)
from the old folder to the new one, and editing the references to the old location that you already
know of. Do not search for others. Name each move, edit and page to re-render, and any move that
cannot be made as stated (a folder missing at the old location, or already at the new one), then
show the location gate. On a request to change the proposal, revise it and show the gate again. On
approval, make exactly the approved changes. Then reconcile, also
when the supervisor declined. Save and Apply approves component reconciliation, never these changes.

## Project Addendum

If `<active-project-root>/skai/addenda/configure-skai-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
