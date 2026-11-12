// spec-review.v2.js — what only the spec and design review pages do; loads after skai-pages.v1.js.
// Filters: with none pressed everything shows; with any pressed, the union of the pressed kinds
// (cards by status, added files, Discussion items by state, gap items with the cards carrying a
// gap footnote), and the headings, file sections and Discussion left empty are hidden.
(function () {
  var P = window.SkaiPages;
  function statusOf(el) { return el.classList.contains("added") ? "added" : el.classList.contains("modified") ? "modified" : el.classList.contains("unchanged") ? "unchanged" : "removed"; }
  function isCard(k) { return k.classList.contains("item") || (k.tagName === "P" && k.classList.contains("modified")); }
  function apply(sel, any) {
    function hide(el, h) { el.classList.toggle("hid", any && h); }
    document.querySelectorAll("section.file").forEach(function (sec) {
      var whole = sel.files && sec.dataset.kind === "added";
      var groups = [], cur = { head: null, kids: [], shown: 0 }, total = 0;
      Array.prototype.forEach.call(sec.children, function (k) {
        if (k.tagName === "H2") return;
        if (k.tagName === "H3") { groups.push(cur); cur = { head: k, kids: [], shown: 0 }; } else cur.kids.push(k);
      });
      groups.push(cur);
      groups.forEach(function (g) {
        g.kids.forEach(function (k) {
          if (!isCard(k)) return;
          var show = whole || sel[statusOf(k)] || (sel.gaps && k.classList.contains("has-gap"));
          hide(k, !show); if (show) g.shown++;
        });
        total += g.shown;
      });
      groups.forEach(function (g) {
        var keep = whole || (g.head ? g.shown > 0 : total > 0);
        g.kids.forEach(function (k) { if (!isCard(k)) hide(k, !keep); });
        if (g.head) hide(g.head, !keep);
      });
      hide(sec, !(whole || total > 0));
    });
    document.querySelectorAll("section.discussion details.discussion").forEach(function (d) {
      var g = d.classList.contains("gap"), r = d.classList.contains("resolved");
      hide(d, !((sel.open && !r && !g) || (sel.gaps && g) || (sel.resolved && r)));
    });
    document.querySelectorAll("section.discussion h3.section").forEach(function (h) {
      var n = h.nextElementSibling, vis = 0;
      while (n && n.tagName === "DETAILS") { if (!n.classList.contains("hid")) vis++; n = n.nextElementSibling; }
      hide(h, !vis);
    });
    var disc = document.querySelector("section.discussion");
    if (disc) hide(disc, !disc.querySelector("details.discussion:not(.hid)"));
  }
  P.onFilter(apply);

  // Popovers: the cited item's or glossary entry's template; a cited rule is outlined.
  P.popover(document.getElementById("pop"), function (a, pop) {
    var t = document.getElementById(a.dataset.tip);
    if (!t) return false;
    pop.appendChild(t.content.cloneNode(true));
    if (a.dataset.rule) { var li = pop.querySelector('[data-rid="' + a.textContent.trim() + '"]'); if (li) li.classList.add("hit"); }
  });

  // The filters, open cards and scroll position survive a reload in the same tab.
  var key = "review-state:" + location.pathname, st = null;
  try { st = JSON.parse(sessionStorage.getItem(key) || "null"); } catch (e) {}
  var all = function () { return Array.prototype.slice.call(document.querySelectorAll("details")); };
  function save() {
    try {
      sessionStorage.setItem(key, JSON.stringify({ f: Object.keys(P.selection()),
        o: all().map(function (d, i) { return d.open ? i : -1; }).filter(function (i) { return i >= 0; }), y: window.scrollY }));
    } catch (e) {}
  }
  if (st) {
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";
    (st.f || []).forEach(function (f) { var b = document.querySelector('.seg button[data-f="' + f + '"]'); if (b) b.setAttribute("aria-pressed", "true"); });
    if ((st.f || []).length) { var sel = P.selection(); apply(sel, Object.keys(sel).length > 0); }
    var o = st.o || [];
    all().forEach(function (d, i) { d.open = o.indexOf(i) >= 0; });
    if (!location.hash) window.scrollTo(0, st.y || 0);
  }
  document.addEventListener("click", function () { setTimeout(save, 0); });
  document.addEventListener("toggle", save, true);
  addEventListener("pagehide", save);

  addEventListener("hashchange", P.openTarget);
  P.openTarget();
})();
