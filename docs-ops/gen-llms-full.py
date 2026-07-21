#!/usr/bin/env python3
"""Génère _publish/llms-full.txt : le contenu INTÉGRAL de la doc FR (le texte
RÉELLEMENT PUBLIÉ), concaténé en Markdown pour ingestion par les assistants IA
(ChatGPT, Claude, Perplexity…). Convention https://llmstxt.org/ (variante « full »).

Source = le SITE FR CONSTRUIT (`site/<version>/…/index.html`), pas l'ancien
`docs/fr` : ainsi le fichier reflète toujours le contenu à jour (landing, seed
FR, descriptions raccourcies) et ne peut plus se désynchroniser.

Appelé automatiquement par `build_docs.py` (après le build, avant copy_publish),
ou à la main :  .venv/Scripts/python.exe docs-ops/gen-llms-full.py
"""
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

REPO = Path(__file__).resolve().parent.parent
BASE = "https://www.lplg.eu/resthome/documentation/"

# Ordre de lecture = ordre de la navigation (docnames, sans .md).
ORDER = [
    "index",
    "premiers-pas", "parcours-facturation",
    "residents/index", "residents/admissions", "residents/gerer-un-resident",
    "residents/katz", "residents/evaluations", "residents/changement-chambre",
    "residents/chambres", "residents/etat-des-lieux",
    "residents/procedure-emmenagement", "residents/mobilier",
    "facturation/index", "facturation/forfait-inami", "facturation/facturer-un-mois",
    "facturation/supplements", "facturation/application-supplements",
    "facturation/absences", "facturation/depart-deces",
    "facturation/note-de-frais-annexe12", "facturation/cpas", "facturation/split-billing",
    "ehealth/index", "ehealth/mda", "ehealth/mda-erreurs", "ehealth/efact",
    "ehealth/efact-rejets", "ehealth/efact-paiements", "ehealth/eagreement",
    "ehealth/eagreement-refus", "ehealth/eagreement-signature",
    "soins/index", "soins/dossier-medical", "soins/prescriptions",
    "soins/sam-base-medicaments", "soins/plans-de-soins", "soins/registres",
    "repas/index", "repas/menus-regimes", "repas/distribution",
    "repas/suivi-nutritionnel", "repas/portail-familles",
    "documents/index", "documents/centralisation",
    "configuration/index", "configuration/reglages-generaux",
    "configuration/reglages-facturation", "configuration/reglages-ehealth",
    "configuration/reglages-repas", "configuration/reglages-documents",
    "faq", "glossaire", "support",
]


def _html_path(site_fr: Path, slug: str) -> Path:
    """docname (sans .md) -> fichier index.html construit (dirhtml)."""
    if slug == "index":
        return site_fr / "index.html"
    if slug.endswith("/index"):
        return site_fr / slug[: -len("/index")] / "index.html"
    return site_fr / slug / "index.html"


def _url(slug: str) -> str:
    """URL versionless (redirige vers la version canonique)."""
    if slug == "index":
        return BASE
    if slug.endswith("/index"):
        slug = slug[: -len("/index")]
    return BASE + slug + "/"


def _extract(html_path: Path) -> str:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    art = soup.find("article", class_="md-content__inner")
    if art is None:
        return ""
    # Retirer le bruit : ancres de titre (¶), bouton d'édition, nœuds cachés.
    for sel in ("a.headerlink", ".md-content__button", "template", "script", "style"):
        for el in art.select(sel):
            el.decompose()
    md = markdownify(str(art), heading_style="ATX", bullets="-", strip=["nav"])
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def generate(site_fr: Path, out: Path) -> tuple[int, list[str]]:
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
    for slug in ORDER:
        p = _html_path(site_fr, slug)
        if not p.exists():
            missing.append(slug)
            continue
        parts.append("\n\n---\n")
        parts.append(f"Source : {_url(slug)}\n")
        parts.append(_extract(p))
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return len(ORDER) - len(missing), missing


def main() -> None:
    # Lit la version depuis conf.py (source unique de vérité).
    ns = {"__file__": str(REPO / "conf.py")}
    exec(compile((REPO / "conf.py").read_text(encoding="utf-8"), "conf.py", "exec"), ns)
    site_fr = REPO / "site" / ns["rh_version"]
    out = REPO / "_publish" / "llms-full.txt"
    if not site_fr.exists():
        raise SystemExit(f"Site FR introuvable ({site_fr}). Lance d'abord build_docs.py.")
    n, missing = generate(site_fr, out)
    print(f"Écrit {out.relative_to(REPO)} ({out.stat().st_size} octets, {n} pages)")
    if missing:
        print("MANQUANTES:", ", ".join(missing))


if __name__ == "__main__":
    main()
