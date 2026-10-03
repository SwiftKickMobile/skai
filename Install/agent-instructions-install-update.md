# Agent instruction file install/update guidance (shared)

The Claude Code and Codex adapters use this procedure for the project-owned instruction file:
`CLAUDE.md` (or existing `claude.md`) for Claude Code, root `AGENTS.md` for Codex.
`Install/managed-header.md` remains the authority for the three ownership forms and dated blocks.

## Templates

- Claude Code: `Templates/agents/claudecode/CLAUDE.md`, id `template.claude-instructions`.
- Codex: `Templates/agents/codex/AGENTS.md`, id `template.codex-agents`.
- Both use `Templates/agents/instructions-block.md` for the shared block interior.

The existing adapter template supplies the `BEGIN`/`END` markers and adapter/id metadata. Do not
replace them with a `Section: instructions` marker or drop the marker date.

## Procedure

1. During discovery, classify the destination using `Install/conflict-precedence-policy.md` and
   include the intended change in the adapter's plan. A missing file is created from its adapter
   template after approval, with a project-owned title and `Start here: [README.md](README.md).`
   above the block. For an existing file, preserve everything outside the block. A whole-file
   managed header is converted to block form as specified in `Install/managed-header.md`, then the
   block is updated; do not regenerate the whole file from a skeleton. A project-owned file with no
   block receives the block only after approval. Do not create or overwrite a symlink destination;
   classify it as a legacy candidate and obtain the separate cleanup decision first.
2. Compose the interior from `Templates/agents/instructions-block.md`, omitting its source managed
   header and substituting the actual checkout path for `<skai-root>`, followed by each applicable
   `policy` asset in manifest order: all assets tagged `core`, plus stack-tagged policies only when
   the confirmed stack matches (for example `swift` for Swift projects). Resolve each `sourcePath`
   against the actual SKAI checkout, rather than assuming its default location.
3. For each policy, remove its managed header if present and demote Markdown headings by two levels
   outside fenced code blocks (`#` becomes `###`, `##` becomes `####`). Put the policy under
   `## Policies`, with a blank line between policies. Preserve its substantive text, including
   `universal-stop-conditions`.
4. Replace only the block interior and update the marker date when its content changes. Preserve
   project-owned content and block metadata; an unchanged block is not rewritten just to bump its
   date. Keep both adapters' template ids stable. Do not add a whole-file header or an enumerated
   installed-skills list; the skills wrappers describe themselves.

## Codex location migration

Before writing root `AGENTS.md`, inspect `.agents/AGENTS.md` if present. Preserve project-owned
content outside its SKAI block: show it in the plan and obtain approval for where to migrate it.
If root `AGENTS.md` already exists, preserve its content and resolve any collision before writing.
Create or update the root file first; cleanup of the old file is a separate permission-gated step.
Do not silently discard custom instructions or remove the old file just because its path is obsolete.

The Cursor adapter inventories root `AGENTS.md` for awareness but never writes into it; its policies
are delivered as `.mdc` rules. Claude Code writes its own instruction file, not root `AGENTS.md`.
