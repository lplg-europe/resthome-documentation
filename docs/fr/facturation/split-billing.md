---
title: Débiteurs alimentaires (facturation partagée)
description: Répartir la part résident d'une facture entre plusieurs débiteurs alimentaires dans Resthome, par pourcentage.
---

# Débiteurs alimentaires (facturation partagée)

Quand la **part résident** (hébergement + suppléments) doit être payée par
**plusieurs personnes** — typiquement les **débiteurs alimentaires** (enfants,
proches) — Resthome permet de la **répartir automatiquement**.

## Le principe

Vous définissez, pour un résident, une **répartition en pourcentage** entre
plusieurs débiteurs. À chaque facture mensuelle, Resthome **découpe la part
résident** selon ces pourcentages et adresse à chaque débiteur **sa quote-part**.

!!! note "Ce qui est réparti"
    Seule la **part résident** est concernée (la chambre et les suppléments). Le
    **forfait INAMI** (part mutuelle) n'est pas réparti : il part vers la mutuelle
    via l'[eFact](../ehealth/efact.md).

## Mettre en place une répartition

1. Sur la fiche du **résident** (ou sa période de facturation), ouvrez l'onglet de
   **répartition**.
2. Ajoutez les **débiteurs** et leur **pourcentage** (le total doit faire 100 %).
3. **Enregistrez.**

Les factures suivantes sont automatiquement **scindées** selon cette clé.

!!! tip "Solde à zéro"
    La répartition est conçue pour **tomber juste** : la somme des quotes-parts
    correspond exactement à la part résident, sans reste ni écart d'arrondi.

## Pour aller plus loin

- [Vue d'ensemble de la facturation](index.md)
- [Les suppléments](supplements.md)
