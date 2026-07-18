---
title: Les évaluations gériatriques (hors Katz)
description: "Les échelles gériatriques hors Katz en maison de repos (MR/MRS) avec Resthome : MMSE, Braden, MNA, OHAT et Tinetti — saisie, score, interprétation et suivi."
faq:
  - q: "Quelles échelles gériatriques Resthome propose-t-il en dehors de Katz ?"
    a: "Cinq échelles standard sur l'onglet « Evaluation Tools » du résident : MMSE (cognition), Braden (risque d'escarre), MNA (état nutritionnel), OHAT (santé bucco-dentaire) et Tinetti (équilibre, marche et risque de chute)."
  - q: "Où saisir une évaluation gériatrique dans Resthome ?"
    a: "Depuis la fiche du résident, onglet « Evaluation Tools », ou via le menu Healthcare > Evaluation Tools. Chaque échelle a sa propre liste et son formulaire guidé."
  - q: "Qui peut valider une évaluation ?"
    a: "Tout utilisateur peut la saisir et la confirmer, mais seuls l'infirmier-chef ou le médecin peuvent la valider. Une évaluation validée est verrouillée : il faut la repasser en brouillon pour la corriger."
  - q: "Comment interpréter un score de Braden bas ?"
    a: "Sur l'échelle de Braden, plus le score est bas, plus le risque d'escarre est élevé : 19-23 pas de risque, 15-18 risque léger, 13-14 modéré, 10-12 élevé, 9 ou moins très élevé."
  - q: "Comment ré-évaluer un résident ?"
    a: "Saisissez une nouvelle évaluation à une nouvelle date (une par jour et par échelle) ; l'historique complet est conservé. Pour un cycle de ré-évaluation périodique avec échéance, utilisez les registres cliniques."
  - q: "L'échelle de Morse (risque de chute) est-elle disponible ?"
    a: "L'onglet « Evaluation Tools » propose Tinetti pour l'équilibre et la marche. L'échelle de Morse et le registre des chutes se trouvent dans les registres cliniques du module de soins."
---

# Les évaluations gériatriques (hors Katz)

Au-delà de l'[échelle de Katz](katz.md), Resthome regroupe les principales
**échelles gériatriques** utilisées en maison de repos (MR/MRS) pour objectiver la
cognition, le risque d'escarre, l'état nutritionnel, la santé bucco-dentaire et le
risque de chute. Vous les retrouvez à deux endroits :

- sur la **fiche du résident**, onglet **« Evaluation Tools »**, où chaque échelle
  affiche l'historique du résident et permet une saisie directe ;
- via le menu **Healthcare > Evaluation Tools**, qui liste toutes les évaluations de
  l'établissement, échelle par échelle.

<!-- capture à ajouter : onglet « Evaluation Tools » sur la fiche résident -->

## Les échelles disponibles

| Échelle | Ce qu'elle mesure | Score | Sens |
|---|---|---|---|
| **MMSE** | Fonctions cognitives | /30 | Plus haut = meilleur |
| **Braden** | Risque d'escarre | /23 | Plus bas = plus à risque |
| **MNA** | État nutritionnel | /14 | Plus bas = plus à risque |
| **OHAT** | Santé bucco-dentaire | /16 | Plus haut = plus à risque |
| **Tinetti** | Équilibre et marche (chute) | /28 | Plus bas = plus à risque |

!!! info "La catégorie Katz reste à part"
    L'échelle de Katz détermine la **catégorie de dépendance** et le **forfait** ; elle
    a sa propre page et son propre cycle de renouvellement. Voir [L'évaluation
    Katz](katz.md).

## MMSE — fonctions cognitives

Le **MMSE** (Mini Mental State Examination) est un test de dépistage cognitif standard
sur **30 points**. Vous cochez chaque item réussi, réparti en 7 domaines :

| Domaine | Points |
|---|---|
| Orientation dans le temps | 5 |
| Orientation dans l'espace | 5 |
| Apprentissage (3 mots) | 3 |
| Attention et calcul | 5 |
| Rappel (3 mots) | 3 |
| Langage | 8 |
| Praxie visuo-constructive | 1 |

Resthome additionne les items cochés et affiche l'interprétation :

| Score | Interprétation |
|---|---|
| 27-30 | Normal |
| 21-26 | Trouble cognitif léger |
| 11-20 | Trouble cognitif modéré |
| 0-10 | Trouble cognitif sévère |

## Braden — risque d'escarre

L'échelle de **Braden** prédit le **risque d'escarre**. Vous cotez **6 sous-échelles**
(boutons radio) :

- Perception sensorielle (1-4)
- Humidité de la peau (1-4)
- Activité (1-4)
- Mobilité (1-4)
- Nutrition (1-4)
- Friction et cisaillement (1-3)

Le total va de 6 à 23. **Attention : plus le score est bas, plus le risque est élevé.**

| Score | Niveau de risque |
|---|---|
| 19-23 | Aucun risque |
| 15-18 | Risque léger |
| 13-14 | Risque modéré |
| 10-12 | Risque élevé |
| 9 ou moins | Risque très élevé |

<!-- capture à ajouter : formulaire Braden avec cotations radio et badge de risque -->

## MNA — état nutritionnel

Le **MNA** (Mini Nutritional Assessment, forme courte) dépiste le **risque de
dénutrition** sur **14 points**, à partir de 6 questions :

- Diminution des prises alimentaires sur 3 mois (0-2)
- Perte de poids récente (0-3)
- Motricité (0-2)
- Maladie aiguë / stress psychologique (0 ou 2)
- Problèmes neuropsychologiques (0-2)
- Indice de masse corporelle — IMC (0-3)

| Score | Statut nutritionnel |
|---|---|
| 12-14 | Normal |
| 8-11 | Risque de dénutrition |
| 0-7 | Dénutrition |

!!! tip "Suivi nutritionnel"
    Le suivi de la dénutrition (rappels de re-cotation MNA, apports vs besoins,
    hydratation) s'appuie sur les registres cliniques et le module de soins. Voir [Les
    registres cliniques](../soins/registres.md).

## OHAT — santé bucco-dentaire

L'**OHAT** (Oral Health Assessment Tool) évalue la **santé bucco-dentaire** en
**8 catégories**, cotées de 0 (sain) à 2 (à traiter) : lèvres, langue, gencives et
tissus, salive, dents naturelles, prothèses, propreté buccale et douleur dentaire.

Le total va de 0 à 16. **Ici, plus le score est haut, plus la situation est
préoccupante.**

| Score | État bucco-dentaire |
|---|---|
| 0-3 | Sain |
| 4-8 | Changements nécessaires (orienter vers un professionnel dentaire) |
| 9-16 | Non sain (orientation urgente) |

!!! note "Options « N/A »"
    Les catégories **Dents naturelles** et **Prothèses** disposent d'une option **N/A**
    (non applicable) : elle est exclue du calcul du score total.

## Tinetti — équilibre, marche et risque de chute

L'échelle de **Tinetti** (POMA) évalue l'**équilibre** et la **marche** pour estimer le
**risque de chute** :

- Section Équilibre : 9 items, /16
- Section Marche : /12
- Total : /28

Resthome calcule les deux sous-scores et le total.

| Score | Risque de chute |
|---|---|
| 25-28 | Risque faible |
| 19-24 | Risque modéré |
| Moins de 19 | Risque élevé |

!!! note "Tinetti, Morse et registre des chutes"
    L'onglet « Evaluation Tools » propose **Tinetti**. Pour l'échelle de **Morse** et le
    **registre des chutes** (incidents, mesures préventives, ré-évaluations), utilisez
    les [registres cliniques](../soins/registres.md).

## Saisir et valider une évaluation

Toutes les échelles suivent le même circuit :

1. Ouvrez l'échelle : depuis l'onglet **« Evaluation Tools »** du résident, ou via
   **Healthcare > Evaluation Tools**.
2. **Nouveau** : le résident, la **date** (aujourd'hui par défaut) et l'**évaluateur**
   (vous) sont pré-remplis. Cotez les items.
3. **Confirmer** : l'évaluation passe de **Brouillon** à **Confirmé**.
4. **Valider** : l'infirmier-chef ou le médecin valide ; l'évaluation passe à
   **Validé**, avec le validateur et la date de validation enregistrés.

La barre d'état suit ces étapes : **Brouillon → Confirmé → Validé** (plus **Annulé**).
Les boutons disponibles sont **Confirmer**, **Valider**, **Annuler** et **Remettre en
brouillon**.

!!! warning "Verrouillage et conservation"
    Une évaluation **validée** est **verrouillée** : ses cotations ne sont plus
    modifiables. Pour corriger, cliquez sur **Remettre en brouillon** (réservé à
    l'infirmier-chef). Les évaluations validées **ne peuvent pas être supprimées** : les
    données de santé doivent être conservées (RGPD + INAMI).

!!! note "Une évaluation par jour"
    Il ne peut exister qu'**une seule évaluation par résident, par date et par échelle**.
    La date ne peut pas être dans le futur, et aucune évaluation ne peut être créée pour
    un résident décédé.

## Suivi et ré-évaluation

- L'onglet « Evaluation Tools » conserve l'**historique daté** de chaque échelle : pour
  ré-évaluer, saisissez une **nouvelle évaluation** à une nouvelle date.
- L'échelle de **Katz** a son propre **cycle de renouvellement** (échéance de validité,
  rappels). Voir [L'évaluation Katz](katz.md).
- Pour un **cycle de ré-évaluation périodique** structuré (échéance calculée, décision
  maintenir / modifier / arrêter, journal de suivi), utilisez les [registres
  cliniques](../soins/registres.md).

## Points clés à retenir

- Cinq échelles hors Katz : MMSE, Braden, MNA, OHAT et Tinetti, sur l'onglet
  « Evaluation Tools » du résident.
- Sens des scores : MMSE et Tinetti, score **haut** = situation favorable ; Braden et
  MNA, score **bas** = plus à risque ; OHAT, score **haut** = plus à risque.
- Circuit commun : **Brouillon → Confirmé → Validé** ; la validation est réservée à
  l'infirmier-chef ou au médecin.
- Validé = **verrouillé et conservé** ; repassez en brouillon pour corriger.
- Une évaluation par résident, par date et par échelle.

## Pour aller plus loin

- [L'évaluation Katz](katz.md) — catégorie de dépendance et forfait.
- [Les registres cliniques](../soins/registres.md) — chutes (Morse), contention, douleur, plaies, ré-évaluations périodiques.
- [Les plans de soins](../soins/plans-de-soins.md)
- [Gérer un résident](gerer-un-resident.md)