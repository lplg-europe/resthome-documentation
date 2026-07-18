---
title: De app Supplementen
description: "De app Supplementen van een woonzorgcentrum (WZC/RVT): invoer voor meerdere bewoners via de catalogus, eenmalige of terugkerende supplementen, conventies, catalogus en rapportage."
faq:
  - q: "Waarvoor dient de app Supplementen in een woonzorgcentrum (WZC/RVT)?"
    a: "Het is het speciale scherm om supplementen in te voeren: de catalogus van een bewoner openen, supplementen aan meerdere bewoners tegelijk toevoegen, de terugkerende conventies beheren, de catalogus van supplementen bijhouden en de gefactureerde bedragen opvolgen."
  - q: "Hoe voeg ik een supplement aan meerdere bewoners tegelijk toe?"
    a: "Selecteer op het scherm Bewoners meerdere bewoners (Ctrl+klik op een computer, lang indrukken op een tablet, of de knop « Meervoudige selectie ») en klik dan op « Supplementen (N) ». Eén catalogus opent en elk toegevoegd supplement wordt doorgevoerd op de open enveloppe van elke geselecteerde bewoner."
  - q: "Wat is het verschil tussen een eenmalig supplement en een conventie?"
    a: "Een eenmalig supplement wordt één keer gefactureerd op de enveloppe van de maand (kapper, drank…). Een conventie bundelt de terugkerende supplementen van de bewoner (eenpersoonskamer, tv, telefoon): ze leeft op de bewoner en overleeft een afsluiting van verblijf, een kamerwissel of een overdracht."
  - q: "Waar bepaal ik de lijst van supplementen en hun prijzen?"
    a: "In Configuratie → Catalogus. Elk supplement heeft een type (dagelijks, maandelijks of eenmalig), een prijs eigen aan de instelling en, indien nodig, een AViQ-code voor de aangifte aan de verzekeringsinstelling."
  - q: "Kan ik de gefactureerde supplementen per bewoner of per maand opvolgen?"
    a: "Ja, via het menu Rapportage: grafiek-, draaitabel- en lijstweergaven verdelen de gefactureerde supplementen per bewoner, per product en per maand."
---

# De app Supplementen

De app **Supplementen** is het speciale scherm om de supplementen van de bewoners
in te voeren en te beheren. Ze verzamelt op één plek wat anders verspreid zit over
de bewonersfiche en de facturatieperiode: de catalogus van een bewoner openen,
supplementen aan meerdere bewoners tegelijk toevoegen, de terugkerende conventies
beheren, de catalogus bijhouden en de gefactureerde bedragen opvolgen.

U vindt ze in het **hoofdmenu → app Supplementen**.

!!! info "Deze pagina vult « De supplementen » aan"
    De basisbegrippen — de **supplementenenveloppe** per bewoner en per maand, de
    **automatische synchronisatie** van de factuur, de bescherming wanneer een
    maand al geboekt is — staan uitgelegd in [De supplementen](supplements.md).
    Deze pagina beschrijft de **speciale app** en haar invoersneltoetsen. De app
    maakt geen parallelle gegevens aan: ze werkt op dezelfde enveloppes en
    dezelfde conventies.

<!-- capture toe te voegen : de app Supplementen geopend op het scherm Bewoners (kanban-weergave) -->

## Het scherm Bewoners (het vertrekpunt)

Bij het openen toont de app het scherm **Bewoners**: de lijst van de actieve
bewoners, in **kanban-weergave** (kaarten) of in **lijstweergave**. Elke kaart
toont de foto, de naam, de **kamer** en het **verblijfstype** (MR / MRS), met een
winkelmandje-icoon « Supplementen toevoegen ».

- **Klik op een bewoner**: Resthome opent meteen de **catalogus** van zijn
  supplementenenveloppe van de lopende maand. U komt rechtstreeks op het
  toevoegraster terecht, zonder langs de fiche te gaan.
- In **lijstweergave** draagt elke regel een knop **Supplementen toevoegen**, en
  de kop een knop **Via catalogus toevoegen** om de aangevinkte bewoners te
  bedienen.

!!! tip "Filteren en groeperen"
    De zoekbalk filtert op **MR** / **MRS** en groepeert op **kamer** of op
    **verblijfstype** — handig om snel een vleugel of een verdieping te vinden
    vóór een gegroepeerde invoer.

## Supplementen aan meerdere bewoners toevoegen

Dit is de centrale sneltoets van de app: hetzelfde supplement op meerdere bewoners
toepassen zonder elke fiche opnieuw te openen.

1. Op het scherm **Bewoners** **selecteert u meerdere bewoners**:
   - **Ctrl+klik** (of Cmd+klik) op een computer voegt een bewoner toe of
     verwijdert hem; **Shift+klik** breidt de selectie uit tot een reeks;
   - **lang indrukken** op een aanraaktablet;
   - of activeer de knop **Meervoudige selectie**, waarna een gewone klik
     selecteert.
2. Klik op de knop **Supplementen (N)** die verschijnt (N = aantal geselecteerde
   bewoners). In lijstweergave gebruikt u **Via catalogus toevoegen**.
3. **Eén catalogus** opent. Elk supplement dat u erin toevoegt, wijzigt of
   verwijdert, wordt **doorgevoerd op de open enveloppe van elke geselecteerde
   bewoner**, voor de lopende maand.

In deze gedeelde catalogus toont het linkerpaneel een sectie **Bewoners**: de
betrokken bewoners verschijnen als labels (de « leidende » bewoner in het grijs,
de andere in het groen). Via de link **Toevoegen** voegt u er onderweg nog toe;
een label verwijderen haalt de bewoner eruit (de laatste kan niet verwijderd
worden).

<!-- capture toe te voegen : de multi-bewonercatalogus met de sectie Bewoners (labels) links -->

!!! note "Een supplement dat al onder een conventie valt, wordt overgeslagen"
    Heeft een van de geselecteerde bewoners dit product al in een **actieve
    conventie**, dan wordt de regel voor hem **niet** toegevoegd (ze zou bij de
    facturatie toch geweerd worden) — de andere bewoners krijgen ze gewoon. Bij
    invoer op één enkele bewoner blokkeert Resthome de toevoeging ronduit en
    verwijst het u naar de conventie.

## Eenmalige en terugkerende supplementen

De app onderscheidt de twee aarden van supplementen die al voorgesteld werden in
[De supplementen](supplements.md).

- **Eenmalig** — toegevoegd aan de enveloppe van de maand via de catalogus
  (kapper, pedicure, drank, telefoon…). Het menu **Eenmalige supplementen** geeft
  er de **lijst** van, gegroepeerd per bewoner, met de periode, het product, de
  hoeveelheid, de prijs en het totaal. Dit is de plek om alles na te lezen wat de
  maand met de hand werd ingevoerd.
- **Terugkerend** — elke maand hernomen via een **conventie** (zie de volgende
  sectie).

<!-- capture toe te voegen : het menu Eenmalige supplementen, lijst gegroepeerd per bewoner -->

!!! tip "Waar is mijn supplement gebleven?"
    Bij elke toevoeging toont Resthome een melding met **op welke periode(s)** het
    supplement werd gefactureerd — of het verwittigt u dat **geen enkele open
    periode** nog met zijn datum overeenkomt (het wordt dan pas gefactureerd
    wanneer de betrokken maand gegenereerd is). Controleer de **startdatum** als
    het supplement niet verschijnt waar u het verwachtte.

## De supplementenconventies

Een **conventie** bundelt de **terugkerende** supplementen van een bewoner
(eenpersoonskamer, tv, telefoon…). Ze leeft op de **bewoner**, niet op het
verblijf: ze **overleeft** een afsluiting van verblijf, een kamerwissel of een
overdracht MR ↔ MRS. Elke bewoner heeft **één enkele** conventie, die al zijn
terugkerende regels verzamelt.

In de app somt het menu **Conventies** de regels van terugkerende supplementen op
(bewoner, conventie, product, type, data, hoeveelheid, actief). De conventie zelf
— met haar status en haar knoppen — beheert u via de app **MR/MRS → Facturatie →
Supplementenconventies**.

Op de conventie:

| Element | Rol |
|---|---|
| **Status** | **Open** of **Gesloten** (bovenaan de fiche). |
| Knop **Afsluiten** | Legt een **einddatum** vast en stopt de facturatie van elke regel daarna. |
| Knop **Heropenen** | Wist de einddatum en heractiveert de regels die afgesloten waren. |
| **Regels** | Product, type, prijs, startdatum, einddatum, hoeveelheid, actief, notities. |

<!-- capture toe te voegen : een supplementenconventie met de knop Afsluiten en de lijst van regels -->

!!! warning "Een product onder conventie voert u niet eenmalig in"
    Zolang een product door een **actieve conventie** gedekt is, kan het niet als
    eenmalig supplement voor dezelfde bewoner toegevoegd worden. Voeg het toe **in
    de conventie**, of **sluit** die eerst **af**.

## De catalogus van supplementen

Het menu **Configuratie → Catalogus** houdt de lijst van de factureerbare
**supplementtypes** bij (« Supplementtypes »). Elk supplement heeft er:

| Veld | Beschrijving |
|---|---|
| **Referentie** | Interne code van het supplement. |
| **Naam** | Benaming getoond in de catalogus. |
| **Supplementtype** | **Dagelijks** (pro rata van de dagen gefactureerd), **Maandelijks** (per maand) of **Eenmalig** (één keer). |
| **Prijs** | Eenheidsbedrag — **waarde eigen aan de instelling**. |
| **AViQ-code** | Pseudo-code voor aangifte, wanneer het supplement aan de verzekeringsinstelling wordt aangegeven. |

!!! info "Aangegeven aan de VI of niet?"
    Naargelang zijn **categorie** wordt een supplement ofwel **aangegeven aan de
    verzekeringsinstelling** in de eFact (ET50), ofwel **uitsluitend op de factuur
    van de bewoner** gefactureerd. Deze instelling gebeurt op de productcategorie —
    zie [Facturatie-instellingen](../configuration/reglages-facturation.md).

## De rapportage

Het menu **Rapportage** opent een analyseweergave van de **gefactureerde**
supplementen:

- een **grafiek** van de bedragen per product;
- een **draaitabel** (bewoners × maand);
- een **lijst** met de detailregels van de supplementen.

U kunt filteren tussen **eenmalige** en **conventie**-supplementen, en groeperen
per **bewoner**, **product** of **maand**.

<!-- capture toe te voegen : de rapportage van de supplementen (draaitabel bewoners × maand) -->

!!! note "Pas na generatie"
    De supplementen verschijnen pas in de rapportage zodra de
    **facturatieperiode gegenereerd** is voor de betrokken maand.

## Kernpunten om te onthouden

- De app **Supplementen** is een speciaal invoerscherm; ze werkt op **dezelfde
  enveloppes en conventies** als de facturatie — geen dubbele gegevens.
- Het scherm **Bewoners** is het vertrekpunt: klik op een bewoner om zijn catalogus
  te openen, of **selecteer er meerdere** (Ctrl+klik / lang indrukken /
  **Meervoudige selectie**) en dan **Supplementen (N)** om ze in één keer te
  bedienen.
- **Eenmalig** = één keer op de enveloppe; **conventie** = terugkerend, op de
  bewoner, bestand tegen verblijfswijzigingen.
- Een product onder **actieve conventie** voert u niet eenmalig in.
- De **catalogus** draagt het type en de prijs (waarde eigen aan de instelling);
  de **rapportage** volgt de bedragen per bewoner, product en maand.

## Verder

- [De supplementen](supplements.md)
- [Een maand factureren, stap voor stap](facturer-un-mois.md)
- [Facturatie-overzicht](index.md)
- [Facturatie-instellingen](../configuration/reglages-facturation.md)