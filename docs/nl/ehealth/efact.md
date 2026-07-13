---
title: Elektronische facturatie (eFact)
description: Het mutualiteitsaandeel versturen via eFact in Resthome — loten genereren, doorsturen naar de verzekeringsinstellingen, ontvangstbewijzen en weigeringen opvolgen, creditnota's.
---

# Elektronische facturatie (eFact)

De **eFact** is de elektronische verzending van het **mutualiteitsaandeel** (het
RIZIV-forfait) naar de **verzekeringsinstellingen**. Resthome genereert de
bestanden, stuurt ze door en **volgt de antwoorden** voor u op.

## Het principe

Zodra de facturen van de maand **geboekt** zijn, stelt Resthome de **eFact-loten**
samen en stuurt ze via het eHealth-netwerk naar de mutualiteiten. Elke verzending
krijgt een **ontvangstbewijs**, daarna een **afrekening** (aanvaard / geweigerd)
die Resthome automatisch afpunt.

!!! note "Eén verzending per unie van mutualiteiten"
    De verzendingen worden gegroepeerd **per unie** (de grote families van
    mutualiteiten), niet per kleine individuele mutualiteit. Resthome zorgt voor de
    groepering.

## Genereren en versturen

1. Controleer op de **facturatieperiode** dat de facturen **geboekt** zijn.
2. **Genereer de eFact** (samenstelling van de loten).
3. **Verstuur** — de verzending vertrekt naar de verzekeringsinstellingen.

## De antwoorden opvolgen

Elk lot doorloopt zichtbare statussen:

1. **Verstuurd** — doorgestuurd, in afwachting van ontvangstbewijs.
2. **Ontvangstbewijs ontvangen** — de mutualiteit heeft goed ontvangen.
3. **Aanvaard** / **Geweigerd** — de afrekening is terug.

Bij een **weigering** toont Resthome de reden zodat u kunt corrigeren
(verzekerbaarheid, data, bedragen…) en **opnieuw versturen**. De opvolging van de
herzendingen vermijdt dubbels.

!!! tip "eFact-cockpit"
    Een opvolgtabel geeft u de status van alle loten (verstuurd, aanvaard,
    geweigerd, te herzenden) om de mutualiteitsfacturatie in één oogopslag te
    sturen.

## Creditnota's

Moet u een reeds verstuurde mutualiteitsfactuur **terugbetalen** of corrigeren, dan
maakt Resthome de overeenkomstige elektronische **creditnota** aan en neemt ze op
in de verzendingen, in overeenstemming met het gefactureerde forfait.

## Vereisten

!!! warning "Te controleren vóór de verzending"
    - **Verzekerbaarheid (MDA)** gecontroleerd voor de periode.
    - Correcte **mutualiteit** op elke bewoner.
    - Facturen **geboekt**.
    - **eHealth-certificaat** actief.

## Verder

- [Verzekerbaarheid (MDA)](mda.md)
- [Akkoorden (eAgreement)](eagreement.md)
- [Facturatie-overzicht](../facturation/index.md)
