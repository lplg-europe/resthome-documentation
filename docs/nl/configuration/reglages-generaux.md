---
title: Algemene instellingen (bewoners, kamers)
description: "De algemene instellingen van een woonzorgcentrum (WZC/RVT) in Resthome configureren: bewoners, huisvesting, verantwoordelijke kamers en intrekprocedure."
faq:
  - q: "Waar vind ik de algemene instellingen?"
    a: "In Instellingen > Rusthuis (bewoners, huisvesting, demogegevens) en in Instellingen > Medisch (dashboard). Deze schermen zijn voorbehouden aan de beheerders van de instelling."
  - q: "Waarvoor dient de « Technisch verantwoordelijke kamers »?"
    a: "Dat is de gebruiker die de activiteit « kamer voorbereiden » krijgt telkens een bewoner aankomt, of wanneer een kamerwissel of overdracht een nieuw verblijf opent. Dit is een keuze eigen aan uw instelling."
  - q: "Waarvoor dient de « Verantwoordelijke intrekprocedure »?"
    a: "Dat is de gebruiker die de intrekchecklist (overeenkomst, plaatsbeschrijving, inventaris, medicatiekast, linnen, ontsmetting) op de fiche van de bewoner krijgt wanneer een verblijf opent. Leeg gelaten, is de procedure uitgeschakeld."
  - q: "Welke standaardwaarden voor verblijfsduur en kamercapaciteit?"
    a: "30 dagen voor de verblijfsduur en 1 bed voor de capaciteit passen bij de meeste ROB/RVT. Het zijn slechts voorinvulwaarden, nadien aanpasbaar op elk verblijf of elke kamer."
  - q: "Moet ik de demogegevens in productie laden?"
    a: "Nee. De knop « Demogegevens laden » maakt fictieve bewoners, kamers en facturen aan: houd ze voor een testomgeving. Gebruik ze nooit op uw echte database."
  - q: "Wat doet « Hide Empty Stat Cards »?"
    a: "Standaard uitgeschakeld houdt deze instelling alle dashboardkaarten zichtbaar, ook wanneer hun teller op 0 staat. Schakel ze enkel in als u een opgeruimder scherm verkiest."
---

# Algemene instellingen (bewoners, kamers)

Dit tabblad bundelt de instellingen die het dagelijkse leven van uw huis
structureren: hoe de **bewoners** beheerd worden, de **huisvesting**
(verblijfsduur, capaciteit, verantwoordelijken) en de weergave van het
**zorgdashboard**.

U vindt ze in de toepassing **Instellingen**:

- **Instellingen > Rusthuis (MR/MRS)** — bewoners, huisvesting, demogegevens;
- **Instellingen > Medisch** — dashboard.

!!! info "Voorbehouden aan beheerders"
    Deze instellingen zijn enkel zichtbaar voor gebruikers met de rol
    **beheerder** van de instelling. Ze worden één keer ingesteld en evolueren
    daarna nog nauwelijks.

## Bewoners

*Instellingen > Rusthuis > Bewoners.* Twee opties omkaderen het aanmaken en
opvolgen van de bewoners.

| Instelling | Waarvoor | Aanbevolen waarde (ROB/RVT) |
|---|---|---|
| **Medische gegevens vereist** | Maakt de medische gegevens verplicht voor alle bewoners. | Eigen aan de instelling — schakel in als de hoofdverpleegkundige een volledig medisch dossier eist vanaf de opname. |
| **Familie verwittigen** | Stuurt automatische meldingen naar de familie van de bewoner. | Eigen aan de instelling — schakel in als u vanuit Resthome met de families communiceert. |

## Huisvesting

*Instellingen > Rusthuis > Huisvesting.* Dit blok legt de standaardwaarden van
kamers en verblijven vast, en duidt aan **wie** verwittigd wordt wanneer een
bewoner aankomt of van kamer wisselt.

| Instelling | Waarvoor | Aanbevolen waarde (ROB/RVT) |
|---|---|---|
| **Standaard verblijfsduur** | Vult de duur (in dagen) voor die voorgesteld wordt bij het openen van een nieuw verblijf. | **30 dagen** |
| **Standaard kamercapaciteit** | Aantal bedden dat vooringevuld wordt bij het aanmaken van een nieuwe kamer. | **1 bed** (eenpersoonskamer) |
| **Technisch verantwoordelijke kamers** | Gebruiker die de activiteit « kamer voorbereiden » krijgt bij de aankomst van een bewoner of bij een kamerwissel / overdracht. | De technische of onderhoudsmedewerker van uw huis. |
| **Verantwoordelijke intrekprocedure** | Gebruiker die de intrekchecklist (overeenkomst, plaatsbeschrijving, inventaris, medicatiekast, linnen, ontsmetting) op de fiche van de bewoner krijgt. | De opnamereferent — **laat leeg om uit te schakelen**. |

!!! tip "Twee complementaire verantwoordelijken"
    Bij elke **[kamerwissel of overdracht](../residents/changement-chambre.md)**
    net als bij de **[opname](../residents/gerer-un-resident.md)** opent Resthome
    een nieuw verblijf en start automatisch:

    - een activiteit **« kamer voorbereiden »** voor de **technisch
      verantwoordelijke**;
    - de **intrekchecklist** (als er een **verantwoordelijke intrekprocedure** is
      ingesteld) op de fiche van de bewoner.

    Het zijn werkherinneringen: ze instellen voorkomt vergetelheden bij de aankomst.

## Dashboard

*Instellingen > Medisch > Dashboard.* Eén enkele instelling, die de weergave van
de statistiekkaarten van het zorgdashboard bepaalt.

| Instelling | Waarvoor | Aanbevolen waarde (ROB/RVT) |
|---|---|---|
| **Hide Empty Stat Cards** (lege kaarten verbergen) | Verbergt de dashboardkaarten (gemiste zorg, aandachtspunten, Katz-vernieuwingen…) waarvan de teller op 0 staat. | **Uitgeschakeld laten** (standaard): een getoonde « 0 » is een positief signaal, geen ontbrekende informatie. |

## Demogegevens

*Instellingen > Rusthuis > Demogegevens.* Om een **test**database te vullen met
fictieve bewoners, kamers, verblijven en facturen.

| Instelling | Waarvoor | Aanbevolen waarde (ROB/RVT) |
|---|---|---|
| **Demogegevens laden** | Maakt fictieve bewoners, kamers, verblijven, facturatieperiodes, medische gegevens en maaltijden aan. | Houd voor een **test**omgeving. |
| **Update Demo Data** | Herstart de lader om sindsdien toegevoegde demogegevens (meubilair, supplementen…) toe te voegen zonder het bestaande te dupliceren. | Enkel test. |

!!! warning "Nooit op uw echte database"
    De demogegevens maken **fictieve bewoners en facturen** aan. Gebruik deze
    knoppen enkel op een test- of opleidingsdatabase, **nooit** op uw
    productieomgeving.

## Verder lezen

- [Configuratie](index.md)
- [Een bewoner beheren](../residents/gerer-un-resident.md)
- [Kamerwissel en overdracht](../residents/changement-chambre.md)
- [Aan de slag](../premiers-pas.md)
- [FAQ](../faq.md) · [Woordenlijst](../glossaire.md)
