Managed-By: skai
Managed-Id: guide.design-specs-artifacts
Managed-Source: Guides/DesignSpecs/design-specs-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-31

# Design Spec Artifact Formats

Print `📖 SKAI guide: design-specs-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

Typed formats for design-spec workflows. Content rules and checks:
[`design-specs.md`](design-specs.md); shape and tool: [`spec-file-shape.md`](../Core/spec-file-shape.md).
The package mirrors the product spec package
([`product-specs-artifacts.md`](../ProductSpecs/product-specs-artifacts.md)); only differences are here.

## The Package

`skai/changes/<change-id>/design-specs/`; after promotion, `skai/promoted/<change-id>/design-specs/`.
For the **base** and requests, read [`change-requests.md`](../Core/change-requests.md).
Packages depend only on their base and cited draft requirements in active product spec packages
until promotion repoints them. Input citations, such as requests in other packages, are not dependencies.

The layout is the product spec package's, with `design-specs-authoring.md` (`## Spec Changes`),
`proposed-design-specs/**` (touched files only, each whole),
`design-specs-review.html`, `change-requests/<nnn>/` and `promoted-change-requests/<nnn>/` holding
requests of this layout, `design-specs-promotion.md`, and `working-docs/`. The page follows the
product spec guide's render/link rules. Checked `C3` means the base is written; `C4`, archived.
Promotion's own failed check is not a request: it blocks and returns the package to authoring.

## Spec Change Items

`## Spec Changes` gives each base-to-draft difference in held files one typed entry, by prose and
resolved target identity. Entries omit spec text; the page shows each difference under its justification.

```
- S<n> <operation> <object>: <identity>
  - **Justification** <why the change is needed>; <Source>: <reference>
  - **Touches** draft-file links; an intro may ride here, an index line only with the new file it describes
```

- **ID** `S01`, `S02`, …: package-local, never renumbered or reused; dev specs cite `UI-*`, never
  `S`. Order entries by root, glossary, folder, file and item; no checkbox.
- **Operation** `add | modify | retire | move` × **object** `spec file | item | rule | index line |
  glossary entry | known-difference note`. Only items move; a rule changing parent retires and is
  re-added; files never retire. [Modify vs. Retire](design-specs.md#modify-vs-retire) decides; a
  retired glossary entry or note disappears, only items and rules keep `(retired)`.
- **Identity** file titles linked to drafts, item and rule IDs to the draft item heading, terms
  to the draft glossary, index lines by the file described. A `move` puts `from → to` in Touches;
  promotion verifies identical prose and resolved targets and repoints incoming links; move plus
  modify keeps one contract, the move verified first. Draft every design-spec file whose links a move or
  retirement changes, in Touches after it.
- **Source** as the product spec guide, after the reason; `Catalog` is existing specs or requirements.

`check-changes` confirms the list matches the projection.

**Granularity follows the file.** A new spec file gets one entry, its index line in `Touches`;
list incoming moves separately. Root creation gets one entry (root index, glossary, three folder
indexes). In existing files, each changed item, rule, glossary entry, index line or known-difference
note gets an entry.

```markdown
- S02 move item: [UI-NOTES-05]
  - **Justification** The list screen now shows pinned notes the same way, and a second copy of the rule would drift; Catalog: [UI-NOTES-05]
  - **Touches** [notes][s-notes] → [list-screen][s-list]

[UI-NOTES-05]: proposed-design-specs/screens/list-screen.md#ui-notes-05
[s-notes]: proposed-design-specs/screens/notes.md
[s-list]: proposed-design-specs/screens/list-screen.md
```

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-artifacts-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
