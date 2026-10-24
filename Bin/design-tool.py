#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""design-tool.py — render a design package's authoring artifact as a review page.

A design package has no drafts to diff: its drawings live in the design file. The page shows
what the spec page shows — the package card, the Discussion, and the changes, here the typed
Design Changes list under its per-screen headings, each frame a card with its description, its
link into the design file and its justification, or its numbered sub-changes — in the same shell, stylesheet and script as the spec pages, which it imports
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
SUB_RE = re.compile(r"^  - \*\*(?P<num>\d{2})\*\* (?P<text>.+?)\s*$", re.M)
HEADING_RE = re.compile(r"^### (?P<name>.+?)\s*$", re.M)
GAP_DEF_RE = re.compile(r"^[ \t]*\[\^(?P<label>[A-Za-z0-9-]+)\]:[ \t]*\*\*Gap:\*\*[ \t]*(?P<text>.+?)[ \t]*$", re.M)
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
    """The '## Design Changes' entries in artifact order: {cid, op, obj, identity, description,
    justification, section, subs, gaps}; `section` is the `###` heading the entry sits under ("" with
    none), `subs` the numbered sub-changes [(num, text, justification)] of a frame changed in
    several ways (the justification is what follows the last ' — ' of the line), `gaps` the
    footnotes defined under the entry, each (label, owning item, the provisional answer the entry
    builds on); one footnote per entry whose change rests on a gap, the question staying with its owner."""
    body = re.search(r"^## Design Changes\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not body:
        return []
    src = body.group(1)
    heads = list(CHANGE_RE.finditer(src))
    headings = [(m.start(), m.group("name").strip()) for m in HEADING_RE.finditer(src)]
    out = []
    for c, nxt in zip(heads, heads[1:] + [None]):
        block = src[c.end(): nxt.start() if nxt else len(src)]
        block = block[: next((m.start() for m in HEADING_RE.finditer(block)), len(block))]
        gaps = []  # this entry's footnotes: (label, owning item, the the provisional answer this entry builds on)
        for m in GAP_DEF_RE.finditer(block):
            owner, _, placeholder = m.group("text").partition(". Placeholder:")
            gaps.append((m.group("label"), owner.strip().rstrip("."), placeholder.strip()))
        block = GAP_DEF_RE.sub("", block)
        section = next((name for pos, name in reversed(headings) if pos < c.start()), "")
        subs = []
        for m in SUB_RE.finditer(block):
            text_, _, why = m.group("text").rpartition(" — ")
            subs.append((m.group("num"), text_ if why else m.group("text"), why))
        out.append({"cid": c.group("cid"), "op": c.group("op"), "obj": c.group("obj"), "identity": c.group("identity"),
                    "description": st.norm(st.change_field("Description", block)),
                    "justification": st.norm(st.change_field("Justification", block)), "section": section, "subs": subs, "gaps": gaps})
    return out


OWNER_RE = re.compile(r"^(?P<scope>.*?)\s*(?P<did>D\d+)$")


def owner_ref(owner, owners):
    """The owning item named in a footnote (`D15`, `base D15`, `product specs D21`) as the spec tool's chip."""
    m = OWNER_RE.match(owner)
    return st.gap_owner_chip(m.group("scope").strip().lower(), m.group("did"), owners) if m else html.escape(owner)


def render_change(ch, gloss, links, owners):
    """One change as a card: the badge says add, modify or remove; the summary carries the ID,
    the object and the identity, linked into the design file; the description and the
    justification follow."""
    status = STATUS[ch["op"]]
    cid = ch["cid"].lower()
    st.RESOLVER["item"] = cid  # the spec renderer's inline() turns a [^n] mark into a link to #gap-<item>-<n>
    ident = links.show(st.inline(links.hide(ch["identity"]), gloss, auto=True))
    summary = (f'<span class="badge">{status}</span><span class="id">{ch["cid"]}</span>'
               f'<span class="status">{html.escape(ch["op"])} {html.escape(ch["obj"])}</span><span class="title">{ident}</span>')
    body = f"<p>{links.show(st.inline(links.hide(ch['description']), gloss, auto=True))}</p>" if ch["description"] else ""
    if ch["subs"]:
        body += "<ul>" + "".join(
            f'<li><span class="rid">{num}</span>{links.show(st.inline(links.hide(text), gloss, auto=True))}'
            + (f' <span class="why">— {links.show(st.inline(links.hide(why), gloss, auto=True))}</span>' if why else "") + "</li>"
            for num, text, why in ch["subs"]) + "</ul>"
    why = f'<div class="why"><b>Why</b> {links.show(st.inline(links.hide(ch["justification"]), gloss, auto=True))}</div>' if ch["justification"] else ""
    notes = st.gap_notes(((label, owner_ref(owner, owners), placeholder) for label, owner, placeholder in ch["gaps"]), cid, gloss)
    gap = " has-gap" if ch["gaps"] else ""
    return f'<details class="item request {status}{gap}" id="{cid}" open><summary>{summary}</summary>{body}{why}{notes}</details>'


def page_shell(title, counts, body, gloss, out, subtitle="", tips=""):
    css, js = st.asset_links(out)
    sub = f'<div class="sub">{html.escape(subtitle)}</div>' if subtitle else ""
    change = "".join(f'<button type="button" data-f="{f}" aria-pressed="false"><span class="badge {b}"></span><b>{counts[k]}</b> {k}</button>'
                     for f, b, k in (("added", "added", "added"), ("modified", "modified", "modified"), ("removed", "retired", "removed")))
    state = st.state_tiles(counts)
    return f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><link rel="stylesheet" href="{css}"></head><body>
<div class="top"><div class="titles"><h1>{html.escape(title).replace(" | ", '<span class="sep">|</span>')}</h1>{sub}</div><div class="seg change" role="group" aria-label="Change">{change}</div>{state}</div><div class="wrap">
{body}
{st.render_popovers(gloss)}{tips}
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
    name = title.split(" — ")[-1].strip()  # the artifact's name: the last dash-separated part of its heading
    linkdefs = {m.group("name"): m.group("target") for m in map(st.LINKDEF_RE.match, text.splitlines()) if m}
    specs = [Path(s) for s in specs]
    gloss = st.prepare(specs[0], specs[1:], None, out) if specs else {}
    st.RESOLVER["out_dir"] = out.resolve().parent
    st.set_resolver(linkdefs, authoring)
    links = Links(authoring.parent, out.resolve().parent)
    disc = st.parse_discussion(text)
    changes = parse_changes(text)
    owners = st.gap_owners(authoring, disc)
    st.RESOLVER["gap_owners"] = owners
    items = [it for _, its in disc for it in its]
    n_gap_items = sum(1 for it in items if not it["done"] and it["gap"])
    n_open = sum(1 for it in items if not it["done"]) - n_gap_items
    n_gap = n_gap_items + sum(1 for c in changes if c["gaps"])  # open gap items plus footnoted entries
    n_done = len(items) - n_open - n_gap_items
    gaps = f"{n_gap} gap{'s' if n_gap != 1 else ''}"
    if n_open:
        state = f"{n_open} open" + (f", {gaps}" if n_gap else "")
    elif items:
        state = f"discussion complete; {gaps} carried" if n_gap else "discussion complete"
    else:  # inherited gaps show even with no Discussion item
        state = f"no discussion items; {gaps} carried" if n_gap else "no discussion items"
    goal = section(text, "Goal")
    head = (f'<div class="item request"><div class="head"><span class="status">{html.escape(state)}</span></div>'
            + (f"<p>{links.show(st.inline(links.hide(goal), gloss, auto=True))}</p>" if goal else "") + "</div>")
    body = head
    if disc:
        body += '<section class="discussion"><h2>Discussion</h2>' + "".join(
            (f'<h3 class="section">{html.escape(topic)}</h3>' if topic else "") + "".join(st.render_discussion_item(it, gloss) for it in its)
            for topic, its in disc) + "</section>"
    if changes:
        cards, last = [], None
        for c in changes:
            if c["section"] != last:
                cards.append(f'<h3 class="section">{html.escape(c["section"])}</h3>' if c["section"] else "")
                last = c["section"]
            cards.append(render_change(c, gloss, links, owners))
        body += '<section class="file"><h2>Design Changes</h2>' + "".join(cards) + "</section>"
    counts = {"added": sum(c["op"] == "add" for c in changes), "modified": sum(c["op"] == "modify" for c in changes),
              "removed": sum(c["op"] == "remove" for c in changes), "open": n_open, "gaps": n_gap, "resolved": n_done}
    out.write_text(page_shell(short_title(authoring.parent), counts, body, gloss, out, subtitle=name, tips=""), encoding="utf-8")
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
