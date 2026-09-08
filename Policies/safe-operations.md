Managed-By: skai
Managed-Id: policy.safe-operations
Managed-Source: Policies/safe-operations.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# Safe Operations (Agent Policy)

This policy applies to agents executing the `skai` workflows, including install/update runbooks.

## Rules

- Do not change code without explicit operator authorization when in discussion/troubleshooting mode.
- Do not commit unless explicitly authorized by the operator.
- Do not push unless explicitly authorized by the operator.
- Do not delete project files unless explicitly authorized by the operator.
- Do not add dependencies unless explicitly authorized by the operator.
- Do not revert changes unless explicitly authorized by the operator.
- Hard prohibition: do not run destructive/irreversible operations unless the operator explicitly
  approves that specific operation within its delegated authority. If the operator lacks that
  authority, it escalates to its own operator. If unsure, STOP and ask.
- `auto` never bypasses this rule.
- Prefer minimal, reversible changes.
- Before overwriting anything, determine whether the file is managed vs project-owned.
  - Managed files are identified by the managed header.
  - Project-owned files must not be overwritten.

## Explicit approval requirement (destructive operations)

"Explicit approval" means the operator clearly instructs you to run the specific destructive
operation now (an imperative request), not merely to discuss options or describe what the command
would do. A standing authorization is sufficient only when it explicitly includes that class of
operation.

If the operator's intent or authority is ambiguous, treat the operation as NOT approved and STOP to
ask: "Do you want me to run <exact command>?"

Examples:

- Approved:
  - "Run `git reset --hard`."
  - "Discard those changes. Go ahead and run `git restore -- path/to/file`."
  - "Force push this branch with `git push --force-with-lease`."
- Not approved:
  - "Should we reset?"
  - "Can you clean this up?"
  - "What does `git clean -fd` do?"
  - "We might need to force push."

## Destructive operations (examples; not exhaustive)

Destructive operations are actions that discard work, destroy data, or are difficult to reverse.

Before running a destructive operation:
- Describe what will be affected (scope).
- Describe what could be lost.
- Ask for explicit operator approval, then STOP and wait.

Examples (git):
- Discarding changes (e.g., `git checkout -- <path>`, `git restore -- <path>`, `git reset --hard`, `git clean -fd`, `git clean -fdx`)
- Deleting branches or tags (e.g., `git branch -D`, `git tag -d`)
- Force pushing (e.g., `git push --force`, `git push --force-with-lease`)
- Dropping stashes (e.g., `git stash drop`, `git stash clear`)
- History rewrite or branch-pointer moves (e.g., `git rebase`, `git commit --amend`, `git reset --soft|--mixed|--hard`)

Examples (filesystem / data):
- Deleting files or directories (e.g., `rm`, `rm -rf`, deleting/overwriting a non-managed file)
- Data resets (e.g., dropping a database, wiping a local app data directory)
- Bulk rewrites without a clean recovery plan (e.g., mass search/replace across the repo)
