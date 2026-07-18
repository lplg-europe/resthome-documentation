---
title: De maaltijdverdeelronde
description: "Maaltijden verdelen in een woonzorgcentrum (WZC/RVT) met Resthome: tabletassistent bewoner per bewoner, hoeveelheid gegeten, afdrukbare verdeelbladen per sector."
howto_auto: true
faq:
  - q: "Waar start je de maaltijdverdeelronde in Resthome ?"
    a: "In de toepassing Maaltijden → Operaties. Klik vanaf een bevestigd menu op « Snelle distributie » voor de tabletassistent, of druk het verdeelblad van de maaltijd af via het menu Actie."
  - q: "Hoe markeer je een bewoner tijdens de ronde ?"
    a: "De assistent toont de bewoners één voor één met vier grote knoppen: Geserveerd, Overslaan, Afwezig en Kamer. Eén tik registreert de dienst en gaat automatisch naar de volgende wachtende bewoner."
  - q: "Hoe noteer je de hoeveelheid die een bewoner at ?"
    a: "Op de maaltijddienst van de bewoner (Maaltijden → Operaties → Maaltijddiensten) biedt het veld « Hoeveelheid gegeten » de keuzes Niet gegeten, 25 %, 50 %, 75 % of Volledig gegeten. Die waarde voedt de voedingsopvolging."
  - q: "Waarvoor dienen de afdrukbare verdeelbladen ?"
    a: "Dit zijn papieren bladen, één pagina per sector, met aankruisvakjes (eetzaal, kamer, afwezig, geserveerd) en een handtekeningregel voor de verantwoordelijke — een noodoplossing wanneer de tablet niet beschikbaar is."
  - q: "Kun je de ronde filteren per sector of plaats ?"
    a: "Ja. Kies in de assistent een sector voordat je op Laden klikt, en beperk indien nodig tot de eetzaal of de maaltijden op kamer."
  - q: "Wat gebeurt er als een bewoner heel weinig eet ?"
    a: "Als de bewoner 25 % of minder at en zijn familie geïntegreerd is in de meldingen, kan Resthome een waarschuwing sturen. De waarde verlaagt ook de voedingsdekking die op de fiche van de bewoner wordt getoond."
---

# De maaltijdverdeelronde

De **verdeelronde** volgt elke maaltijd tot bij de bewoner: wie eet **waar**, wie
is **geserveerd**, wie is **afwezig**, en **hoeveel** ieder gegeten heeft.
Resthome biedt twee aanvullende hulpmiddelen, beide in de toepassing
**Maaltijden → Operaties** :

- de **tabletassistent** (knop **Snelle distributie**) om de bewoners **één voor
  één** op het scherm af te punten ;
- de **afdrukbare verdeelbladen** per sector, als **papieren** oplossing.

!!! note "Vóór het verdelen"
    Het **menu** van de maaltijd moet in de status **Bevestigd** staan. De
    **maaltijddiensten** (één record per bewoner en per maaltijd) worden
    automatisch aangemaakt wanneer je de verdeling start — je hoeft ze niet
    handmatig in te voeren.

## 1. De assistent openen vanaf het bevestigde menu

1. Ga naar **Maaltijden → Operaties → Menu's** en open het menu van de betrokken
   maaltijd.
2. Staat het nog in concept, klik dan op **Bevestigen** : de knoppen **Dienst
   starten** en **Snelle distributie** verschijnen alleen op een menu met status
   **Bevestigd**.
3. Klik op **Snelle distributie** (tabletpictogram). De assistent opent in een
   venster op volle breedte, geschikt voor een aanraakscherm.

!!! tip "Dienst starten of Snelle distributie ?"
    **Dienst starten** maakt de maaltijddiensten voor alle bewoners aan en opent
    hun **lijst**. **Snelle distributie** doet dezelfde voorbereiding en start
    daarna meteen de **assistent** om af te punten. Gebruik voor de ronde
    **Snelle distributie**.

<!-- capture toe te voegen : kop van een bevestigd menu met de knoppen Dienst starten en Snelle distributie -->

## 2. De ronde filteren en laden

Bovenaan in de assistent bakenen drie instellingen de ronde af :

- **Menu** — vooraf ingevuld met het menu waarvan je vertrok.
- **Sector** — optioneel: beperkt de ronde tot één sector (een vleugel, een
  verdieping).
- **Plaats** — beperkt tot bewoners die in de **eetzaal** of **op kamer** worden
  bediend ; laat het op alle plaatsen om iedereen te zien.

Klik op **Laden** om de lijst (opnieuw) op te bouwen. Ze is gesorteerd op
**sector**, dan **kamer**, dan **bewoner**, in de volgorde van je rondgang.

## 3. De bewoners overlopen

Tik op een bewoner om zijn **kaart** te openen: foto, **kamer**, **sector** en
**diëten**. Met vier grote knoppen punt je in één beweging af :

| Knop | Effect |
| --- | --- |
| **Geserveerd** | Markeert de maaltijd als **geserveerd** en gaat naar de volgende wachtende bewoner. |
| **Overslaan** | Gaat naar de volgende bewoner **zonder iets te wijzigen** (later te behandelen). |
| **Afwezig** | Markeert de bewoner als **afwezig** (niet geserveerd) en gaat naar de volgende. |
| **Kamer** | Geeft aan dat de bewoner **op kamer** eet en blijft op zijn kaart. |

Het tabblad **Volledige lijst** toont alle bewoners met een **kleurcode** :
**groen** = geserveerd, **grijs** = afwezig, **rood** = kritieke waarschuwing,
**oranje** = waarschuwing. Elke regel heeft ook haar knoppen **Geserveerd** en
**Afwezig** om snel af te punten zonder de kaart te openen.

Bovenaan telt een **voortgangsbalk** live mee : **geserveerd / totaal**, **in
afwachting**, **afwezig** en het percentage voltooid.

!!! warning "Kritieke allergiewaarschuwing"
    Een **rode banner** signaleert een ernstige onverenigbaarheid tussen een
    voorzien gerecht en het profiel van de bewoner. Resthome **weigert
    « Geserveerd »** te markeren voor een dienst met een **kritiek allergeen**
    zolang de gerechten niet zijn aangepast. Zie [Menu's, diëten en
    hydratatie](menus-regimes.md).

<!-- capture toe te voegen : bewonerkaart van de assistent met de vier grote knoppen Geserveerd / Overslaan / Afwezig / Kamer -->

## 4. De hoeveelheid gegeten noteren

Het **gegeten percentage** wordt genoteerd op de **maaltijddienst** van de
bewoner (het maakt geen deel uit van de afpuntassistent) :

1. Open **Maaltijden → Operaties → Maaltijddiensten** en selecteer de dienst van
   de bewoner.
2. Vul het veld **Hoeveelheid gegeten** in :

| Keuze | Betekenis |
| --- | --- |
| **Niet gegeten** | De bewoner heeft niets gegeten. |
| **25 %** | Ongeveer een kwart van de maaltijd. |
| **50 %** | Ongeveer de helft. |
| **75 %** | Ongeveer drie kwart. |
| **Volledig gegeten** | Maaltijd op. |

De hoeveelheid gegeten is meer dan een notitie: samen met de geserveerde
gerechten berekent ze de **werkelijke inname** (energie, eiwitten) die de
**voedingsdekking** op de fiche van de bewoner voedt. Zie
[Voedingsopvolging](suivi-nutritionnel.md).

!!! info "Lage inname en families"
    Als een bewoner **25 % of minder** at en zijn familie **geïntegreerd is in de
    maaltijdmeldingen**, kan Resthome automatisch een **waarschuwing** sturen.
    Deze optie wordt per bewoner ingesteld. Zie [Familieportaal en
    kiosk](portail-familles.md).

## 5. De ronde afsluiten

- Klik op **Gereed** (of **Sluiten**) om de assistent te verlaten.
- Op het maaltijdmenu kun je daarna op **Markeer als geserveerd** klikken om het
  menu naar de status **Geserveerd** te brengen.

!!! note "Traceerbaarheid"
    Een **geserveerde** dienst en een **Geserveerd** menu kunnen niet meer worden
    **verwijderd** : Resthome bewaart ze voor de traceerbaarheid. Corrigeer
    liever de gegevens op het bestaande record.

## Het verdeelbord (per plaats)

Als aanvulling op de tabletassistent opent **Maaltijden → Operaties →
Distributie** een **kanbanbord** van de diensten van de dag, **gegroepeerd per
plaats** (eetzaal, op kamer, afwezig). Elke kaart toont de foto, de **kamer**, de
**sector**, het **dieet**badge en, indien van toepassing, een badge **Alarm**,
**Waarschuwing** of **Geserveerd**.

Vanuit de **lijst** met maaltijddiensten kun je met twee kopknoppen op een
**meervoudige selectie** inwerken : **Markeer als geserveerd** en **Markeer
afwezig**. Het menu **Actie** biedt ook aan de diensten **in de eetzaal** of **op
kamer** te markeren.

## De afdrukbare verdeelbladen per sector

Verkies je **papier**, druk de bladen dan af vanaf een **menu** (formulier- of
lijstweergave), via het menu **Actie** : je kunt het **verdeelblad** van één
maaltijd afdrukken, of **alle bladen van de dag**. Resthome maakt daarbij de
ontbrekende diensten aan en opent vervolgens het document.

Het blad ziet er zo uit :

- **één pagina per sector**, met kop : **sector**, **maaltijdtype**, **datum** en
  **aantal bewoners** ;
- een tabel : **#**, **Bewoner**, **Kamer**, **Diëten / Allergieën** (**blauwe**
  badges voor diëten, **rode** voor allergieën, « **!** » voor een kritiek
  alarm), dan **aankruisvakjes** **Eetzaal**, **Kamer**, **Afwezig** en
  **Geserveerd**, en een kolom **Notities** ;
- een voettekst met een regel **Handtekening verantwoordelijke** en de **datum en
  het uur van afdruk**.

Het is een **checklist voor op het terrein** : het personeel kruist de vakjes aan
tijdens de ronde, laat de verantwoordelijke tekenen en brengt de gegevens
nadien in Resthome in.

<!-- capture toe te voegen : afgedrukt verdeelblad van een sector met de aankruisvakjes en de handtekeningregel -->

## Kernpunten om te onthouden

- De ronde leeft in **Maaltijden → Operaties** ; ze start vanaf een menu met
  status **Bevestigd**.
- **Snelle distributie** is de tabletassistent : vier knoppen **Geserveerd**,
  **Overslaan**, **Afwezig**, **Kamer**, met automatische doorstroming naar de
  volgende bewoner.
- De **Hoeveelheid gegeten** (Niet gegeten → Volledig gegeten) noteer je op de
  **maaltijddienst** en ze voedt de **voedingsopvolging**.
- De **afdrukbare verdeelbladen per sector** (aankruisvakjes + handtekening) zijn
  de papieren noodoplossing.
- Een **geserveerde** dienst of menu wordt niet verwijderd : Resthome bewaart het
  spoor.

## Meer weten

- [Menu's, diëten en hydratatie](menus-regimes.md)
- [Voedingsopvolging](suivi-nutritionnel.md)
- [Familieportaal en kiosk](portail-familles.md)
- [Overzicht van de toepassing Maaltijden](index.md)