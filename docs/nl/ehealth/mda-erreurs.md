---
title: MDA-fouten — oorzaken en oplossingen
description: "MDA-fouten en bijzondere gevallen (verzekerbaarheid) oplossen in Resthome: verkeerd INSZ, onbekende rechthebbende, « niet in orde », zonder antwoord, mutatie, bijzondere stelsels."
faq:
  - q: "Wat te doen wanneer de MDA een fout teruggeeft?"
    a: "Afhankelijk van het bericht: is het INSZ de oorzaak (het vaakst), corrigeer het op de fiche en probeer opnieuw; is het « zonder antwoord » (vaak buiten de openingsuren), probeer later opnieuw; is de fout technisch of blijft ze aanhouden, meld ze aan de intermutualist."
  - q: "Wat betekent « verzekerd maar niet in orde »?"
    a: "De bewoner is aangesloten maar zijn dekking is niet geldig voor de periode (onbetaalde bijdragen, te regulariseren dossier). Factureer de verzekeringsinstelling niet: klaar dit uit met de bewoner of zijn ziekenfonds, en factureer het aandeel ondertussen aan de bewoner."
  - q: "De MDA heeft de bewoner niet gevonden, waarom?"
    a: "Ofwel is het INSZ verkeerd ingevoerd (formaat geweigerd), ofwel is het correct maar nog niet gekend bij het platform (zeer recente inschrijving, bijzonder geval). Controleer het INSZ; is het juist, neem contact op met het ziekenfonds."
  - q: "Wat werkt Resthome bij na een geslaagde MDA?"
    a: "Het reële ziekenfonds (verzekeringsinstelling), het BIM-statuut, het aansluitingsnummer, de identiteit als er velden ontbraken, en de overlijdensdatum als de instelling die meldt. Voor een bijzonder stelsel wordt het ziekenfonds van het profiel niet overschreven."
---

# MDA-fouten — oorzaken en oplossingen

De [MDA](mda.md) bevraagt voor u het platform van de ziekenfondsen (MyCareNet /
WalCareNet) om te bevestigen dat een bewoner **verzekerd is voor de periode** en om
**het ziekenfonds dat hem werkelijk dekt** te identificeren. Het is de **voorwaarde voor
de eFact**. Deze pagina bundelt de fouten en bijzondere gevallen, met de te volgen weg.

!!! tip "De juiste reflex"
    Start de MDA **aan het begin van de maand, vóór u de facturen genereert**: zo
    vermijdt u latere [eFact-weigeringen](efact-rejets.md) door een verkeerd ziekenfonds
    of een te laat ontdekt verlies van verzekerbaarheid.

## MDA-situaties → actie

Herinnering aan de statussen die Resthome kan tonen: **Concept · Verzonden / In
afwachting · Succes · Niet verzekerd · Zonder antwoord · Fout**. Beschikbare acties:
**Verzenden · Antwoord controleren · Opnieuw proberen · Contact opnemen met de VI ·
Melden aan de intermut.**

| Situatie | Wat Resthome toont | Waarschijnlijke oorzaak | Actie |
|---|---|---|---|
| **INSZ niet herkend** | **Fout**: de aanvraag wordt geweigerd vóór ze een ziekenfonds bereikt | Het **INSZ** is verkeerd ingevoerd (omgekeerd cijfer, typfout): ongeldig formaat | Controleer het INSZ (identiteitskaart), **corrigeer het**, en **probeer opnieuw**. Dit is de vaakst voorkomende oorzaak. |
| **Rechthebbende onvindbaar** | **Fout**: « niet gevonden » | INSZ goed gevormd maar **(nog) niet gekend** bij het platform (zeer recente inschrijving, bijzonder geval) | Bevestig het INSZ en de aansluiting. Is het nummer correct: **Contact opnemen met de VI**; in laatste instantie **Melden aan de intermut.** |
| **Verzekerd maar « niet in orde »** | **Niet verzekerd** + **waarschuwing** | Bestaande aansluiting maar **niet-geldige dekking** (onbetaalde bijdragen, te regulariseren dossier) | Factureer de VI niet voor deze periode. **Contact opnemen met de VI** of de bewoner om te regulariseren; factureer het aandeel ondertussen **aan de bewoner**. |
| **Geen ziekenfonds op de fiche** | Niet blokkerend: na een geslaagde MDA wordt het ziekenfonds **automatisch ingevuld** | Onvolledig profiel (nieuwe bewoner) | Start de MDA: slaagt ze, dan **vult** Resthome het ziekenfonds en het aansluitingsnummer in. Zo niet, controleer het INSZ opnieuw. |
| **Verandering van ziekenfonds (mutatie)** | **Mutatie gedetecteerd**: het profiel wordt **bijgewerkt** | De bewoner is van ziekenfonds veranderd; het profiel was niet bijgewerkt | Laat Resthome het profiel corrigeren; **controleer** het nieuwe ziekenfonds vóór u factureert. |
| **« Zonder antwoord »** | **Zonder antwoord** | Het platform heeft de aanvraag zonder antwoord afgesloten — vaak **buiten de openingsuren** (avond/weekend) of tijdelijke onbeschikbaarheid. Dit is geen fout van u | **Probeer opnieuw** tijdens de openingsuren. Blijft dit aanhouden, **Melden aan de intermut.** |
| **Technische fout** | **Fout** + technisch detail | Tijdelijke panne bij het platform of het ziekenfonds | **Probeer later opnieuw**; blijft de fout terugkomen, **Melden aan de intermut.** Niet in een lus opnieuw starten. |
| **Overlijden gemeld door het ziekenfonds** | **Overlijdensdatum** op de fiche + waarschuwing | De VI meldt een overlijden (dekking afgesloten) | Controleer en **stop de facturatie** op de juiste datum. |
| **Bijzonder stelsel** | Het MDA-antwoord wordt **genegeerd**; het ziekenfonds van het profiel **blijft ongewijzigd** | De bewoner valt onder een bijzonder stelsel (zie verder) | Corrigeer niets: de beveiliging is **bewust**. Factureer volgens het bijzondere stelsel. |

## Bijzondere stelsels

Sommige bewoners vallen **niet** onder de standaard ziekenfondsstroom. In die gevallen
**overschrijft** Resthome het ziekenfonds van hun profiel niet met het MDA-antwoord, en
gebeurt de facturatie vaak **op papier**, gericht aan de werkelijke betaler (of aan de
bewoner), in plaats van via eFact.

- **BIM-statuut (verhoogde tegemoetkoming)** — dit is geen apart stelsel: de MDA
  **haalt het op en werkt het vanzelf bij**. Het geeft recht op een **verminderd
  remgeld** voor de bewoner (het aandeel te zijnen laste daalt); het dagforfait blijft
  ongewijzigd.
- **Oorlogsinvaliden / burgerlijke slachtoffers** — de bewoner heeft **twee dekkingen**:
  zijn standaard ziekenfonds (zichtbaar in de MDA) **en** een specifieke dekking die
  **niet** via de MDA verloopt. De beveiliging vermijdt dat deze configuratie
  overschreven wordt.
- **Gepensioneerden van internationale instellingen** — gedekt door een eigen stelsel
  van hun organisatie, niet door een klassiek Belgisch ziekenfonds.
- **Buitenlandse gepensioneerden** — dekking van een buitenlands stelsel via de Europese
  coördinatieformulieren; in de praktijk sluiten velen zich toch bij een Belgisch
  ziekenfonds aan.

!!! warning "Bij twijfel"
    Voor een bijzonder stelsel, bij twijfel over de te factureren instelling, neem
    contact op met het ziekenfonds of de betrokken instelling vóór u de factuur opmaakt.

## Goede praktijken

- **MDA aan het begin van de maand, vóór het factureren.**
- **Individuele controle** (onmiddellijk) voor een specifieke bewoner; **controle per
  lot** voor een volledige periode — plak indien nodig een kolom namen/INSZ.
    - **Onmiddellijke verzending (Sync)** voor **kleine volumes**;
    - **Groepsverzending (Async)** voor **grote maandelijkse loten**: de aanvraag
      vertrekt, daarna **haalt u de antwoorden** wat later op met **Antwoorden
      controleren** (vereist minstens 2 bewoners).
- Het lot toont **tellers** (Verzekerd, Niet verzekerd, Fouten, In afwachting,
  Overlijdens) om in één oogopslag te zien wat nog te behandelen valt.
- **Wat Resthome bijwerkt** na een geslaagde MDA: het reële **ziekenfonds (VI)**, het
  **BIM-statuut**, het **aansluitingsnummer**, de **identiteit** als er velden
  ontbraken, en de **overlijdensdatum** als de instelling die meldt. Uitzondering: het
  ziekenfonds van een **bijzonder stelsel** wordt niet overschreven.

## Verder

- [Verzekerbaarheid (MDA)](mda.md)
- [eFact-weigeringen](efact-rejets.md) · [Elektronische facturatie (eFact)](efact.md)
- [FAQ](../faq.md) · [Woordenlijst](../glossaire.md)
