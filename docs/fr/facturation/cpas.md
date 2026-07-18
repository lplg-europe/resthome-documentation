---
title: La prise en charge CPAS
description: "La prise en charge CPAS en maison de repos (MR/MRS) : enregistrer la décision, la couverture totale ou partielle, et router la facture de la part résident."
howto_auto: true
faq:
  - q: "Comment indiquer qu'un résident est pris en charge par le CPAS ?"
    a: "Sur la fiche du résident, ouvrez l'onglet Facturation, cochez « Pris en charge CPAS », choisissez le CPAS responsable et la couverture (totale ou partielle). Ces champs enregistrent la décision du CPAS et sont tracés dans le journal d'audit financier."
  - q: "Le CPAS paie-t-il tout ou seulement une partie ?"
    a: "Les deux cas sont prévus. « Prise en charge totale » : le CPAS prend en charge toute la part résident. « Prise en charge partielle » : le CPAS paie une part et vous saisissez le « Montant mensuel CPAS » ; le reste est à charge du résident ou de sa famille."
  - q: "Cocher « Pris en charge CPAS » envoie-t-il automatiquement la facture au CPAS ?"
    a: "Non. La section CPAS est un enregistrement de la décision, pas un moteur de répartition. Pour adresser la part résident au CPAS, renseignez le « Contact facturation » du résident (le CPAS) ; pour un partage entre le CPAS et un autre payeur, utilisez les débiteurs alimentaires (facturation partagée)."
  - q: "Où crée-t-on un CPAS dans Resthome ?"
    a: "Dans l'application Facturation → Configuration → CPAS. Créez le contact (société) et cochez « Est un CPAS ». Seuls les contacts marqués ainsi apparaissent dans le champ CPAS de la fiche résident."
  - q: "Le forfait de dépendance est-il concerné par la prise en charge CPAS ?"
    a: "Non. Le forfait de dépendance part vers la mutuelle via l'eFact (tiers payant). La prise en charge CPAS concerne uniquement la part résident : l'hébergement (la chambre) et les suppléments."
  - q: "Le montant mensuel CPAS est-il le même pour tous les résidents ?"
    a: "Non. Le montant dépend de la décision du CPAS pour ce résident : c'est une valeur propre à chaque dossier, à saisir d'après la notification reçue du CPAS."
---

# La prise en charge CPAS

Quand un résident n'a pas les moyens de couvrir sa **part personnelle** (hébergement
et suppléments), le **CPAS** (Centre Public d'Action Sociale) de sa commune peut la
**prendre en charge**, en totalité ou en partie. Resthome vous permet d'**enregistrer
cette décision** sur la fiche du résident et de **router la facture** vers le bon
débiteur.

Vous trouvez ces réglages dans l'onglet **Facturation** de la fiche résident, et la
liste des CPAS dans **Facturation → Configuration → CPAS**.

!!! note "Ce que couvre le CPAS"
    Le CPAS intervient sur la **part résident** (chambre + suppléments), pas sur le
    **forfait de dépendance** : celui-ci est pris en charge à 100 % par la mutuelle
    et facturé via l'[eFact](../ehealth/efact.md). Voir
    [Le forfait INAMI (dépendance)](forfait-inami.md).

## À quoi sert la prise en charge CPAS

Deux notions sont à distinguer :

- **Enregistrer la décision** — qui est le CPAS, à partir de quand, sous quelle
  référence, pour quelle couverture et quel montant. Ces informations documentent le
  dossier et sont **tracées dans le journal d'audit** (catégorie financière).
- **Router la facture** — décider **à qui** Resthome adresse la part résident : au
  résident, à sa famille, ou au CPAS. Ce routage se pilote via le **Contact
  facturation** ou les **débiteurs alimentaires** (voir plus bas).

<!-- capture à ajouter : onglet Facturation d'un résident avec les groupes « Payeur par défaut » et « Aide CPAS » -->

## 1. Déclarer le CPAS comme organisme

Avant de rattacher un résident à un CPAS, le CPAS doit exister comme contact.

1. Ouvrez **Facturation → Configuration → CPAS**.
2. Cliquez sur **Nouveau** et encodez le **nom** du CPAS, sa ville, son téléphone et
   son e-mail.
3. Vérifiez que la case **« Est un CPAS »** est cochée (elle l'est par défaut depuis
   ce menu).
4. **Enregistrez.**

!!! tip "Pourquoi cocher « Est un CPAS »"
    Le champ **CPAS** de la fiche résident ne propose que les contacts marqués
    **« Est un CPAS »**. Un CPAS créé ailleurs (dans les contacts génériques)
    n'apparaîtra dans la liste que si cette case est cochée sur sa fiche.

## 2. Renseigner la prise en charge sur le résident

1. Ouvrez la fiche du **résident** et l'onglet **Facturation**.
2. Dans le groupe **Aide CPAS**, cochez **Pris en charge CPAS**.
3. Sélectionnez le **CPAS** responsable.
4. Choisissez la **Couverture CPAS** : *Prise en charge totale* ou *Prise en charge
   partielle*.
5. En couverture partielle, saisissez le **Montant mensuel CPAS**.
6. Complétez la **Décision CPAS** : date, référence et, si besoin, des **Notes CPAS**.

| Champ | Rôle |
|---|---|
| **Pris en charge CPAS** | Active la prise en charge et bascule le **Payeur par défaut** sur CPAS |
| **CPAS** | L'organisme responsable (liste filtrée sur « Est un CPAS ») |
| **Couverture CPAS** | *Totale* (le CPAS paie tout) ou *Partielle* (le CPAS paie une part) |
| **Date décision CPAS** | Date de la décision d'octroi |
| **Référence décision CPAS** | Numéro / référence de la décision reçue |
| **Montant mensuel CPAS** | Montant payé par le CPAS — **couverture partielle uniquement** |
| **Notes CPAS** | Texte libre (conditions, contact, remarques) |

!!! info "Champs qui apparaissent au fur et à mesure"
    Le CPAS, la couverture et le bloc **Décision CPAS** ne s'affichent qu'une fois
    **« Pris en charge CPAS »** coché. Le **Montant mensuel CPAS** n'apparaît qu'en
    couverture **partielle**.

## 3. Router la facture vers le CPAS

C'est l'étape qui décide **à qui** part la facture de la part résident.

- **Le CPAS paie tout** → renseignez le **Contact facturation** du résident (dans le
  groupe *Payeur par défaut*) avec le contact du **CPAS**. La facture mensuelle de la
  part résident sera alors **adressée au CPAS**.
- **Le CPAS paie une partie** → utilisez les
  [débiteurs alimentaires (facturation partagée)](split-billing.md) : ajoutez le CPAS
  comme débiteur avec son **pourcentage**, et le reste des payeurs (résident, famille)
  pour le solde.

!!! warning "La section « Aide CPAS » est un enregistrement, pas un moteur de répartition"
    Les champs de la section **Aide CPAS** documentent la décision et basculent le
    **Payeur par défaut** sur CPAS, mais **ils ne redirigent pas et ne scindent pas
    automatiquement la facture**. Le destinataire de la facture reste déterminé par le
    **Contact facturation** du résident (ou le contact de facturation du séjour), et la
    répartition partielle par la **facturation partagée**. Sans l'un de ces deux
    leviers, la part résident continue d'être adressée **au résident**.

## Ce que Resthome fait — et ne fait pas

| Action | Automatique ? |
|---|---|
| Tracer la décision CPAS (audit financier) | Oui, dès la saisie |
| Basculer le **Payeur par défaut** sur CPAS quand vous cochez « Pris en charge CPAS » | Oui |
| Adresser la facture au CPAS | Non — via le **Contact facturation** |
| Répartir la part résident entre CPAS et famille | Non — via la [facturation partagée](split-billing.md) |
| Déduire le **Montant mensuel CPAS** des montants facturés | Non — champ documentaire |

## Points clés à retenir

- La prise en charge CPAS concerne la **part résident** (chambre + suppléments), pas le
  **forfait de dépendance** (part mutuelle, via eFact).
- Créez d'abord le CPAS dans **Facturation → Configuration → CPAS** (case **« Est un
  CPAS »**), puis rattachez-le au résident dans l'onglet **Facturation**.
- La couverture est **totale** ou **partielle** ; le **Montant mensuel CPAS** ne
  s'applique qu'à la couverture partielle.
- La section **Aide CPAS** **enregistre** la décision ; pour **router** la facture,
  utilisez le **Contact facturation** (couverture totale) ou la **facturation partagée**
  (couverture partielle).
- Le **Montant mensuel CPAS** et la référence de décision sont **propres à chaque
  dossier**, d'après la notification du CPAS.

## Pour aller plus loin

- [Gérer un résident](../residents/gerer-un-resident.md)
- [Facturer un mois](facturer-un-mois.md)
- [Débiteurs alimentaires (facturation partagée)](split-billing.md)
- [Le forfait INAMI (dépendance)](forfait-inami.md)