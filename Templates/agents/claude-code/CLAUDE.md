# Claude Code Instructions

This repo uses `skai` for reusable agentic coding workflows and policies.

## Operator model

Your operator is the human or parent agent that requested your current work. Return gates and
blockers to your operator. The operator may resolve them within its delegated authority or escalate
them to its own operator. When you delegate, you become the child agent's operator and may pass only
authority you already have. Never approve your own work where independent review is required. A
blocked child workflow does not prevent you from continuing unrelated work.

Before running a `skai` workflow:

- Read `skai/integration.md` for project-specific build, test, lint, artifact, and evidence-capture details.
- Use the installed skills under `.claude/skills/skai-*/` when the current request matches one of their descriptions.
- Follow `Submodules/skai/Policies/unauthorized-changes.md`, `Submodules/skai/Policies/safe-operations.md`, and `Submodules/skai/Policies/universal-stop-conditions.md` for authorization and safety boundaries.
- Prefer the canonical guides under `Submodules/skai/Guides/` over older copied guidance elsewhere in the repo.

If project-specific instructions conflict with `skai` defaults, ask the operator before proceeding.
