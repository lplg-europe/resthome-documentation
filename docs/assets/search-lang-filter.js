/*
 * Filtre de recherche par langue.
 * mkdocs-static-i18n construit UN seul index de recherche combiné (FR + NL).
 * Ce script masque, dans les résultats, ceux de l'autre langue que celle de la
 * page courante (déduite de <html lang>). Les URL des pages NL contiennent
 * « /nl/ » ; celles des pages FR ne le contiennent pas.
 */
(function () {
  function pageIsNL() {
    return (document.documentElement.lang || "").toLowerCase().indexOf("nl") === 0;
  }

  function resultIsNL(link) {
    if (!link) return false;
    try {
      return new URL(link.href, location.href).pathname.indexOf("/nl/") !== -1;
    } catch (e) {
      return /(^|\/)nl\//.test(link.getAttribute("href") || "");
    }
  }

  function applyFilter() {
    var wantNL = pageIsNL();
    var items = document.querySelectorAll(".md-search-result__item");
    var visible = 0;
    items.forEach(function (item) {
      var link = item.querySelector("a.md-search-result__link") || item.querySelector("a[href]");
      var keep = resultIsNL(link) === wantNL;
      item.hidden = !keep;
      if (keep) visible++;
    });
    // Recale le compteur « N documents trouvés » sur les résultats visibles.
    var meta = document.querySelector(".md-search-result__meta");
    if (meta && items.length && /\d/.test(meta.textContent)) {
      meta.textContent = meta.textContent.replace(/\d[\d\s .,]*/, String(visible) + " ");
    }
  }

  function init() {
    var output =
      document.querySelector("[data-md-component='search-result']") ||
      document.querySelector(".md-search__output") ||
      document.body;
    var scheduled = false;
    var obs = new MutationObserver(function () {
      if (scheduled) return;
      scheduled = true;
      requestAnimationFrame(function () {
        scheduled = false;
        applyFilter();
      });
    });
    obs.observe(output, { childList: true, subtree: true });
  }

  if (document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
})();
