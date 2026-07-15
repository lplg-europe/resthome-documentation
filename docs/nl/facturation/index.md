---
title: Facturatie
description: Facturatieperiodes, RIZIV-forfaits, supplementen, afwezigheden en facturen in Resthome.
---

# Facturatie

Resthome automatiseert de MR/MRS-facturatie: het **mutualiteitsaandeel**
(RIZIV-forfait) en het **bewonersaandeel** (verblijf + supplementen), periode per
periode.

## De grote principes

- **Facturatieperiode**: één maand. Ze wordt **gegenereerd** en dan
  **gefactureerd**.
- **RIZIV-forfait**: berekend volgens de **Katz-categorie** en de
  aanwezigheidsdagen; het door de mutualiteit terugbetaalde deel.
- **Verblijf**: het door de bewoner betaalde deel (de kamer), volgens tarief.
- **Supplementen**: eenmalige of terugkerende prestaties (eenpersoonskamer, tv,
  kapper…), via de **supplementenenveloppe** van de bewoner.
- **Afwezigheden**: een afwezigheid (hospitalisatie, vakantie) **vermindert het
  forfait** voor de betrokken periode en kan een eHealth-melding uitlokken.

!!! note "Anticipatieve facturatie"
    Voor vooraf gefactureerde bewoners wordt het verblijf van een maand de
    **voorgaande maand** gefactureerd. Het forfait en de supplementen worden
    daarentegen op de prestatiemaand gefactureerd.

## De knop « Vernieuwen »

Op een facturatieperiode herberekent de actie **Vernieuwen** alles met één klik:
factuurregels, supplementen en conceptfacturen.

!!! tip "Goed om te weten"
    - Bewoners van wie de factuur **al geboekt** is, blijven ongewijzigd; al de
      rest wordt herberekend.
    - Een supplement of afwezigheid toevoegen **synchroniseert automatisch**: u
      hoeft doorgaans niet op « Vernieuwen » te klikken.

## Cyclus van een periode

1. **Nieuwe periode** (de maand).
2. De factuurregels **genereren**.
3. De **verzekerbaarheid (MDA)** van de bewoners controleren.
4. De facturen **aanmaken** (bewonersaandeel).
5. De facturen **boeken**.
6. De **eFact genereren** (mutualiteitsaandeel) en versturen.

!!! tip "Stap voor stap"
    Volg de gedetailleerde gids [Een maand factureren, stap voor stap](facturer-un-mois.md),
    of bekijk het volledige [facturatietraject](../parcours-facturation.md).

## Verder

- [Een maand factureren, stap voor stap](facturer-un-mois.md) — de volledige gids van de maand.
- [De supplementen](supplements.md) — supplementenenveloppe, eenmalig of terugkerend.
- [Afwezigheden en hospitalisaties](absences.md) — effect op het forfait,
  72-uurregel, automatische eHealth-melding.
- [Vertrek en overlijden](depart-deces.md) — stop van de facturatie, creditnota
  van het vooraf gefactureerde verblijf.
- [Onderhoudsplichtigen](split-billing.md) — het bewonersaandeel over debiteuren verdelen.
- [Akkoorden (eAgreement)](../ehealth/eagreement.md) — de mutualiteit verwittigen
  (opname, afwezigheid, terugkeer, vertrek).
- [eHealth](../ehealth/index.md) — versturen van het mutualiteitsaandeel (eFact)
  en akkoorden.
- [Een bewoner beheren](../residents/gerer-un-resident.md)
- [Het facturatietraject](../parcours-facturation.md) · [FAQ](../faq.md) · [Woordenlijst](../glossaire.md)
