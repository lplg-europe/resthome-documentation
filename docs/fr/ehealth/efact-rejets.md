---
title: Rejets eFact — causes et solutions
description: "Pourquoi une facture eFact de maison de repos est rejetée par la mutuelle et comment la corriger dans Resthome : assurabilité, forfait, dates, doublon, renvoi."
faq:
  - q: "Pourquoi une facture eFact est-elle rejetée ?"
    a: "Le plus souvent : assurabilité (MDA) non valide, mauvaise mutuelle sur la fiche, forfait déclaré au-delà de la fin d'intervention INAMI, absence non clôturée, catégorie Katz manquante, NISS incorrect ou double envoi. Le code et le motif de rejet renvoyés par l'organisme assureur indiquent la cause."
  - q: "Que faire quand un lot eFact est rejeté ?"
    a: "On ne renvoie pas un lot tel quel : on corrige la cause à la source (MDA, mutuelle, Katz, dates…), on régénère, puis on renvoie. Le compteur Renvois trace les retransmissions pour éviter les doublons."
  - q: "Quelle est la différence entre un rejet global et un rejet partiel ?"
    a: "Un rejet partiel refuse seulement certaines lignes (le reste est payé) : on ne corrige et ne renvoie que ces lignes. Un rejet global refuse le lot entier : on corrige la cause et on renvoie un lot neuf."
  - q: "Comment corriger une surfacturation (départ, décès, forfait sur-déclaré) ?"
    a: "Resthome le détecte via l'auto-contrôle et prépare une note de crédit côté résident et, si la part mutuelle est concernée, un lot correctif vers l'organisme assureur. Les lignes de crédit sont intégrées à l'envoi suivant."
---

# Rejets eFact — causes et solutions

Quand vous envoyez l'[eFact](efact.md), l'**organisme assureur (OA)** vérifie chaque
ligne et vous renvoie un résultat. Cette page explique **comment lire une réponse**,
**pourquoi un lot ou une ligne est rejeté**, et **comment corriger puis renvoyer**.

!!! info "Deux lignes de défense"
    La plupart des causes de rejet sont **interceptées par Resthome avant l'envoi**
    (auto-contrôle de la période, contrôles à la génération). Elles apparaissent alors
    comme un **message d'anomalie** à traiter, pas comme un rejet. Les cas qui passent
    malgré tout reviennent ensuite sous forme de **rejet de l'OA**. Cette page couvre
    les deux.

## Le cycle de réponse, en clair

Après l'envoi d'un lot, les réponses de l'OA font évoluer le **statut du lot** et
remplissent les **montants** (facturé / accepté / refusé) :

1. **Accusé de réception** — l'OA confirme avoir reçu le fichier et passé le premier
   contrôle. Rien à faire.
2. **Décompte de l'OA** — l'OA renvoie le résultat **ligne par ligne** : ce qui est
   **accepté** et ce qui est **refusé**. Resthome rapproche ce décompte et met à jour
   les montants du lot.
3. **Acceptation et/ou rejet** — trois issues possibles :
    - **tout est accepté** → le lot est décompté, puis peut être clôturé ;
    - **rejet partiel** — certaines lignes sont refusées, le reste est payé : on ne
      corrige et ne renvoie **que** les lignes refusées ;
    - **rejet global** — le lot entier est refusé, rien n'est payé : on corrige la
      cause et on **renvoie un lot neuf**.

!!! note "Quand un lot est-il rejeté globalement ?"
    L'organisme assureur rejette **tout le lot** (920099) en cas d'**erreur bloquante**
    ou lorsque le **taux d'erreurs dépasse environ 5 %** des lignes. En dessous, les
    lignes fautives font l'objet d'un **rejet partiel** et le reste est payé — d'où
    l'intérêt de traiter l'auto-contrôle et le MDA **avant** d'envoyer.

Sur chaque ligne refusée, un **code** et un **motif de rejet** en clair pointent la
cause.

## Causes de rejet fréquentes → action

| Cause | Ce que vous voyez | Action dans Resthome |
|---|---|---|
| **Assurabilité (MDA) non valide ou manquante** | Compteur **MDA** pas au vert ; lot retenu à l'envoi ; ou rejet de l'OA pour assurabilité | Lancer **Vérifier MDA**, obtenir le statut **Succès** pour chaque résident, puis **régénérer** l'eFact. Le MDA doit être validé **avant** de générer. |
| **Mutuelle erronée ou absente** | Le forfait part au mauvais OA (rejet) ou n'apparaît pas dans le lot | Renseigner/corriger la **mutuelle** sur la fiche du résident, puis **régénérer**. Vérifier que chaque résident facturé en tiers payant a bien une mutuelle. |
| **Forfait déclaré au-delà de la fin d'intervention** | Auto-contrôle : **« forfait OA sur-déclaré »** ; l'OA refuse les jours en trop | Émettre une **note de crédit / un reliquat** pour les jours sur-déclarés (voir plus bas). |
| **Chambre libérée / décès — hébergement encore facturé** | Auto-contrôle : **surfacturation** ; refus des jours indus | **Clôturer l'hébergement** à la bonne date + **note de crédit**. |
| **Absence non clôturée** | Compteur **Absences** actif ; jours de forfait faussés | Clôturer les absences de la période, puis re-contrôler. |
| **Catégorie Katz manquante ou évaluation expirée** | Compteur **« Katz à faire »** ; blocage à la génération | Compléter ou renouveler l'**évaluation Katz**, puis **régénérer**. |
| **NISS manquant ou incorrect** | Donnée d'identification obligatoire → rejet technique | Corriger le **NISS** sur la fiche du résident, puis régénérer. |
| **Double envoi** | L'OA signale un **envoi déjà reçu** | Ne pas renvoyer un lot **déjà accepté**. Pour un renvoi légitime, s'appuyer sur le compteur **Renvois** (anti-doublon). |
| **Discordance de montant / tarif** | L'OA renvoie un **montant/tarif inattendu** | Vérifier le **tarif** appliqué et le montant de la ligne, corriger le paramétrage, régénérer, renvoyer. |
| **Rejet technique / de format** | **Rejet global** : le fichier n'a pas passé le contrôle de format | Cas rare à escalader : utiliser **Contact OA** ou **Helpdesk**, corriger, puis renvoyer un lot neuf. |

## Corriger, puis renvoyer

Le principe : **on ne repousse pas un lot rejeté tel quel — on corrige la cause à la
source, puis on renvoie.**

- **Boucle corriger → renvoyer.** Après avoir traité la cause (MDA, mutuelle, Katz,
  absence, dates…), régénérez la partie concernée et renvoyez. Le compteur **Renvois**
  garde la trace de chaque retransmission pour **éviter d'envoyer deux fois** le même
  lot.
- **Réintégration.** Le bouton **Réintégration** permet de réintégrer des lignes
  (par exemple des lignes rejetées, une fois corrigées) dans un **nouvel envoi**,
  plutôt que de tout refaire.
- **Note de crédit / lot correctif.** Chaque fois que vous avez **facturé plus que
  dû** — départ ou décès en cours de mois facturé, forfait sur-déclaré — Resthome
  prépare une **note de crédit** (côté résident) et, si la part mutuelle est concernée,
  un **lot correctif** vers l'OA. Les lignes de crédit sont intégrées à l'**envoi eFact
  suivant**.

## Les réponses que vous pouvez croiser

Selon le message renvoyé par l'OA, vous pouvez apercevoir, dans les statuts ou le
journal du lot :

| Réponse | Ce que ça veut dire |
|---|---|
| **Accusé de réception** | L'OA a **reçu** le fichier et il a passé le premier contrôle. Étape normale. |
| **Notification avec avertissements** | Le lot est **accepté**, mais avec des **avertissements** (erreurs mineures) à lire. |
| **Décompte** | Le **résultat ligne par ligne** : montants **acceptés** et **refusés**. C'est ici qu'apparaissent les rejets partiels à corriger. |
| **Rejet global** | Le **lot entier est refusé** (trop d'erreurs). Corriger la cause et **renvoyer un lot neuf**. |
| **Rejet technique** | Le fichier n'a pas passé le **contrôle de format** ; retransmission nécessaire après correction. |

## Points clés

- **Prévenez plutôt que guérir** : traitez les messages d'**auto-contrôle** et
  validez le **MDA** avant de facturer — la plupart des rejets sont ainsi évités.
- Un **rejet partiel** se corrige **ligne par ligne** ; un **rejet global** se
  **renvoie en lot neuf**.
- Une **surfacturation** (départ, décès, forfait sur-déclaré) se corrige par une
  **note de crédit / un lot correctif**, pas par un simple renvoi.

## Pour aller plus loin

- [Facturation électronique (eFact)](efact.md)
- [Assurabilité (MDA)](mda.md) · [Erreurs MDA](mda-erreurs.md)
- [Départ et décès](../facturation/depart-deces.md)
- [FAQ](../faq.md) · [Glossaire](../glossaire.md)
