Managed-By: skai
Managed-Id: guide.change-requests
Managed-Source: Guides/Core/change-requests.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-11

# Change Requests

Print `📖 SKAI guide: change-requests` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read for any base or request.

1. **Packages author against a base, their first input.** A change's package (`skai/changes/<change-id>/<type>/`) or a request's sub-package builds on the nearest package of its type above it, else production.
2. **A request is a folder `CR-<id>/` with one sub-package per type it changes,** each in its type's layout with only files it changes. It sits in its parent's `changes/` until promoted; the parent is the change or, against a request, that request (`skai/changes/<change-id>/changes/CR-01/changes/CR-01-01/`). IDs are the parent's next free two digits across its open and promoted requests, whatever their types, after the parent's ID when nested. A type kept in another repository uses the same path there.
3. **When the supervisor's words don't say whether work is a request, ask before creating or reopening anything.** For a request, reopen an open one for the same work, named or in context, never a promoted one; else file a new one. A base defect goes to an open package for it or starts one against the base.
4. **Promotion folds a sub-package into its base, then moves it to its parent's `promoted/`, or, into production, under `skai/promoted/<change-id>/`; with it go the promoted sub-packages folded into it, paths kept.** A request's sub-packages promote together unless the supervisor asks otherwise; its other types stay. When a request's last sub-package moves, its open requests move to its parent's `changes/`, IDs kept (`changes/CR-01/changes/CR-01-01/` becomes `changes/CR-01-01/`), first inputs repointed to new bases. Type guides fold drafts or frames. Into a package:
   1. The request's drafts overwrite the base's, file by file; append the request's change items at the base's next IDs, reason and source kept, ending `; Change request: CR-01 <id>`; link to the request its bare `D<n>` in its drafts and appended items (`[D5][CR-01 D5]`, per 5.1).
   2. Check off items the request decided (5.3) where they live: Decision `<decision> (CR-01)`, no Gap line or marker; log there `- D12 decided — <decision> (CR-01)`.
   3. Name the request in the base's Assumptions; re-render the base after the move.
5. **Open items and gaps stay where raised, keeping their IDs, even when cited or decided elsewhere.**
   1. Cite other packages' items, the base's too, by link; when copying a base file, link its bare `D<n>` (the base's). Define labels once per file: `[D27][reminder-expiry D27]`, `[reminder-expiry D27]: <cited authoring artifact>#d27`.
   2. Copies, moves and folds keep links, repairing paths.
   3. A request deciding its base's item logs `- [D12][reminder-expiry D12] decided — <decision>` and holds each base file marking it, drafted to the decision, minus the marker.
6. **Requests inherit the base's open gaps like any input's.** Into production, a package allows no other open request part of its type in the change, nor an open Discussion item or gap in it or any promoted part of its type there; resolve those where raised.
7. **Use the same renderer and checks.** Request pages layer on the drafts of every package rule 1 walks, nearest winning; top bar: `<title>: <change-id> | CR-01 | …`.
8. **For each input your decisions change, except your base, the supervisor picks: edit it in its workflow or file a request against it.** Ask before your review gate advances. Before promotion apply every outcome; invalidating ones reopen authoring, pending ones block.

LumenNotes: `skai/changes/reminder-expiry/changes/CR-01/product-specs/` holds `product-specs-authoring.md` and `proposed-product-specs/features/reminders.md`, the one draft it changes.

## Project Addendum

If `<active-project-root>/skai/addenda/change-requests-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
