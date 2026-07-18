---
title: Documentinstellingen
description: "De centralisatie van bewonersdocumenten in het woonzorgcentrum (WZC/RVT) configureren — hoofdmap, standaardtags, automatisch opbergen in de Documenten-app."
faq:
  - q: "Waar vind ik de instellingen voor documentcentralisatie?"
    a: "In « Instellingen > Documenten > Bestandscentralisatie », blok « Woonzorgcentrum ». Dit blok verschijnt alleen wanneer de Documenten-app geïnstalleerd is."
  - q: "Wat doet de centralisatie van bewonersdocumenten precies?"
    a: "Wanneer ze geactiveerd is, wordt elke bijlage die op de fiche van een bewoner (discussievenster) wordt gezet, automatisch opgeborgen in de persoonlijke map van die bewoner in de Documenten-app. Zo vindt u alle stukken van een bewoner op één plek terug, zonder handmatig te klasseren."
  - q: "Moet ik de hoofdmap « Residents » zelf aanmaken?"
    a: "Nee. Resthome maakt de hoofdmap « Residents » (met een submap « Blank forms ») automatisch aan zodra de vennootschap wordt aangemaakt. Het veld « Hoofdmap » verwijst er al naar; u hoeft niets voor te bereiden."
  - q: "Waarvoor dienen de standaardtags?"
    a: "Dat is optioneel. De gekozen labels worden automatisch toegepast op de gecentraliseerde documenten, wat het zoeken en filteren in de Documenten-app vergemakkelijkt. U mag dit veld leeg laten."
  - q: "Kan ik de centralisatie uitschakelen?"
    a: "Ja, door het blok « Woonzorgcentrum » uit te vinken. De reeds opgeborgen documenten blijven in de bewonersmappen; enkel de toekomstige bijlagen worden niet meer automatisch gecentraliseerd."
  - q: "Geldt de instelling voor al mijn instellingen?"
    a: "Nee. Ze is eigen aan elke vennootschap (instelling) in de database. Elke vennootschap heeft haar eigen hoofdmap « Residents » en haar eigen parametrering, zodat de mappen afgeschermd blijven."
---

# Documentinstellingen

Het tabblad **Instellingen > Documenten** groepeert de parameters van de Odoo
**Documenten**-app. Resthome voegt daar, in de sectie **Bestandscentralisatie**, een blok
**Woonzorgcentrum** toe dat de bijlagen van uw bewoners **automatisch opbergt** in hun
**persoonlijke map**. U vindt deze instellingen in **Instellingen > Documenten >
Bestandscentralisatie**.

!!! info "Vereiste"
    Deze instellingen verschijnen alleen als de applicatie **Documenten** geïnstalleerd
    is. De hoofdmap van de bewoners wordt automatisch aangemaakt — u hoeft niets voor te
    bereiden vóór u de centralisatie activeert.

## Centralisatie van bewonersdocumenten

Het blok **Woonzorgcentrum** stuurt het automatisch opbergen van documenten aan. Een
selectievakje activeert de centralisatie; eenmaal aangevinkt, toont het de **hoofdmap** en
de **standaardtags**.

| Instelling | Waarvoor ze dient | Aanbevolen waarde (WZC/RVT) |
|---|---|---|
| **Woonzorgcentrum** (centralisatie) | Activeert het automatisch opbergen: elke bijlage op de fiche van een bewoner wordt in zijn persoonlijke map van de Documenten-app geklasseerd. | **Geactiveerd** (aangevinkt) |
| **Hoofdmap** | De map van de Documenten-app waaronder Resthome alle bewonersmappen opbergt. | Map **« Residents »** (automatisch aangemaakt) |
| **Standaardtags** | De labels die automatisch op de gecentraliseerde documenten worden toegepast, om ze terug te vinden en te filteren. | **Optioneel** — leeg laten, of 1 tot 2 tags kiezen |

!!! tip "De hoofdmap wordt voor u aangemaakt"
    Bij het aanmaken van de vennootschap maakt Resthome automatisch de map **« Residents »**
    aan (met een submap **« Blank forms »** voor uw sjablonen). Het veld **Hoofdmap**
    verwijst er al naar. Er is normaal geen reden om ze te wijzigen; pas ze enkel aan als u
    de bewoners bewust elders opbergt.

## Eén map per bewoner

U maakt de mappen niet handmatig aan. Bij de opname van een bewoner (of bij het activeren
van zijn bewonersfiche) maakt Resthome zijn **persoonlijke map** aan onder de hoofdmap, met
drie klaargezette submappen:

- **Medical documents** (medische documenten)
- **Administrative documents** (administratieve documenten)
- **Billing documents** (facturatiedocumenten)

De map draagt de **naam van de bewoner** en wordt automatisch hernoemd als de naam wijzigt.
De knop **Documenten** op de bewonersfiche opent rechtstreeks deze map (de teller omvat de
stukken uit de submappen).

!!! note "Afgeschermd per instelling"
    Bij multi-vennootschap heeft **elke vennootschap haar eigen hoofdmap** « Residents ». De
    instelling is **eigen aan elke instelling**: activeer de centralisatie in elk van hen als
    u meerdere huizen uitbaat.

## Standaardtags (optioneel)

De **tags** (labels) dienen om documenten te categoriseren en terug te vinden. Resthome
levert al een lijst klaargezette labels — bijvoorbeeld **Katz**, **Einde verblijf**,
**eAgreement**, **VI**, **Overeenkomst**, **Medisch formulier**, **Facturatie**, **OCMW**,
**GDPR**. In **Standaardtags** kiest u die welke **automatisch** op elk gecentraliseerd
document worden toegepast.

!!! tip "Begin licht"
    Laat dit veld bij de start **leeg**, of zet er één algemene tag in. U kunt elk document
    achteraf altijd fijner labelen in de Documenten-app.

## De centralisatie uitschakelen

Het blok **Woonzorgcentrum** uitvinken **stopt** het automatisch opbergen van toekomstige
bijlagen. De reeds geklasseerde documenten **blijven** in de bewonersmappen staan — er wordt
niets verwijderd of verplaatst.

## Verder

- [Configuratie](index.md)
- [Een bewoner beheren](../residents/gerer-un-resident.md)
- [FAQ](../faq.md) · [Woordenlijst](../glossaire.md)
