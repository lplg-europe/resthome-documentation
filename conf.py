# Configuration Sphinx — documentation Resthome (modèle Odoo).
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
    "sphinx_immaterial",
    "sphinxcontrib.mermaid",
    "resthome_meta",          # _ext/ : description/faq + JSON-LD + hreflang
]
source_suffix = {".md": "markdown"}
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Le glossaire utilise des ### directement sous le # (liste plate volontaire).
suppress_warnings = ["myst.header"]

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

# -- i18n (le cœur du modèle Odoo) -------------------------------------------
# Chemin ABSOLU : sphinx-build (base = content/) et sphinx-intl (base = cwd) ne
# résolvent pas les chemins relatifs pareil → on force l'absolu, seul robuste.
locale_dirs = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "locale")]
gettext_compact = False        # un catalogue par page (granulaire, comme Odoo)
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
