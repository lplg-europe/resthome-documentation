---
title: L'évaluation Katz
description: L'échelle de Katz en maison de repos avec Resthome — coter les 6 critères, déterminer la catégorie (O, A, B, C, Cd) et le forfait INAMI de dépendance.
faq:
  - q: "Comment calculer la catégorie Katz d'un résident ?"
    a: "Cotez les 6 critères de dépendance (se laver, s'habiller, transfert, aller à la toilette, continence, manger) de 1 à 4 ; Resthome en déduit la catégorie (O, A, B, C, Cd), déclarée à la mutuelle pour le forfait INAMI."
  - q: "Que signifie la catégorie O ?"
    a: "La catégorie O correspond à un résident autonome. Dans les tarifs AViQ, le forfait de dépendance est le même montant pour toutes les catégories, y compris O. Tant qu'aucune évaluation Katz n'est validée, le résident est en catégorie O par défaut ; validez le Katz pour déclarer la bonne catégorie à la mutuelle."
  - q: "Comment gérer une aggravation de la dépendance ?"
    a: "Saisissez une nouvelle évaluation Katz avec un motif d'aggravation. Resthome prépare l'Annexe 10 (motif + signature du clinicien) ; la nouvelle catégorie n'est facturée qu'une fois l'accord de la mutuelle obtenu."
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
| **O** | Autonome |
| **A** | Dépendance légère |
| **B** | Dépendance moyenne |
| **C** | Forte dépendance |
| **Cd / Cc** | Forte dépendance avec désorientation / cas particuliers |

!!! info "Le forfait est le même pour toutes les catégories"
    Dans les tarifs **AViQ**, le montant du forfait de dépendance est **identique pour
    toutes les catégories**, y compris **O**. La catégorie ne change pas le montant :
    elle sert à déclarer le bon profil à la mutuelle (voir [Le forfait
    INAMI](../facturation/forfait-inami.md)).

!!! note "Catégorie O par défaut"
    Tant qu'aucun Katz **validé** n'existe, le résident est en catégorie **O** par
    défaut, et un rappel « Katz à faire » apparaît sur le tableau de bord. Validez le
    Katz pour déclarer la bonne catégorie à la mutuelle.

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

- [Le forfait INAMI (dépendance)](../facturation/forfait-inami.md) — de la catégorie au montant facturé.
- [Gérer un résident](gerer-un-resident.md)
- [Facturation](../facturation/index.md)
- [Accords (eAgreement)](../ehealth/eagreement.md)
