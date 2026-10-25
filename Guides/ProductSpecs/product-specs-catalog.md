Managed-By: skai
Managed-Id: guide.product-specs-catalog
Managed-Source: Guides/ProductSpecs/product-specs-catalog.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Product Specs Catalog

Print `📖 SKAI guide: product-specs-catalog` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

A project's **product specs** are its library of behavioral requirements — what the system
must do, observed from the outside — written for the agent implementing, debugging or testing.
Each ID'd item is a **requirement**. This guide owns what the catalog contains, how it is organized
and how a requirement is written. How a spec file is laid out — headings, rules, tables, known
differences, links, IDs, glossary and index form, and the validating tool — is
[`spec-file-shape.md`](../Core/spec-file-shape.md), cited here and never restated. No gates; not
a workflow.

[`product-specs-authoring.md`](product-specs-authoring.md) drafts into a change package;
[`product-specs-promotion.md`](product-specs-promotion.md) writes the catalog. Work-spec implementation
may update or remove known-difference notes after verified fixes; other text and IDs are
read-only. Rules bind new or changed content: a defect in an untouched canonical
file never blocks a package; a package against the base fixes it ([`change-requests.md`](../Core/change-requests.md)); release migrations are separate.

The catalog holds behavior that survives a future rewrite. A constraint that exists only for the
duration of one change — migration steps, refactor decisions, intermediate constructs — belongs in
the work spec.

## Scopes

Every requirement lives in exactly one scope:

- **`platform`** — protocol, infrastructure and format contracts, the same for every app and
  feature. *"All persisted documents must round-trip losslessly through the canonical format."*
- **`domains`** — what things are: entities, invariants, valid state transitions, relationships.
  *"A Note in `draft` may transition to `published` or `discarded`, never straight to `archived`."*
- **`features`** — capabilities a user can do, shared by more than one app. *"Users can mark notes
  as favorites; favorited notes appear in a dedicated list, most recent first."*
- **`apps`** — behavior of a single app. *"In LumenNotes for iPad, the sidebar collapses below a
  compact width."*

Choose the first that fits. **Feature vs. domain** is the line most
often confused: a rule that still applies with no UI is a domain rule; one that only matters because
a user is interacting is a feature. Complex behavior often needs both, citing each other.

An app's index lists the shared feature files that app offers; a feature absent from an app's index
is not in that app. `features/` exists so shared behavior is written once. Never organize by
project, module, framework, team or codebase.

## Layout

```
skai/product-specs/                the fixed root, in the repository the README links
  _product-specs.md                root index
  glossary.md                     second index
  platform/   _platform.md  <topic>.md
  domains/    _domains.md   <entity>.md
  features/   _features.md  <feature>.md
  apps/       _apps.md      <app-name>/  _<app-name>.md  <subject>.md
```

A file that outgrows itself becomes a folder with its own index (`features/widgets.md` →
`features/widgets/_widgets.md`); a change package cannot express that split, so it stops at a
blocked gate (see authoring).

### Topic files are subjects, not screens

A topic file covers one coherent area of behavior — authentication, purchase, scheduling — never one
screen or class. Typical size is two to a dozen requirements: a file with one usually merges into a
neighbor; one with thirty usually splits.

### Indexes route

The root index holds a product paragraph, which scopes this catalog uses, and a pointer to the
glossary. Each scope and app index carries a one-line reminder of the scope, then one line per file
or folder in the shape guide's form, with an optional `(uses: [NOTE-04])` field last. No status
field; `(retired)` marks a requirement, never a file.

**An index line names the questions a file answers, not its subject:**

```markdown
- [modes] -- `MODE-` -- Desktop vs. Menu Bar, including panel sizing, on-screen
  constraints, and which commands appear in which surface
```

When a reader who needs a rule would not recognize it from the line, the line is wrong.

### Glossary

The folder tree indexes one dimension, subject; questions that cut across subjects — syncing,
persistence, permissions — are named in no file, and the glossary makes them findable. It is the
catalog's **second index**, so each entry's paragraph ends by linking the requirements governing
the term; one without them is a definition, not an index.

Entries: domain entities and concepts, status names, project jargon, every cross-cutting behavior
term; not scope definitions or general software-engineering terms. The glossary gains each
cross-cutting term in the package that introduces it, including the package that creates the
catalog. Every occurrence of a term in spec prose links its entry — the link is
what marks a defined term, so terms stay in sentence case; `link-terms` writes the links.

## Requirements

A requirement is one `###` item: a statement, then any rules and tables, in the shape guide's form.
Judgment the shape does not settle:

- **One item per claim, not per row.** Rules and tables are how a product manager conveys an
  enumeration (states, fields, statuses) and its constraints. ❌ three requirements
  for three reminder states · ✅ one item whose table lists the states, with a rule for each
  state-specific constraint. Most requirements are one statement.
- **Every behavioral claim has an ID.** Intro, index and glossary prose orients. A root index
  reading *"The location list syncs across the user's devices"* has smuggled a requirement into
  prose nothing can cite, modify or test against. Give it an ID.
- **Cite dependencies inline, where they apply.** Resolve targets before linking: the
  package's draft, else the nearest base's up the chain, else the canonical file. Headings and tool output are not
  citations.
- **Known differences** record a confirmed implementation gap under the affected requirement:
  the current behavior, the gap, a tracking issue if any; an observation, never an
  exception, and the catalog's only implementation note. Suspected differences stay Discussion
  items until the supervisor resolves them.
- No other status anywhere: `(retired)` is the one marker.

## IDs

ID and anchor form are the shape guide's. Prefixes are project-defined, unique across the catalog
and registered on the file's index line; check the indexes before introducing one.

### Stability

- IDs never change when files move, rename or reorganize.
- IDs are **append-only from the moment they are drafted**, not from promotion: a work spec may
  already cite a `(pending)` ID. A retired ID is burned — never reused, never renumbered.
- A retired requirement keeps its heading and ID in place, its body replaced by a statement naming
  what superseded it. ❌ deleting the heading breaks every citation; ❌ leaving the old text under
  `(retired)` leaves a contradicted rule readable as if it held.

### Modify vs. retire

Work specs cite these IDs, so the difference matters:

- **Modify — keep the ID.** The same rule, clarified. Anything citing the ID was citing this promise
  and still is.
- **Retire and add — new ID.** The contract changed so that something previously conforming no
  longer conforms. Citations of the old ID meant a different promise and are re-pointed
  deliberately, never left to inherit new meaning.

The same test applies to a rule or table row inside an item. Before either, run the tool's
`references` and decide per citation whether it still holds (authoring's reference sweep).

## Writing style

Write as a **product manager with no knowledge of the codebase**. Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

### Required

- User-visible behavior, domain invariants and system contracts in `must` / `should` / `will`
  voice; readable by non-engineers and verifiable by users, QA or other systems without reading code.
- Product guarantees, not screen arrangement or mechanics. ✅ *"Canceling an edit preserves the
  saved note and returns users to their previous context."* · ❌ *"The editor opens as a sheet
  from Profile."* Meaningful navigation and presentation guarantees still belong here.
- Bugs earn requirements only for missing contracts or essential boundaries, never a rule per failure.
  ✅ *"Each confirmed reminder produces one notification."* · ❌ *"Reopening the screen must not
  trigger that notification again."*

### Forbidden

Plans (`implement`, `add`, `refactor`); data structures, algorithms and execution strategies ("use
caching", "debounce"); storage mechanisms ("persist as JSON"); concurrency design ("off the main
thread"); code identifiers, file paths, method and type names; frameworks and tooling. Important technical details belong in the work spec. ❌ *"The
`AssetCatalog` should DFS templates and throw `CircularReferenceError`."* · ✅ *"The system must
detect and report circular references in templated documents."*

### Nothing that decays

Requirements must make sense years later without knowing the original change.
❌ *"Must behave identically to the app as it existed before modes were introduced"* — a temporal
reference; state the behavior. ❌ *"(The former relaunch caption is dropped while the design is
reconsidered.)"* — workflow state; it belongs in the package's Discussion. The known-difference
note is the only exception.

## Cross-references

- [`spec-file-shape.md`](../Core/spec-file-shape.md) — file shape and the spec tool
- [`product-specs-artifacts.md`](product-specs-artifacts.md) — package, change items, change requests
- [`product-specs-authoring.md`](product-specs-authoring.md) · [`product-specs-promotion.md`](product-specs-promotion.md)

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-catalog-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
