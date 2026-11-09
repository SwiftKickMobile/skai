# Maintainer migration bookkeeping — review standard

## Purpose

Maintain SKAI so an upgrading agent has the information required to migrate existing host
installations when shipped assets, formats, or conventions change. This standard applies to the
maintainer's bookkeeping and maintenance retro, not to implementing requirements issue #64.

## Existing contract

The maintainer runbook's Required bookkeeping section makes the changelog's audience the installing
agent. It requires entries to provide what that agent needs to migrate, including renamed/moved
assets, additions/removals, managed-content changes, and required reruns. Pure-internal changes with
no host effect are omitted. Released notes remain frozen; a session records its net host-visible
change under Unreleased.

The maintenance retro checks work completed in the session for omissions and fixes straightforward
misses. It is a completeness backstop, not a transcript or a detailed diff report.

The update-installation guide reads applicable changelog sections, reports changes for review,
then runs each installed adapter's migration-capable algorithm. Each adapter discovers, classifies,
plans, obtains approval, and executes. Project-owned content and canonical artifact ownership remain
protected. A claim that this process cannot use changelog migration instructions must be supported
by inspection of these documents, not assumed.

## Desired outcome

A maintainer considering a change that affects stored host artifacts accounts for existing artifacts
as well as future outputs and leaves usable migration instructions when migration is necessary.
For changes requiring none, the maintainer can explain why; this does not require new permanent
fields, extra gates, or a prescribed extra artifact.

The failure under assessment is a session's omission of existing-artifact migration from its initial
proposal and its unsupported claim that changelog instructions alone would be insufficient. The
review may conclude that existing rules were overlooked and no guide edit is justified. Judge any
proposed text against the existing contract and proportionality rather than treating the proposal
as an approved new requirement.

## Boundaries

Preserve current safety and approval rules, existing installer workflow, changelog audience and
release-history rules, and concise maintenance guidance. Do not implement issue #64, alter host
catalog ownership, generalize presentation rules, or add new installer capability in this pass.

## Release Documents — 2026-10-18

Supervisor decision, superseding the single-changelog contract above. The changelog had grown to
113 KB of installer-facing text that people also had to read.

### Two documents, two audiences

- `CHANGELOG.md` is **release notes for people**: per release, a short themed summary and one link
  to that release's technical document. A release's section is also its GitHub release notes.
- `Releases/release-<N>.md` is the **technical document the installing agent reads**: asset moves
  as old path to new path, additions and removals, managed-content changes, required reruns,
  existing-artifact transformations (what to discover, how to transform, what to preserve, how to
  verify), and any migration the supervisor wants reviewed rather than merely run, written as
  stops the agent makes. `Releases/unreleased.md` stages the next release's document; cutting a
  release renames it to `release-<N>.md` and writes the human notes into `CHANGELOG.md`.
- Every host-affecting change writes both: a human line and a technical entry. Internal-only
  changes write neither. The maintenance retro checks that neither is missing and that they agree.
- Releases 1 to 13 are split out of the existing changelog mechanically, one document each, so one
  mechanism serves a host that is several releases behind; their human notes are a line or two each.

### The updater reads every intervening release

The update-installation guide has a hard step, not a suggestion: resolve the host's `lastRelease`;
list `Releases/release-<n>.md` for every n after it up to the target; read and apply them in
ascending order; record the list of documents read as evidence; then, for a commit or branch-head
target, apply the unreleased document's entries dated on or after the host's `lastUpdatedAt` (re-run safety
makes the same-day overlap harmless; "after" would skip same-day entries, settled 2026-10-18); set
`lastRelease` afterwards. Reading only the latest document when a host is several releases behind
is the failure this step exists to prevent; the guide says so in those words.

### Invariants

- **`lastRelease` is never nulled.** For a commit or branch-head target it is set to the latest
  `v<N>` tag that is an ancestor of the new SHA (the previous rule, "leave null", erased the base
  release and is withdrawn). A host whose state has no `lastRelease` derives it the same way from
  `lastSHA`; a host with neither reads every release document.
- **Migration steps are safe to re-run.** A host that is "release N plus a prefix of unreleased"
  later applies release N+1's document whole; moves of already-moved paths and conversions of
  already-converted files must be no-ops. A step that cannot be made re-runnable says so and states
  its guard.
- **Source and transition** (settled 2026-10-18, round 1): release documents are read from the
  target checkout; a target older than the first release that carries `Releases/` is a blocked
  gate. For the one transition from v13, the Release 14 human notes open with a bold line telling
  an installing agent running the older guide to read `Releases/release-14.md` before the runbooks.
- The changelog-review gate in the update guide becomes the release-documents gate: the agent
  reports what the documents require before running the adapter runbooks, as today.

### Scope

Target for refinement: `Guides/Core/update-installation-guide.md` and its wrapper. Maintenance
pass, not refinement: the three adapter install runbooks (their `lastRelease` rule follows the
update guide's), `internal/maintenance/releases.md`, `internal/maintain-skai.md` (Required
bookkeeping), `internal/maintain-retro.md`, the install runbooks' changelog gate, the reference
mentions in `Install/component-history.md`, `Install/managed-header.md`,
`internal/maintenance/change-packages.md`, `internal/maintain-tickets.md`, `README.md`, and the
"changelog instructs" lines in the other design specs. Size budget for the update guide: 12,500
bytes whole file (10,889 today; the new step and the never-null rule are the growth).

