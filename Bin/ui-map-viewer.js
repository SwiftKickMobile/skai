// ui-map-viewer.js — the interactive UI Map viewer that `ui-map-render.py --html` pages load.
// Vanilla JS, no dependencies. Reads the map model from window.UI_MAP (emitted by the renderer;
// see "HTML OUTPUT" in ui-map-render.py's docstring for the model and the viewer's behaviour).
// Layout: levels as rows (depth in the primary-parent tree), fixed width, vertical scroll.
// Each scene's route boxes sit in the row below it; reused scenes appear as placeholders.
// Selecting a scene (or domains) filters the map to the connected neighbourhood and collapses
// empty rows; "All" keeps the whole map and dims instead.
(function () {
  "use strict";
  const M = window.UI_MAP;
  const S = M.scenes;
  const $ = (s, r) => (r || document).querySelector(s);
  const el = (tag, attrs, ...kids) => {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (k === "class") n.className = v;
      else if (k === "style") n.style.cssText = v;
      else if (k.startsWith("on")) n.addEventListener(k.slice(2), v);
      else if (v !== null && v !== undefined) n.setAttribute(k, v);
    }
    for (const k of kids.flat()) if (k !== null && k !== undefined) n.append(k.nodeType ? k : document.createTextNode(String(k)));
    return n;
  };
  const svgEl = html => { const t = document.createElement("template"); t.innerHTML = html.trim(); return t.content.firstChild; };
  const domainColor = Object.fromEntries(M.domains.map(d => [d.id, d.color]));
  const domainLabel = Object.fromEntries(M.domains.map(d => [d.id, d.label]));
  const KIND = { nav: "Nav", modal: "Modal", composite: "Composite", tab: "Tab", child: "Child" };
  // Scene-box icons: existence only; the panel spells the content out.
  const ICONS = {
    note: '<path d="M3 2.5h7l3 3V13.5H3z"/><path d="M10 2.5v3h3M5.5 8h5M5.5 10.5h5"/>',
    implements: '<path d="M8 2.5 14 5.5 8 8.5 2 5.5z"/><path d="M2 8.5l6 3 6-3M2 11.5l6 3 6-3"/>',
    modal: '<rect x="2" y="4.5" width="12" height="9" rx="1.5"/><path d="M5 2.5h6"/>',
    reuse: '<path d="M4 12 12 4M6.5 4H12v5.5"/>',
  };
  const icon = (name, title) => svgEl(`<svg class="ic" width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"><title>${title}</title>${ICONS[name]}</svg>`);
  const calloutIcons = sc => [
    sc.notes.length ? icon("note", sc.notes.length === 1 ? "1 note" : `${sc.notes.length} notes`) : null,
    sc.implements.length ? icon("implements", `implements ${sc.implements.join(", ")}`) : null,
    sc.modalStyle ? icon("modal", `modal style: ${sc.modalStyle}`) : null,
  ].filter(Boolean);

  // hops: 1 | 2 | "all" — how far from the selection (or the chosen domains) the filter reaches.
  // anchor: the clicked cell's key and screen position; after a reflow the canvas scrolls or pads so it stays put.
  // pad: extra space kept around the graph so the anchor can hold even when the graph is smaller than the viewport.
  const state = { selected: null, domains: new Set(), query: "", hops: 1, anchor: null, pad: { top: 0, left: 0, bottom: 0, right: 0 }, help: false };

  // ---- theme ----
  try { const t = localStorage.getItem("um-theme"); if (t) document.documentElement.dataset.theme = t; } catch (e) {}
  function toggleTheme() {
    const cur = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("um-theme", next); } catch (e) {}
  }

  // ---- facts ----
  const depth = sid => S[sid].parent ? depth(S[sid].parent) + 1 : 0;
  const isCanonical = (t, source, kind) => S[t].parent === source && S[t].parentKind === kind;
  const key = (t, source, kind) => isCanonical(t, source, kind) ? t : `${t}@${source}.${kind}`;
  const itemKey = (it, box) => it.canonical ? it.id : `${it.id}@${box.source}.${box.kind}`;
  const noteAt = (s, kind) => s.notes.filter(n => n.at === kind);
  const generalNotes = s => s.notes.filter(n => !n.at);
  const appearances = sid => S[sid].reachedFrom.map(r => ({ ...r, canonical: isCanonical(sid, r.source, r.kind) }));
  const neighbours = sid => [...new Set([...S[sid].reachedFrom.map(r => r.source), ...S[sid].routes.flatMap(r => r.targets)])];

  // Scenes shown under the current filter; null = everything.
  function visibleScenes() {
    const seeds = state.selected ? [state.selected] : state.domains.size ? M.order.filter(s => state.domains.has(S[s].domain)) : null;
    if (!seeds || state.hops === "all") return null;
    const V = new Set(seeds); let frontier = seeds;
    for (let h = 0; h < state.hops; h++) {
      const next = [];
      for (const s of frontier) for (const n of neighbours(s)) if (!V.has(n)) { V.add(n); next.push(n); }
      frontier = next;
    }
    return V;
  }

  // Rows of boxes. Row 0 holds the roots; a box is one scene's destinations for one route kind.
  function fullRows() {
    const out = [[{ source: null, kind: null, items: M.roots.map(id => ({ id, canonical: true })) }]];
    for (let L = 0; ; L++) {
      const next = [];
      for (const box of out[L]) for (const it of box.items) {
        if (!it.canonical) continue;
        for (const r of S[it.id].routes) next.push({ source: it.id, kind: r.kind, items: r.targets.map(t => ({ id: t, canonical: isCanonical(t, it.id, r.kind) })) });
      }
      if (!next.length) return out;
      out.push(next);
    }
  }
  // The rows after filtering: boxes keep only visible items; a visible scene whose box went away
  // stands alone ("bare") at its depth; empty rows collapse.
  function rows() {
    const full = fullRows(); const V = visibleScenes();
    if (!V) return full;
    const out = full.map(row => row.flatMap(box => {
      if (box.source && !V.has(box.source)) return [];
      const items = box.items.filter(it => V.has(it.id));
      return items.length ? [{ ...box, items }] : [];
    }));
    const shown = new Set(out.flat().flatMap(b => b.items.filter(i => i.canonical).map(i => i.id)));
    for (const sid of V) if (!shown.has(sid)) out[depth(sid)].push({ source: null, kind: null, bare: true, items: [{ id: sid, canonical: true }] });
    return out.filter(r => r.length);
  }

  // ---- layout ----
  const IW = 156;   // cells never shrink; rows wrap instead
  const IH = 64, IGAP = 8, BPAD = 8, BGAP = 18, ROWGAP = 44, BH = IH + 2 * BPAD;
  const boxW = box => box.items.length * IW + (box.items.length - 1) * IGAP + 2 * BPAD;
  function layout(width) {
    const R = rows();
    const pos = {}, boxes = [];
    let y = 0;
    for (const row of R) {
      // Place boxes in groups (one source scene's boxes) so a wrap never splits a scene's boxes.
      const groups = [];
      for (const box of row) { const g = groups[groups.length - 1]; if (g && !box.bare && !g[0].bare && g[0].source === box.source) g.push(box); else groups.push([box]); }
      let x = 0, placed = 0;
      for (const g of groups) {
        const gw = g.reduce((a, b) => a + boxW(b), 0) + (g.length - 1) * BGAP;
        let gx = x;
        if (gx + gw > width && placed) { y += BH + ROWGAP; x = 0; placed = 0; gx = 0; }
        let bx = gx;
        for (const box of g) {
          const w = boxW(box);
          boxes.push({ box, x: bx, y, w, h: BH });
          box.items.forEach((it, i) => { pos[itemKey(it, box)] = { x: bx + BPAD + i * (IW + IGAP), y: y + BPAD }; });
          bx += w + BGAP;
        }
        x = gx + gw + BGAP; placed++;
      }
      y += BH + ROWGAP;
    }
    return { pos, boxes, w: width, h: y - ROWGAP + 8, rows: R.length };
  }

  // ---- selection ----
  function select(id, scrollTo) {
    state.selected = id; state.domains.clear(); state.pad = { top: 0, left: 0, bottom: 0, right: 0 };
    render();
    if (scrollTo && id) flash(id, !state.anchorApplied);
  }
  // Keep the cell the user clicked at the same screen position after a reflow: scroll when the canvas
  // allows it, otherwise pad the graph so it can.
  function holdAnchor(wrap, dag) {
    const a = state.anchor; state.anchor = null; state.anchorApplied = false;
    if (!a) return;
    const n = dag.querySelector(`[data-key="${CSS.escape(a.key)}"]`); if (!n) return;
    const r = n.getBoundingClientRect();
    let st = wrap.scrollTop + (r.top - a.top), sl = wrap.scrollLeft + (r.left - a.left);
    if (st < 0) { state.pad.top = -st; st = 0; }
    if (sl < 0) { state.pad.left = -sl; sl = 0; }
    dag.style.marginTop = `${state.pad.top}px`; dag.style.marginLeft = `${state.pad.left}px`;
    const needH = st - (wrap.scrollHeight - wrap.clientHeight), needW = sl - (wrap.scrollWidth - wrap.clientWidth);
    if (needH > 0) { state.pad.bottom = needH; dag.style.marginBottom = `${needH}px`; }
    if (needW > 0) { state.pad.right = needW; dag.style.marginRight = `${needW}px`; }
    wrap.scrollTop = st; wrap.scrollLeft = sl;
    state.anchorApplied = true;
  }
  function flash(k, scroll = true) {
    const n = document.querySelector(`[data-key="${CSS.escape(k)}"]`);
    if (!n) return;
    if (scroll) n.scrollIntoView({ block: "center", inline: "center", behavior: "smooth" });
    n.classList.remove("flash"); void n.offsetWidth; n.classList.add("flash");
  }
  // What a selection lights: item keys and route edges (source.kind).
  function lit() {
    const sid = state.selected; if (!sid) return null;
    const keys = new Set([sid]), edges = new Set();
    for (const r of S[sid].routes) { edges.add(`${sid}.${r.kind}`); for (const t of r.targets) keys.add(key(t, sid, r.kind)); }
    for (const a of appearances(sid)) { keys.add(key(sid, a.source, a.kind)); keys.add(a.source); edges.add(`${a.source}.${a.kind}`); }
    return { keys, edges };
  }

  // ---- render ----
  function render() {
    const app = $("#app"); app.innerHTML = "";
    app.className = "app" + (state.selected ? " with-panel" : "");
    app.append(renderTop());
    const main = el("div", { class: "main" });
    const wrap = el("div", { class: "canvasw" });
    main.append(wrap, renderPanel());
    app.append(main);
    if (state.help) app.append(renderHelp());
    const draw = () => {
      const keepTop = wrap.scrollTop, keepLeft = wrap.scrollLeft;
      wrap.innerHTML = "";
      const { pos, boxes, w, h } = layout(wrap.clientWidth - 56);
      const L = lit();
      const q = state.query.trim().toLowerCase();
      const matches = q ? new Set(M.order.filter(s => S[s].label.toLowerCase().includes(q) || s.includes(q))) : null;
      const filtered = !!visibleScenes();
      const focus = !filtered && !!(L || state.domains.size || matches);   // a filtered view shows only connected elements, so nothing is dimmed
      const dag = el("div", { class: "dag" + (focus ? " focus" : ""), style: `width:${w}px;height:${h}px;--bw:${IW}px` });
      const paths = [], labels = [];
      for (const b of boxes) {
        const box = b.box;
        const edge = box.source ? `${box.source}.${box.kind}` : null;
        const litBox = L ? box.items.some(it => L.keys.has(itemKey(it, box)) && (L.edges.has(edge) || it.id === state.selected)) : false;
        const inDomain = state.domains.size && box.items.some(it => state.domains.has(S[it.id].domain));
        const matched = matches && box.items.some(it => matches.has(it.id));
        // A route box is "on" when its connector is: it belongs to the selected scene, or holds it.
        const on = !!(L && edge && L.edges.has(edge) && (box.source === state.selected || box.items.some(it => it.id === state.selected)));
        dag.append(el("div", { class: `box ${box.bare ? "bare" : box.kind || "root"}` + (litBox || inDomain || matched ? " near" : "") + (on ? " on" : ""), style: `left:${b.x}px;top:${b.y}px;width:${b.w}px;height:${b.h}px` }));
        if (box.source) {
          const s = pos[box.source]; const sx = s.x + IW / 2, sy = s.y + IH, ex = b.x + b.w / 2, ey = b.y, mid = (sy + ey) / 2;
          paths.push(`<path class="e ${box.kind}${on ? " on" : ""}" d="M${sx} ${sy} C${sx} ${mid} ${ex} ${mid} ${ex} ${ey}"/>`);
          labels.push(el("span", { class: "st" + (on ? " on" : ""), style: `left:${ex}px;top:${ey - 12}px` }, KIND[box.kind], noteAt(S[box.source], box.kind).length ? icon("note", "note on this route") : null));
        }
        for (const it of box.items) {
          const k = itemKey(it, box); const sc = S[it.id]; const p = pos[k];
          let cls = "nb" + (it.canonical ? "" : " ph") + (sc.todo ? " todo" : "");
          if (L) { if (it.canonical && it.id === state.selected) cls += " sel"; else if (L.keys.has(k)) cls += " near"; }
          if (state.domains.has(sc.domain)) cls += " near";
          if (matches && matches.has(it.id)) cls += " match";
          dag.append(el("button", { class: cls, "data-key": k, style: `left:${p.x}px;top:${p.y}px`,
            title: it.canonical ? sc.id : `${sc.id} · reused here; canonical under ${sc.parent}`,
            onclick: e => { const r = e.currentTarget.getBoundingClientRect(); state.anchor = { key: k, top: r.top, left: r.left };
              select(it.canonical && it.id === state.selected ? null : it.id, !it.canonical); } },   // clicking the selected cell again clears
            el("div", { class: "nbtop" }, el("i", { class: "dm", style: `--c:${domainColor[sc.domain]}`, title: domainLabel[sc.domain] }),
              el("span", { class: "icons" }, ...(it.canonical ? calloutIcons(sc) : [icon("reuse", "reused scene; click to go to its home")]))),
            el("div", { class: "nmw" }, el("div", { class: "nm" }, sc.label))));
        }
      }
      dag.prepend(svgEl(`<svg class="edges" width="${w}" height="${h}" aria-hidden="true">${paths.join("")}</svg>`));
      labels.forEach(l => dag.append(l));
      dag.style.margin = `${state.pad.top}px ${state.pad.right}px ${state.pad.bottom}px ${state.pad.left}px`;
      wrap.append(dag);
      wrap.scrollTop = keepTop; wrap.scrollLeft = keepLeft;
      holdAnchor(wrap, dag);
    };
    draw();
    let lastW = wrap.clientWidth;
    new ResizeObserver(() => { if (wrap.clientWidth !== lastW) { lastW = wrap.clientWidth; draw(); } }).observe(wrap);
  }

  function renderTop() {
    const filtering = state.selected || state.domains.size;
    return el("div", { class: "top" },
      el("div", { class: "brand" }, M.app, " ", el("b", {}, "UI Map")),
      el("div", { class: "legend" }, ...M.domains.map(d => el("button", { class: state.domains.has(d.id) ? "on" : "",
        onclick: () => { state.selected = null; state.domains.has(d.id) ? state.domains.delete(d.id) : state.domains.add(d.id); render(); } },
        el("i", { class: "dm", style: `--c:${d.color}` }), d.label))),
      filtering ? el("div", { class: "hops", role: "tablist" }, ...[[1, "1 hop"], [2, "2 hops"], ["all", "All"]].map(([v, t]) =>
        el("button", { role: "tab", "aria-selected": String(state.hops === v), onclick: () => { state.hops = v; render(); } }, t))) : null,
      el("div", { class: "status" },
        el("input", { type: "search", placeholder: "Find a scene", value: state.query,
          oninput: e => { state.query = e.target.value; render(); const i = $(".status input"); i.focus(); i.setSelectionRange(i.value.length, i.value.length); },
          onkeydown: e => { if (e.key === "Enter") { const q = state.query.trim().toLowerCase(); const hit = M.order.find(s => S[s].label.toLowerCase().includes(q) || s.includes(q)); if (hit) { state.query = ""; select(hit, true); } } } }),
        el("button", { class: "clear", onclick: () => { state.selected = null; state.domains.clear(); state.query = ""; render(); } }, "Clear"),
        el("button", { class: "theme", onclick: toggleTheme }, "Theme"),
        el("button", { class: "info", "aria-label": "How to read this map", title: "How to read this map", onclick: () => { state.help = true; render(); } }, "?")));
  }

  function renderPanel() {
    const panel = el("div", { class: "panel" });
    const s = state.selected && S[state.selected]; if (!s) return panel;
    const apps = appearances(s.id);
    panel.append(el("div", { class: "ph" },
      el("div", { class: "row1" }, el("h2", {}, s.label), el("button", { class: "close", onclick: () => select(null), "aria-label": "Close" }, "×")),
      el("p", { class: "sub" }, el("span", { class: "dom" }, el("i", { class: "dm", style: `--c:${domainColor[s.domain]}` }), `${domainLabel[s.domain]} domain`), "·", el("span", {}, "id ", el("span", { class: "mono" }, s.id)), s.todo ? ["·", "TODO"] : null)));
    const body = el("div", { class: "pbody" });
    const link = (id, kind, where) => el("button", { class: "lk", onclick: () => select(id, true) },
      el("span", { class: "k" }, kind ? KIND[kind] : ""), el("i", { class: "dm", style: `--c:${domainColor[S[id].domain]}` }), el("span", {}, S[id].label), el("span", { class: "where" }, where || ""));
    // Reached from: one row per route into this scene; "home" marks the route under which its canonical cell is drawn.
    body.append(el("div", { class: "pg" }, el("span", { class: "lab" }, `Reached from · ${apps.length}`),
      el("div", { class: "links" }, ...(apps.length ? apps.map(a => link(a.source, a.kind, apps.length > 1 ? (a.canonical ? "home" : "reused") : null)) : [el("span", { class: "empty" }, "root")]))));
    const opens = s.routes.flatMap(r => [
      ...r.targets.map(t => link(t, r.kind, isCanonical(t, s.id, r.kind) ? null : "reused")),
      ...noteAt(s, r.kind).map(n => el("div", { class: "note" }, el("span", { class: "k" }, KIND[r.kind]), n.text))]);
    body.append(el("div", { class: "pg" }, el("span", { class: "lab" }, `Opens · ${s.routes.reduce((a, r) => a + r.targets.length, 0)}`),
      el("div", { class: "links" }, ...(opens.length ? opens : [el("span", { class: "empty" }, "nothing")]))));
    // Callout sections carry the same icons as the scene cell.
    const labIcon = (name, text) => el("span", { class: "lab withicon" }, icon(name, text), text);
    if (s.notes.length) body.append(el("div", { class: "pg" }, labIcon("note", s.notes.length === 1 ? "Note" : "Notes"),
      ...s.notes.map(n => el("div", { class: "note" }, n.at ? el("span", { class: "k" }, KIND[n.at]) : null, n.text))));
    if (s.implements.length) body.append(el("div", { class: "pg" }, labIcon("implements", "Implements"),
      el("div", { class: "chips" }, ...s.implements.map(i => el("span", { class: "chip mono" }, i)))));
    if (s.modalStyle) body.append(el("div", { class: "pg" }, labIcon("modal", "Modal style"), el("span", { class: "chip mono" }, s.modalStyle)));
    body.append(el("div", { class: "pg" }, el("span", { class: "lab" }, "Specs"), el("span", { class: "empty" }, "No sidecar yet.")));
    panel.append(body);
    return panel;
  }

  // ---- help: a legend of the map's vocabulary and the viewer's controls ----
  function renderHelp() {
    const closeHelp = () => { state.help = false; render(); };
    const cell = (label, cls, icons = [], color = "var(--cyan)") => el("span", { class: "nb sample " + cls },
      el("div", { class: "nbtop" }, el("i", { class: "dm", style: `--c:${color}` }), el("span", { class: "icons" }, ...icons)),
      el("div", { class: "nmw" }, el("div", { class: "nm" }, label)));
    const row = (sample, text) => el("div", { class: "lrow" }, el("div", { class: "lsample" }, sample), el("p", {}, text));
    const route = kind => el("span", { class: "lroute" }, el("i", { class: "lline" }), el("span", { class: "st static" }, KIND[kind]), el("i", { class: "lline arrow" }));
    return el("div", { class: "scrim", onclick: e => { if (e.target === e.currentTarget) closeHelp(); } },
      el("div", { class: "help", role: "dialog", "aria-label": "How to read this map" },
        el("div", { class: "ph" }, el("div", { class: "row1" }, el("h2", {}, "How to read this map"), el("button", { class: "close", onclick: closeHelp, "aria-label": "Close" }, "×")),
          el("p", { class: "sub" }, "The UI Map defines every scene in the app and the routes between them. A scene is a view with its own identity; a route is a navigational relationship from one scene to another.")),
        el("div", { class: "pbody" },
          el("div", { class: "pg" }, el("span", { class: "lab" }, "Scenes"),
            row(cell("Scene"), "A scene, drawn in full once, under the scene that is its home. The colour square is its domain; the legend in the top bar lists the domains."),
            row(cell("Scene", "ph", [icon("reuse", "")]), "A reused scene: it is reached from here too, but drawn in full elsewhere. Click it to go to the scene."),
            row(cell("Scene", "todo"), "A TODO scene: part of the map, not yet built."),
            row(el("span", { class: "licons" }, icon("note", "")), "The scene has a note. Select it to read the note in the side panel."),
            row(el("span", { class: "licons" }, icon("implements", "")), "The scene implements several variants (for example one setup scene for every game type); the panel lists them."),
            row(el("span", { class: "licons" }, icon("modal", "")), "The scene opens as a modal and declares its modal style; the panel names it.")),
          el("div", { class: "pg" }, el("span", { class: "lab" }, "Route boxes"),
            row(el("span", { class: "box sample nav" }), "A set of mutually exclusive routes of one kind from one scene: the parent reaches exactly one of the scenes inside at a time."),
            row(el("span", { class: "box sample composite" }), "The parts that make up a composite parent. They are embedded, not routed to.")),
          el("div", { class: "pg" }, el("span", { class: "lab" }, "Route kinds"),
            row(route("nav"), "The parent pushes the child onto a navigation stack."),
            row(route("modal"), "The parent presents the child modally; the child's modal style says how."),
            row(route("tab"), "The child is one of the parent's tabs."),
            row(route("child"), "The parent embeds the child as a subview and routes to it."),
            row(route("composite"), "The parent embeds the child as a subview without any routing."),
            row(el("span", { class: "st static" }, "Nav", icon("note", "")), "A note is attached to this route; the parent's panel shows it.")),
          el("div", { class: "pg" }, el("span", { class: "lab" }, "Using the viewer"),
            el("p", {}, "Click a scene to see only the scenes connected to it; the clicked scene stays where it is and the rest of the map collapses around it. 1 hop shows direct connections, 2 hops one step further, All keeps the whole map and dims what is unconnected. Click the scene again, press Escape, or use Clear to restore the map."),
            el("p", {}, "Click domains in the top bar to filter to those domains and their connections. Type in the search box to highlight scenes; Enter selects the first match.")))));
  }

  document.addEventListener("keydown", e => { if (e.key === "Escape") { if (state.help) { state.help = false; render(); } else select(null); } });
  render();
})();
