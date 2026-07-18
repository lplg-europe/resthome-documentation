---
title: De kostennota (Bijlage 12)
description: "Bijlage 12-kostennota's opmaken in een woonzorgcentrum (WZC/RVT) met Resthome: individuele nota per bewoner en verzamelnota per verzekeringsinstelling."
faq:
  - q: "Waarvoor dient Bijlage 12 in een woonzorgcentrum (WZC/RVT)?"
    a: "Het is het officiële AViQ-document dat de kosten van een maand verantwoordt: een individuele kostennota per bewoner en een verzamelnota per verzekeringsinstelling."
  - q: "Waar genereer ik Bijlage 12 in Resthome?"
    a: "Via de knop Afdrukken: op een facturatieperiode voor de verzamelnota, op een facturatiefiche per bewoner voor de individuele nota."
  - q: "Wat is het verschil tussen de individuele nota en de verzamelnota?"
    a: "De individuele nota detailleert de kosten van één bewoner over drie pagina's; de verzamelnota lijst alle bewoners van eenzelfde verzekeringsinstelling op met de totalen."
  - q: "Welke bedragen staan op Bijlage 12?"
    a: "De drie verplichte bedragen: ten laste van de verzekeringsinstelling (V.I.), ten laste van de patiënt en het totaal, met het aantal aanwezigheidsdagen van de maand."
  - q: "Moet ik Bijlage 12 aan de bewoner overhandigen?"
    a: "Ja: een dubbel van de individuele kostennota moet aan de begunstigde worden bezorgd; de verzamelnota begeleidt de facturatie naar de verzekeringsinstelling."
---

# De kostennota (Bijlage 12)

**Bijlage 12** is het officiële document dat maand per maand de verblijf- en
zorgkosten van een bewoner van een woonzorgcentrum (WZC/RVT) verantwoordt.
Resthome maakt ze op in twee complementaire vormen:

- de **Individuele Kostennota** — een gedetailleerd bewijsstuk **per bewoner** ;
- de **Verzamelnota** (« Note Récapitulative ») — een tabel **per
  verzekeringsinstelling (V.I.)** die alle bewoners van eenzelfde mutualiteit
  samenbrengt.

Beide worden gegenereerd via de knop **Afdrukken** (Print), vanuit een
**facturatieperiode** of een **facturatiefiche per bewoner**.

!!! info "Een officieel AViQ-document"
    Bijlage 12 betreft de « instellingen bedoeld in artikel 43/7, 4° van het Waalse
    Wetboek van sociale actie en gezondheid ». Resthome vult het officiële formulier
    automatisch in met de gegevens van uw periode: u hoeft niets manueel over te
    typen.

!!! note "Waalse regelgeving"
    Bijlage 12 en het AViQ-forfait zijn eigen aan het Waalse Gewest. De knoplabels
    behouden hun officiële Franse benaming (« Annexe 12 — Note de Frais
    Individuelle » en « Annexe 12 — Note Récapitulative »).

## Twee documenten, twee reikwijdtes

| Document | Reikwijdte | Afgedrukt bestand | Gegenereerd vanuit |
|---|---|---|---|
| **Individuele Kostennota** | Eén bewoner | `Annexe12_<bewoner>_<periode>` | Fiche **Facturatie per bewoner** → **Afdrukken** |
| **Verzamelnota** | Eén verzekeringsinstelling | `NoteRecap_<periode>` | **Facturatieperiode** → **Afdrukken** |

!!! tip "De link tussen beide"
    Elke regel van de verzamelnota draagt een **nummer van individuele nota** dat
    verwijst naar de individuele nota van de betrokken bewoner. U maakt dus meestal
    **beide documenten voor dezelfde maand** op: de verzamelnota voor de V.I., de
    individuele nota's voor de bewoners.

## De Individuele Kostennota (per bewoner)

Dit is het volledige bewijsstuk van **één bewoner** voor de maand. Resthome maakt
het op het **officiële formulier** in drie pagina's.

| Pagina | Inhoud |
|---|---|
| **1. Overzicht van de bewoner** | Identificatie van de instelling (naam, adres, RIZIV-nummer) en van de mutualiteit, periode, regel van de bewoner (naam, inschrijvingsnummer INSZ, aanwezigheidsdagen) en de **drie verplichte bedragen**: ten laste V.I., ten laste patiënt, totaal. |
| **2. Vaste kosten** | Het **zorgforfait** (aandeel verzekeringsinstelling), met zijn **AViQ-pseudocode**, de dagprijs, het aantal dagen en het bedrag — opgesplitst per deelperiode indien nodig — evenals de **incontinentiekorting**. |
| **3. Supplementen** | Het **verblijf** (de kamer), de **supplementen** (televisie, telefoon, wasserij, pedicure, eenpersoonskamer…), de (para)farmaceutische **geneesmiddelen** en het **totaal van de supplementen**. |

!!! note "De drie verplichte bedragen"
    De eerste pagina draagt de **drie bedragen** die de elektronische facturatie
    vereist: **ten laste van de V.I.** (het terugbetaalde forfait, incontinentie­korting
    inbegrepen), **ten laste van de patiënt** (verblijf + supplementen) en het
    **totaal**. Deze bedragen verantwoorden tegenover de bewoner wat de mutualiteit
    ten laste neemt en wat hem te betalen overblijft.

!!! info "Het forfait hangt niet af van de Katz-categorie"
    Het bedrag van het **zorgforfait** is **hetzelfde voor alle Katz-categorieën**
    (AViQ-tarieven): de categorie dient om het **afhankelijkheidsprofiel aan te
    geven** bij de mutualiteit, niet om een ander bedrag vast te leggen. Zie
    [Het RIZIV-forfait](forfait-inami.md).

### Een individuele nota opmaken

1. Open de **facturatieperiode** van de maand (toepassing **MR/MRS → Facturatie →
   Facturatieperiodes**).
2. Open de **facturatiefiche van de betrokken bewoner** (« Facturatie per
   bewoner »).
3. Klik **Afdrukken → Annexe 12 — Note de Frais Individuelle**.
4. De PDF wordt gegenereerd op naam van de bewoner en de periode.

<!-- capture a ajouter : de geopende knop Afdrukken op een facturatiefiche per bewoner, met de invoer « Annexe 12 — Note de Frais Individuelle » -->

!!! warning "Bezorg een dubbel aan de bewoner"
    De verzamelnota certificeert dat « een dubbel van de individuele kostennota aan
    de begunstigde werd bezorgd ». Denk er dus aan de **individuele nota** (of het
    dubbel ervan) aan elke bewoner of zijn vertegenwoordiger te **overhandigen**.

## De Verzamelnota (per verzekeringsinstelling)

De verzamelnota bundelt voor een maand **alle bewoners van eenzelfde
verzekeringsinstelling** in één tabel. Resthome maakt **één pagina per V.I.** op:
als uw periode bewoners van meerdere mutualiteiten telt, bevat het document
evenveel pagina's als er instellingen zijn.

Hoofding van elke pagina:

- de **identificatie van de instelling**: naam, adres, telefoon, **RIZIV-nummer** ;
- de **identificatie van de mutualiteit**: nummer (V.I.-code) en naam ;
- de gedekte **periode** (« Note récapitulative du … au … — établie le … »).

De bewonerstabel bevat de volgende kolommen:

| Kolom | Inhoud |
|---|---|
| **N° note individuelle** | Referentie van de individuele nota van de bewoner |
| **Nom et prénom du bénéficiaire** | De bewoner |
| **N° d'inscription** | Het INSZ van de bewoner |
| **Nombre de jours** | Gefactureerde aanwezigheidsdagen |
| **À charge O.A.** | Aandeel terugbetaald door de verzekeringsinstelling |
| **À charge patient** | Aandeel te betalen door de bewoner |
| **Total** | Som van beide |

De laatste regel telt het **Algemeen totaal voor de V.I.**, ten laste patiënt en
totaal op. Het document eindigt met een **certificering** ondertekend door de
**Verantwoordelijke van de Instelling** (datum, naam en handtekening).

### Een verzamelnota opmaken

1. Open de **facturatieperiode** van de maand (of selecteer ze in de lijst
   **Facturatieperiodes**).
2. Klik **Afdrukken → Annexe 12 — Note Récapitulative**.
3. Resthome genereert de PDF, **één pagina per verzekeringsinstelling**.

<!-- capture a ajouter : de gegenereerde verzamelnota, met de hoofding instelling/mutualiteit en de tabel van de per V.I. gegroepeerde bewoners -->

## Wanneer Bijlage 12 opmaken

Maak Bijlage 12 op **zodra de maand gefactureerd is**: de bedragen nemen de door
Resthome berekende factuurregels over (forfait, verblijf, supplementen,
geneesmiddelen, afwezigheden). Wijzigt u een factuur achteraf, **vernieuw** dan de
periode en genereer het document opnieuw zodat het de nieuwe bedragen weergeeft.

!!! tip "Ze begeleidt de eFact"
    De verzamelnota is het « papieren » bewijsstuk dat de **naar elke
    verzekeringsinstelling verzonden facturatie begeleidt**. Voor de volledige
    elektronische stroom (verzending van het forfait naar de mutualiteit), zie
    [Een maand factureren, stap voor stap](facturer-un-mois.md).

!!! note "Vertrek of overlijden tijdens de maand"
    De bedragen houden rekening met de **werkelijke aanwezigheidsdagen**: een
    vertrek of overlijden tijdens de maand is al verwerkt in de factuurregels, en
    dus in Bijlage 12. Zie [Vertrek en overlijden](depart-deces.md).

## Kernpunten om te onthouden

- Bijlage 12 bestaat in **twee vormen**: de **individuele nota** (per bewoner) en
  de **verzamelnota** (per verzekeringsinstelling).
- Beide worden gegenereerd via de knop **Afdrukken**: de verzamelnota op de
  **periode**, de individuele nota op de **facturatiefiche per bewoner**.
- De individuele nota draagt de **drie verplichte bedragen**: ten laste V.I., ten
  laste patiënt en totaal.
- De verzamelnota maakt **één pagina per verzekeringsinstelling** op en telt het
  **Algemeen totaal voor de V.I.** op.
- Een **dubbel van de individuele nota** moet aan de bewoner worden **bezorgd**.
- Het RIZIV-nummer van de instelling en de tarieven zijn **eigen aan uw
  instelling**: controleer of ze correct geconfigureerd zijn.

## Verder

- [Een maand factureren, stap voor stap](facturer-un-mois.md)
- [De supplementen](supplements.md)
- [Overzicht van de facturatie](index.md)
- [Vertrek en overlijden](depart-deces.md)