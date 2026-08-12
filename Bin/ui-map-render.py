#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml",
#   "jsonschema",
# ]
# ///
"""
ui-map-render.py — render a UI Map YAML document as a Mermaid flowchart.

The input is a UI Map YAML document conforming to ui-map.schema.json.
The output is a Mermaid `flowchart TD` block (bare, no ``` fences).

Usage:
    uv run ui-map-render.py <input.yaml>                     # write Mermaid to stdout
    uv run ui-map-render.py <input.yaml> -o <output.mmd>     # write Mermaid to a file
    uv run ui-map-render.py <input.yaml> --markdown          # wrap in ```mermaid fences
    uv run ui-map-render.py <input.yaml> --svg <output.svg>  # also render an SVG
    uv run ui-map-render.py <input.yaml> --svg <o.svg> --open   # render SVG, then open it
    uv run ui-map-render.py <input.yaml> --no-validate       # skip JSON Schema validation

The Mermaid-text outputs (-o / --markdown / stdout) and the --svg output are
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
   - A `---`-delimited front matter sets Mermaid config: padding 12,
     nodeSpacing 30, rankSpacing 40, subGraphTitleMargin top/bottom 0.
   - The diagram is `flowchart TD`.
   - The first block is a Domain Legend subgraph (one labeled node per
     domain, colored to match the scenes in that domain).
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
   - The Domain Legend subgraph at the top of the diagram contains one node
     per domain, named `leg_<domain_id>`, classed with that domain's color.

4. CANONICAL POSITION (which wrapper holds the rounded-rect instance)
   The script chooses each scene's visual home by these rules, in order:
     a. `primary_parent: X` set → canonical instance renders inside X's wrapper
        that routes to this scene. The route kind is the unique kind connecting
        X to this scene; if X routes to this scene via multiple kinds, the
        first declared kind wins.
     b. Exactly one inbound reference → that single parent's wrapper.
     c. Zero inbound references → root scene: declared at top level, no
        enclosing wrapper.
     d. Multiple inbound references with no `primary_parent` → semantic error.

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
     wrapper: `<T>_at_<S>` with the same label as the canonical `T`, classed
     `pointer` (gray fill — overrides T's domain color).
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

12. ERRORS
    - Schema validation runs first (unless --no-validate); failures abort.
    - Semantic validation runs next; failures abort with a specific message.
      Categories: duplicate canonical home, undefined scene reference,
      ambiguous visual home (multiple inbound, no primary_parent),
      `primary_parent` that doesn't actually route to the scene,
      too many domains for the palette, missing modal_style or vocabulary,
      modal_style outside the vocabulary.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import jsonschema
import yaml

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
    for kind in ROUTE_KINDS:
        for sub_item in body.get(kind, []) or []:
            _walk_item(sub_item, scene_id, kind, domain_id, scenes, edges, scene_domain)


def build_model(data: dict[str, Any]) -> Model:
    scenes: dict[str, dict[str, Any]] = {}
    edges: list[tuple[str, str, str]] = []
    scene_domain: dict[str, str | None] = {}
    domain_order: list[str] = []

    for domain_id, domain_data in data["domains"].items():
        domain_order.append(domain_id)
        if "scenes" in domain_data:
            for item in domain_data["scenes"]:
                _walk_item(item, None, None, domain_id, scenes, edges, scene_domain)
        else:
            _walk_item(
                {domain_id: domain_data}, None, None, domain_id, scenes, edges, scene_domain
            )

    common_items = data.get("common", []) or []
    for item in common_items:
        _walk_item(item, None, None, COMMON_DOMAIN_ID, scenes, edges, scene_domain)
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
        "flowchart TD",
    ])

    # Domain legend (one node per domain, colored to match its scenes)
    if model.domain_order:
        out.append("    %% Domains")
        out.append('    subgraph domain_legend[" "]')
        out.append("        direction LR")
        for domain_id in model.domain_order:
            out.append(f'        leg_{domain_id}(["{humanize(domain_id)}"])')
        # The legend nodes have no edges, so `direction LR` has nothing to flow.
        # Chain them with invisible edges to force a horizontal row.
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
    # invisible edge forces it onto the top rank, above the root scene.
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
                    pid = f"{target_id}_at_{sid}"
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

    macOS forces a browser explicitly: Preview cannot display SVG, and Launch
    Services may map .svg to a non-browser app. Defaults to Safari; override
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
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render a UI Map YAML document as a Mermaid flowchart."
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
        "--svg",
        type=Path,
        help="Also render an SVG to this path (requires the mmdc CLI).",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the rendered SVG in a browser (requires --svg).",
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

    if args.open and not args.svg:
        parser.error("--open requires --svg")

    data = load_yaml(args.input)

    if not args.no_validate:
        schema_path = args.schema or (Path(__file__).parent / "ui-map.schema.json")
        try:
            validate_schema(data, schema_path)
        except jsonschema.ValidationError as exc:
            print(f"Schema validation failed: {exc.message}", file=sys.stderr)
            return 2

    try:
        model = build_model(data)
        mermaid = render(model)
    except SemanticError as exc:
        print(f"UI Map error: {exc}", file=sys.stderr)
        return 3

    text_output = f"```mermaid\n{mermaid}\n```\n" if args.markdown else mermaid

    generated: list[Path] = []
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

    if not args.output and not args.svg:
        print(text_output)

    if generated:
        print(f"Generated: {', '.join(p.name for p in generated)}", file=sys.stderr)

    if args.open:
        open_in_browser(args.svg)

    return 0


if __name__ == "__main__":
    sys.exit(main())
