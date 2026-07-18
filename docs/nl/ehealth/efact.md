---
title: Elektronische facturatie (eFact)
description: "De volledige gids voor eFact in een woonzorgcentrum (WZC/RVT) met Resthome: RIZIV-forfaits genereren, controleren, factureren en versturen naar de mutualiteiten."
howto_auto: true
faq:
  - q: "Ik ontvang een ontvangstbewijs (931000) na de eFact-verzending, moet ik wachten?"
    a: "Ja. De 931000 bevestigt enkel dat de verzekeringsinstelling het lot heeft ontvangen en de eerste controle heeft doorstaan — het is niet het eindresultaat. U hoeft niets opnieuw te versturen: wacht op de afrekening (920900), die aangeeft wat aanvaard en betaald wordt. Dit kan enkele dagen duren."
  - q: "Wat betekent « termijn overschreden » op een eFact-periodekaart?"
    a: "De uiterste verzenddatum van deze periode is overschreden. Verzend het lot zonder uitstel: daarna kunnen sommige verzekeringsinstellingen het weigeren."
  - q: "Eén eFact-lot per mutualiteit of per unie?"
    a: "Eén lot per unie van mutualiteiten (100 Landsbond der Christelijke Mutualiteiten, 300 Solidaris, 500 Onafhankelijke Ziekenfondsen, 600 HZIV, 900 HR Rail…), niet per kleine afzonderlijke mutualiteit. Resthome zorgt automatisch voor de groepering."
  - q: "Hoe corrigeer ik een geweigerd eFact-lot?"
    a: "De code en de reden van weigering geven de oorzaak aan (verzekerbaarheid, forfait, datums). Corrigeer die en verzend opnieuw; de teller Heruitzendingen vermijdt dubbels en de knop Herintegratie laat toe om lijnen in een nieuwe verzending te herintegreren."
  - q: "Wat is het verschil tussen het ontvangstbewijs (931000) en de afrekening (920900)?"
    a: "De 931000 bevestigt enkel dat de verzekeringsinstelling uw lot heeft ontvangen en de eerste controle heeft doorstaan. De afrekening (920900) is het eindresultaat: ze geeft de bedragen aan die werkelijk aanvaard en/of geweigerd zijn. Zolang de afrekening niet binnen is, ligt niets definitief vast — maar u hoeft niets opnieuw te versturen."
  - q: "Wat betekent een globale weigering (920099) op een eFact-lot?"
    a: "Het volledige lot werd geweigerd door de verzekeringsinstelling. De code en de reden van weigering geven de oorzaak aan (verzekerbaarheid, forfait, datums…). Corrigeer die en verzend het lot opnieuw; de teller Heruitzendingen houdt de heruitzendingen bij om dubbels te vermijden."
  - q: "Hoe herintegreer ik geweigerde eFact-lijnen in een nieuwe verzending?"
    a: "Nadat u de oorzaak van de weigering hebt gecorrigeerd, gebruikt u de knop Herintegratie: die plaatst de betrokken lijnen in een nieuwe verzending, zonder de hele periode opnieuw te moeten doen."
  - q: "Kan ik een bewoner via eFact factureren als zijn verzekerbaarheid (MDA) niet gevalideerd is?"
    a: "Nee. Zonder geldige verzekerbaarheid (MDA) kan de bewoner niet in derdebetaler aan de mutualiteit gefactureerd worden. Voer MDA controleren uit vóór u de facturen aanmaakt en corrigeer indien nodig de mutualiteit van de bewoner."
  - q: "Is elektronische facturatie (eFact) verplicht?"
    a: "Ja. De elektronische verzending van de RIZIV-forfaits is verplicht: de productie is gestart in april 2026 en de uiterste rechte lijn om in orde te zijn is 1 oktober 2026. Resthome respecteert de uiterste verzenddatums per periode en waarschuwt u wanneer een termijn nadert of overschreden is."
  - q: "Een bewoner vertrekt of overlijdt tijdens een reeds gefactureerde maand: wat gebeurt er met de eFact?"
    a: "Een deel van het forfait werd te veel gefactureerd. Resthome detecteert dit bij de automatische controle en bereidt de overeenkomstige creditnota (of het saldo) voor, aan de kant van de bewoner en, indien nodig, aan de kant van de mutualiteit via een corrigerend lot."
  - q: "Waar zie ik de status van een eFact-verzending en de afrekening in Resthome?"
    a: "Op elk lot worden de status (Concept, verzonden, ontvangstbewijs, aanvaard, geweigerd) en de bedragen gefactureerd / aanvaard / geweigerd getoond. Voor een totaalbeeld van alle verzendingen van een maand opent u de eFact Cockpit vanuit de periode of een dashboardkaart: die toont in één oogopslag wat verzonden, aanvaard, geweigerd of in afwachting van afrekening is."
---

# Elektronische facturatie (eFact)

De **eFact** is de **elektronische** verzending van het **mutualiteitsaandeel**
(het RIZIV-forfait) naar de **verzekeringsinstellingen** (VI), via het eHealth-
/ MyCareNet-netwerk. Resthome stelt de bestanden samen, stuurt ze door en **volgt
de antwoorden** voor u op — ontvangstbewijzen, afrekeningen, aanvaardingen en
weigeringen.

Deze gids begeleidt u van begin tot einde: een periode genereren, controleren,
factureren, de eFact versturen en de antwoorden verwerken.

!!! info "Verplichting 2026"
    De elektronische facturatie van de forfaits is **verplicht**. De productie is
    gestart in **april 2026**; de uiterste rechte lijn om in orde te zijn is
    **1 oktober 2026**. Resthome respecteert de **uiterste verzenddata** per
    periode en waarschuwt u wanneer een termijn nadert of overschreden is.

## De cyclus van een periode in één oogopslag

Elke facturatiemaand is een **periode** die vier statussen doorloopt, in volgorde:

| Status | Wat het betekent |
|--------|------------------|
| **Draft** (concept) | De periode is aangemaakt, er is nog niets berekend. |
| **Generated** (gegenereerd) | De forfaits en aandelen zijn berekend, bewoner per bewoner. Te controleren. |
| **Invoiced** (gefactureerd) | De facturen zijn geboekt. De eFact kan samengesteld en verstuurd worden. |
| **Closed** (afgesloten) | De periode is voltooid en vergrendeld. |

De rode draad: **Genereren → controleren → Facturen aanmaken → eFact genereren →
versturen → antwoorden opvolgen**.

## 1. Het dashboard met periodes

Open de toepassing **MR/MRS → Dashboard**. Elke maand is een kaart die het
essentiële samenvat.

![Dashboard met facturatieperiodes, één kaart per maand met de eFact-status](../../assets/screenshots/efact/01-tableau-de-bord.webp)

Op elke kaart:

- de **status** van de periode (Invoiced, Generated…);
- **Invoices** (aantal facturen) en **Total**;
- **Resident Part** (het aandeel ten laste van de bewoner);
- de **uiterste eFact-datum** (bv. « eFact: 20 sept. »);
- snelkoppelingen: **View Invoices**, **eFact** (de loten), **eFact Cockpit**.

!!! warning "« termijn overschreden »"
    Toont een kaart **eFact: termijn overschreden** in het rood, dan is de uiterste
    verzenddatum van die periode **overschreden**. Verstuur zonder uitstel —
    daarna kunnen sommige verzekeringsinstellingen het lot weigeren.

## 2. De periode genereren (Draft → Generated)

Open de periode van de maand. In status **Draft** telt maar één knop: **Générer**.

![Facturatieperiode in status Draft, met de knop Générer en de automatische controleberichten rechts](../../assets/screenshots/efact/02-periode-draft.webp)

Een assistent **« Générer la facturation »** opent.

![Assistent Générer la facturation: periode, data, bewoners en MDA laden](../../assets/screenshots/efact/03-generer-wizard.webp)

- **Billing Period / data**: herinnering aan de betrokken maand.
- **Residents**: laat **leeg voor alle actieve bewoners** (of richt op een
  specifieke bewoner voor een bijzonder geval).
- **Charger MDA**: laadt de reeds gecontroleerde verzekerbaarheid (MDA) — « Succès »
  of « en attente ». De legende toont de MDA-status van de periode.

Klik op **Generate**. De periode gaat naar **Generated**: Resthome heeft voor
**elke bewoner** het Katz-forfait, het **RIZIV-aandeel** (mutualiteit) en het
**bewonersaandeel** berekend.

![Periode in status Generated: werkbalk Créer les factures / Vérifier MDA / Générer eFact, en tabel met bewoners, RIZIV-aandeel en bewonersaandeel](../../assets/screenshots/efact/04-periode-generated.webp)

In het tabblad **Residents** vindt u regel per regel terug:

- het **verblijfstype** (MR / MRS) en de **kamer**;
- de **Katz-categorie** (B, C, Cd, D…) of **No Katz**;
- de **aanwezigheidsdagen** en **afwezigheidsdagen**;
- het **RIZIV-aandeel**, het **bewonersaandeel** en het **totaalbedrag**.

De andere tabbladen: **Billing Lines** (de detailregels), **Invoices** (de
facturen), **eHealth** (de uitwisselingen) en **Info**.

## 3. Controleren vóór het factureren

Dit is de belangrijkste stap. Bovenaan de periode geven **tellers** de
gezondheidstoestand van de maand weer: **Suppléments**, **Absences**,
**Non facturés**, **MDA** en **Katz à faire** (ontbrekende Katz-evaluaties in te
vullen).

!!! tip "De automatische controle van Resthome"
    Na het genereren zeeft Resthome de periode en **signaleert de afwijkingen** in
    de discussiedraad (rechts). Elk bericht beschrijft het probleem **én** de te
    ondernemen actie. De meest voorkomende gevallen:

    - **Kamer vrijgekomen maar nog gefactureerd** (overfacturatie) — een bewoner
      heeft zijn kamer in de loop van de maand verlaten, maar het verblijf wordt
      nog gefactureerd. → Maak een **creditnota** aan of sluit het verblijf af.
    - **Forfait OA overgedeclareerd** — het einde van de RIZIV-tussenkomst (of een
      overlijden) ligt vóór het einde van de periode, maar het forfait werd verder
      gedeclareerd. → Maak een **creditnota / een saldo** aan voor de
      overgedeclareerde dagen.
    - **Overlijden — verblijf nog gefactureerd** — de bewoner is overleden maar de
      kamer is nog niet vrijgegeven (« Verblijf afsluiten »).
    - **Lopende afwezigheden** — niet-afgesloten afwezigheden beïnvloeden het
      forfait.

    Behandel elk punt (knop **Terminé** eens opgelost) vóór het factureren.

**Vérifier MDA** — de knop **Vérifier MDA** controleert de **verzekerbaarheid** van
uw bewoners bij de mutualiteiten (zie [Verzekerbaarheid (MDA)](mda.md)). Een
bewoner zonder geldige dekking kan niet in derdebetaler gefactureerd worden.

## 4. Facturen aanmaken (Generated → Invoiced)

Wanneer de controles op groen staan, klik op **Créer les factures**. Resthome
genereert en boekt:

- de **bewonersfacturen** (aandeel ten laste van de bewoner / de familie);
- het **mutualiteitsaandeel**, dat de eFact zal voeden.

De periode gaat naar **Invoiced**. U kunt nog altijd **Remettre en brouillon**
zolang u de eFact niet verstuurd hebt, indien een correctie nodig is.

## 5. De eFact genereren (de loten)

Klik op **Générer eFact**. Resthome stelt de **loten** samen — één elektronisch
bestand per verzekeringsinstelling — en toont dan de lijst **Lots eFact**.

<!-- capture toe te voegen: 06-lots-efact.png — lijst van de eFact-loten (één lot per unie, status, bedragen gefactureerd/aanvaard/geweigerd) -->

!!! note "Eén lot per unie van mutualiteiten"
    De verzendingen worden gegroepeerd **per unie** (de grote VI-families), niet
    per kleine individuele mutualiteit: **100** (Landsbond der Christelijke),
    **300** (Solidaris), **500** (Onafhankelijke ziekenfondsen), **600** (HZIV),
    **900** (HR Rail)… Resthome zorgt voor de groepering.

Elke lotregel toont:

- de **VI** en haar **code**;
- de **referentie** van het lot (bv. `EF/2026/…`) en de **facturatiemaand**;
- de **uiterste datum** van verzending en de **MDA**-status;
- de **status** van het lot (Draft, verstuurd, aanvaard, geweigerd…);
- de **bedragen**: gefactureerd, aanvaard, geweigerd;
- bij weigering, de **code** en de **reden van weigering**.

## 6. Versturen en de antwoorden opvolgen

Zodra de loten samengesteld zijn, **verstuurt** u ze: de verzending vertrekt naar
de verzekeringsinstellingen via het eHealth-netwerk.

De antwoordcyclus is automatisch:

1. **Ontvangstbewijs (931000)** — de VI bevestigt het lot **ontvangen** te hebben en de
   eerste controle doorstaan. **Dit is normaal: er valt niets opnieuw te versturen, u
   wacht op de afrekening** (enkele dagen).
2. **Melding met waarschuwingen (920098)** of **globale weigering (920099)** — in
   voorkomend geval: ofwel is het lot aanvaard ondanks kleine fouten, ofwel is het
   volledige lot geweigerd (te corrigeren en opnieuw te versturen).
3. **Afrekening (920900)** — het eindresultaat: **aanvaarde** en/of **geweigerde**
   bedragen. Resthome **punt de antwoorden af** en werkt elk lot bij (code en reden van
   weigering).

!!! warning "Een weigering behandelen"
    Wordt een lot (of een deel) **geweigerd**, dan zeggen de **code** en de **reden
    van weigering** waarom (verzekerbaarheid, forfait, data…). Corrigeer de oorzaak
    en **verstuur opnieuw**. De teller **Renvois** houdt de herzendingen bij om
    dubbels te vermijden.

De knop **Réintégration** laat toe om, indien nodig, regels opnieuw op te nemen
(bijvoorbeeld na correctie) in een nieuwe verzending.

## 7. De eFact-cockpit

Vanaf een periode of een dashboardkaart biedt **eFact Cockpit** een
**stuuroverzicht**: de status van alle loten en verzendingen in één oogopslag —
doorgestuurd, aanvaard, geweigerd, in afwachting. Het ideale scherm om een
**maandelijkse campagne op te volgen** en te zien wat blokkeert.

<!-- capture toe te voegen: 07-cockpit.png — eFact Cockpit, stuuroverzicht van alle verzendingen -->

## 8. Creditnota's en regularisaties

Wanneer een bewoner in de loop van een reeds gefactureerde maand **vertrekt** of
**overlijdt**, werd een deel van het verblijf of het forfait **overgefactureerd**.
Resthome detecteert dit (zie de automatische controle hierboven) en bereidt de
overeenkomstige **creditnota** of het **saldo** voor, om de niet-verschuldigde
periode terug te betalen — aan bewonerszijde **én**, indien nodig, aan
mutualiteitszijde via een corrigerend lot.

## Vereisten

!!! warning "Te controleren vóór de verzending"
    - **Verzekerbaarheid (MDA)** gecontroleerd voor de periode.
    - Correcte **mutualiteit** op elke bewoner.
    - Facturen **geboekt** (periode in status *Invoiced*).
    - **eHealth-certificaat** actief.

## Belangrijkste punten om te onthouden

- De periode volgt altijd de volgorde **Draft → Generated → Invoiced → Closed**.
- **Controleer vóór het factureren**: behandel elk automatisch controlebericht.
- **Controleer de MDA** — geen derdebetaler zonder geldige verzekerbaarheid.
- **Eén eFact-lot per unie** van mutualiteiten, niet per mutualiteit.
- Respecteer de **uiterste verzenddatum** van elke periode (« termijn overschreden »).
- Een **weigering** corrigeert u en **verstuurt u opnieuw** — de teller Renvois
  vermijdt dubbels.

## Verder

- [eFact-weigeringen — oorzaken en oplossingen](efact-rejets.md)
- [Verzekerbaarheid (MDA)](mda.md)
- [Akkoorden (eAgreement)](eagreement.md)
- [Vertrek en overlijden](../facturation/depart-deces.md)
- [Afwezigheden en hospitalisaties](../facturation/absences.md)
- [Facturatie-overzicht](../facturation/index.md)
