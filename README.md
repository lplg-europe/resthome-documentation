# Documentation Resthome (publique)

Documentation **utilisateur** du logiciel **Resthome** (maisons de repos et de
soins MR/MRS), éditée par **LPLG**. Site généré avec **Sphinx** (thème
sphinx-immaterial), sur le **modèle Odoo** : **source unique en anglais** dans
`content/`, traductions **FR / NL** par catalogues gettext (`locale/`),
**multi-version** (`/documentation/<version>/…`).

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour le cycle de travail et les conventions.

> **Public vs privé.** Ce dépôt est **public** et ne contient **que** la
> documentation destinée aux clients. Toute la documentation **technique** et
> la **propriété intellectuelle** de l'éditeur restent **privées** et ne sont
> pas publiées ici. Ne jamais copier de contenu interne dans ce dépôt.

## Prérequis

- Python 3.10 ou plus.

## Aperçu en local

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
# source .venv/bin/activate       # Linux / macOS
pip install -r requirements.txt
python build_docs.py              # ./site (FR racine, /nl, /en) + statiques + sitemap
python -m http.server 8000 --directory site
```

Ouvrez **http://127.0.0.1:8000/2026/** (le `/` sans version redirige vers la
dernière). Édition rapide d'une langue avec rechargement auto :

```bash
sphinx-autobuild -c . content _build/live
```

## Traductions (catalogues gettext)

```bash
python build_docs.py --gettext    # (ré)extrait les POT + met à jour locale/{fr,nl}
```

Traduire ensuite les `.po` (ou via l'outillage de seed), puis rebuild.

## Contrôle avant push

```bash
python build_docs.py              # doit finir « 0 warning »
python check_docs.py              # conventions (H1, rh-description, résidus)
```

## Déploiement

Push sur `main` → GitHub Actions (`.github/workflows/build.yml`) construit avec
`build_docs.py` et publie `./site` sur GitHub Pages (`docs.lplg.eu`), servi sous
`www.lplg.eu/resthome/documentation/` via le Worker Cloudflare.

## Structure

```
docs/
├── assets/          # logo, CSS
├── llms.txt         # index « pour IA » (voir plus bas)
├── fr/              # documentation en français (langue par défaut)
└── nl/              # documentation en néerlandais (miroir de fr/)
```

- Chaque page FR a son équivalent **au même chemin** dans `nl/`
  (ex. `fr/premiers-pas.md` ↔ `nl/premiers-pas.md`).
- La navigation est définie une seule fois dans `mkdocs.yml` (`nav:`), les
  titres NL sont traduits via `nav_translations`.

## Rendre la doc « lisible par les IA »

Deux niveaux, déjà prévus :

1. **`llms.txt` statique** — un index Markdown listant les pages, présent dès
   maintenant dans `docs/llms.txt` (servi sur `/llms.txt`). C'est la convention
   [llmstxt.org](https://llmstxt.org/) : les assistants IA le lisent pour
   répondre aux questions des clients.
2. **Génération automatique** (optionnel) — pour garder `llms.txt` synchronisé
   avec le contenu, activez le plugin déjà installé en ajoutant dans
   `mkdocs.yml` :

   ```yaml
   plugins:
     - llmstxt:
         markdown_description: Documentation utilisateur du logiciel Resthome (MR/MRS).
         sections:
           Documentation:
             - fr/index.md
             - fr/premiers-pas.md
             - fr/residents/gerer-un-resident.md
             - fr/facturation/index.md
             - fr/ehealth/index.md
   ```

   (Placez-le **après** le plugin `i18n`. Supprimez alors le `docs/llms.txt`
   manuel pour éviter le doublon.)

Un bouton **« Poser une question »** (RAG sur cette doc) pourra être ajouté plus
tard — le Markdown de ce dépôt est la source idéale.

## Contribuer

- Écrivez en **Markdown**.
- Toute nouvelle page FR doit avoir sa **traduction NL au même chemin**.
- Ajoutez la page à `nav:` dans `mkdocs.yml` (et son titre NL dans
  `nav_translations`).
- Encadrés : `!!! note`, `!!! tip`, `!!! warning` (voir les pages existantes).

## Licence

Documentation sous licence **CC BY 4.0** (voir `LICENSE`).
