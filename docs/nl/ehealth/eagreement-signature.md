---
title: Verantwoordelijke zorgverlener en ondertekening van de bijlagen
description: "Verantwoordelijke eAgreement-zorgverlener en ondertekening van Bijlagen 7/10/11 in een woonzorgcentrum (WZC/RVT): NIHII-resolutie en FEMARBEL-handtekening."
faq:
  - q: "Wie is de verantwoordelijke zorgverlener van een eAgreement-aanvraag?"
    a: "Dat is de clinicus die de Katz-evaluatie uitvoerde (de evaluator), niet degene die de aanvraag verstuurt — een medisch secretariaat mag ze gerust doorsturen. Resthome zet zijn persoonlijke NIHII op de aanvraag. Heeft hij geen NIHII, dan leent de aanvraag de identiteit van de hoofdverpleegkundige en daarna van de coördinerend arts, ingesteld in de eHealth-instellingen."
  - q: "Waar vul ik het NIHII en de handtekening van een zorgverlener in?"
    a: "Op zijn werknemersfiche (app Werknemers, tabblad Nursing Home). Het NIHII, de rol en de handtekeningafbeelding staan op de werknemer — niet op een gebruikersaccount — zodat zorgverleners die af en toe tekenen geen gebruikerslicentie verbruiken."
  - q: "Hoe onderteken ik een Bijlage 10, 7 of 11 zonder te printen of te scannen?"
    a: "Laad een handtekeningafbeelding op de werknemersfiche en klik daarna, op de eAgreement-aanvraag in Concept, op Sign Annexe 10 (of Sign Annexe 7 / Sign Annexe 11). Resthome plaatst uw handtekening op de PDF en markeert die als ondertekend. Is er geen afbeelding ingesteld, dan blijft de oude weg printen / tekenen / scannen mogelijk."
  - q: "Wie mag een Bijlage 10 ondertekenen (FEMARBEL-regels)?"
    a: "Standaard een arts OF een verpleegkundige. De handtekening van een arts wordt verplicht voor een Katz van categorie D (of Cd) en voor een snelle herziening (nieuwe evaluatie minder dan 6 maanden na de vorige). De Bijlagen 7 en 11 worden ondertekend door de verantwoordelijke van de instelling, zonder medische regel."
  - q: "Mag ik in de plaats van een collega tekenen?"
    a: "Nee, tenzij u eHealth-beheerdersrechten hebt. Ieder tekent met zijn eigen handtekeningafbeelding; tekenen namens een andere clinicus, wiens naam en rol op een wettelijke bijlage staan, vereist eHealth-beheerdersrechten. De werkelijke auteur blijft geregistreerd in het auditlogboek."
  - q: "Wat met een buitenlandse arts zonder Belgisch NIHII?"
    a: "Vink « Foreign physician (no Belgian NIHII) » aan op zijn werknemersfiche (enkel zichtbaar voor een arts). Resthome gebruikt dan het generieke nummer dat de eHealth-specificatie voorziet voor buitenlandse zorgverleners, dat de verzekeringsinstellingen aanvaarden."
---

# Verantwoordelijke zorgverlener en ondertekening van de bijlagen

Een [eAgreement](eagreement.md)-aanvraag moet een **verantwoordelijke
zorgverlener** aanduiden en een **handtekening** op de bijlagen dragen. Deze
pagina legt de twee mechanismen uit die Resthome hiervoor voorziet:

- **Wie geïdentificeerd wordt** als verantwoordelijke zorgverlener op de
  elektronische aanvraag — en hoe zijn **NIHII**-nummer automatisch bepaald wordt;
- **Hoe u ondertekent** — de **Bijlagen 7, 10 en 11** rechtstreeks in de app,
  vertrekkend van een opgeslagen **handtekeningafbeelding**, in plaats van te
  printen, tekenen en scannen.

De ondertekenknoppen verschijnen op de **eAgreement-aanvraag** (bereikbaar via de
fiche van de bewoner of de facturatieperiode). De identiteiten stelt u in op de
**werknemersfiche** en in de **eHealth-instellingen**.

!!! note "Twee identiteiten niet te verwarren"
    - **De verantwoordelijke zorgverlener**: de **elektronische** identiteit in de
      aanvraag die naar de mutualiteit gaat — de clinicus die de **Katz**-evaluatie
      uitvoerde. Resthome bepaalt die **automatisch** (zie verder).
    - **De ondertekenaar**: de persoon wiens **handtekeningafbeelding** op de
      **PDF** van de bijlage komt. Standaard bent dat **u** (de aangemelde
      gebruiker).

    Meestal vallen beide rollen samen, maar ze zijn verschillend: een secretariaat
    kan een aanvraag versturen waarvan de verantwoordelijke zorgverlener de
    verpleegkundige is die de Katz scoorde.

## De verantwoordelijke zorgverlener

De verantwoordelijke zorgverlener is de **clinicus die de
[Katz](../residents/katz.md)-evaluatie uitvoerde** — de evaluator —, **niet**
degene die de aanvraag verstuurt. Resthome bepaalt zijn **NIHII** via een
terugvalketen, om altijd een coherente identiteit naar de mutualiteit te sturen.

| Volgorde | Resthome neemt… | Wanneer |
|---|---|---|
| 1 | **De Katz-evaluator**, als hij een persoonlijk NIHII heeft | Normaal geval |
| 2 | **De hoofdverpleegkundige** ingesteld (zijn NIHII) | De evaluator (verpleegkundige, zorgkundige) heeft geen NIHII |
| 3 | **De coördinerend arts** ingesteld (zijn NIHII) | Noch de evaluator noch de hoofdverpleegkundige heeft een NIHII |
| 4 | Een **generiek AViQ-verpleegkundigennummer** | Laatste redmiddel, geen enkel NIHII beschikbaar |

!!! warning "Katz categorie D: een arts is verplicht"
    Voor een Katz van **categorie D** (of **Cd**) legt de specificatie een **arts**
    op als verantwoordelijke zorgverlener. Resthome neemt dan de evaluator als hij
    arts is (met NIHII), anders de ingestelde **coördinerend arts**. Is er geen
    arts beschikbaar, dan wordt de verzending **geblokkeerd** met een duidelijke
    melding: stel een coördinerend arts in bij de eHealth-instellingen.

!!! info "Het generieke nummer is een laatste redmiddel"
    Heeft niemand in de keten een bruikbaar NIHII, dan valt Resthome terug op het
    **generieke AViQ-verpleegkundigennummer**. Dat is een vangnet: voor een
    correcte identiteit vult u het persoonlijke NIHII van de zorgverlener in, of
    minstens een hoofdverpleegkundige en een coördinerend arts als terugval.

## Waar de identiteiten bewaard worden (werknemersfiche)

Het **NIHII**, de **rol** en de **handtekeningafbeelding** van een zorgverlener
staan op zijn **werknemersfiche**, niet op een gebruikersaccount. Zo verbruikt een
zorgverlener die af en toe een Bijlage 10 tekent **geen gebruikerslicentie**: het
volstaat dat hij als werknemer bestaat.

**App Werknemers → fiche van de werknemer → tabblad Nursing Home.**

| Veld | Waarvoor het dient |
|---|---|
| **INAMI Number** (NIHII/RIZIV-nr.) | Het persoonlijke NIHII van de zorgverlener, gebruikt als verantwoordelijke zorgverlener op de eAgreement-aanvraag. 11 cijfers. |
| **Care role** (zorgrol) | Het beroep (verpleegkundige, hoofdverpleegkundige, zorgkundige, arts…). Bepaalt de eHealth-rol. |
| **eHealth Role** (eHealth-rol) | Automatisch afgeleid uit de zorgrol: *nurse* (verpleegkundige / hoofdverpleegkundige / zorgkundige) of *physician* (arts). Alleen-lezen. |
| **Foreign physician (no Belgian NIHII)** (buitenlandse arts) | Aan te vinken voor een grensarts zonder Belgisch NIHII. Enkel zichtbaar voor een arts. |
| **Signature image (Annexe 10)** (handtekeningafbeelding) | De scan van de handtekening (PNG/JPG, bij voorkeur transparante achtergrond), op de PDF geplaatst bij het ondertekenen in de app. |

!!! tip "Een nette handtekeningafbeelding"
    Verkies een **PNG met transparante achtergrond**, bijgesneden op de lijn.
    Resthome plaatst ze in het vak « Handtekening » van de bijlage met **behoud van
    de verhoudingen** — een goed uitgeknipte afbeelding geeft een net resultaat.

## De terugval-identiteiten instellen

**Instellingen > Nursing Home > eAgreement Responsible Practitioner.** Deze twee
instellingen leveren het terugval-NIHII wanneer de Katz-evaluator het zijne niet
heeft.

| Instelling | Waarvoor het dient |
|---|---|
| **Head Nurse (NIHII fallback)** (hoofdverpleegkundige) | Zijn NIHII identificeert de verantwoordelijke zorgverlener wanneer de evaluator (verpleegkundige, zorgkundige) geen persoonlijk NIHII heeft. |
| **Coordinating Physician (NIHII fallback)** (coördinerend arts) | Terugval wanneer geen enkel verpleegkundigen-NIHII beschikbaar is, en **verplicht** voor een Katz van categorie D. |

Zie ook [eHealth- en eFact-instellingen](../configuration/reglages-ehealth.md).

!!! note "De Katz-categorie dient om te verklaren, niet om het bedrag te bepalen"
    Het **afhankelijkheidsforfait** bedraagt **hetzelfde bedrag** voor alle
    Katz-categorieën (AViQ-tarieven); de categorie dient om het **profiel** van de
    bewoner aan de mutualiteit te **verklaren**. Een categorie **D** legt evenwel
    een **arts** op als verantwoordelijke zorgverlener — vandaar het belang van de
    coördinerend arts als terugval.

## De buitenlandse arts

Een **grensarts** die **geen** Belgisch NIHII heeft, kan geen persoonlijk nummer
leveren. Vink op zijn werknemersfiche (rol *arts*) **Foreign physician (no Belgian
NIHII)** aan. Resthome zet dan het **generieke nummer dat de eHealth-specificatie
voorziet** voor buitenlandse zorgverleners op de aanvraag, dat de
verzekeringsinstellingen aanvaarden. U hoeft zelf geen nummer in te voeren.

## Een bijlage ondertekenen in de app

In plaats van te **printen, met de hand te tekenen en dan te scannen**, plaatst
Resthome uw **handtekeningafbeelding** op de PDF van de bijlage en bewaart die —
een werkwijze conform de **FEMARBEL**-regels. De betrokken bijlagen:

- **Bijlage 10** — de Katz-schaal (zorgakkoord);
- **Bijlage 7** — het opnameakkoord (opname / heropname);
- **Bijlage 11** — de melding van einde verblijf.

<!-- capture a ajouter : eAgreement-aanvraag in Concept met de knoppen Sign Annexe 10 / Sign Annexe 7 in de actiebalk -->

Het verloop, op een aanvraag in **Concept**:

1. **Genereer de bijlage** als dat nog niet gebeurd is (Bijlage 10 komt uit de
   Katz; Bijlage 7 of 11 vanuit de aanvraag).
2. Klik op **Sign Annexe 10** (of **Sign Annexe 7** / **Sign Annexe 11**). Deze
   knoppen verschijnen enkel in Concept, wanneer de bijlage bestaat en **nog niet
   ondertekend** is.
3. Controleer in het venster **Sign annex** de **Signer** (ondertekenaar,
   standaard uzelf), zijn **rol**, de **handtekeningdatum** en het **voorbeeld** van
   de handtekening.
4. Klik op **Sign & replace PDF**. Resthome genereert een propere PDF, plaatst de
   handtekening en vinkt de bijlage als **ondertekend** (een groen ✓ « Signed »
   verschijnt naast de bijlage).

!!! tip "De handtekening is een voorwaarde om te versturen"
    Zolang een gegenereerde bijlage **niet ondertekend** is, blijft de knop **Send
    Request** verborgen. Onderteken eerst alle bijlagen en verstuur dan.
    Opnieuw tekenen is risicoloos: Resthome vertrekt telkens van een blanco PDF en
    stapelt geen handtekeningen.

!!! note "Katz al ondertekend bij de evaluatie"
    Werd de Katz-evaluatie **in de app ondertekend** op het moment van de scoring,
    dan draagt de PDF van Bijlage 10 de handtekening al: Resthome markeert ze
    **automatisch** als ondertekend en bovenstaande stap is niet nodig.

### Wie mag ondertekenen (FEMARBEL-regels)

| Situatie | Toegelaten ondertekenaar |
|---|---|
| Bijlage 10 — standaardgeval | **Arts OF verpleegkundige** |
| Bijlage 10 — Katz **categorie D / Cd** | **Arts verplicht** (geen verpleegkundige-terugval) |
| Bijlage 10 — **snelle herziening** (nieuwe Katz < 6 maanden na de vorige) | **Arts verplicht** |
| Bijlage 7 (opname) / Bijlage 11 (einde verblijf) | **Verantwoordelijke van de instelling** — geen medische regel |

Het ondertekenvenster herinnert aan de toepasselijke regel in een banner
**FEMARBEL signature rules**. Vereist de regel een arts en is de ondertekenaar er
geen, dan wordt de handtekening geweigerd met een duidelijke melding.

!!! info "Heropname na een lange afwezigheid"
    Een **heropname** na meer dan 30 dagen afwezigheid kan een **nieuwe
    Katz-evaluatie** vergen, maar legt **geen** arts op: Bijlage 10 mag door een
    **arts OF een verpleegkundige** ondertekend worden.

### Ieder tekent met zijn eigen handtekening

Uit veiligheid kunt u enkel tekenen **met uw eigen** handtekeningafbeelding.
Tekenen **namens een ander** clinicus — wiens naam en rol op een wettelijke
bijlage naar de mutualiteit gaan — vereist **eHealth-beheerdersrechten**. In alle
gevallen blijft de **werkelijke auteur** van de handeling geregistreerd in het
auditlogboek.

### Als er geen handtekeningafbeelding is ingesteld

Heeft de ondertekenaar **geen** handtekeningafbeelding op zijn werknemersfiche,
dan waarschuwt het venster u en wordt de knop **Sign & replace PDF** niet
aangeboden. Twee opties:

- **een handtekeningafbeelding laden** op de werknemersfiche en opnieuw beginnen;
- **de manuele weg behouden**: de bijlage printen, laten tekenen, het ondertekende
  document scannen en opnieuw op de aanvraag laden (vink voor Bijlage 7 / 11
  daarna **Annex signed** aan).

## Belangrijkste punten om te onthouden

- De **verantwoordelijke zorgverlener** is de **Katz-evaluator**, niet de
  verzender; Resthome bepaalt zijn **NIHII** in cascade: evaluator →
  hoofdverpleegkundige → coördinerend arts → generiek nummer.
- Een Katz van **categorie D** legt een **arts** op; stel een **coördinerend arts**
  als terugval in bij de eHealth-instellingen.
- Het **NIHII**, de **rol** en de **handtekeningafbeelding** staan op de
  **werknemersfiche** (tabblad *Nursing Home*) — geen gebruikerslicentie nodig
  voor zorgverleners die af en toe tekenen.
- **Sign Annexe 10 / 7 / 11** plaatst uw handtekeningafbeelding op de PDF: geen
  printen / tekenen / scannen meer. Tekenen is een **voorwaarde om te versturen**.
- **FEMARBEL**-regels: standaard arts OF verpleegkundige; **arts verplicht** bij
  categorie D of snelle herziening (< 6 maanden).
- Men tekent enkel **met de eigen** handtekening, tenzij met
  **eHealth-beheerdersrechten**.

## Meer weten

- [Akkoorden (eAgreement)](eagreement.md)
- [Geweigerd akkoord (eAgreement) — oorzaken en oplossingen](eagreement-refus.md)
- [De afhankelijkheidsschaal (Katz)](../residents/katz.md)
- [eHealth- en eFact-instellingen](../configuration/reglages-ehealth.md)
- [eHealth-overzicht](index.md)
