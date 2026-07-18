---
title: Praticien responsable et signature des annexes
description: "Praticien responsable eAgreement et signature des Annexes 7/10/11 dans l'app en maison de repos (MR/MRS) : résolution du NIHII et signature FEMARBEL sans imprimer."
faq:
  - q: "Qui est le praticien responsable d'une demande eAgreement ?"
    a: "C'est le clinicien qui a réalisé l'évaluation Katz (l'évaluateur), pas la personne qui envoie la demande — une secrétaire médicale peut très bien transmettre. Resthome inscrit son NIHII personnel sur la demande. S'il n'a pas de NIHII, la demande emprunte l'identité de l'infirmier-chef, puis du médecin coordinateur configurés dans les réglages eHealth."
  - q: "Où renseigner le NIHII et la signature d'un soignant ?"
    a: "Sur sa fiche employé (application Employés, onglet Nursing Home). Le NIHII, le rôle et l'image de signature vivent sur l'employé — pas sur un compte utilisateur — pour que les soignants qui signent de temps en temps ne consomment pas de licence utilisateur."
  - q: "Comment signer une Annexe 10, 7 ou 11 sans imprimer ni scanner ?"
    a: "Chargez une image de signature sur la fiche employé, puis, sur la demande eAgreement en Brouillon, cliquez sur Sign Annexe 10 (ou Sign Annexe 7 / Sign Annexe 11). Resthome appose votre signature sur le PDF et le marque signé. Si aucune image n'est configurée, l'ancien circuit imprimer / signer / scanner reste possible."
  - q: "Qui a le droit de signer une Annexe 10 (règles FEMARBEL) ?"
    a: "Par défaut, un médecin OU un infirmier. La signature d'un médecin devient obligatoire pour un Katz de catégorie D (ou Cd) et pour une révision rapide (nouvelle évaluation à moins de 6 mois de la précédente). Les Annexes 7 et 11 sont signées par le responsable de l'institution, sans règle médicale."
  - q: "Puis-je signer à la place d'un collègue ?"
    a: "Non, sauf si vous avez les droits de gestionnaire eHealth. Chacun signe avec sa propre image de signature ; signer au nom d'un autre clinicien, dont le nom et le rôle figurent sur une annexe légale, exige les droits de gestionnaire eHealth. L'auteur réel reste tracé dans le journal."
  - q: "Que se passe-t-il pour un médecin étranger sans NIHII belge ?"
    a: "Cochez « Foreign physician (no Belgian NIHII) » sur sa fiche employé (visible uniquement pour un médecin). Resthome utilise alors le numéro générique prévu par la spécification eHealth pour les praticiens étrangers, accepté par les organismes assureurs."
---

# Praticien responsable et signature des annexes

Une demande [eAgreement](eagreement.md) doit désigner un **praticien
responsable** et porter une **signature** sur ses annexes. Cette page explique
les deux mécanismes que Resthome met en place :

- **Qui est identifié** comme praticien responsable sur la demande électronique —
  et comment son numéro **NIHII** est déterminé automatiquement ;
- **Comment signer** les **Annexes 7, 10 et 11** directement dans l'application, à
  partir d'une **image de signature** stockée, au lieu d'imprimer, signer et
  scanner.

Les boutons de signature apparaissent sur la **demande eAgreement** (accessible
depuis la fiche du résident ou la période de facturation). Les identités se
configurent sur la **fiche employé** et dans les **réglages eHealth**.

!!! note "Deux identités à ne pas confondre"
    - **Le praticien responsable** : l'identité **électronique** inscrite dans la
      demande envoyée à la mutuelle — le clinicien qui a réalisé l'évaluation
      **Katz**. Resthome la **résout automatiquement** (voir plus bas).
    - **Le signataire** : la personne dont l'**image de signature** est apposée
      sur le **PDF** de l'annexe. Par défaut, c'est **vous** (l'utilisateur
      connecté).

    Dans la plupart des cas, ces deux rôles se rejoignent, mais ils sont
    distincts : une secrétaire peut envoyer une demande dont le praticien
    responsable est l'infirmier qui a coté le Katz.

## Le praticien responsable

Le praticien responsable est le **clinicien qui a réalisé l'évaluation
[Katz](../residents/katz.md)** — l'évaluateur —, **pas** la personne qui envoie la
demande. Resthome détermine son **NIHII** en descendant une chaîne de secours,
pour toujours transmettre une identité cohérente à la mutualité.

| Ordre | Resthome retient… | Quand |
|---|---|---|
| 1 | **L'évaluateur Katz**, s'il a un NIHII personnel | Cas normal |
| 2 | **L'infirmier-chef** configuré (son NIHII) | L'évaluateur (infirmier, aide-soignant) n'a pas de NIHII |
| 3 | **Le médecin coordinateur** configuré (son NIHII) | Ni l'évaluateur ni l'infirmier-chef n'ont de NIHII |
| 4 | Un **numéro infirmier générique AViQ** | Dernier recours, aucun NIHII disponible |

!!! warning "Katz de catégorie D : un médecin est obligatoire"
    Pour un Katz de **catégorie D** (ou **Cd**), la spécification impose un
    **médecin** comme praticien responsable. Resthome retient alors l'évaluateur
    s'il est médecin (avec NIHII), sinon le **médecin coordinateur** configuré. Si
    aucun médecin n'est disponible, l'envoi est **bloqué** avec un message
    explicite : renseignez un médecin coordinateur dans les réglages eHealth.

!!! info "Le numéro générique est un dernier recours"
    Si personne dans la chaîne n'a de NIHII utilisable, Resthome se rabat sur le
    **numéro infirmier générique de l'AViQ**. C'est un filet de sécurité : pour
    une identité correcte, renseignez le NIHII personnel du soignant, ou au moins
    un infirmier-chef et un médecin coordinateur de secours.

## Où sont stockées les identités (fiche employé)

Le **NIHII**, le **rôle** et l'**image de signature** d'un soignant vivent sur sa
**fiche employé**, et non sur un compte utilisateur. Ainsi, un soignant qui signe
une Annexe 10 de temps en temps **ne consomme pas de licence utilisateur** : il
suffit qu'il existe comme employé.

**Application Employés → fiche de l'employé → onglet Nursing Home.**

| Champ | À quoi ça sert |
|---|---|
| **INAMI Number** (n° NIHII/INAMI) | Le NIHII personnel du soignant, utilisé comme praticien responsable sur la demande eAgreement. 11 chiffres. |
| **Care role** (rôle de soins) | Le métier (infirmier, infirmier-chef, aide-soignant, médecin…). Il détermine le rôle eHealth. |
| **eHealth Role** (rôle eHealth) | Déduit automatiquement du rôle de soins : *nurse* (infirmier / infirmier-chef / aide-soignant) ou *physician* (médecin). En lecture seule. |
| **Foreign physician (no Belgian NIHII)** (médecin étranger) | À cocher pour un médecin transfrontalier sans NIHII belge. Visible uniquement pour un médecin. |
| **Signature image (Annexe 10)** (image de signature) | Le scan de la signature (PNG/JPG, fond transparent de préférence), apposé sur le PDF lors de la signature dans l'app. |

!!! tip "Une image de signature nette"
    Préférez une image **PNG à fond transparent**, cadrée sur le trait. Resthome
    la place dans la case « Signature » de l'annexe en **respectant ses
    proportions** — une image bien détourée rend un résultat propre.

## Configurer les identités de secours

**Réglages > Nursing Home > eAgreement Responsible Practitioner.** Ces deux
réglages fournissent le NIHII de secours quand l'évaluateur Katz n'a pas le sien.

| Réglage | À quoi ça sert |
|---|---|
| **Head Nurse (NIHII fallback)** (infirmier-chef) | Son NIHII identifie le praticien responsable quand l'évaluateur (infirmier, aide-soignant) n'a pas de NIHII personnel. |
| **Coordinating Physician (NIHII fallback)** (médecin coordinateur) | Secours quand aucun NIHII infirmier n'est disponible, et **obligatoire** pour un Katz de catégorie D. |

Voir aussi [Réglages eHealth et eFact](../configuration/reglages-ehealth.md).

!!! note "La catégorie Katz sert à déclarer, pas à fixer le montant"
    Le **forfait de dépendance** vaut le **même montant** pour toutes les
    catégories Katz (tarifs AViQ) ; la catégorie sert à **déclarer le profil** du
    résident à la mutualité. Une catégorie **D** impose toutefois un **médecin**
    comme praticien responsable — d'où l'importance du médecin coordinateur de
    secours.

## Le médecin étranger

Un médecin **transfrontalier** qui n'a **pas** de NIHII belge ne peut pas fournir
de numéro personnel. Sur sa fiche employé (rôle *médecin*), cochez **Foreign
physician (no Belgian NIHII)**. Resthome inscrit alors sur la demande le **numéro
générique prévu par la spécification eHealth** pour les praticiens étrangers, que
les organismes assureurs acceptent. Vous n'avez aucun numéro à saisir vous-même.

## Signer une annexe dans l'application

Plutôt que d'**imprimer, signer à la main puis scanner**, Resthome appose votre
**image de signature** sur le PDF de l'annexe et l'enregistre — un circuit conforme
aux règles **FEMARBEL**. Les annexes concernées :

- **Annexe 10** — l'échelle Katz (accord de soins) ;
- **Annexe 7** — l'accord d'admission (entrée / réadmission) ;
- **Annexe 11** — la notification de fin de séjour.

<!-- capture a ajouter : demande eAgreement en Brouillon avec les boutons Sign Annexe 10 / Sign Annexe 7 dans la barre d'action -->

Le parcours, sur une demande en **Brouillon** :

1. **Générez l'annexe** si ce n'est pas déjà fait (l'Annexe 10 est produite à
   partir du Katz ; l'Annexe 7 ou 11 depuis la demande).
2. Cliquez sur **Sign Annexe 10** (ou **Sign Annexe 7** / **Sign Annexe 11**). Ces
   boutons n'apparaissent qu'en Brouillon, quand l'annexe existe et n'est **pas
   encore signée**.
3. Dans la fenêtre **Sign annex**, vérifiez le **Signer** (signataire, vous par
   défaut), son **rôle**, la **date de signature** et l'**aperçu** de la signature.
4. Cliquez sur **Sign & replace PDF**. Resthome régénère un PDF propre, y appose la
   signature et coche l'annexe comme **signée** (un ✓ vert « Signed » apparaît à
   côté de l'annexe).

!!! tip "La signature est un prérequis à l'envoi"
    Tant qu'une annexe générée n'est **pas signée**, le bouton **Send Request**
    reste masqué. Signez d'abord toutes les annexes, puis envoyez. Re-signer est
    sans risque : Resthome repart d'un PDF vierge à chaque fois, sans empiler les
    signatures.

!!! note "Katz déjà signé lors de l'évaluation"
    Si l'évaluation Katz a été **signée dans l'app** au moment de la cotation, le
    PDF de l'Annexe 10 porte déjà la signature : Resthome la marque **signée
    automatiquement** et l'étape ci-dessus n'est pas nécessaire.

### Qui peut signer (règles FEMARBEL)

| Situation | Signataire autorisé |
|---|---|
| Annexe 10 — cas standard | **Médecin OU infirmier** |
| Annexe 10 — Katz **catégorie D / Cd** | **Médecin obligatoire** (pas de repli infirmier) |
| Annexe 10 — **révision rapide** (nouveau Katz à < 6 mois du précédent) | **Médecin obligatoire** |
| Annexe 7 (admission) / Annexe 11 (fin de séjour) | **Responsable de l'institution** — aucune règle médicale |

La fenêtre de signature rappelle la règle applicable dans un bandeau **FEMARBEL
signature rules**. Si la règle exige un médecin et que le signataire n'en est pas
un, la signature est refusée avec un message clair.

!!! info "Réadmission après une longue absence"
    Une **réadmission** après plus de 30 jours d'absence peut nécessiter une
    **nouvelle évaluation Katz**, mais elle n'impose **pas** de médecin :
    l'Annexe 10 peut être signée par un **médecin OU un infirmier**.

### Chacun signe avec sa propre signature

Par sécurité, vous ne pouvez signer **qu'avec votre propre** image de signature.
Signer **au nom d'un autre** clinicien — dont le nom et le rôle se retrouvent sur
une annexe légale transmise à la mutualité — exige les droits de **gestionnaire
eHealth**. Dans tous les cas, l'**auteur réel** de l'action reste enregistré dans
le journal d'audit.

### Si aucune image de signature n'est configurée

Si le signataire n'a **pas** d'image de signature sur sa fiche employé, la fenêtre
vous en avertit et le bouton **Sign & replace PDF** n'est pas proposé. Deux
options :

- **charger une image de signature** sur la fiche employé, puis recommencer ;
- **conserver le circuit manuel** : imprimer l'annexe, la faire signer, scanner le
  document signé et le re-charger sur la demande (pour l'Annexe 7 / 11, cochez
  alors **Annex signed**).

## Points clés à retenir

- Le **praticien responsable** est l'**évaluateur Katz**, pas l'expéditeur ;
  Resthome résout son **NIHII** en cascade : évaluateur → infirmier-chef → médecin
  coordinateur → numéro générique.
- Un Katz de **catégorie D** impose un **médecin** ; configurez un **médecin
  coordinateur** de secours dans les réglages eHealth.
- Le **NIHII**, le **rôle** et l'**image de signature** vivent sur la **fiche
  employé** (onglet *Nursing Home*) — pas besoin de licence utilisateur pour les
  soignants qui signent occasionnellement.
- **Sign Annexe 10 / 7 / 11** appose votre image de signature sur le PDF : plus
  besoin d'imprimer / signer / scanner. Signer est un **prérequis à l'envoi**.
- Règles **FEMARBEL** : médecin OU infirmier par défaut ; **médecin obligatoire**
  en catégorie D ou en révision rapide (< 6 mois).
- On ne signe **qu'avec sa propre** signature, sauf droits de **gestionnaire
  eHealth**.

## Pour aller plus loin

- [Accords (eAgreement)](eagreement.md)
- [Accord refusé (eAgreement) — causes et solutions](eagreement-refus.md)
- [L'échelle de dépendance (Katz)](../residents/katz.md)
- [Réglages eHealth et eFact](../configuration/reglages-ehealth.md)
- [Vue d'ensemble eHealth](index.md)
