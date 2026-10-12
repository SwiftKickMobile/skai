# Project guide addenda — design

## Requested capability

Each SKAI guide supports a project-owned, optional freeform Markdown addendum. It can add rules or explicitly override that guide's procedure/conventions. SKAI skills are building blocks composed by a project; this does not introduce a SKAI-wide workflow.

The base guide owns its dependencies, including reading Integration whenever operational settings are needed. Addendum authors do not have to restate or reference those dependencies. Integration remains the global settings document; no global configuration format migration is requested.

## Loading contract

- Read the complete base guide, then its addendum if present, before applying the guide or executing a procedure. A short entry cue routes to a footer containing the protocol and exact lookup path.
- Use `skai/addenda/<guide-name>-addendum.md` under the active project root as the initial entry point. It may reference shared addenda in another repository; a shared-context repository can itself be the active project. Use the published guide filename stem initially; preserve this lookup name across future renames or explicitly migrate it. Names must be unambiguous.
- Read required shared addenda before applying project-local additions/overrides; resolve relative links from their containing file. Report each successfully loaded file. Missing/unreadable required references block. This freeform composition needs no addendum inventory.
- An absent project entry is normal. Unknown root, failed existence lookup or unreadable existing file blocks instead of implying absence.
- Report an emoji-prefixed receipt with the resolved path and loaded/absent status. It introduces no approval gate and precedes any required trailing GATE line. Loading and reporting remain required even when the addendum replaces the guide's procedure.
- Apply addendum additions and overrides instead of conflicting guide defaults. Current task instructions and project-wide policies remain authoritative; unexpected conflicts there use existing escalation. A supported guide override does not require repeated permission merely because it differs from SKAI's guide text.
- Load only guides needed for the selected building block; every such guide checks its own addendum, including references and handoffs after rollout. The addendum applies to its own guide, not arbitrary other guides.
- No required headings, frontmatter, schema or managed header. Project owners control the content; SKAI installers must not create, overwrite, conform or delete addenda. No mandatory empty folders/files.

## Prototype and rollout

Prototype Requirements Promotion with its thin wrapper and the installed instruction-block exception. Other guides' addendum support is not yet assumed during prototype review. Review the loading/precedence/receipt contract in this concrete guide; unrelated requirements semantics and earlier change-package work are outside this review.

After refinement, promote the exact settled entry/footer text into a maintainer house-style reference and apply it to all 35 registered guide assets: 33 files under Guides plus the two internal guide-runbooks. Non-guide installer runbooks and maintainer-only references are not separate skill building blocks; their ownership/update instructions must preserve addenda. No new runtime loader or guide dependency is requested.

## Constraints and acceptance

- Current guide behavior remains the default when no addendum exists; no new review gate or progress field.
- Only the thin wrapper routes to the canonical guide; it must not restate procedure restrictions that contradict overrides or current recovery.
- Keep the existing 11,000-word cap across the four requirements guides. Initial total is 10,608; additions during rollout may need compensating trims.
- Verify no-addendum, added-rule, explicit-override, unreadable/unknown-root and root-project/task conflict paths. The receipt must be truthful and before work, while existing gate placement is preserved.
- This is instruction-based loading and acknowledgement, not a technical guarantee that an agent obeys the text. Do not add hooks, mandatory user schemas or proof fields to address that limitation.
- Preserve current asset IDs, addendum content and released changelog history. No commit, push, release, host migration or issue operation is requested.

## Shared-context follow-up — 2026-10-09

Supervisor chose a conventional project addendum that points to shared content and may add local rules. The README provides optional copyable shared-first/local-second prose. This supersedes the prototype's categorical shared-repository exclusion; its review remains historical, not a new review of this clarification.
