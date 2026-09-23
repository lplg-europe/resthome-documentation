/* The header breadcrumb: [WideCare] › [suite ▾] › [country ▾].
 *
 * WideCare is the ecosystem (the link leads to its portal page); each suite
 * serves one trade and has its own site; the country filters this site. Both
 * menus come from <template>s emitted by _ext/countries.py (relative links).
 *
 * The country itself is decided in <head>, before the page is drawn: the
 * country of the page when it sits in a country space, else the reader's last
 * choice, else the default. CSS then hides the sidebar sections and the
 * content blocks of the other countries.
 *
 * Choosing a country on a common page filters it in place — same page, the
 * sidebar and the country blocks follow. On a page of another country's
 * space, it opens the chosen country's space instead. Choosing a suite opens
 * its site (or the portal, while the suite has no documentation yet). */
(function () {
  "use strict";

  var KEY = "rh-country";

  function store(code) {
    try { localStorage.setItem(KEY, code); } catch (e) { /* private mode */ }
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
    var st = document.getElementById("rh-suite");
    if (!h || h.querySelector(".rh-switch")) { return; }
    // The portal is above suites and countries: no menu there.
    if (st && st.getAttribute("data-is-portal")) { return; }
    var title = h.querySelector(".md-header__title");
    var anchor = title ? title.nextSibling : null;
    var parent = title ? title.parentNode : h;

    if (st) {
      var label = st.getAttribute("data-label");
      var suite = dropdown("rh-suiteswitch", st,
        "<span class='rh-suite'>" + st.getAttribute("data-name") + "</span>" +
        (label ? "<span class='rh-suite-label'>" + label + "</span>" : ""),
        function () { /* every suite link opens a page */ });
      parent.insertBefore(suite.box, anchor);
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

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", build);
  } else {
    build();
  }
})();
