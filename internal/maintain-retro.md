Managed-By: skai
Managed-Id: guide.maintain-retro
Managed-Source: internal/maintain-retro.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Maintenance retro checklist (agent + supervisor)

Print `📖 SKAI guide: maintain-retro` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Use this after making changes to `skai` to ensure nothing was forgotten.

## Retro intent (read this first)

This retro is a **backstop for completeness**, not a git/diff report.

- Scope: the retro covers **everything that changed since the previous retro** (if any). If no prior retro was performed, cover everything changed in the current session.
- Do **not** do a detailed "what changed" writeup unless explicitly asked.
- Prefer scanning docs/templates/runbooks for **consistency and missing updates**.
- If you find a straightforward miss **inside this repo** (e.g., a stale path in `README.md`, a missing `CHANGELOG.md` bullet, a missing manifest entry), **fix it immediately** and continue scanning.
- The expected output is either:
  - a short list of **misses / follow-ups**, or
  - **"Retro complete; no misses found."**

## 1) Inventory (high level only)

- In 1-2 bullets: what you changed (e.g., "Integration template format", "runbook behavior", "new asset added").
- State whether it's **host-install-visible** (affects host repo installs) or internal only.

## 2) Required bookkeeping

- For each host-install-affecting change since the last retro, verify `CHANGELOG.md` meets `internal/maintain-skai.md`'s `Required bookkeeping` migration contract: it tells the upgrading agent how to handle existing artifacts, not only what future outputs will look like. Fix missing or unusable migration instructions; pure-internal changes with no host effect need no entry.
  - Changelog is release notes: prefer multiple short bullets over a single mega-entry.
- Ensure `assets.manifest.json` is updated if you added/moved/renamed any installable asset or installer dependency (templates/sections/runbooks/policies).
- Ensure every managed file edited since the last retro carries a `Managed-Updated-At` no earlier than that edit.
- Ensure `README.md` is updated if needed:
  - Quick start prompts if any runbook paths changed
  - Usage section: ensure the workflow descriptions and phases match the updated guide checkpoint/gate behavior (and add/update any guide inventory section if your README has one).
  - Any new conventions/invariants developers need to know
- Ensure `internal/maintain-skai.md` is updated if you changed invariants or introduced a new maintenance rule.

## 3) Integration doc architecture checks (common misses)

- If you changed Integration behavior:
  - `Templates/docs/skai/integration.md` still has a project-owned "Special instructions / overrides" section.
  - Stack-specific templates exist under `Templates/docs/skai/integration-sections/`.
  - Runbooks still describe how to merge/update/remove the managed blocks.
  - 🟡 is used only for true project-specific constants/mappings (not for variables or standard procedures).
  - Integration section templates are **integration-doc-ready** content (no 🟡 TODO lists; no installer/supervisor instruction prose; include copy/pasteable CLI templates with `<...>` variables).

## 4) Installer safety checks

- Runbooks still enforce:
  - discover → classify → plan → confirm → execute
  - permission-gated deletion/replacement of legacy candidates
  - managed headers for generated files
  - managed blocks for project-owned files like ignore files / Integration doc

## 5) Consistency checks

**Record the result of every check, even when clean.** For each check below, write down either `0 occurrences` (with the search / inspection used — file paths, `grep` / `rg` pattern, or "visual review of section X") or a list of occurrences classified per-check (`<path>:<line>` → `false positive (intentional per …)` / `to fix` / `to revisit`). Reading the check and self-certifying "done" without a recorded result is the failure mode this rule prevents — a `0 occurrences` line with the search used is the minimum evidence. This matches the recording discipline used by [`maintenance/guide-authoring.md` § Sanity scan](maintenance/guide-authoring.md#sanity-scan-after-every-guide-edit).

- Search for stale paths (e.g. old install target directories) and update all occurrences.
- Ensure new files referenced by runbooks exist at those paths.
- README link check: when `README.md` references a file or directory within this repo, ensure it is a markdown link (clickable in the browser), not just a bare backticked path.
- If you added or substantially edited any files under `Guides/`:
  - Verify each changed/new guide has a managed header.
  - Verify it has a `## Gates` section if it is a gated workflow — one where the agent waits on the supervisor and emits `⏳ GATE:` lines — and that its declared control model preserves the shared process-flow invariants (see [`maintenance/gated-workflows.md`](maintenance/gated-workflows.md), "Standard structure for guides with gates"). A bare "STOP" inside a method guide (stop and run the self-check; stop and present a tradeoff) is not a gate and needs no `## Gates` section.
  - Search for terminology drift (e.g., "Next Command") and fix to "advance intent".
  - For each planned gate, verify its review artifact, declared state/marker lifecycle and post-approval action. Preserve explicit variants such as Discussion-only markers already resolved at the planned gate, or a no-auto control model; do not create default markers/auto behavior to satisfy a template check.
  - Verify marker conventions match the canonical rule: `- [ ]` / `- [x]` in process artifacts (markdown workflow docs); `🟡` only in source files (test code, app code) where completion = removal. The canonical in-code case is `Guides/Test/unit-test-planning-guide.md`.
  - Verify `- [ ]` items have stable letter-led IDs on the same line (`D1`, `T1`, `F1`, `S1`, etc.), tight lists under shared headings (no blank lines between sibling checkbox items), and that markers are never on heading lines.
  - Verify discussion-based phases use the Structured discussion items schema (`[Question]`/`[Proposal]`/`[Tradeoff]`, inline-with-topic, no aggregator sections like `## Questions` / `## Decisions`). See `Guides/Core/process-flow.md` "Structured discussion items".
  - If the guide creates ephemeral working docs, verify its paths use `skai/working-docs/<branch-path>/<session-name>/...` rather than placing files directly under `skai/working-docs/<branch-path>/...`.
- Every manifest `skill` asset has at least one `adapter:` tag and an existing `sourcePath`; runbooks install from those fields. Untagged skills install nowhere.
- If change-package workflows, artifact formats, or callers changed: run and record the [change package verification](maintenance/change-packages.md#verification), including coexistence, independent promotion, archival recovery, link repair and migration coverage.
- If guides or wrappers changed: verify the [guide addendum contract](maintenance/guide-addenda.md#verification), including coverage, host-root paths, receipts, thin routing, name compatibility and preserving user files.
- If maintenance references moved: verify the main routing table, cross-references and retro point to their current homes.
- If a new skill was added or changed: verify the skill template is a **thin wrapper** (just references to Guides), not a self-contained document with inline logic. All substantive instructions must live in a Guide under `Guides/`.

## 6) Process reflection

Reflect on the session since the last retro (or since session start). Consider:

- **Pattern violations**: Did you break an established convention? What cue did you miss, and what check would have caught it earlier?
- **Recurring friction**: Were there repeated failures (e.g., tooling issues, encoding problems, ambiguous instructions) that a process change could prevent?
- **Missing knowledge**: Did you lack context that a skill, rule, or documentation improvement would provide? Would a new skill or rule help future LLMs avoid the same mistake?
- **Documentation gaps**: Are there undocumented invariants, conventions, or patterns that you had to learn from supervisor correction?
- **Supervisor corrections**: Did the supervisor have to point out something you should have caught yourself? What was the root cause -- a missing check, a missing convention, or a gap in your understanding of the system?

Output: 1-4 concrete suggestions (not vague observations). Each suggestion should name the specific file or artifact to create/update and what it should say. The supervisor will decide which to act on.

If nothing stands out, say **"No process suggestions."**

## 7) Retro output (keep it short)

- Always start your message with a one-line declaration that the retro was performed:
  - `Maintenance retro: DONE`
- If you fixed misses during the retro: list what you fixed (1-6 bullets), then list any remaining follow-ups.
- If you found misses you did not fix (because they require supervisor decision): list them as **actionable follow-ups** (1-6 bullets).
- If you found none: say **"Maintenance retro complete; no misses found."**
- Include process suggestions from step 6 (if any) as a separate **"Process suggestions"** section at the end.

## Project Addendum

If `<active-project-root>/skai/addenda/maintain-retro-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
