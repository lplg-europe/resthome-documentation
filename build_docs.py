#!/usr/bin/env python3
"""Build Sphinx multilingue — modèle Odoo (source unique EN + catalogues).

Sortie :
    _build/site/        ← FR (langue racine, URLs indexées inchangées)
    _build/site/nl/     ← NL
    _build/site/en/     ← EN

Le build recopie les fichiers de publication (_publish/ : CNAME, robots.txt,
llms.txt, clé IndexNow…) à la racine du site et génère un sitemap.xml propre
couvrant les 3 langues.

Usage :
    python build_docs.py              # build complet des 3 langues + statiques
    python build_docs.py --gettext    # (re)extrait POT + met à jour les catalogues
"""
import subprocess
import sys
import shutil
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SPHINX = [sys.executable, "-m", "sphinx"]
OUT = ROOT / "site"
PUBLISH = ROOT / "_publish"

BASE = "https://www.lplg.eu/resthome/documentation/"
PREFIX = {"fr": "", "nl": "nl/", "en": "en/"}
BUILDS = [("fr", OUT), ("nl", OUT / "nl"), ("en", OUT / "en")]
SITEMAP_EXCLUDE = {"genindex", "search", "404"}


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd))
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode:
        sys.exit(r.returncode)


def gettext():
    run(SPHINX + ["-b", "gettext", "-c", ".", "content", "_build/gettext"])
    run([sys.executable, "-m", "sphinx_intl", "update",
         "-p", "_build/gettext", "-l", "fr", "-l", "nl"])
    print("\nCatalogues mis a jour dans locale/. Traduire puis relancer sans --gettext.")


def copy_publish():
    if not PUBLISH.exists():
        return
    for f in PUBLISH.iterdir():
        if f.is_file():
            shutil.copy2(f, OUT / f.name)
    print(f"Statiques copies depuis _publish/ ({len(list(PUBLISH.iterdir()))} fichiers).")


def build_sitemap():
    """Sitemap propre : toutes les pages des 3 langues, sans genindex/search/404."""
    urls = []
    for html in sorted(OUT.rglob("index.html")):
        rel = html.parent.relative_to(OUT).as_posix()
        top = rel.split("/", 1)[0] if rel else ""
        # exclut genindex/search/404 (et leurs variantes /nl/ /en/)
        parts = rel.split("/")
        if any(p in SITEMAP_EXCLUDE for p in parts):
            continue
        loc = BASE + (rel + "/" if rel else "")
        urls.append(loc)
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines.append(f"  <url><loc>{u}</loc></url>")
    lines.append("</urlset>\n")
    (OUT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")
    # supprime les sitemaps par-langue générés par le thème (on garde le nôtre)
    for extra in (OUT / "nl" / "sitemap.xml", OUT / "en" / "sitemap.xml"):
        extra.unlink(missing_ok=True)
    print(f"Sitemap : {len(urls)} URLs (3 langues).")


def main():
    if "--gettext" in sys.argv:
        gettext()
        return

    if OUT.exists():
        shutil.rmtree(OUT)          # build reproductible
    for lang, out in BUILDS:
        run(SPHINX + ["-b", "dirhtml", "-c", ".", "-D", f"language={lang}",
                      "-D", f"html_baseurl={BASE}{PREFIX[lang]}",
                      "content", str(out)])
    copy_publish()
    build_sitemap()
    print(f"\nSite construit : {OUT}  (fr racine, /nl, /en)")


if __name__ == "__main__":
    main()
