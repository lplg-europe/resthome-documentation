---
title: Réglages eHealth et eFact
description: "Configurer les réglages eHealth et eFact de votre maison de repos (MR/MRS) : certificat, plateforme, Compte C wallon, licence CIN et en-tête de facturation."
faq:
  - q: "Dois-je choisir l'environnement Acceptance ou Production ?"
    a: "Restez en Acceptance (serveurs de test, aucune donnée réelle) tant que vos envois ne sont pas validés par le CIN et l'AViQ. Passez en Production seulement une fois l'agrément obtenu : à partir de là, les envois facturent réellement aux mutualités."
  - q: "Où obtenir le certificat eHealth et la licence Package CIN ?"
    a: "Le certificat .p12 s'obtient sur le portail eHealth (ehealth.fgov.be), après l'enregistrement de l'institution et la désignation du gestionnaire d'accès. La licence Package (nom d'utilisateur et mot de passe) est délivrée par le CIN/NIC lors de l'agrément du logiciel. Ces éléments ne figurent jamais en clair dans la documentation."
  - q: "Faut-il désactiver le mode stub ?"
    a: "Le mode stub simule les réponses eHealth pour tester sans appel réel. Laissez-le activé en phase de test ; désactivez-le en production, ce qui exige un certificat eHealth valide et une licence Package CIN configurée."
  - q: "Pourquoi renseigner un médecin coordinateur ?"
    a: "Son numéro NIHII sert de praticien responsable sur les demandes eAgreement quand l'évaluateur Katz n'a pas de NIHII personnel. Il est obligatoire pour un Katz de catégorie D, qui requiert un médecin."
  - q: "Le Compte C est-il obligatoire pour l'eFact en Wallonie ?"
    a: "Oui. En MR/MRS wallonne, l'organisme assureur paie les forfaits sur le compte financier C. Sans journal bancaire C renseigné, WalCareNet rejette le lot (104511 pour l'IBAN, 105311 pour le BIC absents)."
  - q: "Quelle valeur choisir pour le Type de facture (Z308) ?"
    a: "Laissez 01 (Hospitalisation) par défaut : c'est la valeur acceptée au contrôle préalable 931000. Ne passez à 03 (Ambulatoire) que si le CIN ou l'AViQ le confirme pour votre secteur."
---

# Réglages eHealth et eFact

Cet écran regroupe les **identifiants et choix techniques** que Resthome utilise
pour dialoguer avec l'écosystème e-santé belge (eHealth, MyCareNet, WalCareNet) :
assurabilité [MDA](../ehealth/mda.md), facturation
[eFact](../ehealth/efact.md) et accords [eAgreement](../ehealth/eagreement.md).

Les réglages sont répartis sur **deux onglets** :

- **Réglages > Nursing Home** : la partie **eHealth** (certificat, plateforme,
  automatisation, praticien responsable, licence CIN).
- **Réglages > MR/MRS** : la partie **facturation wallonne** (Compte C et
  en-tête eFact).

La plupart de ces valeurs se règlent **une fois**, à la mise en route, puis
n'évoluent plus qu'à la marge.

!!! warning "Champs sensibles — aucune valeur ne se recopie d'une documentation"
    Le **certificat .p12**, la **licence Package CIN** et les **mots de passe**
    sont des secrets **propres à votre établissement**. On explique ici **à quoi
    ils servent** et **où les obtenir** (portail eHealth, CIN/NIC), jamais leur
    contenu. Ne les partagez pas et ne les saisissez qu'à partir de la source
    officielle.

## Plateforme eHealth

**Réglages > Nursing Home > eHealth Platform.** Le socle : quelle identité, quel
environnement et quelle plateforme Resthome utilise pour tous les échanges.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Active Certificate** (certificat actif) | Le certificat **.p12** eHealth qui authentifie l'institution et signe les messages SOAP. À importer d'abord sous *eHealth / Certificates*, puis à sélectionner ici. | Le certificat de **votre établissement**, obtenu sur **ehealth.fgov.be**. Jamais une valeur recopiée. |
| **Institution INAMI Number** (n° INAMI de l'établissement) | Numéro INAMI/RIZIV de votre institution, utilisé dans les requêtes STS, MDA, eFact et eAgreement. | **Votre numéro** : 8 chiffres (institution) ou 11 chiffres (NIHII-11). |
| **Competence Code** (code de compétence) | Les 3 derniers chiffres du NIHII-11 (MR/MRS uniquement, pas CSJ) ; secours quand le NIHII-11 certifié ne peut être lu du jeton. | **110** (MR) ou **210** (certaines MRS). |
| **Legal Interest Rate (%)** (taux d'intérêt légal) | Taux légal belge annuel servant à calculer les intérêts de retard qu'un OA doit sur un envoi payé hors délai. | Le **taux publié pour l'année** ; **0** désactive le calcul. |
| **Care Provider NIHII** (NIHII du prestataire) | NIHII-11 **personnel** du soignant (infirmier, médecin) qui émet les demandes d'assurabilité MDA — exigé par WalCareNet/MyCareNet. | Le NIHII du **prestataire de votre établissement** (11 chiffres). |
| **Environment** (environnement) | *Acceptance* = serveurs de test (données simulées) ; *Production* = serveurs réels (facturation réelle). | **Acceptance** tant que non validé, puis **Production** après agrément. |
| **Default Platform** (plateforme par défaut) | Le réseau visé : WalCareNet (AViQ, Wallonie), MyCareNet (fédéral), IrisCareNet (Bruxelles, MDA). | **WalCareNet** pour une MR/MRS wallonne. |
| **Stub Mode (Development)** (mode stub) | Simule les réponses eHealth sans appel réel — pour tester. | **Activé** en test ; **désactivé** en production (exige certificat valide + licence CIN). |

!!! tip "Commencer prudemment"
    Au démarrage : **Acceptance + Stub Mode activé**. Vous validez tout le
    parcours sans rien envoyer de réel. Une fois l'agrément obtenu, basculez
    **Stub Mode désactivé** puis **Production**.

## Automatisation eHealth

**Réglages > Nursing Home > eHealth Automation.** Les comportements automatiques
autour de l'assurabilité et des journaux.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Auto MDA Check** (vérif. MDA auto avant facturation) | Vérifie automatiquement l'assurabilité de chaque résident avant de générer l'eFact — évite les rejets pour assurabilité invalide (voir [MDA](../ehealth/mda.md)). | **Activé** dès que le MDA est en production. |
| **Log Retention (days)** (rétention des logs) | Nombre de jours de conservation des journaux de communication et d'audit ; les plus anciens sont purgés par le cron mensuel. | **2555** (7 ans, exigence légale belge pour les données de santé). |
| **No-Facet Report Email** (e-mail rapport « no-facet ») | Adresse utilisée par le bouton *Report to intermut* sur une demande MDA restée « no-facet » (aucun OA n'a répondu dans les 24 h) — à escalader au CIN/intermut. | Laisser l'adresse **intermut** par défaut. |

## Service Desk logiciel

**Réglages > Nursing Home > Software Service Desk.** Le **1er point de contact**
en cas de problème chez un prestataire — une exigence d'agrément AViQ.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Service Desk Contact** (contact du service desk) | Le contact de l'éditeur logiciel (nom, e-mail, téléphone, logo), affiché par le bouton *Contacter LPLG* sur les demandes eAgreement. | Laisser le **contact LPLG** par défaut. |

## Praticien responsable eAgreement

**Réglages > Nursing Home > eAgreement Responsible Practitioner.** Sur une
demande [eAgreement](../ehealth/eagreement.md), le praticien responsable est le
clinicien qui a réalisé l'évaluation Katz. S'il n'a pas de NIHII personnel, la
demande emprunte l'identité de l'infirmier-chef, puis du médecin coordinateur.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Head Nurse (NIHII fallback)** (infirmier-chef) | Son NIHII identifie le praticien responsable quand l'évaluateur Katz (infirmier, aide-soignant) n'a pas de NIHII. | Renseigner l'**infirmier(ère)-chef** de l'établissement. |
| **Coordinating Physician (NIHII fallback)** (médecin coordinateur) | Secours quand aucun NIHII infirmier n'est disponible, et **obligatoire** pour un Katz de catégorie D (médecin requis). | Renseigner le **médecin coordinateur** — indispensable pour les Katz D. |

!!! note "La catégorie Katz sert à déclarer, pas à fixer le montant"
    Le **forfait de dépendance** vaut le **même montant** pour toutes les
    catégories Katz (tarifs AViQ) ; la catégorie sert à **déclarer le profil** du
    résident à la mutualité. Une catégorie **D** impose toutefois un **médecin**
    comme praticien responsable de l'eAgreement — d'où l'importance de ce champ.

## Licence Package CIN

**Réglages > Nursing Home > CIN Package License.** Les identifiants qui autorisent
Resthome à envoyer via GenAsync (eFact) et CommonInput (MDA).

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Package License Username** (nom d'utilisateur) | Nom d'utilisateur de la licence logicielle, exigé pour l'eFact et le MDA. | Fourni par le **CIN/NIC** lors de l'agrément — propre à votre logiciel. |
| **Package License Password** (mot de passe) | Mot de passe de la licence logicielle (champ masqué). | Fourni par le **CIN/NIC** ; **secret**, ne le communiquez pas. |

!!! info "Où l'obtenir"
    La licence Package est délivrée par le **CIN/NIC** au moment de l'agrément du
    logiciel. Elle n'a **aucune valeur par défaut** : tant qu'elle n'est pas
    configurée (et le mode stub désactivé), les envois réels restent bloqués.

## Compte C (Wallonie)

**Réglages > MR/MRS > Account C (Wallonia).** Depuis la 6ᵉ Réforme de l'État,
l'organisme assureur paie les forfaits MR/MRS wallons sur un **compte financier
C** dédié, déclaré au CIN lors de l'inscription eFact.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Account C Bank Journal** (journal bancaire du Compte C) | Le journal bancaire du compte wallon. L'**IBAN** (ET 10 Z 45-47a) et le **BIC** (Z 53-54a) écrits dans le 920000 en sont dérivés. | Le **journal du compte C** de votre établissement. Renseignez l'IBAN sur le compte bancaire et le BIC sur la banque. |

!!! warning "Sinon, rejet WalCareNet"
    Sans Compte C valide, WalCareNet **rejette le lot** :
    **104511** (IBAN absent) ou **105311** (BIC absent). L'IBAN et le BIC affichés
    sous le champ sont en lecture seule — ils viennent du compte bancaire du
    journal. Voir [Rejets eFact](../ehealth/efact-rejets.md).

## En-tête eFact

**Réglages > MR/MRS > eFact Header.** Les informations d'en-tête portées par
chaque message [eFact](../ehealth/efact.md) 920000 (segment 300).

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **eFact Contact Person** (personne de contact) | Nom et téléphone écrits dans l'en-tête (Z305 nom / Z306 prénom / Z307 téléphone) — la personne qu'un OA joint pour une question de facturation. | Par ex. le **directeur** de l'établissement. Si vide, le nom de l'établissement est utilisé. |
| **eFact Invoice Type (Z308)** (type de facture) | Zone Z308 « type de facture » : 01 Hospitalisation, 03 Ambulatoire, 09 Mixte. | **01** par défaut (accepté au contrôle 931000). Ne passer à **03** que si l'AViQ/CIN le confirme. |

## Pour aller plus loin

- [Configuration](index.md)
- [eHealth — vue d'ensemble](../ehealth/index.md)
- [Facturation électronique (eFact)](../ehealth/efact.md)
- [Assurabilité (MDA)](../ehealth/mda.md)
- [Accords (eAgreement)](../ehealth/eagreement.md)
- [Rejets eFact — causes et solutions](../ehealth/efact-rejets.md)