---
title: L'évaluation Katz
description: L'échelle de Katz dans Resthome — coter les 6 critères, déterminer la catégorie (O, A, B, C, Cd) et le forfait INAMI, valider, gérer une aggravation.
---

# L'évaluation Katz

L'**échelle de Katz** mesure le degré de **dépendance** d'un résident. C'est elle
qui détermine sa **catégorie** de soins et donc le **forfait INAMI** remboursé par
la mutuelle. Dans Resthome, la saisie est guidée et le calcul est automatique.

## Les 6 critères

Chaque critère est coté de **1** (autonome) à **4** (totalement dépendant) :

1. **Se laver**
2. **S'habiller**
3. **Transfert et déplacements**
4. **Aller à la toilette**
5. **Continence**
6. **Manger**

À partir de ces cotations, Resthome calcule la **catégorie** conformément à la
réglementation.

## Les catégories

| Catégorie | Signification |
|---|---|
| **O** | Autonome — **non remboursée** par l'INAMI |
| **A** | Dépendance légère |
| **B** | Dépendance moyenne |
| **C** | Forte dépendance |
| **Cd / Cc** | Forte dépendance avec désorientation / cas particuliers |

!!! note "Catégorie O par défaut"
    Tant qu'aucun Katz **validé** n'existe, le résident est facturé en catégorie
    **O** (non remboursée), et un rappel « Katz à faire » apparaît sur le tableau
    de bord. Saisir et valider le Katz débloque le forfait correspondant.

## Saisir une évaluation

1. Depuis la fiche du résident, ouvrez **Katz** (bouton ou outils d'évaluation).
2. **Nouveau** : cotez les 6 critères.
3. **Confirmez** puis **Validez** l'évaluation.

La catégorie et le forfait se mettent à jour automatiquement pour la facturation.

!!! tip "Ce que Resthome fait pour vous"
    À la validation, Resthome relie l'évaluation à la facturation (forfait) et, le
    cas échéant, prépare l'accord de soins avec la mutuelle. Vous n'avez pas à
    reporter la catégorie ailleurs.

## Aggravation en cours de séjour

Si l'état du résident se dégrade, saisissez une **nouvelle évaluation** avec un
**motif d'aggravation**. Resthome prépare alors la mise à jour de l'accord
(**Annexe 10**) : le motif renseigné est repris automatiquement, et la
**signature** du clinicien vient compléter le document.

## Pour aller plus loin

- [Gérer un résident](gerer-un-resident.md)
- [Facturation](../facturation/index.md)
- [Accords (eAgreement)](../ehealth/eagreement.md)
