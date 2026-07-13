# Documentation Resthome (publique)

Documentation **utilisateur** du logiciel **Resthome** (maisons de repos et de
soins MR/MRS), éditée par **LPLG**. Site généré avec
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), bilingue
**Français / Néerlandais**.

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
mkdocs serve
```

Ouvrez http://127.0.0.1:8000 — la page se recharge à chaque modification.

## Construire le site statique

```bash
mkdocs build          # génère le dossier ./site
```

Le contenu de `./site` est un site 100 % statique (HTML/CSS/JS), déployable
n'importe où.

## Déploiement sur `www.lplg.eu/resthome/documentation`

L'URL cible est un **sous-chemin** (pas un sous-domaine). `site_url` est déjà
réglé sur cette adresse dans `mkdocs.yml` pour que la recherche et les liens
soient corrects.

- **Serveur web (Nginx/Apache)** : copiez `./site` vers le dossier servi à ce
  chemin, ou ajoutez une `location /resthome/documentation/ { ... }` qui pointe
  vers ces fichiers statiques.
- **Cloudflare Pages / Netlify** : possible aussi, avec une règle de proxy
  depuis `www.lplg.eu/resthome/documentation` vers le déploiement.

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
