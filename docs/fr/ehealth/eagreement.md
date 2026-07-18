---
title: Accords (eAgreement)
description: "eAgreement et eAgreement Light dans Resthome (maison de repos MR/MRS) — faire une demande d'accord, notifier la mutuelle à l'admission, en cas d'absence, au départ et au retour (Annexes 7, 10, 11)."
faq:
  - q: "Comment faire une demande d'accord (eAgreement) dans Resthome ?"
    a: "Dans la plupart des cas, vous n'avez pas à la créer à la main : Resthome prépare automatiquement la notification qui correspond à votre action métier — démarrer un séjour (accord d'admission, Annexe 7), valider une aggravation Katz (mise à jour de l'accord de soins, Annexe 10), enregistrer une absence ou un départ (notification de sortie, Annexe 11). Vérifiez que le résident a un NISS et une mutuelle valides et que le certificat eHealth est actif, puis envoyez. Vous suivez ensuite le statut : Brouillon → Envoyé → Accepté ou Rejeté."
  - q: "Où voir le statut d'un accord ou d'une demande dans Resthome ?"
    a: "Depuis la fiche du résident ou la période de facturation : vous y voyez la liste des accords et leur statut (Brouillon, Envoyé, Accepté, Rejeté), avec un lien vers le détail."
  - q: "Quelle est la différence entre eAgreement et eAgreement Light ?"
    a: "eAgreement est l'accord de prise en charge des soins, lié à la catégorie Katz et au forfait. eAgreement Light regroupe les notifications plus simples liées aux mouvements du résident (admission, absence, départ, retour), que Resthome génère automatiquement au fil de vos actions."
  - q: "Que faire si une demande d'accord est rejetée ?"
    a: "Resthome affiche le motif de rejet en clair (français et néerlandais) directement sur l'accord. Corrigez la cause — le plus souvent le NISS, la mutuelle ou les dates — puis renvoyez."
---

# Les accords eHealth (eAgreement)

Quand un résident entre, s'absente, revient ou quitte l'établissement, la
**mutuelle (organisme assureur)** doit en être informée par voie électronique.
Resthome s'en charge : au bon moment, il **prépare automatiquement** la
notification eHealth qui correspond à votre action. Vous n'avez, la plupart du
temps, **rien à saisir en plus** — juste à vérifier et, si besoin, à envoyer.

!!! note "Deux notions proches"
    - **eAgreement** : l'accord de prise en charge des soins (lié à la catégorie
      **Katz** et au forfait).
    - **eAgreement Light** : les notifications plus simples liées aux
      **mouvements** du résident — admission, absence, départ, retour. Ce sont
      elles que Resthome génère tout seul au fil de vos actions.

## Quand Resthome crée-t-il un accord ?

Vous faites l'action métier habituelle ; Resthome en déduit la notification.

| Votre action dans Resthome | Notification préparée | Document |
|---|---|---|
| **Démarrer un séjour** (admission) | Accord d'admission | Annexe 7 |
| **Enregistrer une absence** / hospitalisation | Notification de sortie | Annexe 11 |
| **Retour** du résident (fin d'absence) | Réadmission | Annexe 7 |
| **Aggravation Katz** validée | Mise à jour de l'accord de soins | Annexe 10 |
| **Fin de séjour / décès** | Notification de sortie | Annexe 11 |

!!! tip "Le principe, en une phrase"
    Vous gérez le **résident** (entrée, absence, retour, sortie) ; Resthome gère
    l'**eHealth** derrière. Les manipulations de facturation et d'accords que vous
    voyez apparaître sont le reflet automatique de ce que vous venez de faire.

## Ce qu'il faut avant d'envoyer

!!! warning "À vérifier"
    - Le résident a un **NISS** (numéro national) valide.
    - Sa **mutuelle** est renseignée.
    - Le **certificat eHealth** de l'établissement est actif.

    Sans NISS, l'accord ne peut pas être transmis. Vous pouvez tout de même
    enregistrer le mouvement (admission, absence…) : Resthome le note et vous
    invite à compléter le NISS dès que possible.

## Suivre un accord

Chaque accord passe par des **statuts** clairs :

1. **Brouillon** — préparé par Resthome, pas encore envoyé.
2. **Envoyé** — transmis à la mutuelle via eHealth.
3. **Accepté** — la mutuelle a marqué son accord.
4. **Rejeté** — la mutuelle refuse, avec un **motif**.

Depuis la fiche du résident ou la période de facturation, vous voyez la liste des
accords et leur statut, avec un lien vers le détail.

### En cas de rejet

Si la mutuelle rejette une demande, Resthome affiche le **motif de rejet en clair,
en français et en néerlandais**, directement sur l'accord. Vous savez ainsi
immédiatement quoi corriger (souvent : NISS, mutuelle, ou dates) avant de
renvoyer.

## Cas particuliers utiles

- **Absence de courte durée** : une absence de plus de **72 h** (ou toute
  **hospitalisation**) déclenche l'**Annexe 11** de sortie ; le **retour** génère
  l'**Annexe 7** de réadmission. Voir [Absences et
  hospitalisations](../facturation/absences.md).
- **Facturation déjà clôturée** : si la facture du mois concerné est **déjà
  comptabilisée** pour ce résident, Resthome **ne recrée pas** d'accord en double
  pour ce mois — il protège la cohérence. Repassez la facture en brouillon (ou
  faites une note de crédit) si vous devez vraiment modifier ce mois, puis
  actualisez.
- **Réadmission après un long congé** : selon la durée, la réadmission peut
  nécessiter une **nouvelle évaluation Katz** — Resthome vous le signale.

## Pour aller plus loin

- [Accord refusé (eAgreement) — causes et solutions](eagreement-refus.md)
- [Absences et hospitalisations](../facturation/absences.md)
- [Départ et décès](../facturation/depart-deces.md)
- [Vue d'ensemble eHealth](index.md)
