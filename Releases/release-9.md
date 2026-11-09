# Release 9 — 2026-10-05

**UI Map renderer**

- **Left-to-right ELK layout.** `Bin/ui-map-render.py` renders maps as `flowchart LR`, laid out by Mermaid's bundled ELK engine with simple node placement, and puts the domain legend in a single column. Deep maps come out far less wide. No YAML or schema change, and nothing to install beyond the Mermaid CLI. `Guides/UIMap/ui-map-demo.md`'s render is regenerated to match.
- **A scene referenced twice by one parent draws twice.** Pointer node ids include the route kind (`<target>_at_<source>_<kind>`), so a parent listing the same scene under two route kinds (e.g. `nav` and `modal`) shows the pointer in both wrappers instead of leaving one empty.

**Upgrade instructions**

1. **No adapter re-run is required by this release.** No installed asset changed. A host upgrading from Release 7 or earlier still follows Release 8's upgrade instructions.
2. **Re-render UI Maps** (`skai/ui-map/ui-map.svg`, and any open change package's `proposed-ui-map.svg`) to pick up the new layout and the pointer fix.
