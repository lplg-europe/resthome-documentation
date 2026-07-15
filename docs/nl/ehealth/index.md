---
title: eHealth
description: Verzekerbaarheid MDA, elektronische facturatie eFact en akkoorden eAgreement in Resthome.
---

# eHealth

Resthome is verbonden met het Belgische e-gezondheidsecosysteem (eHealth,
MyCareNet, WalCareNet) om rechtstreeks met de mutualiteiten uit te wisselen.

## De diensten

<div class="grid cards" markdown>

-   :material-shield-check:{ .lg .middle } **MDA — Verzekerbaarheid**

    ---

    Controleert of een bewoner **verzekerd** is en haalt zijn mutualiteit en
    BIM-status op, individueel of in batch.

    [:octicons-arrow-right-24: De verzekerbaarheid in detail](mda.md)

-   :material-send:{ .lg .middle } **eFact — Elektronische facturatie**

    ---

    Verstuurt het **mutualiteitsaandeel** (bericht 920000) naar de
    verzekeringsinstellingen en volgt de ontvangstbewijzen en afrekeningen op.

    [:octicons-arrow-right-24: De eFact-facturatie in detail](efact.md)

-   :material-file-sign:{ .lg .middle } **eAgreement — Akkoorden**

    ---

    Meldt de VI bij een **opname**, een **einde verblijf** of een
    **afwezigheid** (Bijlagen 7, 10, 11…).

    [:octicons-arrow-right-24: De akkoorden in detail](eagreement.md)

</div>

## Vereisten

!!! warning "Te controleren vóór het versturen"
    - De bewoner heeft een geldig **NISS**.
    - Zijn **mutualiteit** is ingevuld.
    - Er is een **verzekerbaarheid (MDA)** gecontroleerd voor de periode.
    - Het **eHealth-certificaat** van de instelling is actief.

## Goed om te weten

- Een **afwezigheid** van meer dan 72 u (of elke hospitalisatie) lokt een
  **Bijlage 11** einde verblijf uit; de **terugkeer** genereert een **Bijlage 7**
  heropname.
- Een reeds **geboekte** factuur « bevriest » de facturatie van de maand voor die
  bewoner: om ze te wijzigen, zet ze terug naar concept (of maak een creditnota
  op) en vernieuw dan.

## Verder

- [Akkoorden (eAgreement)](eagreement.md) — opname, afwezigheid, terugkeer,
  vertrek (Bijlagen 7, 10, 11).
- [Het facturatietraject](../parcours-facturation.md) — van opname tot betaling.
- [Afwezigheden en hospitalisaties](../facturation/absences.md)
- [Facturatie](../facturation/index.md)
- [FAQ](../faq.md) · [Woordenlijst](../glossaire.md)
