---
title: De SAM-geneesmiddelendatabank
description: "De authentieke Belgische SAM-databank in Resthome: ATC-referentie, BCFI-klasse, zwarte driehoek, SKP/bijsluiter en de Search SAM-assistent voor het woonzorgcentrum (WZC/RVT)."
howto_auto: true
faq:
  - q: "Wat is de SAM-databank?"
    a: "SAM (Authentieke Bron van de Geneesmiddelen) is het officiële Belgische referentiebestand van geneesmiddelen. Resthome bevat er een kopie van om de catalogus van uw woonzorgcentrum (WZC/RVT) te voeden met betrouwbare gegevens: CNK-code, werkzaam bestanddeel, ATC-code, BCFI-klasse, bijsluiters."
  - q: "Waar vind ik de SAM-databank in Resthome?"
    a: "Twee ingangen. De raadpleging, via de toepassing Zorg → Configuratie → SAM-databank. En de importassistent « Search SAM », via de toepassing WZC/RVT → Configuratie → eHealth Configuration → Search SAM."
  - q: "Hoe voeg ik een SAM-geneesmiddel toe aan mijn catalogus?"
    a: "Open de assistent Search SAM, zoek op naam of op CNK-code, vink de gewenste regels aan en klik op Import Selected. De geneesmiddelen worden met hun SAM-gegevens in uw catalogus aangemaakt."
  - q: "Wat betekent « zwarte driehoek »?"
    a: "De zwarte driehoek duidt op een geneesmiddel onder verscherpt toezicht (bijkomende geneesmiddelenbewaking). De informatie wordt ter indicatie overgenomen uit SAM, op de referentiefiche."
  - q: "Werkt het zoeken zonder eHealth-verbinding?"
    a: "Ja. Het zoeken steunt eerst op de lokale kopie van SAM, offline beschikbaar en meteen. De live DICS v5-dienst wordt enkel als reserve gebruikt en vereist een gecertificeerde eHealth-verbinding."
  - q: "Hoe werk ik een reeds aanwezig geneesmiddel bij?"
    a: "Herhaal de zoekopdracht en importeer de regel opnieuw. Als de CNK-code al in de catalogus bestaat, werkt Resthome de bestaande fiche bij in plaats van een tweede aan te maken."
---

# De SAM-geneesmiddelendatabank

**SAM** (Authentieke Bron van de Geneesmiddelen) is het officiële Belgische
referentiebestand van geneesmiddelen. Resthome gebruikt het als basis voor zijn
**geneesmiddelencatalogus**: in plaats van een geneesmiddel manueel in te voeren,
zoekt u het op in SAM en importeert u het, met zijn betrouwbare gegevens
(CNK-code, werkzaam bestanddeel, classificatie, bijsluiters).

Twee ingangen:

- **Raadplegen** van het referentiebestand — toepassing **Zorg** →
  **Configuratie** → **SAM-databank** (alleen-lezen).
- **Zoeken en importeren** — de assistent **Search SAM**, in de toepassing
  **WZC/RVT** → **Configuratie** → **eHealth Configuration** → **Search SAM**.

!!! info "Een functie van de eHealth-integratie"
    De assistent **Search SAM** maakt deel uit van de Belgische eHealth-laag van
    Resthome. Hij installeert automatisch zodra de medische module en de
    eHealth-module aanwezig zijn, en de toegang is voorbehouden aan de
    **eHealth-beheerder**. Het raadplegen van het bestand (Zorg → Configuratie)
    blijft toegankelijk zonder die rol.

## Wat de SAM-databank brengt

Elk geneesmiddel in het referentiebestand draagt authentieke gegevens, nuttig
voor de zorg én voor de traceerbaarheid:

| Gegeven | Waarvoor het dient |
| --- | --- |
| **CNK-code** | Belgische apotheekcode (7 cijfers) die de verpakking identificeert. |
| **Werkzaam bestanddeel (INN)** | De actieve stof, in het Frans en het Nederlands. |
| **ATC-code** | Anatomische, therapeutische en chemische classificatie (WHO), met beschrijving. |
| **BCFI-klasse** | Farmacotherapeutische indeling van het Belgisch Centrum voor Farmacotherapeutische Informatie. |
| **Zwarte driehoek** | Duidt op een geneesmiddel onder verscherpt toezicht (bijkomende geneesmiddelenbewaking). |
| **Vorm en toedieningsweg** | Farmaceutische vorm en toedieningsweg, in het Frans en het Nederlands. |
| **SKP en bijsluiter** | Links naar de Samenvatting van de Kenmerken van het Product en de patiëntbijsluiter (FR en NL). |
| **BCFI-link** | Rechtstreekse verwijzing naar de geneesmiddelenfiche op de BCFI-website. |
| **Voorschrift en fabrikant** | Afleveringsstatus (voorschrift vereist) en houder van de vergunning. |

!!! note "Een referentiekopie, geen bestelling"
    De SAM-databank van Resthome is een **lokale kopie**, geladen bij de
    installatie. Ze helpt u een geneesmiddel te identificeren en te documenteren;
    ze beheert geen voorraad of prijzen. Die leven op de catalogusfiche, zodra het
    geneesmiddel geïmporteerd is.

## De SAM-databank raadplegen

Via **Zorg → Configuratie → SAM-databank** doorbladert u het referentiebestand in
alleen-lezen. De lijst toont de CNK-code, de naam, het werkzaam bestanddeel, de
ATC-code, de vorm en de fabrikant.

Gebruik de zoekbalk en de filters om gericht te werken:

- **zoeken** op naam (FR/NL), CNK-code, ATC-code, werkzaam bestanddeel of
  fabrikant;
- **filters** « Prescription Required » (voorschrift vereist), « Black Triangle »
  (zwarte driehoek) en « With CNK » (met CNK-code);
- **groeperingen** op ATC-code, op vorm of op fabrikant.

De fiche van een geneesmiddel detailleert de identificatie, de classificatie, de
farmaceutische vorm, het werkzaam bestanddeel en de links naar de officiële
documenten (SKP en bijsluiter, FR en NL).

<!-- capture toe te voegen : fiche van een geneesmiddel in de SAM-databank, tabbladen identificatie / classificatie / officiële documenten -->

## De assistent Search SAM

De assistent **Search SAM** zoekt een geneesmiddel op in SAM en voegt het in één
beweging toe aan uw catalogus. Open hem via **WZC/RVT → Configuratie → eHealth
Configuration → Search SAM**.

### 1. Een zoekopdracht starten

Kies het **zoektype**:

- **By Name** — op merknaam of werkzaam bestanddeel (bv. *Dafalgan*, *Rilatine*);
- **By CNK Code** — op CNK-code.

Voer uw term in het zoekveld in en klik op **Search**. Het zoeken is
**ongevoelig voor accenten** en verwerkt meerdere woorden (bv. *Amlodipine 5mg*).

!!! tip "Eerst lokaal zoeken"
    De assistent bevraagt eerst de lokale kopie van SAM: het antwoord is meteen
    beschikbaar, ook zonder verbinding. Is die kopie leeg, dan kan Resthome
    overschakelen op de **DICS v5**-dienst in real time — maar die weg vereist een
    gecertificeerde eHealth-verbinding.

### 2. Kiezen uit de resultaten

De resultaten verschijnen in een tabel. Elke regel toont de **CNK**-code, de
**naam**, het **werkzaam bestanddeel (INN)**, de **sterkte**, de **vorm** en — in
optionele kolommen — de fabrikant, de ATC-code, de BCFI-klasse en de links naar
SKP / bijsluiter.

De kolom **In Catalog** geeft aan of het geneesmiddel al in uw catalogus staat.
Die regels verschijnen **in het blauw**: ze hoeven niet opnieuw aangemaakt te
worden.

Vink het vakje **Select** vooraan de regel aan voor elk te importeren
geneesmiddel.

<!-- capture toe te voegen : resultaten van Search SAM met aangevinkte Select-vakjes en de kolom In Catalog -->

### 3. Importeren naar de catalogus

Klik op **Import Selected**. Resthome maakt in uw catalogus één fiche per
aangevinkt geneesmiddel aan, met overname van de SAM-gegevens:

| SAM-gegeven | Catalogusveld |
| --- | --- |
| Name | Naam van het geneesmiddel |
| CNK | CNK-code |
| INN (werkzaam bestanddeel) | Werkzaam bestanddeel |
| Strength | Dosering |
| Form | Vorm (omgezet naar een Resthome-categorie) |
| Manufacturer | Fabrikant |
| ATC | ATC-code |
| SKP / bijsluiter / BCFI-link | Tabblad **Officiële documenten** van de fiche |

Een melding bevestigt het aantal **aangemaakte** (en in voorkomend geval
**bijgewerkte**) geneesmiddelen.

### 4. Een bestaand geneesmiddel bijwerken

Om een reeds aanwezige fiche te verversen, herhaalt u de zoekopdracht (knop
**Search Again**) en importeert u de regel opnieuw. Resthome **matcht op
CNK-code**: bestaat het geneesmiddel al, dan **werkt het de fiche bij** in plaats
van een dubbel aan te maken.

!!! warning "Een import vervangt het voorschrift niet"
    Een geneesmiddel importeren voegt het toe aan de **catalogus** van de
    instelling. Daarna moet het nog **voorgeschreven** worden aan de bewoner, met
    posologie en periode. Zie [Voorschriften en geneesmiddelen](prescriptions.md).

## Kernpunten om te onthouden

- **SAM = het officiële Belgische referentiebestand** van geneesmiddelen,
  ingebed in Resthome als basis van de catalogus.
- **Twee ingangen**: de raadpleging (Zorg → Configuratie → SAM-databank) en de
  importassistent **Search SAM** (WZC/RVT → Configuratie → eHealth Configuration).
- Het zoeken aanvaardt de **naam**, de **CNK-code** of het **werkzaam
  bestanddeel** en werkt **offline** op de lokale kopie.
- **Import Selected** maakt de fiches aan; een herimport **werkt** reeds aanwezige
  geneesmiddelen **bij** (matching op CNK).
- SAM levert **ATC, BCFI-klasse, zwarte driehoek, SKP en bijsluiter (FR/NL)** —
  betrouwbare gegevens, bij wijze van referentie.

## Verder

- [Voorschriften en geneesmiddelen](prescriptions.md)
- [Zorgplannen en vitale parameters](plans-de-soins.md)
- [De eHealth-integratie](../ehealth/index.md)