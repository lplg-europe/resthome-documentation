/* Keeps the navigation column where the reader expects to find it.
 *
 * The column is a scrollable div of its own, and Chrome restores the scroll
 * offset of such a div when you come back to a page. Leaving a deep page for
 * the home page — which has no entry in the tree — therefore left the column
 * opened in the middle of another group, far from its first item.
 *
 * Rule applied here: no page of the tree is current => back to the top;
 * a page is current but out of sight => bring it into view, moving the column
 * alone (never the document, which `scrollIntoView` would also scroll). */
(function () {
  "use strict";

  var WRAP = ".md-sidebar--primary .md-sidebar__scrollwrap";

  function place() {
    var wrap = document.querySelector(WRAP);
    if (!wrap || wrap.scrollHeight <= wrap.clientHeight) {
      return;
    }
    /* The theme marks several copies of the current page: the one in the tree,
       and the one it inserts to host the page summary. Only the drawn one has
       a box — the others would give an empty rectangle. */
    var current = null;
    var marked = wrap.querySelectorAll(".md-nav__link--active");
    for (var i = 0; i < marked.length; i++) {
      if (marked[i].getBoundingClientRect().height > 0) {
        current = marked[i];
        break;
      }
    }
    if (!current) {
      wrap.scrollTop = 0;
      return;
    }
    var link = current.getBoundingClientRect();
    var frame = wrap.getBoundingClientRect();
    if (link.top >= frame.top && link.bottom <= frame.bottom) {
      return;
    }
    wrap.scrollTop += link.top - frame.top - (frame.height - link.height) / 2;
  }

  /* Twice: once as soon as the tree exists, once after the browser has had
     its say — the restored offset is applied after `load`. */
  function schedule() {
    place();
    requestAnimationFrame(place);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", schedule);
  } else {
    schedule();
  }
  window.addEventListener("load", schedule);
  window.addEventListener("pageshow", schedule);
})();
