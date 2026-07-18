# -*- coding: utf-8 -*-
"""resthome_meta — port Sphinx de notre machinerie SEO/AEO MkDocs (overrides/main.html).

Directives (contenu TRADUISIBLE via gettext, invisible dans la page) :
  :::{rh-description}   → <meta name="description"> + JSON-LD
  :::{rh-faq}           → schema.org FAQPage (liste de définitions Q/A)

Émis dans <head> de chaque page :
  - TechArticle + BreadcrumbList (toutes les pages)
  - FAQPage (si rh-faq), HowTo (si front-matter `howto_auto: true`, titres numérotés)
  - SoftwareApplication + Organization (accueil uniquement)
  - hreflang alternates absolus (fr racine / nl / en) + x-default
"""
import json
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective

LANG_TAGS = {"fr": "fr-BE", "nl": "nl-BE", "en": "en"}


class rh_hidden(nodes.General, nodes.Element):
    """Conteneur présent dans le doctree (donc extrait par gettext) mais non rendu."""


def visit_rh_hidden(self, node):
    raise nodes.SkipNode


class RhDescription(SphinxDirective):
    has_content = True

    def run(self):
        node = rh_hidden()
        node["rh_kind"] = "description"
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class RhFaq(SphinxDirective):
    has_content = True

    def run(self):
        node = rh_hidden()
        node["rh_kind"] = "faq"
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# --------------------------------------------------------------------------- #
#  Collecte (doctree résolu = déjà traduit par gettext)
# --------------------------------------------------------------------------- #
def _text(node):
    return " ".join(node.astext().split())


def collect(app, doctree, docname):
    meta = {"description": "", "faq": [], "howto": []}

    for hidden in doctree.findall(rh_hidden):
        if hidden.get("rh_kind") == "description":
            meta["description"] = _text(hidden)
        elif hidden.get("rh_kind") == "faq":
            for dl in hidden.findall(nodes.definition_list):
                for item in dl.findall(nodes.definition_list_item):
                    term = item.next_node(nodes.term)
                    definition = item.next_node(nodes.definition)
                    if term is not None and definition is not None:
                        meta["faq"].append((_text(term), _text(definition)))

    page_meta = app.env.metadata.get(docname, {})
    if page_meta.get("howto_auto"):
        for section in doctree.findall(nodes.section):
            title = section.next_node(nodes.title)
            if title is None:
                continue
            t = _text(title)
            if t and t[0].isdigit():
                anchor = section["ids"][0] if section["ids"] else ""
                meta["howto"].append((t, anchor))

    if not hasattr(app.env, "rh_meta"):
        app.env.rh_meta = {}
    app.env.rh_meta[docname] = meta


def purge(app, env, docname):
    if hasattr(env, "rh_meta"):
        env.rh_meta.pop(docname, None)


def merge(app, env, docnames, other):
    if not hasattr(env, "rh_meta"):
        env.rh_meta = {}
    if hasattr(other, "rh_meta"):
        env.rh_meta.update(other.rh_meta)


# --------------------------------------------------------------------------- #
#  Émission <head>
# --------------------------------------------------------------------------- #
def _page_path(pagename):
    if pagename == "index":
        return ""
    if pagename.endswith("/index"):
        return pagename[:-5]
    return pagename + "/"


def _ld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False) + "</script>")


def html_page_context(app, pagename, templatename, context, doctree):
    if doctree is None:
        return
    cfg = app.config
    lang = app.config.language or "en"
    lang_tag = LANG_TAGS.get(lang, lang)
    base = cfg.rh_site_base
    prefix = cfg.rh_languages.get(lang, "")
    path = _page_path(pagename)
    page_url = base + prefix + path
    meta = getattr(app.env, "rh_meta", {}).get(pagename, {})
    title = context.get("title") or cfg.project
    desc = meta.get("description", "")

    out = []

    # meta description (traduite)
    if desc:
        from html import escape
        out.append(f'<meta name="description" content="{escape(desc, quote=True)}">')

    # hreflang absolus (spec : URL absolue obligatoire) + x-default = langue racine
    for code, pfx in cfg.rh_languages.items():
        out.append(f'<link rel="alternate" href="{base}{pfx}{path}" '
                   f'hreflang="{LANG_TAGS.get(code, code)}">')
    default_pfx = cfg.rh_languages.get(cfg.rh_default_language, "")
    out.append(f'<link rel="alternate" href="{base}{default_pfx}{path}" hreflang="x-default">')

    # TechArticle (chaque page)
    out.append(_ld({
        "@context": "https://schema.org", "@type": "TechArticle",
        "headline": title, "description": desc, "url": page_url,
        "inLanguage": lang_tag,
        "author": {"@type": "Organization", "name": "LPLG", "url": "https://www.lplg.eu/"},
        "isPartOf": {"@type": "WebSite", "name": "Resthome docs", "url": base},
        "about": {"@type": "SoftwareApplication", "name": "Resthome",
                  "applicationCategory": "BusinessApplication",
                  "applicationSubCategory":
                      "Logiciel de gestion pour maisons de repos (MR/MRS)",
                  "operatingSystem": "Web"},
        "publisher": {"@type": "Organization", "name": "LPLG",
                      "url": "https://www.lplg.eu/",
                      "logo": base + "assets/logo.svg"},
    }))

    # BreadcrumbList (Accueil → section → page)
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Accueil",
               "item": base + prefix}]
    if "/" in pagename:
        section = pagename.split("/", 1)[0]
        sec_title_node = app.env.titles.get(f"{section}/index")
        if sec_title_node is not None and pagename != f"{section}/index":
            crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1,
                           "name": _text(sec_title_node),
                           "item": base + prefix + section + "/"})
    if pagename != "index":
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1,
                       "name": title, "item": page_url})
    if len(crumbs) > 1:
        out.append(_ld({"@context": "https://schema.org",
                        "@type": "BreadcrumbList", "itemListElement": crumbs}))

    # FAQPage
    faq = meta.get("faq") or []
    if faq:
        out.append(_ld({
            "@context": "https://schema.org", "@type": "FAQPage",
            "url": page_url, "inLanguage": lang_tag,
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in faq],
        }))

    # HowTo (titres numérotés, howto_auto)
    howto = meta.get("howto") or []
    if howto:
        out.append(_ld({
            "@context": "https://schema.org", "@type": "HowTo",
            "name": title, "description": desc, "inLanguage": lang_tag,
            "step": [{"@type": "HowToStep", "position": i + 1, "name": t,
                      "text": t, "url": f"{page_url}#{anchor}"}
                     for i, (t, anchor) in enumerate(howto)],
        }))

    # Accueil : SoftwareApplication + Organization (entité de marque)
    if pagename == "index":
        out.append(_ld({
            "@context": "https://schema.org", "@type": "SoftwareApplication",
            "name": "Resthome", "alternateName": "Resthome Suite",
            "applicationCategory": "BusinessApplication",
            "applicationSubCategory":
                "Logiciel de gestion pour maisons de repos (MR/MRS) en Belgique",
            "operatingSystem": "Web", "url": "https://www.lplg.eu/resthome",
            "inLanguage": lang_tag, "description": desc,
            "featureList": [
                "Dossier résident", "Évaluation Katz",
                "Facturation INAMI et forfaits mutuelle",
                "Assurabilité MDA (MyCareNet)",
                "Facturation électronique eFact", "Accords eAgreement",
                "Dossier de soins et prescriptions",
                "Gestion des repas et régimes"],
            "offers": {"@type": "Offer", "category": "SaaS"},
            "publisher": {"@type": "Organization", "name": "LPLG",
                          "url": "https://www.lplg.eu/",
                          "logo": base + "assets/logo.svg",
                          "sameAs": [
                              "https://www.lplg.eu/resthome",
                              "https://www.linkedin.com/company/lplg-europe/",
                              "https://x.com/LPLGEurope",
                              "https://www.facebook.com/profile.php?id=61583440537827",
                              "https://www.instagram.com/lplg.official/",
                              "https://github.com/lplg-europe"]},
        }))

    context["metatags"] = (context.get("metatags") or "") + "\n".join(out)


def setup(app):
    app.add_config_value("rh_site_base",
                         "https://www.lplg.eu/resthome/documentation/", "html")
    app.add_config_value("rh_languages", {"fr": "", "nl": "nl/", "en": "en/"}, "html")
    app.add_config_value("rh_default_language", "fr", "html")
    app.add_node(rh_hidden, html=(visit_rh_hidden, None),
                 latex=(visit_rh_hidden, None), text=(visit_rh_hidden, None),
                 gettext=(None, None))
    app.add_directive("rh-description", RhDescription)
    app.add_directive("rh-faq", RhFaq)
    app.connect("doctree-resolved", collect)
    app.connect("env-purge-doc", purge)
    app.connect("env-merge-info", merge)
    app.connect("html-page-context", html_page_context)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
