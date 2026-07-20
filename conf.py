# Configuration Sphinx — documentation Resthome (modèle docs-as-code).
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
project = "Resthome docs"
author = "LPLG"
copyright = "LPLG — CC BY 4.0"

# -- Général ------------------------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",          # grilles de cartes (accueil façon Odoo)
    "sphinx_immaterial",
    "sphinxcontrib.mermaid",
    "resthome_meta",          # _ext/ : description/faq + JSON-LD + hreflang
    "redirects",              # _ext/ : redirige les anciennes URLs (redirects.txt)
]
source_suffix = {".md": "markdown"}
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# La langue est surchargée par build_docs.py (-D language=fr|nl).
language = "en"

# -- MyST ---------------------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",      # :::{directive}
    "deflist",          # listes de définitions (directive rh-faq)
    "attrs_block",
]
myst_fence_as_directive = ["mermaid"]   # les fences ```mermaid → directive
myst_heading_anchors = 3

# -- i18n (le cœur du modèle docs-as-code) -------------------------------------------
# Chemin ABSOLU : sphinx-build (base = content/) et sphinx-intl (base = cwd) ne
# résolvent pas les chemins relatifs pareil → on force l'absolu, seul robuste.
locale_dirs = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "locale")]
gettext_compact = False        # un catalogue par page (granulaire)
gettext_uuid = False
gettext_location = True

# -- HTML ---------------------------------------------------------------------
html_theme = "sphinx_immaterial"
html_title = "Resthome docs"
html_theme_options = {
    "site_url": "https://www.lplg.eu/resthome/documentation/",
    "font": False,   # pas de fetch Google Fonts au build ; notre CSS importe Inter/Roboto Slab
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
html_logo = "content/assets/logo.svg"
html_favicon = "content/assets/favicon.svg"
html_css_files = ["resthome-brand.css"]
html_static_path = ["_static"]
templates_path = ["_templates"]
html_show_sourcelink = False
html_copy_source = False

# html_baseurl est surchargé par langue dans build_docs.py (canonical + hreflang).
html_baseurl = "https://www.lplg.eu/resthome/documentation/"

# -- Extension resthome_meta --------------------------------------------------
rh_site_base = "https://www.lplg.eu/resthome/documentation/"
rh_languages = {"fr": "", "nl": "nl/", "en": "en/"}   # langue -> préfixe d'URL
rh_default_language = "fr"                             # langue servie à la racine

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
