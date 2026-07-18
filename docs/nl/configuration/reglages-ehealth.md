---
title: eHealth- en eFact-instellingen
description: "De eHealth- en eFact-instellingen van uw woonzorgcentrum (WZC/RVT) configureren: certificaat, platform, Waalse C-rekening, CIN-licentie en facturatiehoofding."
faq:
  - q: "Moet ik de omgeving Acceptance of Production kiezen?"
    a: "Blijf in Acceptance (testservers, geen echte gegevens) zolang uw verzendingen niet gevalideerd zijn door het CIN en de AViQ. Schakel pas over naar Production zodra de erkenning verkregen is: vanaf dan factureren de verzendingen echt aan de mutualiteiten."
  - q: "Waar verkrijg ik het eHealth-certificaat en de CIN-pakketlicentie?"
    a: "Het .p12-certificaat verkrijgt u op het eHealth-portaal (ehealth.fgov.be), na registratie van de instelling en aanduiding van de toegangsbeheerder. De pakketlicentie (gebruikersnaam en wachtwoord) wordt door het CIN/NIC afgeleverd bij de erkenning van de software. Deze gegevens staan nooit leesbaar in de documentatie."
  - q: "Moet ik de stub-modus uitschakelen?"
    a: "De stub-modus simuleert de eHealth-antwoorden om te testen zonder echte oproep. Laat hem ingeschakeld tijdens de testfase; schakel hem uit in productie, wat een geldig eHealth-certificaat en een geconfigureerde CIN-pakketlicentie vereist."
  - q: "Waarom een coördinerend arts invullen?"
    a: "Zijn NIHII-nummer dient als verantwoordelijke zorgverlener op de eAgreement-aanvragen wanneer de Katz-evaluator geen persoonlijk NIHII heeft. Hij is verplicht voor een Katz van categorie D, die een arts vereist."
  - q: "Is de C-rekening verplicht voor eFact in Wallonië?"
    a: "Ja. In een Waals WZC/RVT betaalt de verzekeringsinstelling de forfaits op de financiële C-rekening. Zonder ingevuld C-bankjournaal weigert WalCareNet het lot (104511 voor de ontbrekende IBAN, 105311 voor de ontbrekende BIC)."
  - q: "Welke waarde kies ik voor het Factuurtype (Z308)?"
    a: "Laat 01 (Hospitalisatie) als standaard: dat is de waarde die aanvaard wordt bij de voorafgaande controle 931000. Schakel pas over naar 03 (Ambulant) als het CIN of de AViQ dit bevestigt voor uw sector."
---

# eHealth- en eFact-instellingen

Dit scherm bundelt de **technische identificatiegegevens en keuzes** die Resthome
gebruikt om te communiceren met het Belgische e-gezondheidslandschap (eHealth,
MyCareNet, WalCareNet): verzekerbaarheid [MDA](../ehealth/mda.md), facturatie
[eFact](../ehealth/efact.md) en akkoorden [eAgreement](../ehealth/eagreement.md).

De instellingen zijn verdeeld over **twee tabbladen**:

- **Instellingen > Nursing Home**: het **eHealth**-gedeelte (certificaat,
  platform, automatisering, verantwoordelijke zorgverlener, CIN-licentie).
- **Instellingen > MR/MRS**: het **Waalse facturatiegedeelte** (C-rekening en
  eFact-hoofding).

De meeste waarden stelt u **eenmaal** in, bij de opstart, en wijzigen daarna nog
zelden.

!!! warning "Gevoelige velden — geen enkele waarde overneemt u uit documentatie"
    Het **.p12-certificaat**, de **CIN-pakketlicentie** en de **wachtwoorden** zijn
    geheimen die **eigen zijn aan uw instelling**. We leggen hier uit **waarvoor
    ze dienen** en **waar u ze verkrijgt** (eHealth-portaal, CIN/NIC), nooit hun
    inhoud. Deel ze niet en voer ze enkel in vanuit de officiële bron.

## eHealth-platform

**Instellingen > Nursing Home > eHealth Platform.** De basis: welke identiteit,
welke omgeving en welk platform Resthome voor alle uitwisselingen gebruikt.

| Instelling | Waarvoor het dient | Aanbevolen waarde (MR/MRS) |
|---|---|---|
| **Active Certificate** (actief certificaat) | Het eHealth-**.p12**-certificaat dat de instelling authenticeert en de SOAP-berichten ondertekent. Eerst importeren onder *eHealth / Certificates*, dan hier selecteren. | Het certificaat van **uw instelling**, verkregen op **ehealth.fgov.be**. Nooit een overgenomen waarde. |
| **Institution INAMI Number** (RIZIV-nr. instelling) | RIZIV/INAMI-nummer van uw instelling, gebruikt in de STS-, MDA-, eFact- en eAgreement-aanvragen. | **Uw nummer**: 8 cijfers (instelling) of 11 cijfers (NIHII-11). |
| **Competence Code** (competentiecode) | De laatste 3 cijfers van de NIHII-11 (enkel MR/MRS, geen CDV) ; terugval wanneer de gecertificeerde NIHII-11 niet uit het token leesbaar is. | **110** (MR) of **210** (sommige MRS). |
| **Legal Interest Rate (%)** (wettelijke interestvoet) | De jaarlijkse Belgische wettelijke voet om de nalatigheidsintresten te berekenen die een VI verschuldigd is op een laattijdig betaalde verzending. | De voor het jaar **gepubliceerde voet**; **0** schakelt de berekening uit. |
| **Care Provider NIHII** (NIHII zorgverlener) | Het **persoonlijke** NIHII-11 van de zorgverlener (verpleegkundige, arts) die de MDA-verzekerbaarheidsaanvragen uitgeeft — vereist door WalCareNet/MyCareNet. | Het NIHII van de **zorgverlener van uw instelling** (11 cijfers). |
| **Environment** (omgeving) | *Acceptance* = testservers (gesimuleerde gegevens); *Production* = echte servers (echte facturatie). | **Acceptance** zolang niet gevalideerd, daarna **Production** na erkenning. |
| **Default Platform** (standaardplatform) | Het beoogde netwerk: WalCareNet (AViQ, Wallonië), MyCareNet (federaal), IrisCareNet (Brussel, MDA). | **WalCareNet** voor een Waals WZC/RVT. |
| **Stub Mode (Development)** (stub-modus) | Simuleert de eHealth-antwoorden zonder echte oproep — om te testen. | **Ingeschakeld** in test; **uitgeschakeld** in productie (vereist geldig certificaat + CIN-licentie). |

!!! tip "Voorzichtig starten"
    Bij de opstart: **Acceptance + Stub Mode ingeschakeld**. U valideert het
    volledige traject zonder iets echts te versturen. Zodra de erkenning
    verkregen is, schakelt u **Stub Mode uit** en dan **Production** in.

## eHealth-automatisering

**Instellingen > Nursing Home > eHealth Automation.** De automatische gedragingen
rond verzekerbaarheid en logboeken.

| Instelling | Waarvoor het dient | Aanbevolen waarde (MR/MRS) |
|---|---|---|
| **Auto MDA Check** (auto MDA-controle vóór facturatie) | Controleert automatisch de verzekerbaarheid van elke bewoner vóór het genereren van de eFact — vermijdt weigeringen door ongeldige verzekerbaarheid (zie [MDA](../ehealth/mda.md)). | **Ingeschakeld** zodra MDA in productie is. |
| **Log Retention (days)** (logbewaring) | Aantal dagen dat de communicatie- en auditlogboeken bewaard blijven; de oudste worden door de maandelijkse cron gewist. | **2555** (7 jaar, Belgische wettelijke vereiste voor gezondheidsgegevens). |
| **No-Facet Report Email** (no-facet rapport-e-mail) | Adres gebruikt door de knop *Report to intermut* op een MDA-aanvraag die « no-facet » bleef (geen VI antwoordde binnen 24 u) — te escaleren naar het CIN/intermut. | Het **intermut**-adres als standaard laten. |

## Software-servicedesk

**Instellingen > Nursing Home > Software Service Desk.** Het **1e aanspreekpunt**
bij een probleem bij een zorgverlener — een AViQ-erkenningsvereiste.

| Instelling | Waarvoor het dient | Aanbevolen waarde (MR/MRS) |
|---|---|---|
| **Service Desk Contact** (servicedeskcontact) | Het contact van de software-uitgever (naam, e-mail, telefoon, logo), getoond door de knop *Contacteer LPLG* op de eAgreement-aanvragen. | Het **LPLG-contact** als standaard laten. |

## Verantwoordelijke zorgverlener eAgreement

**Instellingen > Nursing Home > eAgreement Responsible Practitioner.** Op een
[eAgreement](../ehealth/eagreement.md)-aanvraag is de verantwoordelijke
zorgverlener de clinicus die de Katz-evaluatie uitvoerde. Heeft die geen
persoonlijk NIHII, dan leent de aanvraag de identiteit van de hoofdverpleegkundige,
en vervolgens van de coördinerend arts.

| Instelling | Waarvoor het dient | Aanbevolen waarde (MR/MRS) |
|---|---|---|
| **Head Nurse (NIHII fallback)** (hoofdverpleegkundige) | Zijn NIHII identificeert de verantwoordelijke zorgverlener wanneer de Katz-evaluator (verpleegkundige, zorgkundige) geen NIHII heeft. | De **hoofdverpleegkundige** van de instelling invullen. |
| **Coordinating Physician (NIHII fallback)** (coördinerend arts) | Terugval wanneer geen verpleegkundig NIHII beschikbaar is, en **verplicht** voor een Katz van categorie D (arts vereist). | De **coördinerend arts** invullen — onmisbaar voor Katz D. |

!!! note "De Katz-categorie dient om te declareren, niet om het bedrag te bepalen"
    Het **afhankelijkheidsforfait** bedraagt **hetzelfde bedrag** voor alle
    Katz-categorieën (AViQ-tarieven); de categorie dient om het **profiel** van de
    bewoner aan de mutualiteit te **declareren**. Een categorie **D** vereist wel
    een **arts** als verantwoordelijke zorgverlener van de eAgreement — vandaar
    het belang van dit veld.

## CIN-pakketlicentie

**Instellingen > Nursing Home > CIN Package License.** De identificatiegegevens die
Resthome toelaten te versturen via GenAsync (eFact) en CommonInput (MDA).

| Instelling | Waarvoor het dient | Aanbevolen waarde (MR/MRS) |
|---|---|---|
| **Package License Username** (gebruikersnaam) | Gebruikersnaam van de softwarelicentie, vereist voor eFact en MDA. | Geleverd door het **CIN/NIC** bij de erkenning — eigen aan uw software. |
| **Package License Password** (wachtwoord) | Wachtwoord van de softwarelicentie (verborgen veld). | Geleverd door het **CIN/NIC**; **geheim**, deel het niet. |

!!! info "Waar verkrijgen"
    De pakketlicentie wordt door het **CIN/NIC** afgeleverd op het moment van de
    software-erkenning. Ze heeft **geen standaardwaarde**: zolang ze niet
    geconfigureerd is (en de stub-modus uitgeschakeld), blijven de echte
    verzendingen geblokkeerd.

## C-rekening (Wallonië)

**Instellingen > MR/MRS > Account C (Wallonia).** Sinds de 6e Staatshervorming
betaalt de verzekeringsinstelling de Waalse MR/MRS-forfaits op een aparte
**financiële C-rekening**, aangegeven bij het CIN tijdens de eFact-inschrijving.

| Instelling | Waarvoor het dient | Aanbevolen waarde (MR/MRS) |
|---|---|---|
| **Account C Bank Journal** (bankjournaal C-rekening) | Het bankjournaal van de Waalse rekening. De **IBAN** (ET 10 Z 45-47a) en de **BIC** (Z 53-54a) in de 920000 worden eruit afgeleid. | Het **journaal van de C-rekening** van uw instelling. Zet de IBAN op de bankrekening en de BIC op de bank. |

!!! warning "Anders: WalCareNet-weigering"
    Zonder geldige C-rekening **weigert** WalCareNet het lot:
    **104511** (ontbrekende IBAN) of **105311** (ontbrekende BIC). De IBAN en BIC
    onder het veld zijn alleen-lezen — ze komen van de bankrekening van het
    journaal. Zie [eFact-weigeringen](../ehealth/efact-rejets.md).

## eFact-hoofding

**Instellingen > MR/MRS > eFact Header.** De hoofdinggegevens die elk
[eFact](../ehealth/efact.md) 920000-bericht meedraagt (segment 300).

| Instelling | Waarvoor het dient | Aanbevolen waarde (MR/MRS) |
|---|---|---|
| **eFact Contact Person** (contactpersoon) | Naam en telefoon in de hoofding (Z305 naam / Z306 voornaam / Z307 telefoon) — de persoon die een VI bereikt voor een facturatievraag. | Bijv. de **directeur** van de instelling. Indien leeg, wordt de naam van de instelling gebruikt. |
| **eFact Invoice Type (Z308)** (factuurtype) | Zone Z308 « factuurtype »: 01 Hospitalisatie, 03 Ambulant, 09 Gemengd. | **01** als standaard (aanvaard bij controle 931000). Pas naar **03** als de AViQ/CIN dit bevestigt. |

## Meer informatie

- [Configuratie](index.md)
- [eHealth — overzicht](../ehealth/index.md)
- [Elektronische facturatie (eFact)](../ehealth/efact.md)
- [Verzekerbaarheid (MDA)](../ehealth/mda.md)
- [Akkoorden (eAgreement)](../ehealth/eagreement.md)
- [eFact-weigeringen — oorzaken en oplossingen](../ehealth/efact-rejets.md)