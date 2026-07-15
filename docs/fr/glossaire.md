---
title: Glossaire
description: "Glossaire des termes et sigles de Resthome et de la facturation en maison de repos : MDA, eFact, eAgreement, Katz, forfait INAMI, OA, tiers payant, Annexes."
---

# Glossaire

Les termes et sigles utilisés dans Resthome et dans la facturation des maisons de
repos belges, expliqués simplement. Chaque entrée renvoie, quand c'est utile, vers
la page qui la détaille.

---

### Annexe 7

Document eHealth d'**accord d'admission** (prise en charge) transmis à la mutuelle
au démarrage d'un séjour ou lors d'une **réadmission** après une absence.
Voir : [Accords (eAgreement)](ehealth/eagreement.md)

### Annexe 10

Document de **mise à jour de l'accord de soins**, préparé lors d'une **aggravation
Katz** validée (le motif d'aggravation y est repris, la signature du clinicien le
complète).
Voir : [L'évaluation Katz](residents/katz.md)

### Annexe 11

**Notification de sortie** transmise à la mutuelle lors d'une absence de plus de
72 h, d'une hospitalisation, ou d'une fin de séjour / d'un décès.
Voir : [Absences et hospitalisations](facturation/absences.md)

### BIM (statut)

**Bénéficiaire de l'intervention majorée** : statut social donnant droit à un
meilleur remboursement. Le MDA le remonte automatiquement sur la fiche du résident.
Voir : [Assurabilité (MDA)](ehealth/mda.md)

### Cockpit eFact

Vue de **pilotage** de la facturation électronique : l'état de tous les lots et
envois d'un coup d'œil (transmis, acceptés, rejetés, en attente).
Voir : [Facturation électronique (eFact)](ehealth/efact.md)

### eAgreement

**Accord de prise en charge des soins** (lié à la catégorie Katz et au forfait),
échangé électroniquement avec la mutuelle via eHealth.
Voir : [Accords (eAgreement)](ehealth/eagreement.md)

### eAgreement Light

Les **notifications simples** liées aux **mouvements** du résident (admission,
absence, départ, retour), que Resthome génère automatiquement au fil de vos actions.
Voir : [Accords (eAgreement)](ehealth/eagreement.md)

### eFact

Envoi **électronique** de la **part mutuelle** (le forfait INAMI) aux organismes
assureurs via le réseau eHealth / MyCareNet, avec suivi des accusés, décomptes,
acceptations et rejets.
Voir : [Facturation électronique (eFact)](ehealth/efact.md)

### eHealth

Plateforme belge d'**échanges électroniques sécurisés** dans les soins de santé.
Resthome l'utilise pour le MDA, l'eAgreement et l'eFact (via MyCareNet / WalCareNet).

### Enveloppe de suppléments

Le **regroupement mensuel des suppléments** d'un résident (produits et prestations
hors forfait). Toute modification met à jour automatiquement sa facture.
Voir : [Les suppléments](facturation/supplements.md)

### Facturation anticipative

Mode de facturation où l'**hébergement** d'un mois est facturé **le mois précédent**,
tandis que le **forfait INAMI** et les **suppléments** sont facturés sur le mois de
prestation.
Voir : [Vue d'ensemble de la facturation](facturation/index.md)

### Forfait INAMI

Montant **journalier** pris en charge par la mutuelle pour les soins, déterminé par
la **catégorie Katz** du résident et calculé sur ses **jours de présence**.
Voir : [L'évaluation Katz](residents/katz.md)

### INAMI

**Institut national d'assurance maladie-invalidité** (en néerlandais : RIZIV).
L'organisme fédéral qui fixe les règles et les forfaits de l'assurance soins de santé.

### Katz (échelle de)

Échelle mesurant le **degré de dépendance** d'un résident sur 6 critères (se laver,
s'habiller, transfert et déplacements, aller à la toilette, continence, manger), cotés
de 1 à 4. Elle détermine la **catégorie** (**O**, **A**, **B**, **C**, **Cd / Cc**) et
donc le forfait.
Voir : [L'évaluation Katz](residents/katz.md)

### Lot eFact

Un **fichier électronique** regroupant les forfaits d'un envoi eFact. Resthome
constitue **un lot par union** de mutualités.
Voir : [Facturation électronique (eFact)](ehealth/efact.md)

### MDA (assurabilité)

*Member Data* — la **vérification de l'assurabilité** d'un résident et de sa
**mutuelle exacte** auprès de MyCareNet / WalCareNet pour une période donnée. Préalable
indispensable à l'eFact.
Voir : [Assurabilité (MDA)](ehealth/mda.md)

### MR / MRS

**Maison de repos** (MR) et **maison de repos et de soins** (MRS) — les deux types
d'établissement d'hébergement pour personnes âgées, avec des niveaux de soins et des
forfaits distincts. En néerlandais : ROB / RVT (regroupés sous le terme *woonzorgcentrum*).

### MyCareNet / WalCareNet

Les **guichets électroniques** des mutualités (via eHealth) que Resthome interroge
pour le MDA, l'eAgreement et l'eFact. WalCareNet est le pendant wallon.

### NISS

**Numéro d'identification à la Sécurité sociale** (le numéro de registre national).
Indispensable pour envoyer le MDA et les accords eAgreement d'un résident.
Voir : [Gérer un résident](residents/gerer-un-resident.md)

### Note de crédit

Document qui **annule ou rembourse** tout ou partie d'une facture. Resthome en prépare
une automatiquement, par exemple lors d'un départ en cours de mois déjà facturé
(hébergement facturé d'avance).
Voir : [Départ et décès](facturation/depart-deces.md)

### Organisme assureur (OA)

La **mutualité** du résident, destinataire de la part INAMI via l'eFact. Les OA sont
regroupés en grandes **unions**.
Voir : [Assurabilité (MDA)](ehealth/mda.md)

### Période de facturation

Le **mois de facturation** dans Resthome, qui passe par quatre états : **Draft**
(brouillon), **Generated** (calculée), **Invoiced** (facturée) et **Closed**
(clôturée).
Voir : [Facturer un mois, pas à pas](facturation/facturer-un-mois.md)

### Réintégration

Bascule des lignes **du résident vers la mutuelle** (ou l'inverse) quand l'assurabilité
change entre deux contrôles MDA (perte puis retour d'assurabilité, par exemple).
Voir : [Assurabilité (MDA)](ehealth/mda.md)

### Règle de midi

Convention de décompte des journées : c'est la **présence à midi** (heure de Bruxelles)
qui détermine si une journée compte pour le forfait, d'où l'importance des dates et
heures de départ et de retour.
Voir : [Absences et hospitalisations](facturation/absences.md)

### Tiers payant

Mécanisme où la **mutuelle paie directement** sa part à l'établissement (via l'eFact),
le résident ne réglant que sa propre part. En néerlandais : *derdebetaler*.

### Union de mutualités

Les grandes **familles d'organismes assureurs** utilisées pour regrouper les envois
eFact : **100** (Alliance nationale), **300** (Solidaris), **500** (Union nationale),
**600** (CAAMI), **900** (HR Rail)…
Voir : [Facturation électronique (eFact)](ehealth/efact.md)

---

## Pour aller plus loin

- [FAQ — Questions fréquentes](faq.md)
- [Le parcours de facturation](parcours-facturation.md)
- [Vue d'ensemble de la facturation](facturation/index.md)
