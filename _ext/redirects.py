# -*- coding: utf-8 -*-
"""redirects — port de la mécanique redirects d'Odoo (github.com/odoo/documentation).

But : quand une page est **renommée ou déplacée**, l'ancienne URL doit continuer
d'exister et rediriger vers la nouvelle, sinon on perd son référencement (liens
externes, index Google/Bing/IA). On ne SUPPRIME jamais une URL indexée : on la
redirige.

Fonctionnement : lit `redirects.txt` (une règle par ligne : `ancien nouveau`,
chemins sans extension, `#` = commentaire) et génère, à l'emplacement de l'ancienne
page, une page HTML **meta-refresh** vers la nouvelle (URL relative → marche dans
les 3 langues automatiquement).

Exemple de règle (après avoir renommé le dossier) :
    residents/gerer-un-resident   residents/manage-a-resident
"""
import os
import re
from pathlib import Path

from sphinx.util import logging

logger = logging.getLogger(__name__)

_RULE = re.compile(r"^\s*([\w\-/]+)\s+([\w\-/]+)\s*(?:#.*)?$")

_TMPL = (
    '<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
    '<meta http-equiv="refresh" content="0; url={url}">'
    '<link rel="canonical" href="{url}">'
    '<meta name="robots" content="noindex,follow">'
    "<title>Redirection</title></head>"
    '<body>Cette page a déménagé : <a href="{url}">{url}</a></body></html>'
)


def _load(path):
    rules = []
    if not path.exists():
        return rules
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = _RULE.match(line)
        if m:
            rules.append((m.group(1), m.group(2)))
        else:
            logger.warning("[redirects] ligne ignorée (format invalide) : %r", line)
    return rules


def _urlpath(docname):
    """Dossier dirhtml d'un docname (sans slash) : index→'', a/index→'a', a/b→'a/b'."""
    if docname == "index":
        return ""
    if docname.endswith("/index"):
        return docname[:-6]
    return docname


def build_finished(app, exc):
    if exc is not None:
        return
    rules = _load(Path(app.confdir) / app.config.redirects_file)
    if not rules:
        return
    out = Path(app.outdir)
    lang = app.config.language or "en"
    n = 0
    for old, new in rules:
        # La page redirect est servie à old/ (dirhtml) → relatif depuis old/.
        target = _urlpath(new) or "."
        rel = os.path.relpath(target, old).replace(os.sep, "/")
        rel = "../" if rel == ".." else (rel.rstrip("/") + "/")
        old_dir = out / old
        old_dir.mkdir(parents=True, exist_ok=True)
        (old_dir / "index.html").write_text(
            _TMPL.format(url=rel, lang=lang), encoding="utf-8")
        n += 1
    logger.info("[redirects] %d redirection(s) générée(s).", n)


def setup(app):
    app.add_config_value("redirects_file", "redirects.txt", "env")
    app.connect("build-finished", build_finished)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
