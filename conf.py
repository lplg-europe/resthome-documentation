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
    "sphinx_design",          # grilles de cartes (accueil)
    "sphinx_immaterial",
    "resthome_meta",          # _ext/ : description/faq + JSON-LD + hreflang
    "redirects",              # _ext/ : redirige les anciennes URLs (redirects.txt)
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
# Conséquence assumée : les libellés des diagrammes mermaid restent en anglais
# dans les trois langues.
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
html_show_sphinx = False   # pas de « Created using Sphinx » — footer LPLG (voir layout.html)

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

    class RhMermaid(SphinxDirective):
        """Un bloc littéral CLASSÉ, pas un bloc brut.

        Un `nodes.raw` serait plus court, mais gettext ne l'extrait pas : les
        libellés des diagrammes resteraient en anglais sur les pages FR et NL.
        Un literal_block, lui, est extrait dès que `gettext_additional_targets`
        contient « literal-block » — ce qu'active ce fichier plus haut.
        """

        has_content = True

        def run(self):
            text = "\n".join(self.content)
            node = nodes.literal_block(text, text)
            node["language"] = "none"
            node["classes"] = ["rh-mermaid"]
            self.set_source_info(node)
            return [node]

    app.add_directive("mermaid", RhMermaid)
    app.add_js_file("rh-mermaid.js", loading_method="defer")
    app.connect("build-finished", _mermaid_bundle)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
