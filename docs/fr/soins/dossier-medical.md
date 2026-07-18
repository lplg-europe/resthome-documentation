---
title: Le dossier médical du résident
description: "Le dossier clinique du résident en maison de repos (MR/MRS) avec Resthome : mesures, état clinique, pathologies CIM-10, allergies, dispositifs, directives anticipées."
faq:
  - q: "Où se trouve le dossier médical d'un résident dans Resthome ?"
    a: "Sur la fiche du résident, ouvrez l'onglet Informations médicales. Il regroupe les mesures, l'état clinique, les sens et risques, les dispositifs, les diagnostics (CIM-10), les allergies, les contacts médicaux et les directives anticipées. L'onglet n'est visible que pour les résidents et réservé au personnel soignant."
  - q: "Comment saisir le poids d'un résident ?"
    a: "Le poids est en lecture seule dans le dossier : il provient de la saisie des signes vitaux. Utilisez le bouton Saisir les signes vitaux (en haut de la fiche) ou le petit + à côté du champ Poids. L'IMC est ensuite calculé automatiquement à partir de la taille et du poids."
  - q: "Comment enregistrer une pathologie ou un diagnostic ?"
    a: "Dans la section Diagnostics / Pathologies, ajoutez une ligne, choisissez la pathologie dans le catalogue CIM-10, puis réglez la sévérité et le statut (Actif ou Résolu) propres à ce résident. Une même pathologie ne peut être enregistrée qu'une fois par résident."
  - q: "Les allergies bloquent-elles vraiment une prescription ?"
    a: "Oui pour les allergènes médicamenteux. Une allergie de sévérité Critique bloque la prescription du médicament concerné ; une sévérité Élevé, Moyen ou Faible affiche un avertissement. Les allergies alimentaires et environnementales sont documentaires."
  - q: "Comment signaler un ordre de non-réanimation (DNR) ?"
    a: "Dans la section Directives anticipées, cochez Ordre DNR (Ne pas réanimer). Un bandeau d'alerte orange apparaît alors en haut de la fiche du résident, un badge DNR s'affiche sur sa carte kanban et dans la liste, et un filtre DNR permet de retrouver les résidents concernés."
  - q: "Qui peut voir le dossier médical ?"
    a: "L'accès est réservé au personnel soignant (groupe médical). Les modifications des données médicales sont journalisées à des fins de traçabilité et de conformité RGPD."
---

# Le dossier médical du résident

L'onglet **Informations médicales** de la fiche résident constitue son **dossier
clinique** dans Resthome. Il rassemble en une page les **mesures**, l'**état
clinique**, les **sens et risques**, les **dispositifs**, les **diagnostics
(CIM-10)**, les **allergies**, les **contacts médicaux** et les **directives
anticipées**.

Vous le trouvez sur la **fiche du résident** (application **Résidents** ou
**Soins**), dans l'onglet **Informations médicales**. L'onglet n'apparaît que
pour les **résidents**.

!!! warning "Accès réservé au personnel soignant"
    L'onglet **Informations médicales** et les indicateurs qui en découlent (badge
    DNR, filtres) ne sont visibles que pour le **personnel soignant**. Les
    modifications des données médicales sont **journalisées** (traçabilité et
    conformité **RGPD**).

Au-dessus de l'onglet, une série de **boutons statistiques** ouvre les autres
volets du suivi : **Prescriptions**, **Plans de soins**, **Notes**, **Katz**,
**Signes vitaux** et **Tendances**. Le dossier médical décrit ci-dessous
concentre, lui, le **profil clinique** du résident.

## Mesures et IMC

La section **Mesures** réunit les données morphologiques de base :

| Champ | Rôle |
|---|---|
| **Groupe sanguin** | Groupe sanguin du résident |
| **Taille (cm)** | Taille, saisie une fois |
| **Poids (kg)** | En lecture seule — provient des signes vitaux |
| **IMC** | Calculé automatiquement (poids / taille²) |

!!! tip "Le poids passe par les signes vitaux"
    Le champ **Poids** n'est pas saisi directement ici : il reprend la dernière
    valeur enregistrée lors d'une **saisie de signes vitaux**. Utilisez le bouton
    **Saisir les signes vitaux** en haut de la fiche, ou le petit **+** à côté du
    champ Poids. L'**IMC** se recalcule alors tout seul dès que la taille et le
    poids sont connus.

## La dépendance (Katz)

La section **Dépendance** affiche, en lecture, la synthèse de la dépendance du
résident :

- la **catégorie Katz** en cours (O, A, B, C, Cd) ;
- la **fin de validité** de l'évaluation Katz ;
- le **plan de soins actif**, s'il en existe un.

Ces informations proviennent de l'**évaluation Katz** et du **plan de soins** ;
vous ne les modifiez pas depuis le dossier médical.

!!! info "La catégorie Katz se déclare, elle ne fixe pas le montant"
    La catégorie sert à **déclarer le profil de dépendance** à la mutuelle. Dans
    les tarifs **AViQ**, le forfait de dépendance est le **même montant pour toutes
    les catégories** (voir [L'évaluation Katz](../residents/katz.md)).

## L'état clinique

La section **État clinique** décrit l'autonomie fonctionnelle du résident. Chaque
champ propose une liste de valeurs :

| Champ | Valeurs |
|---|---|
| **Mobilité** | Autonome · Canne · Déambulateur · Fauteuil roulant · Alité |
| **Continence** | Continent · Incontinence occasionnelle · Incontinence fréquente · Incontinent |
| **Statut cognitif** | Normal · Trouble léger · Trouble modéré · Trouble sévère |
| **Communication** | Normale · Difficulté · Non verbal · Aphasie |

<!-- capture à ajouter : onglet Informations médicales, sections Mesures, Dépendance et État clinique -->

## Les sens et les risques

La section **Sens & Évaluation des risques** complète le profil :

| Champ | Valeurs |
|---|---|
| **Vision** | Normale · Corrigée (lunettes) · Diminuée · Aveugle |
| **Audition** | Normale · Appareil auditif · Diminuée · Sourd |
| **Risque de chute** | Oui / Non |
| **Risque d'escarre** | Faible · Modéré · Élevé |

Ces indicateurs orientent la surveillance quotidienne et alimentent le plan de
soins.

## Les dispositifs médicaux

La section **Dispositifs médicaux** recense les dispositifs et conditions
permanentes :

- **Sonde urinaire** (oui / non) ;
- **Stomie** (oui / non) ;
- **État dentaire** : Dents naturelles · Prothèse partielle · Prothèse complète ·
  Édenté.

## Les diagnostics (pathologies CIM-10)

La section **Diagnostics / Pathologies** liste les pathologies du résident,
codées selon la **CIM-10** (classification internationale des maladies). Chaque
ligne relie le résident à une pathologie du **catalogue**.

| Colonne | Rôle |
|---|---|
| **Pathologie** | La pathologie du catalogue (code CIM-10) |
| **Catégorie** | Reprise du catalogue (circulatoire, nerveux, endocrinien…) |
| **Sévérité** | Léger · Modéré · Sévère — propre à ce résident |
| **Statut** | **Actif** ou **Résolu** |
| **Confirmé** | Diagnostic cliniquement confirmé (oui / non) |
| **Date** | Date du diagnostic |
| **Notes** | Observations cliniques |

!!! note "Sévérité et statut propres au résident"
    Le catalogue porte une sévérité **par défaut**, mais vous fixez la sévérité et
    le statut (Actif / Résolu) **pour ce résident**. Un statut *Résolu* impose une
    **date de résolution**. Une même pathologie ne peut être enregistrée **qu'une
    fois** par résident.

<!-- capture à ajouter : liste des diagnostics avec catégorie, sévérité en badge et statut Actif/Résolu -->

## Les allergies

La section **Allergies** recense les allergies **propres au résident**, reliées au
**catalogue d'allergènes**.

| Colonne | Rôle |
|---|---|
| **Allergène** | L'allergène du catalogue |
| **Catégorie** | Médicament · Aliment · Environnemental · Contact · Insecte/Venin |
| **Sévérité** | Faible · Moyen · Élevé · **Critique** — propre à ce résident |
| **Confirmé** | Allergie cliniquement confirmée (oui / non) |
| **Date** | Date d'identification |
| **Réaction** | Description de la réaction |

!!! warning "Les allergènes médicamenteux protègent la prescription"
    Pour un **allergène médicamenteux**, la sévérité pilote le comportement à la
    prescription : **Critique** **bloque** la prescription du médicament concerné ;
    **Élevé**, **Moyen** ou **Faible** affiche un **avertissement**. Les allergies
    **alimentaires** et **environnementales** sont documentaires. Voir
    [Prescriptions et médicaments](prescriptions.md).

Un champ **Notes d'allergies complémentaires** permet de consigner en texte libre
les allergies ou remarques qui ne figurent pas dans la liste structurée.

## Les contacts médicaux

La section **Contacts médicaux** relie le résident à ses intervenants de santé :

- **Médecins spécialistes** — un ou plusieurs médecins (étiquettes) ;
- **Pharmacie** de référence.

Le **médecin traitant** (médecin attitré du résident) se renseigne, lui, sur les
informations générales du résident. Ces contacts sont réutilisés ailleurs dans
Resthome (prescriptions, échanges eHealth).

## Les directives anticipées et le DNR

La section **Directives anticipées** consigne les volontés du résident :

- **Directives anticipées** (oui / non) — lorsqu'elle est cochée, un champ
  **contenu** apparaît pour en décrire la teneur ;
- **Ordre DNR (Ne pas réanimer)** — décision de non-réanimation.

!!! warning "Le DNR est signalé partout dans Resthome"
    Dès que **Ordre DNR (Ne pas réanimer)** est coché, Resthome le rend visible pour
    le personnel soignant :

    - un **bandeau orange** « DNR — Ne pas réanimer » en haut de la fiche du
      résident ;
    - un **badge DNR** sur la carte **kanban** et dans la **liste** des résidents ;
    - un **filtre DNR** dans la recherche, pour retrouver les résidents concernés.

<!-- capture à ajouter : fiche résident avec le bandeau orange DNR et la section Directives anticipées -->

## Notes médicales

Enfin, un champ **Notes médicales** en texte libre permet de consigner toute
information importante qui n'entre pas dans les rubriques structurées.

## Points clés à retenir

- Le dossier médical est l'onglet **Informations médicales** de la fiche
  résident ; il est **réservé au personnel soignant** et **journalisé** (RGPD).
- Le **poids** vient des **signes vitaux** (lecture seule) et l'**IMC** se calcule
  automatiquement à partir de la taille et du poids.
- La **catégorie Katz** et le **plan de soins actif** s'y affichent en lecture ;
  la catégorie **déclare** le profil, elle ne fixe pas le montant du forfait.
- Les **diagnostics** utilisent la **CIM-10** ; **sévérité** et **statut** (Actif /
  Résolu) sont propres au résident.
- Les **allergènes médicamenteux** protègent la prescription : **Critique** bloque,
  les autres avertissent.
- Le **DNR** déclenche un **bandeau**, un **badge kanban/liste** et un **filtre**
  de recherche.

## Pour aller plus loin

- [Prescriptions et médicaments](prescriptions.md) — allergies et interactions au moment de prescrire.
- [Plans de soins et signes vitaux](plans-de-soins.md)
- [Registres cliniques](registres.md)
- [L'évaluation Katz](../residents/katz.md) — de la dépendance à la catégorie.
