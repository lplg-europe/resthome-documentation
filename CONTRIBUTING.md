# Contribuer à la documentation Resthome

Doc **modèle docs-as-code** : source unique en **anglais** dans `content/` (MyST Markdown,
Sphinx), traductions FR/NL par **catalogues gettext** (`locale/`). On écrit et on
relit **une seule langue** ; FR et NL sont générés.

## Cycle de travail

1. Éditer / créer une page dans `content/` (en anglais).
2. `python build_docs.py --gettext` → met à jour les catalogues `locale/{fr,nl}`.
3. Traduire les nouvelles chaînes dans les `.po` (ou via l'outillage de seed).
4. `python build_docs.py` → construit `site/` (FR racine, `/nl`, `/en`) + statiques + sitemap.
5. Pousser sur `main` → la CI publie sur GitHub Pages (`docs.lplg.eu`).

> La source unique, c'est `content/` (anglais, MyST) + les catalogues de
> traduction `locale/{fr,nl}/LC_MESSAGES/`. L'ancien arbre MkDocs `docs/` a été
> retiré. `_publish/llms-full.txt` est régénéré automatiquement au build depuis
> le site FR construit (ne pas l'éditer à la main).

## Structure d'une page

- **H1** = le titre de la page — orienté **métier**, pas marketing.
- **Paragraphe d'intro** juste après le H1 : confirme au lecteur qu'il est au bon
  endroit. En parallèle, un bloc `:::{rh-description}` (1 phrase) alimente la
  meta description + le JSON-LD.
- **Premier H2** = configuration / prérequis quand il y en a.
- **H2 suivants** = les actions / fonctionnalités principales ; H3 = sous-détails.
- Bloc `:::{rh-faq}` (liste de définitions Q/R) → schema FAQPage.
- Front-matter `howto_auto: true` si la page est une procédure à étapes numérotées
  (`## 1. …`, `## 2. …`) → schema HowTo automatique.

## Titres

- **Concis** : pas de phrases, pas de questions, pas de « comment… ».
- **Casse de phrase** (sentence case) : majuscule au premier mot et aux noms
  propres uniquement. Convertir les libellés tout en majuscules.
- Éviter les pronoms (« vous / votre ») dans les titres. Les verbes d'action sont OK.

## Ton et voix

- **Présent** pour décrire et instruire ; futur seulement pour un événement différé.
- **Impératif** : « Cliquez sur **Générer** », pas « Vous pouvez cliquer… ».
- Informer, pas vendre : zéro langage marketing.
- **Cohérence** : reprendre le ton et les termes des pages existantes.

## Libellés d'interface

- Écrire les **libellés d'app exactement comme ils apparaissent** (boutons,
  onglets, statuts) — ex. l'onglet **Convention**, les états **Draft / Generated /
  Invoiced / Closed**.
- Termes belges/techniques conservés : INAMI, MDA, eFact, eAgreement, Katz, MR/MRS,
  NISS, AViQ, WalCareNet, codes réponse (931000…), **pseudo-codes** (jamais
  « codes INAMI »), Annexes.
- Règle métier : le **forfait de dépendance = même montant pour toutes les
  catégories Katz** (tarifs AViQ, O incluse) — la catégorie sert à déclarer le profil.

## Listes

- **Numérotée** = séquence où l'ordre compte (procédures). **À puces** = éléments
  non ordonnés (options, champs).
- Point final seulement si l'item est une phrase complète.

## Admonitions

`:::{note}`, `:::{tip}`, `:::{warning}`, `:::{admonition} Titre` + `:class: …`.
Réserver aux mises en garde / astuces utiles, sans en abuser.

## Liens et références

- Ne pas dupliquer : **référencer** une page existante en lien relatif
  `[texte](../section/page.md)`.
- ⚠️ **Ancres cross-langue interdites** : `page.md#une-ancre` casse en FR/NL (MyST
  régénère l'ancre depuis le titre traduit). Lier au niveau **page**, ou utiliser
  une cible explicite + `{ref}`.
- **Renommer / supprimer une page** → ajouter la redirection dans `redirects.txt`
  (`ancien nouveau`). On ne perd jamais une URL indexée.

## Images et captures

- **Largeur 768–933 px** (pas de plein écran). **Compresser** les PNG/WebP.
- **Texte alt** = une phrase décrivant l'action, non répétitive.
- **Annotations** uniquement celles de l'outil de capture : pastilles numérotées
  (le numéro = l'étape de la page), encadré bleu sur ce qu'il faut lire, curseur
  sur le bouton à cliquer. Jamais de rouge (il veut dire « erreur » à l'écran),
  jamais de flèche ou de rectangle dessiné à la main : recadrer et légender.
- Fichiers en **minuscules-avec-traits-d'union**, rangés sous `content/assets/…`.
- Placeholder tant que la capture manque : `<!-- screenshot to add: … -->`.

## Pays : pages communes et espaces pays

La documentation sert **plusieurs pays** sur **un seul site** : une URL par page
et par langue, quel que soit le pays (pas de page dupliquée par pays).

- **Pages communes** (tout ce qui n'est pas sous un espace pays) : valables
  partout, en termes neutres — « dependency category », « national
  identification number », « the resident's health insurer », « the care
  allowance paid by the health insurer ». Jamais de Katz, NISS, INAMI, MR/MRS,
  eFact, MDA, AViQ, CPAS… dans une page commune.
- **Espaces pays** : `content/belgique/`, `content/france/`,
  `content/luxembourg/`. Tout ce qui vient des règles d'un pays y vit, avec les
  termes du pays (ceux listés plus haut sous « Libellés d'interface »).
- **Renvoi depuis une page commune** : un encadré par sujet, qui ne s'affiche
  que pour le pays choisi :

  ```
  :::{admonition} In Belgium
  :class: rh-country rh-country-be

  What Belgium adds here, in one or two sentences: see [The Katz assessment](../belgique/katz.md).
  :::
  ```

- **Sélecteur de pays** (en-tête) : `_ext/countries.py` + `_static/rh-country.js`.
  La barre latérale ne montre que les groupes communs et celui du pays choisi ;
  sur une page d'un espace pays, le pays est celui de la page.
- **Ajouter un pays** : une entrée dans `rh_countries` (`conf.py`, `status:
  "soon"` tant que l'espace est vide), un dossier `content/<espace>/index.md`,
  un toctree `:caption:` à son nom dans `content/index.md`, son drapeau
  (`FLAGS` de `_ext/countries.py`, `#__nav_N_label` et `.rh-country-<code>` de
  `_static/resthome-brand.css`).
- ⚠️ Les icônes de la barre latérale sont **positionnelles** (`#__nav_3_5` = 5e
  entrée du 3e groupe) : réordonner un toctree de `content/index.md` impose de
  revoir `_static/resthome-brand.css`.

## Modules documentés : la doc suit le graphe du code

La documentation est une **projection du code** : produit WideCare = socle
(`healthcare_*`) + une **suite** métier (Resthome aujourd'hui ; dentaire,
hôpital, logopédie… demain) + un **pack pays** (`l10n_health_<pays>`).
Cible : **un site par suite** ; le pays reste le sélecteur de l'en-tête.

- Chaque page déclare en front-matter les modules dont elle décrit
  l'interface ou le comportement — le module qui DÉFINIT l'écran, pas ceux qui
  en dépendent :

  ```
  ---
  modules: [resthome_day_care, healthcare_accommodation_billing]
  ---
  ```

  `modules: []` seulement pour une page de navigation (accueil, FAQ, glossaire).
- La suite et le pays d'une page ne s'écrivent pas : ils se **calculent** depuis
  `docs-ops/modules.json`, un instantané du graphe (nom, suite, pays,
  application — rien d'autre, ce dépôt est public). Le régénérer après un
  changement de modules :

  ```bash
  python docs-ops/sync-modules.py ../widecare-odoo/resthome-odoo
  ```

- `check_docs.py` refuse une page sans `modules:`, un module inconnu, et une
  page **mal placée** : page commune qui documente un module lié à un pays,
  page d'espace pays sans module de ce pays.
- `python check_docs.py --coverage` écrit `docs-ops/coverage.md` : par cellule
  suite × pays, les modules qu'aucune page ne documente.

## Contrôle avant push

```bash
python build_docs.py          # doit finir « 0 warning »
python check_docs.py --coverage   # conventions, termes pays, placement vs modules, couverture
```
