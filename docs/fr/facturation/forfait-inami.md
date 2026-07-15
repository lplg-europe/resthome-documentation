---
title: Le forfait INAMI (dépendance)
description: "Le forfait de dépendance INAMI en maison de repos, expliqué : de l'évaluation Katz à la catégorie, au montant facturé à la mutuelle, et le rôle de l'accord OA."
faq:
  - q: "Qu'est-ce que le forfait INAMI (dépendance) ?"
    a: "C'est le montant journalier pris en charge par la mutuelle pour les soins liés à la dépendance d'un résident. Il est déterminé par la catégorie de dépendance (issue de l'évaluation Katz) et calculé sur les jours de présence. Il est facturé à l'organisme assureur via l'eFact, pas au résident."
  - q: "Comment le forfait de dépendance est-il calculé ?"
    a: "Forfait = tarif journalier de la catégorie × nombre de jours de présence facturables sur la période d'intervention INAMI. Les absences réduisent les jours (règle de midi). Le tarif applicable est celui en vigueur à la date de facturation."
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
**catégorie de dépendance**, qui détermine le forfait :

| Catégorie | Dépendance | Forfait INAMI |
|---|---|---|
| **O** | Autonome | **Aucun** — non remboursée |
| **A** | Légère | oui |
| **B** | Moyenne | oui |
| **C** | Forte | oui |
| **Cd** | Forte, avec désorientation / démence | oui |
| **D** | Démence (diagnostic spécialisé) | oui |

!!! note "Catégorie O par défaut"
    Tant qu'aucune évaluation Katz n'est **validée**, le résident est facturé en
    catégorie **O** (non remboursée) et un rappel **« Katz à faire »** apparaît. Saisir
    et valider le Katz débloque le forfait correspondant.

!!! info "Patient comateux"
    Le forfait des patients **comateux** est un forfait **fédéral** particulier : il
    nécessite une **accréditation** spécifique de l'établissement. Sans elle, la ligne
    de forfait correspondante n'est pas générée (l'hébergement reste facturé).

## Comment le montant est calculé

Le forfait facturé pour un résident suit une règle simple :

> **Forfait = tarif journalier de la catégorie × nombre de jours de présence facturables**

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

- La **catégorie Katz** détermine le **forfait journalier** ; **O = non remboursée**.
- Le forfait facturé = **tarif de la catégorie × jours de présence** (période
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
