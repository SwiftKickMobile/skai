Managed-By: skai
Managed-Id: guide.requirements-catalog
Managed-Source: Guides/Requirements/requirements-catalog.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-27

# Requirements Catalog

## Purpose

The **requirements catalog** is a project's living library of behavioral and contractual
requirements — what the system must do, observed from the outside. This guide defines what the
catalog contains, how it is organized, and how a single requirement is written.

Its primary audience is the **agent**. When implementing, debugging, or testing, an agent consults
the catalog to learn what behavior the system must exhibit. Humans read it too, but the agent is the
consumer that shapes the conventions here: predictable layout, stable IDs, and enough indexing that
a relevant requirement can be found without reading everything.

This guide owns **content rules only** — what a good catalog looks like. It has no gates and is not
a workflow.

**An existing catalog is not retroactively conformed.** A project whose requirements predate these
rules keeps working; the rules apply to what a package writes, not to what it carries forward. There is no migration pass,
and a package is never blocked by a defect it did not introduce.

The workflows that write the catalog are:

- [`requirements-authoring.md`](requirements-authoring.md) — drafts requirements into a change package
- [`requirements-promotion.md`](requirements-promotion.md) — promotes an approved package into the catalog

The catalog is **read-only** from work-spec implementation. It consumes requirements and never
mutates them.

### What belongs here vs. the work spec

- **Catalog**: behavioral / contractual requirements. What the system must do as observed from
  outside. Implementation-agnostic.
- **Work spec**: technical / transitional requirements (`MIG-01`, `TEMP-02`). Migration steps,
  refactor decisions, intermediate constructs.

The test: a behavior that survives a future rewrite belongs in the catalog. A constraint that exists
only for the duration of a specific change belongs in the work spec.

## Scopes

Catalog content is organized by **scope**. Each requirement lives in exactly one.

- **`platform`** — system-wide invariants that hold regardless of which app or feature uses them.
  Protocol-level, infrastructure-level, format-level.
  - *"All persisted documents must round-trip losslessly through the canonical serialization format."*
- **`domains`** — business rules about *what things are*. Entities, invariants, valid state
  transitions, relationships. Noun-level.
  - *"A Note in `draft` may transition to `published` or `discarded`; it may not skip to `archived`."*
- **`features`** — user-facing capabilities reusable across multiple apps. Verb-level — things a
  user can *do*.
  - *"Users can mark notes as favorites; favorited notes appear in a dedicated list, most recent first."*
- **`apps`** — behavior specific to a single app and not shared.
  - *"In LumenNotes for iPad, the sidebar collapses automatically below a compact width."*

### Placement decision tree

For each requirement, choose exactly one scope:

1. If the rule applies regardless of any app or feature → `platform`
2. Else if it defines what an entity is or how it behaves as a domain object → `domains`
3. Else if multiple apps offer it as a user-facing capability → `features`
4. Else → `apps/<app-name>`

### Edge case: feature vs. domain

The most commonly confused line. The test: **if the rule still applies when there is no UI, it is a
domain rule**; if it only matters because a user is interacting with it, it is a feature.

Complex behaviors often need both — a domain entry defining the model and its invariants, and a
feature entry defining the user-visible behavior. When that happens, cross-reference them.

### Prohibited structures

- Do **not** organize by Xcode project, Gradle module, package, target, or framework.
- Do **not** create per-team or per-codebase folders.

Scope is by behavioral domain, never by implementation grouping.

## Repository shape

Where the catalog lives varies by project. From any given repo there are three possibilities:

- **`local`** — the catalog is, or will be, in this repo, at the root the Integration block names. A project that intends
  to keep requirements here is `local` before the folder exists; `none` is an opt-out, not a
  not-yet.
- **`shared`** — the catalog is in another repo, typically pulled in as a submodule. This repo keeps
  none of its own. Common for a pair of platform repos — an iOS app and an Android app — that
  implement one product and therefore have one set of requirements.
- **`none`** — this project keeps no catalog, and requirements workflows skip.

Every shape has exactly **one** catalog, so a requirement ID is unambiguous everywhere and IDs are
always written bare.

**The shape and the catalog root are recorded in the project's Integration doc**, under the managed
`Section: requirements` block. Read that section before reading or writing the catalog: it is what
tells you where requirements live in this project — and under `shared`, that the path is outside
this repo.

## Layout

```
requirements/
  _requirements.md              <- root index (system overview + map of scopes)
  glossary.md                   <- domain terms, and the catalog's second index
  platform/
    _platform.md                <- scope index
    <topic>.md
  domains/
    _domains.md
    <entity>.md                 <- typically one file per domain entity
  features/
    _features.md
    <feature>.md
  apps/
    _apps.md                    <- catalog of apps
    <app-name>/
      _<app-name>.md            <- per-app index
      <subject>.md
```

A file that grows too large becomes a folder: `features/widgets.md` → `features/widgets/`, with its
own `_widgets.md` index and the content split across files inside — a change package cannot express
that split; see [`requirements-authoring.md`](requirements-authoring.md).

### Topic files are subjects, not screens

A topic file covers one **subject** — a coherent area of behavior. Not one screen, not one class.
For an app with twenty screens, expect roughly six to twelve topic files: authentication, purchase,
scheduling, notifications, and so on. Screens that participate in the same subject share a file.

Typical size is two to a dozen requirements. A file with one requirement usually belongs merged into
a neighbor; a file with thirty usually wants splitting into a folder.

### Index naming: `<folder>/_<folder>.md`

Every folder carries an index, named `<folder>/_<folder>.md` — the index shares its folder's name,
prefixed with `_`.

### Root index

The root index contains a short paragraph describing the product, a brief
restatement of which scopes this repo uses, and a pointer to the glossary.

### Scope and app indexes

Each index carries a one-line reminder of what the scope is, then a **catalog** of its files:

```markdown
- [<filename>](<filename>.md) -- `<PREFIX>-` -- <what questions this file answers> (uses: NOTE-04)
- [<folder>](<folder>/_<folder>.md) -- <what questions the files inside answer>
```

A folder line carries no prefix and links to the folder's own index. Either line may take the
optional cross-reference field last.

The prefix is required on a file line and must be unique across the catalog. Check the indexes for a
collision before introducing one.

**Catalog lines name the questions a file answers, not its subject.** This is the difference between
an index that routes and one that merely lists:

```markdown
- [modes](modes.md) -- `MODE-` -- Desktop vs. Menu Bar, including panel sizing, on-screen
  constraints, and which commands appear in which surface
```

Cutting the tail at *Desktop vs. Menu Bar* would name the topic without telling an agent whether to
open the file.

When a reader who needs a rule would not recognize it from the catalog line, the line is wrong.

One further optional field, when relevant: cross-references (`(uses: NOTE-04)`). No status field —
`(retired)` marks a retired requirement, never a file.

### Glossary

`glossary.md` is an alphabetical list of domain terms, one short paragraph each — and
it is the catalog's **second index**.

The folder tree indexes on one dimension: subject. Any question that cuts across subjects — syncing,
persistence, scaling, abbreviation, permissions — is spread across files and named in none of them.
The glossary is what makes those findable, so **every entry ends by pointing at the requirements
that govern the term**:

```markdown
**Solar phase** — whether a location's local time falls in day or night. Clock faces adapt their
appearance to it (see CLOCK-FACE-04); the day/night boundary itself is defined by PLATFORM-07.
```

An entry without a pointer is a definition, not an index. Both are useful, but only the pointer
earns the term its place here.

What goes here: domain entities and concepts, recurring status names, project jargon, and every
cross-cutting behavior term. What does not: scope definitions (they live in this guide), and general
software engineering terms.

The glossary gains each cross-cutting term in the same package that introduces it — including the
package that creates the catalog, where every term is new.

## Requirement file shape

```markdown
# <Title>

<One to three sentences: what this file covers.>

## <PREFIX>-<NN>
<The requirement. One or more paragraphs.>

## <PREFIX>-<NN>
<The requirement.>
```

Each requirement is an `##` heading carrying only its ID, with the statement as prose beneath. The
heading form matters: it makes every requirement individually anchorable, and it lets a requirement
run to several paragraphs when the rule genuinely needs a statement, a test, an exception, and a
constraint. A bullet list cannot hold that without becoming unreadable.

Most requirements are one sentence. Let them be longer only when the rule is actually that complex.

No status fields, no implementation notes, no progress markers, no `🟡`. The catalog is a stable
contract; transient state lives in the change package that produced it. The one exception is a
retired requirement, which keeps its ID and carries `(retired)` — nothing else in the catalog carries
a status of any kind.

### Cross-references are mandatory

**A requirement that depends on another must cite it, inline, by ID.** Not in a footer section — at
the point in the prose where the dependency exists:

> Location details must abbreviate rather than shrink without limit. When the space available would
> render them substantially smaller than the clock they accompany, they must advance one stage
> through the abbreviation sequence of `ENTRY-06` — repeating until they fit or the sequence is
> exhausted.

This is what makes the catalog traversable from any entry point. An agent that lands on the wrong
file still reaches the right requirement, and indexing errors stop being dead ends.

### Every behavioral claim has an ID

Prose in an index or a file header is orientation, not specification. If a sentence states something
the system must do, it is a requirement and needs an ID — otherwise nothing can cite it, no change
can modify it, and no test can be traced to it.

A root index reading *"The location list syncs across the user's devices"* has smuggled a real
requirement into a paragraph nobody can reference. Give it an ID and a home.

## ID conventions

### Format

`<PREFIX>-<NN>` — uppercase prefix of letters and hyphens only, then a hyphen and a zero-padded
two-digit number. `NOTE-04`,
`FAVORITES-02`, `CLOCK-FACE-11`. Past 99, widen to three digits for new IDs.

**Zero-pad new IDs; where a file's existing IDs are unpadded, match the file.** `MODE-07` beneath
`MODE-6` reads as an error, and in-file consistency is what a reader sees.

### Prefix registry

Prefixes are project-defined, but they must be **unique across the catalog** and recorded. A catalog
with a handful of files can keep them straight by inspection; one with twenty cannot, and the
failure mode is two files independently claiming `LEAD-` and neither noticing.

The prefix is recorded on the file's line in its scope index — see *Scope and app indexes*.

### Stability

- IDs never change when files are moved, renamed, or reorganized.
- IDs are **append-only from the moment they are drafted**, not from promotion: a work spec may
  already cite a `(pending)` ID, and renumbering a draft breaks citations no check can see. A retired
  ID is burned — never reused, never renumbered.
- Retiring a requirement leaves the ID in place, marked `(retired)`. It is not deleted: something
  elsewhere may still cite it, and a reader who follows that citation needs to land on an
  explanation rather than a gap.

### Modify vs. retire

When a requirement's text changes, one of two things is happening, and the difference matters
because work specs cite these IDs:

- **Modify — keep the ID.** The same rule, clarified or tightened. Anything citing the ID was citing
  this promise and still is.
- **Retire and add — new ID.** The contract changed such that something previously conforming no
  longer conforms. Anything citing the old ID was citing a different promise, so it needs to be
  re-pointed deliberately rather than silently inheriting new meaning.

A retired requirement stays in its file, in place. Its body is replaced by a short statement that
the rule no longer holds, naming the superseding ID when there is one:

```markdown
## NOTE-07 (retired)
Superseded by NOTE-19.
```

❌ Deleting the heading, or leaving the old text under a `(retired)` marker — the first breaks every
citation, the second leaves a contradicted rule readable as if it still holds.

## Writing style

Write as a **product manager with no knowledge of the codebase**.

### Required

- Focus on user-visible behavior, domain invariants, and system contracts.
- Describe what must be true, not how it is achieved.
- Every requirement is verifiable from outside — by a user, QA, or another system — without reading
  code.
- Use `must` / `should` / `will` voice, not `implement` / `add` / `refactor`.

### Forbidden

- Data structures, algorithms, or execution strategies ("use caching", "debounce", "run in a
  background task")
- Storage mechanisms ("persist as JSON", "CoreData", "SQLite")
- Concurrency and threading design ("async/await", "MainActor", "off the main thread")
- Code identifiers, file paths, method names, type names
- Frameworks and third-party tooling

If a detail is important but inherently technical, it belongs in the work spec, not here.

### Nothing that decays

A requirement is read years after it is written, by someone with no memory of the change that
produced it. Two failure modes:

- **Temporal references.** *"Must behave identically to the app as it existed before modes were
  introduced"* is unreadable once nobody remembers that state. State the behavior.
- **Workflow state.** *"(The former relaunch caption is dropped while the design is
  reconsidered.)"* is a note about an in-flight decision. That belongs in the change package's
  Discussion, not in canon.

### Self-check

Before writing a requirement:

1. Could a non-engineer read this without losing meaning?
2. Does it name any code identifier, file, module, dependency, or framework? If yes, rewrite.
3. Is it phrased as a behavior (`must` / `should` / `will`) rather than a plan (`implement` / `add`)?
4. Will it still be true and legible in two years, with no knowledge of today's change?

### Examples

- Good: *"The system must detect and report circular references in templated documents."*
- Bad: *"The `AssetCatalog` should DFS templates and throw `CircularReferenceError`."*

- Good: *"Users must be able to view all validation issues for an asset in a single report."*
- Bad: *"Accumulate errors during parsing and return an aggregated error array."*

- Good: *"The menu bar icon must survive the system reclaiming disk space from background
  applications, and the app must report any unclean exit from a previous run without surfacing it to
  the user."*
- Bad: *"The app must keep its cache storage empty so these sweeps pass it by, and on next launch
  detect and report (as telemetry, never a user-facing error) any previous run that did not exit
  cleanly."*

The third pair is the subtle one: it states a real, externally-observable requirement, but names the
mechanism (cache storage, sweeps, telemetry) rather than the guarantee.

## Cross-references

- [`requirements-authoring.md`](requirements-authoring.md) — drafting requirements into a change package
- [`requirements-promotion.md`](requirements-promotion.md) — promoting an approved package
- [`requirements-artifacts.md`](requirements-artifacts.md) — typed formats for change items and change requests
