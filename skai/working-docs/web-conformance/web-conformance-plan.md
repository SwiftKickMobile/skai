# UI Map Plan — web-conformance

## Goal

Bring the Debug SwiftUI fixture app into conformance with the approved `Debug/SwiftUI/ui-map.yaml`. The map is the source of truth; code follows it.

## Inputs

- Conformance target (approved map): `Submodules/skai/Debug/SwiftUI/ui-map.yaml`
- Code under audit: `Submodules/skai/Debug/SwiftUI/Debug/` (and the sibling `UI` framework target in the same Xcode project)
- Xcode project: `Submodules/skai/Debug/SwiftUI/Debug.xcodeproj` (targets: `Debug` app, `UI` framework; both link `SKAISwiftUI`; `Debug` links + embeds + depends on `UI`)
- Platform reference: `Submodules/skai/Guides/Dev/ui-map-swiftui.md`
- YAML format reference: `Submodules/skai/Guides/Dev/ui-map-guide.md`
- Placeholder package source: `Submodules/skai/Dev/Swift/Sources/SKAISwiftUI/`
- No project `README.md` exists for this fixture; only the standard route kinds and modal styles (`sheet`, `full_screen`, `popover`) are used, so the SwiftUI reference alone governs.

## Discussion

Audit conformance pass over all 15 map scenes against the SwiftUI reference's conformance dimensions (`folder-org`, `file-layout`, `naming`, `route-kind`, `platform-pattern`) and against the map's structural facts (route kinds, modal styles, reuse/`primary_parent`).

Baseline: `xcodebuild build -scheme Debug` succeeded before the audit (`/tmp/uimap-baseline-build.txt`) — the fixture compiles as-is.

Conformant scenes are not enumerated (findings are deviations only). 14 of 15 scenes conform on every dimension:
`app` (child, default `.library` = first listed), `login` (nav), `welcome` (leaf, todo), `library` (tab + sheet + full_screen), `notes_tab` (nav), `folders_tab` (leaf), `trash_tab` (leaf), `note` (composite + popover + full_screen + sheet), `editor`, `tag_picker` (popover), `attachment_viewer` (full_screen), `share_sheet` (sheet), `profile` (sheet modal, nav→web), `search` (reused, nests under `primary_parent: library`, full_screen from both `library` and `note`).

One deviation found.

### Code conformance

- [x] A. `web` common scene lives in the app target instead of the shared UI module
  - **Concern** File-layout / folder-org deviates from the SwiftUI reference's rule for `common:` scenes.
  - **Discrepancy** The map declares `web` under top-level `common:` (with `implements: [privacy_policy, terms_of_service]`). The SwiftUI reference states common scenes "live in the shared UI module under its own top-level `Scenes/` folder — one folder per scene." `WebView.swift` currently lives in the `Debug` app target at `Debug/Scenes/Web/WebView.swift`. The project has a SwiftUI-capable shared module — the `UI` framework target — which already links `SKAISwiftUI` and is linked/embedded/depended-on by `Debug`, but it holds no scenes (`UI/` contains only an empty `UI.swift` and a `.docc`). The `web` scene is referenced from `profile.nav` (`ProfileView` in the `Debug` target instantiates `WebView()`).
  - **Resolution** Fix code — move the `Web` scene folder to the `UI` module at `UI/Scenes/Web/WebView.swift`; make `WebView` `public` (with a `public init()`) so the `Debug` target can construct it across the module boundary; add `import UI` to the one call site (`ProfileView.swift`). The `implements` annotation requires no code: per the SwiftUI reference's new-scene no-inputs rule, a scaffolded placeholder models no variant enum or inputs.
  - **Why** Guide convention: domain-agnostic `common:` scenes belong in the shared UI module, not the app target. The project supplies exactly that module (`UI`), already wired to host such scenes.
  - **Decision** Fix code as proposed — move `Web/` to `UI/Scenes/Web/`, make `WebView` public, add `import UI` to `ProfileView.swift`.

### Defers

(none)

## Change list

- [x] 1. Conformance / folder-org: `web` → shared UI module
  - **Description** Relocate the `Web` common scene from the app target into the shared `UI` framework module and wire the cross-module call site:
    - Move `Debug/Scenes/Web/WebView.swift` → `UI/Scenes/Web/WebView.swift` (untracked file → plain `mv`; synchronized folders update target membership automatically — leaves `Debug`, joins `UI`).
    - In the moved `WebView.swift`, make the type `public struct WebView` and add an explicit `public init() {}` so it is constructible from the `Debug` target.
    - Add `import UI` to `Debug/Scenes/App/Library/Profile/ProfileView.swift` (its `WebView()` call now crosses the module boundary).
  - **Justification** Guide convention: `ui-map-swiftui.md` — `common:` scenes live in the shared UI module's own top-level `Scenes/` folder; the `UI` target already links `SKAISwiftUI` and is linked/embedded/depended-on by `Debug`.
  - **Touches** scene `web`; route `profile.nav → web`; files `Debug/Scenes/Web/WebView.swift` (moved), `UI/Scenes/Web/WebView.swift` (new home, made public), `Debug/Scenes/App/Library/Profile/ProfileView.swift` (add `import UI`).
  - [evidence: xcodebuild build -scheme Debug -project Debug/SwiftUI/Debug.xcodeproj -destination 'platform=iOS Simulator,name=iPhone 17 Pro,OS=26.4'; exit 0; output: working-docs/main/web-conformance/implementation/evidence/build-after-move.txt]

## Deferrals

(none)

## Out of scope

- The map itself: it validates (schema + semantic, render exit 0) and is the approved conformance target — this pass makes no map changes.
- Style-only observation, not a conformance finding: `ProfileView` reads `$viewModel.navRoute` without a `@Bindable var viewModel = viewModel` line (other routing views in the fixture use `@Bindable`). It compiles and routes correctly (`@State`'s projected value yields the binding), so it is not a guide-mandated pattern deviation. Noted, not actioned.
