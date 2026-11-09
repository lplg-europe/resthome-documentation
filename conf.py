# Configuration Sphinx — documentation WideCare (modèle docs-as-code).
#
# Source UNIQUE en anglais dans content/ (slugs français conservés = URLs indexées).
# Traductions par catalogues gettext dans locale/{fr,nl}/LC_MESSAGES/.
# Publication : FR à la racine, NL sous /nl/, EN sous /en/ (voir build_docs.py).
#
# Pendant la transition, MkDocs (mkdocs.yml + docs/) continue de servir le site ;
# la bascule CI n'aura lieu qu'à parité prouvée.
import os
import sys

sys.path.insert(0, os.path.abspath("_ext"))

# -- Projet -------------------------------------------------------------------
project = "WideCare"
author = "LPLG"
# Tous droits réservés (plus de CC BY 4.0 depuis le 08/11/2026) : le texte
# complet du pied de page, par langue, est dans _templates/partials/copyright.html.
copyright = "2026 LPLG SRL"

# -- Général ------------------------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",          # grilles de cartes (accueil)
    "sphinx_immaterial",
    "resthome_meta",          # _ext/ : description/faq + JSON-LD + hreflang
    "redirects",              # _ext/ : redirige les anciennes URLs (redirects.txt)
    "countries",              # _ext/ : sélecteur de pays (en-tête) + espaces pays
]
source_suffix = {".md": "markdown"}
master_doc = "index"
# Les .md sous assets/ sont des notes internes (conventions de prise de vue) :
# ce sont des fichiers d'accompagnement, pas des pages du site.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "assets/**/*.md"]

# La langue est surchargée par build_docs.py (-D language=fr|nl).
language = "en"

# -- MyST ---------------------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",      # :::{directive}
    "deflist",          # listes de définitions (directive rh-faq)
    "attrs_block",
]
myst_fence_as_directive = ["mermaid"]   # les fences ```mermaid → directive (voir setup())
myst_heading_anchors = 3

# -- i18n (le cœur du modèle docs-as-code) -------------------------------------------
# Chemin ABSOLU : sphinx-build (base = content/) et sphinx-intl (base = cwd) ne
# résolvent pas les chemins relatifs pareil → on force l'absolu, seul robuste.
locale_dirs = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "locale")]
gettext_compact = False        # un catalogue par page (granulaire)
# PAS de "literal-block" dans gettext_additional_targets, et ce n'est pas un
# oubli : les pages sont écrites en MyST, or Sphinx re-parse le message traduit
# avec le parser du document APRÈS l'avoir préfixé du « :: » de la syntaxe RST.
# En Markdown, ce « :: » n'est qu'un paragraphe : le bloc traduit sortait réduit
# à « :: » (mesuré le 04/09/2026 en FR et en NL, l'anglais restant correct).
# Les libellés des diagrammes mermaid passent donc par un autre chemin : la
# directive `mermaid` de ce fichier (voir setup()) les extrait un par un et
# les remplace au rendu par leur traduction.
gettext_uuid = False
gettext_location = True

# -- HTML ---------------------------------------------------------------------
html_theme = "sphinx_immaterial"
html_title = "WideCare"
html_theme_options = {
    "site_url": "https://www.lplg.eu/resthome/documentation/",
    "font": False,   # pas de fetch Google Fonts au build ; notre CSS importe Inter/Roboto Slab
    # Arbre COMPLET dans la barre latérale : sans ça le thème n'écrit que les
    # sous-pages de la section active, et les autres sections ne peuvent pas
    # porter de chevron dépliable (disposition « à la Odoo »).
    "globaltoc_collapse": False,
    "palette": [
        {"media": "(prefers-color-scheme: light)", "scheme": "default",
         "toggle": {"icon": "material/weather-night", "name": "Mode sombre"}},
        {"media": "(prefers-color-scheme: dark)", "scheme": "slate",
         "toggle": {"icon": "material/weather-sunny", "name": "Mode clair"}},
    ],
    "features": [
        "navigation.top",
        "navigation.sections",
        "search.highlight",
        "search.share",
        "toc.follow",
    ],
}
html_logo = "content/assets/favicon.svg"   # icône WideCare (cœur et pouls), pas le logo LPLG
html_favicon = "content/assets/favicon.svg"
html_css_files = ["resthome-brand.css"]
# rh-mermaid.js est chargé par la directive elle-même (voir setup()) ; celui-ci
# vaut pour toutes les pages : il remet la colonne de navigation en place.
html_js_files = ["rh-sidebar.js", "rh-country.js"]
html_static_path = ["_static"]
templates_path = ["_templates"]
html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False   # pas de « Created using Sphinx » — footer LPLG (voir layout.html)

# html_baseurl est surchargé par langue dans build_docs.py (canonical + hreflang).
html_baseurl = "https://www.lplg.eu/resthome/documentation/"

# -- Extension resthome_meta --------------------------------------------------
rh_site_base = "https://www.lplg.eu/resthome/documentation/"
rh_languages = {"fr": "", "nl": "nl/", "en": "en/"}   # langue -> préfixe d'URL
rh_default_language = "fr"                             # langue servie à la racine

# -- Pays (_ext/countries.py) ----------------------------------------------------
# Un espace par pays sous content/<space>/ ; le reste du site est commun.
# status "soon" : MASQUÉ (ni sélecteur ni carte) ; ses pages restent à écrire.
rh_countries = [
    {"code": "be", "space": "belgique", "status": "live",
     "label": {"en": "Belgium", "fr": "Belgique", "nl": "België"}},
    {"code": "fr", "space": "france", "status": "soon",
     "label": {"en": "France", "fr": "France", "nl": "Frankrijk"}},
    {"code": "lu", "space": "luxembourg", "status": "soon",
     "label": {"en": "Luxembourg", "fr": "Luxembourg", "nl": "Luxemburg"}},
    {"code": "de", "space": "allemagne", "status": "soon",
     "label": {"en": "Germany", "fr": "Allemagne", "nl": "Duitsland"}},
    {"code": "es", "space": "espagne", "status": "soon",
     "label": {"en": "Spain", "fr": "Espagne", "nl": "Spanje"}},
]
# -- Secteurs WideCare (_ext/countries.py) ------------------------------------------
# Un seul site, plusieurs SECTEURS de soins : l'en-tête se lit
# « [WideCare] › [secteur ▾] › [pays ▾] ». Chaque page déclare en front-matter
# les secteurs qu'elle concerne (`sectors: [mr, csj]`) ; la barre latérale, les
# cartes et les listes de pages ne montrent que celles du secteur choisi, et un
# bloc `:class: rh-sector rh-sector-<code>` ne s'affiche que pour ce secteur.
# Le produit s'appelle WideCare dans tous les secteurs (plus de « Resthome »).
# status "soon" : MASQUÉ (ni menu ni carte) tant qu'il n'a pas sa documentation.
rh_sectors = [
    {"code": "mr", "status": "live",
     "label": {"en": "Nursing homes", "fr": "Maisons de repos", "nl": "Woonzorgcentra"},
     "desc": {"en": "Nursing and care homes, short stay", "fr": "MR, MRS et court séjour",
              "nl": "Woonzorgcentra, rust- en verzorgingstehuizen, kortverblijf"}},
    {"code": "csj", "status": "live",
     "label": {"en": "Day care centres", "fr": "Centres de soins de jour", "nl": "Dagverzorgingscentra"},
     "desc": {"en": "People who come by day", "fr": "Les usagers qui viennent en journée",
              "nl": "Gebruikers die overdag komen"}},
    {"code": "rs", "status": "live",
     "label": {"en": "Serviced residences", "fr": "Résidences-services", "nl": "Assistentiewoningen"},
     "desc": {"en": "Housing units, contracts and services", "fr": "Logements, contrats et services",
              "nl": "Wooneenheden, contracten en diensten"}},
    {"code": "gp", "status": "live",
     "label": {"en": "General practitioners", "fr": "Médecins généralistes", "nl": "Huisartsen"},
     "desc": {"en": "The practice, patients and consultations", "fr": "Le cabinet, les patients et les consultations",
              "nl": "De praktijk, patiënten en raadplegingen"}},
    {"code": "hospital", "status": "soon",
     "label": {"en": "Hospitals", "fr": "Hôpitaux", "nl": "Ziekenhuizen"}},
    {"code": "dental", "status": "soon",
     "label": {"en": "Dentists", "fr": "Dentistes", "nl": "Tandartsen"}},
    {"code": "speech", "status": "soon",
     "label": {"en": "Speech therapists", "fr": "Logopèdes", "nl": "Logopedisten"}},
]
rh_default_sector = "mr"   # secteur montré tant que le lecteur n'en a pas choisi
rh_portal = "widecare"       # page portail WideCare (content/widecare.md)
rh_default_country = "be"   # pays montré tant que le lecteur n'en a pas choisi
# Icône de chaque groupe de la barre latérale, repéré par la PREMIÈRE page de son
# toctree dans content/index.md (les groupes pays reçoivent leur drapeau).
rh_nav_group_icons = {
    "premiers-pas": "start",
    "residents/index": "apps",
    "configuration/index": "admin",
    "faq": "help",
}
# Icône d'app devant chaque application de la barre latérale, repérée par sa
# page (jamais par sa position : ajouter ou réordonner une app ne décale rien).
# « nom.png » = icône d'app d'Odoo copiée dans _static/app-icons/ ;
# « mono:nom » = pictogramme à la couleur du texte, variable --rh-appicon-<nom>
# de _static/resthome-brand.css (une app sans icône propre dans Odoo).
rh_nav_app_icons = {
    "residents/index": "residents.png",
    "admissions/index": "admissions.png",
    "residences-services/index": "serviced-living.png",
    "soins/index": "care.png",
    "medicaments/index": "mono:pill",
    "medecins/index": "mono:stethoscope",
    "soins-mobile/index": "care-mobile.png",
    "repas/index": "meals.png",
    "facturation/index": "billing.png",
    "facturation-partagee/index": "split-billing.png",
    "argent-de-poche/index": "mono:wallet",
    "portail-famille/index": "family-portal.png",
    "documents/index": "mono:document",
    "interventions/index": "mono:wrench",
    "planning/index": "planning.png",
    "qualite/index": "mono:quality",
}

# -- Multi-version (modèle docs-as-code) ----------------------------------------------
# URL = base + <version>/ + <préfixe langue> + page  (ex. /documentation/2026/nl/…).
# Le /documentation/ sans version redirige vers rh_canonical_version.
# Nouvelle version : brancher git, bumper rh_version, ajouter en tête de rh_versions,
# et pointer rh_canonical_version sur la dernière stable.
rh_version = "2026"                       # version courante (ce build)
rh_versions = ["2026"]                    # toutes les versions publiées (récentes d'abord)
rh_canonical_version = "2026"             # version canonique (dernière stable = <link canonical>)

# Sélecteur de version : seulement s'il y a PLUSIEURS versions (sinon inutile et
# trompeur — il pointe vers l'URL de prod absolue).
if len(rh_versions) > 1:
    html_theme_options["version_dropdown"] = True
    html_theme_options["version_info"] = [
        {"version": rh_site_base + v + "/", "title": v,
         "aliases": (["latest"] if v == rh_canonical_version else [])}
        for v in rh_versions
    ]

# Lien dépôt (icône GitHub dans l'en-tête, comme l'ancien header).
html_theme_options["repo_url"] = "https://github.com/lplg-europe/resthome-documentation"
html_theme_options["repo_name"] = "resthome-documentation"
html_theme_options["icon"] = {"repo": "fontawesome/brands/github"}


# -- Diagrammes mermaid ---------------------------------------------------------------
# Rendus par `_static/rh-mermaid.js`, depuis le bundle que sphinx-immaterial
# livre dans son paquet — jamais depuis un CDN.
#
# Ni `sphinxcontrib.mermaid` ni la directive du thème ne conviennent :
#   * la première charge mermaid depuis jsdelivr et ne fait pas copier le
#     bundle, si bien que le thème échouait sur « Invalid script:
#     _static/mermaid/mermaid.min.js » et le diagramme restait en texte brut ;
#   * la seconde fait bien copier le bundle, mais son propre rendu laisse un
#     conteneur VIDE (constaté le 04/09/2026 sur toutes les pages à diagramme,
#     alors qu'un appel direct à `mermaid.render` sur le même contenu rend un
#     SVG complet).
#
# La classe est `rh-mermaid` et non `mermaid` : le thème ne touche qu'aux
# secondes, les deux mécanismes ne se marchent donc pas dessus.
def _mermaid_bundle(app, exception):
    """Copie le bundle mermaid à côté du script qui le charge."""
    import shutil
    from pathlib import Path

    import sphinx_immaterial

    # `dirhtml`, pas `html` : c'est le builder que build_docs.py appelle.
    if exception is not None or "html" not in app.builder.name:
        return
    source = Path(sphinx_immaterial.__file__).parent / "bundles" / "mermaid"
    target = Path(app.outdir) / "_static" / "mermaid"
    if source.exists() and not target.exists():
        shutil.copytree(str(source), str(target))


def setup(app):
    """Routage des fences ```mermaid + chargement du rendu maison."""
    from docutils import nodes
    from sphinx.util.docutils import SphinxDirective

    import re

    # Les libellés d'un diagramme : A[texte], B{texte}, -->|texte| et -- texte -->.
    label_re = re.compile(r"(\[)([^\]]+)(\])|(\{)([^}]+)(\})|(\|)([^|]+)(\|)"
                          r"|(--\s+)([^->][^-]*?)(\s+-->)")

    class RhMermaid(SphinxDirective):
        """Un bloc littéral CLASSÉ, pas un bloc brut, dont les LIBELLÉS se traduisent.

        Le bloc entier ne peut pas passer par gettext (voir plus haut pourquoi
        « literal-block » n'est pas dans `gettext_additional_targets`) : ce
        sont ses libellés qui y passent, un par un. Au build `gettext`, chacun
        devient un message de la page (un paragraphe émis pour l'extraction
        seulement) ; au build HTML, chacun est remplacé par sa traduction, lue
        dans le catalogue de la page. Un libellé non traduit reste en anglais,
        comme n'importe quel message.
        """

        has_content = True

        def run(self):
            text = "\n".join(self.content)
            labels = []
            for m in label_re.finditer(text):
                lab = next(g for g in m.group(2, 5, 8, 11) if g)
                if lab.strip() and lab not in labels:
                    labels.append(lab)
            builder = self.env.app.builder.name
            lang = self.config.language or "en"
            if builder != "gettext" and lang != "en" and labels:
                from sphinx.locale import init as init_locale
                from sphinx.util.i18n import docname_to_domain
                domain = docname_to_domain(self.env.docname, self.config.gettext_compact)
                catalog, _found = init_locale(self.config.locale_dirs, lang, domain)

                def translate(m):
                    for i in (1, 4, 7, 10):
                        lab = m.group(i + 1)
                        if lab:
                            return m.group(i) + catalog.gettext(lab) + m.group(i + 2)
                    return m.group(0)
                text = label_re.sub(translate, text)
            node = nodes.literal_block(text, text)
            node["language"] = "none"
            node["classes"] = ["rh-mermaid"]
            self.set_source_info(node)
            result = [node]
            if builder == "gettext":
                for lab in labels:
                    para = nodes.paragraph(lab, "", nodes.Text(lab))
                    self.set_source_info(para)
                    result.append(para)
            return result

    app.add_directive("mermaid", RhMermaid)
    app.add_js_file("rh-mermaid.js", loading_method="defer")
    app.connect("build-finished", _mermaid_bundle)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
