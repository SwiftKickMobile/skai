// skai-pages.v1.js — behaviours every page SKAI renders shares (see skai-pages.v1.css).
// Vanilla JS, no dependencies; load it before the page family's own script, which uses window.SkaiPages.
//   Segmented controls: a click on a `.seg` button toggles its aria-pressed (`.seg.single`: the
//     clicked one is pressed, the rest released) and fires a bubbling "seg-change" event on the group.
//   SkaiPages.selection(scope): the pressed buttons' data-f values under scope (default: the page), as an object of 1s.
//   SkaiPages.clear(scope): releases every pressed button under scope, then fires "seg-change" on the document.
//   SkaiPages.onFilter(apply): calls apply(selection, any) after every change (filter application).
//   SkaiPages.popover(pop, fill): the hover and focus popover: resting on an element with data-tip
//     for 400 ms (focus: at once) fills `pop` through fill(anchor, pop) — false keeps it closed — and
//     shows it under the anchor; leaving hides it after 150 ms unless the pointer moves onto it.
//   SkaiPages.openTarget(): brings the URL's #target into view: clears the filters when they hide it,
//     opens every collapsed <details> around it. The page calls it once its own state is restored,
//     and on every hash change.
// Versioned like the page assets (internal/maintain-skai.md).
(function () {
  "use strict";
  var P = window.SkaiPages = {};
  var each = function (sel, scope, fn) { Array.prototype.forEach.call((scope || document).querySelectorAll(sel), fn); };

  // ---- segmented controls and filter application ----
  P.selection = function (scope) {
    var sel = {};
    each('.seg button[aria-pressed="true"]', scope, function (b) { sel[b.dataset.f] = 1; });
    return sel;
  };
  P.clear = function (scope) {
    each('.seg button[aria-pressed="true"]', scope, function (b) { b.setAttribute("aria-pressed", "false"); });
    document.dispatchEvent(new CustomEvent("seg-change", { detail: { group: null } }));
  };
  P.onFilter = function (apply) {
    document.addEventListener("seg-change", function () { var sel = P.selection(); apply(sel, Object.keys(sel).length > 0); });
  };
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".seg button");
    if (!b) return;
    var group = b.closest(".seg");
    if (group.classList.contains("single")) each("button", group, function (x) { x.setAttribute("aria-pressed", String(x === b)); });
    else b.setAttribute("aria-pressed", String(b.getAttribute("aria-pressed") !== "true"));
    group.dispatchEvent(new CustomEvent("seg-change", { bubbles: true, detail: { group: group, button: b } }));
  });

  // ---- popover ----
  P.popover = function (pop, fill) {
    var hideTimer, showTimer;
    var hide = function () { pop.style.display = "none"; };
    function show(a) {
      pop.innerHTML = "";
      if (fill(a, pop) === false) return;
      var r = a.getBoundingClientRect();
      pop.style.display = "block";
      var left = Math.min(r.left + window.scrollX, window.scrollX + document.documentElement.clientWidth - pop.offsetWidth - 16);
      pop.style.top = (r.bottom + window.scrollY + 6) + "px";
      pop.style.left = Math.max(8, left) + "px";
    }
    document.addEventListener("mouseover", function (e) {
      if (pop.contains(e.target)) return;
      var a = e.target.closest("[data-tip]");
      if (a) { clearTimeout(hideTimer); clearTimeout(showTimer); showTimer = setTimeout(function () { show(a); }, 400); }
    });
    document.addEventListener("mouseout", function (e) {
      if (pop.contains(e.target)) return;
      if (e.target.closest("[data-tip]")) { clearTimeout(showTimer); hideTimer = setTimeout(hide, 150); }
    });
    document.addEventListener("focusin", function (e) {
      if (pop.contains(e.target)) return;
      var a = e.target.closest("[data-tip]");
      if (a) { clearTimeout(hideTimer); clearTimeout(showTimer); show(a); }
    });
    document.addEventListener("focusout", function (e) { if (!pop.contains(e.target) && e.target.closest("[data-tip]")) hide(); });
    pop.addEventListener("mouseenter", function () { clearTimeout(hideTimer); });
    pop.addEventListener("mouseleave", hide);
  };

  // ---- hash targets ----
  P.openTarget = function () {
    var el = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!el) return;
    if (el.closest(".hid")) P.clear();
    for (var d = el.closest("details"); d; d = d.parentElement && d.parentElement.closest("details")) d.open = true;
    el.scrollIntoView();
  };
})();
