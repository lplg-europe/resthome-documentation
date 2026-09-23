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

Émis dans <head> : <template id="rh-cs"> (menu des pays, liens RELATIFS), que
layout.html place dans l'en-tête, et `data-rh-page-country` sur <html>.
"""
import os

FLAGS = {
    # Drapeaux en SVG : les émojis-drapeaux ne s'affichent pas sous Windows.
    "be": '<rect width="1" height="2" fill="#1a1a1a"/><rect x="1" width="1" height="2" '
          'fill="#FDDA24"/><rect x="2" width="1" height="2" fill="#EF3340"/>',
    "fr": '<rect width="1" height="2" fill="#002395"/><rect x="1" width="1" height="2" '
          'fill="#fff"/><rect x="2" width="1" height="2" fill="#ED2939"/>',
    "lu": '<rect width="3" height=".67" fill="#EF3340"/><rect y=".67" width="3" '
          'height=".66" fill="#fff"/><rect y="1.33" width="3" height=".67" fill="#00A3E0"/>',
}

LABELS = {
    "menu": {"en": "Country", "fr": "Pays", "nl": "Land"},
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
    context["metatags"] = ((context.get("metatags") or "") + "\n" + tmpl + "\n"
                           + _style(app) + "\n" + _boot(app, current))


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
    return "<style>" + "".join(rules) + "</style>"


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
    app.connect("html-page-context", html_page_context)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
