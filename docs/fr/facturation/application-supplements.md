---
title: L'application Suppléments
description: "L'application Suppléments d'une maison de repos (MR/MRS) : saisie multi-résidents via le catalogue, suppléments ponctuels ou récurrents, conventions, catalogue et reporting."
faq:
  - q: "À quoi sert l'application Suppléments dans une maison de repos (MR/MRS) ?"
    a: "C'est l'écran dédié à la saisie des suppléments : ouvrir le catalogue d'un résident, en ajouter à plusieurs résidents à la fois, gérer les conventions récurrentes, tenir le catalogue des suppléments et suivre les montants facturés."
  - q: "Comment ajouter un supplément à plusieurs résidents en une fois ?"
    a: "Sur l'écran Résidents, sélectionnez plusieurs résidents (Ctrl+clic sur ordinateur, appui long sur tablette, ou le bouton « Sélection multiple »), puis cliquez sur « Suppléments (N) ». Un seul catalogue s'ouvre et chaque supplément ajouté est répercuté sur l'enveloppe ouverte de chaque résident sélectionné."
  - q: "Quelle différence entre un supplément ponctuel et une convention ?"
    a: "Un supplément ponctuel est facturé une seule fois sur l'enveloppe du mois (coiffeur, boisson…). Une convention regroupe les suppléments récurrents du résident (chambre individuelle, TV, téléphone) : elle vit sur le résident et survit à une clôture de séjour, un changement de chambre ou un transfert."
  - q: "Où définir la liste des suppléments et leurs prix ?"
    a: "Dans Configuration → Catalogue. Chaque supplément a un type (journalier, mensuel ou ponctuel), un prix propre à l'établissement et, si nécessaire, un code AViQ pour la déclaration à l'organisme assureur."
  - q: "Puis-je suivre les suppléments facturés par résident ou par mois ?"
    a: "Oui, via le menu Reporting : des vues graphique, tableau croisé et liste répartissent les suppléments facturés par résident, par produit et par mois."
---

# L'application Suppléments

L'application **Suppléments** est l'écran dédié à la saisie et à la gestion des
suppléments des résidents. Elle rassemble en un seul endroit ce qui, autrement,
se répartit entre la fiche résident et la période de facturation : ouvrir le
catalogue d'un résident, en ajouter à plusieurs résidents à la fois, gérer les
conventions récurrentes, tenir le catalogue et suivre les montants facturés.

Vous la trouvez dans le **menu principal → application Suppléments**.

!!! info "Cette page complète « Les suppléments »"
    Les notions de base — l'**enveloppe de suppléments** par résident et par mois,
    la **synchronisation automatique** de la facture, la protection quand un mois
    est déjà comptabilisé — sont expliquées dans
    [Les suppléments](supplements.md). Cette page-ci décrit l'**application
    dédiée** et ses raccourcis de saisie. L'application ne crée aucune donnée
    parallèle : elle agit sur les mêmes enveloppes et les mêmes conventions.

<!-- capture a ajouter : l'application Suppléments ouverte sur l'écran Résidents (vue kanban) -->

## L'écran Résidents (le point de départ)

À l'ouverture, l'application affiche l'écran **Résidents** : la liste des
résidents actifs, en **vue kanban** (cartes) ou en **vue liste**. Chaque carte
montre la photo, le nom, la **chambre** et le **type de séjour** (MR / MRS), avec
une icône de panier « Ajouter des suppléments ».

- **Cliquez sur un résident** : Resthome ouvre directement le **catalogue** de son
  enveloppe de suppléments du mois en cours. Vous atterrissez sur la grille
  d'ajout, sans passer par la fiche.
- En **vue liste**, chaque ligne porte un bouton **Ajouter des suppléments**, et
  l'en-tête un bouton **Ajouter via le catalogue** pour agir sur les résidents
  cochés.

!!! tip "Filtrer et regrouper"
    La barre de recherche filtre par **MR** / **MRS** et regroupe par **chambre**
    ou par **type de séjour** — utile pour repérer rapidement une aile ou un
    étage avant une saisie groupée.

## Ajouter des suppléments à plusieurs résidents

C'est le raccourci central de l'application : appliquer le même supplément à
plusieurs résidents sans rouvrir chaque fiche.

1. Sur l'écran **Résidents**, **sélectionnez plusieurs résidents** :
   - **Ctrl+clic** (ou Cmd+clic) sur ordinateur ajoute/retire un résident ;
     **Maj+clic** étend la sélection à une plage ;
   - **appui long** sur tablette tactile ;
   - ou activez le bouton **Sélection multiple**, qui fait sélectionner au simple
     clic.
2. Cliquez sur le bouton **Suppléments (N)** qui apparaît (N = nombre de résidents
   sélectionnés). En vue liste, utilisez **Ajouter via le catalogue**.
3. **Un seul catalogue** s'ouvre. Chaque supplément que vous y ajoutez, modifiez
   ou retirez est **répercuté sur l'enveloppe ouverte de chaque résident
   sélectionné**, pour le mois en cours.

Dans ce catalogue partagé, le panneau de gauche affiche une section
**Résidents** : les résidents concernés apparaissent sous forme d'étiquettes (le
résident « pilote » en gris, les autres en vert). Le lien **Ajouter** permet d'en
ajouter d'autres à la volée ; supprimer une étiquette retire le résident (le
dernier ne peut pas être retiré).

<!-- capture a ajouter : le catalogue multi-résidents avec la section Résidents (étiquettes) à gauche -->

!!! note "Un supplément déjà couvert par une convention est ignoré"
    Si l'un des résidents sélectionnés a déjà ce produit dans une **convention
    active**, la ligne n'est **pas** ajoutée pour lui (elle serait de toute façon
    écartée à la facturation) — les autres résidents la reçoivent normalement.
    Pour une saisie sur un seul résident, Resthome bloque carrément l'ajout et
    vous invite à passer par la convention.

## Suppléments ponctuels et récurrents

L'application distingue les deux natures de suppléments déjà présentées dans
[Les suppléments](supplements.md).

- **Ponctuels** — ajoutés à l'enveloppe du mois via le catalogue (coiffeur,
  pédicure, boisson, téléphone…). Le menu **Suppléments ponctuels** en donne la
  **liste**, regroupée par résident, avec la période, le produit, la quantité, le
  prix et le total. C'est l'endroit pour relire tout ce qui a été saisi à la main
  sur le mois.
- **Récurrents** — reconduits chaque mois via une **convention** (voir la section
  suivante).

<!-- capture a ajouter : le menu Suppléments ponctuels, liste groupée par résident -->

!!! tip "Où est passé mon supplément ?"
    À chaque ajout, Resthome affiche une notification indiquant **sur quelle(s)
    période(s)** le supplément a été facturé — ou vous prévient qu'**aucune
    période ouverte** ne correspond encore à sa date (il ne sera alors facturé que
    lorsque le mois concerné sera généré). Vérifiez la **date de début** si le
    supplément n'apparaît pas où vous l'attendiez.

## Les conventions de suppléments

Une **convention** regroupe les suppléments **récurrents** d'un résident (chambre
individuelle, TV, téléphone…). Elle vit sur le **résident**, pas sur le séjour :
elle **survit** à une clôture de séjour, un changement de chambre ou un transfert
MR ↔ MRS. Chaque résident a **une seule** convention, qui rassemble toutes ses
lignes récurrentes.

Dans l'application, le menu **Conventions** liste les lignes de suppléments
récurrents (résident, convention, produit, type, dates, quantité, actif). La
convention elle-même — avec son statut et ses boutons — se gère depuis
l'application **MR/MRS → Facturation → Conventions de suppléments**.

Sur la convention :

| Élément | Rôle |
|---|---|
| **Statut** | **Ouverte** ou **Clôturé** (en haut de la fiche). |
| Bouton **Clôturer** | Fixe une **date de fin** et arrête de facturer chaque ligne au-delà. |
| Bouton **Rouvrir** | Efface la date de fin et réactive les lignes qui avaient été clôturées. |
| **Lignes** | Produit, type, prix, date de début, date de fin, quantité, actif, notes. |

<!-- capture a ajouter : une convention de suppléments avec le bouton Clôturer et la liste des lignes -->

!!! warning "Un produit sous convention ne se saisit pas en ponctuel"
    Tant qu'un produit est couvert par une **convention active**, il ne peut pas
    être ajouté comme supplément ponctuel pour le même résident. Ajoutez-le **dans
    la convention**, ou **clôturez** d'abord celle-ci.

## Le catalogue des suppléments

Le menu **Configuration → Catalogue** tient la liste des **types de suppléments**
facturables (« Types de suppléments »). Chaque supplément y a :

| Champ | Description |
|---|---|
| **Référence** | Code interne du supplément. |
| **Nom** | Libellé affiché dans le catalogue. |
| **Type de supplément** | **Journalier** (facturé au prorata des jours), **Mensuel** (par mois) ou **Ponctuel** (une fois). |
| **Prix** | Montant unitaire — **valeur propre à l'établissement**. |
| **Code AViQ** | Pseudo-code de déclaration, quand le supplément est déclaré à l'organisme assureur. |

!!! info "Déclaré à l'OA ou non ?"
    Selon sa **catégorie**, un supplément est soit **déclaré à l'organisme
    assureur** dans l'eFact (ET50), soit facturé **uniquement sur la facture du
    résident**. Ce réglage se fait sur la catégorie de produit — voir
    [Réglages de facturation](../configuration/reglages-facturation.md).

## Le reporting

Le menu **Reporting** ouvre une vue d'analyse des suppléments **facturés** :

- un **graphique** des montants par produit ;
- un **tableau croisé** (résidents × mois) ;
- une **liste** détaillée des lignes de suppléments.

Vous pouvez filtrer entre suppléments **ponctuels** et de **convention**, et
regrouper par **résident**, **produit** ou **mois**.

<!-- capture a ajouter : le reporting des suppléments (tableau croisé résidents × mois) -->

!!! note "Après génération seulement"
    Les suppléments n'apparaissent dans le reporting qu'une fois la **période de
    facturation générée** pour le mois concerné.

## Points clés à retenir

- L'application **Suppléments** est un écran de saisie dédié ; elle agit sur les
  **mêmes enveloppes et conventions** que la facturation — pas de données en
  double.
- L'écran **Résidents** est le point de départ : cliquez un résident pour ouvrir
  son catalogue, ou **sélectionnez-en plusieurs** (Ctrl+clic / appui long /
  **Sélection multiple**) puis **Suppléments (N)** pour les servir en une fois.
- **Ponctuel** = une fois sur l'enveloppe ; **convention** = récurrent, sur le
  résident, survivant aux changements de séjour.
- Un produit sous **convention active** ne se saisit pas en ponctuel.
- Le **catalogue** porte le type et le prix (valeur propre à l'établissement) ; le
  **reporting** suit les montants par résident, produit et mois.

## Pour aller plus loin

- [Les suppléments](supplements.md)
- [Facturer un mois, pas à pas](facturer-un-mois.md)
- [Vue d'ensemble de la facturation](index.md)
- [Réglages de facturation](../configuration/reglages-facturation.md)