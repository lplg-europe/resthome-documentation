---
title: eHealth
description: Assurabilité MDA, facturation électronique eFact et accords eAgreement dans Resthome.
---

# eHealth

Resthome est connecté à l'écosystème e-santé belge (eHealth, MyCareNet,
WalCareNet) pour échanger directement avec les mutuelles.

## Les services

<div class="grid cards" markdown>

-   :material-shield-check:{ .lg .middle } **MDA — Assurabilité**

    ---

    Vérifie qu'un résident est **assuré** et récupère sa mutuelle et son statut
    BIM, individuellement ou par lot.

-   :material-send:{ .lg .middle } **eFact — Facturation électronique**

    ---

    Envoie la **part mutuelle** (message 920000) aux organismes assureurs et
    suit les accusés et décomptes.

-   :material-file-sign:{ .lg .middle } **eAgreement — Accords**

    ---

    Notifie l'OA lors d'une **admission**, d'une **fin de séjour** ou d'une
    **absence** (Annexes 7, 10, 11…).

</div>

## Prérequis

!!! warning "À vérifier avant d'envoyer"
    - Le résident a un **NISS** valide.
    - Sa **mutuelle** est renseignée.
    - Une **assurabilité (MDA)** a été vérifiée pour la période.
    - Le **certificat eHealth** de l'établissement est actif.

## Bon à savoir

- Une **absence** de plus de 72 h (ou toute hospitalisation) déclenche une
  **Annexe 11** de fin d'hébergement ; le **retour** génère une **Annexe 7** de
  réadmission.
- Une facture déjà **comptabilisée** « fige » la facturation du mois pour ce
  résident : pour la modifier, remettez-la en brouillon (ou émettez une note de
  crédit), puis actualisez.

*Le détail des envois et du suivi des réponses sera documenté dans les pages à
venir de cette section.*

## À suivre

- [Facturation](../facturation/index.md)
