/* The header breadcrumb: [WideCare] › [sector ▾] › [country ▾].
 *
 * WideCare is the ecosystem (the link leads to its portal page). The SECTOR
 * (nursing homes, day care centres, serviced residences, general
 * practitioners…) and the country both filter this one site. Both menus come
 * from <template>s emitted by _ext/countries.py (relative links), with the
 * map page → sectors (#rh-sector-map).
 *
 * Country and sector are decided in <head>, before the page is drawn (see
 * _boot in _ext/countries.py). CSS hides the sidebar sections and the content
 * blocks of the other countries and sectors; this script hides, in the
 * sidebar and in the page (cards, lists of pages), every link to a page that
 * does not concern the sector.
 *
 * Choosing a country on a common page filters it in place. On a page of
 * another country's space, it opens the chosen country's space instead.
 * Choosing a sector filters in place when the page concerns it, else opens
 * the home page, filtered for that sector. */
(function () {
  "use strict";

  var KEY = "rh-country";
  var SKEY = "rh-sector";

  function store(code, key) {
    try { localStorage.setItem(key || KEY, code); } catch (e) { /* private mode */ }
  }

  /* --- Sector filter ------------------------------------------------------ */
  var smap = {};
  try {
    var el = document.getElementById("rh-sector-map");
    if (el) { smap = JSON.parse(el.textContent); }
  } catch (e) { smap = {}; }

  function rootUrl() {
    var t = document.getElementById("rh-sector");
    return new URL((t && t.getAttribute("data-root")) || "./", location.href).href;
  }

  /* The page a link points to, as a docname ("soins/registres", "index"), or
     null for a link outside the site. */
  function docOf(a, root) {
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "#" || /^(mailto|tel):/.test(href)) { return null; }
    var u;
    try { u = new URL(href, location.href); } catch (e) { return null; }
    var abs = u.origin + u.pathname;
    if (abs.indexOf(root) !== 0) { return null; }
    var path = abs.slice(root.length).replace(/index\.html$/, "").replace(/\/$/, "");
    if (path === "") { return "index"; }
    if (smap[path]) { return path; }
    if (smap[path + "/index"]) { return path + "/index"; }
    return null;
  }

  function concerns(doc, sector) {
    var s = doc && smap[doc];
    return !s || s.indexOf(sector) >= 0;
  }

  function hide(node, yes) {
    if (node) { node.classList.toggle("rh-sector-off", yes); }
  }

  function filterSector(sector) {
    var root = rootUrl();
    // Sidebar (and the tabs of the theme): one item per page.
    var links = document.querySelectorAll(
      ".md-sidebar--primary a.md-nav__link, .md-tabs a.md-tabs__link");
    for (var i = 0; i < links.length; i++) {
      var item = links[i].closest(".md-nav__item, .md-tabs__item");
      hide(item, !concerns(docOf(links[i], root), sector));
    }
    // A section whose pages are all hidden disappears too.
    var sections = document.querySelectorAll(".md-sidebar--primary .md-nav__item--nested");
    for (var j = sections.length - 1; j >= 0; j--) {
      var kids = sections[j].querySelectorAll(":scope > nav > ul > .md-nav__item");
      if (!kids.length) { continue; }
      var any = false;
      for (var k = 0; k < kids.length; k++) {
        if (!kids[k].classList.contains("rh-sector-off")) { any = true; break; }
      }
      var own = sections[j].querySelector(":scope > a.md-nav__link, :scope > .md-nav__container > a");
      if (!any && !(own && concerns(docOf(own, root), sector))) { hide(sections[j], true); }
    }
    // In the page: cards and lists of pages (toctrees) of other sectors.
    var cards = document.querySelectorAll(".md-content .sd-card");
    for (var c = 0; c < cards.length; c++) {
      var a = cards[c].querySelector("a.sd-stretched-link");
      if (!a) { continue; }
      hide(cards[c].closest(".sd-col") || cards[c], !concerns(docOf(a, root), sector));
    }
    var toc = document.querySelectorAll(".md-content .toctree-wrapper li");
    for (var t = 0; t < toc.length; t++) {
      var ta = toc[t].querySelector(":scope > a");
      if (ta) { hide(toc[t], !concerns(docOf(ta, root), sector)); }
    }
    // Lists of links in the text: an item whose page links all lead to other
    // sectors goes; a section (h2) left with nothing visible goes with it.
    var article = document.querySelector(".md-content article") || document.querySelector(".md-content");
    if (article) {
      var lis = article.querySelectorAll("li");
      for (var l = 0; l < lis.length; l++) {
        if (lis[l].closest(".toctree-wrapper, .sd-card")) { continue; }
        var docs = [], links = lis[l].querySelectorAll("a[href]");
        for (var x = 0; x < links.length; x++) {
          var d = docOf(links[x], root);
          if (d) { docs.push(d); }
        }
        if (!docs.length) { continue; }
        var keep = false;
        for (var y = 0; y < docs.length; y++) { if (concerns(docs[y], sector)) { keep = true; break; } }
        hide(lis[l], !keep);
      }
      var heads = article.querySelectorAll("h2");
      for (var hh = 0; hh < heads.length; hh++) {
        var body = [], n = heads[hh].nextElementSibling;
        while (n && n.tagName !== "H2" && !(n.tagName === "SECTION")) { body.push(n); n = n.nextElementSibling; }
        var sec = heads[hh].closest("section");
        if (sec && sec.firstElementChild === heads[hh]) {
          body = Array.prototype.slice.call(sec.children, 1);
        }
        var lists = body.filter(function (e) { return e.tagName === "UL" || e.tagName === "OL"; });
        if (!lists.length || lists.length !== body.length) { continue; }
        var empty = lists.every(function (ul) {
          return !ul.querySelector(":scope > li:not(.rh-sector-off)");
        });
        hide(sec && sec.firstElementChild === heads[hh] ? sec : heads[hh], empty);
      }
    }
    document.documentElement.classList.remove("rh-nav-pending");
  }

  var CARET = "<svg class='rh-caret' viewBox='0 0 24 24' aria-hidden='true'>" +
              "<path d='M7 10l5 5 5-5z'/></svg>";

  /* A dropdown: button + menu of the template's links. `onPick(link, event)`
     may call event.preventDefault() to stay on the page. */
  function dropdown(cls, template, label, onPick) {
    var box = document.createElement("div");
    box.className = "rh-switch " + cls;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "rh-switch__button";
    btn.setAttribute("aria-haspopup", "true");
    btn.setAttribute("aria-expanded", "false");
    btn.title = template.getAttribute("data-menu") || "";
    var menu = document.createElement("div");
    menu.className = "rh-switch__menu";
    menu.setAttribute("role", "menu");
    menu.innerHTML = template.innerHTML;
    box.appendChild(btn);
    box.appendChild(menu);

    function items() { return menu.querySelectorAll(".rh-country"); }
    function open(yes) {
      box.classList.toggle("is-open", yes);
      btn.setAttribute("aria-expanded", yes ? "true" : "false");
      if (yes) {
        var cur = menu.querySelector(".rh-country.is-current") || items()[0];
        if (cur) { cur.focus(); }
      }
    }
    btn.addEventListener("click", function (ev) {
      ev.stopPropagation();
      open(!box.classList.contains("is-open"));
    });
    menu.addEventListener("click", function (ev) {
      var a = ev.target.closest(".rh-country");
      if (!a) { return; }
      onPick(a, ev);
      if (ev.defaultPrevented) { open(false); btn.focus(); }
    });
    menu.addEventListener("keydown", function (ev) {
      var all = Array.prototype.slice.call(items());
      var i = all.indexOf(document.activeElement);
      if (ev.key === "ArrowDown") { ev.preventDefault(); all[(i + 1) % all.length].focus(); }
      if (ev.key === "ArrowUp") { ev.preventDefault(); all[(i - 1 + all.length) % all.length].focus(); }
      if (ev.key === "Escape") { open(false); btn.focus(); }
    });
    document.addEventListener("click", function (ev) {
      if (!box.contains(ev.target)) { open(false); }
    });
    btn.innerHTML = label + CARET;
    return { box: box, btn: btn, menu: menu, items: items };
  }

  function build() {
    var h = document.querySelector(".md-header__inner");
    var ct = document.getElementById("rh-cs");
    var st = document.getElementById("rh-sector");
    if (!h || h.querySelector(".rh-switch")) { return; }
    // The portal is above sectors and countries: no menu there.
    if (st && st.getAttribute("data-is-portal")) { return; }
    var title = h.querySelector(".md-header__title");
    var anchor = title ? title.nextSibling : null;
    var parent = title ? title.parentNode : h;

    if (st) {
      var root = document.documentElement;
      var here = document.getElementById("rh-sector-map") ? docOf(
        { getAttribute: function () { return location.href; } }, rootUrl()) : null;
      var sector = dropdown("rh-suiteswitch", st, "", function (a, ev) {
        var code = a.getAttribute("data-sector");
        if (!code) { return; }              // a sector coming soon: open the portal
        store(code, SKEY);
        if (!concerns(here, code)) { return; }  // not this page's sector: open the home
        ev.preventDefault();
        showSector(code);
      });
      var showSector = function (code) {
        root.setAttribute("data-rh-sector", code);
        var cur = sector.menu.querySelector('.rh-country[data-sector="' + code + '"]');
        if (cur) {
          var name = cur.getAttribute("data-name");
          sector.btn.innerHTML = (name ? "<span class='rh-suite'>" + name + "</span>" : "") +
            "<span class='rh-suite-label'>" + cur.getAttribute("data-label") + "</span>" + CARET;
        }
        var all = sector.items();
        for (var i = 0; i < all.length; i++) {
          all[i].classList.toggle("is-current", all[i] === cur);
          all[i].setAttribute("aria-current", all[i] === cur ? "true" : "false");
        }
        filterSector(code);
      };
      showSector(root.getAttribute("data-rh-sector") || "mr");
      parent.insertBefore(sector.box, anchor);
    }

    if (ct) {
      var root = document.documentElement;
      var pageCountry = ct.getAttribute("data-page-country") || "";
      var country = dropdown("rh-countryswitch", ct, "", function (a, ev) {
        var code = a.getAttribute("data-country");
        store(code);
        // On a page of a country space, another country means another space:
        // let the link open it. On a common page, stay and filter.
        if (pageCountry && pageCountry !== code) { return; }
        ev.preventDefault();
        show(code);
      });
      var show = function (code) {
        root.setAttribute("data-rh-country", code);
        var cur = country.menu.querySelector('.rh-country[data-country="' + code + '"]');
        if (!cur) { return; }
        country.btn.innerHTML = cur.querySelector(".rh-flag").outerHTML +
          "<span class='rh-switch__name'>" + cur.getAttribute("data-name") + "</span>" + CARET;
        var all = country.items();
        for (var i = 0; i < all.length; i++) {
          all[i].classList.toggle("is-current", all[i] === cur);
          all[i].setAttribute("aria-current", all[i] === cur ? "true" : "false");
        }
      };
      show(root.getAttribute("data-rh-country") || ct.getAttribute("data-default"));
      parent.insertBefore(country.box, anchor);
    }
  }

  /* The portal's sector cards: remember the sector, then open the home. */
  document.addEventListener("click", function (ev) {
    var card = ev.target.closest && ev.target.closest("[data-pick-sector]");
    if (card) { store(card.getAttribute("data-pick-sector"), SKEY); }
  });

  function start() {
    build();
    // A page with no sector menu (the portal) still drops the pending state.
    if (document.documentElement.classList.contains("rh-nav-pending")) {
      filterSector(document.documentElement.getAttribute("data-rh-sector") || "mr");
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
