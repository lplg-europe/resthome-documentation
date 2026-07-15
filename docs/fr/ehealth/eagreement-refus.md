---
title: Accord refusé (eAgreement) — causes et solutions
description: "Pourquoi une notification d'accord (eAgreement) est refusée par la mutuelle et comment la corriger dans Resthome : NISS, assurabilité, document, Katz, doublon, puis renvoi."
faq:
  - q: "Que faire quand un accord eAgreement est refusé ?"
    a: "Lisez le motif de rejet (affiché en clair, FR et NL, sur l'accord), corrigez la cause à la source (NISS, mutuelle, assurabilité MDA, évaluation Katz, document PDF ou la bonne action métier), puis renvoyez l'accord."
  - q: "Un accusé de réception veut-il dire que l'accord est accepté ?"
    a: "Non. Un accusé électronique confirme seulement que la mutuelle a reçu la notification. Pour eAgreement Light, la décision de fond (acceptation ou refus sur le bien-fondé) revient généralement par courrier."
  - q: "Pourquoi mon accord est-il refusé immédiatement ?"
    a: "Un rejet immédiat vient d'une donnée qui bloque : NISS non reconnu ou mal formé, mutuelle inconnue, document manquant ou pas au bon format, évaluation Katz absente, établissement non reconnu, ou doublon."
  - q: "Qu'est-ce qu'un accord tacite ?"
    a: "Si la mutuelle ne se manifeste pas dans le délai réglementaire, l'accord est réputé accepté (silence = acquis). L'accusé de réception ne suffit pas : c'est l'absence de refus dans le délai qui vaut accord."
---

# Accord refusé (eAgreement) — causes et solutions

Quand un résident **entre**, **s'absente**, **revient** ou **quitte** l'établissement,
Resthome prévient automatiquement sa **mutuelle (organisme assureur, OA)** par voie
électronique, avec le bon document officiel (Annexe 7, 10 ou 11). Ce service —
**[eAgreement](eagreement.md) Light** — est **agréé** (opérationnel). La mutuelle peut
ensuite **accepter** l'accord, le laisser devenir **tacite**, ou le **refuser**.

Cette page explique **pourquoi un accord est refusé** et **comment le corriger puis le
renvoyer**.

## Deux moments où « ça bloque »

!!! info "À distinguer"
    - **Rejet technique immédiat** — une donnée cloche (NISS, document, champ obligatoire)
      et la mutuelle ou la plateforme renvoie **tout de suite** une erreur. C'est l'objet
      du tableau ci-dessous : ça se **corrige et se renvoie**.
    - **Décision de fond de la mutuelle** — pour eAgreement Light, la **vraie réponse**
      (acceptation ou refus sur le bien-fondé, p. ex. la catégorie Katz) arrive
      généralement **par courrier**, pas électroniquement.

!!! warning "Un accusé de réception n'est pas un accord"
    Un accusé électronique « bien reçu » signifie **reçu**, **pas accepté**. Ne considérez
    pas un accord comme acquis sur la seule base de l'accusé.

## Causes de refus fréquentes → action

| Cause | Ce que vous voyez | Action dans Resthome |
|---|---|---|
| **NISS non reconnu** | Rejet « bénéficiaire inconnu » ; l'accord repasse en *Rejeté* | Vérifier le NISS (carte d'identité / eID), corriger, renvoyer. |
| **NISS mal formé / incomplet** | Rejet « identifiant invalide » (format) | Ressaisir les 11 chiffres du NISS, renvoyer. |
| **Numéro de mutuelle inconnu** | Rejet « numéro de mutualité inconnu » | Vérifier la mutuelle et le n° d'affiliation ; privilégier l'identification par NISS ; renvoyer. |
| **Assurabilité (MDA) non confirmée** | Resthome **bloque l'envoi** : assurabilité pas en ordre | Relancer / mettre à jour la [vérification MDA](mda.md), corriger mutuelle/NISS, réessayer. *(Les notifications de sortie/décès ne sont pas bloquées par ce contrôle.)* |
| **Données résident incomplètes** | Rejet « donnée obligatoire manquante » (nom, identifiant) | Compléter la fiche résident, renvoyer. |
| **Document (annexe) absent ou mauvais format** | Envoi bloqué si l'annexe est vide ; sinon rejet « format de pièce invalide » | Régénérer / joindre l'Annexe **en PDF**, vérifier qu'elle s'ouvre, renvoyer. |
| **Pièce jointe trop volumineuse** | L'envoi n'aboutit pas | Alléger le PDF (réduire le poids du scan), renvoyer. |
| **Évaluation Katz manquante ou non validée** | Envoi bloqué : « évaluation Katz requise » | Créer, **confirmer** puis **valider** le Katz ; vérifier l'Annexe 10 ; renvoyer. |
| **Doublon d'accord** | Rejet « enregistrement déjà existant » | Ne pas renvoyer un accord déjà transmis ; corriger la donnée fautive (Resthome régénère alors une nouvelle notification). |
| **Mauvaise annexe / type inadapté** | Rejet « type d'accord non autorisé / incohérent » | Refaire la **bonne action métier** (admission ≠ absence ≠ sortie) : **une situation = une annexe**. |
| **Établissement ou soignant non reconnu** | Rejet « organisation / prestataire inconnu » | Faire vérifier par l'administrateur la configuration eHealth (n° INAMI établissement / soignant), renvoyer. |

## Corriger, puis renvoyer

1. **Lisez le motif.** En cas de rejet, Resthome affiche le **motif en clair, en français
   et en néerlandais**, directement sur l'accord.
2. **Corrigez la cause à la source** (fiche résident, mutuelle/NISS, MDA, évaluation Katz,
   document PDF, ou la bonne action métier).
3. **Renvoyez l'accord** une fois la donnée corrigée.
4. **Accusé de réception.** Il confirme la **réception**, pas l'acceptation.
5. **Accord tacite.** Si la mutuelle ne se manifeste pas dans le délai réglementaire,
   l'accord est **tacitement acquis** (silence = accepté).

Les statuts visibles : **Brouillon → Envoyé → Accepté / Rejeté**, avec le motif affiché en
cas de rejet.

## Bonnes pratiques (éviter le refus)

- **MDA d'abord** — vérifiez l'[assurabilité](mda.md) **avant** de préparer l'accord :
  c'est le blocage le plus fréquent, et il s'anticipe.
- **Fiche résident complète** — NISS valide (eID), mutuelle renseignée, identité correcte,
  avant tout mouvement.
- **Le bon document, une fois** — une situation = une annexe (7 admission/retour,
  10 Katz, 11 sortie/décès). Ne renvoyez pas un accord déjà transmis.
- **Katz validé** avant l'envoi pour les admissions et aggravations.
- **Certificat eHealth actif** et configuration établissement (n° INAMI) à jour.
- **Laissez Resthome faire** — gérez le résident (entrée, absence, retour, sortie) ;
  Resthome en déduit la notification. Le plus souvent : vérifier et envoyer.

## Pour aller plus loin

- [Accords (eAgreement)](eagreement.md)
- [Assurabilité (MDA)](mda.md) · [Erreurs MDA](mda-erreurs.md)
- [Rejets eFact](efact-rejets.md)
- [FAQ](../faq.md) · [Glossaire](../glossaire.md)
