# Ticket planning — install-layer

Session: `install-layer` on `work/context`. Ready tickets: #61, #62, #60, #58, #41, #34.

## Phases

- [x] Phase A: Instruction files and the managed-header spec (#61, #62, #41)
- [x] Phase B: Adapter skill lists derived from the manifest (#58)
- [x] Phase C: Change-package and UI Map roots under the `shared` shape (#60)
- [x] Phase D: Update guide shows every changelog entry between SHAs (#34)

Overlaps: A and B both edit the three adapter runbooks (`Install/ClaudeCode/`, `Install/Codex/`, `Install/Cursor/`) — A lands first, B edits on top. C touches `Templates/docs/skai/integration.md` and `Install/integration-doc-install-update.md`, which A also references for block semantics.

### Phase A: Instruction files and the managed-header spec (#61, #62, #41)

Primary tickets:
- [#61 Instruction files (CLAUDE.md, AGENTS.md) are whole-file managed; projects need a project-owned area with a managed block](https://github.com/SwiftKickMobile/skai/issues/61)
  - Friction: the Integration doc and ignore files get `BEGIN/END` managed blocks inside project-owned files; the instruction files get a line-1 header and are treated as wholly skai's, so a project can't add even a "start at README" line without it being overwritten.
  - Suggestion: same block treatment as the Integration doc; project-owned "start here" area above the block; generalize block semantics into `managed-header.md`; migrate existing whole-file instruction files by wrapping; drop the redundant skills list for Claude Code.
  - Notes: no Claude Code instruction template exists today — the runbook only says "create/update … using managed headers".
- [#62 Codex adapter writes AGENTS.md to .agents/, where Codex does not read it](https://github.com/SwiftKickMobile/skai/issues/62)
  - Friction: Codex reads root `AGENTS.md` (and per-directory ones); `.agents/` is only for skills.
  - Suggestion: destination root `AGENTS.md`; inventory an existing one during discovery; keep the stop clause for repos with a different convention.
  - Notes: root `AGENTS.md` is also read by Cursor, Copilot and Gemini CLI, so its skai block must be agent-neutral (issue comment).
- [#41 Add .mdc rule file section to managed-header spec](https://github.com/SwiftKickMobile/skai/issues/41)
  - Friction: spec says the header goes "at the very top"; `.mdc` files need YAML frontmatter first, so installs produced files Cursor can't parse.
  - Suggestion: a "Cursor rule files (`.mdc`)" section parallel to the skill-file carve-out, with an example.
  - Notes: `Install/Cursor/install-update-cursor.md` line "Each generated `.mdc` begins with the managed header" must change with it.

#### Discussion
- [x] PA1 [Proposal] Block layout for instruction files
  - **Concern** The block markers and the ownership rule need one exact shape every adapter follows.
  - **Proposal** `<!-- BEGIN Managed-By: skai | Section: instructions -->` … `<!-- END Managed-By: skai | Section: instructions -->`, same marker grammar as the Integration doc. Everything outside the block is project-owned and never touched. The file no longer carries a line-1 managed header (it would re-classify the whole file as managed).
  - **Why** Reuses a marker grammar installers already implement; one rule for every project-owned file skai writes into.
  - **Decision** Approved as proposed.
- [x] PA2 [Proposal] Where the block semantics live
  - **Concern** Today the merge/update/remove rules for managed blocks live only in `Install/integration-doc-install-update.md`.
  - **Proposal** Add a "Managed blocks in project-owned files" section to `Install/managed-header.md` (the general rule: classification, insert-if-missing, replace-between-markers, never touch outside); have the Integration doc guide and the three runbooks reference it.
  - **Why** `managed-header.md` is already the ownership spec every runbook reads.
  - **Decision** Approved as proposed.
- [x] PA3 [Proposal] Migration of existing whole-file-managed instruction files
  - **Concern** Hosts on v6 have a `CLAUDE.md` whose entire content is skai's under a line-1 header.
  - **Proposal** On update, when the instruction file has the line-1 header and no block: replace it with the template — project-owned "start here" stub above, the current skai content regenerated inside the block. Human-gated in the plan step like every other migration. A file with neither header nor block is project-owned: insert the block at the end, touch nothing else.
  - **Why** The regenerated block is the same content the host would get from a fresh install; nothing project-authored can exist in a whole-file-managed file, so nothing is lost.
  - **Decision** Withdrawn as a separate mechanism. A file with the old line-1 header classifies as managed under the existing rules and is overwritten with the new template, which yields the new shape; the changelog entry tells the installing agent and the confirm gate shows the overwrite. The runbooks state the one-line rule only.
- [x] PA4 [Proposal] A Claude Code instruction template
  - **Concern** No template exists; the runbook composes `CLAUDE.md` freehand, which is how the skills list and the missing README pointer happened.
  - **Proposal** Add `Templates/agents/claude-code/CLAUDE.md`: a project-owned stub ("Start here: `README.md`" placeholder above the block) and a managed block holding the Integration-doc pointer and the policies. Drop the skills list — Claude Code discovers `.claude/skills/` itself.
  - **Why** Policies stay inlined because `CLAUDE.md` is Claude Code's only always-on channel; the skills list is pure duplication.
  - **Decision** Approved as proposed. The block carries all seven policies — the v6 Claude Code install omitted `universal-stop-conditions.md`, which Cursor and Codex do install.
- [x] PA5 [Proposal] Codex destination and the agent-neutral root block (#62)
  - **Concern** `.agents/AGENTS.md` is never read; root `AGENTS.md` is read by several agents.
  - **Proposal** Codex runbook: destination root `AGENTS.md`; discovery inventories root `AGENTS.md`; `Templates/agents/codex/AGENTS.md` becomes the root template with the PA1 block, written agent-neutral — Integration-doc pointer, the policies (inlined per PA7), skills described without assuming a location. Cursor runbook: inventory root `AGENTS.md` during discovery and never write policies into it (`.mdc` remains Cursor's policy channel).
  - **Why** Matches Codex's documented discovery; avoids two adapters fighting over one shared file.
  - **Decision** Approved as proposed.
- [x] PA6 [Proposal] `.mdc` carve-out (#41)
  - **Concern** Spec and Cursor runbook both say header-first, which breaks `.mdc` parsing.
  - **Proposal** Add a "Cursor rule files (`.mdc`)" section to `managed-header.md` — frontmatter first, header lines immediately after the closing `---`, with an example — and reword the Cursor runbook line to match.
  - **Why** Same shape as the existing skill-file carve-out.
  - **Decision** Approved as proposed.
- [x] PA7 [Question] Should the root `AGENTS.md` block inline the policies or link them?
  - **Concern** Claude Code inlines (no other always-on channel); Codex and Cursor can read linked files on demand, and Cursor already gets the policies as `.mdc`.
  - **Proposal** Link, as the current Codex template does.
  - **Decision** Inline for both. `AGENTS.md` and `CLAUDE.md` carry the same block content; one shared block body with thin per-agent templates so the two cannot drift. Cursor sees the rules twice (`.mdc` + root `AGENTS.md`), identical content, accepted.

#### File-change plan

Shared pieces first, then per-adapter runbooks, then bookkeeping.

- FA1 `Install/managed-header.md` — add "Managed blocks in project-owned files": marker grammar `<!-- BEGIN Managed-By: skai | Section: <id> -->` … `<!-- END Managed-By: skai | Section: <id> -->`; a file containing one is a **managed block file**; installers create the block if missing (append at the end unless the template fixes a position), replace only what is between the markers on update, remove the block when its section no longer applies, and never touch anything outside. Managed block files carry no line-1 header. Applies to the Integration doc, ignore files, and the agent instruction files (`CLAUDE.md`, root `AGENTS.md`). Add "Cursor rule files (`.mdc`)": YAML frontmatter first, then the managed marker comment immediately after the closing `---` (same form as skill files), with an example. (#61, #41)
- FA2 `Install/conflict-precedence-policy.md` — "Managed block file" class names the Integration doc, ignore files, and the instruction files; "When destination path already exists" gains: an instruction file that still carries the legacy line-1 header is a managed file and is regenerated from the template, which produces the block form (PA3). (#61)
- FA3 `Install/integration-doc-install-update.md` — its "Managed blocks" section keeps the Integration-doc specifics and defers the general block rules to FA1. (#61)
- FA4 `Install/agent-instructions-install-update.md` (new, parallel to FA3) — the one composition procedure both agent adapters follow: create the file from `Templates/agents/instructions.md` when missing (fill the project name); insert or replace the `instructions` block; block interior = `Templates/agents/instructions-block.md` followed by every policy whose manifest tags apply (`core` always; stack-tagged policies such as `policy.swift-code-organization` only for that stack), each under a `###` heading with its managed-header lines stripped. No skills list — Claude Code and Codex discover their skills folders themselves. (#61, PA4, PA7)
- FA5 `Templates/agents/instructions.md` (new) — the project-owned file skeleton: `# <Project> — agent instructions`, `Start here: [README.md](README.md).`, then empty `instructions` block markers. Replaces `Templates/agents/codex/AGENTS.md`; one file serves both adapters, so the two instruction files cannot drift (refines PA7's "thin per-agent templates" — the per-agent versions would be byte-identical). (#61, #62)
- FA6 `Templates/agents/instructions-block.md` (new) — the block interior: what skai is, pointer to `skai/integration.md`, that skills are installed in the agent's skills folder and used when a request matches, the conflict rule ("if project instructions conflict with skai defaults, ask"), then a `## Policies` heading the policies are appended under. Agent-neutral wording (root `AGENTS.md` is read by Codex, Cursor, Copilot, Gemini CLI). (#61, #62)
- FA7 `Templates/agents/codex/AGENTS.md` — removed (superseded by FA5). (#62)
- FA8 `Install/ClaudeCode/install-update-claudecode.md` — Assumptions: `CLAUDE.md` is a project-owned managed block file. Discovery: inventory `CLAUDE.md`/`claude.md` and classify (block → managed block file; legacy line-1 header → managed, regenerate; neither → project-owned, append block). Execute step 4: follow FA4. (#61)
- FA9 `Install/Codex/install-update-codex.md` — Assumptions: the Codex instruction file is root `AGENTS.md` (Codex reads `AGENTS.md` per directory from the project root; `.agents/` holds skills only). Discovery: inventory root `AGENTS.md`; treat an existing `.agents/AGENTS.md` as a legacy candidate and propose cleanup. Execute step 4: follow FA4. Ignore-file guidance unchanged. (#62, #61)
- FA10 `Install/Cursor/install-update-cursor.md` — "Each generated `.mdc` begins with the managed header" → frontmatter first, marker comment after it, per FA1. Discovery: inventory root `AGENTS.md` for awareness only — Cursor reads it, but its skai block belongs to the agent adapters and the Cursor adapter never writes policies into it; `.mdc` stays Cursor's policy channel. (#41, #62)
- FA11 `assets.manifest.json` — remove `template.codex-agents`; add `template.agent-instructions` (`Templates/agents/instructions.md`) and `template.agent-instructions-block` (`Templates/agents/instructions-block.md`), tags `adapter:claude-code`, `adapter:codex`; add `install-policy.agent-instructions-install-update` (`Install/agent-instructions-install-update.md`, `core`).
- FA12 `README.md` — Codex quick-start prompt: "Use root `AGENTS.md` as the Codex instruction file"; one sentence in the developer conventions that instruction files are project-owned with a skai block. Claude Code prompt gains the matching line for `CLAUDE.md`.
- FA13 `maintain-skai.md` — "Installer invariants → Managed blocks" lists the instruction files; "Required bookkeeping" notes the two instruction templates and FA4 as the place composition rules live.
- FA14 `CHANGELOG.md` (Unreleased, dated) — instruction files are now managed block files (re-run adapters; `CLAUDE.md` is regenerated with a project-owned stub; keep anything you want above the block); Codex `AGENTS.md` moves to the repo root and legacy `.agents/AGENTS.md` is proposed for cleanup; `template.codex-agents` → `template.agent-instructions` + `template.agent-instructions-block`; `.mdc` header placement corrected (re-run the Cursor adapter to regenerate); Claude Code installs now include `universal-stop-conditions`.

Out of scope for A: the skill install lists in the runbooks (Phase B).

### Phase B: Adapter skill lists derived from the manifest (#58)

Primary tickets:
- [#58 Adapter runbooks omit the requirements skills that the Release 5 changelog says adapters install](https://github.com/SwiftKickMobile/skai/issues/58)
  - Friction: each runbook restates the skill list; the lists drifted from `assets.manifest.json` (16 skills in the manifest, 14–15 in the runbooks), so hosts silently miss skills.
  - Suggestion: derive the install list from the manifest; or keep inline lists plus a release-checklist check.
  - Notes: the manifest already tags every skill asset with `adapter:cursor` / `adapter:claude-code` / `adapter:codex`.

#### Discussion
- [x] PB1 [Tradeoff] Derive from the manifest vs keep inline lists with a check
  - **Concern** Inline lists are readable but are the drift source; derivation moves the truth to one file.
  - **Options**
    - A — Runbooks say "install every `skill.*` asset in `assets.manifest.json` tagged for this adapter"; inline lists removed.
    - B — Keep inline lists; add a release-checklist step that diffs them against the manifest.
  - **Proposal** A.
  - **Why** The manifest is already tagged per adapter; B leaves the drift mechanism in place and adds a manual step.
  - **Decision** A — derive from the manifest by adapter tag; inline lists removed.
- [x] PB2 [Proposal] Maintainer bookkeeping for new skills
  - **Concern** With the lists gone, a new skill missing its adapter tags would silently not install anywhere.
  - **Proposal** `maintain-skai.md` "Skills" bookkeeping bullet: a new skill asset must carry the adapter tags; the retro checklist verifies every `skill.*` entry has at least one.
  - **Decision** Approved as proposed.

### Phase C: Change-package and UI Map roots under the `shared` shape (#60)

Primary tickets:
- [#60 `shared` repository shape: guides don't say where change packages live](https://github.com/SwiftKickMobile/skai/issues/60)
  - Friction: `shared` relocates the catalog root but every guide still says a package lives at `skai/changes/<change-id>/` relative to the current repo, so authoring writes into the host while the catalog is in the submodule; promotion scans the host's `skai/changes/`; the UI Map guides have no shape concept at all.
  - Suggestion: define the change-package root as living with the catalog (recorded in the Integration doc), have authoring, promotion and the UI Map guides resolve `skai/changes/` through it, and give the UI Map an official-map root the same way.
  - Notes: touches the requirements guides, the UI Map guides, `Templates/docs/skai/integration.md`, `Install/integration-doc-install-update.md`.

#### Discussion

- [x] PC1 [Tradeoff] Where change packages live under `shared`
  - **Concern** A package must sit with the catalog it proposes, and the agent must be able to find it from either repo.
  - **Options**
    - A — Record roots in the Integration doc (one artifact root, or per-block roots).
    - B — Infer from the artifact's own location.
    - C — Read the artifact's location from the project README, which the instruction file's "Start here" line already sends every agent to.
  - **Proposal** C.
  - **Decision** Human-directed, source-agnostic: the agent must know which repo holds the artifact — from whatever the project provides (its README, the Integration doc's `Requirements root`, the human's instructions). A change package lives in that repo, at its `skai/changes/`. Unknown or ambiguous → blocked gate; the guide never defaults to this repo. Pointing at the artifacts from the README is a recommended project convention, not a rule any guide enforces. No new Integration doc fields.
- [x] PC2 [Proposal] Guide changes
  - **Proposal** Each affected guide's setup section states the rule; the literal `skai/changes/…` and `skai/ui-map/…` paths stay and are resolved against that repo; the guide states the resolved repo before writing outside this one; promotion discovers open packages in the catalog's repo.
  - **Decision** Approved.
- [x] PC3 [Proposal] Where the convention is written down
  - **Proposal** skai `README.md` (a host README points at its requirements catalog and official UI Map; that is how agents find them), the `shared` paragraph in `requirements-catalog.md`, and a changelog entry. No templates or installer changes; the installer never touches a host README.
  - **Decision** Approved.

#### Sanity scan (Phase C)

- `grep -rn 'Next Command' Guides/` → 0 occurrences.
- New "STOP at a blocked gate" sentences trace to existing blocked gates: `ui-map-architecture.md` (reason added to the Blocked gates list), `ui-map-implementation.md` (existing "map … not identifiable" case), `requirements-authoring.md` and `requirements-promotion.md` (existing unresolved-root cases). No new gate categories.
- No `## Gates` / `## Advance intent` sections changed; no marker conventions touched. Headers bumped to 2026-09-13 on all nine edited guides.

### Phase D: Update guide shows every changelog entry between SHAs (#34)

Primary tickets:
- [#34 Update guide uses date filtering for changelog, misses same-day entries](https://github.com/SwiftKickMobile/skai/issues/34)
  - Friction: step 4 filters changelog entries by date "after `lastUpdatedAt`", so same-day releases are dropped; the SHAs are already known.
  - Suggestion: `git diff <oldSHA>..<newSHA> -- CHANGELOG.md`; and/or release-based grouping.
  - Notes: `## Release <N>` sections and `lastRelease` in `install-state.json` already exist since Release 5.

#### Discussion
- [x] PD1 [Tradeoff] SHA diff vs release sections
  - **Options**
    - A — Replace the date filter with the SHA diff.
    - B — Show every `## Release <N>` section newer than `lastRelease`, plus `## Unreleased` when targeting HEAD.
  - **Proposal** B as the primary instruction (releases are the unit the update targets), with A as the cross-check that nothing host-affecting is missed.
  - **Decision** Human-directed: no change. Release targeting (`lastRelease`, `## Release <N>` sections) already covers the normal update path; the date filter stays as the fallback for installs that predate release tracking. Phase D implements nothing; #34 closes as addressed.
