# Artifact Location — Design Spec

The standard for refining how skai guides locate, create and record the project's canonical
artifacts: the requirements catalog, the design specs, the UI Map, and the design file. Decided by
the supervisor on 2026-10-13 in discussion; this document is that discussion's record.

## The Problem

Four artifacts, found three ways: requirements through a managed block in the Integration doc,
the UI Map through "the project README or established map location", the design file through a
README row described down to its row names. The design-specs block copied the requirements
pattern and widened the split. Guides restated location rules at every entry point, taught the
agent to scan `skai/changes/` for packages it was not told about, and inferred the host repository
from the presence of a submodule.

## Decisions

1. **skai artifacts live under `skai/`** in whichever repository the supervisor names for each:
   the app repository, or a context repository pulled in as a submodule. Artifacts need not share
   a repository (supervisor, 2026-10-13, replacing the earlier "one repository per product"). Fixed
   roots: `skai/requirements/`, `skai/design-specs/`, `skai/ui-map/`; change packages at
   `skai/changes/<change-id>/<type>/`, promoted at `skai/promoted/<change-id>/<type>/`, in the
   artifact's repository.
2. **The README links the project's resources.** The agent instruction block opens with: read
   `README.md` first; it links the project's resources, and a linked resource is where the README
   says it is; if a resource a task needs is not linked there, stop at a blocked gate and do not
   look for it; an unlinked resource is unavailable even when something else names it (sharpened
   2026-10-13 after dry runs questioned a linked path against the fixed roots, searched before
   blocking, and used a design-file URL found inside a change package). The fixed roots of decision 1 govern where a new
   artifact goes; an existing artifact is where its link points. No guide describes how the README
   is structured (no "resources table", no row names).
3. **If information is missing, the agent blocks.** It is not the agent's job to distrust
   instructions or audit whether they are correct. No guide teaches discovery, fallback or
   verification of what the supervisor supplied: no scanning for packages, no "or established
   location", no inferring the host. The package is the one named or already in context.
4. **Authoring establishes the host.** The one place location is decided is the first package for
   an artifact, because the artifact does not exist yet (not every "baseline": the authoring
   guides use that word for new scope inside an existing artifact; corrected 2026-10-13). The
   authoring guides follow one small shared guide to: learn
   from the supervisor which repository the artifact goes in (never inferred), and add the README
   link when the package is created, pointing at the final location. The link resolves when
   promotion writes the artifact, which creates the root; nothing creates it earlier (supervisor,
   2026-10-13). No temporary link to the change package, so nothing to clean up later.
5. **No other guide mentions location.** Promotion, implementation, work-spec and retro guides
   rely on the README having been read. Content guides keep their Layout sections (the fixed path
   and file names) and nothing else about location.
6. **The Integration doc records no artifact locations.** The `requirements` and `design-specs`
   managed blocks are gone (removed 2026-10-13); the installer proposes removing a legacy block as
   cleanup after the README link exists.

## Holes Already Found

- Creating an artifact must not trip the "not linked, block" rule: it is the one case where its
  absence is expected. The shared guide says so in one sentence.
- The design file cannot be bootstrapped by authoring; decision 4 applies to the three file
  artifacts. A project with no linked design file is blocked, correctly.
- Every baseline's repository is the supervisor's call, never inferred.
- Moving `requirements/` and `design-specs/` under `skai/` keeps their links to each other intact
  (same depth) but changes the depth of links from change packages and from the app README by
  one; migration must repair those.

## Scope

**Target:** the guides that locate or create artifacts — `Guides/Requirements/*.md`,
`Guides/DesignSpecs/*.md`, `Guides/UIMap/ui-map-architecture.md` and `ui-map-implementation.md`,
`Guides/Design/design-authoring.md`, `design-promotion.md` and `figma-designer-guide.md`,
`Guides/Spec/work-spec-creation.md` and `work-spec-implementation.md`, `Guides/Process/dev-retro.md`,
the shared instruction block `Templates/agents/instructions-block.md`, and the new shared hosting
guide under `Guides/Core/`.

**Not the target:** the Integration doc's other sections and stack templates; the UI Map renderer
and its paths; the content rules of any artifact (format, IDs, writing style).

## What Simple Looks Like

- One shared guide for hosting, read only when the artifact does not exist yet. No size cap; the supervisor judges the draft (2026-10-13).
- Each authoring guide: one sentence pointing at it. Every other guide: nothing about location.
- The instruction block line is the only runtime statement of where resources are found.
- Net guide text shrinks; a refinement that adds location text anywhere else has failed.

## Settled Dispositions

- Integration blocks for artifact location: rejected, removed.
- Per-guide location sentences in non-authoring guides: rejected, removed.
- Scanning `skai/changes/` and "multiple candidates" blocked gates: rejected.
- Temporary README links to change packages: rejected.
- Enumerating artifacts or README structure in the instruction line: rejected ("myopic").
