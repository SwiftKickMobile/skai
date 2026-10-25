Managed-By: skai
Managed-Id: guide.change-requests
Managed-Source: Guides/Core/change-requests.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Change Requests

Print `📖 SKAI guide: change-requests` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read for any base or request.

1. **Packages author against a base.** Default: production; a request differs only in its base: another open package of its type, including a request.
2. **Requests have their base's contents and list it as first input.** Production: `skai/changes/<change-id>/<type>/`; requests: `<base>/change-requests/<nnn>/`, in filing order. Any package may hold open `change-requests/` and archived `promoted-change-requests/`.
3. **Name the base: "request a change to <package>".** Reopen a named or contextual request for the same work; otherwise use the next free number. A base defect with no open package starts one against that base.
4. **Whoever runs a package's workflow authors it under the same rules and may edit anything.** To accept part, trim or edit, then promote the rest. Discussion and Decision Log record what stayed, changed or was dropped and why; the originator reads them.
5. **Promotion folds into the base.** The type's promotion guide folds drafts or frames. Into a package, drafts become the base's; append change items with its next IDs, each keeping its own reason and source and ending `; Change request: <nnn> <id>`; a cited decision stays the request's. Name the request in the base's Assumptions, re-render its page and archive at `<base>/promoted-change-requests/<nnn>/`.
6. **Open work moves up into a package.** Append open items and gaps to its Discussion as its own: next `D` numbers, Gap lines kept, transfers logged; footnotes follow: a carried item's new number, `base D3` becoming `D3`; re-file open requests against it at its next numbers.
7. **Requests inherit the base's open gaps like any input's.** Promotion into production allows no open Discussion item, gap or request.
8. **Use the same renderer and checks.** Layer request pages on base drafts; top bar: `<title>: <change-id> | <nnn> | …`.
9. **File a package against each input your decisions change, except your base.** Use its process, or tell the supervisor if none, by your review gate's advance. Before promotion, apply every outcome; an invalidating outcome returns the package to authoring, a missing outcome blocks.

LumenNotes: `skai/changes/reminder-expiry/product-specs/change-requests/001/` holds `product-specs-authoring.md` and `proposed-product-specs/**`; promoted, it moves to the base's `promoted-change-requests/001/`.

## Project Addendum

If `<active-project-root>/skai/addenda/change-requests-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
