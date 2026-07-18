---
title: Réglages de facturation (MR/MRS)
description: "Configurer l'onglet de réglages MR/MRS de Resthome pour une maison de repos (MR/MRS) : facturation automatique, journaux, agrément Cc, absences."
faq:
  - q: "Où se trouvent les réglages de facturation MR/MRS ?"
    a: "Dans Réglages > MR/MRS. L'onglet n'est visible que pour les gestionnaires MR/MRS. Il regroupe la facturation automatique, les journaux, l'agrément de l'établissement, la facturation partagée et la gestion des absences."
  - q: "Faut-il activer l'actualisation automatique de la facturation ?"
    a: "Oui, c'est la valeur conseillée. Activée, elle garde chaque période de facturation ouverte à jour dès qu'une donnée change : supplément, absence, fin de séjour, changement de chambre ou de mutuelle, admission en cours de mois. Désactivez-la seulement si vous préférez ne recalculer qu'en cliquant « Actualiser » sur la période."
  - q: "Quelle différence entre le Journal INAMI et le Journal résident ?"
    a: "Le Journal INAMI reçoit les factures de la part mutuelle (envoyée via l'eFact) ; le Journal résident reçoit celles de la part résident (hébergement et suppléments). Ce sont deux journaux de vente de votre établissement, distincts de préférence pour un suivi comptable clair."
  - q: "Quand cocher l'Agrément Cc ?"
    a: "Uniquement si votre établissement détient l'agrément qui autorise à facturer le forfait comateux Ccoma. Sans cet agrément, un résident classé Ccoma n'est pas facturable via l'eFact ; l'hébergement, lui, reste facturé. C'est une valeur propre à l'établissement."
  - q: "Activer la facturation partagée installe-t-il un module ?"
    a: "Oui. Cocher « Facturation partagée (débiteurs alimentaires) » installe le module correspondant ; le décocher le désinstalle. Activez-la si des débiteurs alimentaires se partagent la part résident."
  - q: "À quoi sert l'assigné de l'activité Katz ?"
    a: "C'est l'utilisateur à qui Resthome assigne l'activité « Nouveau Katz requis » lorsqu'une réadmission après hospitalisation dépasse 30 jours. Si le champ est vide, l'activité va à l'utilisateur courant s'il est clinique, sinon au premier infirmier-chef, infirmier ou médecin trouvé."
---

# Réglages de facturation (MR/MRS)

L'onglet **MR/MRS** des réglages regroupe les paramètres qui pilotent la
**facturation** de votre maison de repos : génération des factures, journaux
comptables, agrément de l'établissement et gestion des absences. On les configure
**une fois**, puis ils n'évoluent qu'à la marge.

Vous les trouvez dans **Réglages > MR/MRS**. L'onglet n'est visible que pour les
**gestionnaires MR/MRS**.

!!! info "Les secrets eHealth se configurent ailleurs"
    Le **certificat eHealth (.p12)**, la **licence CIN** et les identifiants de
    connexion aux mutuelles ne se trouvent **pas** dans cet onglet, mais dans la
    configuration **[eHealth](../ehealth/index.md)**. Cet onglet ne contient
    **aucune donnée secrète** ; vous n'y saisissez ni mot de passe, ni clé.

## Facturation automatique

Ce bloc décide **comment** et **quand** les factures sont produites, et si les
périodes ouvertes se tiennent à jour toutes seules.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Facturation automatique** | Génère automatiquement les factures mensuelles des séjours, sans passer par le cycle manuel. Désactivée par défaut. | Selon votre organisation ; souvent laissée **désactivée** au profit du cycle manuel (générer → facturer), qui donne plus de contrôle. |
| **Jour de facturation** | Jour du mois où les factures automatiques sont générées (visible seulement si la facturation automatique est activée). | **1** (début de mois) par défaut ; à ajuster selon votre organisation. |
| **Actualisation automatique de la facturation** | Garde chaque période ouverte à jour dès qu'une donnée change : supplément, absence, fin de séjour, changement de chambre ou de mutuelle, admission en cours de mois. | **Activée** — recommandé. |

!!! tip "Actualisation automatique et bouton « Actualiser »"
    Avec l'actualisation **activée**, ajouter un supplément ou une absence se
    répercute tout seul sur la période : vous n'avez en général rien à faire. Le
    bouton **« Actualiser »** de la période reste disponible pour un recalcul
    complet à la demande. Voir [Facturer un mois](../facturation/facturer-un-mois.md).

## Journaux de facturation

Resthome émet **deux flux** de factures : la **part mutuelle** (forfait de
dépendance, envoyée à l'organisme assureur via l'eFact) et la **part résident**
(hébergement et suppléments). Chaque flux part dans son propre journal de vente.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Journal INAMI** | Journal de vente qui reçoit les factures de la **part mutuelle** (forfait de dépendance envoyé via l'eFact). | Un journal de vente de votre établissement. |
| **Journal résident** | Journal de vente qui reçoit les factures de la **part résident** (hébergement et suppléments). | Un journal de vente **distinct** du précédent (recommandé). |

!!! warning "Valeur propre à l'établissement"
    Ces deux journaux dépendent de **votre plan comptable**. Choisissez des
    journaux de **vente** existants. Les séparer (INAMI d'un côté, résident de
    l'autre) facilite le rapprochement et le suivi par payeur.

## Agrément de l'établissement

Certains forfaits fédéraux exigent un **agrément particulier** de l'établissement.
C'est le cas du forfait **comateux (Ccoma)**.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Agrément Cc (forfait comateux)** | À cocher si l'établissement détient l'agrément permettant de facturer le forfait comateux **Ccoma**. Sans lui, un résident classé Ccoma n'est **pas** facturable via l'eFact (ni régional, ni fédéral) ; l'hébergement reste facturé. | À cocher **seulement** si votre établissement est agréé. |

!!! note "À ne pas confondre avec le montant du forfait"
    Le **forfait de dépendance** ordinaire est le **même montant** pour toutes les
    catégories Katz ; la catégorie sert à **déclarer le profil** à la mutuelle, pas
    à fixer le montant (voir [Le forfait INAMI](../facturation/forfait-inami.md)).
    L'agrément Cc, lui, concerne uniquement le **cas particulier du forfait
    comateux**.

## Fonctionnalités optionnelles

Un module complémentaire s'installe directement depuis les réglages, en cochant
une case.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Facturation partagée (débiteurs alimentaires)** | Répartit la part résident de la facture mensuelle entre plusieurs débiteurs, chacun payant un pourcentage. Cocher cette case **installe** le module. | À activer **si** des débiteurs alimentaires se partagent la part résident. |

!!! tip "Ce que fait la case"
    Cocher installe le module et le décocher le désinstalle (convention Odoo). Une
    fois activée, la répartition se paramètre par résident. Voir
    [Débiteurs alimentaires](../facturation/split-billing.md).

## Gestion des absences

Les règles de **jours de présence** (règle de midi, hospitalisation, congés) sont
**intégrées** à Resthome et ne se paramètrent pas ici. Seul l'**assigné** d'une
activité de suivi est configurable.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Assigné de l'activité Katz** | Utilisateur à qui est assignée l'activité « Nouveau Katz requis » quand une réadmission hospitalière dépasse **30 jours**. Si vide : utilisateur courant (s'il est clinique), sinon premier infirmier-chef, infirmier ou médecin trouvé. | L'**infirmier-chef** (ou le responsable des soins). |

!!! note "Pourquoi 30 jours ?"
    Une réadmission après plus de 30 jours d'hospitalisation impose une **nouvelle
    évaluation Katz**. L'activité assignée sert de rappel. Voir
    [Absences et hospitalisations](../facturation/absences.md).

## Pour aller plus loin

- [Configuration](index.md) — chambres, tarifs, mutuelles, établissement.
- [Vue d'ensemble de la facturation](../facturation/index.md)
- [Facturer un mois, pas à pas](../facturation/facturer-un-mois.md)
- [Le forfait INAMI (dépendance)](../facturation/forfait-inami.md)
- [Débiteurs alimentaires](../facturation/split-billing.md)
- [Absences et hospitalisations](../facturation/absences.md)
