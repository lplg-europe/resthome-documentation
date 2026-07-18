---
title: Suivi des paiements et rapprochement des décomptes
description: "Savoir si la mutualité a payé vos forfaits en maison de repos (MR/MRS) : lire le décompte (920900), le rapprocher automatiquement et relancer les OA en retard."
howto_auto: true
faq:
  - q: "Quelle est la différence entre l'accusé de réception (931000) et le décompte (920900) ?"
    a: "L'accusé (931000) confirme seulement que l'organisme assureur a reçu votre envoi et passé le premier contrôle — rien n'est encore payé. Le décompte (920900) est le résultat final : il indique, ligne par ligne, ce qui est accepté et ce qui est rejeté, et vaut avis de paiement en Compte C. Tant que le décompte n'est pas arrivé, aucun montant n'est définitif."
  - q: "Comment savoir si un envoi eFact a été payé dans Resthome ?"
    a: "Ouvrez le lot : l'onglet Paiement affiche Payé, la référence de paiement et le montant. En Compte C, dès que le décompte porte une référence de paiement réelle, Resthome marque le lot Payé automatiquement. Pour une vue d'ensemble, le Cockpit eFact regroupe les envois décomptés non encore pointés et les OA en retard."
  - q: "Que veut dire « pointer » un décompte ?"
    a: "Pointer, c'est confirmer que l'argent annoncé par le décompte a bien été reçu. Resthome rapproche automatiquement chaque décompte de son lot ; vous confirmez la réception en ouvrant le décompte et en cliquant sur Mark Reconciled (pointé)."
  - q: "Un organisme assureur tarde à payer : puis-je réclamer des intérêts de retard ?"
    a: "Oui, si l'envoi a été introduit dans les délais (au plus tard le 20 du mois M+1). L'OA doit payer pour la fin du 2e mois suivant l'introduction ; au-delà, Resthome calcule les intérêts de retard (montant accepté × taux légal × jours de retard / 365). Le taux légal se règle dans les réglages eHealth."
  - q: "Le décompte indique à la fois des montants acceptés ET rejetés : que faire ?"
    a: "C'est un rejet partiel : la partie acceptée est payée, les lignes rejetées doivent être corrigées et renvoyées. Resthome crée automatiquement un reliquat pour les lignes rejetées et les inscrit dans la liste Rejected lines (lignes rejetées) du Cockpit."
  - q: "Où voir la liste de tous les décomptes et réponses reçus des OA ?"
    a: "Le Cockpit eFact propose la liste OA retrievals (récupérations OA) : tous les messages récupérés (accusés, décomptes, rejets), filtrables par OA, mois et type, avec export XLSX. La liste eFact Settlements ne montre, elle, que les décomptes (920900)."
---

# Suivi des paiements et rapprochement des décomptes

Une fois vos forfaits envoyés en [eFact](efact.md), reste la vraie question :
**« ai-je été payé ? »**. Cette page explique comment Resthome répond, du
**décompte (920900)** rapproché automatiquement jusqu'à la **relance des
organismes assureurs (OA)** en retard.

Vous trouverez tout dans l'application **MR/MRS → eHealth → eFact** :

- le **Cockpit** — votre tableau de pilotage « quoi faire maintenant » ;
- **eFact Settlements** — la liste des **décomptes** reçus ;
- **eFact Batches** (Lots eFact) — chaque lot et son **onglet Paiement**.

!!! info "Accusé de réception ≠ décompte"
    Ne confondez pas les deux réponses de l'OA. L'**accusé de réception
    (931000)** dit juste « bien reçu ». Le **décompte (920900)** dit « voici ce
    que je paie ». C'est le décompte qui compte pour l'argent.

## Accusé (931000) ou décompte (920900) : le bon repère

| Réponse | Ce que ça veut dire | Y a-t-il paiement ? |
|---|---|---|
| **Accusé de réception (931000)** | L'OA a **reçu** votre envoi et passé le premier contrôle de format. | Non — rien n'est encore décidé. Il faut attendre le décompte. |
| **Décompte (920900)** | Le **résultat final**, ligne par ligne : montants **acceptés** et **rejetés**. En Compte C, il **vaut avis de paiement**. | Oui — c'est ici qu'apparaît ce qui est réellement payé. |

!!! note "Compte C (Wallonie / AViQ)"
    Depuis 2025, la facturation MR/MRS wallonne fonctionne en **Compte C** :
    l'OA paie et **le décompte fait office d'avis de paiement**. Le décompte
    porte donc la **référence de paiement** et le **montant**, mais **pas de date
    de paiement** (le format n'en prévoit pas). Resthome ne fabrique jamais de
    date : elle reste vide tant qu'une date bancaire réelle n'est pas saisie.

## 1. Le décompte (920900) rapproché automatiquement

Quand un décompte revient de l'OA (via la récupération automatique ou le bouton
**Process Response** d'un lot), Resthome le **rapproche tout seul**, sans saisie
de votre part :

1. il crée un enregistrement **décompte (Settlement)** rattaché au lot ;
2. il **réassocie chaque ligne** du décompte à la ligne facturée du bon
   résident (par NISS et montant) ;
3. il marque chaque ligne **acceptée** ou **rejetée** ; un forfait accepté n'est
   pas répété dans le décompte, donc **toute ligne non citée est réputée
   acceptée** (règle AViQ) ;
4. il **met à jour le statut du lot** : **settled** (tout accepté), **rejected**
   (tout rejeté) ou **partial_reject** (mélange, ou décompte partiel en attente
   du reste) ;
5. si des lignes sont rejetées, il prépare **automatiquement un reliquat** pour
   les réintroduire (voir [Rejets eFact](efact-rejets.md)).

En Compte C, dès que le décompte porte une **référence de paiement réelle** et un
**montant accepté positif**, le lot est marqué **Payé** automatiquement. Un
décompte entièrement rejeté (0 € accepté) porte une référence mais ne paie
rien — il n'est donc **pas** marqué payé.

## 2. L'écran eFact Settlements (les décomptes)

Menu **eHealth → eFact → eFact Settlements**. C'est la liste de tous les
**décomptes (920900)** reçus, un par paiement.

La liste affiche : la **référence**, le **lot** concerné, la **date de
réception**, les montants **Accepted** / **Rejected** / **Paid** et la
**référence de paiement**, plus un badge de **statut**.

<!-- capture à ajouter : liste eFact Settlements — un décompte par ligne avec montants acceptés/rejetés/payés et badge de statut -->

Ouvrez un décompte pour le détail. L'écran est en **lecture seule** (rien ne se
saisit à la main) et suit trois états :

| État | Signification |
|---|---|
| **Received** (reçu) | Le décompte vient d'arriver. |
| **Processed** (traité) | Ses lignes ont été ventilées sur le lot. Resthome fait cette étape **automatiquement** à la réception. |
| **Reconciled** (pointé) | Vous avez **confirmé** que l'argent a bien été reçu. |

- Le bouton **Process** (traiter) n'apparaît que si un décompte est resté en
  *Received* sans traitement — cliquez pour le ventiler.
- Le bouton **Mark Reconciled** (marquer pointé) confirme la réception du
  paiement une fois vérifié sur votre extrait bancaire.

L'onglet **Lines** détaille, ligne par ligne : n°, résident, montant réclamé,
accepté, rejeté, la case **Accepted**, et — en cas de refus — le **code** et le
**motif de rejet**. Les lignes rejetées ressortent en rouge.

!!! tip "Lire le décompte tel que l'OA l'a envoyé"
    Un bouton **Decoded 920900** (réservé aux gestionnaires eHealth) affiche le
    fichier brut du décompte, zone par zone, pour vérifier une valeur au plus
    près de la source.

## 3. L'onglet Paiement d'un lot

Sur un lot ([Lots eFact](efact.md)), une fois l'envoi parti, le groupe
**Payment** (Paiement) résume l'état du paiement :

- **Paid** (Payé) — la coche passe au vert quand le lot est payé ;
- **Payment Reference** — la référence de paiement de l'OA ;
- **Payment Date** — la date (souvent vide en Compte C, voir plus haut) ;
- **Total Paid** — le montant payé.

!!! info "Marquer payé manuellement"
    Certains OA paient sans référence de paiement exploitable dans le décompte.
    Un gestionnaire eHealth peut alors activer **Marked Paid Manually** (marqué
    payé manuellement) pour attester le paiement reçu hors flux.

Un encart **Status** indique en un badge ce que le lot attend : *Awaiting OA
response* (en attente de réponse), *Awaiting settlement (920900)* (en attente du
décompte), *Complete* (terminé) ou *Rejected* (à corriger). Quand un lot est
**settled**, le bouton **Close** (clôturer) permet de le classer définitivement.

Dans la liste des lots, les filtres **Paid** / **Unpaid** (payé / impayé) et les
colonnes optionnelles **Payment Ref.**, **Payment Date**, **Amount Paid** aident
à faire le point mois par mois.

## 4. Le Cockpit eFact : « ai-je été payé ? » d'un coup d'œil

Menu **eHealth → eFact → Cockpit** (aussi accessible depuis une période ou une
carte du tableau de bord). Le Cockpit range tout le travail en **piles
d'action**, avec un compteur et un bouton par pile. Trois piles répondent
directement à la question du paiement.

<!-- capture à ajouter : Cockpit eFact — boutons compteurs (To reconcile, Overdue payments, Rejected lines, OA retrievals) et tableau « Rejects by cause » -->

- **To reconcile** (à pointer) — les lots **décomptés mais dont le paiement
  n'est pas encore confirmé**. Le montant total attendu est affiché ; le bouton
  **Reconcile payments** ouvre la liste pour les pointer un à un.
- **Overdue payments** (paiements en retard) — les envois **acceptés mais
  toujours impayés** dont l'**échéance de paiement OA est dépassée**. Voir la
  relance ci-dessous.
- **Rejected lines** (lignes rejetées) — la **liste de travail** des lignes
  rejetées encore à renvoyer (résident + code + montant), filtrable par cause,
  OA et mois.

Deux repères complètent le tableau :

- **OA retrievals** (récupérations OA) — le **journal complet** de tout ce que
  l'OA a renvoyé : accusés, décomptes et rejets, filtrables par OA, mois et
  type, avec un bouton **Export XLSX**.
- **Rejects by cause** (rejets par cause) — un tableau qui regroupe les lignes
  rejetées **par motif**, pour traiter la cause systémique plutôt que ligne par
  ligne.

!!! tip "Aller chercher les réponses"
    Si des lots restent en attente, le bouton **Fetch responses** (récupérer les
    réponses) interroge la plateforme OA et met à jour les statuts. Les réponses
    arrivent aussi automatiquement, mais ce bouton force une vérification
    immédiate.

## 5. Relancer un OA en retard

La pile **Overdue payments** liste les envois **introduits dans les délais**,
**acceptés** par l'OA mais **non payés** au-delà de l'échéance. Le bouton
**Chase (by OA)** ouvre ces lots **regroupés par organisme assureur** : vous
voyez immédiatement **qui relancer** et **pour quel montant** (le total accepté
est additionné par OA).

Pour écrire à l'OA, le bouton **Contact OA** (présent sur chaque lot) prépare la
prise de contact avec le bon interlocuteur de facturation.

## 6. Intérêts de retard (intérêts moratoires)

Un envoi payé trop tard peut donner droit à des **intérêts de retard**. Resthome
applique la règle AViQ :

- l'envoi doit avoir été **introduit dans les délais** (envoyé au plus tard le
  **20 du mois M+1**) — c'est la condition d'**éligibilité** ;
- l'OA doit payer **pour la fin du 2e mois suivant l'introduction** : c'est
  l'**OA Payment Deadline** (échéance de paiement) ;
- passé cette date, les intérêts courent, calculés ainsi :
  **montant accepté × taux légal annuel × jours de retard / 365**.

Sur le lot, dès que l'échéance est dépassée et le lot toujours impayé, un groupe
**Late-payment interest (OA)** apparaît avec l'**échéance**, les **jours de
retard** et l'**intérêt dû**. La liste des lots propose le filtre **OA Payment
Overdue** et une colonne **OA Pay Deadline** (en rouge si dépassée).

!!! warning "Renseigner le taux légal"
    Le calcul reste à **0 tant que le taux légal n'est pas saisi**. Indiquez le
    **taux d'intérêt légal annuel** publié dans **eHealth → Réglages → Legal
    Interest Rate (%)** — voir [Réglages eHealth](../configuration/reglages-ehealth.md).
    C'est une valeur **propre à votre établissement / à l'année** en cours.

## Points clés à retenir

- L'**accusé (931000)** ne paie rien ; seul le **décompte (920900)** dit ce qui
  est réellement payé.
- Resthome **rapproche le décompte automatiquement** : lignes ventilées, statut
  du lot mis à jour, reliquat créé pour les rejets.
- En **Compte C**, un décompte avec référence de paiement réelle marque le lot
  **Payé** automatiquement (la date de paiement peut rester vide).
- **Pointer** un décompte (**Mark Reconciled**), c'est confirmer l'argent reçu ;
  le Cockpit regroupe le **À pointer** et les **OA à relancer**.
- Les **intérêts de retard** ne se calculent qu'après avoir renseigné le **taux
  légal** dans les réglages eHealth.

## Pour aller plus loin

- [Facturation électronique (eFact)](efact.md)
- [Rejets eFact — causes et solutions](efact-rejets.md)
- [Facturer un mois](../facturation/facturer-un-mois.md)
- [Réglages eHealth](../configuration/reglages-ehealth.md)
- [Vue d'ensemble eHealth](index.md)