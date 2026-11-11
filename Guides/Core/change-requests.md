Managed-By: skai
Managed-Id: guide.change-requests
Managed-Source: Guides/Core/change-requests.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-10

# Change Requests

Print `📖 SKAI guide: change-requests` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read for any base or request.

1. **Packages author against a base.** Default production; a request differs only by base: an open package or request of its type.
2. **Requests have the base's layout, only files they change, the base as first input.** Against production: `skai/changes/<change-id>/<type>/`; requests: `<base>/change-requests/<nnn>/`, numbered in filing order across open and promoted. Any package may hold open `change-requests/` and archived `promoted-change-requests/`.
3. **Name the base: "request a change to <package>".** Reopen an open request for the same work, named or in context; else the next free number. A base defect goes to an open package for it or starts one against the base.
4. **Promotion folds into the base.** Type guides fold drafts or frames. Into a package:
   1. The request's drafts overwrite the base's, file by file; append the request's change items at the base's next IDs, reason and source kept, ending `; Change request: <nnn> <id>`; link the request's bare `D<n>` in its drafts and appended items to the request (`[D5][001 D5]`, per 5.1).
   2. Check off items the request decided (5.3) where they live: Decision `<decision> (<nnn>)`, no Gap line or marker; log there `- D12 decided — <decision> (<nnn>)`.
   3. Move the request's open requests to `<base>/change-requests/<nnn>-<their nnn>/`, first input repointed to the base.
   4. Name the request in the base's Assumptions; archive it at `<base>/promoted-change-requests/<nnn>/`, then re-render the base.
5. **Open items and gaps stay where raised, keeping their IDs, even when cited or decided elsewhere.**
   1. Cite other packages' items, the base's too, by link; when copying a base file, link its bare `D<n>` (the base's). Define labels once per file: `[D27][reminder-expiry D27]`, `[reminder-expiry D27]: <cited authoring artifact>#d27`.
   2. Copies, moves and folds keep links, repairing paths.
   3. A request deciding its base's item logs `- [D12][reminder-expiry D12] decided — <decision>` and holds each base file marking it, drafted to the decision, minus the marker.
6. **Requests inherit the base's open gaps like any input's.** Promotion into production allows no open Discussion item, gap or request, even in a promoted request, where the base's author resolves any as that request's own.
7. **Use the same renderer and checks.** Request pages layer on base drafts; top bar: `<title>: <change-id> | <nnn> | …`.
8. **For each input your decisions change, except your base, the supervisor picks: edit it in its workflow or file a request against it.** Ask before your review gate advances. Before promotion apply every outcome; invalidating ones reopen authoring, pending ones block.

LumenNotes: `skai/changes/reminder-expiry/product-specs/change-requests/001/` holds `product-specs-authoring.md` and `proposed-product-specs/features/reminders.md`, the one draft it changes.

## Project Addendum

If `<active-project-root>/skai/addenda/change-requests-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
