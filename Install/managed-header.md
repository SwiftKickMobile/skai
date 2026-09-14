# Managed File Header (Required)

Any file generated/maintained by `skai` in a host project must start with this header block, with three exceptions defined below: files whose format requires YAML frontmatter first (skill files, Cursor `.mdc` rule files) carry the header as a marker comment after the frontmatter; symlinks are identified by target; and **managed block files** — project-owned files skai writes a delimited block into — carry no header at all.

## Header format

The first lines of the file must be:

```
Managed-By: skai
Managed-Id: <asset-id>
Managed-Source: <repo-relative-source> OR <submodule-path>/<repo-relative-source>
Managed-Adapter: <adapter-id>
Managed-Updated-At: <yyyy-mm-dd>
```

Rules:
- Header must appear at the very top of the file.
- Header keys and casing must match exactly.
- `Managed-Id` must match an entry in `assets.manifest.json`.
- Installer/update overwrites a file only when this header is present (or the destination does not exist).
- `Managed-Updated-At` should only change when the file content actually changes. If the source template is unchanged and the destination already has the managed header, **skip the file** -- do not rewrite it just to bump the date. This avoids unnecessary diffs during submodule updates.

## Determining today's date

Whenever a date is needed (for `Managed-Updated-At`, CHANGELOG entries, `install-state.json`, or any other purpose), **always run `date +%Y-%m-%d` in the terminal** to get the current date. Do not rely on dates from the system prompt or conversation context -- they may be stale or in a different timezone than the human.

## Notes

- For file formats that require comment prefixes, the header should still be present as plain text at the top of the file unless that breaks the format. If it breaks the format, adapt by prefixing each line with the file's comment marker while preserving the same keys.

## Skill files (`.cursor/skills/**/SKILL.md`, `.claude/skills/**/SKILL.md`, `.agents/skills/**/SKILL.md`)

Skill files require YAML frontmatter at the top of the file, so the standard managed header cannot appear as the literal first lines.

For these files, treat a skill file as managed if it contains a managed marker comment **immediately after the YAML frontmatter**, for example:

```markdown
---
name: skai-debugging
description: ...
---
<!-- Managed-By: skai | Managed-Id: skill.skai-debugging | Managed-Source: Submodules/skai/Templates/skills/skai-debugging/SKILL.md | Managed-Adapter: cursor | Managed-Updated-At: 2026-02-17 -->
```

The shared skill templates at `Templates/skills/*/SKILL.md` do **not** contain the managed marker. Each installer stamps it at copy time with the appropriate `Managed-Adapter` value (`cursor`, `claude-code`, or `codex`).

Rules:
- Installers may overwrite a skill file only when this marker is present (or when the destination does not exist).
- `Managed-Id` must match an entry in `assets.manifest.json`.
- Previously installed skills may have adapter-prefixed IDs (e.g., `cursor-skill.skai-debugging`); treat these as managed (the marker is present) and overwrite with the current ID format.

## Cursor rule files (`.cursor/rules/**/*.mdc`)

Cursor parses a rule file only if its YAML frontmatter (`description`, `globs`, `alwaysApply`) is the very first thing in the file, so the standard header cannot be the first lines. Treat an `.mdc` file as managed if it contains the managed marker comment **immediately after the closing `---` of the frontmatter**, in the same form as skill files:

```markdown
---
description: Enforce error handling patterns WHEN writing code that throws
globs: ["**/*.swift"]
alwaysApply: true
---
<!-- Managed-By: skai | Managed-Id: policy.error-handling | Managed-Source: Submodules/skai/Policies/error-handling.md | Managed-Adapter: cursor | Managed-Updated-At: 2026-09-13 -->

# Error Handling Policy
...
```

Rules:
- Never place anything above the frontmatter. A header above it makes Cursor ignore the rule.
- Installers may overwrite an `.mdc` only when this marker is present (or when the destination does not exist).

## Symlinks

Symlinks cannot "contain" a managed header. For symlinked installs, treat a host path as managed if it is a symlink pointing at the expected `skai` target path.

## Managed blocks in project-owned files

Some files skai writes into belong to the project: the Integration doc (`skai/integration.md`), the ignore files (`.gitignore`, `.cursorignore`, `.claudeignore`), and the agent instruction files (`CLAUDE.md`, root `AGENTS.md`). Installers never overwrite these wholesale. Instead each such file holds one or more **managed blocks**, delimited by markers, and the installer owns only what lies between the markers.

Marker grammar — HTML comments in markdown files, `#` comments in ignore files:

```markdown
<!-- BEGIN Managed-By: skai | Section: <section-id> -->
... skai-owned content ...
<!-- END Managed-By: skai | Section: <section-id> -->
```

```
# BEGIN Managed-By: skai
... patterns ...
# END Managed-By: skai
```

A file containing at least one such block is a **managed block file** (see `Install/conflict-precedence-policy.md`). It carries no line-1 managed header: a header would classify the whole file as skai's and license overwriting the project's content.

Rules:
- If the file does not exist, the installer creates it from the corresponding template — the template's project-owned part is written once and never touched again.
- If the file exists and lacks the block, the installer appends the block (at the end unless the template fixes a position). Nothing else in the file changes.
- If the block exists, the installer replaces only the content between its markers.
- If a block's section no longer applies (a stack that is no longer present, a section the human asked to omit), the installer removes that block, markers included, and nothing else.
- Content outside every block is project-owned. Installers never edit, reorder, or reformat it.
- `Section:` ids are stable across releases; renaming one is a migration and must appear in `CHANGELOG.md`.

Per-file specifics live with the guide that owns the file: `Install/integration-doc-install-update.md` for the Integration doc, `Install/agent-instructions-install-update.md` for the instruction files, and each adapter runbook for its ignore file.
