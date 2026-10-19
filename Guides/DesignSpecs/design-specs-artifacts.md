Managed-By: skai
Managed-Id: guide.design-specs-artifacts
Managed-Source: Guides/DesignSpecs/design-specs-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-18

# Design Spec Artifact Formats

Print `📖 SKAI guide: design-specs-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

The typed formats the design-spec workflows produce and consume. Content rules and checks:
[`design-specs.md`](design-specs.md); shape and tool: [`spec-file-shape.md`](../Core/spec-file-shape.md).
The package mirrors the product spec package
([`product-specs-artifacts.md`](../ProductSpecs/product-specs-artifacts.md)); only differences are here.

## The Package

`skai/changes/<change-id>/design-specs/`; after promotion, `skai/promoted/<change-id>/design-specs/`.
Packages are independent — never link another package — except a draft requirement cited from an
active product spec package until promotion repoints it, and a change request filed against that
package.

The layout is the product spec package's, with `design-specs-authoring.md` (`## Spec Changes`),
`proposed-design-specs/**` (touched files only, each whole),
`design-specs-review.html`, `change-requests/<nnn>/request.md` with optional
`proposed-design-specs/**` beside it, and `design-specs-promotion.md`. The review page and each
request's `request-review.html` follow the product spec guide's render and link rules. Checked
`C3` in the promotion artifact means the specs are written, `C4` the package archived.

## Spec Change Items

`## Spec Changes` lists exactly the canon/draft differences in package-held files, one typed entry
per difference, by prose and resolved target identity; the rendered page shows each difference
under its justification, so an entry carries no text of its own.

```
- S<n> <operation> <object>: <identity>
  - **Justification** <Source>: <reference or rationale>
  - **Touches** draft-file links; an intro or index line is an entry or a line here
```

- **ID** `S1`, `S2`, …: never renumbered or reused; package-local — work specs cite `UI-*`, never
  `S`. Entries run root, glossary, then folder, file and item order; no checkbox.
- **Operation** `add | modify | retire | move` × **object** `spec file | item | rule | index line |
  glossary entry | known-difference note`. Only items move; a rule changing parent retires and is
  re-added; files never retire. [Modify vs. Retire](design-specs.md#modify-vs-retire) decides; a
  retired glossary entry or note disappears, only items and rules keep `(retired)`.
- **Identity** file titles linked to drafts, item and rule IDs to the draft item heading, terms
  to the draft glossary, index lines by the file described. A `move` puts `from → to` in Touches;
  promotion verifies identical prose and resolved targets and repoints incoming links; move plus
  modify keeps one contract, the move verified first. Draft every design-spec file whose links a move or
  retirement changes, in Touches after it.
- **Source** as the product spec guide; `Catalog` means existing specs or requirements.

`check-changes` confirms the list matches the projection.

**Granularity follows the file.** A new spec file is one entry, its index line in `Touches`;
incoming moves are listed separately. Root creation is one entry (root index, glossary, three
folder indexes). In an existing file, each changed item, rule, glossary entry, index line or
known-difference note is its own entry.

```markdown
- S2 move item: [UI-NOTES-05]
  - **Justification** Catalog: reuse on a second screen would duplicate the rule.
  - **Touches** [notes][s-notes] → [list-screen][s-list]

[UI-NOTES-05]: proposed-design-specs/screens/list-screen.md#ui-notes-05
[s-notes]: proposed-design-specs/screens/notes.md
[s-list]: proposed-design-specs/screens/list-screen.md
```

## Change Requests

Any downstream consumer — work specs, tests, promotion — files a change request for any reason,
against the open package for the screen or, failing one, against the specs, which opens a new
package. Promotion's own failed check is not a request: it blocks and returns the
package to authoring. The proposer never edits the package.

`change-requests/<nnn>/request.md` takes the product spec guide's form — status, response, title,
Goal, Requested Changes as `S<n>` entries, optional drafts beside it diffed on its page — and its
lifecycle: `Proposed` on filing; triaged on the request by authoring to `Incorporated` (once
drafts and Spec Changes reflect it), `Rejected` or `Superseded`; `Proposed` blocks readiness; one
filed on promotion's continue branch rides to completion still `Proposed`, its defect carried by
a new package.

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-artifacts-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
