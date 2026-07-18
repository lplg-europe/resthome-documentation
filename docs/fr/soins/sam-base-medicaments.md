---
title: La base de médicaments SAM
description: "La base authentique belge SAM dans Resthome : référentiel ATC, classe BCFI, Triangle noir, RCP/notice et assistant Search SAM pour la maison de repos (MR/MRS)."
howto_auto: true
faq:
  - q: "Qu'est-ce que la base SAM ?"
    a: "SAM (Source Authentique des Médicaments) est le référentiel officiel belge des médicaments. Resthome en embarque une copie pour alimenter le catalogue de votre maison de repos (MR/MRS) avec des données fiables : code CNK, principe actif, code ATC, classe BCFI, notices."
  - q: "Où trouver la base SAM dans Resthome ?"
    a: "Deux accès. La consultation, via l'application Soins → Configuration → Base de données SAM. Et l'assistant d'import « Search SAM », via l'application MR/MRS → Configuration → eHealth Configuration → Search SAM."
  - q: "Comment ajouter un médicament SAM à mon catalogue ?"
    a: "Ouvrez l'assistant Search SAM, cherchez par nom ou par code CNK, cochez les lignes voulues et cliquez sur Import Selected. Les médicaments sont créés dans votre catalogue avec leurs données SAM."
  - q: "Que signifie « Triangle noir » ?"
    a: "Le triangle noir signale un médicament sous surveillance renforcée (pharmacovigilance additionnelle). L'information est reprise depuis SAM, à titre indicatif, sur la fiche de référence."
  - q: "La recherche fonctionne-t-elle sans connexion eHealth ?"
    a: "Oui. La recherche s'appuie d'abord sur la copie locale de SAM, disponible hors ligne et instantanée. Le service live DICS v5 n'est utilisé qu'en secours et exige une connexion eHealth certifiée."
  - q: "Comment mettre à jour un médicament déjà présent ?"
    a: "Relancez la recherche et réimportez la ligne. Si le code CNK existe déjà dans le catalogue, Resthome met à jour la fiche existante au lieu d'en créer une seconde."
---

# La base de médicaments SAM

**SAM** (Source Authentique des Médicaments) est le référentiel officiel belge
des médicaments. Resthome l'utilise comme socle de son **catalogue de
médicaments** : plutôt que de saisir un médicament à la main, vous le recherchez
dans SAM et vous l'importez, avec ses données fiables (code CNK, principe actif,
classification, notices).

Deux portes d'entrée :

- **Consulter** le référentiel — application **Soins** → **Configuration** →
  **Base de données SAM** (lecture seule).
- **Rechercher et importer** — l'assistant **Search SAM**, dans l'application
  **MR/MRS** → **Configuration** → **eHealth Configuration** → **Search SAM**.

!!! info "Une fonctionnalité de l'intégration eHealth"
    L'assistant **Search SAM** fait partie de la couche eHealth belge de Resthome.
    Il s'installe automatiquement dès que le module médical et le module eHealth
    sont présents, et son accès est réservé au **gestionnaire eHealth**. La
    consultation de la base (Soins → Configuration) reste, elle, accessible sans
    ce rôle.

## Ce que la base SAM apporte

Chaque médicament de la base de référence porte des données authentiques,
utiles au soin comme à la traçabilité :

| Donnée | À quoi elle sert |
| --- | --- |
| **Code CNK** | Code pharmacie belge (7 chiffres) qui identifie le conditionnement. |
| **Principe actif (DCI)** | La substance active, en français et en néerlandais. |
| **Code ATC** | Classification anatomique, thérapeutique et chimique (OMS), avec sa description. |
| **Classe BCFI** | Classement pharmacothérapeutique du Centre Belge d'Information Pharmacothérapeutique. |
| **Triangle noir** | Signale un médicament sous surveillance renforcée (pharmacovigilance additionnelle). |
| **Forme et voie** | Forme pharmaceutique et voie d'administration, en français et en néerlandais. |
| **RCP et notice** | Liens vers le Résumé des Caractéristiques du Produit et la notice patient (FR et NL). |
| **Lien BCFI** | Renvoi direct vers la fiche du médicament sur le site du BCFI. |
| **Prescription et fabricant** | Statut de délivrance (prescription requise) et titulaire de l'autorisation. |

!!! note "Une copie de référence, pas une commande"
    La base SAM de Resthome est une **copie locale** chargée à l'installation.
    Elle vous sert à identifier et documenter un médicament ; elle ne gère ni le
    stock ni les prix. Ceux-ci vivent sur la fiche du catalogue, une fois le
    médicament importé.

## Consulter la base SAM

Depuis **Soins → Configuration → Base de données SAM**, vous parcourez le
référentiel en lecture seule. La liste affiche le code CNK, le nom, le principe
actif, le code ATC, la forme et le fabricant.

Utilisez la barre de recherche et les filtres pour cibler :

- **recherche** par nom (FR/NL), code CNK, code ATC, principe actif ou fabricant ;
- **filtres** « Prescription Required » (prescription requise), « Black Triangle »
  (triangle noir) et « With CNK » (avec code CNK) ;
- **regroupements** par code ATC, par forme ou par fabricant.

La fiche d'un médicament détaille son identification, sa classification, sa forme
pharmaceutique, son principe actif et les liens vers ses documents officiels
(RCP et notice, FR et NL).

<!-- capture à ajouter : fiche d'un médicament dans la Base de données SAM, onglets identification / classification / documents officiels -->

## L'assistant Search SAM

L'assistant **Search SAM** cherche un médicament dans SAM et l'ajoute à votre
catalogue en un geste. Ouvrez-le via **MR/MRS → Configuration → eHealth
Configuration → Search SAM**.

### 1. Lancer une recherche

Choisissez le **type de recherche** :

- **By Name** — par nom commercial ou principe actif (ex. *Dafalgan*, *Rilatine*) ;
- **By CNK Code** — par code CNK.

Saisissez votre terme dans le champ de recherche puis cliquez sur **Search**. La
recherche est **insensible aux accents** et gère plusieurs mots (ex.
*Amlodipine 5mg*).

!!! tip "Recherche locale d'abord"
    L'assistant interroge d'abord la copie locale de SAM : la réponse est
    immédiate, même sans connexion. Si cette copie est vide, Resthome peut
    basculer sur le service **DICS v5** en direct — mais cette voie exige une
    connexion eHealth certifiée.

### 2. Choisir dans les résultats

Les résultats s'affichent en tableau. Chaque ligne montre le code **CNK**, le
**nom**, le **principe actif (INN)**, le **dosage**, la **forme** et — en
colonnes optionnelles — le fabricant, le code ATC, la classe BCFI et les liens
RCP / notice.

La colonne **In Catalog** indique si le médicament figure déjà dans votre
catalogue. Ces lignes apparaissent **en bleu** : inutile de les recréer.

Cochez la case **Select** en début de ligne pour chaque médicament à importer.

<!-- capture à ajouter : résultats de Search SAM avec cases Select cochées et colonne In Catalog -->

### 3. Importer au catalogue

Cliquez sur **Import Selected**. Resthome crée dans votre catalogue une fiche par
médicament coché, en reprenant les données SAM :

| Donnée SAM | Champ du catalogue |
| --- | --- |
| Name | Nom du médicament |
| CNK | Code CNK |
| INN (principe actif) | Principe actif |
| Strength | Dosage |
| Form | Forme (convertie en catégorie Resthome) |
| Manufacturer | Fabricant |
| ATC | Code ATC |
| RCP / notice / lien BCFI | Onglet **Documents officiels** de la fiche |

Une notification confirme le nombre de médicaments **créés** (et **mis à jour**,
le cas échéant).

### 4. Mettre à jour un médicament existant

Pour rafraîchir une fiche déjà présente, relancez la recherche (bouton **Search
Again**) et réimportez la ligne. Resthome **rapproche par code CNK** : si le
médicament existe déjà, il **met à jour** la fiche au lieu d'en créer un doublon.

!!! warning "Un import ne remplace pas la prescription"
    Importer un médicament l'ajoute au **catalogue** de l'établissement. Il reste
    ensuite à le **prescrire** au résident, avec sa posologie et sa période. Voir
    [Prescriptions et médicaments](prescriptions.md).

## Points clés à retenir

- **SAM = référentiel belge officiel** des médicaments, embarqué dans Resthome
  comme socle du catalogue.
- **Deux accès** : la consultation (Soins → Configuration → Base de données SAM)
  et l'assistant d'import **Search SAM** (MR/MRS → Configuration → eHealth
  Configuration).
- La recherche accepte le **nom**, le **code CNK** ou le **principe actif**, et
  fonctionne **hors ligne** sur la copie locale.
- **Import Selected** crée les fiches ; un réimport **met à jour** les médicaments
  déjà présents (rapprochement par CNK).
- SAM fournit **ATC, classe BCFI, Triangle noir, RCP et notice (FR/NL)** — de la
  donnée fiable, à titre de référence.

## Pour aller plus loin

- [Prescriptions et médicaments](prescriptions.md)
- [Plans de soins et signes vitaux](plans-de-soins.md)
- [L'intégration eHealth](../ehealth/index.md)