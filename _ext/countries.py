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

Au-dessus du pays, le SECTEUR de soins : l'en-tête se lit
« [WideCare] › [secteur ▾] › [pays ▾] ». WideCare mène au portail (rh_portal,
content/widecare.md, cartes générées par `:::{rh-suites}`). Chaque page déclare
ses secteurs en front-matter (`sectors: [mr, csj]`, conf.py : rh_sectors) :
  - sur une page, le secteur est le dernier choisi s'il la concerne, sinon le
    premier de la page ;
  - la barre latérale, les cartes et les listes de pages ne gardent que les
    pages du secteur (_static/rh-country.js, d'après la carte des secteurs
    émise dans <head>) ;
  - un bloc `:class: rh-sector rh-sector-<code>` ne s'affiche que pour ce secteur.

Émis dans <head> : <template id="rh-cs"> (menu des pays), <template
id="rh-sector"> (menu des secteurs) et la carte page → secteurs, liens
RELATIFS, que _static/rh-country.js place dans l'en-tête ; `data-rh-country`
et `data-rh-sector` sur <html>.
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
    "sector": {"en": "Care sector", "fr": "Secteur", "nl": "Sector"},
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
        if c.get("status") == "soon":       # masqué tant qu'il n'est pas « live »
            continue
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
    # En-tête « WideCare › [secteur ▾] › [pays ▾] » (layout.html).
    tmpl += _sector_template(app, pagename, lang, here)
    context["metatags"] = ((context.get("metatags") or "") + "\n" + tmpl + "\n"
                           + _style(app, context.get("pathto")) + "\n"
                           + _boot(app, current, page_sectors(app, pagename)))


def _rel(target, here):
    rel = os.path.relpath(target or ".", here).replace(os.sep, "/")
    return "./" if rel == "." else rel.rstrip("/") + "/"


def _sector_name(s, lang):
    label = s["label"].get(lang, s["label"]["en"])
    return s.get("name") or "", label


def _live_sectors(app):
    return [s["code"] for s in app.config.rh_sectors if s.get("status") != "soon"]


def page_sectors(app, docname):
    """Secteurs d'une page (front-matter `sectors:`), tous si elle n'en dit rien."""
    raw = app.env.metadata.get(docname, {}).get("sectors")
    if raw is None:
        return _live_sectors(app)
    if isinstance(raw, str):
        raw = raw.strip().strip("[]").split(",")
    return [c.strip().strip("'\"") for c in raw if c and c.strip()]


def sector_map(app):
    """docname → secteurs, pour tout le site (calculé une fois par build)."""
    cached = getattr(app, "_rh_sector_map", None)
    if cached is None:
        cached = {d: page_sectors(app, d) for d in sorted(app.env.found_docs)}
        app._rh_sector_map = cached
    return cached


def _sector_template(app, pagename, lang, here):
    """<template id="rh-sector"> : le menu des secteurs de l'en-tête, et la carte
    page → secteurs que _static/rh-country.js lit pour filtrer la navigation.
    Un secteur vivant mène à l'accueil (filtré pour lui), un secteur « bientôt »
    au portail."""
    import json
    portal = _rel(app.config.rh_portal, here)
    home = _rel("", here)
    items = []
    for s in app.config.rh_sectors:
        if s.get("status") == "soon":       # masqué tant qu'il n'est pas « live »
            continue
        name, label = _sector_name(s, lang)
        live = s.get("status") != "soon"
        soon = ("" if live else
                f'<span class="rh-soon">{LABELS["soon"].get(lang, "Coming soon")}</span>')
        desc = (s.get("desc") or {}).get(lang, "")
        sub = f'<span class="rh-suite-sub">{desc}</span>' if desc else ""
        head = f"{name} · {label}" if name else label
        data = (f' data-sector="{s["code"]}" data-name="{name}" data-label="{label}"'
                if live else "")
        items.append(
            f'<a class="rh-country" role="menuitem" href="{home if live else portal}"{data}>'
            f'<span class="rh-country__name">{head}{sub}</span>{soon}</a>')
    is_portal = "1" if pagename == app.config.rh_portal else ""
    smap = json.dumps(sector_map(app), separators=(",", ":"))
    return (f'<template id="rh-sector" data-portal="{portal}" data-root="{home}" '
            f'data-is-portal="{is_portal}" data-menu="{LABELS["sector"].get(lang, "Sector")}">'
            + "".join(items) + "</template>"
            + f'<script id="rh-sector-map" type="application/json">{smap}</script>')


class RhSuites(SphinxDirective):
    """`:::{rh-suites}` — les cartes des secteurs WideCare, depuis conf.py
    (rh_sectors). Libellés pris dans la config, par langue : rien à traduire.
    Une carte vivante ouvre l'accueil, filtré pour son secteur."""

    def run(self):
        lang = self.config.language or "en"
        here = _dir(self.env.docname) or "."
        cards = []
        for s in self.config.rh_sectors:
            if s.get("status") == "soon":   # masqué tant qu'il n'est pas « live »
                continue
            name, label = _sector_name(s, lang)
            live = s.get("status") != "soon"
            badge = (LABELS["live"] if live else LABELS["soon"]).get(lang, "")
            desc = (s.get("desc") or {}).get(lang, "")
            title = f"{name} · {label}" if name else label
            head = (f'<span class="rh-suite-card__name">{title}</span>'
                    + (f'<span class="rh-suite-card__label">{desc}</span>' if desc else ""))
            # « Disponible » n'a de sens qu'à côté d'un « Bientôt » (masqué).
            foot = "" if live else f'<span class="rh-suite-card__badge is-soon">{badge}</span>'
            if live:
                cards.append(f'<a class="rh-suite-card is-live" href="{_rel("", here)}" '
                             f'data-pick-sector="{s["code"]}">{head}{foot}</a>')
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
        cached = [[doc for _title, doc in tt["entries"]]
                  for tt in root.findall(addnodes.toctree)]
        app._rh_nav_groups = cached
    return cached


def _nav_style(app, pathto=None):
    """Icônes et drapeaux des groupes, et icône d'app de chaque entrée, placés
    d'après l'ordre réel des toctrees : ajouter un pays ou une application (ou
    réordonner) ne décale plus la feuille de style."""
    rules = []
    app_icons = app.config.rh_nav_app_icons
    for n, entries in enumerate(_nav_groups(app), 1):
        first = entries[0] if entries else ""
        for m, doc in enumerate(entries, 1):
            icon = app_icons.get(doc)
            if not icon:
                continue
            link = f"#__nav_{n}_{m} + .md-nav__container > a"
            if icon.startswith("mono:"):
                rules.append(f"{link}{{--rh-app-icon:var(--rh-appicon-{icon[5:]})}}"
                             f"{link}::before{{background:currentColor;opacity:.75;"
                             f"-webkit-mask:var(--rh-app-icon) center/contain no-repeat;"
                             f"mask:var(--rh-app-icon) center/contain no-repeat}}")
            elif pathto:
                # L'image directement sur ::before, pas via --rh-app-icon : un
                # url() relatif dans une variable se résout contre la feuille
                # qui l'UTILISE (_static/…), pas contre cette page.
                url = pathto("_static/app-icons/" + icon, 1)
                rules.append(f'{link}::before{{background-image:url("{url}")}}')
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


def _style(app, pathto=None):
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
    for code in _live_sectors(app):
        rules.append(f'html:not([data-rh-sector="{code}"]) .rh-sector-{code}{{display:none}}')
    # La barre latérale attend le filtre du secteur (rh-country.js) : pas de flash.
    rules.append("html.rh-nav-pending .md-sidebar--primary .md-nav--primary{visibility:hidden}")
    return "<style>" + "".join(rules) + _nav_style(app, pathto) + "</style>"


def _boot(app, current, sectors):
    """Fixe le pays et le secteur sur <html> dès le <head>.
    Pays : celui de la page, sinon le choix mémorisé, sinon le pays par défaut.
    Secteur : le choix mémorisé s'il concerne la page, sinon le premier secteur
    de la page (mémorisé), sinon le secteur par défaut."""
    codes = [c["code"] for c in app.config.rh_countries]
    return ("<script>(function(){var p=%r,d=%r,ok=%s,c='',h=document.documentElement;"
            "try{c=localStorage.getItem('rh-country')||''}catch(e){}"
            "if(p){c=p;try{localStorage.setItem('rh-country',p)}catch(e){}}"
            "if(ok.indexOf(c)<0)c=d;"
            "h.setAttribute('data-rh-country',c);"
            "var ps=%s,sd=%r,all=%s,s='';"
            "try{s=localStorage.getItem('rh-sector')||''}catch(e){}"
            "if(all.indexOf(s)<0)s=sd;"
            "if(ps.length&&ps.indexOf(s)<0){s=ps[0];try{localStorage.setItem('rh-sector',s)}catch(e){}}"
            "h.setAttribute('data-rh-sector',s);h.classList.add('rh-nav-pending')})();</script>"
            % (current, app.config.rh_default_country, str(codes),
               str(list(sectors)), app.config.rh_default_sector, str(_live_sectors(app))))


def setup(app):
    app.add_config_value("rh_countries", [], "html")
    app.add_config_value("rh_default_country", "be", "html")
    app.add_config_value("rh_sectors", [], "html")
    app.add_config_value("rh_default_sector", "mr", "html")
    app.add_config_value("rh_portal", "widecare", "html")
    app.add_directive("rh-suites", RhSuites)
    # Première page d'un toctree de l'accueil → icône de son groupe (variable
    # --rh-icon-<nom> de _static/resthome-brand.css).
    app.add_config_value("rh_nav_group_icons", {}, "html")
    # Page d'une application → son icône d'app (png de _static/app-icons/ ou
    # « mono:<nom> » = variable --rh-appicon-<nom>), où qu'elle soit rangée.
    app.add_config_value("rh_nav_app_icons", {}, "html")
    app.connect("html-page-context", html_page_context)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
