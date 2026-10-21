# UI Map Plan — placeholder-scaffold

## Goal

Scaffold the full LumenNotes placeholder app — skeleton + navigation, no feature content — from the approved `Debug/SwiftUI/ui-map.yaml`. Every map scene becomes a `SKAISwiftUI` placeholder; the result is a fully clickable skeleton. This is the SwiftUI end-to-end test of the UI Map implementation method (build sequence step 4).

## Inputs

- Approved map: `Submodules/skai/Debug/SwiftUI/ui-map.yaml` — the canonical LumenNotes demo; already in its target state, validated (schema + semantic, render exit 0 per the prior `web-conformance` plan).
- Target codebase (currently blank): `Submodules/skai/Debug/SwiftUI/Debug/` (app target) + sibling `UI` framework. `DebugApp.swift` renders `Text("Hello, world!")`; `UI/` holds only an empty `UI.swift`; no `Scenes/` exist yet.
- Xcode project: `Submodules/skai/Debug/SwiftUI/Debug.xcodeproj` — targets `Debug` (app) and `UI` (framework); both link `SKAISwiftUI`; `Debug` links/embeds/depends on `UI`. Both folders are Xcode file-system-synchronized groups, so files dropped on disk auto-join their target (no `.pbxproj` editing).
- Platform references: `Submodules/skai/Guides/Dev/ui-map-swiftui.md`, `Submodules/skai/Guides/Dev/ui-map-swiftui-placeholders.md`; YAML format `Submodules/skai/Guides/Dev/ui-map-guide.md`.
- Placeholder package source: `Submodules/skai/Dev/Swift/Sources/SKAISwiftUI/` (`SKAISwiftUI`, iOS 18+).
- No project `README.md` for the fixture; only standard route kinds and modal styles (`sheet`, `full_screen`, `popover`) are used, so the SwiftUI reference alone governs.
- Prior precedent: `skai/working-docs/web-conformance/` audited an earlier hand-built version of this fixture (since reset to blank).

## Discussion

### Scope

The change is purely additive: 15 scenes, all new, scaffolded from the map. No map edits — the map is the input and already in its target state, so Phase 2 produces no `ui-map.yaml` diff and no new render; the existing demo render stands as the target.

Scene inventory and route kind, top-down (this is the execution order Phase 2 will follow):

- `app` — child → [`library`, `login`] (root scene; default child = `library`, first listed)
- `login` — nav → [`welcome`] (defined inline under `app.child`)
- `welcome` — leaf, `todo: true` (defined inline under `login.nav`)
- `library` — tab → [`notes`, `folders`, `trash`] + modal → [`profile` sheet, `search` full_screen]
- `notes` — nav → [`note`]
- `folders` — leaf; `trash` — leaf
- `note` — composite → [`editor`] + modal → [`tag_picker` popover, `attachment_viewer` full_screen, `share_sheet` sheet, `search` full_screen]
- `tag_picker` — leaf; `attachment_viewer` — leaf; `share_sheet` — leaf
- `profile` — sheet modal style; nav → [`web`]
- `search` — leaf; full_screen; `primary_parent: library` (render-only); reused from `library.modal` and `note.modal`
- `editor` — leaf (composite child of `note`)
- `web` — leaf; `common:`; `implements: [privacy_policy, terms_of_service]` (no inputs modeled — new-scene rule)

### The welcome scene (todo)

`welcome` is flagged `todo: true` with note "Onboarding flow not yet built." In an audit of an existing app, a `todo: true` scene with no code is a Defer (the route is map-defined, the feature unbuilt). But this is a from-scratch placeholder scaffold whose entire deliverable is skeleton + navigation — the placeholder *is* the kind of stub the eventual onboarding work replaces.

- [x] Proposal — scaffold `welcome` as a placeholder leaf (not defer), so `login.nav → welcome` resolves and the skeleton is fully clickable. The map's `todo: true`/`note` remain accurate map annotations about the real feature. Precedent: the prior fixture scaffolded `welcome` as a leaf and the `web-conformance` audit counted it conformant. Alternative (rejected): defer it — leaves `login.nav` with no destination and a map route unrepresented in code, breaking the click-through.
  - **Decision** Scaffold `welcome` as a placeholder leaf.

### App root hosting

`DebugApp.swift` is project-owned host scaffolding currently showing `Text("Hello, world!")`. The root `App` scene (`AppView`) is a domain scene scaffolded into the `Debug` app target, so `DebugApp` can construct it directly (same target, no import).

- [x] Proposal — replace the `DebugApp` body with `AppView()` as part of standing up the skeleton.
  - **Decision** Replace the `DebugApp` body with `AppView()`.

### Folder organization & target placement

The SwiftUI reference mandates the folder tree mirror the `domains:` tree (not routing parentage), with `common:` scenes in the shared UI module. No README override exists, so the reference defaults govern. This differs from the prior fixture, which nested by routing parentage (`Debug/Scenes/App/Library/Profile/…`).

Proposed layout:

```
Debug/Scenes/
  App/            AppView, AppViewModel
    Login/        LoginView, LoginViewModel
      Welcome/    WelcomeView, WelcomeViewModel
  Library/        LibraryView, LibraryViewModel
    Notes/  Folders/  Trash/
  Note/           NoteView, NoteViewModel
    TagPicker/  AttachmentViewer/  ShareSheet/
  Other/
    Profile/  Search/  Editor/
UI/Scenes/
  Web/            WebView, WebViewModel  (public — crosses module boundary)
```

- [x] Proposal — domain scenes in the `Debug` app target under `Debug/Scenes/`, organized to mirror the `domains:` tree; the `common:` scene `web` in the shared `UI` module at `UI/Scenes/Web/`, made `public`. Cross-domain refs (`library`, `note`, `profile`, `search`, `editor`, `web`) create no folders — placed where defined, instantiated where referenced.
  - **Decision** Domain scenes in `Debug/Scenes/` mirroring the `domains:` tree; `web` in `UI/Scenes/Web/` (public).

### Verification tooling

`docs/skai/integration.md` targets the SalesPro project, not this fixture, so the build-verify command isn't covered there. The prior plan built the fixture with `xcodebuild build -scheme Debug` (exit 0).

- [x] Proposal — use this command for stage/completion build-verify: `xcodebuild build -scheme Debug -project Submodules/skai/Debug/SwiftUI/Debug.xcodeproj -destination 'platform=iOS Simulator,name=iPhone 17 Pro,OS=26.4'`.
  - **Decision** Use `xcodebuild build -scheme Debug -project Submodules/skai/Debug/SwiftUI/Debug.xcodeproj -destination 'platform=iOS Simulator,name=iPhone 17 Pro,OS=26.4'`.

## Change list

All entries are `Add scene` with Source `Map`: the map is the source of truth and already defines every scene; these entries realize each map-defined scene in code as a `SKAISwiftUI` placeholder (skeleton + navigation). No map edits occur. (This from-scratch-scaffold-from-a-complete-map situation sits between the guide's two taxonomy arms — new-change `add scene` normally implies a map edit, audit `conformance/<dim>` has no "absent scene" dimension — represented here as `Add scene` / Source `Map`.)

Execute top-down. Cross-domain references mean intermediate states don't compile; build-verify runs once at completion, not at per-domain stage gates. Every scene gets a `View` + `ViewModel` per `ui-map-swiftui.md`'s file layout; placeholder shapes per `ui-map-swiftui-placeholders.md`. Modal-style → enum/property: `sheet`→`Sheet`/`sheetRoute`, `full_screen`→`Cover`/`coverRoute`, `popover`→`Popover`/`popoverRoute`.

### app domain

- [x] T1 Add scene: app
  - **Description** Root scene + app host. `AppViewModel` with `AppChildRoute { case library, login }` defaulting to `.library` (first child listed). `AppView` uses `PlaceholderChildHost(title: "App", routes:)` with both children as `.child` routes (`isCurrent` bound to `childRoute`); in the switch, `case .library: LibraryView()` (tabbed child → **not** wrapped), `case .login: NavigationStack { LoginView() }` (non-tab child → wrapped). Also wire the host: replace `DebugApp.swift`'s body with `AppView()` (same target, no import).
  - **Justification** Map: `domains.app` (collapsed domain, root scene), `child: [library, login]`. Host wiring per the App-root-hosting decision.
  - **Touches** scene `app`; route `app.child → library, login`; files `Debug/Scenes/App/AppView.swift`, `Debug/Scenes/App/AppViewModel.swift`, `Debug/DebugApp.swift`.

- [x] T2 Add scene: login
  - **Description** Nav scene. `LoginViewModel` with `LoginNavRoute { case welcome }`. `LoginView` uses `PlaceholderScene(title: "Login", routes: [.nav → welcome])` and a `.navigationDestination(item:)` whose `welcome` case yields `WelcomeView().environment(\.placeholderShowsDismiss, false).placeholderCrumb("Login")`. Owns no `NavigationStack` (its `app.child` slot supplies one).
  - **Justification** Map: `app.child → login`, `login.nav: [welcome]`.
  - **Touches** scene `login`; route `login.nav → welcome`; files `Debug/Scenes/App/Login/LoginView.swift`, `Debug/Scenes/App/Login/LoginViewModel.swift`.

- [x] T3 Add scene: welcome
  - **Description** Leaf placeholder (per the welcome decision — scaffolded, not deferred). Empty `WelcomeViewModel`; `WelcomeView` is `PlaceholderScene(title: "Welcome")`.
  - **Justification** Map: `login.nav → welcome` (`todo: true` — annotation only; scaffolded as a leaf so the skeleton is clickable).
  - **Touches** scene `welcome`; files `Debug/Scenes/App/Login/Welcome/WelcomeView.swift`, `Debug/Scenes/App/Login/Welcome/WelcomeViewModel.swift`.

### library domain

- [x] T4 Add scene: library
  - **Description** Tab scene with modals. `LibraryViewModel` with `LibrarySheetRoute { case profile }` and `LibraryCoverRoute { case search }`. `LibraryView` uses `PlaceholderScene(title: "Library", routes: [.sheet → profile, .fullScreen → search], tabs: [Notes/`note.text`, Folders/`folder`, Trash/`trash`])`, each tab content `NavigationStack { …View() }`. Attach `.sheet(item:)` (profile, `NavigationStack`-wrapped, `showsDismiss: true`, crumb "Library") and `.fullScreenCover(item:)` (search, same).
  - **Justification** Map: `domains.library` (collapsed), `tab: [notes, folders, trash]`, `modal: [profile sheet, search full_screen]`.
  - **Touches** scene `library`; routes `library.tab → notes/folders/trash`, `library.modal → profile/search`; files `Debug/Scenes/Library/LibraryView.swift`, `Debug/Scenes/Library/LibraryViewModel.swift`.

- [x] T5 Add scene: notes
  - **Description** Nav scene. `NotesViewModel` with `NotesNavRoute { case note }`. `NotesView` is `PlaceholderScene(title: "Notes", routes: [.nav → note])` + `.navigationDestination(item:)` yielding `NoteView().environment(\.placeholderShowsDismiss, false).placeholderCrumb("Notes")`. No own stack (its tab supplies one).
  - **Justification** Map: `library.tab → notes`, `notes.nav: [note]`.
  - **Touches** scene `notes`; route `notes.nav → note`; files `Debug/Scenes/Library/Notes/NotesView.swift`, `Debug/Scenes/Library/Notes/NotesViewModel.swift`.

- [x] T6 Add scene: folders
  - **Description** Leaf. Empty `FoldersViewModel`; `FoldersView` is `PlaceholderScene(title: "Folders")`.
  - **Justification** Map: `library.tab → folders` (`{}`).
  - **Touches** scene `folders`; files `Debug/Scenes/Library/Folders/FoldersView.swift`, `Debug/Scenes/Library/Folders/FoldersViewModel.swift`.

- [x] T7 Add scene: trash
  - **Description** Leaf. Empty `TrashViewModel`; `TrashView` is `PlaceholderScene(title: "Trash")`.
  - **Justification** Map: `library.tab → trash` (`{}`).
  - **Touches** scene `trash`; files `Debug/Scenes/Library/Trash/TrashView.swift`, `Debug/Scenes/Library/Trash/TrashViewModel.swift`.

### note domain

- [x] T8 Add scene: note
  - **Description** Composite + modals. `NoteViewModel` with `NotePopoverRoute { case tagPicker }`, `NoteSheetRoute { case shareSheet }`, `NoteCoverRoute { case attachmentViewer, search }` (two `full_screen` targets share `coverRoute`). `NoteView` uses the embedded form `PlaceholderScene(title: "Note", routes: [.popover → tagPicker, .fullScreen → attachmentViewer, .sheet → shareSheet, .fullScreen → search]) { EditorView() }`, then `.popover(item:)` (tagPicker, `+ .presentationCompactAdaptation(.popover)`, no stack), `.sheet(item:)` (shareSheet, stack), `.fullScreenCover(item:)` (attachmentViewer + search, stack). All modal destinations `showsDismiss: true`, crumb "Note".
  - **Justification** Map: `domains.note` (collapsed), `composite: [editor]`, `modal: [tag_picker popover, attachment_viewer full_screen, share_sheet sheet, search full_screen]`.
  - **Touches** scene `note`; routes `note.composite → editor`, `note.modal → tag_picker/attachment_viewer/share_sheet/search`; files `Debug/Scenes/Note/NoteView.swift`, `Debug/Scenes/Note/NoteViewModel.swift`.

- [x] T9 Add scene: tag_picker
  - **Description** Leaf. Empty `TagPickerViewModel`; `TagPickerView` is `PlaceholderScene(title: "Tag Picker")`.
  - **Justification** Map: `note.modal → tag_picker` (`modal_style: popover`).
  - **Touches** scene `tag_picker`; files `Debug/Scenes/Note/TagPicker/TagPickerView.swift`, `Debug/Scenes/Note/TagPicker/TagPickerViewModel.swift`.

- [x] T10 Add scene: attachment_viewer
  - **Description** Leaf. Empty `AttachmentViewerViewModel`; `AttachmentViewerView` is `PlaceholderScene(title: "Attachment Viewer")`.
  - **Justification** Map: `note.modal → attachment_viewer` (`modal_style: full_screen`).
  - **Touches** scene `attachment_viewer`; files `Debug/Scenes/Note/AttachmentViewer/AttachmentViewerView.swift`, `Debug/Scenes/Note/AttachmentViewer/AttachmentViewerViewModel.swift`.

- [x] T11 Add scene: share_sheet
  - **Description** Leaf. Empty `ShareSheetViewModel`; `ShareSheetView` is `PlaceholderScene(title: "Share Sheet")`.
  - **Justification** Map: `note.modal → share_sheet` (`modal_style: sheet`).
  - **Touches** scene `share_sheet`; files `Debug/Scenes/Note/ShareSheet/ShareSheetView.swift`, `Debug/Scenes/Note/ShareSheet/ShareSheetViewModel.swift`.

### other domain

- [x] T12 Add scene: profile
  - **Description** Nav scene. `ProfileViewModel` with `ProfileNavRoute { case web }`. `ProfileView` is `PlaceholderScene(title: "Profile", routes: [.nav → web])` + `.navigationDestination(item:)` yielding `WebView().environment(\.placeholderShowsDismiss, false).placeholderCrumb("Profile")`. Add `import UI` (WebView crosses the module boundary). Its `sheet` modal_style is how `library` presents it, not its own routing.
  - **Justification** Map: `domains.other.scenes → profile` (`modal_style: sheet`), `profile.nav: [web]`.
  - **Touches** scene `profile`; route `profile.nav → web`; files `Debug/Scenes/Other/Profile/ProfileView.swift`, `Debug/Scenes/Other/Profile/ProfileViewModel.swift`.

- [x] T13 Add scene: search
  - **Description** Leaf (reused from `library.modal` and `note.modal`). Empty `SearchViewModel`; `SearchView` is `PlaceholderScene(title: "Search")`. `primary_parent: library` is render-only — folder stays under `Other/`, no move.
  - **Justification** Map: `domains.other.scenes → search` (`modal_style: full_screen`, `primary_parent: library`).
  - **Touches** scene `search`; files `Debug/Scenes/Other/Search/SearchView.swift`, `Debug/Scenes/Other/Search/SearchViewModel.swift`.

- [x] T14 Add scene: editor
  - **Description** Leaf (composite child of `note`, instantiated directly in `NoteView`'s embedded builder). Empty `EditorViewModel`; `EditorView` is `PlaceholderScene(title: "Editor")`.
  - **Justification** Map: `domains.other.scenes → editor` (`{}`), referenced by `note.composite`.
  - **Touches** scene `editor`; files `Debug/Scenes/Other/Editor/EditorView.swift`, `Debug/Scenes/Other/Editor/EditorViewModel.swift`.

### common

- [x] T15 Add scene: web
  - **Description** Leaf in the shared `UI` module. `public struct WebView` with `public init()` (constructed across the module boundary by `ProfileView`); internal `WebViewModel`. `WebView` is `PlaceholderScene(title: "Web")`. `implements: [privacy_policy, terms_of_service]` models **no** inputs — new-scene rule (no variant enum, no init params).
  - **Justification** Map: `common → web` (`implements: [privacy_policy, terms_of_service]`); `ui-map-swiftui.md`: `common:` scenes live in the shared UI module.
  - **Touches** scene `web`; files `UI/Scenes/Web/WebView.swift`, `UI/Scenes/Web/WebViewModel.swift`.

**Completion build** (all entries; cross-domain refs compile only once all scenes exist):
[evidence: `xcodebuild build -scheme Debug -project Submodules/skai/Debug/SwiftUI/Debug.xcodeproj -destination 'platform=iOS Simulator,name=iPhone 17 Pro,OS=26.4'`; BUILD SUCCEEDED; output: working-docs/main/placeholder-scaffold/implementation/evidence/build.txt]

## Deferrals

(none)

## Out of scope

- The map itself: it validates and is the approved input — this pass makes no `ui-map.yaml` edits, so there is no map diff and no re-render; the existing demo render stands as the target.
- Feature content: placeholders are skeleton + navigation only (the placeholder boundary). No real UI, business logic, or data.
- `folders` subfolder navigation: tracked by the map's `todos[scope=folders]` ("Subfolder navigation planned for v2"); `folders` is scaffolded as a leaf tab.
- `web`'s `implements` variants (privacy policy / terms of service): feature content, not modeled — the placeholder takes no inputs.
