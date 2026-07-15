---
title: Assurabilité (MDA)
description: Vérifier l'assurabilité d'un résident dans Resthome via MDA (MyCareNet/WalCareNet) — mutuelle, statut BIM, périodes de couverture, contrôle individuel ou par lot, statuts et gestion des erreurs.
---

# Assurabilité (MDA)

Avant de facturer, il faut s'assurer que le résident est **en ordre
d'assurabilité** et connaître sa **mutuelle** exacte. Le **MDA** interroge pour
vous **MyCareNet / WalCareNet** et récupère l'information à jour, pour une
**période** donnée. C'est le préalable indispensable à l'envoi
[eFact](efact.md).

Menu : **eHealth → Assurabilité → Requêtes MDA** (et **Lots MDA**).

## Ce que le MDA récupère

- **Assuré ou non** sur la période.
- La **mutuelle (OA)** qui a réellement répondu — à comparer avec celle du profil
  (une **mutation** de mutuelle est détectée et signalée).
- Le **statut BIM** (intervention majorée).
- Les **périodes de couverture** (dates de début/fin ; plusieurs sous-périodes si
  l'assurance a changé pendant l'intervalle).
- Le **numéro d'affiliation** à la mutuelle.
- Le cas échéant : **tiers payant**, **date de décès** signalée par l'OA, et selon
  la demande, la **pharmacie de référence**, le **DMG**, le **statut palliatif**
  ou une **hospitalisation**.

!!! warning "Le cas « pas en ordre »"
    Si les codes bénéficiaire reviennent à zéro (assuré mais cotisations
    impayées / dossier à problème), Resthome affiche une **alerte** : le résident
    est affilié mais **pas en ordre**. À clarifier avec lui ou sa mutuelle avant de
    facturer à l'OA.

## Prérequis

!!! warning "À vérifier"
    - Le résident a un **NISS** valide.
    - Le **numéro INAMI** de l'établissement est configuré.
    - Le **certificat eHealth** est actif.

    La **mutuelle du profil** n'est pas bloquante (l'OA réel est identifié par la
    réponse), mais la renseigner aide à repérer les mutations.

Resthome applique aussi des règles de période automatiques : la fin doit être
après le début, au plus **5 ans** d'historique, et un MDA standard ne dépasse pas
le mois courant.

## Contrôle individuel

1. Créez une **requête MDA** (résident, NISS pré-rempli, période = le mois
   courant par défaut).
2. Cliquez **Envoyer (Sync)** : l'envoi est **immédiat** et la réponse revient
   tout de suite.
3. Consultez le résumé et les périodes d'assurabilité.

!!! note "Un seul MDA par résident et par période"
    Refaire un contrôle pour le même résident et la même période **réutilise** la
    requête existante — pas de doublon.

## Contrôle par lot (recommandé en début de mois)

Pour toute une période, lancez le contrôle **par lot** : sélectionnez les
résidents (vous pouvez **coller une colonne** de noms/NISS), la période et
envoyez tout le lot d'un coup.

- **Envoi immédiat (Sync)** : pour de petits volumes.
- **Envoi groupé (Async)** : pour les **gros lots mensuels** — la demande part,
  et la réponse se récupère un peu plus tard avec **Vérifier les réponses**
  (nécessite au moins 2 résidents).

Le lot affiche des **compteurs** : Assurés, Non assurés, Erreurs, En attente, et
« Décès détectés ».

!!! tip "Le bon réflexe"
    Faites le MDA **en début de mois**, avant de générer les factures : vous
    évitez les rejets eFact ultérieurs dus à une mutuelle erronée ou à une perte
    d'assurabilité.

## Les statuts

| Statut | Signification |
|---|---|
| **Brouillon** | Pas encore envoyé |
| **Envoyé / En attente** | Transmis, réponse attendue (surtout en groupé) |
| **Succès** | Réponse reçue, résident assuré |
| **Non assuré** | Réponse OK, mais résident non couvert |
| **Sans réponse** | La plateforme a clôturé sans réponse d'un OA (à réessayer) |
| **Erreur** | L'OA ou la plateforme a renvoyé une erreur |

## Les boutons

| Bouton | Effet |
|---|---|
| **Envoyer (Sync)** | Envoi immédiat, réponse tout de suite |
| **Vérifier la réponse** | Récupère une réponse d'un envoi groupé |
| **Réessayer** | Remet en brouillon pour renvoyer |
| **Contacter l'OA** | Ouvre un e-mail pré-rempli vers la mutuelle qui a répondu |
| **Signaler à l'intermut.** | Ouvre un e-mail vers le CIN pour les blocages plateforme |

Sur un lot, les mêmes actions existent en version groupée (**Envoyer**,
**Vérifier les réponses**, **Réessayer les erreurs**, **Réessayer les
sans-réponse**).

## Ce que Resthome met à jour tout seul

Après une réponse réussie, la fiche résident est **corrigée automatiquement** :

- **Mutuelle (OA)** : si l'OA qui répond diffère du profil, le profil est mis à
  jour (et l'OA créé s'il manquait).
- **Statut BIM**, **numéro d'affiliation**, et **identité** (nom, date de
  naissance, sexe) si des champs manquaient.
- **Date de décès** si l'OA la signale → alerte sur la fiche.

!!! warning "Garde-fou régimes spéciaux"
    Pour les résidents sous **régime particulier** (INIG, CEE, Fedasil, étranger,
    privé…), Resthome **n'écrase pas** la mutuelle du profil : un message explique
    que la réponse MDA a été ignorée pour ne pas casser une couverture non
    standard.

## Réintégration (perte puis retour d'assurabilité)

Resthome compare avec le contrôle précédent :

- **Non assuré → assuré** : une notification apparaît sur la période, et l'action
  **Réintégration** permet de basculer vers l'OA les lignes qui avaient été
  facturées au résident.
- **Assuré → non assuré** : Resthome signale que le résident « n'est plus en
  ordre » — son forfait est exclu de la facturation OA de la période et facturé
  au résident jusqu'au rétablissement.

## Gestion des erreurs

| Situation | Quoi faire |
|---|---|
| **Sans réponse** (plateforme) | **Réessayer les sans-réponse** ; si ça persiste, **Signaler à l'intermut.** |
| **Rejet de l'OA** | **Contacter l'OA** (motif affiché) |
| **Erreur technique** | **Signaler à l'intermut.** |
| **Résident sans mutuelle** | Non bloquant : l'OA réel vient de la réponse |
| **En attente (groupé)** | **Vérifier les réponses** ou patienter |

## Pour aller plus loin

- [Erreurs MDA — causes et solutions](mda-erreurs.md)
- [Facturation électronique (eFact)](efact.md)
- [Accords (eAgreement)](eagreement.md)
- [Vue d'ensemble de la facturation](../facturation/index.md)
