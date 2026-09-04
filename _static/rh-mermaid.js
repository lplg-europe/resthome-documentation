/* Rendu des diagrammes mermaid — fait ici, pas par le thème.
 *
 * sphinx-immaterial repère les <pre class="mermaid">, retire la classe, crée
 * un conteneur… et le laisse VIDE : son appel de rendu n'aboutit pas avec le
 * bundle mermaid qu'il livre lui-même (reproduit le 04/09/2026 sur toutes les
 * pages à diagramme). Avant cela, `sphinxcontrib.mermaid` chargeait mermaid
 * depuis un CDN et le thème échouait sur « Invalid script » : le diagramme
 * s'affichait en texte brut.
 *
 * On garde donc la main : nos blocs portent la classe `rh-mermaid`, que le
 * thème ignore, et ce script les rend avec le bundle servi depuis `_static`.
 * Aucun CDN : la doc se construit et se lit hors ligne.
 */
(function () {
  "use strict";

  var blocks = document.querySelectorAll(".rh-mermaid pre");
  if (!blocks.length) {
    return;
  }

  // Le chemin du bundle se déduit de CE script : les pages vivent à des
  // profondeurs différentes, un chemin relatif écrit en dur casserait sur la
  // moitié d'entre elles.
  var self = document.querySelector('script[src*="rh-mermaid.js"]');
  var src = self ? self.src.replace(/rh-mermaid\.js.*$/, "mermaid/mermaid.min.js")
                 : "_static/mermaid/mermaid.min.js";

  function isDark() {
    return document.body.getAttribute("data-md-color-scheme") === "slate";
  }

  function render() {
    window.mermaid.initialize({
      startOnLoad: false,
      theme: isDark() ? "dark" : "default",
      flowchart: { useMaxWidth: true },
      securityLevel: "strict",
    });
    blocks.forEach(function (pre, index) {
      var code = pre.textContent;
      window.mermaid
        .render("rh-mermaid-" + index, code)
        .then(function (result) {
          var figure = document.createElement("div");
          figure.className = "rh-mermaid-diagram";
          figure.innerHTML = result.svg;
          var container = pre.closest(".rh-mermaid") || pre;
          container.replaceWith(figure);
        })
        .catch(function (error) {
          // Le bloc source reste affiché : un diagramme illisible vaut mieux
          // qu'un cadre vide, et l'erreur dit laquelle des sources est fautive.
          console.error("mermaid: diagramme non rendu", error);
        });
    });
  }

  var script = document.createElement("script");
  script.src = src;
  script.onload = render;
  script.onerror = function () {
    console.error("mermaid: bundle introuvable —", src);
  };
  document.head.appendChild(script);
})();
