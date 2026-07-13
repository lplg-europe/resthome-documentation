---
title: Absences et hospitalisations
description: Enregistrer une absence ou une hospitalisation dans Resthome — effet sur le forfait, règle des 72 h, notification eHealth automatique, annulation.
---

# Absences et hospitalisations

Quand un résident s'absente (hospitalisation, vacances, congé familial), cela
influence **le forfait INAMI** de la période et peut déclencher une
**notification à la mutuelle**. Resthome gère les deux automatiquement à partir de
l'absence que vous saisissez.

## Enregistrer une absence

1. Ouvrez la **période de facturation** du mois, ou la fiche du résident.
2. Ajoutez une **absence** en indiquant :
   - le **résident** ;
   - le **type** (hospitalisation, vacances…) ;
   - la **date/heure de départ** et la **date/heure de retour** (ou laissez le
     retour vide tant que le résident n'est pas revenu).
3. **Enregistrez.**

!!! tip "Vous n'avez pas besoin de cliquer sur « Actualiser »"
    Ajouter, modifier ou supprimer une absence **synchronise automatiquement** la
    facturation du résident concerné : le forfait est recalculé et, le cas
    échéant, la notification eHealth est préparée. Voir la
    [facturation](index.md#le-bouton-actualiser).

## Effet sur le forfait

Le **forfait INAMI** (part mutuelle) est calculé sur les **jours de présence**.
Une absence **réduit** ce forfait pour les jours concernés.

!!! note "La « règle de midi »"
    Le décompte des jours d'absence suit une règle de présence à **midi** (heure de
    Bruxelles) : c'est la présence à midi qui détermine si la journée compte. Les
    **dates et heures** de départ et de retour sont donc importantes — Resthome
    s'appuie dessus pour un décompte exact.

La **part hébergement** (la chambre, payée par le résident) suit ses propres
règles selon votre convention.

## Notification à la mutuelle (eHealth)

Certaines absences doivent être signalées à la mutuelle :

- une absence de **plus de 72 h**, ou **toute hospitalisation**, prépare une
  **Annexe 11** (notification de sortie) ;
- le **retour** du résident prépare une **Annexe 7** (réadmission).

Resthome crée ces notifications **au moment où vous enregistrez l'absence et le
retour**, sans manipulation supplémentaire. Vous n'avez qu'à les vérifier et les
envoyer. Voir [Accords (eAgreement)](../ehealth/eagreement.md).

## Annuler une absence

Une absence saisie par erreur ? **Supprimez-la** ou remettez-la en brouillon :
Resthome **fait machine arrière proprement** — le forfait est recalculé comme si
l'absence n'avait pas eu lieu, et les notifications préparées sont retirées tant
qu'elles n'ont pas été validées côté mutuelle.

!!! warning "Mois déjà facturé"
    Si la facture du mois est **déjà comptabilisée** pour ce résident, Resthome ne
    modifie pas ce mois automatiquement (protection contre la double facturation).
    Pour corriger malgré tout : repassez la facture en **brouillon** (ou créez une
    **note de crédit**), puis **actualisez**. Les autres résidents de la période
    ne sont pas touchés.

## Pour aller plus loin

- [Accords (eAgreement)](../ehealth/eagreement.md)
- [Départ et décès](depart-deces.md)
- [Vue d'ensemble de la facturation](index.md)
