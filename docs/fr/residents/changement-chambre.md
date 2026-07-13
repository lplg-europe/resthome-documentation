---
title: Changement de chambre et transfert
description: Changer un résident de chambre ou le transférer entre MR et MRS dans Resthome — facturation scindée automatiquement, sans nouvelle admission.
---

# Changement de chambre et transfert

Un résident peut **changer de chambre** ou passer de **MR à MRS** (ou l'inverse)
en cours de séjour. Resthome gère la **transition** proprement : la facturation
est **scindée** à la bonne date, sans que vous ayez à refaire une admission.

## Changer de chambre

Pour un simple changement de chambre (même type de soins) :

1. Sur le **séjour** du résident, utilisez l'action **Changer de chambre**.
2. Indiquez la **nouvelle chambre** et la **date/heure** du changement.
3. **Validez.**

Resthome **clôt** la facturation de l'ancienne chambre à cette date et **ouvre**
celle de la nouvelle, au tarif correspondant.

!!! note "Pas de nouvelle admission"
    Un changement de chambre n'est **pas** une nouvelle entrée : l'intervention
    INAMI (le forfait) reste **continue**, il n'y a pas de nouvel accord à
    demander. Seule la **part hébergement** est scindée aux deux tarifs.

## Transfert MR ↔ MRS

Le passage d'un type de soins à l'autre (MR ↔ MRS) est un **transfert interne** :

1. Sur le séjour, utilisez l'action **Transfert interne**.
2. Indiquez la **date/heure** du transfert et le **nouveau type de soins**.
3. **Validez.**

Resthome scinde la facturation à la date de transfert et **met à jour le forfait**
selon le nouveau type. Le cas échéant, il prépare la **notification eHealth**
correspondante.

!!! tip "La facturation suit toute seule"
    Après un changement de chambre ou un transfert, vous n'avez rien à recalculer
    à la main : les segments sont facturés chacun à leur tarif, et le forfait
    continue sans rupture.

## Pour aller plus loin

- [Gérer un résident](gerer-un-resident.md)
- [Vue d'ensemble de la facturation](../facturation/index.md)
