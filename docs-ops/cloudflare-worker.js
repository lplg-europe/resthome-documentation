// Worker Cloudflare — sert la doc sous www.lplg.eu/resthome/documentation/*
// (et ses variantes /nl/, /en/ préfixées par la langue) tout en laissant la
// plateforme principale gérer le reste du domaine.
//
// Routes à créer dans Cloudflare (une par préfixe de langue) :
//   www.lplg.eu/resthome/documentation*
//   www.lplg.eu/nl/resthome/documentation*
//   www.lplg.eu/en/resthome/documentation*
// Origine doc : docs.lplg.eu (GitHub Pages, déjà en place). La doc n'a que 2
// locales : fr (racine, défaut) et nl (/nl/) — "en" n'existe pas côté doc, on
// retombe sur le français dans ce cas.
// Origine par défaut (passthrough) : la plateforme principale, inchangée — le
// Worker ne s'applique qu'aux routes ci-dessus, tout le reste continue de
// passer par le reverse-proxy Cloudflare normal.

const DOC_PREFIX = "/resthome/documentation";
const DOC_ORIGIN = "https://docs.lplg.eu";
// préfixe de langue (dans l'URL affichée) -> préfixe de locale doc (sur docs.lplg.eu)
const LANG_TO_DOC_LOCALE = { nl: "/nl", en: "" }; // en: pas de locale doc -> repli sur le français
// Fichiers uniques à la racine de docs.lplg.eu, non déclinés par langue
// (ex: llms.txt) — toujours servis depuis la racine quel que soit le préfixe.
const ALWAYS_ROOT_FILES = ["llms.txt", "llms-full.txt"];

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // Détecte un éventuel préfixe de langue (/nl/... ou /en/...) avant
    // le chemin de la doc, et le retire pour la suite du traitement.
    let langPrefix = "";
    let pathname = url.pathname;
    for (const lang of Object.keys(LANG_TO_DOC_LOCALE)) {
      const withLang = `/${lang}${DOC_PREFIX}`;
      if (pathname === withLang || pathname.startsWith(withLang + "/")) {
        langPrefix = `/${lang}`;
        pathname = pathname.slice(langPrefix.length);
        break;
      }
    }

    if (!pathname.startsWith(DOC_PREFIX)) {
      // Ne devrait pas arriver si les routes Cloudflare sont bien scopées,
      // mais on repasse en clair au cas où.
      return fetch(request);
    }

    // Sans slash final, le navigateur résout les chemins relatifs des CSS/JS
    // un niveau trop haut. On force le slash sur les pages (pas sur
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
      : LANG_TO_DOC_LOCALE[langPrefix.slice(1)] || "";
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

    // GitHub Pages répond parfois par un 301 interne (trailing slash, i18n) —
    // on le laisse passer tel quel, le navigateur suit sur le même domaine
    // www.lplg.eu grâce au Worker qui interceptera aussi la nouvelle URL.
    const headers = new Headers(originResponse.headers);
    headers.delete("content-security-policy"); // évite un CSP GitHub Pages incompatible avec le site principal

    return new Response(originResponse.body, {
      status: originResponse.status,
      statusText: originResponse.statusText,
      headers,
    });
  },
};
