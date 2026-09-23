# -*- coding: utf-8 -*-
"""countries — documentation multi-pays, sur un seul site.

Les pages communes vivent à la racine de content/ ; ce qui vient des règles
d'un pays vit dans son espace (content/belgique/, content/france/…). Un seul
build par langue : pas de page commune dupliquée par pays (SEO), et une URL
reste la même quel que soit le pays choisi.

Le choix du pays se fait dans l'en-tête (_static/rh-country.js) :
  - sur une page d'un espace pays, c'est le pays de la page ;
  - ailleurs, le dernier pays choisi (localStorage), par défaut `rh_default_country` ;
  - la barre latérale ne montre que les sections communes et celle du pays ;
  - dans une page commune, un bloc `:class: rh-country-<code>` ne s'affiche que
    pour ce pays (renvoi vers ses spécificités).

Au-dessus du pays, la hiérarchie WideCare : l'en-tête se lit
« [WideCare] › [suite ▾] › [pays ▾] ». WideCare mène au portail (rh_portal,
content/widecare.md, cartes générées par `:::{rh-suites}`) ; le menu de la
suite liste rh_suites (celle de CE site : rh_suite_code).

Émis dans <head> : <template id="rh-cs"> (menu des pays) et <template
id="rh-suite"> (menu des suites), liens RELATIFS, que _static/rh-country.js
place dans l'en-tête, et `data-rh-country` sur <html>.
"""
import os

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

FLAGS = {
    # Drapeaux en SVG : les émojis-drapeaux ne s'affichent pas sous Windows.
    "be": '<rect width="1" height="2" fill="#1a1a1a"/><rect x="1" width="1" height="2" '
          'fill="#FDDA24"/><rect x="2" width="1" height="2" fill="#EF3340"/>',
    "fr": '<rect width="1" height="2" fill="#002395"/><rect x="1" width="1" height="2" '
          'fill="#fff"/><rect x="2" width="1" height="2" fill="#ED2939"/>',
    "lu": '<rect width="3" height=".67" fill="#EF3340"/><rect y=".67" width="3" '
          'height=".66" fill="#fff"/><rect y="1.33" width="3" height=".67" fill="#00A3E0"/>',
    "de": '<rect width="3" height=".67" fill="#000"/><rect y=".67" width="3" '
          'height=".66" fill="#DD0000"/><rect y="1.33" width="3" height=".67" fill="#FFCE00"/>',
    "es": '<rect width="3" height="2" fill="#AA151B"/><rect y=".5" width="3" height="1" '
          'fill="#F1BF00"/>',
}

LABELS = {
    "menu": {"en": "Country", "fr": "Pays", "nl": "Land"},
    "suite": {"en": "Suite", "fr": "Suite", "nl": "Suite"},
    "live": {"en": "Available", "fr": "Disponible", "nl": "Beschikbaar"},
    "soon": {"en": "Coming soon", "fr": "Bientôt", "nl": "Binnenkort"},
}


def _flag(code):
    return (f'<svg class="rh-flag" viewBox="0 0 3 2" aria-hidden="true">'
            f'{FLAGS.get(code, "")}</svg>')


def _dir(pagename):
    """Dossier dirhtml d'une page : index→'', a/index→'a', a/b→'a/b'."""
    if pagename == "index":
        return ""
    if pagename.endswith("/index"):
        return pagename[:-6]
    return pagename


def page_country(app, pagename):
    for c in app.config.rh_countries:
        if pagename == c["space"] or pagename.startswith(c["space"] + "/"):
            return c["code"]
    return ""


def html_page_context(app, pagename, templatename, context, doctree):
    if doctree is None:
        return
    lang = app.config.language or "en"
    here = _dir(pagename) or "."
    items = []
    for c in app.config.rh_countries:
        rel = os.path.relpath(c["space"], here).replace(os.sep, "/")
        rel = "./" if rel == "." else rel.rstrip("/") + "/"
        name = c["label"].get(lang, c["label"]["en"])
        soon = ""
        if c.get("status") == "soon":
            soon = f'<span class="rh-soon">{LABELS["soon"].get(lang, "Coming soon")}</span>'
        items.append(
            f'<a class="rh-country" role="menuitem" href="{rel}" data-country="{c["code"]}" '
            f'data-name="{name}" data-space="{c["space"]}">{_flag(c["code"])}'
            f'<span class="rh-country__name">{name}</span>{soon}</a>')
    menu = LABELS["menu"].get(lang, "Country")
    current = page_country(app, pagename)
    tmpl = (f'<template id="rh-cs" data-page-country="{current}" '
            f'data-default="{app.config.rh_default_country}" data-menu="{menu}">'
            + "".join(items) + "</template>")
    # En-tête « WideCare › <suite> · <métier> » (layout.html) : un site par suite.
    tmpl += _suite_template(app, pagename, lang, here)
    context["metatags"] = ((context.get("metatags") or "") + "\n" + tmpl + "\n"
                           + _style(app) + "\n" + _boot(app, current))


def _rel(target, here):
    rel = os.path.relpath(target or ".", here).replace(os.sep, "/")
    return "./" if rel == "." else rel.rstrip("/") + "/"


def _suite_name(s, lang):
    label = s["label"].get(lang, s["label"]["en"])
    return s.get("name") or label, label


def _suite_template(app, pagename, lang, here):
    """<template id="rh-suite"> : le fil « [WideCare] › [suite ▾] » de l'en-tête
    (layout.html, _static/rh-country.js). « WideCare » mène au portail ; le menu
    liste les suites — celle de CE site ouvre son accueil, une suite « bientôt »
    ouvre le portail, qui dit où elle en est."""
    portal = _rel(app.config.rh_portal, here)
    home = _rel("", here)
    items = []
    for s in app.config.rh_suites:
        name, label = _suite_name(s, lang)
        mine = s["code"] == app.config.rh_suite_code
        soon = (f'<span class="rh-soon">{LABELS["soon"].get(lang, "Coming soon")}</span>'
                if s.get("status") == "soon" else "")
        sub = f'<span class="rh-suite-sub">{label}</span>' if name != label else ""
        items.append(
            f'<a class="rh-country{" is-current" if mine else ""}" role="menuitem" '
            f'href="{home if mine else portal}" data-suite="{s["code"]}">'
            f'<span class="rh-country__name">{name}{sub}</span>{soon}</a>')
    cur = next((s for s in app.config.rh_suites if s["code"] == app.config.rh_suite_code), None)
    name, label = _suite_name(cur, lang) if cur else ("", "")
    is_portal = "1" if pagename == app.config.rh_portal else ""
    return (f'<template id="rh-suite" data-portal="{portal}" data-name="{name}" '
            f'data-label="{label}" data-is-portal="{is_portal}" '
            f'data-menu="{LABELS["suite"].get(lang, "Suite")}">' + "".join(items) + "</template>")


class RhSuites(SphinxDirective):
    """`:::{rh-suites}` — les cartes des suites WideCare, depuis conf.py
    (rh_suites). Libellés pris dans la config, par langue : rien à traduire."""

    def run(self):
        lang = self.config.language or "en"
        here = _dir(self.env.docname) or "."
        cards = []
        for s in self.config.rh_suites:
            name, label = _suite_name(s, lang)
            live = s.get("status") != "soon"
            badge = (LABELS["live"] if live else LABELS["soon"]).get(lang, "")
            head = (f'<span class="rh-suite-card__name">{name}</span>'
                    + (f'<span class="rh-suite-card__label">{label}</span>' if name != label else ""))
            foot = f'<span class="rh-suite-card__badge{"" if live else " is-soon"}">{badge}</span>'
            if live:
                cards.append(f'<a class="rh-suite-card is-live" href="{_rel("", here)}">'
                             f'{head}{foot}</a>')
            else:
                cards.append(f'<div class="rh-suite-card">{head}{foot}</div>')
        return [nodes.raw("", '<div class="rh-suite-cards">' + "".join(cards) + "</div>",
                          format="html")]


def _flag_uri(code):
    """Le drapeau en URL data: pour une propriété CSS (guillemets simples, # échappé)."""
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 3 2'>"
           + FLAGS.get(code, "").replace('"', "'") + "</svg>")
    return 'url("data:image/svg+xml,' + svg.replace("#", "%23") + '")'


def _nav_groups(app):
    """Première page de chaque toctree de la page d'accueil, dans l'ordre : le
    thème numérote les groupes de la barre latérale dans cet ordre
    (#__nav_1_label, #__nav_2_label…). Calculé une fois par build."""
    cached = getattr(app, "_rh_nav_groups", None)
    if cached is None:
        from sphinx import addnodes
        root = app.env.get_doctree(app.config.root_doc)
        cached = [tt["entries"][0][1] if tt["entries"] else ""
                  for tt in root.findall(addnodes.toctree)]
        app._rh_nav_groups = cached
    return cached


def _nav_style(app):
    """Icônes et drapeaux des groupes, placés d'après l'ordre réel des toctrees :
    ajouter un pays (ou réordonner) ne décale plus la feuille de style."""
    rules = []
    for n, first in enumerate(_nav_groups(app), 1):
        label = f"#__nav_{n}_label"
        icon = app.config.rh_nav_group_icons.get(first)
        if icon:
            rules.append(f"{label}{{--rh-group-icon:var(--rh-icon-{icon})}}")
        for c in app.config.rh_countries:
            if first == c["space"] or first.startswith(c["space"] + "/"):
                rules.append(
                    f"{label}::before{{-webkit-mask:none;mask:none;width:1.05rem;height:.7rem;"
                    f"border-radius:2px;box-shadow:0 0 0 1px rgba(0,0,0,.18);"
                    f"background:{_flag_uri(c['code'])} center/cover no-repeat}}")
    for c in app.config.rh_countries:
        rules.append(f".md-typeset .admonition.rh-country-{c['code']}"
                     f"{{--rh-flag:{_flag_uri(c['code'])}}}")
    return "".join(rules)


def _style(app):
    """Filtre en CSS pur, appliqué avant le premier affichage (pas de flash).

    Une section de la barre latérale qui mène à l'espace d'un AUTRE pays est
    masquée. Les liens d'une section vers son propre espace sont relatifs
    (« ../katz/ ») depuis une page de cet espace — mais on est alors dans ce
    pays, donc cette section n'a jamais à disparaître."""
    rules = []
    for c in app.config.rh_countries:
        not_c = f'html:not([data-rh-country="{c["code"]}"])'
        rules.append(f'{not_c} .md-nav__item--section:has(a[href*="{c["space"]}/"])'
                     '{display:none}')
        rules.append(f'{not_c} .rh-country-{c["code"]}{{display:none}}')
    return "<style>" + "".join(rules) + _nav_style(app) + "</style>"


def _boot(app, current):
    """Fixe le pays sur <html> dès le <head> : pays de la page, sinon le choix
    mémorisé, sinon le pays par défaut."""
    codes = [c["code"] for c in app.config.rh_countries]
    return ("<script>(function(){var p=%r,d=%r,ok=%s,c='';"
            "try{c=localStorage.getItem('rh-country')||''}catch(e){}"
            "if(p){c=p;try{localStorage.setItem('rh-country',p)}catch(e){}}"
            "if(ok.indexOf(c)<0)c=d;"
            "document.documentElement.setAttribute('data-rh-country',c)})();</script>"
            % (current, app.config.rh_default_country, str(codes)))


def setup(app):
    app.add_config_value("rh_countries", [], "html")
    app.add_config_value("rh_default_country", "be", "html")
    app.add_config_value("rh_suites", [], "html")
    app.add_config_value("rh_suite_code", "", "html")
    app.add_config_value("rh_portal", "widecare", "html")
    app.add_directive("rh-suites", RhSuites)
    # Première page d'un toctree de l'accueil → icône de son groupe (variable
    # --rh-icon-<nom> de _static/resthome-brand.css).
    app.add_config_value("rh_nav_group_icons", {}, "html")
    app.connect("html-page-context", html_page_context)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
