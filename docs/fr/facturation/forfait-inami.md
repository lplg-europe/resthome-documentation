---
title: Le forfait INAMI (dépendance)
description: "Le forfait de dépendance INAMI en maison de repos, expliqué : de l'évaluation Katz à la catégorie, au montant facturé à la mutuelle, et le rôle de l'accord OA."
faq:
  - q: "Qu'est-ce que le forfait INAMI (dépendance) ?"
    a: "C'est le montant journalier pris en charge par la mutuelle pour les soins liés à la dépendance d'un résident. Dans les tarifs AViQ, c'est un montant unique, le même pour toutes les catégories Katz (y compris O), calculé sur les jours de présence et facturé à l'organisme assureur via l'eFact, pas au résident. La catégorie sert à déclarer le bon profil et à obtenir l'accord de la mutuelle."
  - q: "Le montant du forfait dépend-il de la catégorie Katz ?"
    a: "Non. Dans les tarifs AViQ, le forfait de dépendance est le même montant journalier pour toutes les catégories, y compris la catégorie O (autonome). La catégorie ne change pas le montant : elle sert à déclarer le bon profil de dépendance à la mutuelle et à obtenir l'accord (eAgreement). Le tarif reste configurable par catégorie dans Configuration → INAMI Rates si une convention l'exige."
  - q: "Comment le forfait de dépendance est-il calculé ?"
    a: "Forfait = tarif journalier du forfait (identique pour toutes les catégories) × nombre de jours de présence facturables sur la période d'intervention INAMI. Les absences réduisent les jours (règle de midi). Le tarif applicable est celui en vigueur à la date de facturation."
  - q: "Pourquoi la catégorie facturée diffère-t-elle parfois de la catégorie clinique ?"
    a: "La mutuelle rembourse la catégorie qu'elle a approuvée dans l'accord (eAgreement), pas forcément votre dernière évaluation. Tant qu'un changement n'est pas accepté par l'organisme assureur, Resthome continue de facturer la catégorie précédente pour éviter un rejet."
  - q: "Qui paie le forfait de dépendance ?"
    a: "Le forfait est pris en charge à 100 % par la mutuelle (tiers payant, via l'eFact). L'hébergement (la chambre) est une ligne distincte, à charge du résident."
---

# Le forfait INAMI (dépendance)

Le **forfait de dépendance** est le montant **journalier** pris en charge par la
mutuelle pour les **soins** d'un résident. Il dépend de son **degré de dépendance**,
mesuré par l'**[évaluation Katz](../residents/katz.md)**, et il est envoyé à
l'organisme assureur (OA) via la **[facturation électronique (eFact)](../ehealth/efact.md)**.

Cette page explique la chaîne complète : **évaluation Katz → catégorie → montant
facturé**.

## De l'évaluation Katz à la catégorie

L'[évaluation Katz](../residents/katz.md) cote **6 critères** (se laver, s'habiller,
transfert et déplacements, aller à la toilette, continence, manger) de **1** (autonome)
à **4** (totalement dépendant). À partir de ces cotations, Resthome calcule une
**catégorie de dépendance**, qui est **déclarée à la mutuelle** :

| Catégorie | Dépendance | Forfait INAMI |
|---|---|---|
| **O** | Autonome | Oui (pseudo-code 770501) |
| **A** | Légère | Oui |
| **B** | Moyenne | Oui |
| **C** | Forte | Oui |
| **Cd** | Forte, avec désorientation / démence | Oui |
| **D** | Démence (diagnostic spécialisé) | Oui |

!!! important "Le montant est le même pour toutes les catégories"
    Dans les tarifs **AViQ**, le **montant** du forfait de dépendance est **identique
    pour toutes les catégories Katz**, y compris **O** : un **tarif journalier unique**,
    indexé chaque année (par ex. **85,72 €/jour en 2026**). La catégorie ne change donc
    **pas le montant** — elle sert à **déclarer le bon profil** à la mutuelle (l'**accord
    OA**) et aux **normes de soins**. Le tarif reste **configurable par catégorie** dans
    *Configuration → INAMI Rates* si une convention l'exige.

!!! note "Catégorie O par défaut"
    Tant qu'aucune évaluation Katz n'est **validée**, le résident est en catégorie **O**
    par défaut et un rappel **« Katz à faire »** apparaît. Validez l'évaluation Katz pour
    **déclarer la bonne catégorie** à la mutuelle et obtenir l'**accord** correspondant.

!!! info "Patient comateux"
    Le forfait des patients **comateux** est un forfait **fédéral** particulier : il
    nécessite une **accréditation** spécifique de l'établissement. Sans elle, la ligne
    de forfait correspondante n'est pas générée (l'hébergement reste facturé).

## Comment le montant est calculé

Le forfait facturé pour un résident suit une règle simple :

> **Forfait = tarif journalier du forfait (le même pour toutes les catégories) × nombre de jours de présence facturables**

- Les **jours de présence** sont comptés sur la **période d'intervention INAMI** (de
  l'admission à la fin d'intervention), **moins les absences**. Cette période peut être
  **plus courte** que l'hébergement (admission en cours de mois, départ, décès, fin
  d'intervention avant la libération de la chambre).
- Une **absence** (hospitalisation, vacances) **réduit** le nombre de jours, selon la
  **[règle de midi](absences.md)** (heure de Bruxelles).
- Le **tarif** appliqué est celui **en vigueur à la date** de facturation ; il est
  indexé dans le temps (voir plus bas).

!!! tip "Forfait = mutuelle · hébergement = résident"
    Le **forfait de dépendance** est pris en charge à **100 % par la mutuelle** (tiers
    payant, via l'eFact). L'**hébergement** (la chambre) est une **ligne distincte**, à
    charge du **résident**. Les deux avancent en parallèle sur la même période de
    facturation.

## Catégorie clinique et catégorie facturée

Deux notions coexistent, et il est important de ne pas les confondre :

- La **catégorie clinique** — votre **dernière évaluation Katz validée** ; elle reflète
  la dépendance réelle et sert aux soins.
- La **catégorie facturée** — celle qui figure sur la facture envoyée à la mutuelle.

**Elles peuvent différer.** La mutuelle rembourse **la catégorie qu'elle a approuvée**
dans l'**[accord (eAgreement)](../ehealth/eagreement.md)**, pas forcément votre dernière
évaluation. Concrètement :

- Si un **accord OA** est en vigueur → on facture **la catégorie de cet accord**.
- Si un **changement de catégorie** est demandé mais l'accord est **encore en attente**
  de la mutuelle → Resthome **maintient la catégorie précédente** en facturation.
- Sinon → on facture la catégorie clinique.

!!! warning "Pourquoi cette prudence ?"
    Facturer une catégorie qui **diverge de l'accord** provoque un **rejet** de l'OA
    (« forfait incompatible avec l'accord »). Tant que la nouvelle catégorie n'est pas
    **acceptée par la mutuelle**, Resthome continue donc de facturer l'ancienne. La
    catégorie affichée cliniquement peut ainsi être **plus élevée** que celle facturée.

## Aggravation de la dépendance

Si l'état d'un résident se dégrade, saisissez une **nouvelle évaluation Katz** avec un
**motif d'aggravation**. Resthome prépare la mise à jour de l'accord de soins
(**Annexe 10**), avec le motif repris automatiquement et la **signature** du clinicien.
La **nouvelle catégorie** ne devient **facturée** qu'une fois l'**accord de la mutuelle
obtenu** (voir ci-dessus).

## Configurer les tarifs de forfait

Les tarifs sont configurés dans l'application **MR/MRS → Configuration → INAMI Rates** :
un **tarif par catégorie Katz**, avec une **période de validité**. Resthome applique
automatiquement le tarif en vigueur à la date de facturation. Pour l'**indexation
annuelle**, on ajoute une nouvelle ligne de tarif (nouvelle date de début) et on clôture
l'ancienne. Le même écran gère aussi le **tarif d'hébergement** (à charge du résident).

## Points clés

- Le **forfait journalier** est le **même montant pour toutes les catégories** (y
  compris **O**) ; la catégorie sert à **déclarer le bon profil** à la mutuelle (accord OA).
- Le forfait facturé = **tarif journalier × jours de présence** (période
  d'intervention INAMI, moins les absences).
- On facture la **catégorie convenue avec la mutuelle** (accord), pas forcément la
  dernière évaluation clinique.
- **Forfait = mutuelle**, **hébergement = résident**, sur la même période.

## Pour aller plus loin

- [L'évaluation Katz](../residents/katz.md)
- [Facturation électronique (eFact)](../ehealth/efact.md) · [Rejets eFact](../ehealth/efact-rejets.md)
- [Accords (eAgreement)](../ehealth/eagreement.md)
- [Absences et hospitalisations](absences.md)
- [FAQ](../faq.md) · [Glossaire](../glossaire.md)
