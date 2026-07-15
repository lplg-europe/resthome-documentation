"""Hooks MkDocs pour la doc Resthome.

Le plugin mkdocs-static-i18n émet les liens hreflang alternate en **relatif**
(ex. href="../../../ehealth/efact/"). Or les moteurs de recherche **ignorent le
hreflang relatif** (la spec Google/Bing exige des URLs absolues) — conséquence :
la version NL n'est pas correctement servie aux utilisateurs néerlandophones.

Ce hook réécrit, après rendu de chaque page, les href des liens
`<link rel="alternate" hreflang="...">` en **URLs absolues**, à partir du
canonical (absolu) de la page.
"""
import re
from urllib.parse import urljoin

# <link rel="alternate" href="RELATIF" hreflang="fr">
_ALT_RE = re.compile(r'(<link rel="alternate" href=")([^"]+)(" hreflang="[^"]+">)')


def on_post_page(output, page, config):
    base = page.canonical_url
    if not base and config.get("site_url"):
        base = config["site_url"].rstrip("/") + "/" + page.url
    if not base:
        return output

    def _to_abs(m):
        href = m.group(2)
        if href.startswith(("http://", "https://")):
            return m.group(0)  # déjà absolu
        return m.group(1) + urljoin(base, href) + m.group(3)

    return _ALT_RE.sub(_to_abs, output)
