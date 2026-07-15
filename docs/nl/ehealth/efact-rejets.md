---
title: eFact-weigeringen — oorzaken en oplossingen
description: "Waarom een eFact-factuur van een woonzorgcentrum wordt geweigerd en hoe u ze in Resthome corrigeert: verzekerbaarheid, forfait, datums, dubbels, heruitzending."
faq:
  - q: "Waarom wordt een eFact-factuur geweigerd?"
    a: "Meestal: verzekerbaarheid (MDA) niet geldig, verkeerd ziekenfonds op de fiche, forfait gedeclareerd na het einde van de RIZIV-tussenkomst, niet-afgesloten afwezigheid, ontbrekende Katz-categorie, verkeerd INSZ of dubbele verzending. De code en de reden van weigering van de verzekeringsinstelling geven de oorzaak aan."
  - q: "Wat te doen wanneer een eFact-lot wordt geweigerd?"
    a: "U verstuurt een lot niet zomaar opnieuw: u corrigeert de oorzaak bij de bron (MDA, ziekenfonds, Katz, datums…), genereert opnieuw en verstuurt dan. De teller Heruitzendingen houdt de retransmissies bij om dubbels te vermijden."
  - q: "Wat is het verschil tussen een globale en een gedeeltelijke weigering?"
    a: "Een gedeeltelijke weigering weigert enkel bepaalde lijnen (de rest wordt betaald): u corrigeert en verstuurt enkel die lijnen. Een globale weigering weigert het volledige lot: u corrigeert de oorzaak en verstuurt een nieuw lot."
  - q: "Hoe corrigeer ik een overfacturatie (vertrek, overlijden, overgedeclareerd forfait)?"
    a: "Resthome detecteert het via de automatische controle en bereidt een creditnota voor aan bewonerszijde en, indien het mutualiteitsaandeel betrokken is, een corrigerend lot naar de verzekeringsinstelling. De creditlijnen worden in de volgende verzending opgenomen."
---

# eFact-weigeringen — oorzaken en oplossingen

Wanneer u de [eFact](efact.md) verstuurt, controleert de **verzekeringsinstelling
(VI)** elke lijn en stuurt u een resultaat terug. Deze pagina legt uit **hoe u een
antwoord leest**, **waarom een lot of een lijn geweigerd wordt**, en **hoe u corrigeert
en opnieuw verstuurt**.

!!! info "Twee verdedigingslinies"
    De meeste oorzaken van weigering worden **door Resthome onderschept vóór de
    verzending** (automatische controle van de periode, controles bij het genereren). Ze
    verschijnen dan als een **afwijkingsbericht** dat u moet behandelen, niet als een
    weigering. De gevallen die er toch door raken, komen daarna terug als een **weigering
    van de VI**. Deze pagina behandelt beide.

## De antwoordcyclus, in het kort

Na de verzending van een lot doen de antwoorden van de VI de **status van het lot**
evolueren en vullen ze de **bedragen** in (gefactureerd / aanvaard / geweigerd):

1. **Ontvangstbewijs** — de VI bevestigt het bestand ontvangen te hebben en de eerste
   controle te hebben doorstaan. Niets te doen.
2. **Afrekening van de VI** — de VI stuurt het resultaat **lijn per lijn** terug: wat
   **aanvaard** en wat **geweigerd** is. Resthome stemt deze afrekening af en werkt de
   bedragen van het lot bij.
3. **Aanvaarding en/of weigering** — drie mogelijke uitkomsten:
    - **alles aanvaard** → het lot is afgerekend en kan afgesloten worden ;
    - **gedeeltelijke weigering** — bepaalde lijnen worden geweigerd, de rest wordt
      betaald: u corrigeert en verstuurt **enkel** de geweigerde lijnen ;
    - **globale weigering** — het volledige lot wordt geweigerd, niets wordt betaald: u
      corrigeert de oorzaak en **verstuurt een nieuw lot**.

Bij elke geweigerde lijn geven een **code** en een **reden van weigering** in klare
taal de oorzaak aan.

## Frequente oorzaken van weigering → actie

| Oorzaak | Wat u ziet | Actie in Resthome |
|---|---|---|
| **Verzekerbaarheid (MDA) niet geldig of ontbrekend** | Teller **MDA** niet groen ; lot tegengehouden bij verzending ; of weigering van de VI voor verzekerbaarheid | Start **MDA controleren**, verkrijg de status **Succes** voor elke bewoner, en **genereer** de eFact opnieuw. De MDA moet gevalideerd zijn **vóór** het genereren. |
| **Verkeerd of ontbrekend ziekenfonds** | Het forfait gaat naar de verkeerde VI (weigering) of verschijnt niet in het lot | Vul het **ziekenfonds** in / corrigeer het op de fiche van de bewoner, en **genereer opnieuw**. Controleer dat elke bewoner die in derdebetaler wordt gefactureerd een ziekenfonds heeft. |
| **Forfait gedeclareerd na het einde van de tussenkomst** | Automatische controle: **« forfait VI overgedeclareerd »** ; de VI weigert de teveel gedeclareerde dagen | Maak een **creditnota / een saldo** aan voor de overgedeclareerde dagen (zie verder). |
| **Kamer vrijgekomen / overlijden — verblijf nog gefactureerd** | Automatische controle: **overfacturatie** ; weigering van de onterechte dagen | **Verblijf afsluiten** op de juiste datum + **creditnota**. |
| **Niet-afgesloten afwezigheid** | Teller **Afwezigheden** actief ; forfaitdagen vervalst | Sluit de afwezigheden van de periode af en controleer de dagen opnieuw. |
| **Ontbrekende Katz-categorie of verlopen evaluatie** | Teller **« Katz te doen »** ; blokkering bij het genereren | Vul de **Katz-evaluatie** aan of vernieuw ze, en **genereer opnieuw**. |
| **Ontbrekend of verkeerd INSZ** | Verplicht identificatiegegeven → technische weigering | Corrigeer het **INSZ** op de fiche van de bewoner en genereer opnieuw. |
| **Dubbele verzending** | De VI meldt een **reeds ontvangen verzending** | Verstuur een **reeds aanvaard** lot niet opnieuw. Voor een gerechtvaardigde heruitzending steunt u op de teller **Heruitzendingen** (anti-dubbel). |
| **Discordantie van bedrag / tarief** | De VI stuurt een **onverwacht bedrag/tarief** terug | Controleer het toegepaste **tarief** en het bedrag van de lijn, corrigeer de instelling, genereer opnieuw, verstuur opnieuw. |
| **Technische weigering / formaatfout** | **Globale weigering**: het bestand doorstond de formaatcontrole niet | Zeldzaam geval om te escaleren: gebruik **Contact VI** of **Helpdesk**, corrigeer, en verstuur een nieuw lot. |

## Corrigeren, dan opnieuw versturen

Het principe: **u duwt een geweigerd lot niet zomaar opnieuw door — u corrigeert de
oorzaak bij de bron, en verstuurt dan opnieuw.**

- **Lus corrigeren → opnieuw versturen.** Nadat u de oorzaak hebt behandeld (MDA,
  ziekenfonds, Katz, afwezigheid, datums…), genereert u het betrokken deel opnieuw en
  verstuurt u het. De teller **Heruitzendingen** houdt elke retransmissie bij om te
  **vermijden dat u tweemaal** hetzelfde lot verstuurt.
- **Herintegratie.** De knop **Herintegratie** laat toe om lijnen (bijvoorbeeld
  geweigerde lijnen, eens gecorrigeerd) in een **nieuwe verzending** te herintegreren,
  in plaats van alles over te doen.
- **Creditnota / corrigerend lot.** Telkens u **meer hebt gefactureerd dan verschuldigd**
  — vertrek of overlijden tijdens een gefactureerde maand, overgedeclareerd forfait —
  bereidt Resthome een **creditnota** voor (bewonerszijde) en, indien het
  mutualiteitsaandeel betrokken is, een **corrigerend lot** naar de VI. De creditlijnen
  worden in de **volgende eFact-verzending** opgenomen.

## De antwoorden die u kunt tegenkomen

Afhankelijk van het bericht van de VI kunt u, in de statussen of het logboek van het
lot, tegenkomen:

| Antwoord | Wat het betekent |
|---|---|
| **Ontvangstbewijs** | De VI heeft het bestand **ontvangen** en de eerste controle doorstaan. Normale stap. |
| **Melding met waarschuwingen** | Het lot is **aanvaard**, maar met **waarschuwingen** (kleine fouten) om te lezen. |
| **Afrekening** | Het **resultaat lijn per lijn**: **aanvaarde** en **geweigerde** bedragen. Hier verschijnen de gedeeltelijke weigeringen om te corrigeren. |
| **Globale weigering** | Het **volledige lot is geweigerd** (te veel fouten). Corrigeer de oorzaak en **verstuur een nieuw lot**. |
| **Technische weigering** | Het bestand doorstond de **formaatcontrole** niet ; retransmissie nodig na correctie. |

## Kernpunten

- **Voorkomen is beter dan genezen**: behandel de **automatische controleberichten** en
  valideer de **MDA** vóór u factureert — zo vermijdt u de meeste weigeringen.
- Een **gedeeltelijke weigering** corrigeert u **lijn per lijn**; een **globale
  weigering** **verstuurt u opnieuw als een nieuw lot**.
- Een **overfacturatie** (vertrek, overlijden, overgedeclareerd forfait) corrigeert u met
  een **creditnota / corrigerend lot**, niet met een gewone heruitzending.

## Verder

- [Elektronische facturatie (eFact)](efact.md)
- [Verzekerbaarheid (MDA)](mda.md) · [MDA-fouten](mda-erreurs.md)
- [Vertrek en overlijden](../facturation/depart-deces.md)
- [FAQ](../faq.md) · [Woordenlijst](../glossaire.md)
