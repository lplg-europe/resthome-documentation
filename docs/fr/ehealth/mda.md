---
title: Assurabilité (MDA)
description: Vérifier l'assurabilité d'un résident dans Resthome via MDA (MyCareNet/WalCareNet) — mutuelle, statut BIM, contrôle individuel ou par lot.
---

# Assurabilité (MDA)

Avant de facturer, il faut s'assurer que le résident est **bien assuré** et
connaître sa **mutuelle** exacte. Le **MDA** (contrôle d'assurabilité) interroge
pour vous **MyCareNet / WalCareNet** et récupère l'information à jour.

## À quoi ça sert

- Confirmer que le résident est **en règle** d'assurabilité pour la période.
- Récupérer / corriger automatiquement sa **mutuelle (organisme assureur)**.
- Récupérer son statut **BIM** (intervention majorée), qui peut influencer la
  facturation.

## Lancer un contrôle

1. Ouvrez la **période de facturation** du mois, ou la fiche du résident.
2. Lancez une **vérification MDA**.
3. Resthome met à jour la **mutuelle** et le **statut BIM** si nécessaire, et
   affiche le résultat.

Vous pouvez contrôler **un résident** ou lancer le contrôle **par lot** pour toute
la période.

!!! warning "Prérequis"
    - Le résident a un **NISS** valide.
    - Le **certificat eHealth** de l'établissement est actif.

    Sans NISS, l'assurabilité ne peut pas être interrogée.

!!! tip "Bon réflexe"
    Faites le MDA **en début de mois**, avant de générer les factures : vous évitez
    les rejets ultérieurs dus à une mutuelle erronée ou à une perte
    d'assurabilité.

## Résultats et suivi

Le résultat du contrôle est conservé sur la période / le résident. Si une
information a changé (changement de mutuelle, perte de BIM…), Resthome le reflète
pour que la facturation et les envois eFact partent avec les bonnes données.

## Pour aller plus loin

- [Facturation électronique (eFact)](efact.md)
- [Accords (eAgreement)](eagreement.md)
- [Vue d'ensemble eHealth](index.md)
