#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""design-tool.py — render a design package's authoring artifact as a review page.

A design package has no drafts to diff: its drawings live in the design file. The page shows
what the spec page shows — the package card, the Discussion, and the changes, here the typed
Design Changes list, each change a card with its description, its link into the design file and
its justification — in the same shell, stylesheet and script as the spec pages, which it imports
from spec-tool.py beside it. Spec citations in the artifact get the same
chips and popovers as on a spec page; pass the spec roots so glossary terms do too.

Usage:
    python3 design-tool.py render --authoring FILE [--specs ROOT ...] [--out FILE]
        Writes design-review.html beside the artifact unless --out says otherwise. --specs lists
        spec roots (catalog first, then any package drafts layered over it) whose glossaries and
        items feed the popovers; the artifact's own link definitions reach cited items without it.
"""

import argparse
import html
import importlib.util
import os
import re
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location("spec_tool", Path(__file__).with_name("spec-tool.py"))
st = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(st)

CHANGE_RE = re.compile(r"^- (?P<cid>V\d+) (?P<op>add|modify|remove) (?P<obj>[a-z][a-z -]*?): (?P<identity>.+?)\s*$", re.M)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
STATUS = {"add": "added", "modify": "modified", "remove": "retired"}


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return st.LINKDEF_RE.sub("", m.group(1)).strip() if m else ""


class Links:
    """Inline markdown links, which the spec renderer does not know: swapped for placeholders
    before rendering and for anchors after, so the text in between is escaped and linked as
    usual. A relative target is rewritten from the artifact's folder to the page's."""

    def __init__(self, base, out_dir):
        self.urls, self.base, self.out_dir = [], base, out_dir

    def hide(self, text):
        def keep(m):
            self.urls.append((m.group(1), m.group(2)))
            return f"\x00{len(self.urls) - 1}\x00"
        return MD_LINK_RE.sub(keep, text)

    def show(self, rendered):
        return re.sub(r"\x00(\d+)\x00", lambda m: self.anchor(*self.urls[int(m.group(1))]), rendered)

    def anchor(self, label, url):
        if not re.match(r"[a-z]+:|#", url):
            path, frag = url.split("#", 1) if "#" in url else (url, "")
            url = Path(os.path.relpath((self.base / path).resolve(), self.out_dir)).as_posix() + (f"#{frag}" if frag else "")
        return f'<a href="{html.escape(url)}">{html.escape(label)}</a>'


def parse_changes(text):
    """The '## Design Changes' entries: {cid, op, obj, identity, description, justification, line}."""
    body = re.search(r"^## Design Changes\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not body:
        return []
    heads = list(CHANGE_RE.finditer(body.group(1)))
    out = []
    for c, nxt in zip(heads, heads[1:] + [None]):
        block = body.group(1)[c.end(): nxt.start() if nxt else len(body.group(1))]
        out.append({"cid": c.group("cid"), "op": c.group("op"), "obj": c.group("obj"), "identity": c.group("identity"),
                    "description": st.norm(st.change_field("Description", block)),
                    "justification": st.norm(st.change_field("Justification", block))})
    return out


def render_change(ch, gloss, links):
    """One change as a card: the badge says add, modify or remove; the summary carries the ID,
    the object and the identity, linked into the design file; the description and the
    justification follow."""
    status = STATUS[ch["op"]]
    ident = links.show(st.inline(links.hide(ch["identity"]), gloss, auto=True))
    summary = (f'<span class="badge">{status}</span><span class="id">{ch["cid"]}</span>'
               f'<span class="status">{html.escape(ch["op"])} {html.escape(ch["obj"])}</span><span class="title">{ident}</span>')
    body = f"<p>{links.show(st.inline(links.hide(ch['description']), gloss, auto=True))}</p>" if ch["description"] else ""
    why = f'<div class="why"><b>Why</b> {links.show(st.inline(links.hide(ch["justification"]), gloss, auto=True))}</div>' if ch["justification"] else ""
    return f'<details class="item request {status}" id="{ch["cid"].lower()}" open><summary>{summary}</summary>{body}{why}</details>'


def page_shell(title, counts, body, gloss, out, subtitle=""):
    css, js = st.asset_links(out)
    sub = f'<div class="sub">{html.escape(subtitle)}</div>' if subtitle else ""
    change = "".join(f'<button type="button" data-f="{f}" aria-pressed="false"><span class="badge {b}"></span><b>{counts[k]}</b> {k}</button>'
                     for f, b, k in (("added", "added", "added"), ("modified", "modified", "modified"), ("removed", "retired", "removed")))
    state = "".join(f'<button type="button" data-f="{k}" aria-pressed="false"><b>{counts[k]}</b> {k}</button>' for k in ("open", "gaps") if counts.get(k))
    state = f'<div class="seg state" role="group" aria-label="State">{state}</div>' if state else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><link rel="stylesheet" href="{css}"></head><body>
<div class="top"><div class="titles"><h1>{html.escape(title)}</h1>{sub}</div><div class="seg change" role="group" aria-label="Change">{change}</div>{state}</div><div class="wrap">
{body}
{st.render_popovers(gloss)}
<div id="pop"></div></div>
<script src="{js}"></script>
</body></html>"""


def short_title(folder):
    """The top bar's name, '<title>: <path>': the path is the change id, then each change
    request number down from skai/changes/<id>/design/, joined by ' | ' — 'Offers', 'Offers | 001',
    'Offers | 001 | 002'."""
    parts = list(folder.resolve().parts)
    path = []
    while len(parts) >= 2 and parts[-2] == "change-requests":
        path.insert(0, parts[-1])
        parts = parts[:-2]
    if parts and parts[-1] == "design":
        parts = parts[:-1]
    path.insert(0, parts[-1].replace("-", " ").title() if parts else folder.name)
    return "Design Change: " + " | ".join(path)


def render(authoring, specs, out):
    authoring = Path(authoring).resolve()
    out = Path(out) if out else authoring.parent / "design-review.html"
    text = authoring.read_text(encoding="utf-8")
    tm = re.search(r"^# (.+)$", text, re.M)
    title = tm.group(1).strip() if tm else ""
    name = re.sub(r"^Design\s+—\s+.*?Change Request \d+\s+—\s+|^Design\s+—\s+", "", title)  # the artifact's name without its lead
    linkdefs = {m.group("name"): m.group("target") for m in map(st.LINKDEF_RE.match, text.splitlines()) if m}
    specs = [Path(s) for s in specs]
    gloss = st.prepare(specs[0], specs[1:], None, out) if specs else {}
    st.RESOLVER["out_dir"] = out.resolve().parent
    st.set_resolver(linkdefs, authoring)
    links = Links(authoring.parent, out.resolve().parent)
    disc = st.parse_discussion(text)
    changes = parse_changes(text)
    items = [it for _, its in disc for it in its]
    n_gap = sum(1 for it in items if not it["done"] and it["gap"])
    n_open = sum(1 for it in items if not it["done"]) - n_gap
    n_done = len(items) - n_open - n_gap
    gaps = f"{n_gap} gap{'s' if n_gap != 1 else ''}"
    state = ((f"discussion complete; {gaps} carried" if n_gap else "discussion complete") if items and not n_open
             else (f"{n_open} open" + (f", {gaps}" if n_gap else "") if n_open else "no discussion items"))
    foot = f"Discussion: {n_done} approved, {n_open} open, {gaps}" if items else "No discussion items"
    goal = section(text, "Goal")
    head = (f'<div class="item request"><div class="head"><span class="status">{html.escape(state)}</span></div>'
            + (f"<p>{links.show(st.inline(links.hide(goal), gloss, auto=True))}</p>" if goal else "")
            + f'<div class="why"><b>{foot}</b></div></div>')
    body = head
    if disc:
        body += '<section class="discussion"><h2>Discussion</h2>' + "".join(
            (f'<h3 class="section">{html.escape(topic)}</h3>' if topic else "") + "".join(st.render_discussion_item(it, gloss) for it in its)
            for topic, its in disc) + "</section>"
    if changes:
        body += '<section class="file"><h2>Design Changes</h2>' + "".join(render_change(c, gloss, links) for c in changes) + "</section>"
    counts = {"added": sum(c["op"] == "add" for c in changes), "modified": sum(c["op"] == "modify" for c in changes),
              "removed": sum(c["op"] == "remove" for c in changes), "open": n_open + n_gap, "gaps": n_gap}
    out.write_text(page_shell(short_title(authoring.parent), counts, body, gloss, out, subtitle=name), encoding="utf-8")
    print(f"wrote {out}: {counts}")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("render"); r.add_argument("--authoring", required=True)
    r.add_argument("--specs", action="append", default=[], help="a spec root for popovers (repeatable: catalog first, then drafts layered over it)")
    r.add_argument("--out")
    a = ap.parse_args(argv)
    if a.cmd == "render":
        render(a.authoring, a.specs, a.out)
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
