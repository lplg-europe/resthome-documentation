# Contribuer à la documentation Resthome

Doc **modèle Odoo** : source unique en **anglais** dans `content/` (MyST Markdown,
Sphinx), traductions FR/NL par **catalogues gettext** (`locale/`). On écrit et on
relit **une seule langue** ; FR et NL sont générés.

## Cycle de travail

1. Éditer / créer une page dans `content/` (en anglais).
2. `python build_docs.py --gettext` → met à jour les catalogues `locale/{fr,nl}`.
3. Traduire les nouvelles chaînes dans les `.po` (ou via l'outillage de seed).
4. `python build_docs.py` → construit `site/` (FR racine, `/nl`, `/en`) + statiques + sitemap.
5. Pousser sur `main` → la CI publie sur GitHub Pages (`docs.lplg.eu`).

> Ne **jamais** éditer `docs/fr` / `docs/nl` : ce sont d'anciennes références de
> traduction (MkDocs retiré). La source, c'est `content/` + les catalogues.

## Structure d'une page (repris d'Odoo)

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
- **Pas de flèches/rectangles** en surimpression : recadrer et légender.
- Fichiers en **minuscules-avec-traits-d'union**, rangés sous `content/assets/…`.
- Placeholder tant que la capture manque : `<!-- screenshot to add: … -->`.

## Contrôle avant push

```bash
python build_docs.py          # doit finir « 0 warning »
python check_docs.py          # conventions (H1, rh-description, résidus MkDocs)
```
