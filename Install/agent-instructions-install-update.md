# Agent instruction file install/update guidance (shared)

Shared by the Claude Code and Codex adapters. It covers the agent instruction file — `CLAUDE.md` for Claude Code, root `AGENTS.md` for Codex — which is project-owned and holds one skai-managed block (see `Install/managed-header.md`, "Managed blocks in project-owned files").

## Goals

- The project owns the file. Everything above and below the block — typically a "start here" pointer at the repo's own documentation — is never touched.
- The block is the same for every agent. Its wording is agent-neutral because root `AGENTS.md` is read by Codex, Cursor, GitHub Copilot, and Gemini CLI alike.
- The block carries the policies in full. The instruction file is the only file each agent loads on its own, so a pointer to a policy is not enough.

## Templates

- `Templates/agents/instructions.md` — the file skeleton: a project-owned title and "Start here" line above an empty `instructions` block.
- `Templates/agents/instructions-block.md` — the block interior, up to and including the `## Policies` heading.

## Procedure

1. Classify the destination per `Install/conflict-precedence-policy.md`:
   - **Absent** → create it from `Templates/agents/instructions.md`, replacing `<Project>` with the repo's name.
   - **Present with an `instructions` block** → managed block file; only the block interior is replaced.
   - **Present with a line-1 managed header and no block** → the whole-file form installed before managed blocks existed; regenerate the file from the template. This is an overwrite: list it in the plan for the human to confirm.
   - **Present with neither** → project-owned; append the block markers at the end of the file and change nothing else.
2. Compose the block interior:
   1. `Templates/agents/instructions-block.md`, verbatim.
   2. Every applicable policy from `Policies/`, in `assets.manifest.json` order: all `policy.*` assets tagged `core`, plus a stack-tagged asset (for example `policy.swift-code-organization`, tag `swift`) only when the detected stack matches. Use the stack determination and the human's confirmation from the Integration doc step.
   3. For each policy: drop its managed-header lines, demote its headings by two levels (`#` → `###`, `##` → `####`, and so on), and place it under `## Policies` with a blank line between policies.
3. Write the interior between the markers. Do not add a managed header to the file; the block carries no date — `skai/install-state.json` records what was installed.
4. Do not list the installed skills. Claude Code reads `.claude/skills/` and Codex reads `.agents/skills/` on their own; a list here only drifts.

## Do not

- Do not write anything outside the block, and do not place content inside it that the project would need to edit — project instructions go outside.
- Do not restate the Integration doc's content; point at it.
- Cursor adapter: never write into root `AGENTS.md`. Cursor reads it, but the block belongs to the agent adapters, and Cursor's policies are delivered as `.mdc` rules.
