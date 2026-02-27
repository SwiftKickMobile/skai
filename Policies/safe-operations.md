# Safe Operations (Agent Policy)

This policy applies to agents executing the `ai-dev-process` workflows, including install/update runbooks.

## Rules

- Do not change code without explicit authorization when in discussion/troubleshooting mode.
- Do not commit unless explicitly asked.
- Do not push unless explicitly asked.
- Do not delete project files unless explicitly asked.
- Do not add dependencies unless explicitly asked.
- Do not revert changes unless explicitly asked.
- Do not run destructive/irreversible operations without explicit human approval. If unsure, STOP and ask.
- Prefer minimal, reversible changes.
- Before overwriting anything, determine whether the file is managed vs project-owned.
  - Managed files are identified by the managed header.
  - Project-owned files must not be overwritten.

## Destructive operations (examples; not exhaustive)

Destructive operations are actions that discard work, destroy data, or are difficult to reverse.

Before running a destructive operation:
- Describe what will be affected (scope).
- Describe what could be lost.
- Ask for explicit approval, then STOP and wait.

Examples (git):
- Discarding changes (e.g., `git checkout -- <path>`, `git restore -- <path>`, `git reset --hard`, `git clean -fd`)
- Deleting branches (e.g., `git branch -D`)
- Force pushing (e.g., `git push --force`, `git push --force-with-lease`)
- Dropping stashes (e.g., `git stash drop`, `git stash clear`)

