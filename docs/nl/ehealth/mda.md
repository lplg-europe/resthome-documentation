---
title: Verzekerbaarheid (MDA)
description: De verzekerbaarheid van een bewoner controleren in Resthome via MDA (MyCareNet/WalCareNet) — mutualiteit, BIM-status, dekkingsperiodes, individuele of bulkcontrole, statussen en foutbeheer.
---

# Verzekerbaarheid (MDA)

Vóór het factureren moet u zeker zijn dat de bewoner **in orde is qua
verzekerbaarheid** en zijn exacte **mutualiteit** kennen. De **MDA** bevraagt voor
u **MyCareNet / WalCareNet** en haalt de actuele informatie op voor een bepaalde
**periode**. Het is de onmisbare voorwaarde voor de [eFact](efact.md)-verzending.

Menu: **eHealth → Verzekerbaarheid → MDA-aanvragen** (en **MDA-loten**).

## Wat de MDA ophaalt

- **Verzekerd of niet** voor de periode.
- De **mutualiteit (VI)** die werkelijk antwoordde — te vergelijken met die van het
  profiel (een **verandering** van mutualiteit wordt gedetecteerd en gesignaleerd).
- De **BIM**-status (verhoogde tegemoetkoming).
- De **dekkingsperiodes** (begin-/einddata; meerdere deelperiodes als de
  verzekering tijdens het interval veranderde).
- Het **aansluitingsnummer** bij de mutualiteit.
- Indien van toepassing: **derdebetaler**, door de VI gemelde **overlijdensdatum**,
  en naargelang de aanvraag de **referentieapotheek**, het **GMD**, de
  **palliatieve status** of een **hospitalisatie**.

!!! warning "Het geval « niet in orde »"
    Komen de begunstigdencodes op nul terug (verzekerd maar onbetaalde bijdragen /
    probleemdossier), dan toont Resthome een **waarschuwing**: de bewoner is
    aangesloten maar **niet in orde**. Te verduidelijken met hem of zijn
    mutualiteit vóór u aan de VI factureert.

## Vereisten

!!! warning "Te controleren"
    - De bewoner heeft een geldig **NISS**.
    - Het **RIZIV-nummer** van de instelling is geconfigureerd.
    - Het **eHealth-certificaat** is actief.

    De **mutualiteit van het profiel** is niet blokkerend (de echte VI wordt door
    het antwoord geïdentificeerd), maar ze invullen helpt om veranderingen op te
    sporen.

Resthome past ook automatische perioderegels toe: het einde moet na het begin
liggen, hoogstens **5 jaar** geschiedenis, en een standaard-MDA gaat niet voorbij
de lopende maand.

## Individuele controle

1. Maak een **MDA-aanvraag** (bewoner, vooraf ingevuld NISS, periode = standaard de
   lopende maand).
2. Klik **Verzenden (Sync)**: de verzending is **onmiddellijk** en het antwoord
   komt meteen terug.
3. Raadpleeg de samenvatting en de verzekerbaarheidsperiodes.

!!! note "Eén MDA per bewoner en per periode"
    Een controle overdoen voor dezelfde bewoner en periode **hergebruikt** de
    bestaande aanvraag — geen dubbel.

## Bulkcontrole (aanbevolen bij het begin van de maand)

Start voor een hele periode de controle **in bulk**: selecteer de bewoners (u kunt
een **kolom** namen/NISS plakken), de periode, en verstuur het hele lot in één keer.

- **Onmiddellijke verzending (Sync)**: voor kleine volumes.
- **Gegroepeerde verzending (Async)**: voor de **grote maandelijkse loten** — de
  aanvraag vertrekt, en het antwoord haalt u iets later op met **Antwoorden
  controleren** (vereist minstens 2 bewoners).

Het lot toont **tellers**: Verzekerd, Niet verzekerd, Fouten, In afwachting, en
« Overlijdens gedetecteerd ».

!!! tip "Het goede reflex"
    Doe de MDA **bij het begin van de maand**, vóór het genereren van de facturen:
    zo vermijdt u latere eFact-weigeringen door een verkeerde mutualiteit of een
    verlies van verzekerbaarheid.

## De statussen

| Status | Betekenis |
|---|---|
| **Concept** | Nog niet verstuurd |
| **Verstuurd / In afwachting** | Doorgestuurd, antwoord verwacht (vooral bij bulk) |
| **Succes** | Antwoord ontvangen, bewoner verzekerd |
| **Niet verzekerd** | Antwoord OK, maar bewoner niet gedekt |
| **Zonder antwoord** | Het platform sloot af zonder antwoord van een VI (opnieuw proberen) |
| **Fout** | De VI of het platform gaf een fout terug |

## De knoppen

| Knop | Effect |
|---|---|
| **Verzenden (Sync)** | Onmiddellijke verzending, meteen antwoord |
| **Antwoord controleren** | Haalt een antwoord van een gegroepeerde verzending op |
| **Opnieuw proberen** | Zet terug naar concept om te herverzenden |
| **VI contacteren** | Opent een vooraf ingevulde e-mail naar de mutualiteit die antwoordde |
| **Melden aan intermut.** | Opent een e-mail naar het CIN voor platformblokkeringen |

Op een lot bestaan dezelfde acties in gegroepeerde versie (**Verzenden**,
**Antwoorden controleren**, **Fouten opnieuw proberen**, **Zonder-antwoord opnieuw
proberen**).

## Wat Resthome automatisch bijwerkt

Na een geslaagd antwoord wordt de bewonersfiche **automatisch gecorrigeerd**:

- **Mutualiteit (VI)**: verschilt de antwoordende VI van het profiel, dan wordt het
  profiel bijgewerkt (en de VI aangemaakt als ze ontbrak).
- **BIM-status**, **aansluitingsnummer** en **identiteit** (naam, geboortedatum,
  geslacht) als velden ontbraken.
- **Overlijdensdatum** als de VI ze meldt → waarschuwing op de fiche.

!!! warning "Vangnet bijzondere regimes"
    Voor bewoners onder een **bijzonder regime** (INIG, EEG, Fedasil, buitenland,
    privé…) **overschrijft** Resthome de mutualiteit van het profiel niet: een
    bericht legt uit dat het MDA-antwoord genegeerd werd om een niet-standaard
    dekking niet te breken.

## Herintegratie (verlies en daarna terugkeer van verzekerbaarheid)

Resthome vergelijkt met de vorige controle:

- **Niet verzekerd → verzekerd**: een melding verschijnt op de periode, en de actie
  **Herintegratie** laat toe de regels die aan de bewoner werden gefactureerd naar
  de VI over te hevelen.
- **Verzekerd → niet verzekerd**: Resthome signaleert dat de bewoner « niet meer in
  orde » is — zijn forfait wordt uit de VI-facturatie van de periode gehaald en aan
  de bewoner gefactureerd tot herstel.

## Foutbeheer

| Situatie | Wat te doen |
|---|---|
| **Zonder antwoord** (platform) | **Zonder-antwoord opnieuw proberen**; blijft het duren, **Melden aan intermut.** |
| **Weigering van de VI** | **VI contacteren** (reden getoond) |
| **Technische fout** | **Melden aan intermut.** |
| **Bewoner zonder mutualiteit** | Niet blokkerend: de echte VI komt uit het antwoord |
| **In afwachting (bulk)** | **Antwoorden controleren** of wachten |

## Verder

- [MDA-fouten — oorzaken en oplossingen](mda-erreurs.md)
- [Elektronische facturatie (eFact)](efact.md)
- [Akkoorden (eAgreement)](eagreement.md)
- [Facturatie-overzicht](../facturation/index.md)
