---
title: Réglages des documents
description: "Configurer la centralisation des documents résidents en maison de repos (MR/MRS) — dossier racine, tags par défaut, rangement automatique dans l'app Documents."
faq:
  - q: "Où se trouvent les réglages de centralisation des documents ?"
    a: "Dans « Réglages > Documents > Centralisation des fichiers », bloc « Maison de repos ». Ce bloc n'apparaît que lorsque l'app Documents est installée."
  - q: "Que fait exactement la centralisation des documents résidents ?"
    a: "Quand elle est activée, chaque pièce jointe déposée sur la fiche d'un résident (fil de discussion) est automatiquement rangée dans le dossier personnel de ce résident, dans l'app Documents. Vous retrouvez ainsi toutes les pièces d'un résident au même endroit, sans classement manuel."
  - q: "Dois-je créer le dossier racine « Résidents » moi-même ?"
    a: "Non. Resthome crée automatiquement le dossier racine « Résidents » (avec un sous-dossier « Formulaires vierges ») dès la création de la société. Le champ « Dossier racine » pointe déjà dessus ; vous n'avez rien à préparer."
  - q: "À quoi servent les tags par défaut ?"
    a: "C'est optionnel. Les étiquettes choisies sont appliquées automatiquement aux documents centralisés, ce qui facilite ensuite la recherche et le filtrage dans l'app Documents. Vous pouvez laisser ce champ vide."
  - q: "Puis-je désactiver la centralisation ?"
    a: "Oui, en décochant le bloc « Maison de repos ». Les documents déjà rangés restent dans les dossiers résidents ; seules les futures pièces jointes ne sont plus centralisées automatiquement."
  - q: "Le réglage est-il commun à tous mes établissements ?"
    a: "Non. Il est propre à chaque société (établissement) de la base. Chaque société a son propre dossier racine « Résidents » et son propre paramétrage, ce qui garde les dossiers cloisonnés."
---

# Réglages des documents

L'onglet **Réglages > Documents** rassemble les paramètres de l'app **Documents**
d'Odoo. Resthome y ajoute, dans la section **Centralisation des fichiers**, un bloc
**Maison de repos** qui **range automatiquement** les pièces jointes de vos résidents
dans leur **dossier personnel**. Vous trouvez ces réglages dans **Réglages > Documents
> Centralisation des fichiers**.

!!! info "Prérequis"
    Ces réglages n'apparaissent que si l'application **Documents** est installée. Le
    dossier racine des résidents est créé automatiquement — vous n'avez rien à préparer
    avant d'activer la centralisation.

## Centralisation des documents résidents

Le bloc **Maison de repos** contrôle le rangement automatique des documents. Une case
active la centralisation ; une fois cochée, elle révèle le **dossier racine** et les
**tags par défaut**.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Maison de repos** (centralisation) | Active le rangement automatique : chaque pièce jointe déposée sur la fiche d'un résident est classée dans son dossier personnel de l'app Documents. | **Activé** (coché) |
| **Dossier racine** | Le dossier de l'app Documents sous lequel Resthome range tous les dossiers résidents. | Dossier **« Résidents »** (créé automatiquement) |
| **Tags par défaut** | Les étiquettes appliquées automatiquement aux documents centralisés, pour les retrouver et les filtrer. | **Optionnel** — laissez vide, ou choisissez 1 à 2 tags |

!!! tip "Le dossier racine est créé pour vous"
    À la création de la société, Resthome crée automatiquement le dossier **« Résidents »**
    (avec un sous-dossier **« Formulaires vierges »** pour vos modèles). Le champ
    **Dossier racine** pointe déjà dessus. Il n'y a normalement pas de raison de le
    changer ; ne le modifiez que si vous rangez volontairement les résidents ailleurs.

## Un dossier par résident

Vous ne créez pas les dossiers à la main. À l'admission d'un résident (ou à l'activation
de sa fiche résident), Resthome crée son **dossier personnel** sous le dossier racine,
avec trois sous-dossiers prêts à l'emploi :

- **Documents médicaux**
- **Documents administratifs**
- **Documents de facturation**

Le dossier porte le **nom du résident** et se renomme automatiquement si le nom change.
Le bouton **Documents** sur la fiche du résident ouvre directement ce dossier (le
compteur inclut les pièces des sous-dossiers).

!!! note "Cloisonné par établissement"
    En multi-société, **chaque société a son propre dossier racine** « Résidents ». Le
    réglage est **propre à chaque établissement** : activez la centralisation dans chacun
    d'eux si vous exploitez plusieurs maisons.

## Tags par défaut (optionnel)

Les **tags** (étiquettes) servent à catégoriser et retrouver les documents. Resthome
fournit déjà une liste d'étiquettes prêtes à l'emploi — par exemple **Katz**, **Fin de
séjour**, **eAgreement**, **OA**, **Convention**, **Formulaire médical**, **Facturation**,
**CPAS**, **RGPD**. Dans **Tags par défaut**, vous choisissez celles qui seront appliquées
**automatiquement** à chaque document centralisé.

!!! tip "Commencez léger"
    Laissez ce champ **vide** au démarrage, ou mettez-y un seul tag générique. Vous
    pourrez toujours étiqueter finement chaque document a posteriori dans l'app Documents.

## Désactiver la centralisation

Décocher le bloc **Maison de repos** **arrête** le rangement automatique des futures
pièces jointes. Les documents déjà classés dans les dossiers résidents **restent en
place** — rien n'est supprimé ni déplacé.

## Pour aller plus loin

- [Configuration](index.md)
- [Gérer un résident](../residents/gerer-un-resident.md)
- [FAQ](../faq.md) · [Glossaire](../glossaire.md)
