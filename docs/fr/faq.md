---
title: FAQ — Questions fréquentes
description: "Réponses courtes aux questions fréquentes sur Resthome : prise en main, résidents, Katz, MDA, eAgreement, eFact, facturation, départ et décès."
faq:
  - q: "Comment vérifier l'assurabilité (MDA) d'un résident ?"
    a: "Créez une requête MDA (eHealth → Assurabilité → Requêtes MDA) avec le résident, le NISS pré-rempli et la période, puis cliquez Envoyer (Sync) : la réponse revient immédiatement. Faites-le en début de mois, avant de facturer, pour éviter les rejets eFact."
  - q: "Comment générer une période eFact ?"
    a: "Ouvrez la période du mois en état Draft, cliquez Générer, laissez Residents vide pour tous les résidents actifs, cliquez Charger MDA puis Generate. La période passe en Generated : le forfait Katz, la part INAMI et la part résident sont calculés pour chaque résident."
  - q: "Comment envoyer une période eFact et suivre les réponses ?"
    a: "Depuis le Cockpit eFact ou les lots, cliquez Tout envoyer : les lots partent vers les mutuelles via eHealth. Cliquez ensuite Récupérer les réponses ; chaque lot passe Envoyé → Accusé reçu → Accepté / Rejeté, Resthome rapprochant les montants automatiquement."
  - q: "Pourquoi une facture eFact est-elle rejetée, et comment corriger ?"
    a: "Le code et le motif de rejet indiquent la cause (assurabilité, forfait, dates). Corrigez-la puis renvoyez ; le compteur Renvois évite les doublons et le bouton Réintégration permet de réintégrer des lignes dans un nouvel envoi."
  - q: "Qu'est-ce qu'un lot eFact par union ?"
    a: "Les envois sont regroupés par union de mutualités (100 Alliance nationale, 300 Solidaris, 500 Union nationale, 600 CAAMI, 900 HR Rail…), pas par petite mutualité individuelle. Resthome s'occupe du regroupement."
  - q: "Comment calculer le Katz d'un résident ?"
    a: "Depuis la fiche du résident, ouvrez Katz, cliquez Nouveau et cotez les 6 critères (se laver, s'habiller, transfert et déplacements, aller à la toilette, continence, manger) de 1 à 4, puis Confirmez et Validez. La catégorie et le forfait se mettent à jour automatiquement."
  - q: "Quelles sont les catégories Katz ?"
    a: "O (autonome, non remboursée par l'INAMI), A (dépendance légère), B (dépendance moyenne), C (forte dépendance) et Cd / Cc (forte dépendance avec désorientation ou cas particuliers)."
  - q: "Comment facturer un mois de A à Z dans Resthome ?"
    a: "Ouvrez la période, vérifiez le MDA, cliquez Générer, Créer les factures puis comptabilisez la part résident ; ensuite Générer l'eFact, envoyez la part mutuelle aux organismes assureurs et récupérez les réponses. La part résident et la part mutuelle avancent en parallèle sur une même période."
  - q: "Comment enregistrer une absence ou une hospitalisation ?"
    a: "Ouvrez la période du mois (ou la fiche du résident) et ajoutez une absence en indiquant le type, la date/heure de départ et de retour, puis Enregistrez. La facturation du résident se synchronise automatiquement ; le forfait est réduit pour les jours d'absence selon la règle de midi."
  - q: "Que se passe-t-il au départ ou au décès d'un résident ?"
    a: "Clôturez son séjour en indiquant la date de sortie et le motif (départ, décès, transfert). Resthome arrête la facturation à la bonne date, prépare la note de crédit pour l'hébergement facturé d'avance et signale la sortie à la mutuelle."
  - q: "Qu'est-ce que la facturation anticipative dans Resthome ?"
    a: "Pour les résidents facturés en avance, l'hébergement d'un mois est facturé le mois précédent, tandis que le forfait INAMI et les suppléments sont facturés sur le mois de prestation."
  - q: "Comment ajouter un supplément à un résident ?"
    a: "Ouvrez l'enveloppe de suppléments du résident, ajoutez une ligne (produit/prestation, quantité, prix), indiquez si le supplément est ponctuel ou récurrent, puis Enregistrez. L'ajout met à jour automatiquement la facture du résident concerné."
---

# Questions fréquentes (FAQ)

Cette page regroupe des réponses courtes aux questions les plus courantes. Chaque
réponse renvoie vers la page de documentation qui la détaille.

---

## Prise en main

### Comment me connecter à Resthome ?

Ouvrez votre navigateur à l'adresse fournie par votre établissement, saisissez votre
adresse e-mail et votre mot de passe, puis cliquez sur **Se connecter**. En cas
d'oubli, utilisez le lien « Réinitialiser le mot de passe » ou demandez à votre
administrateur.
→ [Premiers pas](premiers-pas.md)

### Quelles sont les applications de Resthome ?

Resthome est organisé en applications accessibles depuis le menu principal (l'icône
en damier) : **MR/MRS** (résidents, séjours, facturation, Katz, eHealth), **Soins**
(prescriptions, plans de soins, signes vitaux), **Repas** (menus, régimes, portail
familles) et **Configuration** (chambres, tarifs, données de base). Selon votre
rôle, vous ne voyez que les applications qui vous concernent.
→ [Premiers pas](premiers-pas.md)

### À quoi sert le tableau de bord ?

Le tableau de bord de l'application MR/MRS donne une vue d'ensemble : les tâches en
attente (Katz à faire, MDA à vérifier, lots eFact…), des compteurs cliquables qui
ouvrent directement la liste concernée, et les alertes importantes du mois. Cliquez
sur un compteur (par ex. « Katz à faire ») pour ouvrir la liste des éléments à
traiter.
→ [Premiers pas](premiers-pas.md)

### Où configure-t-on les chambres et les tarifs ?

Dans l'application **Configuration** : créez vos chambres avec leur type (MR, MRS,
simple, double…) et équipements, définissez les **tarifs INAMI** (forfait par
catégorie Katz) et les **tarifs d'hébergement**, puis les types de suppléments et
les mutuelles. Resthome gère aussi **plusieurs sociétés** dans une même base, chacune
avec ses résidents, ses chambres et sa facturation cloisonnés.
→ [Configuration](configuration/index.md)

---

## Résidents & Katz

### Comment créer un résident ?

Ouvrez **MR/MRS → Résidents**, cliquez sur **Nouveau**, renseignez au minimum le
nom, la date de naissance, le genre et le **NISS** s'il est connu, sélectionnez la
mutuelle, puis **Enregistrez**. Sans NISS, la vérification MDA et les accords
eAgreement ne peuvent pas être envoyés, mais vous pouvez créer le résident et
compléter le NISS plus tard.
→ [Gérer un résident](residents/gerer-un-resident.md)

### Comment démarrer un séjour ?

Ouvrez une **convention de séjour** (chambre, type MR/MRS, date de début) — le séjour
est alors en **Brouillon**. **Confirmez**-le (la chambre est réservée, complétez
date/heure d'admission), puis cliquez **Start Stay (Démarrer)** : le séjour passe
**En cours**.
→ [Gérer un résident](residents/gerer-un-resident.md)

### Que déclenche automatiquement le démarrage d'un séjour ?

Au démarrage, Resthome ajoute le résident aux périodes de facturation ouvertes, crée
(pour un résident facturé en avance) la première facture d'hébergement du mois
d'admission, ouvre l'enveloppe de suppléments du mois et crée l'eAgreement
d'admission (si le NISS est présent).
→ [Gérer un résident](residents/gerer-un-resident.md)

### Comment calculer le Katz d'un résident ?

Depuis la fiche du résident, ouvrez **Katz**, cliquez **Nouveau** et cotez les 6
critères (se laver, s'habiller, transfert et déplacements, aller à la toilette,
continence, manger) de **1** (autonome) à **4** (totalement dépendant), puis
**Confirmez** et **Validez**. Resthome calcule la catégorie conformément à la
réglementation et met à jour le forfait automatiquement.
→ [L'évaluation Katz](residents/katz.md)

### Quelles sont les catégories Katz ?

**O** (autonome — non remboursée par l'INAMI), **A** (dépendance légère), **B**
(dépendance moyenne), **C** (forte dépendance) et **Cd / Cc** (forte dépendance avec
désorientation / cas particuliers).
→ [L'évaluation Katz](residents/katz.md)

### Que se passe-t-il tant qu'il n'y a pas de Katz validé ?

Tant qu'aucun Katz **validé** n'existe, le résident est facturé par défaut en
catégorie **O** (non remboursée par l'INAMI), et un rappel « Katz à faire » apparaît
sur le tableau de bord. Saisir et valider le Katz débloque le forfait correspondant.
→ [L'évaluation Katz](residents/katz.md)

### Comment enregistrer une aggravation Katz ?

Si l'état du résident se dégrade, saisissez une **nouvelle évaluation** avec un
**motif d'aggravation**. Resthome prépare alors la mise à jour de l'accord de soins
(**Annexe 10**) : le motif est repris automatiquement, et la signature du clinicien
complète le document.
→ [L'évaluation Katz](residents/katz.md)

### Comment changer un résident de chambre ou le transférer MR ↔ MRS ?

Sur le **séjour**, utilisez l'action **Changer de chambre** (ou **Transfert interne**
pour un changement de type de soins), indiquez la nouvelle chambre/le nouveau type et
la date/heure, puis **Validez**. Resthome scinde la facturation à la bonne date, au
tarif correspondant ; ce n'est pas une nouvelle admission et l'intervention INAMI (le
forfait) reste continue.
→ [Changement de chambre et transfert](residents/changement-chambre.md)

---

## Assurabilité (MDA)

### Qu'est-ce que le MDA et à quoi sert-il ?

Le **MDA** vérifie qu'un résident est **en ordre d'assurabilité** et identifie sa
**mutuelle exacte** en interrogeant pour vous **MyCareNet / WalCareNet** pour une
période donnée. C'est le préalable indispensable à l'envoi eFact.
→ [Assurabilité (MDA)](ehealth/mda.md)

### Comment vérifier l'assurabilité MDA d'un résident ?

Créez une **requête MDA** (menu **eHealth → Assurabilité → Requêtes MDA**) avec le
résident, le NISS pré-rempli et la période (mois courant par défaut), puis cliquez
**Envoyer (Sync)** : l'envoi est immédiat et la réponse revient tout de suite.
Consultez ensuite le résumé et les périodes d'assurabilité.
→ [Assurabilité (MDA)](ehealth/mda.md)

### Comment vérifier plusieurs résidents à la fois ?

Lancez le contrôle **par lot** : sélectionnez les résidents (vous pouvez **coller une
colonne** de noms/NISS), la période, puis envoyez tout le lot. Utilisez **Envoi
immédiat (Sync)** pour de petits volumes, ou **Envoi groupé (Async)** pour les gros
lots mensuels — la réponse se récupère ensuite avec **Vérifier les réponses**
(nécessite au moins 2 résidents).
→ [Assurabilité (MDA)](ehealth/mda.md)

### Quand faut-il faire le MDA ?

Faites le MDA **en début de mois**, avant de générer les factures : vous évitez ainsi
les rejets eFact ultérieurs dus à une mutuelle erronée ou à une perte d'assurabilité.
→ [Assurabilité (MDA)](ehealth/mda.md)

### Que veut dire « assuré mais pas en ordre » ?

Si les codes bénéficiaire reviennent à zéro (assuré mais cotisations impayées /
dossier à problème), Resthome affiche une **alerte** : le résident est affilié mais
**pas en ordre**. C'est à clarifier avec lui ou sa mutuelle avant de facturer à l'OA.
→ [Assurabilité (MDA)](ehealth/mda.md)

### Que met à jour Resthome après un MDA réussi ?

La fiche résident est corrigée automatiquement : la **mutuelle (OA)** si elle diffère
du profil, le **statut BIM**, le **numéro d'affiliation**, l'**identité** si des
champs manquaient, et la **date de décès** si l'OA la signale. Pour les résidents sous
régime particulier (INIG, CEE, Fedasil, étranger, privé…), Resthome **n'écrase pas**
la mutuelle du profil.
→ [Assurabilité (MDA)](ehealth/mda.md)

### Que faire en cas d'erreur ou d'absence de réponse MDA ?

Pour une réponse « Sans réponse » de la plateforme, utilisez **Réessayer les
sans-réponse** ; si cela persiste, **Signaler à l'intermut.** Pour un rejet de l'OA,
utilisez **Contacter l'OA** (le motif est affiché) ; pour une erreur technique,
**Signaler à l'intermut.**
→ [Assurabilité (MDA)](ehealth/mda.md)

### Qu'est-ce que la réintégration (perte puis retour d'assurabilité) ?

Resthome compare avec le contrôle précédent : si un résident passe de **non assuré à
assuré**, une notification apparaît et l'action **Réintégration** bascule vers l'OA les
lignes qui avaient été facturées au résident. À l'inverse (**assuré → non assuré**),
son forfait est exclu de la facturation OA de la période et facturé au résident
jusqu'au rétablissement.
→ [Assurabilité (MDA)](ehealth/mda.md)

---

## Accords (eAgreement)

### Qu'est-ce que l'eAgreement ?

Quand un résident entre, s'absente, revient ou quitte l'établissement, la mutuelle
doit en être informée par voie électronique. Resthome **prépare automatiquement** la
notification eHealth correspondant à votre action ; la plupart du temps, vous n'avez
rien à saisir en plus — juste à vérifier et, si besoin, à envoyer.
→ [Accords (eAgreement)](ehealth/eagreement.md)

### Quelle est la différence entre eAgreement et eAgreement Light ?

L'**eAgreement** est l'accord de prise en charge des soins (lié à la catégorie Katz
et au forfait). L'**eAgreement Light** regroupe les notifications plus simples liées
aux **mouvements** du résident (admission, absence, départ, retour) — ce sont elles que
Resthome génère tout seul au fil de vos actions.
→ [Accords (eAgreement)](ehealth/eagreement.md)

### Quel document est préparé selon l'action ?

Démarrer un séjour → **Accord d'admission (Annexe 7)** ; enregistrer une absence /
hospitalisation → **notification de sortie (Annexe 11)** ; retour du résident →
**réadmission (Annexe 7)** ; aggravation Katz validée → **mise à jour de l'accord de
soins (Annexe 10)** ; fin de séjour / décès → **notification de sortie (Annexe 11)**.
→ [Accords (eAgreement)](ehealth/eagreement.md)

### Quels sont les statuts d'un accord, et que faire en cas de rejet ?

Un accord passe par **Brouillon** (préparé, pas envoyé), **Envoyé**, **Accepté** et
**Rejeté** (avec un motif). En cas de rejet, Resthome affiche le **motif en clair, en
français et en néerlandais**, directement sur l'accord — vous savez ainsi quoi corriger
(souvent NISS, mutuelle ou dates) avant de renvoyer.
→ [Accords (eAgreement)](ehealth/eagreement.md)

### Peut-on enregistrer un mouvement sans NISS ?

Sans NISS, l'accord ne peut pas être transmis. Vous pouvez tout de même enregistrer le
mouvement (admission, absence…) : Resthome le note et vous invite à compléter le NISS
dès que possible.
→ [Accords (eAgreement)](ehealth/eagreement.md)

---

## Facturation électronique (eFact)

### Qu'est-ce que l'eFact ?

L'**eFact** est l'envoi **électronique** de la **part mutuelle** (le forfait INAMI) aux
**organismes assureurs (OA)** via le réseau eHealth / MyCareNet. Resthome constitue les
fichiers, les transmet et **suit les réponses** — accusés de réception, décomptes,
acceptations et rejets.
→ [Facturation électronique (eFact)](ehealth/efact.md)

### Quels sont les états d'une période de facturation ?

Une période passe par quatre états, dans l'ordre : **Draft** (créée, rien calculé),
**Generated** (forfaits et parts calculés, à contrôler), **Invoiced** (factures
comptabilisées, l'eFact peut être constitué et envoyé) et **Closed** (terminée et
verrouillée).
→ [Facturation électronique (eFact)](ehealth/efact.md)

### Comment générer une période eFact ?

Ouvrez la période du mois en état **Draft** et cliquez **Générer** ; dans l'assistant,
laissez **Residents** vide pour tous les résidents actifs et cliquez **Charger MDA**,
puis **Generate**. La période passe en **Generated** : Resthome a calculé, pour chaque
résident, le forfait Katz, la part INAMI et la part résident.
→ [Facturation électronique (eFact)](ehealth/efact.md)

### Comment contrôler une période avant de facturer ?

En haut de la période, des compteurs donnent l'état de santé du mois (**Suppléments**,
**Absences**, **Non facturés**, **MDA**, **Katz à faire**) et Resthome signale les
anomalies dans le fil de discussion à droite. Traitez chaque point (bouton **Terminé**
une fois réglé) avant de facturer, et lancez **Vérifier MDA** pour contrôler
l'assurabilité.
→ [Facturation électronique (eFact)](ehealth/efact.md)

### Comment générer les lots eFact ?

Une fois les factures comptabilisées (période **Invoiced**), cliquez **Générer eFact** :
Resthome constitue les **lots** — un fichier électronique par organisme assureur — puis
affiche la liste **Lots eFact** (OA, référence, mois, date limite, statut, montants
facturé/accepté/refusé, et code + motif en cas de refus).
→ [Facturation électronique (eFact)](ehealth/efact.md)

### Qu'est-ce qu'un lot par union ?

Les envois sont regroupés **par union** (les grandes familles d'OA), pas par petite
mutualité individuelle : **100** (Alliance nationale), **300** (Solidaris), **500**
(Union nationale), **600** (CAAMI), **900** (HR Rail)… Resthome s'occupe du
regroupement.
→ [Facturation électronique (eFact)](ehealth/efact.md)

### Comment envoyer une période eFact et suivre les réponses ?

Ouvrez **eHealth → eFact → Cockpit** (ou les lots) et cliquez **Tout envoyer** (ou lot
par lot) ; les envois partent vers les mutuelles via eHealth. Cliquez ensuite
**Récupérer les réponses** : chaque lot passe **Envoyé → Accusé reçu → Accepté /
Rejeté**, Resthome rapprochant automatiquement les montants acceptés/refusés.
→ [Facturer un mois, pas à pas](facturation/facturer-un-mois.md) ·
[Facturation électronique (eFact)](ehealth/efact.md)

### Je reçois un accusé de réception (931000) après l'envoi, dois-je attendre ?

**Oui.** Le **931000** confirme seulement que l'organisme assureur a **reçu** le lot et
passé le premier contrôle — ce n'est pas le résultat final. Vous n'avez **rien à
renvoyer** : attendez le **décompte (920900)**, qui indique ce qui est accepté et payé
(quelques jours). Entre-temps peuvent arriver un **920098** (avertissements, accepté malgré
tout) ou un **920099** (rejet global, à corriger et renvoyer).
→ [Facturation électronique (eFact)](ehealth/efact.md) ·
[Rejets eFact](ehealth/efact-rejets.md)

### Pourquoi une facture eFact est-elle rejetée, et comment corriger ?

Si un lot (ou une partie) est **rejeté**, le **code** et le **motif de rejet** vous
disent pourquoi (assurabilité, forfait, dates…). Corrigez la cause, puis **renvoyez** :
le compteur **Renvois** garde la trace des retransmissions pour éviter les doublons, et
le bouton **Réintégration** permet le cas échéant de réintégrer des lignes dans un
nouvel envoi.
→ [Facturation électronique (eFact)](ehealth/efact.md)

### Que signifie « échéance dépassée » sur une carte de période ?

La **date limite d'envoi** de cette période est **dépassée**. Envoyez sans tarder —
au-delà, certains organismes assureurs peuvent refuser le lot.
→ [Facturation électronique (eFact)](ehealth/efact.md)

---

## Facturation & suppléments

### Comment facturer un mois de A à Z ?

Ouvrez la période (**MR/MRS → Facturation → Périodes de facturation**), **Vérifiez le
MDA**, cliquez **Générer**, **Créer les factures** puis **Comptabilisez** la part
résident, ensuite **Générer l'eFact** et envoyez la part mutuelle aux OA, enfin
**Récupérez les réponses**. Resthome mène en parallèle la part résident (factures
classiques) et la part mutuelle (eFact) sur une même période.
→ [Facturer un mois, pas à pas](facturation/facturer-un-mois.md)

### Qu'est-ce que la facturation anticipative ?

Pour les résidents facturés en avance, l'**hébergement** d'un mois est facturé **le
mois précédent**, tandis que le **forfait** et les **suppléments** sont facturés sur le
mois de prestation.
→ [Facturation](facturation/index.md)

### À quoi sert le bouton « Actualiser » ?

Sur une période, l'action **Actualiser** recalcule tout en un clic (lignes de
facturation, suppléments, factures brouillon). Les résidents dont la facture est déjà
comptabilisée sont laissés intacts ; comme ajouter un supplément ou une absence se
synchronise automatiquement, il n'est en général pas nécessaire de cliquer
« Actualiser ».
→ [Facturation](facturation/index.md#le-bouton-actualiser)

### Comment ajouter un supplément ?

Ouvrez l'**enveloppe de suppléments** du résident (depuis sa fiche ou la période),
ajoutez une ligne (produit/prestation, quantité, prix), indiquez s'il est **ponctuel**
(une fois) ou **récurrent** (chaque mois), puis **Enregistrez**. L'ajout, la
modification ou le retrait met à jour automatiquement la facture du résident concerné —
pas besoin de cliquer « Actualiser ».
→ [Les suppléments](facturation/supplements.md)

### Comment répartir la part résident entre plusieurs débiteurs ?

Sur la fiche du résident (ou sa période), ouvrez l'onglet de **répartition**, ajoutez
les débiteurs et leur **pourcentage** (le total doit faire 100 %), puis **Enregistrez**.
À chaque facture mensuelle, Resthome découpe la part résident selon cette clé ; seule la
part résident est répartie, pas le forfait INAMI (qui part vers la mutuelle via l'eFact).
→ [Débiteurs alimentaires (facturation partagée)](facturation/split-billing.md)

### Que se passe-t-il quand une facture est déjà comptabilisée ?

Une fois **comptabilisée**, la facture d'un résident est **verrouillée** pour ce mois
(protection contre la double facturation). Pour la corriger, remettez-la en
**brouillon** ou faites une **note de crédit**, puis **Actualisez** ; les autres
résidents ne sont pas touchés.
→ [Facturer un mois, pas à pas](facturation/facturer-un-mois.md)

---

## Absences & hospitalisations

### Comment enregistrer une absence ou une hospitalisation ?

Ouvrez la période de facturation du mois (ou la fiche du résident) et ajoutez une
**absence** en indiquant le résident, le **type** (hospitalisation, vacances…), la
**date/heure de départ** et la **date/heure de retour** (ou laissez le retour vide tant
qu'il n'est pas revenu), puis **Enregistrez**. Ajouter, modifier ou supprimer une
absence synchronise automatiquement la facturation du résident concerné.
→ [Absences et hospitalisations](facturation/absences.md)

### Quel est l'effet d'une absence sur le forfait ?

Le **forfait INAMI** est calculé sur les **jours de présence** ; une absence **réduit**
ce forfait pour les jours concernés. Le décompte suit la **« règle de midi »** (heure de
Bruxelles) : c'est la présence à midi qui détermine si la journée compte, d'où
l'importance des dates et heures de départ et de retour.
→ [Absences et hospitalisations](facturation/absences.md)

### Quelles absences doivent être signalées à la mutuelle ?

Une absence de **plus de 72 h**, ou **toute hospitalisation**, prépare une **Annexe 11**
(notification de sortie), et le **retour** prépare une **Annexe 7** (réadmission).
Resthome crée ces notifications au moment où vous enregistrez l'absence et le retour ;
vous n'avez qu'à les vérifier et les envoyer.
→ [Absences et hospitalisations](facturation/absences.md)

### Comment annuler une absence saisie par erreur ?

Supprimez-la ou remettez-la en brouillon : Resthome **fait machine arrière proprement**
— le forfait est recalculé comme si l'absence n'avait pas eu lieu, et les notifications
préparées sont retirées tant qu'elles n'ont pas été validées côté mutuelle. Si le mois
est déjà comptabilisé, repassez d'abord la facture en brouillon (ou créez une note de
crédit) puis actualisez.
→ [Absences et hospitalisations](facturation/absences.md)

---

## Départ & décès

### Que se passe-t-il au départ ou au décès d'un résident ?

Il suffit de **clôturer son séjour** : ouvrez la fiche → le séjour, indiquez la **date
de sortie** (et l'heure) avec le **motif** (départ, décès, transfert…), puis
**Validez**. Resthome arrête la facturation à la bonne date, prépare la régularisation
de ce qui a été facturé d'avance et signale la sortie à la mutuelle.
→ [Départ et décès](facturation/depart-deces.md)

### Pourquoi une note de crédit est-elle créée au départ ?

Comme l'hébergement est facturé **un mois à l'avance**, si le résident part en cours de
mois déjà facturé, Resthome prépare **automatiquement une note de crédit** pour
rembourser la période non occupée (vous êtes notifié de sa création). Le forfait INAMI et
les suppléments, eux, sont facturés sur le mois presté.
→ [Départ et décès](facturation/depart-deces.md)

### Peut-on rouvrir un séjour clôturé par erreur ?

Oui. Si vous avez clôturé un séjour à tort (ou en cas de décès enregistré par erreur),
vous pouvez le **rouvrir** : Resthome rétablit la facturation et annule les
régularisations tant qu'elles ne sont pas définitives. Si le mois est déjà comptabilisé,
la correction passe d'abord par une remise en brouillon ou une note de crédit, puis une
actualisation.
→ [Départ et décès](facturation/depart-deces.md)
