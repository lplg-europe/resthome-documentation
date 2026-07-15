---
title: Erreurs MDA — causes et solutions
description: "Résoudre les erreurs et cas particuliers du MDA (assurabilité) dans Resthome : NISS erroné, bénéficiaire inconnu, « pas en ordre », sans réponse, mutation, régimes spéciaux."
faq:
  - q: "Que faire quand le MDA renvoie une erreur ?"
    a: "Selon le message : si le NISS est en cause (le plus fréquent), corrigez-le sur la fiche puis Réessayez ; si c'est « sans réponse » (souvent hors horaires), réessayez plus tard ; si l'erreur est technique ou persiste, Signalez à l'intermutualiste."
  - q: "Que signifie « assuré mais pas en ordre » ?"
    a: "Le résident est affilié mais sa couverture n'est pas valide sur la période (cotisations impayées, dossier à régulariser). Ne facturez pas l'organisme assureur : clarifiez avec le résident ou sa mutualité, et facturez la part au résident en attendant."
  - q: "Le MDA n'a pas trouvé le résident, pourquoi ?"
    a: "Soit le NISS est mal saisi (format refusé), soit il est correct mais pas encore connu de la plateforme (inscription très récente, cas particulier). Vérifiez le NISS ; s'il est bon, contactez la mutualité."
  - q: "Que met à jour Resthome après un MDA réussi ?"
    a: "La mutualité (organisme assureur) réel, le statut BIM, le numéro d'affiliation, l'identité si des champs manquaient, et la date de décès si l'organisme la signale. Pour un régime particulier, la mutualité du profil n'est pas écrasée."
---

# Erreurs MDA — causes et solutions

Le [MDA](mda.md) interroge pour vous la plateforme des mutualités (MyCareNet /
WalCareNet) pour confirmer qu'un résident est **assuré sur la période** et identifier
**la mutualité qui le couvre réellement**. C'est le **préalable à l'eFact**. Cette page
regroupe les erreurs et cas particuliers, avec la marche à suivre.

!!! tip "Le bon réflexe"
    Lancez le MDA **en début de mois, avant de générer les factures** : vous évitez les
    [rejets eFact](efact-rejets.md) ultérieurs dus à une mauvaise mutualité ou à une
    perte d'assurabilité découverte trop tard.

## Situations MDA → action

Rappel des statuts que Resthome peut afficher : **Brouillon · Envoyé / En attente ·
Succès · Non assuré · Sans réponse · Erreur**. Actions disponibles : **Envoyer ·
Vérifier la réponse · Réessayer · Contacter l'OA · Signaler à l'intermut.**

| Situation | Ce que Resthome affiche | Cause probable | Action |
|---|---|---|---|
| **NISS non reconnu** | **Erreur** : la demande est refusée avant d'arriver à une mutualité | Le **NISS** est mal saisi (chiffre inversé, faute de frappe) : format invalide | Vérifier le NISS (carte d'identité), **le corriger**, puis **Réessayer**. C'est la cause la plus fréquente. |
| **Bénéficiaire introuvable** | **Erreur** : « non trouvé » | NISS bien formé mais **pas (encore) connu** de la plateforme (inscription très récente, cas particulier) | Confirmer le NISS et l'affiliation. Si le numéro est correct : **Contacter l'OA** ; en dernier recours **Signaler à l'intermut.** |
| **Assuré mais « pas en ordre »** | **Non assuré** + **alerte** | Affiliation existante mais **couverture non valide** (cotisations impayées, dossier à régulariser) | Ne pas facturer l'OA pour cette période. **Contacter l'OA** ou le résident pour régulariser ; facturer la part **au résident** en attendant. |
| **Pas de mutualité sur la fiche** | Non bloquant : après un MDA réussi, la mutualité est **remplie automatiquement** | Profil incomplet (nouveau résident) | Lancer le MDA : s'il aboutit, Resthome **renseigne** la mutualité et le n° d'affiliation. Sinon, revérifier le NISS. |
| **Changement de mutualité (mutation)** | **Mutation détectée** : le profil est **mis à jour** | Le résident a changé de mutualité ; le profil n'était pas à jour | Laisser Resthome corriger le profil ; **vérifier** la nouvelle mutualité avant de facturer. |
| **« Sans réponse »** | **Sans réponse** | La plateforme a clôturé la demande sans réponse — souvent **hors horaires** (soir/week-end) ou indisponibilité temporaire. Ce n'est pas une erreur de votre part | **Réessayer** aux heures ouvrables. Si cela persiste, **Signaler à l'intermut.** |
| **Erreur technique** | **Erreur** + détail technique | Panne temporaire côté plateforme ou mutualité | **Réessayer** plus tard ; si l'erreur revient, **Signaler à l'intermut.** Ne pas relancer en boucle. |
| **Décès signalé par la mutualité** | **Date de décès** sur la fiche + alerte | L'OA signale un décès (couverture close) | Vérifier et **arrêter la facturation** à la bonne date. |
| **Régime particulier** | La réponse MDA est **ignorée** ; la mutualité du profil **reste inchangée** | Le résident relève d'un régime spécial (voir plus bas) | Ne rien corriger : le garde-fou est **volontaire**. Facturer selon le régime particulier. |

## Régimes particuliers

Certains résidents ne relèvent **pas** du flux mutualité standard. Dans ces cas,
Resthome **n'écrase pas** la mutualité de leur profil avec la réponse du MDA, et la
facturation se fait souvent **sur papier**, adressée au véritable payeur (ou au
résident), plutôt qu'en eFact.

- **Statut BIM (intervention majorée)** — ce n'est pas un régime à part : le MDA le
  **récupère et met à jour tout seul**. Il ouvre droit à un **ticket modérateur réduit**
  pour le résident (la part à sa charge diminue) ; le forfait journalier, lui, est
  inchangé.
- **Invalides de guerre / victimes civiles** — le résident a **deux couvertures** : sa
  mutualité standard (visible dans le MDA) **et** une couverture spécifique qui **ne
  passe pas** par le MDA. Le garde-fou évite d'écraser cette configuration.
- **Retraités d'institutions internationales** — couverts par un régime propre à leur
  organisation, pas par une mutualité belge classique.
- **Pensionnés étrangers** — couverture d'un régime étranger via les formulaires
  européens de coordination ; en pratique, beaucoup s'affilient tout de même à une
  mutualité belge.

!!! warning "En cas de doute"
    Pour un régime particulier, en cas de doute sur l'organisme à facturer, rapprochez-
    vous de la mutualité ou de l'organisme concerné avant d'émettre la facture.

## Bonnes pratiques

- **MDA en début de mois, avant de facturer.**
- **Contrôle individuel** (immédiat) pour un résident précis ; **contrôle par lot**
  pour une période entière — collez au besoin une colonne de noms/NISS.
    - **Envoi immédiat (Sync)** pour les **petits volumes** ;
    - **Envoi groupé (Async)** pour les **gros lots mensuels** : la demande part, puis
      on **récupère les réponses** un peu plus tard avec **Vérifier les réponses**
      (nécessite au moins 2 résidents).
- Le lot affiche des **compteurs** (Assurés, Non assurés, Erreurs, En attente, Décès)
  pour repérer d'un coup d'œil ce qui reste à traiter.
- **Ce que Resthome met à jour** après un MDA réussi : la **mutualité (OA)** réelle, le
  **statut BIM**, le **numéro d'affiliation**, l'**identité** si des champs manquaient,
  et la **date de décès** si l'organisme la signale. Exception : la mutualité d'un
  **régime particulier** n'est pas écrasée.

## Pour aller plus loin

- [Assurabilité (MDA)](mda.md)
- [Rejets eFact](efact-rejets.md) · [Facturation électronique (eFact)](efact.md)
- [FAQ](../faq.md) · [Glossaire](../glossaire.md)
