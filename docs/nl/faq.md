---
title: FAQ — Veelgestelde vragen
description: "Korte antwoorden op veelgestelde vragen over Resthome: aan de slag, bewoners, Katz, MDA, eAgreement, eFact, facturatie, vertrek en overlijden."
faq:
  - q: "Hoe controleer ik de verzekerbaarheid (MDA) van een bewoner?"
    a: "Maak een MDA-aanvraag aan (eHealth → Verzekerbaarheid → MDA-aanvragen) met de bewoner, het vooraf ingevulde INSZ en de periode, en klik op Verzenden (Sync): het antwoord komt meteen terug. Doe dit aan het begin van de maand, vóór het factureren, om eFact-weigeringen te vermijden."
  - q: "Hoe genereer ik een eFact-periode?"
    a: "Open de periode van de maand in de status Draft, klik op Genereren, laat Residents leeg voor alle actieve bewoners, klik op MDA laden en daarna op Generate. De periode gaat naar Generated: het Katz-forfait, het RIZIV-gedeelte en het bewonersgedeelte worden voor elke bewoner berekend."
  - q: "Hoe verzend ik een eFact-periode en volg ik de antwoorden op?"
    a: "Klik vanaf de eFact-Cockpit of de loten op Alles verzenden: de loten vertrekken naar de ziekenfondsen via eHealth. Klik daarna op Antwoorden ophalen; elk lot gaat Verzonden → Ontvangst bevestigd → Aanvaard / Geweigerd, waarbij Resthome de bedragen automatisch afstemt."
  - q: "Waarom wordt een eFact-factuur geweigerd, en hoe corrigeer ik dit?"
    a: "De code en de reden van weigering geven de oorzaak aan (verzekerbaarheid, forfait, datums). Corrigeer die en verzend opnieuw; de teller Heruitzendingen vermijdt dubbels en de knop Herintegratie laat toe om lijnen in een nieuwe verzending te herintegreren."
  - q: "Wat is een eFact-lot per unie?"
    a: "De verzendingen worden gegroepeerd per unie van mutualiteiten (100 Landsbond der Christelijke Mutualiteiten, 300 Solidaris, 500 Onafhankelijke Ziekenfondsen, 600 HZIV, 900 HR Rail…), niet per kleine afzonderlijke mutualiteit. Resthome zorgt voor de groepering."
  - q: "Hoe bereken ik de Katz van een bewoner?"
    a: "Open vanaf de fiche van de bewoner Katz, klik op Nieuw en scoor de 6 criteria (zich wassen, zich kleden, transfer en verplaatsing, naar het toilet gaan, continentie, eten) van 1 tot 4, en klik daarna op Bevestigen en Valideren. De categorie en het forfait worden automatisch bijgewerkt."
  - q: "Wat zijn de Katz-categorieën?"
    a: "O (zelfstandig), A (lichte afhankelijkheid), B (matige afhankelijkheid), C (sterke afhankelijkheid) en Cd / Cc (sterke afhankelijkheid met desoriëntatie of bijzondere gevallen). In de AViQ-tarieven is het afhankelijkheidsforfait hetzelfde bedrag voor alle categorieën, inclusief O; de categorie dient om het juiste profiel aan de mutualiteit te melden."
  - q: "Hoe factureer ik een maand van A tot Z in Resthome?"
    a: "Open de periode, controleer de MDA, klik op Genereren, Facturen aanmaken en boek het bewonersgedeelte; daarna eFact genereren, verzend het ziekenfondsgedeelte naar de verzekeringsinstellingen en haal de antwoorden op. Het bewonersgedeelte en het ziekenfondsgedeelte lopen parallel op eenzelfde periode."
  - q: "Hoe registreer ik een afwezigheid of een ziekenhuisopname?"
    a: "Open de periode van de maand (of de fiche van de bewoner) en voeg een afwezigheid toe met het type, de vertrekdatum/-uur en de terugkeerdatum/-uur, en klik op Opslaan. De facturatie van de bewoner synchroniseert automatisch; het forfait wordt verminderd voor de afwezigheidsdagen volgens de middagregel."
  - q: "Wat gebeurt er bij het vertrek of het overlijden van een bewoner?"
    a: "Sluit zijn verblijf af met de uittredingsdatum en de reden (vertrek, overlijden, transfer). Resthome stopt de facturatie op de juiste datum, bereidt de creditnota voor de op voorhand gefactureerde huisvesting voor en meldt de uittrede aan het ziekenfonds."
  - q: "Wat is anticipatieve facturatie in Resthome?"
    a: "Voor bewoners die op voorhand worden gefactureerd, wordt de huisvesting van een maand de voorgaande maand gefactureerd, terwijl het RIZIV-forfait en de supplementen op de prestatiemaand worden gefactureerd."
  - q: "Hoe voeg ik een supplement toe aan een bewoner?"
    a: "Open de supplementenenveloppe van de bewoner, voeg een lijn toe (product/prestatie, hoeveelheid, prijs), geef aan of het supplement eenmalig of terugkerend is, en klik op Opslaan. Het toevoegen werkt de factuur van de betrokken bewoner automatisch bij."
---

# Veelgestelde vragen (FAQ)

Deze pagina bundelt korte antwoorden op de meest gestelde vragen. Elk antwoord
verwijst naar de documentatiepagina die het in detail behandelt.

---

## Aan de slag

### Hoe meld ik mij aan bij Resthome?

Open uw browser op het adres dat uw instelling u bezorgde, voer uw e-mailadres en
uw wachtwoord in en klik op **Aanmelden**. Bent u het vergeten, gebruik dan de link
« Wachtwoord opnieuw instellen » of vraag het aan uw beheerder.
→ [Aan de slag](premiers-pas.md)

### Welke apps bevat Resthome?

Resthome is opgebouwd uit apps die u opent via het hoofdmenu (het
dambordpictogram): **MR/MRS** (bewoners, verblijven, facturatie, Katz, eHealth),
**Zorg** (voorschriften, zorgplannen, vitale parameters), **Maaltijden** (menu's,
diëten, familieportaal) en **Configuratie** (kamers, tarieven, basisgegevens).
Afhankelijk van uw rol ziet u enkel de apps die u aanbelangen.
→ [Aan de slag](premiers-pas.md)

### Waarvoor dient het dashboard?

Het dashboard van de app MR/MRS geeft een overzicht: de openstaande taken (Katz te
doen, MDA te controleren, eFact-loten…), aanklikbare tellers die meteen de betrokken
lijst openen, en de belangrijke waarschuwingen van de maand. Klik op een teller (bv.
« Katz te doen ») om de lijst met te behandelen elementen te openen.
→ [Aan de slag](premiers-pas.md)

### Waar stelt men de kamers en de tarieven in?

In de app **Configuratie**: maak uw kamers aan met hun type (MR, MRS, eenpersoons,
tweepersoons…) en uitrusting, bepaal de **RIZIV-tarieven** (forfait per
Katz-categorie) en de **huisvestingstarieven**, en daarna de types supplementen en
de ziekenfondsen. Resthome beheert ook **meerdere vennootschappen** in eenzelfde
database, elk met hun eigen bewoners, kamers en gescheiden facturatie.
→ [Configuratie](configuration/index.md)

---

## Bewoners & Katz

### Hoe maak ik een bewoner aan?

Open **MR/MRS → Bewoners**, klik op **Nieuw**, vul minstens de naam, de
geboortedatum, het geslacht en het **INSZ** in indien gekend, selecteer het
ziekenfonds en klik op **Opslaan**. Zonder INSZ kunnen de MDA-controle en de
eAgreement-akkoorden niet verzonden worden, maar u kunt de bewoner wel aanmaken en
het INSZ later aanvullen.
→ [Een bewoner beheren](residents/gerer-un-resident.md)

### Hoe start ik een verblijf?

Open een **verblijfsovereenkomst** (kamer, type MR/MRS, begindatum) — het verblijf
staat dan op **Concept**. **Bevestig** het (de kamer wordt gereserveerd, vul de
datum/het uur van opname aan) en klik daarna op **Start Stay (Starten)**: het
verblijf gaat naar **Lopend**.
→ [Een bewoner beheren](residents/gerer-un-resident.md)

### Wat wordt automatisch in gang gezet bij de start van een verblijf?

Bij de start voegt Resthome de bewoner toe aan de openstaande facturatieperiodes,
maakt (voor een bewoner die op voorhand wordt gefactureerd) de eerste
huisvestingsfactuur van de opnamemaand aan, opent de supplementenenveloppe van de
maand en maakt het opname-eAgreement aan (als het INSZ aanwezig is).
→ [Een bewoner beheren](residents/gerer-un-resident.md)

### Hoe bereken ik de Katz van een bewoner?

Open vanaf de fiche van de bewoner **Katz**, klik op **Nieuw** en scoor de 6 criteria
(zich wassen, zich kleden, transfer en verplaatsing, naar het toilet gaan,
continentie, eten) van **1** (zelfstandig) tot **4** (volledig afhankelijk), en klik
daarna op **Bevestigen** en **Valideren**. Resthome berekent de categorie volgens de
reglementering en werkt het forfait automatisch bij.
→ [De Katz-evaluatie](residents/katz.md)

### Wat zijn de Katz-categorieën?

**O** (zelfstandig), **A** (lichte
afhankelijkheid), **B** (matige afhankelijkheid), **C** (sterke afhankelijkheid) en
**Cd / Cc** (sterke afhankelijkheid met desoriëntatie / bijzondere gevallen). In de
AViQ-tarieven is het **bedrag van het forfait voor alle categorieën gelijk**, inclusief
O; de categorie dient om het juiste profiel aan de mutualiteit te melden.
→ [De Katz-evaluatie](residents/katz.md)

### Wat gebeurt er zolang er geen gevalideerde Katz is?

Zolang er geen **gevalideerde** Katz bestaat, staat de bewoner standaard in categorie
**O**, en verschijnt er een herinnering « Katz te doen » op het dashboard. Valideer de
Katz om de juiste categorie aan de mutualiteit te melden.
→ [De Katz-evaluatie](residents/katz.md)

### Hoe registreer ik een Katz-verergering?

Verslechtert de toestand van de bewoner, voer dan een **nieuwe evaluatie** in met een
**reden van verergering**. Resthome bereidt dan de bijwerking van het zorgakkoord voor
(**Bijlage 10**): de reden wordt automatisch overgenomen, en de handtekening van de
clinicus vervolledigt het document.
→ [De Katz-evaluatie](residents/katz.md)

### Hoe verhuis ik een bewoner naar een andere kamer of transfereer ik MR ↔ MRS?

Gebruik op het **verblijf** de actie **Kamer wijzigen** (of **Interne transfer** voor
een wijziging van zorgtype), geef de nieuwe kamer/het nieuwe type en de datum/het uur
op, en klik op **Valideren**. Resthome splitst de facturatie op de juiste datum, aan
het overeenkomstige tarief; dit is geen nieuwe opname en de RIZIV-tussenkomst (het
forfait) blijft doorlopen.
→ [Kamerwissel en overdracht](residents/changement-chambre.md)

---

## Verzekerbaarheid (MDA)

### Wat is de MDA en waarvoor dient hij?

De **MDA** controleert of een bewoner **in orde is met de verzekerbaarheid** en
identificeert zijn **exacte ziekenfonds** door voor u **MyCareNet / WalCareNet** te
bevragen voor een bepaalde periode. Het is de onmisbare voorwaarde voor het verzenden
van eFact.
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

### Hoe controleer ik de MDA-verzekerbaarheid van een bewoner?

Maak een **MDA-aanvraag** aan (menu **eHealth → Verzekerbaarheid → MDA-aanvragen**)
met de bewoner, het vooraf ingevulde INSZ en de periode (standaard de lopende maand),
en klik op **Verzenden (Sync)**: de verzending gebeurt onmiddellijk en het antwoord
komt meteen terug. Raadpleeg vervolgens de samenvatting en de
verzekerbaarheidsperiodes.
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

### Hoe controleer ik meerdere bewoners tegelijk?

Start de controle **per lot**: selecteer de bewoners (u kunt een **kolom plakken** met
namen/INSZ), de periode, en verzend het volledige lot. Gebruik **Onmiddellijke
verzending (Sync)** voor kleine volumes, of **Groepsverzending (Async)** voor grote
maandelijkse loten — het antwoord haalt u daarna op met **Antwoorden controleren**
(vereist minstens 2 bewoners).
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

### Wanneer moet ik de MDA doen?

Doe de MDA **aan het begin van de maand**, vóór u de facturen genereert: zo vermijdt u
latere eFact-weigeringen door een verkeerd ziekenfonds of een verlies van
verzekerbaarheid.
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

### Wat betekent « verzekerd maar niet in orde »?

Komen de rechthebbendecodes terug op nul (verzekerd maar onbetaalde bijdragen /
probleemdossier), dan toont Resthome een **waarschuwing**: de bewoner is aangesloten
maar **niet in orde**. Dit moet met hem of zijn ziekenfonds uitgeklaard worden vóór u
aan de VI factureert.
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

### Wat werkt Resthome bij na een geslaagde MDA?

De bewonersfiche wordt automatisch gecorrigeerd: het **ziekenfonds (VI)** als het
afwijkt van het profiel, het **BIM/RVV-statuut** (verhoogde tegemoetkoming), het
**aansluitingsnummer**, de **identiteit** als er velden ontbraken, en de
**overlijdensdatum** als de VI die meldt. Voor bewoners onder een bijzonder stelsel
(INIG, EEG, Fedasil, buitenlands, privé…) **overschrijft** Resthome het ziekenfonds
van het profiel **niet**.
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

### Wat te doen bij een fout of het uitblijven van een MDA-antwoord?

Bij een antwoord « Zonder antwoord » van het platform gebruikt u **Zonder antwoord
opnieuw proberen**; blijft dit aanhouden, dan **Melden aan de intermut.** Bij een
weigering van de VI gebruikt u **Contact opnemen met de VI** (de reden wordt
getoond); bij een technische fout **Melden aan de intermut.**
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

### Wat is de herintegratie (verlies en daarna herstel van verzekerbaarheid)?

Resthome vergelijkt met de vorige controle: gaat een bewoner van **niet verzekerd naar
verzekerd**, dan verschijnt er een melding en verplaatst de actie **Herintegratie** de
lijnen die aan de bewoner waren gefactureerd naar de VI. Omgekeerd (**verzekerd → niet
verzekerd**) wordt zijn forfait uitgesloten van de VI-facturatie van de periode en aan
de bewoner gefactureerd tot het herstel.
→ [Verzekerbaarheid (MDA)](ehealth/mda.md)

---

## Akkoorden (eAgreement)

### Wat is de eAgreement?

Wanneer een bewoner binnenkomt, afwezig is, terugkeert of de instelling verlaat, moet
het ziekenfonds daarvan elektronisch op de hoogte gebracht worden. Resthome **bereidt
automatisch** de eHealth-melding voor die overeenstemt met uw actie; meestal hoeft u
niets extra in te voeren — enkel te controleren en, indien nodig, te verzenden.
→ [Akkoorden (eAgreement)](ehealth/eagreement.md)

### Wat is het verschil tussen eAgreement en eAgreement Light?

De **eAgreement** is het akkoord voor de tenlasteneming van de zorg (gekoppeld aan de
Katz-categorie en het forfait). De **eAgreement Light** groepeert de eenvoudigere
meldingen in verband met de **bewegingen** van de bewoner (opname, afwezigheid,
vertrek, terugkeer) — het zijn deze die Resthome vanzelf genereert naargelang uw
acties.
→ [Akkoorden (eAgreement)](ehealth/eagreement.md)

### Welk document wordt voorbereid naargelang de actie?

Een verblijf starten → **Opname-akkoord (Bijlage 7)**; een afwezigheid /
ziekenhuisopname registreren → **uittredingsmelding (Bijlage 11)**; terugkeer van de
bewoner → **heropname (Bijlage 7)**; gevalideerde Katz-verergering → **bijwerking van
het zorgakkoord (Bijlage 10)**; einde verblijf / overlijden → **uittredingsmelding
(Bijlage 11)**.
→ [Akkoorden (eAgreement)](ehealth/eagreement.md)

### Wat zijn de statussen van een akkoord, en wat te doen bij een weigering?

Een akkoord doorloopt **Concept** (voorbereid, niet verzonden), **Verzonden**,
**Aanvaard** en **Geweigerd** (met een reden). Bij een weigering toont Resthome de
**reden in klare taal, in het Nederlands en het Frans**, rechtstreeks op het akkoord —
zo weet u wat u moet corrigeren (vaak INSZ, ziekenfonds of datums) vóór u opnieuw
verzendt.
→ [Akkoorden (eAgreement)](ehealth/eagreement.md)

### Kan ik een beweging registreren zonder INSZ?

Zonder INSZ kan het akkoord niet verzonden worden. U kunt de beweging (opname,
afwezigheid…) toch registreren: Resthome noteert ze en nodigt u uit om het INSZ zo
snel mogelijk aan te vullen.
→ [Akkoorden (eAgreement)](ehealth/eagreement.md)

---

## Elektronische facturatie (eFact)

### Wat is eFact?

**eFact** is de **elektronische** verzending van het **ziekenfondsgedeelte** (het
RIZIV-forfait) naar de **verzekeringsinstellingen (VI)** via het
eHealth-/MyCareNet-netwerk. Resthome stelt de bestanden samen, verzendt ze en **volgt
de antwoorden op** — ontvangstbewijzen, afrekeningen, aanvaardingen en weigeringen.
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

### Wat zijn de statussen van een facturatieperiode?

Een periode doorloopt vier statussen, in volgorde: **Draft** (aangemaakt, niets
berekend), **Generated** (forfaits en gedeelten berekend, te controleren),
**Invoiced** (facturen geboekt, de eFact kan samengesteld en verzonden worden) en
**Closed** (afgewerkt en vergrendeld).
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

### Hoe genereer ik een eFact-periode?

Open de periode van de maand in de status **Draft** en klik op **Genereren**; laat in
de assistent **Residents** leeg voor alle actieve bewoners en klik op **MDA laden**, en
daarna op **Generate**. De periode gaat naar **Generated**: Resthome heeft voor elke
bewoner het Katz-forfait, het RIZIV-gedeelte en het bewonersgedeelte berekend.
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

### Hoe controleer ik een periode vóór ik factureer?

Bovenaan de periode geven tellers de gezondheidstoestand van de maand weer
(**Supplementen**, **Afwezigheden**, **Niet gefactureerd**, **MDA**, **Katz te doen**)
en signaleert Resthome de anomalieën in de discussiedraad rechts. Behandel elk punt
(knop **Klaar** zodra het geregeld is) vóór u factureert, en start **MDA controleren**
om de verzekerbaarheid na te gaan.
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

### Hoe genereer ik de eFact-loten?

Zodra de facturen geboekt zijn (periode **Invoiced**), klikt u op **eFact genereren**:
Resthome stelt de **loten** samen — één elektronisch bestand per verzekeringsinstelling
— en toont daarna de lijst **eFact-loten** (VI, referentie, maand, uiterste datum,
status, gefactureerde/aanvaarde/geweigerde bedragen, en code + reden bij weigering).
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

### Wat is een lot per unie?

De verzendingen worden gegroepeerd **per unie** (de grote VI-families), niet per kleine
afzonderlijke mutualiteit: **100** (Landsbond der Christelijke Mutualiteiten), **300**
(Solidaris), **500** (Landsbond van de Onafhankelijke Ziekenfondsen), **600**
(HZIV — CAAMI), **900** (HR Rail)… Resthome zorgt voor de groepering.
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

### Hoe verzend ik een eFact-periode en volg ik de antwoorden op?

Open **eHealth → eFact → Cockpit** (of de loten) en klik op **Alles verzenden** (of lot
per lot); de verzendingen vertrekken naar de ziekenfondsen via eHealth. Klik daarna op
**Antwoorden ophalen**: elk lot gaat **Verzonden → Ontvangst bevestigd → Aanvaard /
Geweigerd**, waarbij Resthome de aanvaarde/geweigerde bedragen automatisch afstemt.
→ [Een maand factureren, stap voor stap](facturation/facturer-un-mois.md) ·
[Elektronische facturatie (eFact)](ehealth/efact.md)

### Ik ontvang een ontvangstbewijs (931000) na de verzending, moet ik wachten?

**Ja.** De **931000** bevestigt enkel dat de verzekeringsinstelling het lot heeft
**ontvangen** en de eerste controle heeft doorstaan — het is niet het eindresultaat. U
hoeft **niets opnieuw te versturen**: wacht op de **afrekening (920900)**, die aangeeft
wat aanvaard en betaald wordt (enkele dagen). Ondertussen kunnen een **920098**
(waarschuwingen, toch aanvaard) of een **920099** (globale weigering, te corrigeren en
opnieuw te versturen) binnenkomen.
→ [Elektronische facturatie (eFact)](ehealth/efact.md) ·
[eFact-weigeringen](ehealth/efact-rejets.md)

### Waarom wordt een eFact-factuur geweigerd, en hoe corrigeer ik dit?

Wordt een lot (of een deel ervan) **geweigerd**, dan zeggen de **code** en de **reden
van weigering** u waarom (verzekerbaarheid, forfait, datums…). Corrigeer de oorzaak en
**verzend opnieuw**: de teller **Heruitzendingen** houdt de retransmissies bij om
dubbels te vermijden, en de knop **Herintegratie** laat in voorkomend geval toe om
lijnen in een nieuwe verzending te herintegreren.
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

### Wat betekent « termijn overschreden » op een periodekaart?

De **uiterste verzenddatum** van deze periode is **overschreden**. Verzend zonder
uitstel — daarna kunnen sommige verzekeringsinstellingen het lot weigeren.
→ [Elektronische facturatie (eFact)](ehealth/efact.md)

---

## Facturatie & supplementen

### Hoe factureer ik een maand van A tot Z?

Open de periode (**MR/MRS → Facturatie → Facturatieperiodes**), **Controleer de MDA**,
klik op **Genereren**, **Facturen aanmaken** en **Boek** vervolgens het
bewonersgedeelte, daarna **eFact genereren** en verzend het ziekenfondsgedeelte naar de
VI, en tot slot **Antwoorden ophalen**. Resthome voert het bewonersgedeelte (klassieke
facturen) en het ziekenfondsgedeelte (eFact) parallel op eenzelfde periode.
→ [Een maand factureren, stap voor stap](facturation/facturer-un-mois.md)

### Wat is anticipatieve facturatie?

Voor bewoners die op voorhand worden gefactureerd, wordt de **huisvesting** van een
maand de **voorgaande maand** gefactureerd, terwijl het **forfait** en de
**supplementen** op de prestatiemaand worden gefactureerd.
→ [Facturatie](facturation/index.md)

### Waarvoor dient de knop « Vernieuwen »?

Op een periode herberekent de actie **Vernieuwen** alles met één klik
(facturatielijnen, supplementen, conceptfacturen). Bewoners van wie de factuur al
geboekt is, blijven ongemoeid; aangezien het toevoegen van een supplement of een
afwezigheid automatisch synchroniseert, is het doorgaans niet nodig om op
« Vernieuwen » te klikken.
→ [Facturatie](facturation/index.md#de-knop-vernieuwen)

### Hoe voeg ik een supplement toe?

Open de **supplementenenveloppe** van de bewoner (vanaf zijn fiche of de periode), voeg
een lijn toe (product/prestatie, hoeveelheid, prijs), geef aan of het **eenmalig** (één
keer) of **terugkerend** (elke maand) is, en klik op **Opslaan**. Het toevoegen,
wijzigen of verwijderen werkt de factuur van de betrokken bewoner automatisch bij — u
hoeft niet op « Vernieuwen » te klikken.
→ [De supplementen](facturation/supplements.md)

### Hoe verdeel ik het bewonersgedeelte over meerdere debiteuren?

Open op de fiche van de bewoner (of zijn periode) het tabblad **verdeling**, voeg de
debiteuren en hun **percentage** toe (het totaal moet 100 % bedragen), en klik op
**Opslaan**. Bij elke maandfactuur verdeelt Resthome het bewonersgedeelte volgens deze
sleutel; enkel het bewonersgedeelte wordt verdeeld, niet het RIZIV-forfait (dat via de
eFact naar het ziekenfonds vertrekt).
→ [Onderhoudsplichtigen (gedeelde facturatie)](facturation/split-billing.md)

### Wat gebeurt er wanneer een factuur al geboekt is?

Eenmaal **geboekt** is de factuur van een bewoner **vergrendeld** voor die maand
(bescherming tegen dubbele facturatie). Om ze te corrigeren, zet u ze terug op
**concept** of maakt u een **creditnota**, en daarna **Vernieuwt** u; de andere
bewoners worden niet geraakt.
→ [Een maand factureren, stap voor stap](facturation/facturer-un-mois.md)

---

## Afwezigheden & ziekenhuisopnames

### Hoe registreer ik een afwezigheid of een ziekenhuisopname?

Open de facturatieperiode van de maand (of de fiche van de bewoner) en voeg een
**afwezigheid** toe met de bewoner, het **type** (ziekenhuisopname, vakantie…), de
**vertrekdatum/-uur** en de **terugkeerdatum/-uur** (of laat de terugkeer leeg zolang
hij niet terug is), en klik op **Opslaan**. Het toevoegen, wijzigen of verwijderen van
een afwezigheid synchroniseert automatisch de facturatie van de betrokken bewoner.
→ [Afwezigheden en ziekenhuisopnames](facturation/absences.md)

### Wat is het effect van een afwezigheid op het forfait?

Het **RIZIV-forfait** wordt berekend op de **aanwezigheidsdagen**; een afwezigheid
**vermindert** dit forfait voor de betrokken dagen. De afrekening volgt de
**« middagregel »** (uur van Brussel): het is de aanwezigheid om de middag die bepaalt
of de dag meetelt, vandaar het belang van de vertrek- en terugkeerdatums en -uren.
→ [Afwezigheden en ziekenhuisopnames](facturation/absences.md)

### Welke afwezigheden moeten aan het ziekenfonds gemeld worden?

Een afwezigheid van **meer dan 72 u**, of **elke ziekenhuisopname**, bereidt een
**Bijlage 11** voor (uittredingsmelding), en de **terugkeer** bereidt een **Bijlage 7**
voor (heropname). Resthome maakt deze meldingen aan op het ogenblik dat u de
afwezigheid en de terugkeer registreert; u hoeft ze enkel te controleren en te
verzenden.
→ [Afwezigheden en ziekenhuisopnames](facturation/absences.md)

### Hoe annuleer ik een per vergissing ingevoerde afwezigheid?

Verwijder ze of zet ze terug op concept: Resthome **draait dit netjes terug** — het
forfait wordt herberekend alsof de afwezigheid niet had plaatsgevonden, en de
voorbereide meldingen worden ingetrokken zolang ze niet aan de kant van het
ziekenfonds gevalideerd zijn. Is de maand al geboekt, zet dan eerst de factuur terug op
concept (of maak een creditnota) en vernieuw daarna.
→ [Afwezigheden en ziekenhuisopnames](facturation/absences.md)

---

## Vertrek & overlijden

### Wat gebeurt er bij het vertrek of het overlijden van een bewoner?

U hoeft enkel zijn **verblijf af te sluiten**: open de fiche → het verblijf, geef de
**uittredingsdatum** (en het uur) op met de **reden** (vertrek, overlijden, transfer…),
en klik op **Valideren**. Resthome stopt de facturatie op de juiste datum, bereidt de
regularisatie voor van wat op voorhand werd gefactureerd en meldt de uittrede aan het
ziekenfonds.
→ [Vertrek en overlijden](facturation/depart-deces.md)

### Waarom wordt er bij het vertrek een creditnota aangemaakt?

Aangezien de huisvesting **een maand op voorhand** wordt gefactureerd, bereidt Resthome,
als de bewoner tijdens een al gefactureerde maand vertrekt, **automatisch een
creditnota** voor om de niet-bezette periode terug te betalen (u wordt van de aanmaak
ervan op de hoogte gebracht). Het RIZIV-forfait en de supplementen worden wel op de
gepresteerde maand gefactureerd.
→ [Vertrek en overlijden](facturation/depart-deces.md)

### Kan ik een per vergissing afgesloten verblijf heropenen?

Ja. Hebt u een verblijf ten onrechte afgesloten (of een overlijden per vergissing
geregistreerd), dan kunt u het **heropenen**: Resthome herstelt de facturatie en
annuleert de regularisaties zolang ze niet definitief zijn. Is de maand al geboekt, dan
verloopt de correctie eerst via een terugzetting op concept of een creditnota, en
daarna een vernieuwing.
→ [Vertrek en overlijden](facturation/depart-deces.md)
