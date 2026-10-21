# Release documents — maintenance notes

Session: release-documents (branch `main`, skai checkout). Standard: `skai/refinement-reviews/maintainer-migration-design.md` § Release Documents — 2026-10-18.

## Decisions stated

- Legacy `## Released` bucket → `Releases/release-0.md` ("Release 0 — before release numbering"), so a host with no `lastRelease` and no resolvable `lastSHA` reads it through the same mechanism as every other document.
- `Releases/` is not registered in `assets.manifest.json`: the manifest lists installable assets and installer dependencies that carry a managed header and a `Managed-Id`; release documents are frozen history read from the checkout, never installed, and would otherwise need headers and date bumps that contradict "frozen". Same treatment as `internal/maintenance/`.
- Adapter runbooks' "otherwise set `lastRelease` to null" replaced by the ancestor-tag rule (same invariant the standard withdraws; not in the Scope list by name — flagged in the report).

## Pre-edit workflow model — `Guides/Core/update-installation-guide.md`

- Happy path: read install state → choose target → compare HEAD → checkout → read release documents and report → **release-documents gate** → offer new components (gate when any) → adapter runbooks → write install state → completion line.
- Workflow-owned artifacts: the conversation (reports, evidence list) and the discovered install-state file (written at step 7). No working document, no `- [ ]` markers; Discussion-free.
- Marker lifecycle: none; gate state is the conversation. Install state changes only after runbooks succeed (step 7).
- Blockers: all install-state files missing; malformed state; default target with no `v<N>` tag; new-components gate (planned, inline answer or configure app).
- Simulations (pre-edit):
  - Normal: host `lastRelease: v11`, target v13 → read release-12, release-13 in order → report → gate → `next` → runbooks → state `lastRelease: v13`. Old guide shows "every `## Release <N>` section newer than lastRelease" — same intent, but no evidence list and no order statement.
  - Blocked/tooling: no install state → blocked gate; `git fetch --tags` fails → blocked gate (generic).
  - Ambiguity/spec flaw: host `lastRelease: null` (old rule nulled it on a commit target), target v13 → old guide falls back to "entries dated after lastUpdatedAt", which reads release documents by date and misses same-day cuts; new rule derives the release from `lastSHA`.
  - Auto: `auto` bypasses the release-documents gate and the new-components gate (enabling all), never the blocked cases.

## Post-edit simulation and sanity scan

(recorded after the edit, below)

### Post-edit simulations (update guide, 2026-10-18)

- Normal: state `lastRelease: v11`, default target v13 → step 5 host release 11, target release 13 → read `release-12.md`, `release-13.md` ascending → report with the evidence list → `⏳ GATE: Next: Run the installed adapter update runbooks…` → `next` → 5b (no new components) → runbooks apply both documents whole → step 7 `lastRelease: v13`. No issues.
- Blocked: no install-state file at any of the three paths → workflow-specific blocked gate before step 1; default target with no `v*` tag → blocked gate at step 2. `auto` does not bypass either. No issues.
- Auto: `auto` → release-documents report still printed, gate bypassed; new-components gate bypassed by enabling all; completion names them. No issues.
- Commit past a tag: `lastRelease: v13`, `lastUpdatedAt: 2026-10-15`, target "head of main" whose ancestor tag is v13 → no `release-<n>.md` applies; `unreleased.md` entries dated after 2026-10-15 apply → gate → runbooks → step 7 `lastRelease: v13` (ancestor), never null. No issues.
- No `lastRelease` (old null rule): `lastSHA` is a commit past v12 → derived v12 → target v13 reads `release-13.md` whole; entries the host already applied from the unreleased staging are re-run as no-ops (step 6). No issues.
- Neither `lastRelease` nor a `lastSHA` known to the checkout → every document from `release-0.md` upward. No issues.
- Open (supervisor): same-day staging — "dated after `lastUpdatedAt`" (the standard's words) skips an unreleased entry dated the same day as the host's last update; "on or after" would be safe under re-run safety. Not changed; raised in the report.

### Sanity scan (update guide)

- Managed-Updated-At: bumped to 2026-10-18 in the same edit (header read).
- `## Gates` / `## Advance intent` present; supervisor definition sentence present (line 17).
- Terminology: `grep -n -i 'Next Command\|checkpoint'` → 0 occurrences. `grep '\bhuman\b'` → 1 occurrence, line 17, the standard supervisor definition (false positive, intentional per template).
- Process-flow runtime reference: `grep 'process-flow.md'` → 0 occurrences. No standalone Progress Tracking/Emoji sections (visual review).
- Markers: `grep '🟡\|- \[ \]'` → 0 occurrences (no process artifact in this workflow). No discussion items.
- Flow control: every STOP corresponds to a gate — step 2 blocked (no tag), prerequisites blocked (no state), step 5 planned (line 164), 5b planned (line 43). `grep '⏳ GATE'` → lines 15–25 template, 43, 54, 164; each traces to a `## Gates` entry. `auto` section labels the hard cases (missing state, no tag). No marker clearing anywhere. Working-doc paths: none created.
- Stack references: none. Size: 12,421 bytes ≤ 12,500.

### Sanity scan (maintain-retro.md, maintain-tickets.md, runbooks, references)

- Managed headers bumped where present: `maintain-retro.md`, `maintain-tickets.md` → 2026-10-18. `Install/*.md` files carry no managed header (checked `head -6`); none to bump.
- `grep -rn -i changelog Guides Install internal Templates README.md` → remaining hits all name `CHANGELOG.md` deliberately as the human document (classified above as intentional).
- No gate mechanics changed in the retro, tickets or runbooks (edits were reference text only; visual review of each diff hunk).

## Maintenance retro (2026-10-18)

1. Inventory: `Releases/` created (15 documents), `CHANGELOG.md` rewritten as human notes, update guide step 5/7 and gate renamed, adapter runbooks' `lastRelease` rule and update-review bullet, maintenance references repointed. Host-install-visible: yes (update behaviour; no installed asset changed).
2. Bookkeeping: technical entry in `Releases/unreleased.md` and human line in `CHANGELOG.md` § Unreleased — both present and agree. Manifest: no installable asset added (decision above). `Managed-Updated-At` bumped on `update-installation-guide.md`, `maintain-retro.md`, `maintain-tickets.md` (the only managed files edited). README: Usage phase 1 and Development guide updated; `Releases/` line added during the retro. `maintain-skai.md` updated (bookkeeping + routing row).
3. Integration doc: untouched.
4. Installer safety: runbook order and permission gates unchanged (diff hunks reviewed).
5. Consistency: `grep -rn '## Release <N>\|## Unreleased'` outside the two documents → only intentional mentions in `maintain-skai.md`, `maintain-retro.md`, `releases.md`, the standard, and a working doc (history). Every `](Releases/...)` link in `CHANGELOG.md` resolves (loop over links → 0 missing). README references are markdown links. Guide header and `## Gates` present; wrapper unchanged and thin. No change-package or addendum contract change. Maintenance references did not move.
6. Reflection: no process suggestions.

Result: Maintenance retro complete; one miss fixed during the retro (README `Releases/` line).

## Runbook contract follow-up (supervisor, after refinement round 3)

- Three adapter runbooks (`Install/ClaudeCode`, `Install/Codex`, `Install/Cursor`): on merge, upsert only this adapter's entry and component history; do not advance top-level `lastSHA`/`lastRelease`/`lastUpdatedAt` (the update guide's step 7 does, after every adapter); on create, write the whole file with `lastRelease` from `git tag --list 'v[0-9]*' --merged HEAD --sort=-v:refname | head -1`, never null. Tag pattern narrowed to `v[0-9]*` in the runbooks (supervisor ruling); the guide's two `'v*'` occurrences stay until round 4 closes (guide untouched while the review runs; +10 bytes needs a 4-byte trim).
- `Releases/unreleased.md` entry extended with the runbook contract change.
- Sanity scan: `grep -rn 'update \`lastSHA\`, \`lastRelease\`' Install/` → 0 occurrences; `grep "tag --list 'v\*'"` → only the guide's two occurrences remain (deferred as above); runbooks carry no managed header (none to bump); no gate mechanics changed (the edited bullets are state-write rules). Visual review: `Install/component-history.md` line 67 (legacy global `lastSHA`/`lastUpdatedAt` as evidence) is unaffected — it reads, never writes, those fields.
