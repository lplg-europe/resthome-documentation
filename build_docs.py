#!/usr/bin/env python3
"""Build Sphinx multilingue + multi-version — modèle docs-as-code.

Structure d'URL :  /resthome/documentation/<version>/<préfixe-langue>/<page>
    site/<version>/          ← FR (langue racine de la version)
    site/<version>/nl/       ← NL
    site/<version>/en/       ← EN
    site/<page>/             ← redirection versionless → version canonique (URLs indexées)
    site/{CNAME,robots.txt,sitemap.xml,llms*}   ← racine (neutres)

Nouvelle version : brancher git, bumper `rh_version` (+ rh_versions / rh_canonical_version)
dans conf.py, rebuild. La CI assemble ensuite toutes les versions sous site/.

Usage :
    python build_docs.py              # build des 3 langues de la version courante
    python build_docs.py --gettext    # (re)extrait POT + met à jour les catalogues
"""
import os
import sys
import shutil
import subprocess
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent

# Version lue depuis conf.py (source unique de vérité).
_ns = {"__file__": str(ROOT / "conf.py")}
exec(compile((ROOT / "conf.py").read_text(encoding="utf-8"), "conf.py", "exec"), _ns)
VERSION = _ns["rh_version"]
CANONICAL = _ns["rh_canonical_version"]

SPHINX = [sys.executable, "-m", "sphinx"]
OUT = ROOT / "site"
VOUT = OUT / VERSION
PUBLISH = ROOT / "_publish"
BASE = "https://www.lplg.eu/resthome/documentation/"
LANG_PREFIX = {"fr": "", "nl": "nl/", "en": "en/"}
BUILDS = [("fr", VOUT), ("nl", VOUT / "nl"), ("en", VOUT / "en")]
EXCLUDE = {"genindex", "search", "404"}

_REDIR = ('<!doctype html><html><head><meta charset="utf-8">'
          '<meta http-equiv="refresh" content="0; url={u}">'
          '<link rel="canonical" href="{u}">'
          '<meta name="robots" content="noindex,follow"><title>Redirection</title>'
          '</head><body>Cette page a déménagé : <a href="{u}">{u}</a></body></html>')


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd))
    if subprocess.run(cmd, cwd=ROOT).returncode:
        sys.exit(1)


def gettext():
    run(SPHINX + ["-b", "gettext", "-c", ".", "content", "_build/gettext"])
    run([sys.executable, "-m", "sphinx_intl", "update",
         "-p", "_build/gettext", "-l", "fr", "-l", "nl"])
    print("\nCatalogues mis a jour dans locale/.")


def copy_publish():
    if PUBLISH.exists():
        for f in PUBLISH.iterdir():
            if f.is_file():
                shutil.copy2(f, OUT / f.name)
        print(f"Statiques _publish/ copies a la racine.")


def _pages(root):
    """(rel_dir) de chaque page publiable sous root, hors genindex/search/404."""
    for html in sorted(root.rglob("index.html")):
        rel = html.parent.relative_to(root).as_posix()
        rel = "" if rel == "." else rel
        if any(p in EXCLUDE for p in rel.split("/")):
            continue
        yield rel


def build_sitemap():
    urls = [BASE + VERSION + "/" + (rel + "/" if rel else "") for rel in _pages(VOUT)]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    lines += [f"  <url><loc>{u}</loc></url>" for u in urls]
    lines.append("</urlset>\n")
    (OUT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")
    for extra in VOUT.rglob("sitemap.xml"):       # sitemaps par-langue du thème
        extra.unlink(missing_ok=True)
    print(f"Sitemap : {len(urls)} URLs (version {VERSION}, 3 langues).")


def fix_search_assets():
    """Deux incompatibilités Sphinx 9.1 ↔ thème qui TUENT la recherche :
    1. language_data.js émet `stopwords = new Set(...)` ; le worker du thème
       appelle stopwords.indexOf → TypeError → aucune recherche ne répond.
       On enveloppe : tableau + méthode .has (compatible les deux usages).
    2. translations.js appelle Documentation.addTranslations (doctools.js,
       non chargé par le thème) → ReferenceError. On pose un stub inoffensif.
    Idempotent, appliqué aux _static des 3 langues à chaque build."""
    n = 0
    for p in OUT.rglob("language_data.js"):
        t = p.read_text(encoding="utf-8")
        if "new Set(" in t:
            t = t.replace("const stopwords = new Set(",
                          "const stopwords = ((a) => { a.has = a.includes; return a; })(")
            p.write_text(t, encoding="utf-8")
            n += 1
    for p in OUT.rglob("translations.js"):
        t = p.read_text(encoding="utf-8")
        if not t.startswith("window.Documentation"):
            t = ("window.Documentation = window.Documentation || "
                 "{ addTranslations: function () {} };\n") + t
            p.write_text(t, encoding="utf-8")
            n += 1
    print(f"Assets recherche corriges (stopwords Set->Array, stub doctools) : {n}")


def versionless_redirects():
    """Les anciennes URLs sans version → version canonique (on ne perd rien d'indexé).
    Généré seulement quand on build la version canonique."""
    if VERSION != CANONICAL:
        return
    n = 0
    for rel in _pages(VOUT):
        target = (VERSION + "/" + rel).rstrip("/")
        rel_url = os.path.relpath(target, rel or ".").replace(os.sep, "/") + "/"
        dest = (OUT / rel / "index.html") if rel else (OUT / "index.html")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(_REDIR.format(u=rel_url), encoding="utf-8")
        n += 1
    print(f"Redirections versionless -> /{VERSION}/ : {n}")


def main():
    if "--gettext" in sys.argv:
        gettext()
        return
    if OUT.exists():
        shutil.rmtree(OUT)
    for lang, out in BUILDS:
        run(SPHINX + ["-b", "dirhtml", "-c", ".", "-D", f"language={lang}",
                      "-D", f"html_baseurl={BASE}{VERSION}/{LANG_PREFIX[lang]}",
                      "content", str(out)])
    # llms-full.txt régénéré depuis le SITE FR construit (jamais désynchronisé),
    # AVANT copy_publish qui le recopie à la racine du site.
    run([sys.executable, str(ROOT / "docs-ops" / "gen-llms-full.py")])
    copy_publish()
    build_sitemap()
    fix_search_assets()
    versionless_redirects()
    print(f"\nSite construit : {OUT}  (version {VERSION} — fr racine, /nl, /en)")


if __name__ == "__main__":
    main()
