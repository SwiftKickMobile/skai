# Component configuration release standard

## Scope and distribution

SKAI provides project-composed skills and policies, installed by agent-run adapter runbooks.
The component configurator writes desired configuration only; it never installs/removes collateral.
The repository contains the compiled Apple Silicon/macOS13+ app at Bin/SKAIConfigure.app;
users receive it through their SKAI repo/submodule checkout and agents launch it directly.
No separate user app installation, runtime Xcode, web server, Playwright or certificate/notarization
setup is required by this Git-based distribution model. Source/tests/build/branding are internal.
The configure skill and bundle remain available even when all optional components are off.

## Desired configuration and UI

Absent project config preserves all eligible optional components. Present schemaVersion1 config
contains the explicit selected component IDs; empty selection retains required configure support.
The explicit list pins selection; newly added optional components stay off until chosen.
Gitignored config.local.json contains only explicit boolean overrides; omitted keys inherit.
Required components cannot be selected/deselected through either config layer. Known retired IDs
are tolerated and omitted on next Save for the edited scope; unknown IDs/schema/type errors block.
App reads components/categories/descriptions from assets.manifest.json each launch, so ordinary
catalog additions/removals do not require rebuilding the app.

The final UI has Project and User tabs only. User checkboxes are On/Off/Inherit, with a live override
count. Explicitly overridden rows show blue User:On/Off on Project, Project:On/Off on User.
Inherited User names and categories with no overridden children are subtly dimmed; explicit false
counts as an override. Parent categories and individual components have brief descriptions.
Bulk actions sit behind a compact ellipsis menu and apply to the current tab. No main-screen
Save instructions, checkbox-state helper line or per-row Project/User/Effective summary.
Opening starts at the top and window title is Configure SKAI. Saving is enabled only for changes;
returning to original/saved values disables it. The SVG angular ribbon/icon is the accepted artwork.

## Launch and Save contract

Explicit --project-root wins. Otherwise a standalone launch infers the nearest owning repository
from valid local Git submodule metadata, including nested directories/linked host worktrees;
unresolved hosts get a directory picker. Do not infer host from an arbitrary parent directory.
Explicit --agent-session alone selects agent mode. Agent Save and Apply saves changed layers,
closes without confirmation, emits final saved/reconcile:true, and the waiting agent automatically
reconciles installed adapters. A persistent command session must stay alive through the UI choice.
The hard UI choice gate cannot be bypassed by chat advance intent or auto. Cancel commits nothing.
Standalone Save stays open, rebases the saved baseline and shows manual apply instructions;
standalone events have reconcile:false. Close preserves prior saves and discards only unsaved edits.
A later explicit request to apply saved config authorizes reconciliation without reopening the UI.

No opening/read-only resolve writes. Save preserves unrelated JSON keys and unchanged config layers.
Local-only edits do not create/rewrite project config. Changed external config/catalog blocks stale
writes. Writes are atomic; partial layer-write failures roll back this app's writes without overwriting
external edits. Git private config/history must be ignored; tracked private config needs untracking.
Existing project addenda, Integration values, canonical data and unmanaged content remain protected.

## Installation and history

All three adapters (Codex, Cursor, Claude Code) discover/classify/reconcile their own actual outputs
on every invocation, even at the same SHA/fingerprint. Skills derive from manifest adapter tags;
policies derive from selection and stack eligibility. Required fixed infrastructure is retained.
Codex/Claude update only their dated instruction blocks; Cursor uses managed policy rules and does
not write AGENTS.md. Other adapters' content and custom files inside skill folders remain untouched.
Save and Apply already approves scoped component reconciliation; unrelated migrations/unmanaged
collisions/legacy cleanup still need their existing resolutions. Explicit apply works similarly.

Keep a full component ledger once customization OR any managed removal occurs. Ordinary unchanged
defaults need only per-adapter version metadata. Prior versions must be persisted before removal,
including default/eligibility/retirement changes without custom config. Record verified success only
after inventory and artifact migrations succeed; failures retain prior evidence. Disabled and retired
records retain last-applied versions. Re-enable checks from that component's own version, even at the
same global SHA. Unknown provenance triggers artifact audit and must not be replaced with a guessed
new version. A mixed-adapter legacy global SHA cannot establish an individual adapter baseline.

Use shared install-state.json for project installations until local config/state exists. Seed local
state from shared on first use, then preserve local actual history without updating shared choices.
Local state stays authoritative even after resetting overrides. Preserve other adapters' records and
extra state keys. Returning to defaults does not delete established component history. Helpers are
read-only planners; their nextAdapterState is a proposal, never evidence that installation succeeded.

## Verification and remaining scope

Automated checks cover Save/config safeguards, real Git host discovery, history lifecycle/failure
branches, private/shared ownership and Mac/Python resolver agreement. UI appearance is manually
checked by the supervisor; computer-use automation is not authorized. Release checks must exercise
reconciliation in isolated fixtures for all3 adapters (fresh/default, explicit empty/partial config,
local on/off, disable/re-enable, drift, retirement and preservation). No commit/tag/push until asked.
No guide size budget is declared. House-style/addendum/ownership conventions remain applicable.
