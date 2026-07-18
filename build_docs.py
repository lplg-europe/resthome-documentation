#!/usr/bin/env python3
"""Build Sphinx multilingue — modèle Odoo.

Source unique EN (content/), catalogues locale/{fr,nl}, sortie :
    _build/site/        ← FR (langue racine, comme aujourd'hui)
    _build/site/nl/     ← NL
    _build/site/en/     ← EN (nouvelle)

Usage :  .venv/Scripts/python.exe build_docs.py [--gettext]
    --gettext : (re)extrait les POT et met à jour les catalogues fr/nl.
"""
import subprocess
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SPHINX = [sys.executable, "-m", "sphinx"]
OUT = ROOT / "_build" / "site"

BUILDS = [
    ("fr", OUT),           # langue racine (URLs indexées inchangées)
    ("nl", OUT / "nl"),
    ("en", OUT / "en"),
]
BASE = "https://www.lplg.eu/resthome/documentation/"
PREFIX = {"fr": "", "nl": "nl/", "en": "en/"}


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd))
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode:
        sys.exit(r.returncode)


def main():
    if "--gettext" in sys.argv:
        run(SPHINX + ["-b", "gettext", "-c", ".", "content", "_build/gettext"])
        run([sys.executable, "-m", "sphinx_intl", "update",
             "-p", "_build/gettext", "-l", "fr", "-l", "nl"])
        print("\nCatalogues mis a jour dans locale/. Traduire puis relancer sans --gettext.")
        return

    for lang, out in BUILDS:
        run(SPHINX + ["-b", "dirhtml", "-c", ".", "-D", f"language={lang}",
                      "-D", f"html_baseurl={BASE}{PREFIX[lang]}",
                      "content", str(out)])
    print(f"\nSite construit : {OUT}  (fr racine, /nl, /en)")


if __name__ == "__main__":
    main()
