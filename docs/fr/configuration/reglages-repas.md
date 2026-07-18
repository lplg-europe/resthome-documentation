---
title: Réglages des repas et de la nutrition
description: "Configurer l'onglet Repas de Resthome en maison de repos (MR/MRS) : source nutritionnelle, menu public, kiosque, notifications familles et cibles ESPEN."
faq:
  - q: "Faut-il choisir CIQUAL ou NUBEL comme source nutritionnelle ?"
    a: "CIQUAL (ANSES, France) est la source par défaut : sa base de 3484 aliments est déjà chargée, vous pouvez l'utiliser immédiatement. NUBEL (Belgique) doit d'abord être importée. Pour démarrer, gardez CIQUAL ; passez à NUBEL uniquement si vous avez besoin des références belges et que l'import est fait."
  - q: "À quoi sert le seuil d'alerte de déficit d'apport ?"
    a: "Resthome compare l'apport moyen sur 3 jours aux besoins du résident (énergie et protéines). Quand cet apport couvre moins que le seuil réglé (75 % par défaut), une alerte de déficit est créée. Baissez le seuil pour être alerté plus tard, montez-le pour être alerté plus tôt."
  - q: "Les cibles ESPEN sont-elles les mêmes pour tous les résidents ?"
    a: "Non. Les coefficients (30 kcal/kg, 1 g/kg de protéines, 1,6 l pour les femmes et 2,0 l pour les hommes) sont des réglages d'établissement. Resthome calcule ensuite la cible propre à chaque résident à partir de son poids et de son sexe. La bande énergétique passe à 35 kcal/kg pour un résident en insuffisance pondérale (IMC inférieur ou égal à 21)."
  - q: "Pourquoi les notifications repas aux familles restent-elles sans effet ?"
    a: "L'envoi d'e-mails suppose un serveur de mail sortant configuré dans Odoo. Sans lui, activer l'option ne produit aucun envoi. Configurez d'abord le serveur sortant, puis activez la notification globale et l'opt-in par résident."
  - q: "Où se trouvent ces réglages ?"
    a: "Dans Réglages > Repas. L'onglet regroupe quatre blocs : Nutrition, Menu public et kiosque, Notifications aux familles, et Cibles nutritionnelles (ESPEN)."
---

# Réglages des repas et de la nutrition

L'onglet **Repas** des réglages regroupe le paramétrage de l'application Repas :
la **source des données nutritionnelles**, l'**apparence du menu public et du
kiosque**, les **notifications aux familles** et les **cibles nutritionnelles
(ESPEN)** qui servent au suivi de la dénutrition. Vous le trouvez dans
**Réglages > Repas**.

Ces réglages valent pour toute la maison : vous les définissez une fois, puis ils
n'évoluent qu'à la marge.

## Nutrition

Cette section indique quelle **base de référence** Resthome interroge pour retrouver
les valeurs nutritionnelles des ingrédients (calories, protéines…).

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Source de données nutritionnelles** | Base de référence des valeurs nutritionnelles. CIQUAL (ANSES, France) : 3484 aliments, déjà chargés. NUBEL (Belgique) : base belge, à importer. | **CIQUAL** (par défaut, déjà chargée) |

!!! tip "CIQUAL suffit pour démarrer"
    La base **CIQUAL** est pré-chargée : vous pouvez composer vos menus et suivre la
    nutrition sans aucune préparation. Ne passez à **NUBEL** que si vous avez
    spécifiquement besoin des références belges — l'import doit alors être réalisé au
    préalable.

## Menu public et kiosque

Ces réglages personnalisent l'apparence des pages **menu du jour**, **menu de la
semaine** et **kiosque** (voir [Portail familles et kiosque](../repas/portail-familles.md)).

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Couleur du menu public** | Couleur principale des pages menu et kiosque. | Votre couleur de charte (défaut `#0d6efd`) |
| **Afficher le logo de la société** | Affiche le logo de la société en tête des pages du menu public. | Activé |
| **Rafraîchissement du kiosque (secondes)** | Intervalle de rafraîchissement automatique de la page kiosque (`/menu/kiosk`) affichée en salle à manger. | 600 s (10 min) |

!!! note "Valeurs propres à votre établissement"
    La **couleur** et le **logo** sont propres à votre maison : mettez votre charte
    graphique. Le rafraîchissement du kiosque n'a d'intérêt que si un écran affiche la
    page `/menu/kiosk` en continu.

## Notifications aux familles

Ce bloc active l'envoi automatique d'e-mails aux familles qui l'ont accepté : un
**résumé hebdomadaire** des repas et une **alerte de faible prise**.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Notifications repas aux familles** | Envoie aux familles ayant opté un résumé hebdomadaire et une alerte de faible prise. Nécessite un serveur de mail sortant. | Activé **si** un serveur de mail sortant est configuré, sinon désactivé |

!!! warning "Un serveur de mail sortant est requis"
    Sans **serveur de mail sortant** configuré dans Odoo, activer l'option n'envoie
    rien. L'envoi dépend aussi d'un **opt-in par résident** : seules les familles ayant
    accepté reçoivent les e-mails. Configurez le serveur sortant, activez la
    notification globale, puis l'opt-in résident par résident.

## Cibles nutritionnelles (ESPEN)

Ces coefficients, issus des recommandations gériatriques **ESPEN**, servent à calculer
la **cible propre à chaque résident** (à partir de son poids et de son sexe) et à
déclencher les **alertes de déficit**.

| Réglage | À quoi ça sert | Valeur conseillée (MR/MRS) |
|---|---|---|
| **Énergie (kcal/kg/jour)** | Cible énergétique par kilo de poids. | 30 |
| **Énergie si insuffisance pondérale (kcal/kg/jour)** | Cible relevée pour un résident dénutri (IMC inférieur ou égal à 21) ; ESPEN suggère 32 à 38. | 35 |
| **Protéines (g/kg/jour)** | Cible protéique par kilo de poids (au moins 1 ; 1,2 à 1,5 en cas de maladie). | 1 |
| **Liquides — femmes (ml/jour)** | Cible d'hydratation quotidienne pour les femmes. | 1600 |
| **Liquides — hommes (ml/jour)** | Cible d'hydratation quotidienne pour les hommes. | 2000 |
| **Alerte de déficit d'apport (% de couverture)** | Seuil sous lequel une alerte est créée quand l'apport moyen sur 3 jours ne couvre pas assez de la cible énergie ou protéines. | 75 |

!!! info "Une cible calculée par résident"
    Vous réglez ici les **coefficients** ; Resthome en déduit la **cible individuelle**
    de chaque résident selon son poids et son sexe, puis compare l'**apport** réel à ces
    cibles. Le suivi de la couverture et le dépistage de la dénutrition sont décrits dans
    [Menus, régimes et hydratation](../repas/menus-regimes.md).

## Pour aller plus loin

- [Menus, régimes et hydratation](../repas/menus-regimes.md)
- [Portail familles et kiosque](../repas/portail-familles.md)
- [Vue d'ensemble des Repas](../repas/index.md)
- [Registres cliniques](../soins/registres.md)