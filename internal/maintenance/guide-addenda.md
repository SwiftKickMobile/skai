# Project guide addendum house style

Read this maintainer reference when creating/editing a guide, skill wrapper, guide lookup name or installer instruction composition. It defines the boilerplate authors inline; it is not a runtime dependency or a required user template.

## Scope and ownership

Every registered guide asset supports its own addendum, including reference guides and the internal guide-runbooks. Skills are project-composed building blocks. Integration supplies project-wide operational settings; each base guide loads its own dependencies when needed. Addendum authors write only their additions/overrides, with no required schema, headings, frontmatter or managed header.

The initial addendum lookup is in the active project's `skai/addenda/`. That entry may reference shared addenda in another repository, then add local overrides. A shared-context repository can itself be the active project. They are project-owned; never generate, overwrite, conform or clean them up during installation/update. Do not create mandatory empty directories/files.

## Boilerplate

Insert this cue immediately after the guide's first title, before any procedure or content is applied:

```markdown
Print `📖 SKAI guide: <guide-name>` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).
```

Append this footer, replacing `<guide-name>` with the published lookup name:

```markdown
## Project Addendum

If `<active-project-root>/skai/addenda/<guide-name>-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
```

Initially use the guide filename stem, e.g. `requirements-promotion`. Treat the published name as a compatibility interface: preserve it on a future guide rename, or document an explicit host-addendum path migration without overwriting user content. Names must be unique; lookup never depends on an unannounced rename.

## Shared context

Keep one conventional entry point per guide. It may direct reading shared addenda from another
repository and then apply local additions/overrides; no Integration or README inventory is needed.
Resolve relative references from their containing file, load required shared content before use,
and report only the conventional project entry’s status. Referenced documents need no separate
receipt. Missing/unreadable required references stop; only an absent project
entry is the normal absent case. The [README example](../../README.md#shared-context-and-platform-overrides)
is optional copyable prose, not a required template or schema.

## Wrappers and dependencies

Wrappers point at the full primary guide, including its addendum instructions. Do not restate guide-local restrictions or unconditionally load its reference guides/Integration; that procedure and dependency selection belong in the guide and may be customized. Project policy references retain their separate authority. A referenced guide or nested skill applies its own addendum when used, without loading unrelated addenda.

Use the installed instruction-block exception for supported guide overrides; do not send every intentional override back for permission. Conflicts with current task instructions or project-wide policies still escalate through the existing mechanism. A loading receipt is observable acknowledgement, not enforcement or another review gate.

## Verification

- Entry cue prints the guide line first, then says to read the guide fully; footer path/name is correct and unique; the nested addendum line is printed the moment the addendum is read, and only then; no failure line.
- Emit one addendum line per guide, without separate lines for referenced documents.
- Footer copies differ only in lookup name; neither gate placement nor the guide's no-addendum behavior changes.
- Wrappers remain thin and have no competing guide-default instructions; base dependencies still exist in the guide.
- Reference/handoff cases load the relevant guide's own addendum; no addendum user schema or new global workflow is introduced.
- Header/manifest identity, published-name compatibility, requirements size budget and installed instruction refresh are accounted for. Preserve all user addenda during upgrade.
