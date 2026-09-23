#!/usr/bin/env python3
"""sync-modules.py — instantané du graphe des modules, pour la documentation.

La doc est une PROJECTION du code : chaque page déclare les modules qu'elle
documente (front-matter `modules:`), et sa suite comme son pays se DÉDUISENT
de ces modules — rien n'est étiqueté à la main.

Le code (dépôt privé) n'est pas lisible par la CI de ce dépôt public : on
commite donc ici un instantané, `docs-ops/modules.json`, régénéré à la main ou
par la CI du dépôt Odoo :

    python docs-ops/sync-modules.py ../widecare-odoo/resthome-odoo

Ce qu'il contient, par module (rien de plus — ce dépôt est public) :
  name         libellé affiché dans Applications
  suite        "platform" (socle WideCare) ou la suite métier (ex. "resthome")
  countries    pays dont le module dépend, [] = neutre
  application  True si le module est une application (tuile du menu)

Règles de calcul :
  - pays  = les packs `l10n_health_<cc>` atteints par la fermeture des
            dépendances (un module belge l'est parce qu'il dépend du pack belge) ;
  - suite = la catégorie `Healthcare/<Suite>` du module lui-même, sinon celle
            d'un module dont il dépend (un connecteur pays qui dépend de la
            suite Resthome n'a de sens qu'avec elle) ; « platform » sinon.
"""
import ast
import json
import sys
from functools import lru_cache
from pathlib import Path

OUT = Path(__file__).resolve().parent / "modules.json"
# Catégories qui ne désignent PAS une suite métier.
NOT_A_SUITE = {"Localization", "Belgium", ""}


def main(src):
    src = Path(src)
    manifests = {m.parent.name: ast.literal_eval(m.read_text(encoding="utf-8"))
                 for m in sorted(src.glob("*/__manifest__.py"))}
    if not manifests:
        sys.exit(f"aucun __manifest__.py sous {src}")

    def own_suite(name):
        cat = manifests[name].get("category", "")
        if cat.startswith("Healthcare/"):
            suite = cat.split("/", 1)[1]
            return None if suite in NOT_A_SUITE else suite.lower()
        return None

    @lru_cache(None)
    def closure(name):
        seen = {name}
        for dep in manifests[name].get("depends", []):
            if dep in manifests:
                seen |= closure(dep)
        return frozenset(seen)

    out = {}
    for name, man in manifests.items():
        if not man.get("installable", True):
            continue
        deps = closure(name)
        countries = sorted({d.split("_")[2] for d in deps
                            if d.startswith("l10n_health_") and len(d.split("_")) >= 3})
        suites = sorted({s for s in (own_suite(d) for d in deps) if s})
        if len(suites) > 1:
            print(f"  ! {name} relève de plusieurs suites {suites} : à trancher", file=sys.stderr)
        out[name] = {
            "name": man.get("name", name),
            "suite": suites[0] if suites else "platform",
            "countries": countries,
            "application": bool(man.get("application", False)),
        }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                   encoding="utf-8")
    write_menus(src, manifests)
    cells = {}
    for m in out.values():
        k = (m["suite"], ",".join(m["countries"]) or "neutral")
        cells[k] = cells.get(k, 0) + 1
    print(f"{len(out)} modules → {OUT.name}")
    for (suite, c), n in sorted(cells.items()):
        print(f"  {suite:10s} × {c:8s} {n:3d}")


MENUS = Path(__file__).resolve().parent / "menus.json"


def write_menus(src, manifests):
    """docs-ops/menus.json : l'arbre des menus, pour vérifier les chemins
    « **A → B → C** » cités par la doc.

    Un menu peut être renommé ou déplacé par un autre module (le pack belge
    renomme la racine en « Nursing Home ») ou déplacé selon les modules
    installés (la norme de personnel CSJ passe de Billing à Forfait) : on garde
    TOUS ses noms et TOUS ses parents. Par menu : {"names": [...], "parents": [...]}.
    Les libellés d'interface sont publics : rien d'autre n'est exporté."""
    import xml.etree.ElementTree as ET

    menus = {}

    def full(ref, module):
        return ref if "." in ref else f"{module}.{ref}"

    def add(mid, name=None, parent=None):
        m = menus.setdefault(mid, {"names": [], "parents": []})
        if name and name not in m["names"]:
            m["names"].append(name)
        if parent and parent not in m["parents"]:
            m["parents"].append(parent)

    def walk(el, module, parent=None):
        for child in el:
            if child.tag == "menuitem" and child.get("id"):
                mid = full(child.get("id"), module)
                par = child.get("parent")
                add(mid, child.get("name"), full(par, module) if par else parent)
                walk(child, module, mid)          # menuitems imbriqués
            elif child.tag == "record" and child.get("model") == "ir.ui.menu":
                mid = full(child.get("id"), module)
                name = parent_ref = None
                for f in child.findall("field"):
                    if f.get("name") == "name":
                        name = (f.text or "").strip() or None
                    elif f.get("name") == "parent_id" and f.get("ref"):
                        parent_ref = full(f.get("ref"), module)
                add(mid, name, parent_ref)
            else:
                walk(child, module, parent)

    for module in manifests:
        for xml in sorted((src / module).rglob("*.xml")):
            try:
                root = ET.parse(xml).getroot()
            except ET.ParseError:
                continue
            walk(root, module)
    menus = {k: v for k, v in menus.items() if v["names"] or v["parents"]}
    MENUS.write_text(json.dumps(menus, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                     encoding="utf-8")
    print(f"{len(menus)} menus → {MENUS.name}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../widecare-odoo/resthome-odoo")
