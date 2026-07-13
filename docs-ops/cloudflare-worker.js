// Worker Cloudflare — sert la doc MkDocs sous www.lplg.eu/resthome/documentation/*
// (et ses variantes /nl/, /en/ préfixées par Odoo i18n) tout en laissant Odoo
// SaaS gérer le reste du domaine.
//
// Routes à créer dans Cloudflare (une par préfixe de langue Odoo) :
//   www.lplg.eu/resthome/documentation*
//   www.lplg.eu/nl/resthome/documentation*
//   www.lplg.eu/en/resthome/documentation*
// Origine doc : docs.lplg.eu (GitHub Pages, déjà en place). MkDocs n'a que 2
// locales : fr (racine, défaut) et nl (/nl/) — "en" n'existe pas côté doc, on
// retombe sur le français dans ce cas.
// Origine par défaut (passthrough) : Odoo SaaS (lplg1.odoo.com), inchangé — le
// Worker ne s'applique qu'aux routes ci-dessus, tout le reste continue de
// passer par le reverse-proxy Cloudflare normal vers Odoo.

const DOC_PREFIX = "/resthome/documentation";
const DOC_ORIGIN = "https://docs.lplg.eu";
// préfixe de langue Odoo (dans l'URL affichée) -> préfixe de locale MkDocs (sur docs.lplg.eu)
const ODOO_LANG_TO_DOC_LOCALE = { nl: "/nl", en: "" }; // en: pas de locale MkDocs -> repli sur le français
// Fichiers uniques à la racine de docs.lplg.eu, non déclinés par langue
// (ex: llms.txt) — toujours servis depuis la racine quel que soit le préfixe.
const ALWAYS_ROOT_FILES = ["llms.txt", "llms-full.txt"];

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // Détecte un éventuel préfixe de langue Odoo (/nl/... ou /en/...) avant
    // le chemin de la doc, et le retire pour la suite du traitement.
    let odooLangPrefix = "";
    let pathname = url.pathname;
    for (const lang of Object.keys(ODOO_LANG_TO_DOC_LOCALE)) {
      const withLang = `/${lang}${DOC_PREFIX}`;
      if (pathname === withLang || pathname.startsWith(withLang + "/")) {
        odooLangPrefix = `/${lang}`;
        pathname = pathname.slice(odooLangPrefix.length);
        break;
      }
    }

    if (!pathname.startsWith(DOC_PREFIX)) {
      // Ne devrait pas arriver si les routes Cloudflare sont bien scopées,
      // mais on repasse en clair au cas où.
      return fetch(request);
    }

    // Sans slash final, le navigateur résout les chemins relatifs des CSS/JS
    // MkDocs un niveau trop haut. On force le slash sur les pages (pas sur
    // les fichiers type assets/*.css, *.js, *.svg, *.json...).
    const lastSegment = pathname.split("/").pop();
    const looksLikeFile = lastSegment.includes(".");
    if (!url.pathname.endsWith("/") && !looksLikeFile) {
      const redirectUrl = new URL(request.url);
      redirectUrl.pathname = url.pathname + "/";
      return Response.redirect(redirectUrl.toString(), 301);
    }

    const remainder = pathname.slice(DOC_PREFIX.length) || "/";
    const remainderFile = remainder.replace(/^\//, "");
    const docLocale = ALWAYS_ROOT_FILES.includes(remainderFile)
      ? ""
      : ODOO_LANG_TO_DOC_LOCALE[odooLangPrefix.slice(1)] || "";
    const originUrl = new URL(DOC_ORIGIN);
    originUrl.pathname = docLocale + remainder;
    originUrl.search = url.search;

    const originRequest = new Request(originUrl.toString(), {
      method: request.method,
      headers: request.headers,
      body: request.method === "GET" || request.method === "HEAD" ? undefined : request.body,
      redirect: "manual",
    });

    const originResponse = await fetch(originRequest);

    // GitHub Pages répond parfois par un 301 interne (trailing slash, i18n
    // MkDocs) — on le laisse passer tel quel, le navigateur suit sur le même
    // domaine www.lplg.eu grâce au Worker qui interceptera aussi la nouvelle URL.
    const headers = new Headers(originResponse.headers);
    headers.delete("content-security-policy"); // évite un CSP GitHub Pages incompatible avec le site Odoo

    return new Response(originResponse.body, {
      status: originResponse.status,
      statusText: originResponse.statusText,
      headers,
    });
  },
};
