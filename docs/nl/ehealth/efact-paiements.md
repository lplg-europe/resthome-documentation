---
title: Betalingen opvolgen en afrekeningen afpunten
description: "Weten of de mutualiteit uw forfaits in het woonzorgcentrum (WZC/RVT) betaald heeft: de afrekening (920900) lezen, automatisch afpunten en trage VI's aanmanen."
howto_auto: true
faq:
  - q: "Wat is het verschil tussen het ontvangstbewijs (931000) en de afrekening (920900)?"
    a: "Het ontvangstbewijs (931000) bevestigt enkel dat de verzekeringsinstelling uw zending ontvangen en de eerste controle doorstaan heeft — er is nog niets betaald. De afrekening (920900) is het eindresultaat: ze toont regel per regel wat aanvaard en wat geweigerd wordt, en geldt als betaalbericht in Rekening C. Zolang de afrekening niet binnen is, is geen enkel bedrag definitief."
  - q: "Hoe weet ik of een eFact-zending betaald is in Resthome?"
    a: "Open het lot: het tabblad Betaling toont Betaald, de betalingsreferentie en het bedrag. In Rekening C markeert Resthome het lot automatisch als Betaald zodra de afrekening een echte betalingsreferentie draagt. Voor een totaalbeeld bundelt de eFact Cockpit de afgerekende maar nog niet afgepunte zendingen en de VI's die te laat betalen."
  - q: "Wat betekent een afrekening « afpunten »?"
    a: "Afpunten betekent bevestigen dat het door de afrekening aangekondigde geld ook effectief ontvangen is. Resthome letter elke afrekening automatisch af tegen haar lot; u bevestigt de ontvangst door de afrekening te openen en op Mark Reconciled (afgepunt) te klikken."
  - q: "Een verzekeringsinstelling betaalt te laat: kan ik nalatigheidsintresten vorderen?"
    a: "Ja, als de zending tijdig werd ingediend (uiterlijk de 20e van maand M+1). De VI moet betalen tegen het einde van de 2e maand na de indiening; daarna berekent Resthome de nalatigheidsintresten (aanvaard bedrag × wettelijke rentevoet × dagen vertraging / 365). De wettelijke rentevoet stelt u in bij de eHealth-instellingen."
  - q: "De afrekening toont zowel aanvaarde ALS geweigerde bedragen: wat nu?"
    a: "Dat is een gedeeltelijke weigering: het aanvaarde deel wordt betaald, de geweigerde regels moeten gecorrigeerd en opnieuw verzonden worden. Resthome maakt automatisch een reliquat aan voor de geweigerde regels en zet ze in de lijst Rejected lines (geweigerde regels) van de Cockpit."
  - q: "Waar zie ik de lijst van alle ontvangen afrekeningen en VI-antwoorden?"
    a: "De eFact Cockpit biedt de lijst OA retrievals (VI-ophalingen): alle opgehaalde berichten (ontvangstbewijzen, afrekeningen, weigeringen), filterbaar op VI, maand en type, met XLSX-export. De lijst eFact Settlements toont enkel de afrekeningen (920900)."
---

# Betalingen opvolgen en afrekeningen afpunten

Zodra uw forfaits via [eFact](efact.md) verstuurd zijn, blijft de echte vraag
over: **« ben ik betaald? »**. Deze pagina legt uit hoe Resthome daarop
antwoordt, van de automatisch afgepunte **afrekening (920900)** tot het
**aanmanen van trage verzekeringsinstellingen (VI)**.

U vindt alles in de toepassing **MR/MRS → eHealth → eFact**:

- de **Cockpit** — uw stuurbord « wat nu te doen »;
- **eFact Settlements** — de lijst met ontvangen **afrekeningen**;
- **eFact Batches** (eFact-loten) — elk lot en zijn **tabblad Betaling**.

!!! info "Ontvangstbewijs ≠ afrekening"
    Verwar de twee VI-antwoorden niet. Het **ontvangstbewijs (931000)** zegt
    enkel « goed ontvangen ». De **afrekening (920900)** zegt « dit is wat ik
    betaal ». Voor het geld telt de afrekening.

## Ontvangstbewijs (931000) of afrekening (920900): het juiste houvast

| Antwoord | Wat het betekent | Is er betaling? |
|---|---|---|
| **Ontvangstbewijs (931000)** | De VI heeft uw zending **ontvangen** en de eerste formaatcontrole doorstaan. | Nee — er is nog niets beslist. Wacht op de afrekening. |
| **Afrekening (920900)** | Het **eindresultaat**, regel per regel: **aanvaarde** en **geweigerde** bedragen. In Rekening C **geldt ze als betaalbericht**. | Ja — hier verschijnt wat effectief betaald wordt. |

!!! note "Rekening C (Wallonië / AViQ)"
    Sinds 2025 werkt de Waalse WZC/RVT-facturatie met **Rekening C**: de VI
    betaalt en **de afrekening geldt als betaalbericht**. De afrekening draagt
    dus de **betalingsreferentie** en het **bedrag**, maar **geen betaaldatum**
    (het formaat voorziet er geen). Resthome verzint nooit een datum: die blijft
    leeg zolang geen echte bankdatum wordt ingevoerd.

## 1. De afrekening (920900) automatisch afgepunt

Wanneer een afrekening van de VI terugkomt (via de automatische ophaling of de
knop **Process Response** op een lot), **letter Resthome ze vanzelf af**, zonder
invoer van uw kant:

1. ze maakt een **afrekening (Settlement)** aan, gekoppeld aan het lot;
2. ze **koppelt elke regel** van de afrekening terug aan de gefactureerde regel
   van de juiste bewoner (op NISS en bedrag);
3. ze markeert elke regel **aanvaard** of **geweigerd**; een aanvaard forfait
   wordt niet herhaald in de afrekening, dus **elke niet-vermelde regel geldt
   als aanvaard** (AViQ-regel);
4. ze **werkt de status van het lot bij**: **settled** (alles aanvaard),
   **rejected** (alles geweigerd) of **partial_reject** (mengeling, of
   gedeeltelijke afrekening in afwachting van de rest);
5. bij geweigerde regels bereidt ze **automatisch een reliquat** voor om ze
   opnieuw in te dienen (zie [eFact-weigeringen](efact-rejets.md)).

In Rekening C markeert Resthome het lot automatisch als **Betaald** zodra de
afrekening een **echte betalingsreferentie** en een **positief aanvaard bedrag**
draagt. Een volledig geweigerde afrekening (0 € aanvaard) draagt wel een
referentie maar betaalt niets — ze wordt dus **niet** als betaald gemarkeerd.

## 2. Het scherm eFact Settlements (de afrekeningen)

Menu **eHealth → eFact → eFact Settlements**. Dit is de lijst van alle ontvangen
**afrekeningen (920900)**, één per betaling.

De lijst toont: de **referentie**, het betrokken **lot**, de
**ontvangstdatum**, de bedragen **Accepted** / **Rejected** / **Paid** en de
**betalingsreferentie**, plus een **statusbadge**.

<!-- schermafbeelding toe te voegen: lijst eFact Settlements — één afrekening per regel met aanvaarde/geweigerde/betaalde bedragen en statusbadge -->

Open een afrekening voor het detail. Het scherm is **alleen-lezen** (er wordt
niets manueel ingevoerd) en doorloopt drie statussen:

| Status | Betekenis |
|---|---|
| **Received** (ontvangen) | De afrekening is net binnen. |
| **Processed** (verwerkt) | Haar regels zijn over het lot verdeeld. Resthome doet deze stap **automatisch** bij ontvangst. |
| **Reconciled** (afgepunt) | U hebt **bevestigd** dat het geld effectief ontvangen is. |

- De knop **Process** (verwerken) verschijnt enkel als een afrekening in
  *Received* is blijven staan zonder verwerking — klik om ze te verdelen.
- De knop **Mark Reconciled** (als afgepunt markeren) bevestigt de ontvangst van
  de betaling nadat u ze op uw bankuittreksel hebt nagekeken.

Het tabblad **Lines** detailleert, regel per regel: nr., bewoner, gevraagd,
aanvaard, geweigerd bedrag, het vinkje **Accepted**, en — bij weigering — de
**code** en de **weigeringsreden**. Geweigerde regels springen in het rood eruit.

!!! tip "De afrekening lezen zoals de VI ze verstuurde"
    Een knop **Decoded 920900** (voorbehouden aan eHealth-beheerders) toont het
    ruwe afrekeningsbestand, zone per zone, om een waarde zo dicht mogelijk bij
    de bron na te kijken.

## 3. Het tabblad Betaling van een lot

Op een lot ([eFact-loten](efact.md)) vat, zodra de zending vertrokken is, de
groep **Payment** (Betaling) de betaalstatus samen:

- **Paid** (Betaald) — het vinkje wordt groen wanneer het lot betaald is;
- **Payment Reference** — de betalingsreferentie van de VI;
- **Payment Date** — de datum (vaak leeg in Rekening C, zie hoger);
- **Total Paid** — het betaalde bedrag.

!!! info "Manueel als betaald markeren"
    Sommige VI's betalen zonder bruikbare betalingsreferentie in de afrekening.
    Een eHealth-beheerder kan dan **Marked Paid Manually** (manueel als betaald
    gemarkeerd) inschakelen om de buiten de stroom ontvangen betaling vast te
    leggen.

Een kader **Status** toont in één badge waarop het lot wacht: *Awaiting OA
response* (wacht op antwoord), *Awaiting settlement (920900)* (wacht op de
afrekening), *Complete* (voltooid) of *Rejected* (te corrigeren). Wanneer een lot
**settled** is, laat de knop **Close** (afsluiten) toe het definitief te
klasseren.

In de lotenlijst helpen de filters **Paid** / **Unpaid** (betaald / onbetaald)
en de optionele kolommen **Payment Ref.**, **Payment Date**, **Amount Paid** om
maand per maand de balans op te maken.

## 4. De eFact Cockpit: « ben ik betaald? » in één oogopslag

Menu **eHealth → eFact → Cockpit** (ook bereikbaar vanuit een periode of een
dashboardkaart). De Cockpit ordent al het werk in **actiestapels**, met een
teller en een knop per stapel. Drie stapels beantwoorden rechtstreeks de vraag
naar de betaling.

<!-- schermafbeelding toe te voegen: eFact Cockpit — tellerknoppen (To reconcile, Overdue payments, Rejected lines, OA retrievals) en tabel « Rejects by cause » -->

- **To reconcile** (af te punten) — de **afgerekende loten waarvan de betaling
  nog niet bevestigd is**. Het totale verwachte bedrag staat vermeld; de knop
  **Reconcile payments** opent de lijst om ze één voor één af te punten.
- **Overdue payments** (achterstallige betalingen) — de zendingen die
  **aanvaard maar nog steeds onbetaald** zijn en waarvan de **VI-betaaltermijn
  verstreken** is. Zie het aanmanen hieronder.
- **Rejected lines** (geweigerde regels) — de **werklijst** van geweigerde
  regels die nog opnieuw verzonden moeten worden (bewoner + code + bedrag),
  filterbaar op oorzaak, VI en maand.

Twee bakens vervolledigen het beeld:

- **OA retrievals** (VI-ophalingen) — het **volledige logboek** van alles wat de
  VI terugstuurde: ontvangstbewijzen, afrekeningen en weigeringen, filterbaar op
  VI, maand en type, met een knop **Export XLSX**.
- **Rejects by cause** (weigeringen per oorzaak) — een tabel die de geweigerde
  regels **per reden** groepeert, om de systemische oorzaak aan te pakken in
  plaats van regel per regel.

!!! tip "De antwoorden gaan ophalen"
    Blijven er loten in afwachting, dan bevraagt de knop **Fetch responses**
    (antwoorden ophalen) het VI-platform en werkt de statussen bij. De antwoorden
    komen ook automatisch binnen, maar deze knop forceert een onmiddellijke
    controle.

## 5. Een trage VI aanmanen

De stapel **Overdue payments** lijst de zendingen op die **tijdig ingediend**,
door de VI **aanvaard** maar **niet betaald** zijn na de vervaldag. De knop
**Chase (by OA)** opent die loten **gegroepeerd per verzekeringsinstelling**: u
ziet meteen **wie u moet aanmanen** en **voor welk bedrag** (het aanvaarde
totaal wordt per VI opgeteld).

Om de VI aan te schrijven bereidt de knop **Contact OA** (aanwezig op elk lot)
het contact met de juiste facturatiecontactpersoon voor.

## 6. Nalatigheidsintresten

Een te laat betaalde zending kan recht geven op **nalatigheidsintresten**.
Resthome past de AViQ-regel toe:

- de zending moet **tijdig ingediend** zijn (verstuurd uiterlijk de **20e van
  maand M+1**) — dat is de voorwaarde voor **aanspraak**;
- de VI moet betalen **tegen het einde van de 2e maand na de indiening**: dat is
  de **OA Payment Deadline** (betaaltermijn);
- na die datum lopen de intresten, berekend als:
  **aanvaard bedrag × jaarlijkse wettelijke rentevoet × dagen vertraging / 365**.

Op het lot verschijnt, zodra de termijn verstreken is en het lot nog onbetaald,
een groep **Late-payment interest (OA)** met de **termijn**, de **dagen
vertraging** en de **verschuldigde intrest**. De lotenlijst biedt de filter **OA
Payment Overdue** en een kolom **OA Pay Deadline** (rood indien verstreken).

!!! warning "De wettelijke rentevoet invullen"
    De berekening blijft op **0 zolang de wettelijke rentevoet niet ingevoerd
    is**. Vul de gepubliceerde **jaarlijkse wettelijke rentevoet** in bij
    **eHealth → Instellingen → Legal Interest Rate (%)** — zie
    [eHealth-instellingen](../configuration/reglages-ehealth.md). Dat is een
    waarde **eigen aan uw instelling / aan het lopende jaar**.

## Belangrijkste punten

- Het **ontvangstbewijs (931000)** betaalt niets; enkel de **afrekening
  (920900)** zegt wat effectief betaald wordt.
- Resthome **punt de afrekening automatisch af**: regels verdeeld, lotstatus
  bijgewerkt, reliquat aangemaakt voor de weigeringen.
- In **Rekening C** markeert een afrekening met echte betalingsreferentie het lot
  automatisch als **Betaald** (de betaaldatum kan leeg blijven).
- Een afrekening **afpunten** (**Mark Reconciled**) betekent het ontvangen geld
  bevestigen; de Cockpit bundelt de **af te punten** loten en de **aan te manen
  VI's**.
- **Nalatigheidsintresten** worden pas berekend nadat u de **wettelijke
  rentevoet** in de eHealth-instellingen hebt ingevuld.

## Meer weten

- [Elektronische facturatie (eFact)](efact.md)
- [eFact-weigeringen — oorzaken en oplossingen](efact-rejets.md)
- [Een maand factureren](../facturation/facturer-un-mois.md)
- [eHealth-instellingen](../configuration/reglages-ehealth.md)
- [eHealth-overzicht](index.md)