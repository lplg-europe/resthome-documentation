#!/usr/bin/env python3
"""Génère docs/llms-full.txt : le contenu INTÉGRAL de la doc FR concaténé en un
seul fichier Markdown, pour ingestion par les assistants IA (ChatGPT, Claude,
Perplexity…). Convention https://llmstxt.org/ (variante « full »).

Usage (depuis la racine du repo) :
    .venv/Scripts/python.exe docs-ops/gen-llms-full.py

À relancer après une modification du contenu de la doc, puis commiter
docs/llms-full.txt. (Le fichier est un instantané statique, pas généré au build,
pour éviter tout conflit avec le plugin i18n.)
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FR = REPO / "docs" / "fr"
OUT = REPO / "docs" / "llms-full.txt"
BASE = "https://www.lplg.eu/resthome/documentation/"

# Ordre = ordre de la navigation (mkdocs.yml), pour une lecture cohérente.
ORDER = [
    "index.md",
    "premiers-pas.md",
    "residents/gerer-un-resident.md",
    "residents/katz.md",
    "residents/changement-chambre.md",
    "facturation/index.md",
    "facturation/facturer-un-mois.md",
    "facturation/supplements.md",
    "facturation/absences.md",
    "facturation/depart-deces.md",
    "facturation/split-billing.md",
    "ehealth/index.md",
    "ehealth/mda.md",
    "ehealth/efact.md",
    "ehealth/eagreement.md",
    "soins/index.md",
    "soins/prescriptions.md",
    "soins/plans-de-soins.md",
    "soins/registres.md",
    "repas/index.md",
    "repas/menus-regimes.md",
    "repas/portail-familles.md",
    "configuration/index.md",
]

FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.S)
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
# Nettoyage du markup visuel Material (bruit pour l'IA, pas de contenu utile).
GRID_CARDS = re.compile(r'<div class="grid cards"[^>]*>.*?</div>', re.S)
DIV_TAGS = re.compile(r'</?div[^>]*>')
ICON_SHORTCODE = re.compile(r':(?:material|octicons|fontawesome)[\w-]+:(?:\{[^}]*\})?')
ATTR_LIST = re.compile(r'\{\s*\.[\w .-]+\}')


def clean(text: str) -> str:
    text = HTML_COMMENT.sub("", text)
    text = GRID_CARDS.sub("", text)      # cartes de navigation (redondantes ici)
    text = DIV_TAGS.sub("", text)
    text = ICON_SHORTCODE.sub("", text)  # :material-rocket-launch:{ .lg .middle }
    text = ATTR_LIST.sub("", text)       # { .lg .middle }
    text = re.sub(r"\n{3,}", "\n\n", text)  # compacte les lignes vides multiples
    return text.strip()


def page_url(rel: str) -> str:
    slug = rel[:-3]  # strip .md
    if slug == "index":
        return BASE
    if slug.endswith("/index"):
        slug = slug[: -len("/index")]
    return BASE + slug + "/"


def main() -> None:
    parts = [
        "# Documentation Resthome — contenu intégral",
        "",
        "> Contenu complet de la documentation utilisateur du logiciel Resthome "
        "(maisons de repos MR/MRS en Belgique, édité par LPLG) : résidents, "
        "soins, repas, facturation INAMI/mutuelle, eHealth (MDA, eFact, "
        "eAgreement). Ce fichier suit la convention https://llmstxt.org/ "
        "(variante « full ») pour permettre aux assistants IA de répondre aux "
        "questions des utilisateurs à partir de la documentation officielle.",
        "",
        f"> Index concis : {BASE}llms.txt · Version en ligne : {BASE}",
    ]

    missing = []
    for rel in ORDER:
        f = FR / rel
        if not f.exists():
            missing.append(rel)
            continue
        text = f.read_text(encoding="utf-8")
        text = FRONTMATTER.sub("", text, count=1)
        text = clean(text)
        parts.append("\n\n---\n")
        parts.append(f"Source : {page_url(rel)}\n")
        parts.append(text)

    OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Écrit {OUT.relative_to(REPO)} ({OUT.stat().st_size} octets, "
          f"{len(ORDER) - len(missing)} pages)")
    if missing:
        print("MANQUANTES:", ", ".join(missing))


if __name__ == "__main__":
    main()
