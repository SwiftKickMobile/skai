# UI Map Compose refinement findings

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-09-02 | R1 F1 — guide falsely required project-vendored libraries | closed | Official SKAI Compose dependency selection and mechanical attachment now live in `ui-map-compose.md`. |
| 2026-09-02 | R1 F2 — Android-only Hilt conventions were mandatory for shared KMP | closed | Guide now branches on the consuming source set and makes Hilt an established Android-only option. |
| 2026-09-02 | R1 F3 — modal examples named nonexistent APIs and defaults | closed | Canonical modal table and examples match `ModalNavHost`, `bottomSheet`, `bottomSheetFullScreenModal`, and `dialog`; both artifacts compile. |
| 2026-09-02 | R1 F4 — indexed domain-color API was missing | closed | `PlaceholderColors.domain(index)` implements all nine renderer slots, wraps, and compiles in both artifacts. |
| 2026-09-02 | R1 F5 — destination helpers lost presenter route menus/ancestry | closed | Push and modal helpers append inherited crumbs with the shared presenter route list; examples reuse one list. |
| 2026-09-02 | R1 F6 — root placeholders rendered as embedded composites | closed | `LocalPlaceholderIsEmbedded` is supplied only around composite children; root/start scenes are full-bleed. |
| 2026-09-02 | R1 F7 — long breadcrumbs opened on the ancestor end | closed | Breadcrumb scroll state moves to its maximum when the path or measured range changes. |
| 2026-09-02 | R1 F8 — production cleanup could remove routing still in use | closed | Cleanup now retains the combined dependency while either routing or placeholder symbols remain. |
| 2026-09-02 | R1 F9 — state-file rule contradicted the stateless exemption | closed | State/event/effect files are required only for scenes with state-management responsibility. |
| 2026-09-02 | R2 F1 — tabbed modal destination lost dismiss context | closed | Tab scaffolding now inherits the presentation context; embedded and pushed boundaries preserve their distinct resets. |
| 2026-09-02 | R2 F2 — dependency placement was ambiguous in a mixed KMP module | closed | Paired Gradle examples place the KMP artifact in `commonMain`, prohibit an additional Android artifact, and show the plain-Android alternative. |
| 2026-09-02 | R2 F3 — pushed helper allowed omission of its back action | closed | `onBack` is required and non-null; no external workspace caller required migration. |
| 2026-09-02 | R3 F1 — tab-plus-composite placeholders silently omitted composite children | closed by owner ruling | The current renderer's combined shape is documented as unsupported and blocks in Discussion; real app architecture remains unrestricted. |
| 2026-09-02 | R3 F2 — setup omitted the consuming module's serialization compiler prerequisite | closed | Setup now inspects/adds the project-compatible plugin mechanically and blocks on incompatible constraints. |
| 2026-09-02 | R3 F3 — worked placeholder scaffolds omitted file-level markers | closed | Every Kotlin scaffold example now begins with the exact change-id marker; leaf view-model and screen examples are separate files. |
