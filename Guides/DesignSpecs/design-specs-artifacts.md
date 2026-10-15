Managed-By: skai
Managed-Id: guide.design-specs-artifacts
Managed-Source: Guides/DesignSpecs/design-specs-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Spec Artifact Formats

Print `📖 SKAI guide: design-specs-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

The typed formats the design-spec workflows produce and consume. This is the consumer-facing layer:
a downstream reader resolves any field or value here without reading the authoring method
([`design-specs-authoring.md`](design-specs-authoring.md)). For the specs' own content rules —
layout, item format, IDs, writing style, verification checks — see
[`design-specs.md`](design-specs.md).

## The Package

In the specs repository: `skai/changes/<change-id>/design-specs/`; after promotion:
`skai/promoted/<change-id>/design-specs/`.

| Path | Contents |
| --- | --- |
| `design-specs-authoring.md` | Authoring artifact; typed items in Spec Changes |
| `proposed-design-specs/**` | Drafts mirroring spec paths |
| `change-requests/design-specs-<nnn>.md` | Promotion requests, if any |
| `design-specs-promotion.md` | Promotion artifact, if present |
| `evidence/` | Persisted promotion output, if any |

Packages are independent: never link another package or assume sibling requirements, design or
UI Map packages. Drawing location is incidental and never referenced by specs. Sole exception:
cite permanent requirement IDs in active drafts until promotion repoints them to canon.

Checked `C3` means specs written; checked `C4` means package moved and references repaired.

## Spec Change Items

Spec Changes records exactly the canon/draft differences in package-held files, by prose and
resolved targets; ignore only location-required relative paths. One typed entry per difference:

```
- S<n> <operation> <object>: <identity>
  - **Description** changed text inline (Showing the Diff)
  - **Justification** <Source>: <reference or rationale>
  - **Touches** affected draft-file links; incidental intro changes ride here
```

- **ID:** `S1`, `S2`, …; never reuse or renumber. Package-local only:
  work specs cite `UI-*`, never `S`.
- **Operation:** `add | modify | retire | move`.
- **Object:** `spec file | item | sub-item | index line | glossary entry | known-difference note`.
  Only items move; sub-items changing parent retire-and-add. Files cannot retire/delete.
  Follow [Modify vs. Retire](design-specs.md#modify-vs-retire). Retired glossary entries and
  known-difference notes disappear; only items/sub-items remain with `(retired)`.
- **Identity:** link file titles to drafts, item/sub-item IDs to draft item headings
  (`[UI-NOTES-01.02]` → `…/notes.md#ui-notes-01`), terms to the draft glossary,
  and index lines by the file described.
- **Source:** `Design | Implementation | Supervisor input | Resolved decision | Agent inference |
  Change request | Catalog`. `Resolved decision: D#` cites resolved Discussion.
  Catalog means existing specs or requirements. Agent inference needs a real rationale and
  draws first reviewer scrutiny.

Order entries root, glossary, then folder/file/item order. No checkboxes: drafts realize changes.
Discussion, Inputs and Justification may name frames, nodes and code files; product-language/copy
rules govern specs and quoted proposed text.

### Granularity Follows the File

New spec files get one entry each, index lines in Touches; list incoming moves separately, not new
items. Root creation covers root index, glossary and three folder indexes in one entry. Existing
files get an entry per changed item, sub-item, glossary entry, index line or known-difference note.

**Baseline example** (LumenNotes, excerpt):

```markdown
## Spec Changes

Baseline: every file is new.

- S1 add spec file: [root][s-root]
  - **Description** Creates root index, glossary and three folder indexes; populates screens.
  - **Justification** Catalog: requirements root product paragraph; design file.
  - **Touches** [root][s-root], [glossary][s-glossary], [screens][s-screens], [shared][s-shared],
    [global][s-global]

- S2 add spec file: [List Screen][s-list]
  - **Description** Shared list rules: group headings, empty state, staleness, loading. `UI-LIST-`.
  - **Justification** Design: notes and trash share a shell; Implementation: one list serves both.
  - **Touches** [list-screen][s-list], [screens][s-screens]

[s-root]: proposed-design-specs/_design-specs.md
[s-glossary]: proposed-design-specs/glossary.md
[s-screens]: proposed-design-specs/screens/_screens.md
[s-shared]: proposed-design-specs/shared/_shared.md
[s-global]: proposed-design-specs/global/_global.md
[s-list]: proposed-design-specs/screens/list-screen.md
```

### Showing the Diff

Changes inside an existing file show their text inline; a new file's entry summarizes it, since its
identity links the whole draft. Identity and Touches supply context. Omit unchanged content,
including neighbouring items.

- **Add:** quote new text.
- **Modify:** struck-through old text immediately followed by new.
- **Retire:** strike through text; burn the ID.
- **Move:** unchanged identity, omitted text, Touches `from → to`. Promotion verifies identical
  prose/resolved targets and repoints incoming links. Use move plus modify only for the same contract. Verify move identity before applying the
  declared modify; final endpoints need not have identical text.

For moves and retired headings, draft incoming-link spec files; list in Touches after any move pair.

**Scoped example** (LumenNotes; Discussion topics: Reminder badges, Stale notice):

```markdown
- S1 modify sub-item: [UI-NOTES-01.02]
  - **Description**
    ~~The row's date reads `{Today|Yesterday}` for those days, the weekday name within the last
    week, and `{Mon D}` otherwise, with the year added when it is not the current one.~~
    The row's date reads `{Today|Yesterday}` for those days, the weekday name within the last
    week (`{Monday}`), and `{Mon D}` otherwise, with the year added when it is not the current one.
  - **Justification** Resolved decision: [D3]
  - **Touches** [notes][s-notes]

- S2 retire item: [UI-NOTES-04]
  - **Description** ~~The reminder badge is hidden while the list is stale.~~
  - **Justification** Resolved decision: [D3] — requirements govern badge state, independently of staleness.
  - **Touches** [notes][s-notes]

- S3 add sub-item: [UI-NOTES-02.02]
  - **Description** > A row whose reminder is acknowledged keeps the badge until the list is next
    refreshed ([REMIND-06]).
  - **Justification** Design: `notes — acknowledged reminder`.
  - **Touches** [notes][s-notes]

- S4 move item: [UI-NOTES-05]
  - **Description** The stale notice, now on every list screen.
  - **Justification** Catalog: reuse on a second screen would duplicate the rule.
  - **Touches** [notes][s-notes] → [list-screen][s-list]

- S5 add glossary entry: [Stale notice][s-glossary]
  - **Description** > **Stale notice** — the line telling the person a list is out of date
    ([UI-NOTES-05]).
  - **Justification** Catalog: now cross-cutting.
  - **Touches** [glossary][s-glossary]

[UI-NOTES-01.02]: proposed-design-specs/screens/notes.md#ui-notes-01
[UI-NOTES-02.02]: proposed-design-specs/screens/notes.md#ui-notes-02
[UI-NOTES-04]: proposed-design-specs/screens/notes.md#ui-notes-04-retired
[UI-NOTES-05]: proposed-design-specs/screens/list-screen.md#ui-notes-05
[REMIND-06]: ../../../requirements/features/reminders.md#remind-06
[s-notes]: proposed-design-specs/screens/notes.md
[s-list]: proposed-design-specs/screens/list-screen.md
[s-glossary]: proposed-design-specs/glossary.md
[D3]: #reminder-badges
```

## Change Requests

Only promotion raises requests, for existing-spec defects affecting the write; authoring consumes
them on return. Package defects instead block and return directly to authoring. Spec defects
found elsewhere need new scoped packages. Verified implementation cleanup of known-difference
notes is not a request.

Use one file at `skai/changes/<change-id>/design-specs/change-requests/design-specs-<nnn>.md`.
Above a free-form concern, affected IDs and requested change, put:

```
Change Request Status: Proposed
Reviewer Response: <filled by authoring on reopen>
```

Status is exactly `Proposed | Incorporated | Rejected | Superseded`. Authoring fills the response
and changes status on reopen; Incorporated requires both drafts and Spec Changes updated.
Proposed blocks readiness. A request raised later on promotion's continue branch may finish
Proposed; its defect goes to a new scoped package.

## Cross-References

- [`requirements-artifacts.md`](../Requirements/requirements-artifacts.md) — inherited format conventions

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-artifacts-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
