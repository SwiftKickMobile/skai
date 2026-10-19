# Spec Format And Tool Design

## Purpose

The standard for the shared **spec file shape** that product specs and design specs both follow,
and for the **spec tool** that validates it, lists citations, links glossary terms, and renders
change packages and change requests for human review. It is used to write and cold-review the shape
guide and the tool; it is not something an operator reads at runtime.

Decided 2026-10-18 from the Offers retrospective in the SalesPro checkout
(`working-docs/requirements-process/`: `planning.md` for decisions, `format.md` for the shape draft,
`fixtures/` for samples, `tools/spec_tool.py` for the prototype). The shape guide is the first
refinement target, before the product spec and design spec guides, because both depend on it.

## Authority and references

- [`product-specs-system-design.md`](product-specs-system-design.md) and
  [`design-specs-design.md`](design-specs-design.md) — the two consumers; their invariants about
  IDs, retirement and one-home-per-fact are inherited, not restated here.
- [`internal/maintain-skai.md`](../../internal/maintain-skai.md) — house style; `Bin/ui-map-render.py`
  is the precedent for a tool shipped beside the guides, with its render conventions in its docstring.

## Why one shape

The catalog guide said a requirement is an ID heading with prose and argued against bullet lists;
it never mentioned tables. The design-spec guide, written later, added numbered sub-rules and tables
because screens map conditions to states. Requirements have the same need (seven stages, six offer
amounts, six statuses) and never got it: the Offers draft turned the stage list into nine
requirements. The difference was historical, not principled; nothing in the catalog's reasoning
(stable IDs, one ID per claim, findability) excludes tables once rows carry no IDs. One shape, one
parser, one renderer, and both guide sets cite the shape guide instead of each restating it.

## Decisions

1. **Elements**, in file order: one `#` Title Case title; intro paragraphs (orientation, never
   binding); optional `##` sections with a Title Case name and no ID, each may open with one
   orientation line, never cited or diffed; `###` items carrying only the ID or `ID (retired)`; a
   statement (required, even when the detail is a table); then tables and rules in any order; then
   known-difference blockquotes; link definitions grouped at the end.
2. **Rules.** `- **NN**` bullets numbered from `01`, nested one level by two-space indent and numbered
   `01` again, cited as `ID-NN` and `ID-NN-NN` with dashes; no deeper. Append-only; retired in place
   as `- **NN** (retired) <explanation>`. A rule may name a sibling by its bold number.
3. **Tables.** Header and separator rows required; the first column is the key, unique within the
   table; rows carry no IDs and are never cited — the item owns the claim; order binds only when the
   statement says so. A cell may point at a rule in the same item by its bold number. A table may
   follow the statement or a rule it supports. A bare bold number in a cell or a rule points at a
   top-level rule of the same item; a nested rule is pointed at as `01-01` (settled 2026-10-18, target 1).
4. **Glossary.** `glossary.md` (or, when split per folder along the section seams of design-specs
   decision 5, every `glossary.md` under the root, read as one glossary) entries are `###` headings in sentence case, one paragraph each
   ending with the governing items, alphabetical within the file or, when the file uses optional `##`
   sections (design specs: Global, Shared, one per screen family, per design-specs-design decision
   5), alphabetical within each section (settled 2026-10-18, target 2). Every occurrence of a term in spec prose links the
   entry (`[term][g-anchor]`); the link is the signal that a word is a defined term; the governing
   items are exempt. A word used in its ordinary sense is reworded or linked; the validator does not
   distinguish.
5. **Indexes.** `_<folder>.md`: one reminder line, then `- [name] -- \`PREFIX-\` -- questions` per
   file and `- [name] -- questions` per folder. An app's index also lists the feature files it offers.
6. **IDs and anchors.** `<PREFIX>-<NN>` (design specs: `UI-<PREFIX>-<NN>`), two digits zero-padded,
   three past 99, unique across the catalog; anchor is the lowercased heading, `-retired` when
   retired; a rule citation links the parent item's anchor. Modify keeps the ID; a changed contract
   retires and adds, at item and rule level alike.
7. **Markdown stays the source.** No YAML or JSON authoring format; the shape above is the grammar
   and the tool is its parser. A structured export is derivable if a service ever needs one.
8. **Validator rejects:** a heading that does not fit the shape; an item without a statement; a
   duplicate ID across the projected catalog; rule numbers not two digits, out of sequence, or nested
   too deep; a table without header and separator, with an empty or duplicate key; a link used but
   undefined or defined but unused; a glossary entry out of order, not a heading, or not sentence
   case; an unlinked glossary term occurrence; a progress marker in spec prose. Every failure names
   file and line. Validating a package means validating the **projection**: later roots overlay
   earlier ones, so the drafts replace their catalog files for uniqueness and glossary checks.
   **Scope of blocking** (settled 2026-10-18, target 2): a failure blocks a package only when it is
   in a file the package holds or is a conflict the projection introduces (a duplicate ID, a dangling
   link, an unlinked term across the projection). A per-file fault in an untouched canonical file, including an
   unlinked occurrence of a term the package introduces, is reported, never blocks, and becomes a
   change request or is linked when that file is next touched; a package is never blocked by a defect it
   did not introduce (product-specs P2, design-specs decision 10).
9. **Commands.** (Amended 2026-10-18: `render` locates the package's authoring artifact itself when the drafts folder sits inside a package folder, so a review render always carries the card, discussion and justifications; `--authoring` remains only to point elsewhere or, with `--no-authoring`, for a bare drafts-to-catalog comparison that is never the committed page.) `validate ROOT...`, `references ID-OR-TERM ROOT...` (every citing file and line of an ID, or every linked occurrence of a glossary term, including
   rule citations), `link-terms ROOT...` (rewrite files so every term occurrence is linked),
   `render --catalog --drafts [--authoring] --out`, `render-request --catalog --package-drafts
   --request --out`. One script in `Bin/` beside the UI Map renderer; render conventions in its
   docstring, as that renderer does.
10. **When it runs.** Validation at the authoring gate and before promotion writes, for both spec
    types; a failure within the package's scope (decision 8) blocks. `references` before any modify or retire. `link-terms` during drafting
    and migration.
11. **Diffing.** File by path; intro by text; item by ID (added, modified, retired, missing);
    statement by word; rule by `ID-NN`; table row by key (added, removed, changed cells); known
    difference by parent and app; glossary entry by term; index line by link name. Glossary link
    markup is not content: a term gaining a link is not a change. Link-definition path changes are
    ignored unless the target identity changes. Sections are not diffed (name, order, membership);
    a section's orientation line is prose and diffs like the intro. A reordered table row is always
    shown as moved; the tool cannot read whether the statement binds order, so the reviewer judges
    (settled 2026-10-18).
12. **Package page.** Title `Change Package: <id>`. A legend row of counts (added, modified, retired
    or removed, unchanged, added files), each with its colored square. A card with the package's
    status (open item count, or ready for promotion), title, goal and discussion count. The `## Situations`
    section, when present, rendered after the card as written (added 2026-10-18, target 3). A "Documents"
    box, one linked line per file with its square and changed count. The discussion items, each with its
    square, kind, title and status, expanded to show its concern, proposal, options, why and decision
    as written in the artifact, so the supervisor can resolve an item from the page (amended
    2026-10-18, target 3; previously a table of titles). Then each file: its intro, its sections with their descriptions,
    and its items in file order — changed items expanded, unchanged and retired items collapsed in
    place so links to them resolve and open on arrival. Each change's justification from the
    authoring artifact sits under its card; a new file's under its heading.
13. **Request page.** Title `Change Request: <nnn>` with `Change Package: <id>` beneath; the same
    card with status, title, goal and reviewer response; the Documents box; then the request's drafts
    diffed against the package's drafts, falling back to the catalog, with each requested change's
    justification under its card. A request without drafts shows, after the card, one card per Requested Changes entry (identity, type, justification) so the page still says what is asked (settled 2026-10-18, target 2).
14. **Rendering conventions** (supervisor, 2026-10-18, by iteration on the fixtures): status is a
    small colored square, never a text pill — green added, amber modified, red retired or removed,
    gray unchanged — leading the file heading, item, rule or table row it marks, with no square on
    rows or rules inside an item that is itself new; cards are white on a very light gray page with
    a soft shadow; section headings and descriptive text are normal weight and color, sections in
    uppercase; whole deletions are gray strikethrough with no tint, including the ID; inside a
    modified block, removed words carry a light red tint with strikethrough and added words a light
    green tint, at normal weight; every citation and glossary term that resolves is a link, styled as
    a chip or a dotted term, and opens a popover card on hover showing the full cited item (statement,
    tables, rules, with a cited rule outlined) or the glossary entry; citations that cannot resolve
    are plain muted text, never styled as links; the browser's own tooltip is not used; rule numbers
    and tables are body size; dark mode follows the system setting with the same relationships.
15. **Committed renders.** (For one release after the rename, the tool also accepts the legacy package names `requirements-authoring.md` and `proposed-requirements/`; a change request's drafts folder is `proposed-product-specs/` from the start, since it is new.) The tool renders a package's page into the package folder as
    `product-specs-review.html` (design specs: `design-specs-review.html`) and a request's as
    `request-review.html` beside its `request.md`; both are committed with the package, re-rendered
    at the authoring gate and last before promotion's readiness screen; never after the write, so the
    page that archives with the package keeps the diff the supervisor approved (settled 2026-10-18,
    target 4). After the write, promotion confirms with `validate` on the catalog. The authoring artifact's change
    section opens with a link to the page and holds only ID, type, identity, justification and
    touched files; it never inlines old or new text (supervisor, 2026-10-18). Promotion's
    list-matches-diff check is the tool's `check-changes`: every added, modified or retired item,
    glossary entry, index line or file in the projection has a list entry (an index line or intro: an
    entry or a Touches line) and no entry names an unchanged or absent one (settled 2026-10-18).
16. **Converter.** The migration rewrites an existing catalog mechanically: `##` items to `###`,
    rule citations from dots to dashes, glossary entries to headings, `link-terms`, and validates the
    result; it reorganizes nothing. Reorganization (folding separate requirements into a table) is
    authoring work in a package.

## Guide Shape

One runtime guide holding the shape, under `Guides/Core/` (or a new `Guides/Specs/` if the
maintainer prefers a home shared by both consumers), cited by the product spec catalog guide and the
design spec content guide, which keep only the judgment rules that differ (scopes, writing style,
what counts as a state). Examples use LumenNotes. The tool's docstring is the render spec; the guide
does not restate it.

## Acceptance checks for the guide and tool

1. Every element in decision 1 has one faithful LumenNotes example in the guide, and the validator
   rejects every case in decision 8 with file and line (the fixtures' broken set).
2. The product spec and design spec guides cite the shape guide and restate none of it.
3. A package validated alone and validated projected on its catalog give the results decision 8
   describes.
4. A rendered package and a rendered request match decisions 12 to 14; a reviewer can approve a
   package from the page alone.
5. `references` finds rule citations as well as item citations.
6. The converter run over a catalog produces a validating catalog with no prose change.


17. **Layered bases (supervisor, 2026-10-18).** `render` and `check-changes` take `--base DIR`
    (repeatable): further roots layered over the catalog, later ones winning, so a package can be
    drafted on top of another open package's drafts and diff against them, as `validate` already
    projects several roots. Promotion order is the packages' own concern.
18. **Artifact prose on the page (supervisor, 2026-10-19).** Discussion items, Situations,
    change-item justifications and a request's head get the same chips and dotted terms as spec
    prose: a bare ID and every glossary term are linked at render time, outside links and code; the
    artifact file is not edited (render convention 8). Two defects fixed on the way: `check-changes`
    matched a glossary term, an index line and a section sharing a name as one thing (now matched by
    kind); `link-terms` re-wrapped a term inside a longer term's link (now treated as linked).

19. **Discussion items on the page (supervisor, 2026-10-19).** Each item is a collapsible card
    whose summary line carries its state: the square (green resolved, amber open), the ID, the
    kind, the title, and the word "resolved" or "open" at the end; resolved items start collapsed,
    open items start expanded. The body (Concern, Options, Proposal, Why, Decision) shows on
    expand. Reason: the list grows long and the state was hard to see.

20. **Popover delay (supervisor, 2026-10-19; skai#84).** A popover opens only after the pointer has
    rested on its chip or term for about 400 ms, and a pending open is cancelled when the pointer
    leaves first, so moving across the page does not pop a trail of cards; keyboard focus opens at
    once; hiding stays immediate. Chips and terms inside an open popover open nothing (no nested
    popovers) and do not close it.

## Open

- Whether the judgment half of the catalog guide's layout section (topic-file sizing, index lines
  that name questions, glossary as second index) moves here since it also applies to design specs.
- Rendering a catalog for browsing, as opposed to a package for review, is not designed.

## Size Budgets — 2026-10-18

Set by the supervisor from four efficiency reviews (SalesPro checkout, `working-docs/requirements-process/reviews/`), as today's size less measured obsolete content, less the reviewed trim on what remains, plus known growth. Whole-file bytes by `wc -c`, managed header and addendum footer included. They bind every repair per the refinement guide's size-budget rule.

| Target 1 | Cap |
| --- | --- |
| Guides/Core/spec-file-shape.md | 8,200 |

**Live render (supervisor, 2026-10-18).** The rendered page is the primary way the supervisor views a change package while it is being iterated on. Any time the package materially changes — a draft edited, a discussion item resolved, a change item added, a request triaged — the agent validates and re-renders before anything else, in every workflow that writes a package. The gate and promotion renders are not the only ones; they are the last of many. Validation and rendering take milliseconds, so there is no cost argument for deferring them.
