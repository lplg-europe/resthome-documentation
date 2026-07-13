// Worker Cloudflare — sert la doc MkDocs sous www.lplg.eu/resthome/documentation/*
// tout en laissant Odoo SaaS gérer le reste du domaine.
//
// Route à créer dans Cloudflare : www.lplg.eu/resthome/documentation*
// Origine doc : docs.lplg.eu (GitHub Pages, déjà en place)
// Origine par défaut (passthrough) : Odoo SaaS (lplg1.odoo.com), inchangé — le
// Worker ne s'applique qu'à la route ci-dessus, tout le reste continue de
// passer par le reverse-proxy Cloudflare normal vers Odoo.

const DOC_PREFIX = "/resthome/documentation";
const DOC_ORIGIN = "https://docs.lplg.eu";

export default {
  async fetch(request) {
    const url = new URL(request.url);

    if (!url.pathname.startsWith(DOC_PREFIX)) {
      // Ne devrait pas arriver si la route Cloudflare est bien scoped,
      // mais on repasse en clair au cas où.
      return fetch(request);
    }

    // Sans slash final, le navigateur résout les chemins relatifs des CSS/JS
    // MkDocs un niveau trop haut (ex: /resthome/assets/... au lieu de
    // /resthome/documentation/assets/...). On force le slash sur les pages
    // (pas sur les fichiers type assets/*.css, *.js, *.svg, *.json...).
    const lastSegment = url.pathname.split("/").pop();
    const looksLikeFile = lastSegment.includes(".");
    if (!url.pathname.endsWith("/") && !looksLikeFile) {
      const redirectUrl = new URL(request.url);
      redirectUrl.pathname = url.pathname + "/";
      return Response.redirect(redirectUrl.toString(), 301);
    }

    const originUrl = new URL(DOC_ORIGIN);
    originUrl.pathname = url.pathname.slice(DOC_PREFIX.length) || "/";
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
