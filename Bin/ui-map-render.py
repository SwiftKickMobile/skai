#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml",
#   "jsonschema",
# ]
# ///
"""
ui-map-render.py — render a UI Map YAML document as an interactive HTML page
or a Mermaid flowchart.

The input is a UI Map YAML document conforming to ui-map.schema.json, or a
UI Map change package's folder (rule 12, request layering).
The primary output is a static HTML page (`--html`) that loads the viewer
beside this script (the shared page library, then the viewer's own stylesheet
and script, in the versions VIEWER_ASSETS names; a version bumps only when a
change would break pages already rendered); no server is needed.
The Mermaid `flowchart LR` text (bare, no ``` fences) remains available for
documents that embed a diagram, and `--svg` still renders it through the
Mermaid CLI.

Usage:
    uv run ui-map-render.py <input.yaml> --html <output.html>    # the interactive map
    uv run ui-map-render.py <input.yaml> --html <o.html> --open  # render, then open it
    uv run ui-map-render.py <package>/ui-map --html <o.html>   # a package's page: its map, else the nearest up its chain
    uv run ui-map-render.py <input.yaml>                     # write Mermaid to stdout
    uv run ui-map-render.py <input.yaml> -o <output.mmd>     # write Mermaid to a file
    uv run ui-map-render.py <input.yaml> --markdown          # wrap in ```mermaid fences
    uv run ui-map-render.py <input.yaml> --svg <output.svg>  # also render an SVG
    uv run ui-map-render.py <input.yaml> --no-validate       # skip JSON Schema validation

The HTML, Mermaid-text (-o / --markdown / stdout) and --svg outputs are
independent and may be combined in a single invocation.

SVG rendering shells out to the Mermaid CLI (`mmdc`) — an optional external
dependency, not a Python package. Install it with `brew install mermaid-cli`
or `npm install -g @mermaid-js/mermaid-cli`. `mmdc` drives a headless Chrome
via Puppeteer; when PUPPETEER_EXECUTABLE_PATH is unset, the script points it at
an installed Chrome/Chromium if it can find one. `--open` opens the SVG in a
browser (macOS forces one explicitly, since Preview cannot display SVG;
override the choice with the UI_MAP_BROWSER env var).

Tip on running:
    `uv run` (from https://docs.astral.sh/uv/) reads the PEP 723 metadata at the
    top of this file and runs in an isolated environment. `pipx run` works too
    on recent versions. Both keep the host Python untouched.

================================================================
RENDER CONVENTIONS (the script's authoritative spec)
================================================================

These rules are what the script applies. They are the canonical render spec;
the demo doc and the guide describe the same conventions in prose.

1. OVERALL STRUCTURE
   - A `---`-delimited front matter sets Mermaid config: the ELK layout
     engine with SIMPLE node placement (more compact than Mermaid's default
     layout for deep maps), padding 12, nodeSpacing 30, rankSpacing 40,
     subGraphTitleMargin top/bottom 0. ELK ships inside Mermaid; no extra
     install is needed beyond the Mermaid CLI.
   - The diagram is `flowchart LR`: depth runs left to right and siblings
     stack top to bottom, which keeps deep maps far less wide than a
     top-down layout.
   - The first block is a Domain Legend subgraph (one labeled node per
     domain, colored to match the scenes in that domain), laid out as a
     single column so it does not stretch the diagram's width.
   - All canonical scenes are declared next at top level (stadium shape).
   - Outgoing routes are emitted per source scene, in YAML declaration order.
   - Callouts (implements, notes) are emitted after routes.
   - classDef and class assignments are emitted last.

2. SCENES
   - Every scene is rendered with the same shape: stadium `(["Label"])`.
   - Fill color encodes the scene's DOMAIN (see DOMAIN_PALETTE below).
   - Two overrides take precedence over the plain domain fill:
       * TODO scene (`todo: true`) → keeps the domain identity but signals the
         unimplemented state: full-opacity domain color as a 2px stroke, with
         the domain color at 0.3 alpha as the fill.
       * Pointer (non-canonical reference) → gray fill `#bdbdbd`, dark text.
   - Drop shadows are disabled via `filter: none` on every classDef.
   - Each scene's label is derived by humanizing its snake_case ID
     (`appointment_details` → `Appointment Details`).

3. DOMAINS AND PALETTE
   - Each domain in the YAML's `domains:` section maps to a palette color in
     declaration order using `DOMAIN_PALETTE`, the single authoritative list
     of palette values below.
   - Scenes inside `common:` form their own pseudo-domain `common`, appended
     last in declaration order and labeled "Common" in the legend; it takes
     the next palette slot after the real domains. Common scenes still render
     at their canonical position (their consumer's wrapper) — only the fill
     color and the legend entry mark them as common.
   - The Domain Legend subgraph at the start of the diagram contains one node
     per domain, named `leg_<domain_id>`, classed with that domain's color.

4. CANONICAL POSITION (which wrapper holds the rounded-rect instance)
   The script chooses each scene's visual home by these rules, in order:
     a. `primary_parent: X` set → canonical instance renders inside X's wrapper
        that routes to this scene. The route kind is the unique kind connecting
        X to this scene; if X routes to this scene via multiple kinds, the
        kind whose container defines the scene wins, falling back to the first
        declared kind when the scene is defined elsewhere.
     b. Exactly one inbound reference → that single parent's wrapper.
     c. Zero inbound references → root scene: declared at top level, no
        enclosing wrapper.
     d. Multiple inbound references with no `primary_parent` → semantic error.
     e. Every scene must be reachable from a root through its visual homes; a
        loop of visual homes → semantic error listing the scenes it strands.

5. WRAPPERS (one per route container)
   - Each route kind on a scene becomes a `subgraph <sid>_<kind>[" "]` (empty
     title; the route-kind label sits on the incoming arrow).
   - Mutex wrappers (nav, modal, tab, child): white fill, dashed gray border
     (`stroke-dasharray:10 5`).
   - Composite wrappers (composite): light-gray fill `#f0f0f0`, no visible
     border (`stroke-width:0px`).
   - When a wrapper contains more than one node, the script adds
     `direction LR` inside the subgraph.

6. POINTERS (non-canonical references)
   - When a scene `T` appears in a route container whose source `S` is NOT T's
     visual parent, the script renders a separate pointer node inside S's
     wrapper: `<T>_at_<S>_<kind>` with the same label as the canonical `T`,
     classed `pointer` (gray fill — overrides T's domain color). The route
     kind is part of the id so that S referencing T under two route kinds
     (e.g. `nav` and `modal`) renders a pointer in each wrapper.
   - The canonical `T` is unaffected; it renders inside its visual parent's
     wrapper with its domain fill.

7. EDGE LABELS
   - Each route arrow gets a labeled span with white background, black border,
     small padding, and dark text. Inline HTML used because Mermaid's default
     `.labelBkg` styling is low-contrast.
   - Label text is the route kind, capitalized (`Nav`, `Modal`, `Composite`,
     `Tab`, `Child`).

8. CALLOUTS — IMPLEMENTS
   - For each scene with `implements:`, emit a right-leaning parallelogram
     node `impl_<sid>` with text `Implements: A, B, C` (single line; variants
     joined by commas).
   - Attached to the scene via dashed connector `-.-`.
   - Fill matches the attached scene's domain color.

9. CALLOUTS — NOTES
   - Scene `note:` field → one yellow `tag-rect` node (notched corner, a
     sticky-note look).
   - Scene `notes:` field → one per item.
   - Each note is `note_<sid>` (or `note_<sid>_<i>` for multiple notes on a
     single scene), attached via dashed connector.
   - If a note item is an object with `at: <kind>`, the connector attaches to
     the wrapper `<sid>_<kind>` instead of the scene itself.
   - Note style: pale yellow `#fff7d6`, muted gold stroke `#d4c171`, dark text.

10. CALLOUTS — MODAL STYLES
    - For each modal wrapper `<sid>_modal`, emit one callout `mstyle_<sid>`
      listing each destination as `Scene Name <b>style</b>` — the required style
      bolded — comma-separated on a single line to keep the callout short.
    - Shape is a right-leaning parallelogram, matching the implements callout.
    - Attached to the wrapper via `-.-` (not to the scenes inside — keeps the
      connector off the wrapper interior).
    - Styled to match the mutex wrapper it describes (white fill, dashed gray
      border: `stroke:#999`, `stroke-dasharray:10 5`). It annotates the
      wrapper, not a single scene, so it can't take a scene's domain color
      the way an implements callout does.
    - The scene's `modal_style` must be one of the document's top-level
      `modal_styles`; the build step validates this.

11. WHAT IS NOT RENDERED
    - Top-level `todos:` list: not rendered visually; surfaced via a separate
      report mode (TODO: not yet implemented in this script).
    - Cross-platform `platform:` field: not rendered; informational only.

12. HTML OUTPUT (--html)
    - A static page: the map model inline as `window.UI_MAP` JSON, plus
      stylesheet links and script tags for the shared page library (shared
      with the spec and design review pages) and the viewer's own stylesheet
      and script beside this script, in the versions VIEWER_ASSETS names,
      referenced by a path relative to the output file; a change package's
      page also links the review pages' stylesheet (REVIEW_ASSET) for its
      Review tab. No web fonts: the system font, with IDs and route kinds in
      the system monospace. The page follows the system theme.
      The page works from file:// and from any static server; it needs the
      SKAI checkout at that relative location and nothing else. `--open`
      opens it.
    - The model carries, per scene: id, humanized label, domain, canonical
      home (visual parent and route kind, rule 4), route containers in YAML
      order with their destinations, `implements`, `modal_style`, notes
      (with `at:` when attached to a route container, rule 9), `todo`, and
      every inbound route. Plus the domain list in palette order (rule 3),
      the modal-style vocabulary, scene order, the root scenes, and `review`
      (below; null on the production map).
    - Layout: levels as rows — depth in the canonical-home tree — at a fixed
      cell width that never shrinks, the page growing vertically. Each scene's
      route containers sit in the row below it as dashed boxes (composite:
      filled, no border) holding the destination cells, with the route kind as
      a label on the connector. A box is never shared between scenes, so every
      connector runs one row down. A row too wide for the window wraps
      between route containers, never inside one, so a scene's containers may
      land on different lines. Each visual line is centred horizontally in the
      window; a line too wide to fit stays flush left.
    - Cells: neutral boxes with the title centred (two lines, then clipped), a
      domain colour swatch top-left and icons top-right marking only the
      existence of callouts — notes, implements, modal style — whose content the
      side panel shows. A pointer (rule 6) is a lighter cell with a reuse
      arrow; clicking it selects the canonical scene.
    - Selection: clicking a scene filters the page to its connected
      neighbourhood (1 hop by default; 2 hops or All from the control in the
      top bar), removes everything else and collapses empty rows. The
      selected cell, its route boxes, every box holding it, and their
      connectors and labels are highlighted; All shows the whole map and dims
      the unconnected parts instead. Clicking the selected cell again,
      clicking empty canvas, or Escape restores the full map; closing the
      side panel instead leaves the scene selected and the view filtered,
      uncovering the part of the map it hid without moving anything (see
      Placement). The domain filters filter the same way (multi-select; a
      domain is dropped by clicking it again). A search box highlights
      matches and dims the rest; Enter selects the first; a cross inside the
      box, shown while it has a value, clears it. While a selection or domain
      filter narrows the map, nothing is dimmed.
    - Placement after a selection, in priority order: the selected cell is
      fully visible and clear of the side panel; as much cell area as possible
      is visible, counted continuously so that closing a gap always beats
      leaving one beside a clipped cell; of what does not fit, as little as
      possible falls off the left edge, so overflow sits under the side panel
      instead; the selected cell is as close as possible to its home, its
      place in the full map. A cell already at home does not move. Dismissing
      the side panel re-places nothing: the graph keeps the place it has and
      the overflow the panel covered is simply revealed. Placement is a graph
      offset plus a scroll position, kept on the 4px layout grid so 1px
      borders stay crisp at fractional device pixel ratios.
    - Animation: on every state change, cells, route boxes and labels present
      before and after slide (and boxes resize) to their new place, departing
      elements fade out, arriving ones fade in. The side panel slides in when
      it opens and changes content in place while open. A window resize
      reflows without animating. Off under prefers-reduced-motion.
    - Side panel for the selected scene: its domain, then Changes on a change
      package's page (below), Reached from (every inbound route with its
      kind, tagged home/reused when the scene appears more than once), Opens
      (per route kind, with route notes inline), Notes, Implements, Modal
      style (each headed by the cell's icon, in the heading's colour; ids
      shown humanized). Headings carry no counts. The panel's footprint is a
      safe area: the layout width does not change when it opens, and the
      canvas scrolls under it.
    - Top bar: one-line title, "UI Map" then the package's ID in cyan — the
      change folder above `ui-map/` (a request's IDs chained, "offers | CR-01")
      for a proposed map, else "Production". The HTML <title> keeps the app's
      name ("<app> UI Map"). On the right: the hops drop-down (1 hop, 2 hops,
      All; a fixed width, shown only while a selection or domain filter
      narrows the map, before the domain filters so they never move), the
      domain filters in the review pages' filter style (each domain's colour,
      scene count and name), the Changes toggle on a change package's page,
      the search box, and "?", which opens a legend: the cell and box
      vocabulary, the change badge on a change package's page, the route
      kinds, and the controls. No theme or reset button.
    - A change package's page (the input in a change package's `ui-map/`
      folder, with `ui-map-architecture.md` beside it) reads that artifact's
      Discussion and `## Map Changes`: `### <domain>` headings, entries
      `- M<n> <operation> <element>: <identity>` (operation add, remove, move,
      modify; element domain, scene, route, scene-attribute; the identity a
      scene ID, or a domain ID for a domain change) with Description and
      Justification, or numbered sub-changes `- **01** <change> — <reason>`,
      and gap footnotes. Its top bar adds Map and Review tabs; the page opens
      on Map.
        * Change badges: a scene is changed when an entry names it — a scene,
          route or attribute entry, except a removed scene; a domain change
          marks nothing. Every cell of a changed scene, reused ones too,
          carries the badge: a square in the cell's border colour in its
          bottom right corner, with a triangle.
        * The Changes toggle shows the changed-scene count; on, it shows
          changed scenes as search shows its matches.
        * The side panel of a changed scene opens with Changes: one card per
          entry naming it — marker, ID linking to the entry in the Review tab,
          type, then the description and reason, or the numbered changes with
          their reasons (reasons without their source), then gap footnotes.
        * The Review tab is the design review page's layout: the summary box
          (state and goal), the Discussion, then Map Changes under each
          domain's heading with its colour square, each entry a card whose
          header shows its marker, ID, type and the scene's name linking to
          it on the map; a domain change names its domain unlinked, a removed
          scene is greyed and unlinked. Its top bar filters by change type
          (added, modified, removed, moved) and by the discussion states the
          package has (open, gaps, resolved), as on the review pages.
        * A list whose first line is `Pending re-derivation.` (a reopened
          package's inherited list) is shown with that line and not checked.
        * Links: `#map`, `#review`, `#scene=<id>` and an element of the
          Review tab (`#m3`, `#d01`) open that tab, scene or entry.
    - Request layering: a request's `ui-map/` sub-package renders the
      nearest proposed map up its chain — its own `proposed-ui-map.yaml`,
      else each base package's (spec-tool.py's chain_bases), else the
      production map `skai/ui-map/ui-map.yaml` — with its own architecture
      artifact. Pass the package folder (or its missing proposed map) to use
      it; an existing YAML file is always rendered as given.

13. ERRORS
    - Schema validation runs first (unless --no-validate); failures abort.
    - Semantic validation runs next; failures abort with a specific message.
      Categories: duplicate canonical home, undefined scene reference,
      ambiguous visual home (multiple inbound, no primary_parent),
      `primary_parent` that doesn't actually route to the scene,
      visual homes that form a loop,
      too many domains for the palette, missing modal_style or vocabulary,
      modal_style outside the vocabulary, and, on a change package's page,
      a Map Changes entry not in the entry format or naming a scene or
      domain not on the proposed map (except one it removes; never checked
      while the list is pending re-derivation).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
from html import escape as html_escape
import html
import os
from urllib.parse import quote
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import jsonschema
import yaml

# The review pages' renderer, for a change package's Review tab: its Discussion, summary box and
# change cards (design-tool.py), and through it spec-tool.py's request chain and citation links.
_dt_spec = importlib.util.spec_from_file_location("design_tool", Path(__file__).with_name("design-tool.py"))
dt = importlib.util.module_from_spec(_dt_spec)
_dt_spec.loader.exec_module(dt)
st = dt.st

ROUTE_KINDS: tuple[str, ...] = ("nav", "modal", "composite", "tab", "child")

# Pseudo-domain id for scenes in the YAML's top-level `common:` group. Appended
# last in domain order so it renders as the final "Common" legend entry and
# takes the next palette slot after the real domains.
COMMON_DOMAIN_ID = "common"

# Fill colors assigned to domains in YAML declaration order.
# A project with more domains than slots is a semantic error.
DOMAIN_PALETTE: tuple[str, ...] = (
    "#8AD1FA",  # 1
    "#EFD74E",  # 2
    "#FE9CA8",  # 3
    "#78DB85",  # 4
    "#D39AE7",  # 5
    "#FFB677",  # 6
    "#87AFFF",  # 7
    "#37D8CB",  # 8
    "#F277D5",  # 9
)

# Overrides — applied after domain assignment.
# TODO scenes render with the domain stroke + a 0.3-alpha domain fill so the
# domain stays identifiable but the unimplemented state is unmistakable.
TODO_FILL_ALPHA = 0.3
TODO_STROKE_WIDTH = "2px"
POINTER_FILL = "#bdbdbd"

TEXT_DARK = "#231f20"

# Font size for secondary nodes (implements parallelograms, note stickies,
# domain-legend entries). Smaller than the default scene font so these read
# as secondary to the main scene graph.
SMALL_FONT_SIZE = "13px"


def _hex_with_alpha(hex_str: str, alpha: float) -> str:
    """Return an 8-digit hex (#RRGGBBAA). Mermaid classDef rejects rgba()."""
    h = hex_str.lstrip("#")
    return f"#{h}{round(alpha * 255):02X}"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class Model:
    """Resolved UI Map model used by the renderer."""

    version: int
    app: str
    scenes: dict[str, dict[str, Any]] = field(default_factory=dict)  # id -> body
    edges: list[tuple[str, str, str]] = field(default_factory=list)  # (parent, kind, target)
    inbound: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    visual_parent: dict[str, tuple[str | None, str | None]] = field(default_factory=dict)
    scene_domain: dict[str, str | None] = field(default_factory=dict)  # id -> domain_id
    domain_order: list[str] = field(default_factory=list)  # domains in YAML order
    modal_styles: list[str] = field(default_factory=list)  # project modal-style vocabulary
    todos: list[dict[str, Any]] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Loading and validation
# ---------------------------------------------------------------------------


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text())


def validate_schema(data: dict[str, Any], schema_path: Path) -> None:
    schema = json.loads(schema_path.read_text())
    jsonschema.validate(data, schema)


# ---------------------------------------------------------------------------
# Parsing — walk YAML, collect scenes, edges, and domain assignments
# ---------------------------------------------------------------------------


class SemanticError(ValueError):
    pass


def _scene_id_and_body(item: Any) -> tuple[str, dict[str, Any] | None]:
    """Split a scene list item into (id, body). String → (id, None) for refs."""
    if isinstance(item, str):
        return item, None
    if isinstance(item, dict) and len(item) == 1:
        scene_id = next(iter(item.keys()))
        body = item[scene_id]
        return scene_id, (body if body is not None else {})
    raise SemanticError(f"Invalid scene list item: {item!r}")


def _walk_item(
    item: Any,
    parent_id: str | None,
    route_kind: str | None,
    domain_id: str | None,
    scenes: dict[str, dict[str, Any]],
    edges: list[tuple[str, str, str]],
    scene_domain: dict[str, str | None],
    definition_site: dict[str, tuple[str | None, str | None]],
) -> None:
    scene_id, body = _scene_id_and_body(item)
    if parent_id is not None and route_kind is not None:
        edges.append((parent_id, route_kind, scene_id))
    if body is None:
        return  # bare reference
    if scene_id in scenes:
        raise SemanticError(f"Duplicate canonical home for scene '{scene_id}'")
    scenes[scene_id] = body
    scene_domain[scene_id] = domain_id
    definition_site[scene_id] = (parent_id, route_kind)
    for kind in ROUTE_KINDS:
        for sub_item in body.get(kind, []) or []:
            _walk_item(
                sub_item, scene_id, kind, domain_id, scenes, edges, scene_domain, definition_site
            )


def build_model(data: dict[str, Any]) -> Model:
    scenes: dict[str, dict[str, Any]] = {}
    edges: list[tuple[str, str, str]] = []
    scene_domain: dict[str, str | None] = {}
    definition_site: dict[str, tuple[str | None, str | None]] = {}
    domain_order: list[str] = []

    for domain_id, domain_data in data["domains"].items():
        domain_order.append(domain_id)
        if "scenes" in domain_data:
            for item in domain_data["scenes"]:
                _walk_item(
                    item, None, None, domain_id, scenes, edges, scene_domain, definition_site
                )
        else:
            _walk_item(
                {domain_id: domain_data},
                None,
                None,
                domain_id,
                scenes,
                edges,
                scene_domain,
                definition_site,
            )

    common_items = data.get("common", []) or []
    for item in common_items:
        _walk_item(
            item, None, None, COMMON_DOMAIN_ID, scenes, edges, scene_domain, definition_site
        )
    if common_items:
        domain_order.append(COMMON_DOMAIN_ID)

    inbound: dict[str, list[tuple[str, str]]] = {sid: [] for sid in scenes}
    for parent_id, kind, target_id in edges:
        if target_id not in scenes:
            raise SemanticError(
                f"Undefined scene reference: '{target_id}' (from '{parent_id}.{kind}')"
            )
        inbound[target_id].append((parent_id, kind))

    visual_parent: dict[str, tuple[str | None, str | None]] = {}
    for sid, body in scenes.items():
        pp = body.get("primary_parent")
        if pp is not None:
            if pp not in scenes:
                raise SemanticError(f"primary_parent '{pp}' (on '{sid}') is not a defined scene")
            kinds = [k for (p, k) in inbound[sid] if p == pp]
            if not kinds:
                raise SemanticError(f"primary_parent '{pp}' does not route to '{sid}'")
            # When the primary parent reaches this scene by more than one route
            # kind, render the canonical instance in the container the map
            # actually defines it under; otherwise fall back to route order.
            def_parent, def_kind = definition_site.get(sid, (None, None))
            if def_parent == pp and def_kind in kinds:
                visual_parent[sid] = (pp, def_kind)
            else:
                visual_parent[sid] = (pp, kinds[0])
        elif len(inbound[sid]) == 1:
            visual_parent[sid] = inbound[sid][0]
        elif len(inbound[sid]) == 0:
            visual_parent[sid] = (None, None)
        else:
            listing = ", ".join(f"{p}.{k}" for p, k in inbound[sid])
            raise SemanticError(
                f"Scene '{sid}' has {len(inbound[sid])} inbound refs ({listing}) "
                f"but no primary_parent"
            )

    # Every scene must hang from a root. A loop of visual homes (e.g. a
    # primary_parent the scene itself routes to) would silently drop its scenes.
    placed = {sid for sid, (p, _) in visual_parent.items() if p is None}
    while grown := {sid for sid, (p, _) in visual_parent.items() if p in placed} - placed:
        placed |= grown
    if unplaced := [sid for sid in scenes if sid not in placed]:
        raise SemanticError(
            f"Visual homes form a loop, so these scenes can't be placed: {', '.join(unplaced)}. "
            "Give one of them a primary_parent outside the loop"
        )

    if len(domain_order) > len(DOMAIN_PALETTE):
        raise SemanticError(
            f"Too many domains ({len(domain_order)}) for palette "
            f"({len(DOMAIN_PALETTE)} slots). Extend DOMAIN_PALETTE."
        )

    # Every modal destination has an implementation-significant style from the
    # project's declared vocabulary.
    modal_styles = data.get("modal_styles", []) or []
    modal_style_set = set(modal_styles)
    modal_edges = [edge for edge in edges if edge[1] == "modal"]
    if modal_edges and not modal_style_set:
        raise SemanticError(
            "The map contains modal routes but has no top-level 'modal_styles' vocabulary"
        )
    for parent_id, _, target_id in modal_edges:
        if scenes[target_id].get("modal_style") is None:
            raise SemanticError(
                f"Scene '{target_id}' is reached by modal route from '{parent_id}' "
                "but has no modal_style"
            )
    for sid, body in scenes.items():
        ms = body.get("modal_style")
        if ms is None:
            continue
        if not modal_style_set:
            raise SemanticError(
                f"Scene '{sid}' declares modal_style '{ms}' but the document "
                f"has no top-level 'modal_styles' vocabulary"
            )
        if ms not in modal_style_set:
            raise SemanticError(
                f"Scene '{sid}' modal_style '{ms}' is not in modal_styles "
                f"{sorted(modal_style_set)}"
            )

    return Model(
        version=data["version"],
        app=data["app"],
        scenes=scenes,
        edges=edges,
        inbound=inbound,
        visual_parent=visual_parent,
        scene_domain=scene_domain,
        domain_order=domain_order,
        modal_styles=modal_styles,
        todos=data.get("todos", []) or [],
    )


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def humanize(scene_id: str) -> str:
    return " ".join(part.capitalize() for part in scene_id.split("_"))


def _edge_label_span(kind: str) -> str:
    return (
        f"<span style='background:white;border:1px solid black;padding:4px 8px'>"
        f"{kind.capitalize()}</span>"
    )


def _domain_class_name(domain_id: str) -> str:
    return f"{domain_id}_domain"


def render(model: Model) -> str:
    out: list[str] = []

    # Front matter
    out.extend([
        "---",
        "config:",
        "  layout: elk",
        "  elk:",
        "    nodePlacementStrategy: SIMPLE",
        "  flowchart:",
        "    diagramPadding: 20",
        "    padding: 12",
        "    wrappingWidth: 320",
        "    subGraphTitleMargin:",
        "      top: 0",
        "      bottom: 0",
        "    nodeSpacing: 30",
        "    rankSpacing: 40",
        "---",
        "flowchart LR",
    ])

    # Domain legend (one node per domain, colored to match its scenes)
    if model.domain_order:
        out.append("    %% Domains")
        out.append('    subgraph domain_legend[" "]')
        out.append("        direction TB")
        for domain_id in model.domain_order:
            out.append(f'        leg_{domain_id}(["{humanize(domain_id)}"])')
        # The legend nodes have no edges, so `direction TB` has nothing to flow.
        # Chain them with invisible edges to force a single column.
        if len(model.domain_order) > 1:
            chain = " ~~~ ".join(f"leg_{d}" for d in model.domain_order)
            out.append(f"        {chain}")
        out.append("    end")
        out.append("")

    # Canonical scene declarations
    out.append("    %% Canonical scenes")
    for sid in model.scenes:
        out.append(f'    {sid}(["{humanize(sid)}"])')
    out.append("")

    # Anchor the legend to a root scene with an invisible edge. Without this,
    # the legend subgraph is unconnected and Mermaid's layout drops it in an
    # arbitrary spot, where it can overlap real edges and route labels. The
    # invisible edge forces it onto the first rank, beside the root scene.
    if model.domain_order:
        roots = [sid for sid, vp in model.visual_parent.items() if vp == (None, None)]
        if roots:
            out.append(f"    domain_legend ~~~ {roots[0]}")
            out.append("")

    # Outgoing routes per scene
    pointer_ids: list[str] = []
    mutex_wrappers: list[str] = []
    composite_wrappers: list[str] = []

    for sid, body in model.scenes.items():
        for kind in ROUTE_KINDS:
            targets = body.get(kind)
            if not targets:
                continue
            wrapper_id = f"{sid}_{kind}"
            if kind == "composite":
                composite_wrappers.append(wrapper_id)
            else:
                mutex_wrappers.append(wrapper_id)

            label = _edge_label_span(kind)
            out.append(f'    {sid} -->|"{label}"| {wrapper_id}')
            out.append(f'    subgraph {wrapper_id}[" "]')
            if len(targets) > 1:
                out.append("        direction LR")
            for item in targets:
                target_id, _ = _scene_id_and_body(item)
                if model.visual_parent[target_id] == (sid, kind):
                    out.append(f"        {target_id}")
                else:
                    pid = f"{target_id}_at_{sid}_{kind}"
                    out.append(f'        {pid}(["{humanize(target_id)}"])')
                    pointer_ids.append(pid)
            out.append("    end")
            out.append("")

    # Implements callouts
    impl_by_domain: dict[str, list[str]] = {}
    impl_emitted = False
    for sid, body in model.scenes.items():
        impls = body.get("implements")
        if not impls:
            continue
        impl_id = f"impl_{sid}"
        text = "Implements: " + ", ".join(humanize(v) for v in impls)
        out.append(f'    {impl_id}[/"{text}"/]')
        out.append(f"    {impl_id} -.- {sid}")
        domain = model.scene_domain[sid]
        impl_by_domain.setdefault(domain, []).append(impl_id)
        impl_emitted = True
    if impl_emitted:
        out.append("")

    # Notes
    note_ids: list[str] = []

    def _emit_notes(owner_sid: str, items: list[tuple[str, str | None]]) -> None:
        for i, (text, on_kind) in enumerate(items):
            suffix = f"_{i}" if len(items) > 1 else ""
            note_id = f"note_{owner_sid}{suffix}"
            out.append(f'    {note_id}@{{ shape: tag-rect, label: "{text}" }}')
            attach_target = f"{owner_sid}_{on_kind}" if on_kind else owner_sid
            out.append(f"    {note_id} -.- {attach_target}")
            note_ids.append(note_id)

    notes_emitted = False
    for sid, body in model.scenes.items():
        items: list[tuple[str, str | None]] = []
        if body.get("note"):
            items.append((body["note"], None))
        for n in body.get("notes", []) or []:
            if isinstance(n, str):
                items.append((n, None))
            else:
                items.append((n["text"], n.get("at")))
        if items:
            _emit_notes(sid, items)
            notes_emitted = True
    if notes_emitted:
        out.append("")

    # Modal-style callouts: one per modal wrapper. Lists each destination and
    # its required style, left-aligned.
    # Attached to the wrapper (not the scenes inside) so no edge routes within.
    mstyle_callout_ids: list[str] = []
    for sid, body in model.scenes.items():
        modal_targets = body.get("modal")
        if not modal_targets:
            continue
        lines: list[str] = []
        for item in modal_targets:
            target_id, _ = _scene_id_and_body(item)
            ms = model.scenes[target_id]["modal_style"]
            lines.append(f"{humanize(target_id)} <b>{ms}</b>")
        if not lines:
            continue
        callout_id = f"mstyle_{sid}"
        inner = ", ".join(lines)
        out.append(
            f"    {callout_id}[/\"<div style='text-align:left'>{inner}</div>\"/]"
        )
        out.append(f"    {callout_id} -.- {sid}_modal")
        mstyle_callout_ids.append(callout_id)
    if mstyle_callout_ids:
        out.append("")

    # ===== Class definitions =====

    # Per-domain fills. The legend entry and all scenes in that domain share the class.
    # TODO and pointer scenes are excluded here; they get override classes below.
    todo_ids = [sid for sid, body in model.scenes.items() if body.get("todo")]
    todo_set = set(todo_ids)
    for i, domain_id in enumerate(model.domain_order):
        color = DOMAIN_PALETTE[i]
        cls = _domain_class_name(domain_id)
        out.append(
            f"    classDef {cls} fill:{color},stroke:{color},color:{TEXT_DARK},filter:none"
        )
        domain_scenes = [
            sid
            for sid, d in model.scene_domain.items()
            if d == domain_id and sid not in todo_set
        ]
        members = [f"leg_{domain_id}", *domain_scenes]
        out.append(f"    class {','.join(members)} {cls}")

    # TODO override — per-domain: domain-color stroke, 0.3-alpha domain fill.
    todo_by_domain: dict[str, list[str]] = {}
    for sid in todo_ids:
        todo_by_domain.setdefault(model.scene_domain[sid], []).append(sid)
    for domain_id, sids in todo_by_domain.items():
        base_color = DOMAIN_PALETTE[model.domain_order.index(domain_id)]
        cls = f"{domain_id}_todo"
        fill = _hex_with_alpha(base_color, TODO_FILL_ALPHA)
        out.append(
            f"    classDef {cls} fill:{fill},stroke:{base_color},"
            f"stroke-width:{TODO_STROKE_WIDTH},color:{TEXT_DARK},filter:none"
        )
        out.append(f"    class {','.join(sids)} {cls}")

    # Pointer override
    if pointer_ids:
        out.append(
            f"    classDef pointer fill:{POINTER_FILL},stroke:{POINTER_FILL},"
            f"color:{TEXT_DARK},filter:none"
        )
        out.append(f"    class {','.join(pointer_ids)} pointer")

    # Wrappers
    if mutex_wrappers:
        out.append(
            "    classDef mutex fill:#ffffff,stroke:#999,stroke-dasharray:10 5,filter:none"
        )
        out.append(f"    class {','.join(mutex_wrappers)} mutex")
    if composite_wrappers:
        out.append(
            "    classDef composite fill:#f0f0f0,stroke:#f0f0f0,stroke-width:0px,filter:none"
        )
        out.append(f"    class {','.join(composite_wrappers)} composite")

    # Domain legend container
    if model.domain_order:
        out.append(
            "    classDef legendBox fill:#F5F5F5,stroke:#B5B5B5,color:#231f20,filter:none"
        )
        out.append("    class domain_legend legendBox")

    # Implements callouts inherit their attached scene's domain class.
    for domain_id, impl_ids in impl_by_domain.items():
        cls = _domain_class_name(domain_id)
        out.append(f"    class {','.join(impl_ids)} {cls}")

    # Notes
    if note_ids:
        out.append(
            "    classDef note fill:#fff7d6,stroke:#d4c171,color:#231f20,filter:none"
        )
        out.append(f"    class {','.join(note_ids)} note")

    # Modal-style callouts — styled to match the mutex wrapper they describe
    # (white fill, dashed gray border) since they annotate the wrapper, not a
    # single scene.
    if mstyle_callout_ids:
        out.append(
            "    classDef modalStyle fill:#ffffff,stroke:#999,"
            "stroke-dasharray:10 5,color:#231f20,filter:none"
        )
        out.append(f"    class {','.join(mstyle_callout_ids)} modalStyle")

    # Smaller font for secondary nodes (implements callouts, note stickies,
    # modal-style callouts, legend entries). Applied as a second class so it
    # composes with the fill classes above.
    all_impl_ids = [iid for ids in impl_by_domain.values() for iid in ids]
    legend_ids = [f"leg_{d}" for d in model.domain_order]
    small_font_ids = all_impl_ids + note_ids + mstyle_callout_ids + legend_ids
    if small_font_ids:
        out.append(f"    classDef smallFont font-size:{SMALL_FONT_SIZE}")
        out.append(f"    class {','.join(small_font_ids)} smallFont")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# SVG rendering
# ---------------------------------------------------------------------------

# Chrome/Chromium locations probed when PUPPETEER_EXECUTABLE_PATH is unset, so
# mmdc's Puppeteer can reuse an installed browser instead of downloading its
# own (~150MB) chrome-headless-shell.
_CHROME_CANDIDATES: tuple[str, ...] = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
)


def _ensure_puppeteer_browser() -> None:
    """Point Puppeteer at an installed Chrome when PUPPETEER_EXECUTABLE_PATH is
    unset and a known browser is present. A no-op otherwise."""
    if os.environ.get("PUPPETEER_EXECUTABLE_PATH"):
        return
    for candidate in _CHROME_CANDIDATES:
        if os.access(candidate, os.X_OK):
            os.environ["PUPPETEER_EXECUTABLE_PATH"] = candidate
            return


def render_svg(mermaid: str, svg_path: Path) -> None:
    """Render Mermaid text to an SVG via the Mermaid CLI (`mmdc`).

    Raises RuntimeError if `mmdc` is not installed or the render fails.
    """
    if shutil.which("mmdc") is None:
        raise RuntimeError(
            "mmdc (Mermaid CLI) not found on PATH. Install it with "
            "`brew install mermaid-cli` or "
            "`npm install -g @mermaid-js/mermaid-cli`."
        )
    _ensure_puppeteer_browser()
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".mmd", delete=False, encoding="utf-8"
    )
    try:
        tmp.write(mermaid)
        tmp.close()
        subprocess.run(
            ["mmdc", "-i", tmp.name, "-o", str(svg_path), "-b", "white", "-q"],
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"mmdc exited with status {exc.returncode}") from exc
    finally:
        Path(tmp.name).unlink(missing_ok=True)


def open_in_browser(path: Path) -> None:
    """Open a file in a browser.

    macOS forces a browser explicitly: Preview cannot display SVG, Launch
    Services may map .svg to a non-browser app, and .html may be mapped to an
    editor. Defaults to Safari; override
    with the UI_MAP_BROWSER env var. Other platforms use the OS default opener.
    """
    if sys.platform == "darwin":
        browser = os.environ.get("UI_MAP_BROWSER", "Safari")
        subprocess.run(["open", "-a", browser, str(path)], check=False)
    elif sys.platform.startswith("linux"):
        subprocess.run(["xdg-open", str(path)], check=False)
    elif sys.platform == "win32":
        os.startfile(str(path))  # type: ignore[attr-defined]
    else:
        print(f"Cannot open a browser on platform '{sys.platform}'.", file=sys.stderr)


# ---------------------------------------------------------------------------
# HTML output — the interactive viewer (docstring rule 12)
# ---------------------------------------------------------------------------

VIEWER_ASSETS: tuple[str, ...] = ("skai-pages.v1.css", "ui-map-viewer.v2.css", "skai-pages.v1.js", "ui-map-viewer.v2.js")  # the shared page library, then the viewer's own; a version bumps only when a change would break pages already rendered; old versions stay beside this script
REVIEW_ASSET = "spec-review.v2.css"  # a change package's page also takes the review pages' cards for its Review tab, after the library and before the viewer's own
MAP_FILE = "proposed-ui-map.yaml"
ARTIFACT_FILE = "ui-map-architecture.md"


def package_id(input_path: Path) -> str:
    """The title's package ID: for a map in a `ui-map/` folder of a change package, the change id,
    then each change request ID down from it, joined by ' | ' (`offers/changes/CR-01/ui-map/` gives
    'offers | CR-01'); anything else, the production map included, is 'Production'."""
    folder = package_folder(input_path)
    if folder.name != "ui-map" or folder.parent.name == "skai":
        return "Production"
    pkg, ids = st.locate(folder)
    return " | ".join([pkg.parent.name] + ids)


def package_folder(input_path: Path) -> Path:
    """The folder the input names: itself when it is a folder, else the folder holding the file."""
    path = input_path.resolve()
    return path if path.is_dir() else path.parent


def map_source(input_path: Path) -> Path:
    """The YAML to render. A file that exists is itself. A UI Map package folder, or its missing
    `proposed-ui-map.yaml`, takes the nearest proposed map up its request chain (its own, then
    each package spec-tool.py's chain_bases walks), else the production map, `skai/ui-map/ui-map.yaml`,
    as a request's drafts layer over its bases', nearest winning."""
    if input_path.is_file():
        return input_path
    folder = package_folder(input_path)
    for pkg in [folder] + st.chain_bases(folder):
        if (pkg / MAP_FILE).is_file():
            return pkg / MAP_FILE
    own = st.locate(folder)[0]  # skai/changes/<change-id>/ui-map
    return own.parent.parent.parent / "ui-map" / "ui-map.yaml"


# ---------------------------------------------------------------------------
# Map Changes: a change package's Review tab, change badges and side panel entries
# ---------------------------------------------------------------------------

MAP_CHANGE_RE = re.compile(r"^- (?P<cid>M\d+) (?P<op>add|remove|move|modify) (?P<obj>domain|scene|route|scene-attribute): (?P<identity>`.+`|[^`\s].*?)\s*$", re.M)
MAP_CHANGE_LINE_RE = re.compile(r"^- M\d+\b.*$", re.M)
MAP_STATUS = {"add": "added", "modify": "modified", "remove": "removed", "move": "moved"}
SOURCE_RE = re.compile(r";\s*(?:Upstream requirement|Supervisor input|Resolved decision|Agent proposal|Guide convention|"
                       r"Project convention|Map|Migration mapping|Change request)(?::.*)?\Z", re.S)  # a reason's trailing source


PENDING_LINE = "Pending re-derivation."


def map_changes_pending(text: str) -> bool:
    """Whether `## Map Changes` is an inherited list a reopen marked pending (its first line is
    `Pending re-derivation.`): shown, but not current, so never checked against the map."""
    body = re.search(r"^## Map Changes\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return bool(body) and body.group(1).strip().startswith(PENDING_LINE)


def parse_map_changes(text: str) -> list[dict[str, Any]]:
    """The `## Map Changes` entries in artifact order, as design-tool.py parses Design Changes
    ({cid, op, obj, identity, description, justification, section, subs, gaps}, `section` the
    `### <domain>` heading). A line that starts like an entry but is not one is an error, unless
    the list is pending re-derivation."""
    body = re.search(r"^## Map Changes\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    for line in MAP_CHANGE_LINE_RE.findall(body.group(1) if body and not map_changes_pending(text) else ""):
        if not MAP_CHANGE_RE.match(line):
            raise SemanticError(f"Map Changes entry '{line}' is not '- M<n> <operation> <element>: <identity>' "
                                "(operation add, remove, move or modify; element domain, scene, route or scene-attribute)")
    changes = dt.parse_changes(text, "Map Changes", MAP_CHANGE_RE)
    for c in changes:  # an identity in backticks may hold any character the map's IDs can
        if c["identity"].startswith("`"):
            c["identity"] = c["identity"][1:-1]
    return changes


def check_map_changes(changes: list[dict[str, Any]], model: Model) -> None:
    """Every entry names a scene or domain on the proposed map, except one it removes."""
    for c in changes:
        if c["op"] == "remove" and c["obj"] in ("scene", "domain"):
            continue
        known = model.domain_order if c["obj"] == "domain" else model.scenes
        if c["identity"] not in known:
            raise SemanticError(f"Map Changes {c['cid']} ({c['op']} {c['obj']}) names {c['obj'] if c['obj'] == 'domain' else 'scene'} "
                                f"'{c['identity']}', which is not on the proposed map")


def changed_scene(c: dict[str, Any]) -> str | None:
    """The scene an entry marks on the map: a scene, route or attribute entry's identity, except a
    removed scene's; none for a domain's own change."""
    return None if c["obj"] == "domain" or (c["op"] == "remove" and c["obj"] == "scene") else c["identity"]


def build_review(artifact: Path, model: Model, html_path: Path) -> dict[str, Any]:
    """The Review tab and the change marks for a change package's page, from its architecture
    artifact: the summary box, the Discussion and the Map Changes cards as HTML; the counts its
    filters show; the changed scenes in map order; and each changed scene's side panel cards."""
    text = artifact.read_text(encoding="utf-8")
    out_dir = html_path.resolve().parent
    linkdefs = {m.group("name"): m.group("target") for m in map(st.LINKDEF_RE.match, text.splitlines()) if m}
    gloss: dict[str, Any] = {}
    st.RESOLVER["out_dir"] = out_dir
    st.set_resolver(linkdefs, artifact.resolve())
    links = dt.Links(artifact.resolve().parent, out_dir)
    disc = st.parse_discussion(text)
    changes = parse_map_changes(text)
    pending = map_changes_pending(text)
    if not pending:
        check_map_changes(changes, model)
    owners = st.gap_owners(artifact, disc)
    if "base" in owners:  # a base's items are read on its map page's Review tab
        base_page = owners["base"][3].with_name(MAP_FILE).with_suffix(".html")
        owners["base"] = (os.path.relpath(base_page, out_dir).replace(os.sep, "/"),) + tuple(owners["base"][1:])
    st.RESOLVER["gap_owners"] = owners
    body, states = dt.summary(text, artifact, disc, sum(1 for c in changes if c["gaps"]), gloss, links)
    rendered = lambda s: links.show(st.inline(links.hide(s), gloss, auto=True))
    domains = {d: i for i, d in enumerate(model.domain_order)}
    cards, last, panel = [], None, {}
    for c in changes:
        if c["section"] != last:
            did = c["section"].strip().lower().replace(" ", "_")
            square = f'<i class="dm" style="--c:{DOMAIN_PALETTE[domains[did]]}"></i>' if did in domains else ""
            cards.append(f'<h3 class="section">{square}{html_escape(humanize(did) if did in domains else c["section"])}</h3>' if c["section"] else "")
            last = c["section"]
        sid = changed_scene(c) if c["identity"] in model.scenes else None  # a pending list may name scenes the map no longer has
        label = html_escape(humanize(c["identity"]))
        ident = (f'<a class="scene" href="#scene={c["identity"]}" data-scene="{c["identity"]}">{label}</a>' if sid
                 else f'<span class="gone">{label}</span>' if c["op"] == "remove" else label)
        cards.append(dt.render_change({**c, "obj": c["obj"].replace("-", " ")}, gloss, links, owners, ident))
        if sid:
            panel.setdefault(sid, []).append(panel_change(c, rendered, gloss, owners))
    if changes:
        note = f'<p class="file-why">{PENDING_LINE} This list is from an earlier pass and may not match the map.</p>' if pending else ""
        body += '<section class="file"><h2>Map Changes</h2>' + note + "".join(cards) + "</section>"
    counts = {status: sum(MAP_STATUS[c["op"]] == status for c in changes) for status in MAP_STATUS.values()}
    return {
        "html": body + st.render_popovers(gloss),
        "counts": {**counts, **states},
        "changed": [sid for sid in model.scenes if sid in panel],
        "changes": panel,
    }


def panel_change(c: dict[str, Any], rendered: Any, gloss: dict[str, Any], owners: dict[str, Any]) -> str:
    """One entry as the side panel's card: its marker, its ID linking to the entry in the Review
    tab and its type; then what changes and why, or the numbered changes with their reasons; then
    its gap footnotes. Reasons drop their source, which the Review tab keeps."""
    cid = c["cid"].lower()
    st.RESOLVER["item"] = cid  # a [^n] mark links to the footnote in the Review tab
    reason = lambda s: (lambda r: r + "." if r and r[-1] not in ".!?" else r)(SOURCE_RE.sub("", s).strip())
    body = f"<p>{rendered(c['description'])}</p>" if c["description"] else ""
    if c["subs"]:
        body += "<ul>" + "".join(f'<li><span class="rid">{num}</span>{rendered(text)}'
                                 + (f' <span class="why">— {rendered(reason(why))}</span>' if reason(why) else "") + "</li>"
                                 for num, text, why in c["subs"]) + "</ul>"
    if reason(c["justification"]):
        body += f'<p class="reason">{rendered(reason(c["justification"]))}</p>'
    notes = st.gap_notes(((label, dt.owner_ref(owner, owners), placeholder) for label, owner, placeholder in c["gaps"]), f"p{cid}", gloss)
    return (f'<div class="item pchange {MAP_STATUS[c["op"]]}"><div class="head"><span class="badge"></span>'
            f'<a class="id" href="#{cid}">{c["cid"]}</a><span class="status pill">{html_escape(c["op"])} {html_escape(c["obj"].replace("-", " "))}</span></div>'
            f"{body}{notes}</div>")


def build_viewer_model(model: Model, package: str = "Production", review: dict[str, Any] | None = None) -> dict[str, Any]:
    """The JSON model the viewer renders, derived from the resolved Model; a change package's
    page adds its Review tab and change marks (build_review)."""
    domains = [
        {"id": d, "label": humanize(d), "color": DOMAIN_PALETTE[i]}
        for i, d in enumerate(model.domain_order)
    ]
    scenes: dict[str, dict[str, Any]] = {}
    for sid, body in model.scenes.items():
        parent, kind = model.visual_parent[sid]
        routes = [
            {"kind": k, "targets": [_scene_id_and_body(item)[0] for item in body[k]]}
            for k in body
            if k in ROUTE_KINDS and body[k]
        ]
        notes: list[dict[str, Any]] = []
        if body.get("note"):
            notes.append({"at": None, "text": body["note"]})
        for n in body.get("notes", []) or []:
            if isinstance(n, str):
                notes.append({"at": None, "text": n})
            else:
                notes.append({"at": n.get("at"), "text": n.get("text", "")})
        scenes[sid] = {
            "id": sid,
            "label": humanize(sid),
            "domain": model.scene_domain[sid],
            "parent": parent,
            "parentKind": kind,
            "routes": routes,
            "implements": body.get("implements", []) or [],
            "modalStyle": body.get("modal_style"),
            "notes": notes,
            "todo": bool(body.get("todo")),
            "reachedFrom": [{"source": p, "kind": k} for p, k in model.inbound[sid]],
        }
    return {
        "app": model.app,
        "package": package,
        "version": model.version,
        "modalStyles": model.modal_styles,
        "domains": domains,
        "scenes": scenes,
        "order": list(model.scenes.keys()),
        "roots": [sid for sid, (p, _) in model.visual_parent.items() if p is None],
        "review": review,
    }


def render_html(model: Model, html_path: Path, package: str = "Production", review: dict[str, Any] | None = None) -> str:
    """The viewer page: model inline, the shared library and viewer assets linked relative to html_path."""
    asset_dir = Path(__file__).resolve().parent
    rel = os.path.relpath(os.path.abspath(asset_dir), os.path.abspath(html_path.parent)).replace(os.sep, "/")
    names = VIEWER_ASSETS if review is None else (VIEWER_ASSETS[0], REVIEW_ASSET) + VIEWER_ASSETS[1:]
    urls = [(name, html.escape(quote(f"{rel}/{name}", safe="/"))) for name in names]
    css = "\n".join(f'<link rel="stylesheet" href="{u}">' for n, u in urls if n.endswith(".css"))
    js = "\n".join(f'<script src="{u}"></script>' for n, u in urls if n.endswith(".js"))
    payload = json.dumps(build_viewer_model(model, package, review)).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html_escape(model.app)} UI Map</title>
{css}
</head>
<body>
<div id="app"></div>
<script>window.UI_MAP = {payload};</script>
{js}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render a UI Map YAML document as an interactive HTML page or a Mermaid flowchart."
    )
    parser.add_argument("input", type=Path, help="Path to a UI Map YAML file.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Write the Mermaid text to this file (default: stdout).",
    )
    parser.add_argument(
        "--markdown",
        action="store_true",
        help="Wrap the Mermaid text in ```mermaid fences.",
    )
    parser.add_argument(
        "--html",
        type=Path,
        help="Render the interactive HTML page to this path (loads the viewer beside this script).",
    )
    parser.add_argument(
        "--svg",
        type=Path,
        help="Also render an SVG to this path (requires the mmdc CLI).",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the rendered page in a browser (requires --html or --svg; HTML wins).",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=None,
        help="Path to ui-map.schema.json (default: alongside this script).",
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip JSON Schema validation.",
    )
    args = parser.parse_args(argv)

    if args.open and not (args.html or args.svg):
        parser.error("--open requires --html or --svg")

    source = map_source(args.input)
    if not source.is_file():
        print(f"No UI Map to render: {source}", file=sys.stderr)
        return 2
    data = load_yaml(source)

    if not args.no_validate:
        schema_path = args.schema or (Path(__file__).parent / "ui-map.schema.json")
        try:
            validate_schema(data, schema_path)
        except jsonschema.ValidationError as exc:
            print(f"Schema validation failed: {exc.message}", file=sys.stderr)
            return 2

    # A change package's page carries its Review tab, read from the architecture artifact beside the
    # input (a request's own, whichever package's map it shows); its Map Changes are checked either way.
    package = package_id(args.input)
    artifact = package_folder(args.input) / ARTIFACT_FILE
    try:
        model = build_model(data)
        mermaid = render(model)
        review = build_review(artifact, model, args.html or artifact.with_name("proposed-ui-map.html")) \
            if package != "Production" and artifact.is_file() else None
    except SemanticError as exc:
        print(f"UI Map error: {exc}", file=sys.stderr)
        return 3

    text_output = f"```mermaid\n{mermaid}\n```\n" if args.markdown else mermaid

    generated: list[Path] = []
    if args.html:
        args.html.write_text(render_html(model, args.html, package, review), encoding="utf-8")
        generated.append(args.html)

    if args.output:
        args.output.write_text(text_output + "\n")
        generated.append(args.output)

    if args.svg:
        try:
            render_svg(mermaid, args.svg)
        except RuntimeError as exc:
            print(f"SVG render failed: {exc}", file=sys.stderr)
            return 4
        generated.append(args.svg)

    if not args.output and not args.svg and not args.html:
        print(text_output)

    if generated:
        print(f"Generated: {', '.join(p.name for p in generated)}", file=sys.stderr)

    if args.open:
        open_in_browser(args.html or args.svg)

    return 0


if __name__ == "__main__":
    sys.exit(main())
