#!/usr/bin/env python3
"""Génère l'index documentaire que l'assistant de `widecare_ai` interroge.

Un enregistrement par SECTION (titre de niveau 2), pas par page : c'est l'unité
qui a un sens tout seul, et c'est aussi la seule qui donne une URL citable —
l'ancre du titre. Une page entière serait trop grosse pour être montrée, un
découpage à taille fixe couperait au milieu d'un tableau et ne saurait pas
vers quoi renvoyer.

Source = le SITE CONSTRUIT (comme gen-llms-full.py), donc le texte réellement
publié, traductions comprises. Les pages sont trouvées en parcourant le site :
aucune liste à tenir à jour ici — celle de gen-llms-full.py a déjà pris trois
sections de retard.

Sortie : _publish/doc-index/<lang>.json, repris par le module Odoo.
Appelé par build_docs.py, ou à la main :
    .venv/Scripts/python.exe docs-ops/gen_doc_index.py
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from markdownify import markdownify

REPO = Path(__file__).resolve().parent.parent
BASE = "https://www.lplg.eu/resthome/documentation/"

# Pages construites qui ne sont pas du contenu.
SKIP = {"search", "genindex", "404"}
# Sous-dossiers de langue dans site/<version>/ ; le FR est à la racine.
LANGS = {"fr": "", "nl": "nl", "en": "en"}
# Sous ce nombre de caractères, une section n'apporte rien toute seule
# (un titre suivi d'une phrase de liaison) : elle est recollée à la précédente.
MIN_CHARS = 180


def _clean(article) -> None:
    """Retire le bruit : ancres ¶, boutons, gabarits, scripts."""
    for sel in ("a.headerlink", ".md-content__button", "template", "script", "style"):
        for el in article.select(sel):
            el.decompose()


LINK = re.compile(r"(\]\()([^)\s]+)(\))")


def _text(nodes, url: str) -> str:
    md = markdownify("".join(str(n) for n in nodes), heading_style="ATX", bullets="-")
    # Un extrait est lu LOIN de sa page : « ../../ehealth/efact/ » n'y veut plus
    # rien dire. Les liens sont rendus absolus contre l'URL de la section.
    md = LINK.sub(lambda m: m[1] + urljoin(url, m[2]) + m[3], md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def _pages(root: Path):
    """(slug, chemin) de chaque page de contenu du site construit."""
    for path in sorted(root.rglob("index.html")):
        rel = path.relative_to(root).parent
        slug = "/".join(rel.parts)
        if slug.split("/")[0] in SKIP or "_static" in rel.parts:
            continue
        # Les autres langues sont des sous-dossiers du site FR : on les saute.
        if rel.parts and rel.parts[0] in LANGS.values() and rel.parts[0]:
            continue
        yield slug, path


def _sections(html: str, url: str):
    """Découpe une page en sections de niveau 2, ancre comprise."""
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article", class_="md-content__inner")
    if article is None:
        return None, []
    _clean(article)
    h1 = article.find("h1")
    title = h1.get_text(strip=True) if h1 else ""

    out, current, buffer = [], None, []

    def flush():
        if not current and not buffer:
            return
        body = _text(buffer, url)
        if not body:
            return
        heading, anchor = current if current else (title, "")
        out.append({
            "heading": heading,
            "url": url + (f"#{anchor}" if anchor else ""),
            "text": body,
        })

    for node in article.children:
        if getattr(node, "name", None) == "h1":
            continue
        if getattr(node, "name", None) == "h2":
            flush()
            current = (node.get_text(strip=True), node.get("id", ""))
            buffer = []
            continue
        buffer.append(node)
    flush()
    return title, out


def build(site: Path, lang: str, subdir: str) -> list[dict]:
    root = site / subdir if subdir else site
    base = BASE + (f"{subdir}/" if subdir else "")
    records = []
    for slug, path in _pages(root):
        url = base + (f"{slug}/" if slug else "")
        title, sections = _sections(path.read_text(encoding="utf-8"), url)
        if not sections:
            continue
        for section in sections:
            # Une section trop courte n'est pas un sujet : on la recolle.
            if records and records[-1]["page"] == title and len(section["text"]) < MIN_CHARS:
                records[-1]["text"] += "\n\n" + section["heading"] + "\n" + section["text"]
                continue
            records.append({
                "id": f"{lang}:{slug or 'index'}#{section['url'].partition('#')[2]}",
                "lang": lang,
                "page": title,
                "heading": section["heading"],
                "url": section["url"],
                "text": section["text"],
            })
    return records


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ns = {"__file__": str(REPO / "conf.py")}
    exec(compile((REPO / "conf.py").read_text(encoding="utf-8"), "conf.py", "exec"), ns)
    site = REPO / "site" / ns["rh_version"]
    if not site.exists():
        raise SystemExit(f"Site introuvable ({site}). Lance d'abord build_docs.py.")

    out_dir = REPO / "_publish" / "doc-index"
    out_dir.mkdir(parents=True, exist_ok=True)
    for lang, subdir in LANGS.items():
        records = build(site, lang, subdir)
        out = out_dir / f"{lang}.json"
        out.write_text(
            json.dumps(records, ensure_ascii=False, indent=1),
            encoding="utf-8",
        )
        chars = sum(len(r["text"]) for r in records)
        print(
            f"{lang} : {len(records)} sections, {chars} caracteres, "
            f"{out.stat().st_size // 1024} Ko -> {out.relative_to(REPO)}"
        )


if __name__ == "__main__":
    main()
