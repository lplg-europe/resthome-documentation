/* Country menu of the header — the documentation is multi-country.
 *
 * The country itself is decided in <head> (_ext/countries.py), before the page
 * is drawn: the country of the page when it sits in a country space, else the
 * reader's last choice, else the default. CSS then hides the sidebar sections
 * and the content blocks of the other countries.
 *
 * This script only builds the menu: [flag Belgium ▾] next to the languages.
 * Choosing a country on a common page filters it in place — same page, the
 * sidebar and the country blocks follow. On a page of another country's
 * space, it opens the chosen country's space instead. */
(function () {
  "use strict";

  var KEY = "rh-country";

  function store(code) {
    try { localStorage.setItem(KEY, code); } catch (e) { /* private mode */ }
  }

  function build() {
    var t = document.getElementById("rh-cs");
    var h = document.querySelector(".md-header__inner");
    if (!t || !h || h.querySelector(".rh-countryswitch")) {
      return;
    }
    var root = document.documentElement;
    var pageCountry = t.getAttribute("data-page-country") || "";

    var box = document.createElement("div");
    box.className = "rh-countryswitch";
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "rh-countryswitch__button";
    btn.setAttribute("aria-haspopup", "true");
    btn.setAttribute("aria-expanded", "false");
    btn.title = t.getAttribute("data-menu");
    var menu = document.createElement("div");
    menu.className = "rh-countryswitch__menu";
    menu.setAttribute("role", "menu");
    menu.innerHTML = t.innerHTML;
    box.appendChild(btn);
    box.appendChild(menu);

    function items() {
      return menu.querySelectorAll(".rh-country");
    }

    function show(code) {
      root.setAttribute("data-rh-country", code);
      var cur = menu.querySelector('.rh-country[data-country="' + code + '"]');
      if (!cur) {
        return;
      }
      btn.innerHTML = cur.querySelector(".rh-flag").outerHTML +
        '<span class="rh-countryswitch__name">' + cur.getAttribute("data-name") +
        "</span>" +
        "<svg class='rh-caret' viewBox='0 0 24 24' aria-hidden='true'>" +
        "<path d='M7 10l5 5 5-5z'/></svg>";
      var all = items();
      for (var i = 0; i < all.length; i++) {
        all[i].classList.toggle("is-current", all[i] === cur);
        all[i].setAttribute("aria-current", all[i] === cur ? "true" : "false");
      }
    }

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
      if (!a) {
        return;
      }
      var code = a.getAttribute("data-country");
      store(code);
      // On a page of a country space, another country means another space:
      // let the link open it. On a common page, stay and filter.
      if (pageCountry && pageCountry !== code) {
        return;
      }
      ev.preventDefault();
      show(code);
      open(false);
      btn.focus();
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

    show(root.getAttribute("data-rh-country") || t.getAttribute("data-default"));
    var before = h.querySelector(".lplg-langswitch") || h.querySelector(".md-header__source");
    h.insertBefore(box, before || null);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", build);
  } else {
    build();
  }
})();
