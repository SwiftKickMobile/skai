Managed-By: skai
Managed-Id: guide.design-specs-artifacts
Managed-Source: Guides/DesignSpecs/design-specs-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Spec Artifact Formats

Print `- 📖 SKAI guide: design-specs-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

The typed formats the design-spec workflows produce and consume. This is the consumer-facing layer:
a downstream reader resolves any field or value here without reading the authoring method
([`design-specs-authoring.md`](design-specs-authoring.md)). For the specs' own content rules —
layout, item format, IDs, writing style, verification checks — see
[`design-specs.md`](design-specs.md).

## The Package

A change package lives at `skai/changes/<change-id>/design-specs/` in the repository that holds the
specs, and after promotion at `skai/promoted/<change-id>/design-specs/`. It holds:

| Path | What it is |
| --- | --- |
| `design-specs-authoring.md` | authoring's artifact; its `## Spec Changes` lists the **spec change items** |
| `proposed-design-specs/**` | the draft spec files, mirroring the specs' layout |
| `change-requests/design-specs-<nnn>.md` | requests raised by promotion; may be absent |
| `design-specs-promotion.md` | promotion's artifact; may be absent |
| `evidence/` | check output promotion persisted; may be absent |

Packages are decoupled. A spec package never points at another package and never assumes a sibling
`requirements/`, `design/` or `ui-map/` package exists; where a drawing was made — production or a
change page — is incidental and the spec never references it. The one link that may cross: a spec
may cite a requirement ID that so far exists only as a draft in an active requirements package. The dependency is on the ID, which is permanent from first drafting; the link targets the
draft until promotion repoints it.

In `design-specs-promotion.md`, checked `C3` means the specs are written; checked `C4` means the
package is moved and its references repaired.

## Spec Change Items

`## Spec Changes` lists exactly the differences between the specs and the drafts under
`proposed-design-specs/`, one typed entry per difference. The comparison covers **only the files the
package holds**, by prose and resolved link targets, ignoring only relative-path changes caused by
draft/canonical location. Each entry:

```
- S<n> <operation> <object>: <identity>
  - **Description** what changes, with the text inline (see *Showing the Diff*).
  - **Justification** <Source>: <reference or rationale>
  - **Touches** links to the draft files affected. An index line or intro paragraph this item
    changes rides here rather than earning an item of its own.
```

- **ID** — `S1`, `S2`, … in document order, never renumbered or reused. An `S` ID identifies a
  change in this package and nothing else: work specs cite `UI-*` items and sub-IDs, never `S` items.
- **Operation** — `add` | `modify` | `retire` | `move`.
- **Object** — `spec file` | `item` | `sub-item` | `index line` | `glossary entry` |
  `known-difference note`. Not every pair exists: `move` applies to items and sub-items only, never
  files; `retire` never applies to a file, since a package cannot delete one. Choosing `modify` or
  `retire` for an item follows *Modify vs. Retire* in [`design-specs.md`](design-specs.md).
  Retiring a glossary entry or a known-difference note removes it; only items and sub-items keep
  their place and take `(retired)`.
- **Identity** — a link to the draft: the file title linked to the draft file; the item or sub-item
  ID linked to its draft heading (`[UI-NOTES-01.02]` → `…/notes.md#ui-notes-01`); the glossary term
  linked to the draft glossary; an index line by the file it describes.
- **Source** (the leading token of Justification) — the requirements artifacts' vocabulary:
  `Design` | `Implementation` | `Supervisor input` | `Resolved decision` | `Agent inference` |
  `Change request` | `Catalog`. `Resolved decision: D#` cites a resolved Discussion item. `Catalog`
  is the existing specs or the requirements catalog. `Agent inference` carries a real rationale and
  is the first place a reviewer looks.

Entries are written top-down in the specs' order — root, glossary, then folder by folder, file by
file, item by item. Items carry **no checkbox**: the change is realized by the draft files.

Discussion, Inputs and Justification may name frames, nodes and code files. The product-language and
copy rules govern the spec files and the quoted proposed text, not the package's own prose.

### Granularity Follows the File

A spec file the specs do not yet have is one item, its index line riding in `Touches` — listing its
items individually restates the draft. The package that creates the specs root is one item too, with
`_design-specs.md`, `glossary.md` and the three folder indexes riding in it. Inside a file the specs
already have, each item, sub-item, glossary entry, index line or known-difference note added,
changed, retired or moved is its own entry, carrying its text.

**Baseline example** (LumenNotes, excerpt):

```markdown
## Spec Changes

Baseline: every file is new.

- S1 add spec file: [root][s-root]
  - **Description** Creates the specs root with `_design-specs.md`, `glossary.md` and the three
    folder indexes; `screens/` populated by this package.
  - **Justification** Catalog: the requirements root index's product paragraph; the design file.
  - **Touches** [root][s-root], [glossary][s-glossary], [screens][s-screens], [shared][s-shared],
    [global][s-global]

- S2 add spec file: [List Screen][s-list]
  - **Description** Rules every list screen shares: group headings, the empty state, staleness and
    loading. Prefix `UI-LIST-`.
  - **Justification** Design: the `notes` and `trash` columns share one shell; Implementation: one
    list screen serves both.
  - **Touches** [list-screen][s-list], [screens][s-screens]

- S3 add spec file: [Notes][s-notes]
  - **Description** The notes list: rows, the reminder badge, the empty state. Prefix `UI-NOTES-`.
  - **Justification** Resolved decision: [D1], [D2] — the pinned row and the badge precedence.
  - **Touches** [notes][s-notes], [screens][s-screens], [glossary][s-glossary]

[s-root]: proposed-design-specs/_design-specs.md
[s-glossary]: proposed-design-specs/glossary.md
[s-screens]: proposed-design-specs/screens/_screens.md
[s-shared]: proposed-design-specs/shared/_shared.md
[s-global]: proposed-design-specs/global/_global.md
[s-list]: proposed-design-specs/screens/list-screen.md
[s-notes]: proposed-design-specs/screens/notes.md
[D1]: #pinned-rows
[D2]: #reminder-badges
```

### Showing the Diff

In a scoped change the entry shows what changed, inline. Context is the identity link plus
`Touches`; neighbouring items are never restated.

- **Unchanged → omit entirely.** Omission is the signal.
- **Added → quote the new text.**
- **Modified → the old text struck through, immediately followed by the new text.**
- **Retired → the text struck through.** The ID is burned.
- **Move → identity unchanged, text omitted, `Touches` reads `from → to`.** Promotion verifies the
  text identical (prose plus resolved link targets) and repoints incoming links. A move that also
  changes the text is two items: the move, then the modify.

**Scoped-change example** (LumenNotes, excerpt; the Discussion has `### Reminder badges` and
`### Stale notice` topics):

```markdown
- S1 modify sub-item: [UI-NOTES-01.02]
  - **Description**
    ~~The row's date reads `{Today|Yesterday}` for those days, the weekday name within the last
    week, and `{Mon D}` otherwise, with the year added when it is not the current one.~~
    The row's date reads `{Today|Yesterday}` for those days, the weekday name within the last
    week, and `{Mon D}` otherwise; the year is never shown.
  - **Justification** Resolved decision: [D3]
  - **Touches** [notes][s-notes]

- S2 retire item: [UI-NOTES-04]
  - **Description** ~~The reminder badge is hidden while the list is stale.~~
  - **Justification** Resolved decision: [D3] — the badge's state is the requirements' and does not
    depend on staleness.
  - **Touches** [notes][s-notes]

- S3 add sub-item: [UI-NOTES-02.02]
  - **Description** > A row whose reminder is acknowledged keeps the badge until the list is next
    refreshed ([REMIND-06]).
  - **Justification** Design: `notes — acknowledged reminder`.
  - **Touches** [notes][s-notes]

- S4 move item: [UI-NOTES-05]
  - **Description** The stale notice, now shown on every list screen.
  - **Justification** Catalog: a second screen now shows the notice, so the rule would be written twice.
  - **Touches** [notes][s-notes] → [list-screen][s-list]

- S5 add glossary entry: [Stale notice][s-glossary]
  - **Description** > **Stale notice** — the line giving a list's age, above its first group while
    the list is stale ([UI-NOTES-05]).
  - **Justification** Catalog: the notice is now cross-cutting.
  - **Touches** [glossary][s-glossary]

- S6 modify known-difference note: [UI-NOTES-03]
  - **Description** ~~> **Known difference — Android:** the empty state is shown without the
    message. Tracked in [empty-message].~~ (removed: fixed and verified on Android.)
  - **Justification** Implementation: Android 3.2 shows the message.
  - **Touches** [notes][s-notes]

[UI-NOTES-01.02]: proposed-design-specs/screens/notes.md#ui-notes-01
[UI-NOTES-02.02]: proposed-design-specs/screens/notes.md#ui-notes-02
[UI-NOTES-03]: proposed-design-specs/screens/notes.md#ui-notes-03
[UI-NOTES-04]: proposed-design-specs/screens/notes.md#ui-notes-04-retired
[UI-NOTES-05]: proposed-design-specs/screens/list-screen.md#ui-notes-05
[REMIND-06]: ../../../requirements/features/reminders.md#remind-06
[s-notes]: proposed-design-specs/screens/notes.md
[s-list]: proposed-design-specs/screens/list-screen.md
[s-glossary]: proposed-design-specs/glossary.md
[D3]: #reminder-badges
```

## Change Requests

A change request is what **promotion** raises when the existing specs — not the package — turn out
to be wrong: an item promoted earlier contradicts what is landing now, or is inconsistent with what
promotion is about to write. Authoring consumes it when the package returns to authoring; one raised
on promotion's continue branch rides through to completion still `Proposed`, and the defect it names
is carried by a new scoped-change package.

That is its only raiser. A defect *in the package* needs no request — promotion blocks and the
package returns to authoring. A spec defect found anywhere else opens a new scoped-change package.
Known-difference notes removed by implementation after a verified fix are not change requests.

One markdown file per request, `skai/changes/<change-id>/design-specs/change-requests/design-specs-<nnn>.md`,
with two inline `Label: value` fields above a free-form body stating the concern, the IDs involved
and the requested change:

```
Change Request Status: Proposed
Reviewer Response: <filled by authoring on reopen>
```

`Change Request Status` is exactly one of `Proposed | Incorporated | Rejected | Superseded`. The
request opens `Proposed`; on reopen, authoring fills `Reviewer Response` and moves the status to
`Incorporated` (only once the adjustment is in the drafts *and* in `## Spec Changes`), `Rejected`,
or `Superseded`. A request left `Proposed` blocks promotion.

## Cross-References

- [`design-specs.md`](design-specs.md) — content rules and verification checks
- [`design-specs-authoring.md`](design-specs-authoring.md) — the authoring workflow
- [`design-specs-promotion.md`](design-specs-promotion.md) — the promotion workflow
- [`requirements-artifacts.md`](../Requirements/requirements-artifacts.md) — the formats these mirror

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-artifacts-addendum.md` exists, read it and immediately print
`- 📎 Addendum loaded` as a line of its own, nested under this guide's line; its rules are part of this
guide and win any conflict.
