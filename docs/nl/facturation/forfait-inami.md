---
title: Het RIZIV-forfait (afhankelijkheid)
description: "Het afhankelijkheidsforfait van het RIZIV in het woonzorgcentrum, uitgelegd: van de Katz-evaluatie tot de categorie, tot het aan het ziekenfonds gefactureerde bedrag, en de rol van het VI-akkoord."
faq:
  - q: "Wat is het RIZIV-forfait (afhankelijkheid)?"
    a: "Het is het dagelijkse bedrag dat het ziekenfonds ten laste neemt voor de zorg verbonden aan de afhankelijkheid van een bewoner. In de AViQ-tarieven is het één uniek bedrag, hetzelfde voor alle Katz-categorieën (inclusief O), berekend op de aanwezigheidsdagen en via de eFact aan de verzekeringsinstelling gefactureerd, niet aan de bewoner. De categorie dient om het juiste profiel te melden en het akkoord van het ziekenfonds te verkrijgen."
  - q: "Hangt het bedrag van het forfait af van de Katz-categorie?"
    a: "Nee. In de AViQ-tarieven is het afhankelijkheidsforfait hetzelfde dagbedrag voor alle categorieën, inclusief categorie O (zelfstandig). De categorie wijzigt het bedrag niet: ze dient om het juiste afhankelijkheidsprofiel aan het ziekenfonds te melden en het akkoord (eAgreement) te verkrijgen. Het tarief blijft per categorie configureerbaar in Configuratie → RIZIV-tarieven indien een overeenkomst dat vereist."
  - q: "Hoe wordt het afhankelijkheidsforfait berekend?"
    a: "Forfait = dagtarief van het forfait (identiek voor alle categorieën) × aantal factureerbare aanwezigheidsdagen in de periode van RIZIV-tussenkomst. Afwezigheden verminderen de dagen (middagregel). Het toegepaste tarief is dat wat geldt op de factuurdatum."
  - q: "Waarom verschilt de gefactureerde categorie soms van de klinische categorie?"
    a: "Het ziekenfonds betaalt de categorie terug die het in het akkoord (eAgreement) heeft goedgekeurd, niet noodzakelijk uw laatste evaluatie. Zolang een wijziging niet door de verzekeringsinstelling is aanvaard, blijft Resthome de vorige categorie factureren om een weigering te vermijden."
  - q: "Wie betaalt het afhankelijkheidsforfait?"
    a: "Het forfait wordt voor 100 % ten laste genomen door het ziekenfonds (derdebetaler, via de eFact). De huisvesting (de kamer) is een aparte lijn, ten laste van de bewoner."
---

# Het RIZIV-forfait (afhankelijkheid)

Het **afhankelijkheidsforfait** is het **dagelijkse** bedrag dat het ziekenfonds ten
laste neemt voor de **zorg** van een bewoner. Het hangt af van zijn **graad van
afhankelijkheid**, gemeten door de **[Katz-evaluatie](../residents/katz.md)**, en het
wordt via de **[elektronische facturatie (eFact)](../ehealth/efact.md)** naar de
verzekeringsinstelling (VI) verstuurd.

Deze pagina legt de volledige keten uit: **Katz-evaluatie → categorie → gefactureerd
bedrag**.

## Van de Katz-evaluatie naar de categorie

De [Katz-evaluatie](../residents/katz.md) scoort **6 criteria** (zich wassen, zich
kleden, transfer en verplaatsing, naar het toilet gaan, continentie, eten) van **1**
(zelfstandig) tot **4** (volledig afhankelijk). Op basis daarvan berekent Resthome een
**afhankelijkheidscategorie**, die aan het ziekenfonds wordt **gemeld**:

| Categorie | Afhankelijkheid | RIZIV-forfait |
|---|---|---|
| **O** | Zelfstandig | Ja (pseudo-code 770501) |
| **A** | Licht | Ja |
| **B** | Matig | Ja |
| **C** | Sterk | Ja |
| **Cd** | Sterk, met desoriëntatie / dementie | Ja |
| **D** | Dementie (gespecialiseerde diagnose) | Ja |

!!! important "Het bedrag is voor alle categorieën gelijk"
    In de **AViQ**-tarieven is het **bedrag** van het afhankelijkheidsforfait **gelijk
    voor alle Katz-categorieën**, inclusief **O**: één **uniek dagtarief**, jaarlijks
    geïndexeerd (bv. **85,72 €/dag in 2026**). De categorie wijzigt dus **het bedrag
    niet** — ze dient om het **juiste profiel** aan het ziekenfonds te **melden** (het
    **VI-akkoord**) en voor de **zorgnormen**. Het tarief blijft **per categorie
    configureerbaar** in *Configuratie → RIZIV-tarieven* indien een overeenkomst dat vereist.

!!! note "Categorie O standaard"
    Zolang er geen **gevalideerde** Katz-evaluatie is, staat de bewoner standaard in
    categorie **O** en verschijnt er een herinnering **« Katz te doen »**. Valideer de
    Katz-evaluatie om de **juiste categorie** aan het ziekenfonds te **melden** en het
    overeenkomstige **akkoord** te verkrijgen.

!!! info "Comateuze patiënt"
    Het forfait voor **comateuze** patiënten is een bijzonder **federaal** forfait: het
    vereist een specifieke **accreditatie** van de instelling. Zonder deze wordt de
    overeenkomstige forfaitlijn niet aangemaakt (de huisvesting blijft gefactureerd).

## Hoe het bedrag wordt berekend

Het gefactureerde forfait voor een bewoner volgt een eenvoudige regel:

> **Forfait = dagtarief van het forfait (voor alle categorieën gelijk) × aantal factureerbare aanwezigheidsdagen**

- De **aanwezigheidsdagen** worden geteld over de **periode van RIZIV-tussenkomst** (van
  de opname tot het einde van de tussenkomst), **min de afwezigheden**. Die periode kan
  **korter** zijn dan de huisvesting (opname in de loop van de maand, vertrek,
  overlijden, einde tussenkomst vóór de kamer is vrijgekomen).
- Een **afwezigheid** (ziekenhuisopname, vakantie) **vermindert** het aantal dagen,
  volgens de **[middagregel](absences.md)** (uur van Brussel).
- Het toegepaste **tarief** is dat wat **geldt op de datum** van facturatie; het wordt in
  de tijd geïndexeerd (zie verder).

!!! tip "Forfait = ziekenfonds · huisvesting = bewoner"
    Het **afhankelijkheidsforfait** wordt voor **100 % door het ziekenfonds** ten laste
    genomen (derdebetaler, via de eFact). De **huisvesting** (de kamer) is een **aparte
    lijn**, ten laste van de **bewoner**. Beide lopen parallel op dezelfde
    facturatieperiode.

## Klinische categorie en gefactureerde categorie

Twee begrippen bestaan naast elkaar, en het is belangrijk ze niet te verwarren:

- De **klinische categorie** — uw **laatste gevalideerde Katz-evaluatie**; ze weerspiegelt
  de reële afhankelijkheid en dient voor de zorg.
- De **gefactureerde categorie** — die op de factuur naar het ziekenfonds.

**Ze kunnen verschillen.** Het ziekenfonds betaalt **de categorie die het heeft
goedgekeurd** in het **[akkoord (eAgreement)](../ehealth/eagreement.md)** terug, niet
noodzakelijk uw laatste evaluatie. Concreet:

- Is er een **VI-akkoord** van kracht → dan factureert men **de categorie van dat
  akkoord**.
- Is een **categoriewijziging** aangevraagd maar het akkoord nog **in afwachting** van
  het ziekenfonds → dan **behoudt** Resthome de **vorige categorie** in de facturatie.
- Zo niet → dan factureert men de klinische categorie.

!!! warning "Waarom die voorzichtigheid?"
    Een categorie factureren die **afwijkt van het akkoord** lokt een **weigering** van
    de VI uit (« forfait onverenigbaar met het akkoord »). Zolang de nieuwe categorie
    niet **door het ziekenfonds is aanvaard**, blijft Resthome dus de oude factureren.
    De klinisch getoonde categorie kan zo **hoger** zijn dan de gefactureerde.

## Verergering van de afhankelijkheid

Verslechtert de toestand van een bewoner, voer dan een **nieuwe Katz-evaluatie** in met
een **reden van verergering**. Resthome bereidt de bijwerking van het zorgakkoord voor
(**Bijlage 10**), met de reden automatisch overgenomen en de **handtekening** van de
clinicus. De **nieuwe categorie** wordt pas **gefactureerd** zodra het **akkoord van het
ziekenfonds is verkregen** (zie hierboven).

## De forfaittarieven configureren

De tarieven worden geconfigureerd in de app **MR/MRS → Configuratie → RIZIV-tarieven**:
één **tarief per Katz-categorie**, met een **geldigheidsperiode**. Resthome past
automatisch het tarief toe dat geldt op de factuurdatum. Voor de **jaarlijkse indexering**
voegt men een nieuwe tarieflijn toe (nieuwe begindatum) en sluit men de oude af. Datzelfde
scherm beheert ook het **huisvestingstarief** (ten laste van de bewoner).

## Kernpunten

- Het **dagforfait** is **hetzelfde bedrag voor alle categorieën** (inclusief **O**); de
  categorie dient om het **juiste profiel** aan het ziekenfonds te melden (VI-akkoord).
- Het gefactureerde forfait = **dagtarief × aanwezigheidsdagen** (periode
  van RIZIV-tussenkomst, min de afwezigheden).
- Men factureert de **met het ziekenfonds overeengekomen categorie** (akkoord), niet
  noodzakelijk de laatste klinische evaluatie.
- **Forfait = ziekenfonds**, **huisvesting = bewoner**, op dezelfde periode.

## Verder

- [De Katz-evaluatie](../residents/katz.md)
- [Elektronische facturatie (eFact)](../ehealth/efact.md) · [eFact-weigeringen](../ehealth/efact-rejets.md)
- [Akkoorden (eAgreement)](../ehealth/eagreement.md)
- [Afwezigheden en hospitalisaties](absences.md)
- [FAQ](../faq.md) · [Woordenlijst](../glossaire.md)
