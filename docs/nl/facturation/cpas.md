---
title: De OCMW-tussenkomst
description: "OCMW-tussenkomst in een woonzorgcentrum (WZC/RVT): het besluit registreren, volledige of gedeeltelijke dekking, en de factuur van het bewonersaandeel routeren."
howto_auto: true
faq:
  - q: "Hoe geef ik aan dat een bewoner door het OCMW wordt ondersteund?"
    a: "Open op de bewonersfiche het tabblad Facturatie, vink « OCMW-ondersteund » aan, kies het verantwoordelijke OCMW en de dekking (volledig of gedeeltelijk). Deze velden registreren het OCMW-besluit en worden bijgehouden in het financiële auditspoor."
  - q: "Betaalt het OCMW alles of slechts een deel?"
    a: "Beide gevallen zijn voorzien. « Volledige dekking »: het OCMW neemt het volledige bewonersaandeel ten laste. « Gedeeltelijke dekking »: het OCMW betaalt een deel en u voert het « OCMW-maandbedrag » in; de rest is ten laste van de bewoner of zijn familie."
  - q: "Stuurt het aanvinken van « OCMW-ondersteund » de factuur automatisch naar het OCMW?"
    a: "Neen. De OCMW-sectie is een registratie van het besluit, geen verdeelmotor. Om het bewonersaandeel naar het OCMW te sturen vult u de « Contactpersoon voor facturering » van de bewoner in (het OCMW); voor een verdeling tussen het OCMW en een andere betaler gebruikt u de onderhoudsplichtigen (gedeelde facturatie)."
  - q: "Waar maak ik een OCMW aan in Resthome?"
    a: "In de app Facturatie → Configuratie → OCMW. Maak het contact (bedrijf) aan en vink « Is een OCMW » aan. Alleen zo gemarkeerde contacten verschijnen in het OCMW-veld van de bewonersfiche."
  - q: "Heeft de OCMW-tussenkomst invloed op het afhankelijkheidsforfait?"
    a: "Neen. Het afhankelijkheidsforfait gaat via eFact naar het ziekenfonds (derdebetaler). De OCMW-tussenkomst betreft uitsluitend het bewonersaandeel: het verblijf (de kamer) en de supplementen."
  - q: "Is het OCMW-maandbedrag voor elke bewoner hetzelfde?"
    a: "Neen. Het bedrag hangt af van het OCMW-besluit voor die bewoner: het is een waarde eigen aan elk dossier, in te voeren op basis van de ontvangen OCMW-kennisgeving."
---

# De OCMW-tussenkomst

Wanneer een bewoner zijn **persoonlijk aandeel** (verblijf en supplementen) niet kan
betalen, kan het **OCMW** (Openbaar Centrum voor Maatschappelijk Welzijn) van zijn
gemeente dit **ten laste nemen**, geheel of gedeeltelijk. Met Resthome kunt u dat
**besluit registreren** op de bewonersfiche en de **factuur routeren** naar de juiste
debiteur.

U vindt deze instellingen op het tabblad **Facturatie** van de bewonersfiche, en de
lijst met OCMW's onder **Facturatie → Configuratie → OCMW**.

!!! note "Wat het OCMW dekt"
    Het OCMW komt tussen in het **bewonersaandeel** (kamer + supplementen), niet in het
    **afhankelijkheidsforfait**: dat wordt voor 100 % gedragen door het ziekenfonds en
    gefactureerd via [eFact](../ehealth/efact.md). Zie
    [Het RIZIV-forfait (afhankelijkheid)](forfait-inami.md).

## Waarvoor dient de OCMW-tussenkomst

Er zijn twee zaken te onderscheiden:

- **Het besluit registreren** — wie het OCMW is, vanaf wanneer, onder welke referentie,
  voor welke dekking en welk bedrag. Deze gegevens documenteren het dossier en worden
  **bijgehouden in het auditspoor** (financiële categorie).
- **De factuur routeren** — beslissen **naar wie** Resthome het bewonersaandeel stuurt:
  naar de bewoner, zijn familie of het OCMW. Deze routering stuurt u via de
  **Contactpersoon voor facturering** of de **onderhoudsplichtigen** (zie verder).

<!-- capture toe te voegen: tabblad Facturatie van een bewoner met de groepen « Standaard betaler » en « OCMW-ondersteuning » -->

## 1. Het OCMW als organisatie aanmaken

Voordat u een bewoner aan een OCMW koppelt, moet het OCMW als contact bestaan.

1. Open **Facturatie → Configuratie → OCMW**.
2. Klik op **Nieuw** en voer de **naam** van het OCMW in, samen met stad, telefoon en
   e-mail.
3. Controleer of het vakje **« Is een OCMW »** is aangevinkt (dat is standaard zo vanuit
   dit menu).
4. **Bewaar.**

!!! tip "Waarom « Is een OCMW » aanvinken"
    Het veld **OCMW** op de bewonersfiche toont enkel contacten die als **« Is een
    OCMW »** zijn gemarkeerd. Een OCMW dat elders is aangemaakt (bij de gewone
    contacten) verschijnt pas in de lijst als dit vakje op zijn fiche is aangevinkt.

## 2. De tussenkomst op de bewoner invullen

1. Open de **bewonersfiche** en het tabblad **Facturatie**.
2. Vink in de groep **OCMW-ondersteuning** het vakje **OCMW-ondersteund** aan.
3. Selecteer het verantwoordelijke **OCMW**.
4. Kies de **OCMW-dekking**: *Volledige dekking* of *Gedeeltelijke dekking*.
5. Voer bij gedeeltelijke dekking het **OCMW-maandbedrag** in.
6. Vul het **OCMW-besluit** aan: datum, referentie en eventueel **OCMW-notities**.

| Veld | Rol |
|---|---|
| **OCMW-ondersteund** | Activeert de tussenkomst en zet de **Standaard betaler** op OCMW |
| **OCMW** | De verantwoordelijke organisatie (lijst gefilterd op « Is een OCMW ») |
| **OCMW-dekking** | *Volledig* (OCMW betaalt alles) of *Gedeeltelijk* (OCMW betaalt een deel) |
| **Datum OCMW-besluit** | Datum van het toekenningsbesluit |
| **Referentie OCMW-besluit** | Nummer / referentie van het ontvangen besluit |
| **OCMW-maandbedrag** | Bedrag dat het OCMW betaalt — **enkel bij gedeeltelijke dekking** |
| **OCMW-notities** | Vrije tekst (voorwaarden, contact, opmerkingen) |

!!! info "Velden die stapsgewijs verschijnen"
    Het OCMW, de dekking en het blok **OCMW-besluit** verschijnen pas nadat
    **« OCMW-ondersteund »** is aangevinkt. Het **OCMW-maandbedrag** verschijnt enkel bij
    **gedeeltelijke** dekking.

## 3. De factuur naar het OCMW routeren

Dit is de stap die bepaalt **naar wie** de factuur van het bewonersaandeel gaat.

- **Het OCMW betaalt alles** → vul de **Contactpersoon voor facturering** van de
  bewoner in (in de groep *Standaard betaler*) met het contact van het **OCMW**. De
  maandelijkse factuur van het bewonersaandeel wordt dan **naar het OCMW gestuurd**.
- **Het OCMW betaalt een deel** → gebruik de
  [onderhoudsplichtigen (gedeelde facturatie)](split-billing.md): voeg het OCMW toe als
  debiteur met zijn **percentage**, en de overige betalers (bewoner, familie) voor het
  saldo.

!!! warning "De sectie « OCMW-ondersteuning » is een registratie, geen verdeelmotor"
    De velden in de sectie **OCMW-ondersteuning** documenteren het besluit en zetten de
    **Standaard betaler** op OCMW, maar **ze routeren of splitsen de factuur niet
    automatisch**. De bestemmeling van de factuur blijft bepaald door de
    **Contactpersoon voor facturering** van de bewoner (of het factuurcontact van het
    verblijf), en de gedeeltelijke verdeling door de **gedeelde facturatie**. Zonder een
    van deze twee hefbomen blijft het bewonersaandeel naar **de bewoner** gaan.

## Wat Resthome wel — en niet — doet

| Actie | Automatisch? |
|---|---|
| Het OCMW-besluit bijhouden (financiële audit) | Ja, meteen bij invoer |
| De **Standaard betaler** op OCMW zetten bij het aanvinken van « OCMW-ondersteund » | Ja |
| De factuur naar het OCMW sturen | Neen — via de **Contactpersoon voor facturering** |
| Het bewonersaandeel verdelen tussen OCMW en familie | Neen — via de [gedeelde facturatie](split-billing.md) |
| Het **OCMW-maandbedrag** aftrekken van de gefactureerde bedragen | Neen — documentair veld |

## Kernpunten om te onthouden

- De OCMW-tussenkomst betreft het **bewonersaandeel** (kamer + supplementen), niet het
  **afhankelijkheidsforfait** (ziekenfondsaandeel, via eFact).
- Maak het OCMW eerst aan in **Facturatie → Configuratie → OCMW** (vakje **« Is een
  OCMW »**), koppel het daarna aan de bewoner op het tabblad **Facturatie**.
- De dekking is **volledig** of **gedeeltelijk**; het **OCMW-maandbedrag** geldt enkel
  bij gedeeltelijke dekking.
- De sectie **OCMW-ondersteuning** **registreert** het besluit; om de factuur te
  **routeren** gebruikt u de **Contactpersoon voor facturering** (volledige dekking) of
  de **gedeelde facturatie** (gedeeltelijke dekking).
- Het **OCMW-maandbedrag** en de besluitreferentie zijn **eigen aan elk dossier**,
  volgens de OCMW-kennisgeving.

## Meer weten

- [Een bewoner beheren](../residents/gerer-un-resident.md)
- [Een maand factureren](facturer-un-mois.md)
- [Onderhoudsplichtigen (gedeelde facturatie)](split-billing.md)
- [Het RIZIV-forfait (afhankelijkheid)](forfait-inami.md)