---
title: La tournée de distribution des repas
description: "Distribuer les repas en maison de repos (MR/MRS) avec Resthome : assistant tablette résident par résident, quantité mangée, feuilles imprimables par secteur."
howto_auto: true
faq:
  - q: "Où lancer la tournée de distribution des repas dans Resthome ?"
    a: "Dans l'application Repas → Opérations. Depuis un menu confirmé, cliquez sur « Distribution rapide » pour l'assistant tablette, ou imprimez la feuille de distribution du repas depuis le menu Action."
  - q: "Comment marquer un résident pendant la tournée ?"
    a: "L'assistant présente les résidents un par un avec quatre grands boutons : Servi, Passer, Absent et Chambre. Un appui enregistre le service et passe automatiquement au résident suivant en attente."
  - q: "Comment noter la quantité mangée par un résident ?"
    a: "Sur le service repas du résident (Repas → Opérations → Services repas), le champ « Quantité mangée » propose Non mangé, 25 %, 50 %, 75 % ou Tout mangé. Cette valeur alimente le suivi nutritionnel."
  - q: "À quoi servent les feuilles de distribution imprimables ?"
    a: "Ce sont des feuilles papier, une page par secteur, avec des cases à cocher (salle à manger, chambre, absent, servi) et une ligne de signature du responsable — une solution de secours quand la tablette n'est pas disponible."
  - q: "Peut-on filtrer la tournée par secteur ou par lieu ?"
    a: "Oui. Dans l'assistant, choisissez un secteur avant de cliquer sur Charger, et restreignez au besoin à la salle à manger ou aux repas en chambre."
  - q: "Que se passe-t-il si un résident mange très peu ?"
    a: "Si le résident a mangé 25 % ou moins et que sa famille est abonnée aux notifications, Resthome peut envoyer une alerte. La valeur réduit aussi la couverture nutritionnelle affichée sur la fiche du résident."
---

# La tournée de distribution des repas

La **tournée de distribution** suit chaque repas jusqu'au résident : qui mange
**où**, qui est **servi**, qui est **absent**, et **combien** chacun a mangé.
Resthome propose deux outils complémentaires, tous deux dans l'application
**Repas → Opérations** :

- l'**assistant tablette** (bouton **Distribution rapide**) pour pointer les
  résidents **un par un** à l'écran ;
- les **feuilles de distribution imprimables** par secteur, comme solution
  **papier**.

!!! note "Avant de distribuer"
    Le **menu** du repas doit être à l'état **Confirmé**. Les **services repas**
    (un enregistrement par résident et par repas) sont créés automatiquement
    quand vous démarrez la distribution — inutile de les saisir à la main.

## 1. Ouvrir l'assistant depuis le menu confirmé

1. Allez dans **Repas → Opérations → Menus** et ouvrez le menu du repas concerné.
2. S'il est encore en brouillon, cliquez sur **Confirmer** : les boutons
   **Démarrer le service** et **Distribution rapide** n'apparaissent que sur un
   menu à l'état **Confirmé**.
3. Cliquez sur **Distribution rapide** (icône tablette). L'assistant s'ouvre
   dans une fenêtre pleine largeur, adaptée à un écran tactile.

!!! tip "Démarrer le service ou Distribution rapide ?"
    **Démarrer le service** crée les services repas pour tous les résidents et
    ouvre leur **liste**. **Distribution rapide** fait la même préparation, puis
    lance directement l'**assistant** de pointage. Pour la tournée, utilisez
    **Distribution rapide**.

<!-- capture a ajouter : en-tete d'un menu confirme montrant les boutons Demarrer le service et Distribution rapide -->

## 2. Filtrer et charger la tournée

En haut de l'assistant, trois réglages cadrent la tournée :

- **Menu** — pré-rempli avec le menu d'où vous êtes parti.
- **Secteur** — optionnel : limite la tournée à un secteur (une aile, un étage).
- **Lieu** — restreint aux résidents servis en **salle à manger** ou **en
  chambre** ; laissez-le sur tous les lieux pour voir tout le monde.

Cliquez sur **Charger** pour (re)constituer la liste. Elle est triée par
**secteur**, puis **chambre**, puis **résident**, dans l'ordre où vous ferez
votre passage.

## 3. Passer les résidents en revue

Appuyez sur un résident pour ouvrir sa **carte** : photo, **chambre**,
**secteur** et **régimes**. Quatre grands boutons permettent de pointer d'un
seul geste :

| Bouton | Effet |
| --- | --- |
| **Servi** | Marque le repas comme **servi** et passe au résident suivant en attente. |
| **Passer** | Passe au résident suivant **sans rien changer** (à traiter plus tard). |
| **Absent** | Marque le résident **absent** (non servi) et passe au suivant. |
| **Chambre** | Indique que le résident mange **en chambre** et reste sur sa carte. |

L'onglet **Liste complète** affiche tous les résidents avec un **code couleur** :
**vert** = servi, **grisé** = absent, **rouge** = alerte critique, **orange** =
avertissement. Chaque ligne porte aussi ses boutons **Servi** et **Absent** pour
un pointage rapide sans ouvrir la carte.

En haut, un bandeau de **progression** compte en direct : **servis / total**,
**en attente**, **absents** et le pourcentage d'avancement.

!!! warning "Alerte allergie critique"
    Un **bandeau rouge** signale une incompatibilité grave entre un plat prévu et
    le profil du résident. Resthome **refuse de marquer « Servi »** un service
    comportant un **allergène critique** tant que les plats n'ont pas été
    adaptés. Voir [Menus, régimes et hydratation](menus-regimes.md).

<!-- capture a ajouter : carte resident de l'assistant avec les quatre grands boutons Servi / Passer / Absent / Chambre -->

## 4. Noter la quantité mangée

Le **pourcentage mangé** se consigne sur le **service repas** du résident (il ne
fait pas partie de l'assistant de pointage) :

1. Ouvrez **Repas → Opérations → Services repas** et sélectionnez le service du
   résident.
2. Renseignez le champ **Quantité mangée** :

| Option | Signification |
| --- | --- |
| **Non mangé** | Le résident n'a rien mangé. |
| **25 %** | Environ un quart du repas. |
| **50 %** | Environ la moitié. |
| **75 %** | Environ trois quarts. |
| **Tout mangé** | Repas terminé. |

La quantité mangée n'est pas qu'une note : combinée aux plats servis, elle
calcule l'**apport réel** (énergie, protéines) qui alimente la **couverture
nutritionnelle** de la fiche du résident. Voir [Suivi
nutritionnel](suivi-nutritionnel.md).

!!! info "Faible prise et familles"
    Si un résident a mangé **25 % ou moins** et que sa famille est **abonnée aux
    notifications repas**, Resthome peut envoyer une **alerte** automatique. Cette
    option s'active par résident. Voir [Portail familles et
    kiosque](portail-familles.md).

## 5. Clôturer la tournée

- Cliquez sur **Terminer** (ou **Fermer**) pour quitter l'assistant.
- Sur le menu du repas, vous pouvez ensuite cliquer sur **Marquer servi** pour
  passer le menu à l'état **Servi**.

!!! note "Traçabilité"
    Un service **servi** et un menu **Servi** ne peuvent plus être **supprimés** :
    Resthome les conserve pour la traçabilité. Corrigez plutôt les informations
    sur l'enregistrement existant.

## Le tableau de distribution (par lieu)

En complément de l'assistant tablette, **Repas → Opérations → Distribution**
ouvre un **tableau kanban** des services du jour **regroupés par lieu** (salle à
manger, en chambre, absent). Chaque carte montre la photo, la **chambre**, le
**secteur**, le badge de **régime** et, le cas échéant, un badge **Alerte**,
**Avertissement** ou **Servi**.

Depuis la **liste** des services repas, deux boutons d'en-tête permettent
d'agir sur une **sélection multiple** : **Marquer servis** et **Marquer
absents**. Le menu **Action** propose aussi de marquer les services **en salle à
manger** ou **en chambre**.

## Les feuilles imprimables par secteur

Quand vous préférez le **papier**, imprimez les feuilles depuis un **menu** (vue
formulaire ou liste), via le menu **Action** : vous pouvez imprimer la **feuille
de distribution** d'un repas, ou **toutes les feuilles du jour**. Resthome crée
au passage les services manquants, puis ouvre le document.

La feuille se présente ainsi :

- **une page par secteur**, avec en-tête : **secteur**, **type de repas**,
  **date** et **nombre de résidents** ;
- un tableau : **#**, **Résident**, **Chambre**, **Régimes / Allergies** (badges
  **bleus** pour les régimes, **rouges** pour les allergies, « **!** » pour une
  alerte critique), puis des **cases à cocher** **Salle à manger**, **Chambre**,
  **Absent** et **Servi**, et une colonne **Notes** ;
- un pied de page avec une ligne **Signature du responsable** et la **date et
  l'heure d'impression**.

C'est une **check-list de terrain** : le personnel coche les cases au fil de la
tournée, fait signer le responsable, puis reporte les informations dans Resthome.

<!-- capture a ajouter : feuille de distribution imprimee d'un secteur avec les cases a cocher et la ligne de signature -->

## Points clés à retenir

- La tournée vit dans **Repas → Opérations** ; elle démarre depuis un menu à
  l'état **Confirmé**.
- **Distribution rapide** est l'assistant tablette : quatre boutons **Servi**,
  **Passer**, **Absent**, **Chambre**, avec avancement automatique au résident
  suivant.
- La **Quantité mangée** (Non mangé → Tout mangé) se note sur le **service
  repas** et nourrit le **suivi nutritionnel**.
- Les **feuilles imprimables par secteur** (cases à cocher + signature) sont la
  solution papier de secours.
- Un service ou un menu **servi** ne se supprime pas : Resthome garde la trace.

## Pour aller plus loin

- [Menus, régimes et hydratation](menus-regimes.md)
- [Suivi nutritionnel](suivi-nutritionnel.md)
- [Portail familles et kiosque](portail-familles.md)
- [Vue d'ensemble de l'application Repas](index.md)