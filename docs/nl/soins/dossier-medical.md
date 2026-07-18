---
title: Het medisch dossier van de bewoner
description: "Het medisch dossier van de bewoner in een woonzorgcentrum (WZC/RVT) met Resthome: metingen, klinische status, pathologieën ICD-10, allergieën, hulpmiddelen, wilsverklaringen."
faq:
  - q: "Waar vind ik het medisch dossier van een bewoner in Resthome?"
    a: "Open op de fiche van de bewoner het tabblad Medische informatie. Het bundelt de metingen, de klinische status, de zintuigen en risico's, de hulpmiddelen, de diagnoses (ICD-10), de allergieën, de medische contacten en de wilsverklaringen. Het tabblad is alleen zichtbaar voor bewoners en voorbehouden aan het zorgpersoneel."
  - q: "Hoe voer ik het gewicht van een bewoner in?"
    a: "Het gewicht is alleen-lezen in het dossier: het komt uit de invoer van de vitale functies. Gebruik de knop Vitale functies invoeren (boven de fiche) of het kleine + naast het veld Gewicht. De BMI wordt daarna automatisch berekend uit de lengte en het gewicht."
  - q: "Hoe registreer ik een pathologie of diagnose?"
    a: "Voeg in de sectie Diagnoses / Pathologieën een regel toe, kies de pathologie uit de ICD-10-catalogus en stel de ernst en de status (Actief of Opgelost) in voor deze bewoner. Eenzelfde pathologie kan maar één keer per bewoner worden geregistreerd."
  - q: "Blokkeren allergieën echt een voorschrift?"
    a: "Ja voor geneesmiddelenallergenen. Een allergie met ernst Kritiek blokkeert het voorschrift van het betrokken geneesmiddel; een ernst Hoog, Middel of Laag toont een waarschuwing. Voedings- en omgevingsallergieën zijn documentair."
  - q: "Hoe signaleer ik een niet-reanimeren (DNR)?"
    a: "Vink in de sectie Wilsverklaring het vakje DNR-code (Niet reanimeren) aan. Bovenaan de fiche van de bewoner verschijnt dan een oranje waarschuwingsbanner, een DNR-badge op de kanbankaart en in de lijst, en een DNR-filter laat toe de betrokken bewoners terug te vinden."
  - q: "Wie kan het medisch dossier zien?"
    a: "De toegang is voorbehouden aan het zorgpersoneel (medische groep). Wijzigingen aan de medische gegevens worden gelogd met het oog op traceerbaarheid en GDPR-conformiteit."
---

# Het medisch dossier van de bewoner

Het tabblad **Medische informatie** op de bewonersfiche vormt zijn **medisch
dossier** in Resthome. Het bundelt op één pagina de **metingen**, de **klinische
status**, de **zintuigen en risico's**, de **hulpmiddelen**, de **diagnoses
(ICD-10)**, de **allergieën**, de **medische contacten** en de
**wilsverklaringen**.

U vindt het op de **bewonersfiche** (toepassing **Bewoners** of **Zorg**), in het
tabblad **Medische informatie**. Het tabblad verschijnt enkel voor **bewoners**.

!!! warning "Voorbehouden aan het zorgpersoneel"
    Het tabblad **Medische informatie** en de eruit voortvloeiende indicatoren
    (DNR-badge, filters) zijn enkel zichtbaar voor het **zorgpersoneel**.
    Wijzigingen aan de medische gegevens worden **gelogd** (traceerbaarheid en
    **GDPR**-conformiteit).

Boven het tabblad opent een reeks **statistiekknoppen** de andere luiken van de
opvolging: **Voorschriften**, **Zorgplannen**, **Notities**, **Katz**, **Vitale
functies** en **Trends**. Het medisch dossier dat hieronder wordt beschreven,
bundelt het **klinische profiel** van de bewoner.

## Metingen en BMI

De sectie **Metingen** verzamelt de morfologische basisgegevens:

| Veld | Rol |
|---|---|
| **Bloedgroep** | Bloedgroep van de bewoner |
| **Hoogte (cm)** | Lengte, één keer ingevoerd |
| **Gewicht (kg)** | Alleen-lezen — komt uit de vitale functies |
| **BMI** | Automatisch berekend (gewicht / lengte²) |

!!! tip "Het gewicht loopt via de vitale functies"
    Het veld **Gewicht** wordt hier niet rechtstreeks ingevoerd: het neemt de
    laatste waarde over uit een **invoer van vitale functies**. Gebruik de knop
    **Vitale functies invoeren** boven de fiche, of het kleine **+** naast het veld
    Gewicht. De **BMI** wordt dan vanzelf herberekend zodra lengte en gewicht
    gekend zijn.

## De afhankelijkheid (Katz)

De sectie **Afhankelijkheid** toont, ter lezing, de synthese van de
afhankelijkheid van de bewoner:

- de lopende **Katz-categorie** (O, A, B, C, Cd);
- het **einde van de geldigheid** van de Katz-evaluatie;
- het **actieve zorgplan**, als er een is.

Deze gegevens komen uit de **Katz-evaluatie** en het **zorgplan**; u wijzigt ze
niet vanuit het medisch dossier.

!!! info "De Katz-categorie meldt, ze bepaalt het bedrag niet"
    De categorie dient om het **afhankelijkheidsprofiel** aan de mutualiteit te
    **melden**. In de **AViQ**-tarieven is het afhankelijkheidsforfait **hetzelfde
    bedrag voor alle categorieën** (zie [De Katz-evaluatie](../residents/katz.md)).

## De klinische status

De sectie **Klinische status** beschrijft de functionele zelfstandigheid van de
bewoner. Elk veld biedt een keuzelijst:

| Veld | Waarden |
|---|---|
| **Mobiliteit** | Zelfstandig · Stok · Looprek · Rolstoel · Bedlegerig |
| **Continentie** | Continent · Occasionele incontinentie · Frequente incontinentie · Incontinent |
| **Cognitieve status** | Normaal · Lichte stoornis · Matige stoornis · Ernstige stoornis |
| **Communicatie** | Normaal · Moeilijkheid · Non-verbaal · Afasie |

<!-- schermafbeelding toe te voegen: tabblad Medische informatie, secties Metingen, Afhankelijkheid en Klinische status -->

## De zintuigen en de risico's

De sectie **Zintuigen & risicobeoordeling** vervolledigt het profiel:

| Veld | Waarden |
|---|---|
| **Visie** | Normaal · Gecorrigeerd (bril) · Verminderd · Blind |
| **Gehoor** | Normaal · Hoorapparaat · Verminderd · Doof |
| **Valrisico** | Ja / Nee |
| **Doorligwonden risico** | Laag · Matig · Hoog |

Deze indicatoren sturen de dagelijkse opvolging en voeden het zorgplan.

## De medische hulpmiddelen

De sectie **Medische apparaten** somt de hulpmiddelen en permanente condities op:

- **Urine katheter** (ja / nee);
- **Stoma** (ja / nee);
- **Tandheelkundige status**: Natuurlijke tanden · Gedeeltelijke prothese ·
  Volledige prothese · Tandeloos.

## De diagnoses (pathologieën ICD-10)

De sectie **Diagnoses / Pathologieën** lijst de pathologieën van de bewoner op,
gecodeerd volgens de **ICD-10** (internationale classificatie van ziekten). Elke
regel koppelt de bewoner aan een pathologie uit de **catalogus**.

| Kolom | Rol |
|---|---|
| **Pathologie** | De pathologie uit de catalogus (ICD-10-code) |
| **Categorie** | Overgenomen uit de catalogus (circulatoir, zenuwstelsel, endocrien…) |
| **Ernst** | Licht · Matig · Ernstig — eigen aan deze bewoner |
| **Status** | **Actief** of **Opgelost** |
| **Bevestigd** | Klinisch bevestigde diagnose (ja / nee) |
| **Datum** | Datum van de diagnose |
| **Notities** | Klinische observaties |

!!! note "Ernst en status eigen aan de bewoner"
    De catalogus draagt een **standaard** ernst, maar u legt de ernst en de status
    (Actief / Opgelost) vast **voor deze bewoner**. Een status *Opgelost* vereist
    een **datum van oplossing**. Eenzelfde pathologie kan maar **één keer** per
    bewoner worden geregistreerd.

<!-- schermafbeelding toe te voegen: lijst van diagnoses met categorie, ernst als badge en status Actief/Opgelost -->

## De allergieën

De sectie **Allergieën** somt de allergieën **eigen aan de bewoner** op, gekoppeld
aan de **allergenencatalogus**.

| Kolom | Rol |
|---|---|
| **Allergeen** | Het allergeen uit de catalogus |
| **Categorie** | Geneesmiddel · Voeding · Omgeving · Contact · Insect/Gif |
| **Ernst** | Laag · Middel · Hoog · **Kritiek** — eigen aan deze bewoner |
| **Bevestigd** | Klinisch bevestigde allergie (ja / nee) |
| **Datum** | Datum van vaststelling |
| **Reactie** | Beschrijving van de reactie |

!!! warning "Geneesmiddelenallergenen beschermen het voorschrift"
    Voor een **geneesmiddelenallergeen** stuurt de ernst het gedrag bij het
    voorschrijven: **Kritiek** **blokkeert** het voorschrift van het betrokken
    geneesmiddel; **Hoog**, **Middel** of **Laag** toont een **waarschuwing**.
    **Voedings**- en **omgevingsallergieën** zijn documentair. Zie
    [Voorschriften en geneesmiddelen](prescriptions.md).

Een veld **Aanvullende allergienotities** laat toe in vrije tekst de allergieën of
opmerkingen te noteren die niet in de gestructureerde lijst staan.

## De medische contacten

De sectie **Medische contacten** koppelt de bewoner aan zijn zorgverleners:

- **Specialisten** — één of meerdere artsen (labels);
- referentie**apotheek**.

De **behandelend arts** (vaste arts van de bewoner) wordt ingevuld op de algemene
informatie van de bewoner. Deze contacten worden elders in Resthome hergebruikt
(voorschriften, eHealth-uitwisselingen).

## De wilsverklaringen en de DNR

De sectie **Wilsverklaring** legt de wensen van de bewoner vast:

- **Wilsverklaring** (ja / nee) — wanneer aangevinkt, verschijnt een veld
  **inhoud** om ze te beschrijven;
- **DNR-code (Niet reanimeren)** — beslissing tot niet-reanimeren.

!!! warning "De DNR wordt overal in Resthome gesignaleerd"
    Zodra **DNR-code (Niet reanimeren)** is aangevinkt, maakt Resthome ze zichtbaar
    voor het zorgpersoneel:

    - een **oranje banner** « DNR — Niet reanimeren » bovenaan de bewonersfiche;
    - een **DNR-badge** op de **kanban**kaart en in de **lijst** van bewoners;
    - een **DNR-filter** in de zoekopdracht, om de betrokken bewoners terug te
      vinden.

<!-- schermafbeelding toe te voegen: bewonersfiche met de oranje DNR-banner en de sectie Wilsverklaring -->

## Medische notities

Ten slotte laat een veld **Medische notities** in vrije tekst toe elke belangrijke
informatie te noteren die niet in de gestructureerde rubrieken past.

## Kernpunten om te onthouden

- Het medisch dossier is het tabblad **Medische informatie** op de bewonersfiche;
  het is **voorbehouden aan het zorgpersoneel** en wordt **gelogd** (GDPR).
- Het **gewicht** komt uit de **vitale functies** (alleen-lezen) en de **BMI** wordt
  automatisch berekend uit lengte en gewicht.
- De **Katz-categorie** en het **actieve zorgplan** worden er ter lezing getoond; de
  categorie **meldt** het profiel, ze bepaalt het forfaitbedrag niet.
- De **diagnoses** gebruiken de **ICD-10**; **ernst** en **status** (Actief /
  Opgelost) zijn eigen aan de bewoner.
- De **geneesmiddelenallergenen** beschermen het voorschrift: **Kritiek** blokkeert,
  de andere waarschuwen.
- De **DNR** activeert een **banner**, een **kanban-/lijstbadge** en een
  **zoekfilter**.

## Verder

- [Voorschriften en geneesmiddelen](prescriptions.md) — allergieën en interacties bij het voorschrijven.
- [Zorgplannen en vitale parameters](plans-de-soins.md)
- [Klinische registers](registres.md)
- [De Katz-evaluatie](../residents/katz.md) — van afhankelijkheid tot categorie.
