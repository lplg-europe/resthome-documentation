---
title: Facturation
description: Périodes de facturation, forfaits INAMI, suppléments, absences et factures dans Resthome.
---

# Facturation

Resthome automatise la facturation MR/MRS : la **part mutuelle** (forfait INAMI)
et la **part résident** (hébergement + suppléments), période par période.

## Les grands principes

- **Période de facturation** : un mois. On la **génère**, puis on **facture**.
- **Forfait INAMI** : calculé selon la **catégorie Katz** et les jours de
  présence ; c'est la part remboursée par la mutuelle.
- **Hébergement** : la part payée par le résident (la chambre), selon le tarif.
- **Suppléments** : prestations ponctuelles ou récurrentes (chambre
  individuelle, TV, coiffeur…), via l'**enveloppe de suppléments** du résident.
- **Absences** : une absence (hospitalisation, vacances) **réduit le forfait**
  sur la période concernée et peut déclencher une notification eHealth.

!!! note "Facturation anticipative"
    Pour les résidents facturés en avance, l'hébergement d'un mois est facturé
    **le mois précédent**. Le forfait et les suppléments, eux, sont facturés sur
    le mois de prestation.

## Le bouton « Actualiser »

Sur une période de facturation, l'action **Actualiser** recalcule tout en un
clic : lignes de facturation, suppléments et factures brouillon.

!!! tip "Bon à savoir"
    - Les résidents dont la facture est **déjà comptabilisée** sont laissés
      intacts ; tout le reste est recalculé.
    - Ajouter un supplément ou une absence se **synchronise automatiquement** :
      il n'est en général pas nécessaire de cliquer « Actualiser ».

## Cycle d'une période

1. **Nouvelle période** (le mois).
2. **Générer** les lignes de facturation.
3. Vérifier l'**assurabilité (MDA)** des résidents.
4. **Créer les factures** (part résident).
5. **Comptabiliser** les factures.
6. **Générer l'eFact** (part mutuelle) puis l'envoyer.

!!! tip "Pas à pas"
    Suivez le guide détaillé [Facturer un mois, pas à pas](facturer-un-mois.md), ou
    visualisez l'ensemble du [parcours de facturation](../parcours-facturation.md).

## À suivre

- [Facturer un mois, pas à pas](facturer-un-mois.md) — le guide complet du mois.
- [Le forfait INAMI (dépendance)](forfait-inami.md) — Katz → catégorie → montant facturé.
- [Les suppléments](supplements.md) — enveloppe de suppléments, ponctuels ou récurrents.
- [Absences et hospitalisations](absences.md) — effet sur le forfait, règle des
  72 h, notification eHealth automatique.
- [Départ et décès](depart-deces.md) — arrêt de la facturation, note de crédit de
  l'hébergement prépayé.
- [Débiteurs alimentaires](split-billing.md) — répartir la part résident entre débiteurs.
- [Accords (eAgreement)](../ehealth/eagreement.md) — notifier la mutuelle
  (admission, absence, retour, sortie).
- [eHealth](../ehealth/index.md) — envoi de la part mutuelle (eFact) et accords.
- [Gérer un résident](../residents/gerer-un-resident.md)
- [Le parcours de facturation](../parcours-facturation.md) · [FAQ](../faq.md) · [Glossaire](../glossaire.md)
