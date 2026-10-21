# UI Map Plan — notes-domain

## Goal

Introduce a `notes` domain, move the `notes` (list) scene into it as the domain root, and merge the existing `note` domain (the `note` scene + its sub-scenes) into it. The standalone `note` domain is removed.

## Inputs

- Current map: `Submodules/skai/Debug/SwiftUI/ui-map.yaml` (LumenNotes; code just scaffolded by the `placeholder-scaffold` plan).
- Current code: `Submodules/skai/Debug/SwiftUI/` — `Debug` app target (`Debug/Scenes/…`) + `UI` framework; synchronized Xcode groups (folder moves auto-update target membership).
- YAML format: `Submodules/skai/Guides/Dev/ui-map-guide.md`; folder org / colors: `Submodules/skai/Guides/Dev/ui-map-swiftui.md`, `SKAISwiftUI/Colors.swift` (palette is positional/indexed).
- Render tooling: `Submodules/skai/Bin/ui-map-render.py` (no fixture-specific wrapper; invoked directly on the fixture's `ui-map.yaml`).

## Discussion

### Current structure

- `notes` is a scene defined inline under `library.tab` → it belongs to the `library` domain (folder `Debug/Scenes/Library/Notes/`). Its only route: `nav → note`.
- `note` is its own collapsed domain (root `note`), with `composite: [editor]` and `modal: [tag_picker popover, attachment_viewer full_screen, share_sheet sheet, search full_screen]` (folder `Debug/Scenes/Note/…`).
- `editor` and `search` are cross-domain refs into the `other` domain — unaffected (they stay where defined).
- `library` keeps its **Notes** tab; after the move `library.tab → notes` becomes a cross-domain reference (no folder move for the reference).

### Domain shape

- [x] Proposal — make `notes` a **collapsed** domain (domain id == root scene `notes`), with `note` and its whole subtree defined inline under `notes.nav` (merged from the removed `note` domain). This matches the existing `notes.nav → note` route and the collapsed pattern used by `app`/`library`. A non-collapsed *container* domain isn't viable here: its domain id would collide with the `notes` scene. Net YAML: the `note:` top-level domain is deleted; a `notes:` collapsed domain is added carrying `nav: [note: { composite/modal … }]`; `library.tab`'s `notes` becomes a bare cross-domain ref.
  - **Decision** Collapsed `notes` domain (root scene `notes`); merge `note` + subtree inline under `notes.nav`; delete the `note` domain; `library.tab → notes` becomes a cross-domain ref.

### Palette / declaration order

Domain colors are positional (`Colors`/render palette by declaration order). Current: `app`(0), `library`(1), `note`(2), `other`(3), `common`(last).

- [x] Proposal — declare `notes` in the slot the removed `note` domain vacates (position 2, right after `library`): `app`(0), `library`(1), **`notes`(2)**, `other`(3), `common`(last). The palette is unchanged — `notes` inherits slot 2, and `other`/`common` keep their colors. Code impact: the `note` subtree already uses slot 2; only the `notes` scene's tint changes (`Colors.library` → slot 2). (Slot 2 is the static currently named `Colors.note` — the known indexed-naming miss; value is correct.)
  - **Decision** Declare `notes` at position 2 (the slot `note` vacates); palette unchanged; only the `notes` scene's tint shifts to slot 2.

## Change list

(populated in Phase 2)

## Deferrals

(populated in Phase 2)

## Out of scope

(populated in Phase 2)
