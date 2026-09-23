#!/usr/bin/env python3
"""check_docs.py — contrôle des conventions de contenu (inspiré d'un contrôle de conventions).

Vérifie chaque page de content/ :
  - un titre H1 unique en tête ;
  - un bloc :::{rh-description} (meta + JSON-LD) ;
  - aucun résidu MkDocs (admonitions !!!, grid cards, entités HTML échappées) ;
  - front-matter limité à howto_auto (title/description/faq passent par directives) ;
  - pas de lien ancré cross-fichier (page.md#ancre) — casse en i18n ;
  - pas de terme propre à un pays dans une page COMMUNE (hors espace pays et
    hors encadré `rh-country-<code>`) : voir CONTRIBUTING.md, « Pays » ;
  - front-matter `modules:` présent, modules connus de docs-ops/modules.json
    (instantané du code, voir docs-ops/sync-modules.py), et PLACEMENT cohérent
    avec le code : une page commune ne documente aucun module lié à un pays,
    une page d'un espace pays documente au moins un module de ce pays.

Usage :  python check_docs.py              (exit 1 si au moins une erreur)
         python check_docs.py --coverage   (+ écrit docs-ops/coverage.md :
                                            modules qu'aucune page ne documente)
"""
import json
import re
import sys
import pathlib

import yaml

CONTENT = pathlib.Path(__file__).resolve().parent / "content"
errors = []

# Espaces pays (conf.py : rh_countries) — leurs pages parlent le langage du pays.
COUNTRY_SPACES = {"belgique": "be", "france": "fr", "luxembourg": "lu"}
# Suites publiées par CE site (un site par suite — voir CONTRIBUTING.md).
SITE_SUITES = {"platform", "resthome"}
MODULES = json.loads((CONTENT.parent / "docs-ops" / "modules.json").read_text(encoding="utf-8"))
documented = {}     # module → pages qui le documentent (rapport de couverture)
warnings = []


def _load_debt():
    """docs-ops/placement-debt.txt : (page, module) → « nature — raison »."""
    debt = {}
    path = CONTENT.parent / "docs-ops" / "placement-debt.txt"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            page, module, nature, reason = line.split(None, 3)
            debt[(page, module)] = f"{nature} — {reason}"
    return debt


DEBT = _load_debt()
debt_seen = set()

# Arbre des menus (docs-ops/menus.json, instantané du code) : un chemin cité
# « **A → B → C** » dont A est une application racine doit exister, niveau par
# niveau, sous l'un de ses noms (un module peut renommer ou déplacer un menu).
MENUS = json.loads((CONTENT.parent / "docs-ops" / "menus.json").read_text(encoding="utf-8"))
_CHILDREN = {}
for _mid, _m in MENUS.items():
    for _par in (_m["parents"] or [None]):
        _CHILDREN.setdefault(_par if _par in MENUS else None, []).append(_mid)


def _norm(s):
    return re.sub(r"\s+", " ", s).strip().rstrip(".").lower()


_ROOT_NAMES = {_norm(n) for mid in _CHILDREN.get(None, []) for n in MENUS[mid]["names"]}


def _menu_path_exists(segments):
    level = [m for m in _CHILDREN.get(None, [])
             if _norm(segments[0]) in map(_norm, MENUS[m]["names"])]
    for n, seg in enumerate(segments[1:], 2):
        # Dernier niveau en texte courant : la phrase continue après le libellé
        # (« Forfait → Calculations and create one… ») — on essaie ses débuts.
        words = _norm(seg).split()
        tries = [" ".join(words[:i]) for i in range(len(words), 0, -1)] \
            if n == len(segments) else [_norm(seg)]
        level = next((found for t in tries
                      if (found := [c for p in level for c in _CHILDREN.get(p, [])
                                    if t in map(_norm, MENUS[c]["names"])])), [])
        if not level:
            return False
    return True


def _segment(s):
    """« the **Nursing Home** app » → « nursing home » : gras, articles et le mot
    « app / application » ne font pas partie du libellé du menu."""
    s = re.sub(r"\*\*|`", "", s)
    s = re.sub(r"^\s*(?:through|via|in|under|open|the|l'application|la|le)\s+", "", s, flags=re.I)
    s = re.sub(r"^\s*the\s+", "", s, flags=re.I)
    s = re.sub(r"\s+(?:app|application)\s*$", "", s, flags=re.I)
    return _norm(s)


def check_menu_paths(rel, body):
    # Un chemin = au moins deux libellés séparés par « → » sur une même ligne,
    # en gras d'un bloc (**A → B**), en gras par morceaux (**A** → **B**) ou en
    # texte simple. Seuls ceux qui partent d'une application racine sont vérifiés
    # (« Draft → Sent » est un enchaînement de statuts, pas un menu).
    text = re.sub(r"\s*\n\s*", " ", body)           # un libellé peut passer à la ligne
    for m in re.finditer(r"[^.;:,()«»\[\]→—]+?(?:\s*→\s*[^.;:,()«»\[\]→—]+)+", text):
        segments = [_segment(s) for s in m.group(0).split("→")]
        # le premier morceau peut porter du texte avant le menu : on garde les
        # derniers mots qui forment un nom de racine
        words = segments[0].split()
        for i in range(len(words)):
            if " ".join(words[i:]) in _ROOT_NAMES:
                segments[0] = " ".join(words[i:])
                break
        else:
            continue
        if not _menu_path_exists(segments):
            errors.append(f"{rel}: chemin de menu introuvable dans le code "
                          f"« {' → '.join(segments)} » (docs-ops/menus.json)")
# Termes qui n'ont de sens qu'en Belgique : interdits dans une page commune,
# sauf dans un encadré `:class: rh-country rh-country-be`.
COUNTRY_TERMS = re.compile(
    r"\b(Katz|NISS|INAMI|RIZIV|eFact|MDA|eAgreement|AViQ|CPAS|MyCareNet|"
    r"MR/MRS|MRS|eHealth|BelRAI|WalCareNet|FEMARBEL|pseudo-codes?|"
    r"Annexe?s? \d+|mutualit\w*)\b")


def _without_country_blocks(body):
    """Le texte d'une page commune, sans ses encadrés pays, sans les cibles de
    liens ni les images (une capture montre l'interface d'un pays : accepté)."""
    out, lines, i = [], body.splitlines(), 0
    while i < len(lines):
        m = re.match(r"^(:{3,})\{admonition\}", lines[i].strip())
        if m and any("rh-country" in l for l in lines[i + 1:i + 4]):
            fence = m.group(1)
            i += 1
            while i < len(lines) and lines[i].strip() != fence:
                i += 1
            i += 1
            continue
        out.append(lines[i])
        i += 1
    text = "\n".join(out)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)       # images
    text = re.sub(r"\]\([^)]*\)", "]", text)                 # cibles de liens
    return text


def check_modules(rel, meta):
    """La page déclare ce qu'elle documente ; sa place doit suivre le code."""
    if "modules" not in meta:
        errors.append(f"{rel}: pas de `modules:` en front-matter (liste des modules "
                      f"documentés, `[]` pour une page de navigation)")
        return
    mods = meta["modules"] or []
    unknown = [m for m in mods if m not in MODULES]
    for m in unknown:
        errors.append(f"{rel}: module inconnu `{m}` (absent de docs-ops/modules.json)")
    mods = [m for m in mods if m in MODULES]
    for m in mods:
        documented.setdefault(m, []).append(rel)
        if MODULES[m]["suite"] not in SITE_SUITES:
            errors.append(f"{rel}: `{m}` relève de la suite « {MODULES[m]['suite']} », "
                          f"pas de ce site")
    space = COUNTRY_SPACES.get(rel.split("/", 1)[0])
    if space is None:
        for m in mods:
            if MODULES[m]["countries"] and (rel, m) in DEBT:
                debt_seen.add((rel, m))
                warnings.append(f"{rel}: `{m}` ({DEBT[(rel, m)]}) — dette connue, "
                                f"docs-ops/placement-debt.txt")
            elif MODULES[m]["countries"]:
                errors.append(f"{rel}: page commune, mais `{m}` est lié à "
                              f"{'/'.join(MODULES[m]['countries'])} → espace pays, "
                              f"ou le module neutre qui porte vraiment l'écran")
    elif mods and not any(space in MODULES[m]["countries"] for m in mods):
        errors.append(f"{rel}: page de l'espace {space}, mais aucun de ses modules "
                      f"n'est lié à {space} ({', '.join(mods)})")


def coverage_report():
    """docs-ops/coverage.md : par cellule suite × pays, les modules sans page."""
    cells = {}
    for name, m in sorted(MODULES.items()):
        if m["suite"] not in SITE_SUITES:
            continue
        key = (m["suite"], ", ".join(m["countries"]) or "neutre")
        cells.setdefault(key, []).append(name)
    out = ["# Couverture de la documentation par module", "",
           "Généré par `python check_docs.py --coverage` depuis `docs-ops/modules.json`",
           "et le front-matter `modules:` des pages. Ne pas éditer à la main.", "",
           "| Suite | Pays | Modules | Documentés | Sans page |",
           "| --- | --- | ---: | ---: | --- |"]
    total = done = 0
    for (suite, country), names in sorted(cells.items()):
        missing = [n for n in names if n not in documented]
        total += len(names); done += len(names) - len(missing)
        miss = ", ".join(f"`{n}`" + (" (app)" if MODULES[n]["application"] else "")
                         for n in missing) or "—"
        out.append(f"| {suite} | {country} | {len(names)} | {len(names) - len(missing)} | {miss} |")
    out += ["", f"**{done} / {total} modules documentés.**", ""]
    (CONTENT.parent / "docs-ops" / "coverage.md").write_text("\n".join(out), encoding="utf-8")
    print(f"couverture : {done}/{total} modules documentés → docs-ops/coverage.md")


def check(page, text):
    rel = page.relative_to(CONTENT).as_posix()
    lines = text.splitlines()

    # front-matter éventuel
    body = text
    meta = {}
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end:
            fm = "\n".join(lines[1:end])
            for k in ("title:", "description:", "faq:"):
                if re.search(rf"^{k}", fm, re.M):
                    errors.append(f"{rel}: `{k}` en front-matter → doit être un titre H1 / directive rh-*")
            meta = yaml.safe_load(fm) or {}
            body = "\n".join(lines[end + 1:])
    check_modules(rel, meta)
    check_menu_paths(rel, body)

    h1 = re.findall(r"^# .+", body, re.M)
    if len(h1) == 0:
        errors.append(f"{rel}: pas de titre H1 (`# …`)")
    elif len(h1) > 1:
        errors.append(f"{rel}: {len(h1)} titres H1 (un seul attendu)")

    if "{rh-description}" not in body:
        errors.append(f"{rel}: pas de bloc :::{{rh-description}} (meta/JSON-LD)")

    if re.search(r"^!!!\s", body, re.M):
        errors.append(f"{rel}: admonition MkDocs `!!!` non convertie (→ :::{{note}})")
    if 'class="grid cards"' in body:
        errors.append(f"{rel}: `grid cards` MkDocs non converti")
    if "&lt;!--" in body or "--&gt;" in body:
        errors.append(f"{rel}: entités HTML échappées (`&lt;!--` / `--&gt;`)")

    if rel.split("/", 1)[0] not in COUNTRY_SPACES:
        for n, line in enumerate(_without_country_blocks(body).splitlines(), 1):
            for m in COUNTRY_TERMS.finditer(line):
                errors.append(f"{rel}: terme propre à un pays `{m.group(1)}` dans une page "
                              f"commune → espace pays ou encadré rh-country-be "
                              f"(« {line.strip()[:70]} »)")

    for m in re.finditer(r"\]\(([^)]+\.md)#([\w-]+)\)", body):
        errors.append(f"{rel}: lien ancré cross-fichier `{m.group(1)}#{m.group(2)}` "
                      f"→ casse en FR/NL (lier au niveau page)")


def main():
    # Console Windows (cp1252) : les messages contiennent « → » et des accents.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    # Les .md sous assets/ sont des notes internes (conventions de prise de vue),
    # pas des pages : conf.py les exclut aussi du build.
    pages = [p for p in sorted(CONTENT.rglob("*.md"))
             if "assets" not in p.relative_to(CONTENT).parts]
    for p in pages:
        check(p, p.read_text(encoding="utf-8"))
    if "--coverage" in sys.argv:
        coverage_report()
    # Une dette soldée doit quitter le fichier : sinon le cliquet se desserre.
    for key in sorted(set(DEBT) - debt_seen):
        errors.append(f"{key[0]}: `{key[1]}` n'est plus en défaut → retirer sa ligne "
                      f"de docs-ops/placement-debt.txt")
    print(f"check_docs : {len(pages)} pages contrôlées, {len(errors)} problème(s), "
          f"{len(warnings)} dette(s) de placement connue(s).")
    for w in warnings:
        print("  [~]", w)
    for e in errors:
        print("  [X]", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
