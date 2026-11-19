# Artifact Location Refinement: Locations Set In The Project Config

Targets: the guides that say where production artifacts live and the commands that read them, plus the Configure SKAI guide (skai#144).
Standards: `artifact-location-design.md` § Amendment — 2026-11-18; `component-configuration-design.md` § Amendment — 2026-11-18.
Findings logs: `artifact-location-findings.md`, `component-configuration-findings.md`.
Tier: lightweight. No size caps (neither design spec sets one).

## Proposed Edits

**P1 `Guides/Core/artifact-hosting.md`**, second paragraph. Current:

> The supervisor says which repository the artifact goes in; never infer it. Its fixed
> root under `skai/` is named by its content guide. When the package is created, add the README link
> pointing at that final location; it resolves when promotion writes the artifact.

Proposed:

> The artifact goes in the project's production artifacts root, in the folder its content guide
> names. The root is `productionArtifactsRoot` in the host's `skai/config.json`, a path from the host
> root; when it is not set, the root is the host's `skai/` folder. When the package is created, add
> the README link pointing at that final location; it resolves when promotion writes the artifact.

**P2 `Guides/ProductSpecs/product-specs-catalog.md`** § Layout, first line of the block. Current: `skai/product-specs/                the fixed root, in the repository the README links`. Proposed: `product-specs/                     in the production artifacts root`.

**P3 `Guides/DesignSpecs/design-specs.md`** § Layout, first line of the block. Current: `skai/design-specs/   the fixed root, in the repository the README links`. Proposed: `design-specs/        in the production artifacts root`.

**P4 `Guides/UIMap/ui-map-guide.md`** § Rendering and validation.

Current, second paragraph's last two sentences and the command:

> The renderer takes the map to render and the HTML page to write — map and page paths resolved against the repo that holds the map, which may be separate from the app and SKAI repos. For the production map:
>
> `uv run <skai-root>/Bin/ui-map-render.py <map-repo-root>/skai/ui-map/ui-map.yaml --html <map-repo-root>/skai/ui-map/ui-map.html`

Proposed:

> The renderer takes the map to render and the HTML page to write. The production map is `ui-map/ui-map.yaml` in the production artifacts root ([`artifact-hosting.md`](../Core/artifact-hosting.md)):
>
> `uv run <skai-root>/Bin/ui-map-render.py <production-artifacts-root>/ui-map/ui-map.yaml --html <production-artifacts-root>/ui-map/ui-map.html`

Current, the change package paragraph and command:

> For a change package, the map is its `ui-map/` folder and the page is `proposed-ui-map.html` in it. Pass the product specs and design specs catalogs, each as `--specs <root>`, from where the README links them; the renderer adds the drafts it can reach of the change's spec packages and of the open packages they build on. Glossary terms and spec items on the Review tab and side panel get popovers from the catalogs and the drafts it finds. The production map's page has no Review tab and takes none.
>
> `uv run <skai-root>/Bin/ui-map-render.py <package>/ui-map --html <package>/ui-map/proposed-ui-map.html --specs <product specs catalog> --specs <design specs catalog>`

Proposed:

> For a change package, the map is its `ui-map/` folder and the page is `proposed-ui-map.html` in it. Glossary terms and spec items on the Review tab and side panel get popovers from the spec catalogs in the production artifacts root and from the drafts the renderer can reach of the change's spec packages and of the open packages they build on. The production map's page has no Review tab.
>
> `uv run <skai-root>/Bin/ui-map-render.py <package>/ui-map --html <package>/ui-map/proposed-ui-map.html`

**P5 `Guides/UIMap/ui-map-architecture.md`** line 15. Current: "The **production map** (`skai/ui-map/ui-map.yaml`) is …". Proposed: "The **production map** (`ui-map/ui-map.yaml` in the production artifacts root) is …".

**P6 `Guides/Design/design-authoring.md`** § Artifact maintenance, the command. Current: `python3 <skai>/Bin/design-tool.py render --authoring <package>/design-authoring.md [--specs ROOT ...]`. Proposed: `python3 <skai>/Bin/design-tool.py render --authoring <package>/design-authoring.md`.

**P7 `Guides/Core/spec-file-shape.md`** § The Spec Tool, two rows.

- `render`: command `render [--catalog DIR] [--base DIR]... --drafts DIR [--authoring FILE] [--out FILE]`; description gains, after its first clause: "without `--catalog`, the catalog of the drafts' type in the production artifacts root".
- `check-changes`: command `check-changes [--catalog DIR] [--base DIR]... --drafts DIR --authoring FILE`; description gains: "The catalog is found as for `render`."

**P8 `Guides/Core/configure-skai.md`.**

P8a, opening sentence. Current: "Launch the bundled Mac app to choose optional skills and policies for the active host project." Proposed: "Launch the bundled Mac app to choose optional skills and policies for the active host project, and where its artifacts live."

P8b, § Gates, the planned gate. Current: `⏳ GATE: Next: Choose components in the Mac app, then Save and Apply or Cancel.` Proposed: `⏳ GATE: Next: Choose components and locations in the Mac app, then Save and Apply or Cancel.` And after the blocked-condition paragraph, new:

> After a Save that changes a location, the **location gate**:
> `⏳ GATE: Next: Approve the proposed location changes, or say what to change.`

P8c, § Launch, the tab sentence. Current: "The app has **Project** and **User** tabs, with the explicit override count in the User label. Bulk actions are in the compact **⋯** menu beside the tabs. No layout flag is needed." Proposed: "The app has **Components** and **Locations** tabs. On Components, bulk actions are in the compact **⋯** menu beside the tabs. No layout flag is needed."

P8d, § Launch, the paragraph from "No project config checks all optional entries" to "Drafts persist when switching tabs." Proposed, replacing it whole:

> No project config, or one without a `components` list, checks all optional entries; a config with a list checks only its selection. The **Components** tab uses ordinary checkboxes; a category checkbox selects or clears its members and shows a dash when only some are selected. Rows show the component name and description. Categories start collapsed; the chevron beside each shows its components, and the category checkbox works either way. Components the host has never seen (new in this checkout; see *New components* in `component-selection.md`) are listed first, checked, under **New 🔥 — configure to use** until Save, which moves the checked ones into the config and records the rest as declined; Save stays available while any are listed. On the next launch they sit in their categories like any other. Required Configure SKAI cannot be changed. In the **⋯** menu, Select all and Clear optional turn every optional component on or off.
>
> The **Locations** tab sets two folders, each saved in `skai/config.json` as its path from the host root: **Production artifacts** (`productionArtifactsRoot`), where the product specs, design specs and UI Map live, and **Change packages** (`changePackagesFolder`), the `skai` folder that holds `changes/` and `promoted/`. A folder that is not set shows `skai`, the host's `skai/` folder. **Choose…** picks a folder; the clear button unsets it. Drafts persist when switching tabs.

P8e, § Reconcile after Save, new paragraph after the first:

> A saved event's `locationChanges` lists each location the Save changed, with its folder before and after. After reconciliation, propose for each: moving the old folder's contents to the new one when they are not there yet, and the edits to every reference to the old location that you already know of. Do not search for others. Then show the location gate and change nothing until it advances. Save and Apply approves component reconciliation, not these changes.

P8f, § Gates. Current: "Project/User drafts are the review artifact". Proposed: "The app's drafts are the review artifact".

**P9 `Install/component-selection.md`** § Desired components and § Local user overrides.

- Current: "**Only an absent file selects everything**, preserving the previous adapter/stack eligibility rules." Proposed: "**An absent file, or one without `components`, selects everything**, preserving the previous adapter/stack eligibility rules. The file may also hold the project's two locations, `productionArtifactsRoot` and `changePackagesFolder` ([Configure SKAI](../Guides/Core/configure-skai.md)); reconciliation does not read them."
- Current: "The app has Project and User tabs; Save commits only layers whose settings changed, preserving unrelated JSON keys." Proposed: "Save commits only layers whose settings changed, preserving unrelated JSON keys." (The app's User tab is hidden; an existing local file is still read.)

## Rounds

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|
| r1 (proposal) | — | 8 | 0 | 8 | 0 | 0 |

Proposal round, not scored. Verdict: P1–P3, P5, P6 endorsed; P4, P7, P8, P9 amend.

## Round 1 Matrix

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F1 Tools miss the config for a change packages folder outside the host or not named `skai` | accept (tool) | AL amendment 2; CC amendment 2 | `locations_for` also looks above the working directory; the folder must be named `skai` (picker, Python and Swift readers) | No scanning; no catalog paths in guide commands |
| F2 First catalog: default lookup exits when the catalog folder does not exist yet | accept (tool) | AL decision 4, amendment 3; `spec-file-shape.md` | `catalog_for` returns the would-be folder; the drafts diff against an empty catalog; P7 says so | Nothing created before promotion |
| F3 "Move the old folder's contents" would move config and state out of a shared default `skai/`; `skai` set explicitly reported as a change | accept | CC amendment 4 (wording corrected); `configure-skai.md` Reconcile | Move what the setting covers; same effective folder is no change (app) | Save and Apply approves components only |
| F4 Location gate has no advance, revision, failure or completion path | accept | CC amendment 4; `configure-skai.md` Gates, Advance intent, Reconcile, completion | Rewrite the Reconcile/Gates text around both gates | Chat cannot bypass the UI gate |
| F5 A standalone Save then a later apply has no record of the old locations | supervisor decision | CC amendment 4; `configure-skai.md` standalone and apply paragraphs | Pending ruling | Explicit apply still approves components |
| F6 Hidden User tab: override badges unexplained; Save availability with new components misstated | accept | CC amendment 1; `configure-skai.md` Launch | Say existing overrides still apply and show as badges; Save available when drafts differ or new components await a choice | Local override behavior |
| F7 P9's "reconciliation does not read them" is false (locations are validated) | accept | `component-selection.md` | "they do not decide the selection" | Invalid config blocks |
| F8 New components section keys on file presence | accept | CC amendment 3; `component-selection.md` § New components | "no config, or one without `components`" | Explicit-list behavior |

Tool fixes for F1, F2 and F3 applied and tested (configuration, spec-tool, design-tool, ui-map-render suites pass).

| r2 | 11.25 | 4 | 0 | 4 | 0 | 3 |

F2 location proposal deferred behind a failed reconciliation, "keep the proposal" before one exists — divergent · off-normal · speculative = 1.875 · F3 "made or declined" completes with setting and files disagreeing — divergent · off-normal · verified = 3.75 · F4 apply without event: no comparison of before and current folders — divergent · off-normal · verified = 3.75 · F5 a same-named folder already at the destination — divergent · off-normal · speculative = 1.875 · F1 tools silently fall back when not run from the host — log only (agents run tools from the host root; an outside change packages folder is off-normal; competing host configs are unsupported), noise · F6 a Save error after the write leaves config saved (existing app behavior, not this change) — log only, noise · appendix `check-changes` wording broader than the tool — outside the change, log only, noise

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
|---|---|---|---|---|
| F2 | accept | `configure-skai.md` Location changes | Propose after reconciliation whether or not it succeeded; drop "keep the proposal" | Save and Apply approves components only |
| F3 | accept | Gates completion; Reconcile report | Complete once the location gate is resolved; a declined change is reported as a mismatch | No automatic revert of the saved setting |
| F4 | accept | Location changes, first paragraph | Read an unset location as `skai`; only differing folders are changes | Source control is the only before source; block otherwise |
| F5 | accept (small) | Location changes, first bullet | Name an existing same-named destination folder instead of moving onto it | No new gate |

Applied. Self-check: completion wording in Gates and Reconcile now agree; no stale "keep the proposal".

| r3 | 10.625 | 4 | 0 | 4 | 0 | 2 |

F2 the location gate had no decline outcome — divergent · off-normal · speculative = 1.875 · F3 a blocked reconciliation and the location proposal had no order — divergent · off-normal · speculative = 1.875 · F4 a covered folder missing at the old location — divergent · off-normal · speculative = 1.875 · F6 the spec tool table still offered `--catalog` — divergent · normal · verified = 5 · F1 run-from-host-root, re-raise of logged r2 F1, noise · F5 relative links from moved files — log only (a setting's folders move together, so links among them hold; the proposal names its edits for the supervisor), noise

Three of four live rows (F2, F3, F4) are about my round 2 repairs to the location step: consolidation trigger. Rewrote *Location changes* whole, shorter: proposal before reconciliation (one order, no interleaving with installer gates); approve, decline or revise at one gate; moves that cannot be made as stated are named, not special-cased. F6: `--catalog` removed from the table rows.

| r4 | 13.125 | 4 | 0 | 4 | 0 | 0 |

F1 run-from-host-root not said at the commands, third raise: the settled disposition (tools run from the host root) is not carried out in the text — divergent · normal · verified = 5 · F2 an apply without the event reaches the adapters before *Location changes* — divergent · off-normal · speculative = 1.875 · F3 the approval does not name the re-renders it then makes — divergent · off-normal · verified = 3.75 · F4 the hosting example does not say it shows the default root — divergent · normal · speculative = 2.5

All four accepted and applied as one-phrase fixes: "from the host project root" at the spec tool, UI Map renderer and design render commands; the apply path handles *Location changes* before reconciling; the proposal names the pages to re-render; the hosting example is marked as the default root.

Supervisor (2026-11-18): the Configure guide does not describe the app's screen. Cut the tab, checkbox, badge, menu and button-availability text; kept launch, events, gates, the config's contents, reconciliation and location changes. `configure-skai.md` 10,939 → 10,607 bytes.

Caps were not proposed after round 1, as the refinement guide requires; proposed after round 4 and approved by the supervisor (2026-11-18), recorded in each guide's design spec. Round 5 carries them.

| Guide | Before | Compressed | Delta | Old cap | Cap |
|---|---|---|---|---|---|
| configure-skai.md | 10,939 | 10,607 | −332 | none | 10,600 |
| ui-map-guide.md | 17,359 | 17,889 | +530 | 17,370 | 17,850 |
| component-selection.md | 11,647 | 11,863 | +216 | none | 11,850 |
| artifact-hosting.md | 2,341 | 2,493 | +152 | none | 2,480 |
| spec-file-shape.md | 8,700 | 8,844 | +144 | 8,350 | 8,830 |
| ui-map-architecture.md | 36,980 | 37,058 | +78 | 36,980 | 37,050 |
| design-authoring.md | 18,848 | 18,857 | +9 | 18,900 | 18,900 |
| product-specs-catalog.md | 10,477 | 10,459 | −18 | 10,500 | 10,500 |
| design-specs.md | 15,117 | 15,099 | −18 | 15,000 | 15,100 |

| r5 | 8.75 | 2 | 0 | 2 | 0 | 0 |

F1 "config.local.json still overrides it" reads as overriding locations too — divergent · off-normal · verified = 3.75 · F2 the change-check row promises a separate entry for every change (logged in r2 as outside the change; the row is now in it) — divergent · normal · verified = 5

Applied: F1 "overrides its component selection"; F2 the row says a change may ride on another entry or its Touches, keeping every check it lists (the reviewer's wording dropped "no entry names an unchanged or absent target"); the reviewer's seven trims, each checked to drop no meaning ("frozen" in `ui-map-architecture.md` restated "this guide does not change it"). Every guide is within its cap except `spec-file-shape.md`, 8,866 against 8,830 (14 over before the pass): left for round 6's reviewer to tighten.

| r6 | 11.25 | 3 | 0 | 3 | 0 | 0 |

F1 the location step's "before reconciling, propose" is unconditional — divergent · normal · speculative = 2.5 · F2 the change-check row still generalized riding beyond the tool's type-specific rules; the tool docstring said a product title change is not required, though the code requires Touches coverage — divergent · normal · verified = 5 · F3 the design tool docstring still said to pass spec roots — divergent · off-normal · verified = 3.75

Applied: F1 "When a location changed, before reconciling…" plus the reviewer's trim; F2 the reviewer's row wording (coverage rules point to the tool docstring) and the docstring's title rule corrected (verified at `spec-tool.py` check_changes: a product title rides in Touches); F3 docstring sentence corrected. Every guide within its cap (`spec-file-shape.md` 8,828 / 8,830; `configure-skai.md` 10,594 / 10,600).

| r7 | 11.25 | 3 | 0 | 3 | 0 | 1 |

F2 the production map command linked the creation-only hosting guide — divergent · normal · speculative = 2.5 · F3 the UI Map guide described draft selection beyond the best-effort ruling — divergent · normal · verified = 5 · F4 a blank location value reads as the default, the guides said only "unset" — divergent · off-normal · verified = 3.75 · F1 explicit apply skips Launch's discovery paragraph — the branch predates this change, log only, noise

Applied: F2 link removed; F3 the reviewer's sentence; F4 "blank or absent" in the hosting and Configure guides. All within caps.

| r8 | 2.875 | 2 | 0 | 1 | 1 | 0 |

F1 explicit apply skips Launch's checkout resolution (logged r7 as predating the change; raised again, and the fix is one phrase in the sentence this pass edits) — divergent · off-normal · speculative = 1.875 · F2 "checkboxes represent desired components" describes the screen — cosmetic · normal · speculative = 1 · open question (a declined move leaves tools reading an empty catalog) not a finding: the supervisor's decline choice, settled

Applied both. `configure-skai.md` within its cap.

| r9 | 0 | 0 | 0 | 0 | 0 | 2 |

F1 a declined change-packages move leaves tools falling back to the package's own `skai` folder — re-raise of the settled decline disposition (the supervisor's choice at the gate; the guide reports the mismatch), noise · F2 "absent" read as a missing committed config — rejected: with no committed config the before locations were the defaults, which is determined, not a guess; the block applies only when they cannot be determined, noise

Clean round: converged by the stop rule's (a). Pass closed.

## Closure

All accepted findings closed in rounds 1–8 and held through round 9's clean read: r1 F1–F8 (F1–F3 by tool fixes), r2 F2–F5, r3 F2–F4 and F6 (location step rewritten whole), r4 F1–F4, r5 F1–F2, r6 F1–F3, r7 F2–F4, r8 F1–F2. Logged: r2 F1 (re-raised r3, r4; then accepted in r4 as a one-phrase fix), r2 F6, r2 appendix (accepted in r5 once the row was in the change), r3 F5, r7 F1 (accepted in r8). Rejected: r9 F1–F2.

Net size, before → after (caps approved 2026-11-18 after round 4): `configure-skai.md` 10,939 → 10,585 (10,600); `ui-map-guide.md` 17,359 → 17,692 (17,850); `component-selection.md` 11,647 → 11,845 (11,850); `artifact-hosting.md` 2,341 → 2,469 (2,480); `spec-file-shape.md` 8,700 → 8,828 (8,830); `ui-map-architecture.md` 36,980 → 37,047 (37,050); `design-authoring.md` 18,848 → 18,857 (18,900); `product-specs-catalog.md` 10,477 → 10,459 (10,500); `design-specs.md` 15,117 → 15,099 (15,100).

Process misses recorded: caps were not proposed after round 1 (proposed after round 4); the 2026-11-12 UI Map pass took `ui-map-guide.md` over its 17,370 cap without a proposal.

