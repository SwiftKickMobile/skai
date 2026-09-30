# Managed Content (Required)

Files that `skai` writes into a host project are marked so an install/update can tell what it owns.
There are three forms. The template for a file — or, for skills, the installer's stamping rule — shows which one it uses; the installer applies the
matching rule.

## Whole-file header

The first lines of the file are:

```
Managed-By: skai
Managed-Id: <asset-id>
Managed-Source: <repo-relative-source> OR <submodule-path>/<repo-relative-source>
Managed-Adapter: <adapter-id>
Managed-Updated-At: <yyyy-mm-dd>
```

The installer owns the whole file. It overwrites the file only when this header is present or the
file does not exist. If the format needs comment prefixes, prefix each header line with the file's
comment marker, keeping the same keys.

## Marker comment

For files whose format requires something else first (YAML frontmatter), the same keys appear as one
comment immediately after it:

```markdown
---
name: skai-debugging
description: ...
---
<!-- Managed-By: skai | Managed-Id: skill.skai-debugging | Managed-Source: Submodules/skai/Templates/skills/skai-debugging/SKILL.md | Managed-Adapter: cursor | Managed-Updated-At: <yyyy-mm-dd> -->
```

Same rule as a whole-file header: the installer owns the file and overwrites it only when the marker
is present or the file does not exist. Shared templates do not contain the marker; each installer
stamps it at copy time with its own `Managed-Adapter`. Older markers may carry adapter-prefixed ids
(`cursor-skill.skai-debugging`); treat them as managed and rewrite to the current id.

## Delimited block

For files the project owns, the installer owns only a block:

```
<!-- BEGIN Managed-By: skai | Managed-Id: <asset-id> | Managed-Adapter: <adapter-id> | Managed-Updated-At: <yyyy-mm-dd> -->
...
<!-- END Managed-By: skai -->
```

(Where `<!-- -->` is not a comment, as in ignore files, use the file's comment marker: `# BEGIN Managed-By: skai` / `# END Managed-By: skai`. That form carries no keys.)

The installer creates the file from its template if absent, stamping the marker's `Managed-Updated-At`;
otherwise it replaces the content between the markers and the marker's date, and touches nothing
else. A file with no block is not overwritten; the block is appended after approval. A file carrying a whole-file header where a block is
now expected is converted: the header lines become the `BEGIN` marker (`Managed-Source` is dropped; the template is
the source) and an `END` marker closes the managed content.

## Common rules

- Keys and casing must match exactly.
- `Managed-Id` must match an entry in `assets.manifest.json`.
- `Managed-Updated-At` changes only when the content changes. If the source is unchanged and the
  destination is already managed, skip the file rather than rewriting it to bump the date.

## Determining today's date

Whenever a date is needed (for `Managed-Updated-At`, CHANGELOG entries, `install-state.json`, or any other purpose), **always run `date +%Y-%m-%d` in the terminal** to get the current date. Do not rely on dates from the system prompt or conversation context -- they may be stale or in a different timezone than the supervisor.
