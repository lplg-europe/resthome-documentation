---
title: Facturation électronique (eFact)
description: Envoyer la part mutuelle par eFact dans Resthome — génération des lots, transmission aux organismes assureurs, suivi des accusés et des rejets, notes de crédit.
---

# Facturation électronique (eFact)

L'**eFact** est l'envoi électronique de la **part mutuelle** (le forfait INAMI)
aux **organismes assureurs**. Resthome génère les fichiers, les transmet et **suit
les réponses** pour vous.

## Le principe

Une fois les factures du mois **comptabilisées**, Resthome constitue les **lots
eFact** et les envoie aux mutuelles via le réseau eHealth. Chaque envoi reçoit un
**accusé de réception**, puis un **décompte** (accepté / rejeté) que Resthome
rapproche automatiquement.

!!! note "Un envoi par union de mutualités"
    Les envois sont regroupés **par union** (les grandes familles de mutualités),
    pas par petite mutuelle individuelle. Resthome s'occupe du regroupement.

## Générer et envoyer

1. Sur la **période de facturation**, vérifiez que les factures sont
   **comptabilisées**.
2. **Générez l'eFact** (constitution des lots).
3. **Envoyez** — la transmission part vers les organismes assureurs.

## Suivre les réponses

Chaque lot passe par des états visibles :

1. **Envoyé** — transmis, en attente d'accusé.
2. **Accusé reçu** — la mutuelle a bien reçu.
3. **Accepté** / **Rejeté** — le décompte est revenu.

En cas de **rejet**, Resthome remonte le motif pour que vous puissiez corriger
(assurabilité, dates, montants…) et **renvoyer**. Le suivi des renvois évite les
doublons.

!!! tip "Cockpit eFact"
    Un tableau de suivi vous donne l'état de tous les lots (envoyés, acceptés,
    rejetés, à renvoyer) pour piloter la facturation mutuelle d'un coup d'œil.

## Notes de crédit

Si vous devez **rembourser** ou corriger une facture mutuelle déjà envoyée,
Resthome produit la **note de crédit** électronique correspondante et l'inclut
dans les envois, en cohérence avec le forfait facturé.

## Prérequis

!!! warning "À vérifier avant l'envoi"
    - **Assurabilité (MDA)** contrôlée pour la période.
    - **Mutuelle** correcte sur chaque résident.
    - Factures **comptabilisées**.
    - **Certificat eHealth** actif.

## Pour aller plus loin

- [Assurabilité (MDA)](mda.md)
- [Accords (eAgreement)](eagreement.md)
- [Vue d'ensemble de la facturation](../facturation/index.md)
