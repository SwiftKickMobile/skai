Managed-By: skai
Managed-Id: template.agent-instructions-block
Managed-Source: Templates/agents/instructions-block.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

## SKAI

This repo uses `skai` (`<skai-root>/`) for its development process: guide-based building blocks installed as skills, and the policies below.

- Read `README.md` first; it links the project's resources, and a linked resource is where the README says it is. If a resource a task needs is not linked there, it is unavailable even when something else names it: stop at a blocked gate; do not look for it.
- Read `skai/integration.md` before running any build, test, or verification command. It is the project-owned source of truth for commands, destinations, and evidence collection.
- To change installed SKAI components, use `skai-configure`; the installer reconciles `skai/config.json` on every install/update. Project selections are in `skai/config.json`; private `skai/config.local.json` overrides them. With neither config, all eligible components are selected.
- Use the installed `skai-*` skills when a request matches one of their descriptions. They live in this agent's skills folder and describe themselves.
- Prefer the canonical guides under `<skai-root>/Guides/` over older copied guidance elsewhere in the repo.
- Print each guide's `📖 SKAI guide:` line and any indented `- 📎 Addendum loaded` line when its guide says to, as lines of their own; if your only output is a final report, put them first in it. Apply supported project guide addenda according to each guide's Project Addendum instructions; intentional overrides of guide defaults need no separate approval. Current task instructions and project-wide policies still apply. For other unexpected instruction conflicts, ask the supervisor before proceeding.

## Policies
