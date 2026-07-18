---
title: Réglages généraux (résidents, chambres)
description: "Configurer les réglages généraux d'une maison de repos (MR/MRS) dans Resthome : résidents, hébergement, responsable des chambres et de l'emménagement."
faq:
  - q: "Où se trouvent les réglages généraux ?"
    a: "Dans Réglages > Maison de Repos (résidents, hébergement, données de démonstration) et dans Réglages > Médical (tableau de bord). Ces écrans sont réservés aux gestionnaires de l'établissement."
  - q: "À quoi sert le « Responsable technique des chambres » ?"
    a: "C'est l'utilisateur qui reçoit l'activité « préparer la chambre » chaque fois qu'un résident arrive, ou qu'un changement de chambre ou un transfert ouvre un nouveau séjour. C'est un choix propre à votre établissement."
  - q: "À quoi sert le « Responsable de la procédure d'emménagement » ?"
    a: "C'est l'utilisateur qui reçoit la checklist d'emménagement (contrat, état des lieux, inventaire, armoire à médicaments, linge, désinfection) sur la fiche du résident, à l'ouverture d'un séjour. Laissé vide, la procédure est désactivée."
  - q: "Quelles valeurs par défaut pour la durée de séjour et la capacité des chambres ?"
    a: "30 jours pour la durée de séjour et 1 lit pour la capacité conviennent à la plupart des MR/MRS. Ce ne sont que des valeurs de pré-remplissage, modifiables ensuite sur chaque séjour ou chaque chambre."
  - q: "Faut-il charger les données de démonstration en production ?"
    a: "Non. Le bouton « Charger les données de démonstration » crée des résidents, chambres et factures fictifs : réservez-le à un environnement de test. Ne l'utilisez jamais sur votre base réelle."
  - q: "Que fait « Masquer les cartes de statistiques vides » ?"
    a: "Désactivé par défaut, ce réglage garde toutes les cartes du tableau de bord visibles même quand leur compteur est à 0. Activez-le seulement si vous préférez un écran plus épuré."
---

# Réglages généraux (résidents, chambres)

Cet onglet regroupe les réglages qui structurent le quotidien de votre maison :
comment sont gérés les **résidents**, l'**hébergement** (durée de séjour,
capacité, responsables), et l'affichage du **tableau de bord** de soins.

Vous les trouvez dans l'application **Réglages** :

- **Réglages > Maison de Repos (MR/MRS)** — résidents, hébergement, données de
  démonstration ;
- **Réglages > Médical** — tableau de bord.

!!! info "Réservé aux gestionnaires"
    Ces réglages ne sont visibles que pour les utilisateurs disposant du rôle
    **gestionnaire** de l'établissement. Ils se règlent une fois, puis n'évoluent
    qu'à la marge.

## Résidents

*Réglages > Maison de Repos > Résidents.* Deux options encadrent la création et
le suivi des résidents.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Informations médicales obligatoires** | Rend les informations médicales obligatoires pour tous les résidents. | Propre à l'établissement — activez-le si l'infirmier-chef exige un dossier médical complet dès l'admission. |
| **Notifier la famille** | Envoie des notifications automatiques à la famille du résident. | Propre à l'établissement — activez-le si vous communiquez avec les familles depuis Resthome. |

## Hébergement

*Réglages > Maison de Repos > Hébergement.* Ce bloc fixe les valeurs par défaut
des chambres et des séjours, et désigne **qui** est prévenu quand un résident
arrive ou change de chambre.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Durée de séjour par défaut** | Pré-remplit la durée (en jours) proposée à l'ouverture d'un nouveau séjour. | **30 jours** |
| **Capacité par défaut des chambres** | Nombre de lits pré-rempli à la création d'une nouvelle chambre. | **1 lit** (chambre individuelle) |
| **Responsable technique chambres** | Utilisateur qui reçoit l'activité « préparer la chambre » à l'arrivée d'un résident ou lors d'un changement de chambre / transfert. | L'agent technique ou d'entretien de votre maison. |
| **Responsable procédure d'emménagement** | Utilisateur qui reçoit la checklist d'emménagement (contrat, état des lieux, inventaire, armoire à médicaments, linge, désinfection) sur la fiche du résident. | Le référent admission — **laisser vide pour désactiver** la procédure. |

!!! tip "Deux responsables complémentaires"
    À chaque **[changement de chambre ou transfert](../residents/changement-chambre.md)**
    comme à l'**[admission](../residents/gerer-un-resident.md)**, Resthome ouvre
    un nouveau séjour et déclenche automatiquement :

    - une activité **« préparer la chambre »** pour le **responsable technique** ;
    - la **checklist d'emménagement** (si un **responsable de la procédure** est
      défini) sur la fiche du résident.

    Ce sont des rappels de travail : les définir évite les oublis à l'arrivée.

## Tableau de bord

*Réglages > Médical > Tableau de bord.* Un seul réglage, qui contrôle
l'affichage des cartes de statistiques du tableau de bord de soins.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Hide Empty Stat Cards** (masquer les cartes vides) | Masque les cartes du tableau de bord (soins manqués, points d'attention, renouvellements Katz…) dont le compteur est à 0. | **Laisser désactivé** (défaut) : un « 0 » affiché est un signal positif, pas un manque d'information. |

## Données de démonstration

*Réglages > Maison de Repos > Données de démonstration.* De quoi remplir une base
de **test** avec des résidents, chambres, séjours et factures fictifs.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Charger les données de démonstration** | Crée des résidents, chambres, séjours, périodes de facturation, données médicales et repas fictifs. | À réserver à un environnement de **test**. |
| **Update Demo Data** | Relance le chargeur pour ajouter les enregistrements de démonstration ajoutés depuis (mobilier, suppléments…) sans dupliquer l'existant. | Test uniquement. |

!!! warning "Jamais sur votre base réelle"
    Les données de démonstration créent des **résidents et des factures fictifs**.
    N'utilisez ces boutons que sur une base de test ou de formation, **jamais** sur
    votre environnement de production.

## Pour aller plus loin

- [Configuration](index.md)
- [Gérer un résident](../residents/gerer-un-resident.md)
- [Changement de chambre et transfert](../residents/changement-chambre.md)
- [Premiers pas](../premiers-pas.md)
- [FAQ](../faq.md) · [Glossaire](../glossaire.md)
