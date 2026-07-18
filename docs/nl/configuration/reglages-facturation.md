---
title: Facturatie-instellingen (WZC/RVT)
description: "Het MR/MRS-instellingentabblad van Resthome configureren voor een woonzorgcentrum (WZC/RVT): automatische facturatie, dagboeken, Cc-erkenning, afwezigheden."
faq:
  - q: "Waar vind ik de MR/MRS-facturatie-instellingen?"
    a: "In Instellingen > MR/MRS. Het tabblad is enkel zichtbaar voor MR/MRS-beheerders. Het bundelt de automatische facturering, de dagboeken, de erkenning van de instelling, de gesplitste facturatie en het afwezigheidsbeheer."
  - q: "Moet ik de automatische facturatievernieuwing inschakelen?"
    a: "Ja, dat is de aanbevolen waarde. Ingeschakeld houdt ze elke open facturatieperiode bij zodra een gegeven wijzigt: supplement, afwezigheid, einde verblijf, kamer- of mutualiteitswijziging, opname in de loop van de maand. Schakel ze enkel uit als u pas wil herberekenen bij een klik op « Vernieuwen »."
  - q: "Wat is het verschil tussen het RIZIV-journaal en het bewonersdagboek?"
    a: "Het RIZIV-journaal ontvangt de facturen van het mutualiteitsaandeel (via de eFact verstuurd); het bewonersdagboek ontvangt die van het bewonersaandeel (huisvesting en supplementen). Het zijn twee verkoopdagboeken van uw instelling, bij voorkeur afzonderlijk voor een heldere boekhouding."
  - q: "Wanneer de Cc-erkenning aanvinken?"
    a: "Enkel als uw instelling de erkenning bezit om het comaforfait Ccoma te factureren. Zonder deze erkenning is een als Ccoma geklasseerde bewoner niet factureerbaar via de eFact; de huisvesting blijft wel gefactureerd. Het is een instellingseigen waarde."
  - q: "Installeert de gesplitste facturatie een module?"
    a: "Ja. « Gesplitste facturatie (onderhoudsplichtigen) » aanvinken installeert de bijbehorende module; uitvinken verwijdert ze. Schakel ze in als onderhoudsplichtigen het bewonersaandeel verdelen."
  - q: "Waarvoor dient de toegewezene van de Katz-activiteit?"
    a: "Het is de gebruiker aan wie Resthome de activiteit « Nieuwe Katz vereist » toewijst wanneer een heropname na hospitalisatie langer dan 30 dagen duurt. Is het veld leeg, dan gaat de activiteit naar de huidige gebruiker indien klinisch, anders naar de eerste hoofdverpleegkundige, verpleegkundige of arts."
---

# Facturatie-instellingen (WZC/RVT)

Het tabblad **MR/MRS** in de instellingen bundelt de parameters die de
**facturatie** van uw woonzorgcentrum sturen: het aanmaken van facturen, de
boekhoudkundige dagboeken, de erkenning van de instelling en het
afwezigheidsbeheer. U configureert ze **één keer** en ze wijzigen daarna nog
nauwelijks.

U vindt ze onder **Instellingen > MR/MRS**. Het tabblad is enkel zichtbaar voor
**MR/MRS-beheerders**.

!!! info "eHealth-geheimen worden elders geconfigureerd"
    Het **eHealth-certificaat (.p12)**, de **CIN-licentie** en de andere
    aanmeldgegevens voor de ziekenfondsen staan **niet** in dit tabblad, maar in de
    **[eHealth](../ehealth/index.md)**-configuratie. Dit tabblad bevat **geen enkel
    geheim gegeven**; u voert er geen wachtwoord of sleutel in.

## Automatische facturering

Dit blok bepaalt **hoe** en **wanneer** de facturen worden aangemaakt, en of de
open periodes zichzelf bijhouden.

| Instelling | Waarvoor het dient | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Automatische facturering** | Maakt automatisch de maandelijkse facturen van de verblijven aan, zonder de handmatige cyclus. Standaard uitgeschakeld. | Volgens uw organisatie; vaak **uitgeschakeld** gelaten ten voordele van de handmatige cyclus (genereren → factureren), die meer controle geeft. |
| **Factureringsdag** | Dag van de maand waarop de automatische facturen worden aangemaakt (enkel zichtbaar als de automatische facturering aanstaat). | **1** (begin van de maand) standaard; aan te passen aan uw organisatie. |
| **Automatische facturatievernieuwing** | Houdt elke open periode bij zodra een gegeven wijzigt: supplement, afwezigheid, einde verblijf, kamer- of mutualiteitswijziging, opname in de loop van de maand. | **Ingeschakeld** — aanbevolen. |

!!! tip "Automatische vernieuwing en de knop « Vernieuwen »"
    Met de vernieuwing **ingeschakeld** slaat een toegevoegd supplement of een
    afwezigheid vanzelf door naar de periode: u hoeft doorgaans niets te doen. De
    knop **« Vernieuwen »** op de periode blijft beschikbaar voor een volledige
    herberekening op aanvraag. Zie [Een maand factureren](../facturation/facturer-un-mois.md).

## Facturatiedagboeken

Resthome verstuurt **twee stromen** facturen: het **mutualiteitsaandeel**
(afhankelijkheidsforfait, via de eFact naar de verzekeringsinstelling) en het
**bewonersaandeel** (huisvesting en supplementen). Elke stroom vertrekt in zijn
eigen verkoopdagboek.

| Instelling | Waarvoor het dient | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **RIZIV-journaal** | Verkoopdagboek dat de facturen van het **mutualiteitsaandeel** ontvangt (afhankelijkheidsforfait via de eFact). | Een verkoopdagboek van uw instelling. |
| **Bewonersdagboek** | Verkoopdagboek dat de facturen van het **bewonersaandeel** ontvangt (huisvesting en supplementen). | Een **afzonderlijk** verkoopdagboek (aanbevolen). |

!!! warning "Instellingseigen waarde"
    Beide dagboeken hangen af van **uw rekeningstelsel**. Kies bestaande
    **verkoopdagboeken**. Ze scheiden (RIZIV enerzijds, bewoner anderzijds)
    vergemakkelijkt de aansluiting en de opvolging per betaler.

## Erkenning van de instelling

Sommige federale forfaits vereisen een **bijzondere erkenning** van de instelling.
Dat is het geval voor het **comaforfait (Ccoma)**.

| Instelling | Waarvoor het dient | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Cc-erkenning (comaforfait)** | Aanvinken als de instelling de erkenning bezit om het comaforfait **Ccoma** te factureren. Zonder deze is een als Ccoma geklasseerde bewoner **niet** factureerbaar via de eFact (noch regionaal, noch federaal); de huisvesting blijft gefactureerd. | Enkel aanvinken als uw instelling **erkend** is. |

!!! note "Niet verwarren met het forfaitbedrag"
    Het gewone **afhankelijkheidsforfait** is **hetzelfde bedrag** voor alle
    Katz-categorieën; de categorie dient om het **profiel** aan het ziekenfonds te
    melden, niet om het bedrag te bepalen (zie
    [Het RIZIV-forfait](../facturation/forfait-inami.md)). De Cc-erkenning betreft
    enkel het **bijzondere geval van het comaforfait**.

## Optionele functies

Een aanvullende module wordt rechtstreeks vanuit de instellingen geïnstalleerd,
door een vakje aan te vinken.

| Instelling | Waarvoor het dient | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Gesplitste facturatie (onderhoudsplichtigen)** | Verdeelt het bewonersaandeel van de maandfactuur over meerdere betalers, elk met een percentage. Deze optie aanvinken **installeert** de module. | Inschakelen **als** onderhoudsplichtigen het bewonersaandeel verdelen. |

!!! tip "Wat het vakje doet"
    Aanvinken installeert de module en uitvinken verwijdert ze (Odoo-conventie).
    Eenmaal ingeschakeld stelt u de verdeling per bewoner in. Zie
    [Onderhoudsplichtigen](../facturation/split-billing.md).

## Afwezigheidsbeheer

De regels voor **aanwezigheidsdagen** (middagregel, hospitalisatie, verlof) zijn
in Resthome **ingebouwd** en worden hier niet ingesteld. Enkel de **toegewezene**
van een opvolgingsactiviteit is configureerbaar.

| Instelling | Waarvoor het dient | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Toegewezene Katz-activiteit** | Gebruiker aan wie de activiteit « Nieuwe Katz vereist » wordt toegewezen wanneer een heropname na hospitalisatie **30 dagen** overschrijdt. Leeg: huidige gebruiker (indien klinisch), anders eerste hoofdverpleegkundige, verpleegkundige of arts. | De **hoofdverpleegkundige** (of de zorgverantwoordelijke). |

!!! note "Waarom 30 dagen?"
    Een heropname na meer dan 30 dagen hospitalisatie vereist een **nieuwe
    Katz-evaluatie**. De toegewezen activiteit dient als herinnering. Zie
    [Afwezigheden en hospitalisaties](../facturation/absences.md).

## Verder

- [Configuratie](index.md) — kamers, tarieven, ziekenfondsen, instelling.
- [Facturatie-overzicht](../facturation/index.md)
- [Een maand factureren, stap voor stap](../facturation/facturer-un-mois.md)
- [Het RIZIV-forfait (afhankelijkheid)](../facturation/forfait-inami.md)
- [Onderhoudsplichtigen](../facturation/split-billing.md)
- [Afwezigheden en hospitalisaties](../facturation/absences.md)
