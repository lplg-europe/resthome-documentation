---
title: La note de frais (Annexe 12)
description: "Éditer les notes de frais Annexe 12 en maison de repos (MR/MRS) avec Resthome : note individuelle par résident et note récapitulative par organisme assureur."
faq:
  - q: "À quoi sert l'Annexe 12 dans une maison de repos (MR/MRS) ?"
    a: "C'est le document officiel AViQ qui justifie les frais d'un mois : une note de frais individuelle par résident et une note récapitulative par organisme assureur."
  - q: "Où générer l'Annexe 12 dans Resthome ?"
    a: "Via le bouton Imprimer : sur une période de facturation pour la note récapitulative, sur une fiche de facturation par résident pour la note individuelle."
  - q: "Quelle est la différence entre note individuelle et note récapitulative ?"
    a: "La note individuelle détaille les frais d'un seul résident sur trois pages ; la récapitulative liste tous les résidents d'un même organisme assureur avec les totaux."
  - q: "Quels montants figurent sur l'Annexe 12 ?"
    a: "Les trois montants obligatoires : à charge de l'organisme assureur (O.A.), à charge du patient et le total, avec le nombre de jours de présence du mois."
  - q: "Faut-il remettre l'Annexe 12 au résident ?"
    a: "Oui : un double de la note de frais individuelle doit être remis au bénéficiaire ; la note récapitulative accompagne la facturation transmise à l'organisme assureur."
---

# La note de frais (Annexe 12)

L'**Annexe 12** est le document officiel qui justifie, mois par mois, les frais
d'hébergement et de soins d'un résident de maison de repos (MR/MRS). Resthome la
produit sous deux formes complémentaires :

- la **Note de Frais Individuelle** — un justificatif détaillé **par résident** ;
- la **Note de Frais Récapitulative** — un tableau **par organisme assureur (O.A.)**
  qui regroupe tous les résidents d'une même mutuelle.

Les deux se génèrent depuis le bouton **Imprimer** (Print), à partir d'une
**période de facturation** ou d'une **fiche de facturation par résident**.

!!! info "Un document officiel AViQ"
    L'Annexe 12 vise les « institutions visées à l'article 43/7, 4° du Code wallon
    de l'action sociale et de la santé ». Resthome remplit automatiquement le
    formulaire officiel avec les données de votre période : vous n'avez rien à
    recopier à la main.

## Deux documents, deux portées

| Document | Portée | Modèle imprimé | Généré depuis |
|---|---|---|---|
| **Note de Frais Individuelle** | Un résident | `Annexe12_<résident>_<période>` | Fiche **Facturation par résident** → **Imprimer** |
| **Note de Frais Récapitulative** | Un organisme assureur | `NoteRecap_<période>` | **Période de facturation** → **Imprimer** |

!!! tip "Le lien entre les deux"
    Chaque ligne de la note récapitulative porte un **n° de note individuelle** qui
    renvoie à la note individuelle du résident correspondant. Vous éditez donc en
    général **les deux documents pour le même mois** : le récapitulatif pour l'O.A.,
    les notes individuelles pour les résidents.

## La Note de Frais Individuelle (par résident)

C'est le justificatif complet d'**un seul résident** pour le mois. Resthome le
génère sur le **formulaire officiel** en trois pages.

| Page | Contenu |
|---|---|
| **1. Récapitulatif du résident** | Identification de l'institution (nom, adresse, n° INAMI) et de la mutuelle, période, ligne du résident (nom, n° d'inscription NISS, jours de présence) et les **trois montants obligatoires** : à charge O.A., à charge patient, total. |
| **2. Frais fixes** | Le **forfait de soins** (part organisme assureur), avec son **pseudo-code AViQ**, le prix journalier, le nombre de jours et le montant — ventilé par sous-période le cas échéant — ainsi que la **ristourne incontinence**. |
| **3. Suppléments** | L'**hébergement** (la chambre), les **suppléments** (télévision, téléphone, buanderie, pédicure, chambre individuelle…), les **médicaments** (para)pharmaceutiques et le **total des suppléments**. |

!!! note "Les trois montants obligatoires"
    La première page porte les **trois montants** exigés par la facturation
    électronique : **à charge de l'O.A.** (le forfait remboursé, ristourne
    incontinence comprise), **à charge du patient** (hébergement + suppléments) et
    le **total**. Ce sont ces montants qui justifient, vis-à-vis du résident, ce que
    la mutuelle prend en charge et ce qui lui reste à payer.

!!! info "Le forfait ne dépend pas de la catégorie Katz"
    Le montant du **forfait de soins** est le **même pour toutes les catégories
    Katz** (tarifs AViQ) : la catégorie sert à **déclarer le profil de dépendance**
    à la mutuelle, pas à fixer un montant différent. Voir
    [Le forfait INAMI](forfait-inami.md).

### Éditer une note individuelle

1. Ouvrez la **période de facturation** du mois (application **MR/MRS →
   Facturation → Périodes de facturation**).
2. Ouvrez la **fiche de facturation du résident** concerné (« Facturation par
   résident »).
3. Cliquez **Imprimer → Annexe 12 — Note de Frais Individuelle**.
4. Le PDF est généré au nom du résident et de la période.

<!-- capture a ajouter : le bouton Imprimer ouvert sur une fiche de facturation par résident, montrant l'entrée « Annexe 12 — Note de Frais Individuelle » -->

!!! warning "Remettez-en un double au résident"
    La note récapitulative certifie qu'« un double de la note de frais individuelle
    a été remis au bénéficiaire ». Pensez donc à **remettre la note individuelle**
    (ou son double) à chaque résident ou à son représentant.

## La Note de Frais Récapitulative (par organisme assureur)

La note récapitulative regroupe, pour un mois, **tous les résidents d'un même
organisme assureur** sur un tableau unique. Resthome produit **une page par O.A.** :
si votre période compte des résidents affiliés à plusieurs mutuelles, le document
contient autant de pages que d'organismes.

En-tête de chaque page :

- l'**identification de l'institution** : nom, adresse, téléphone, **n° INAMI** ;
- l'**identification de la mutualité** : n° (code O.A.) et nom ;
- la **période** couverte (« Note récapitulative du … au … — établie le … »).

Le tableau des résidents comporte les colonnes suivantes :

| Colonne | Contenu |
|---|---|
| **N° note individuelle** | Référence de la note individuelle du résident |
| **Nom et prénom du bénéficiaire** | Le résident |
| **N° d'inscription** | Le NISS du résident |
| **Nombre de jours** | Jours de présence facturés |
| **À charge O.A.** | Part remboursée par l'organisme assureur |
| **À charge patient** | Part à payer par le résident |
| **Total** | Somme des deux |

La dernière ligne totalise le **Total général pour l'O.A.**, à charge patient et
total. Le document se termine par une **certification** signée du **Responsable de
l'Institution** (date, nom et signature).

### Éditer une note récapitulative

1. Ouvrez la **période de facturation** du mois (ou sélectionnez-la dans la liste
   **Périodes de facturation**).
2. Cliquez **Imprimer → Annexe 12 — Note Récapitulative**.
3. Resthome génère le PDF, **une page par organisme assureur**.

<!-- capture a ajouter : la note récapitulative générée, avec l'en-tête institution/mutualité et le tableau des résidents groupés par O.A. -->

## Quand éditer l'Annexe 12

Éditez l'Annexe 12 **une fois le mois facturé** : les montants reprennent les
lignes de facturation calculées par Resthome (forfait, hébergement, suppléments,
médicaments, absences). Si vous modifiez une facture après coup, **actualisez** la
période puis régénérez le document pour qu'il reflète les nouveaux montants.

!!! tip "Elle accompagne l'eFact"
    La note récapitulative est le justificatif « papier » qui **accompagne la
    facturation transmise** à chaque organisme assureur. Pour le flux électronique
    complet (envoi du forfait à la mutuelle), voir
    [Facturer un mois, pas à pas](facturer-un-mois.md).

!!! note "Départ ou décès en cours de mois"
    Les montants tiennent compte des **jours de présence réels** : un départ ou un
    décès en cours de mois est déjà reflété dans les lignes de facturation, donc
    dans l'Annexe 12. Voir [Départ et décès](depart-deces.md).

## Points clés à retenir

- L'Annexe 12 existe en **deux formes** : la **note individuelle** (par résident)
  et la **note récapitulative** (par organisme assureur).
- Les deux se génèrent depuis le bouton **Imprimer** : la récapitulative sur la
  **période**, l'individuelle sur la **fiche de facturation par résident**.
- La note individuelle porte les **trois montants obligatoires** : à charge O.A.,
  à charge patient et total.
- La récapitulative produit **une page par organisme assureur** et totalise le
  **Total général pour l'O.A.**.
- Un **double de la note individuelle** doit être **remis au résident**.
- Le n° INAMI de l'institution et les tarifs sont **propres à votre
  établissement** : vérifiez qu'ils sont correctement configurés.

## Pour aller plus loin

- [Facturer un mois, pas à pas](facturer-un-mois.md)
- [Les suppléments](supplements.md)
- [Vue d'ensemble de la facturation](index.md)
- [Départ et décès](depart-deces.md)