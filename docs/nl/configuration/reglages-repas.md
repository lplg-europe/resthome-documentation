---
title: Instellingen voor maaltijden en voeding
description: "Het tabblad Maaltijden in Resthome instellen voor een woonzorgcentrum (WZC/RVT): voedingsbron, openbaar menu, kiosk, familiemeldingen en ESPEN-streefwaarden."
faq:
  - q: "Moet ik CIQUAL of NUBEL als voedingsbron kiezen?"
    a: "CIQUAL (ANSES, Frankrijk) is de standaardbron: de databank met 3484 voedingsmiddelen is al geladen, u kunt ze meteen gebruiken. NUBEL (België) moet eerst geïmporteerd worden. Houd om te starten CIQUAL aan; schakel enkel over op NUBEL als u de Belgische referenties nodig hebt en de import gebeurd is."
  - q: "Waarvoor dient de waarschuwingsdrempel voor innametekort?"
    a: "Resthome vergelijkt de gemiddelde inname over 3 dagen met de behoefte van de bewoner (energie en eiwitten). Dekt die inname minder dan de ingestelde drempel (standaard 75 %), dan wordt een tekortwaarschuwing aangemaakt. Verlaag de drempel om later gewaarschuwd te worden, verhoog ze om vroeger gewaarschuwd te worden."
  - q: "Zijn de ESPEN-streefwaarden voor elke bewoner gelijk?"
    a: "Nee. De coëfficiënten (30 kcal/kg, 1 g/kg eiwit, 1,6 l voor vrouwen en 2,0 l voor mannen) zijn instellingen voor het hele woonzorgcentrum. Resthome berekent daarna de streefwaarde per bewoner op basis van gewicht en geslacht. De energieband stijgt naar 35 kcal/kg bij een bewoner met ondergewicht (BMI kleiner dan of gelijk aan 21)."
  - q: "Waarom hebben de maaltijdmeldingen aan families geen effect?"
    a: "E-mailverzending vereist een uitgaande mailserver die in Odoo geconfigureerd is. Zonder die server levert het inschakelen van de optie geen enkele verzending op. Configureer eerst de uitgaande server, activeer daarna de globale melding en de opt-in per bewoner."
  - q: "Waar vind ik deze instellingen?"
    a: "Bij Instellingen > Maaltijden. Het tabblad bundelt vier blokken: Voeding, Openbaar menu en kiosk, Meldingen aan families, en Nutritionele streefwaarden (ESPEN)."
---

# Instellingen voor maaltijden en voeding

Het tabblad **Maaltijden** van de instellingen bundelt de configuratie van de
toepassing Maaltijden: de **bron van de voedingsgegevens**, het **uitzicht van het
openbaar menu en de kiosk**, de **meldingen aan families** en de **nutritionele
streefwaarden (ESPEN)** die dienen voor de opvolging van ondervoeding. U vindt het
bij **Instellingen > Maaltijden**.

Deze instellingen gelden voor het hele woonzorgcentrum: u legt ze één keer vast en
daarna wijzigen ze slechts uitzonderlijk.

## Voeding

Deze sectie bepaalt welke **referentiedatabank** Resthome raadpleegt om de
voedingswaarden van de ingrediënten op te zoeken (calorieën, eiwitten…).

| Instelling | Waarvoor dient het | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Bron van voedingsgegevens** | Referentiedatabank van de voedingswaarden. CIQUAL (ANSES, Frankrijk): 3484 voedingsmiddelen, al geladen. NUBEL (België): Belgische databank, te importeren. | **CIQUAL** (standaard, al geladen) |

!!! tip "CIQUAL volstaat om te starten"
    De databank **CIQUAL** is voorgeladen: u kunt uw menu's samenstellen en de voeding
    opvolgen zonder enige voorbereiding. Schakel enkel over op **NUBEL** als u
    specifiek de Belgische referenties nodig hebt — de import moet dan vooraf gebeurd
    zijn.

## Openbaar menu en kiosk

Deze instellingen personaliseren het uitzicht van de pagina's **menu van de dag**,
**menu van de week** en **kiosk** (zie [Familieportaal en kiosk](../repas/portail-familles.md)).

| Instelling | Waarvoor dient het | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Kleur van het openbaar menu** | Hoofdkleur van de menu- en kioskpagina's. | Uw huisstijlkleur (standaard `#0d6efd`) |
| **Bedrijfslogo tonen** | Toont het bedrijfslogo bovenaan de pagina's van het openbaar menu. | Ingeschakeld |
| **Kioskverversing (seconden)** | Interval voor de automatische verversing van de kioskpagina (`/menu/kiosk`) in de eetzaal. | 600 s (10 min) |

!!! note "Waarden eigen aan uw instelling"
    De **kleur** en het **logo** zijn eigen aan uw woonzorgcentrum: gebruik uw
    huisstijl. De kioskverversing is enkel nuttig als een scherm de pagina
    `/menu/kiosk` doorlopend toont.

## Meldingen aan families

Dit blok activeert de automatische verzending van e-mails aan families die dit
aanvaard hebben: een **wekelijkse samenvatting** van de maaltijden en een
**waarschuwing bij lage inname**.

| Instelling | Waarvoor dient het | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Maaltijdmeldingen aan families** | Stuurt families die opt-in gaven een wekelijkse samenvatting en een waarschuwing bij lage inname. Vereist een uitgaande mailserver. | Ingeschakeld **als** een uitgaande mailserver geconfigureerd is, anders uitgeschakeld |

!!! warning "Een uitgaande mailserver is vereist"
    Zonder **uitgaande mailserver** die in Odoo geconfigureerd is, verstuurt het
    inschakelen van de optie niets. De verzending hangt ook af van een **opt-in per
    bewoner**: enkel families die dit aanvaard hebben, ontvangen de e-mails.
    Configureer de uitgaande server, activeer de globale melding en daarna de opt-in
    per bewoner.

## Nutritionele streefwaarden (ESPEN)

Deze coëfficiënten, uit de geriatrische **ESPEN**-aanbevelingen, dienen om de
**streefwaarde per bewoner** te berekenen (op basis van gewicht en geslacht) en om de
**tekortwaarschuwingen** te activeren.

| Instelling | Waarvoor dient het | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Energie (kcal/kg/dag)** | Energiestreefwaarde per kilo lichaamsgewicht. | 30 |
| **Energie bij ondergewicht (kcal/kg/dag)** | Verhoogde streefwaarde voor een ondervoede bewoner (BMI kleiner dan of gelijk aan 21); ESPEN stelt 32 tot 38 voor. | 35 |
| **Eiwitten (g/kg/dag)** | Eiwitstreefwaarde per kilo lichaamsgewicht (minstens 1; 1,2 tot 1,5 bij ziekte). | 1 |
| **Vocht — vrouwen (ml/dag)** | Dagelijkse hydratatiestreefwaarde voor vrouwen. | 1600 |
| **Vocht — mannen (ml/dag)** | Dagelijkse hydratatiestreefwaarde voor mannen. | 2000 |
| **Waarschuwing innametekort (% dekking)** | Drempel waaronder een waarschuwing wordt aangemaakt wanneer de gemiddelde inname over 3 dagen onvoldoende van de energie- of eiwitstreefwaarde dekt. | 75 |

!!! info "Een per bewoner berekende streefwaarde"
    U stelt hier de **coëfficiënten** in; Resthome leidt daaruit de **individuele
    streefwaarde** van elke bewoner af volgens gewicht en geslacht, en vergelijkt
    vervolgens de werkelijke **inname** met die streefwaarden. De opvolging van de
    dekking en de screening van ondervoeding staan beschreven in [Menu's, diëten en
    hydratatie](../repas/menus-regimes.md).

## Verder

- [Menu's, diëten en hydratatie](../repas/menus-regimes.md)
- [Familieportaal en kiosk](../repas/portail-familles.md)
- [Overzicht van de Maaltijden](../repas/index.md)
- [Klinische registers](../soins/registres.md)