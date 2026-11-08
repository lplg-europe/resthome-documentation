---
modules: [l10n_health_be_serviced_living, l10n_health_be_serviced_living_perdiem]
sectors: [rs]
---

# Serviced residences in Belgium

:::{rh-description}
What the Belgian pack adds to a serviced residence (RS): the regional regimes, the operating title and fire certificate, the Katz asked at application, the health index, and a residence beside an MR/MRS.
:::

:::{rh-faq}
Does a serviced residence send anything to the mutualities?
: No. A resident of an RS is billed an ordinary monthly invoice: no MDA, no eAgreement, no eFact, no INAMI allowance.

Which regime should my residence choose?
: The one of the authority that licenses it: Wallonia (AViQ), Brussels (COCOM, Iriscare), Brussels (COCOF) or Flanders (Departement Zorg).

Must a resident of an RS have a Katz?
: No. A residence may ask for one at application, by its own house rules: tick **Katz at application** on the residence. It is off by default.

Where do I enter the health index?
: In **Serviced Living → Configuration → Health index**, one figure per month. A price change reads it to propose the index part.

How does a resident move from the RS to the MR?
: Through the internal transfer of the nursing home. See the page on moving between a serviced residence and the nursing home.
:::

The common pages of [Serviced residences](../residences-services/index.md)
describe the application in every country. This page gathers what the Belgian
pack adds. In Belgium the sector reads **RS** on badges and lists, as the MR,
the MRS and the CSJ do.

## The regional regimes

**Serviced Living → Configuration → Regimes** holds four ready-made sheets, one
per licensing authority:

| Regime | Authority | Price basis |
| --- | --- | --- |
| **Wallonia (AViQ)** | AViQ | Per month |
| **Brussels (COCOM, Iriscare)** | Iriscare | Per month |
| **Brussels (COCOF)** | COCOF | Per month |
| **Flanders (Departement Zorg)** | Departement Zorg | Per day |

Each sheet sets the entry age, the surfaces, the rules of the price and of its
increases, the deposit, the notices, the trial and withdrawal periods, the call
register, the council rhythm and the retention of the file. Its **Legal basis**
names the texts it was read from and what is still to confirm with the
authority. See [Regimes](../residences-services/regimes.md) for what each rule
does.

:::{admonition} Check your sheet
:class: warning

The sheets are a starting point read from the published texts, not a legal
opinion. Check the values with your authority, and change them on the sheet
when your title says otherwise.
:::

## The pieces of a Belgian file

The pack lists the usual pieces in **Serviced Living → Configuration → Pieces of
the file**: **Identity card**, **Medical certificate**, **Inventory of the
unit**, **Deposit account**, **What the price includes**, **Signed agreement**
and **House rules**. None is required by default: tick **Required to sign** on
the pieces your residence insists on before a signature.

## The operating title

The residence form gains an **Operating title** tab:

- **Operating title** — **Provisional** or **Definitive**;
- **Title number**, **Title granted on** and **Title valid until** — empty for a
  title without an end date;
- **Fire certificate valid until**;
- **Linked nursing home** — the nursing home the residence is tied to.

From 90 days before the title or the fire certificate ends, a warning shows at
the top of the residence.

<!-- screenshot to add: the Operating title tab of a residence, with the title, its dates and the fire certificate -->

## The Katz at application

Some residences ask for a Katz assessment at application, to check that the
person is independent enough. It is the residence's own rule, off by default.
The assessment is usually made outside the residence, by the person's doctor or
home nurse.

In the residence's **Application** tab:

- **Katz at application** — the contract cannot be signed without a validated
  Katz of each occupant;
- **Katz not older than (months)** — 6 by default; 0 accepts a Katz of any age;
- **Most dependent category** — above it, the contract shows a warning, and the
  signature stays possible.

A resident of an RS without a Katz shows no Katz button on their record, and the
residents list is not sorted by Katz category. See
[The Katz assessment](katz.md).

## The health index

**Serviced Living → Configuration → Health index** keeps the health index, one
line per month, typed in by hand. When you change the price of contracts, the
window proposes **Of which index (%)** from the move of the index since January
of that year. Without a figure, type the index part yourself. See
[Changing the price](../residences-services/changement-prix.md).

## A residence beside an MR/MRS

When the same database runs a nursing home (MR/MRS) or a day care centre and a
residence:

- **Admissions** — the request asks for the stay type first. **RS** shows the
  free units of the residence (for example *6/8 free*), and choosing it fills in
  the **Residence**; the quick-create card asks the same.
- **Billing** — the residents of the RS join the month's period beside the MR,
  MRS and CSJ residents. Their row and their lines show the unit and the
  contract, without Katz category, INAMI share or pseudo-code. See
  [Billing a residence](../residences-services/facturation.md).
- **eHealth** — the residents of the RS never enter the MDA, the eAgreement or
  eFact, and never count in the Katz or MDA alerts of the billing dashboard.
- **Dashboard** — the **Serviced living** lane shows once, with the main
  establishment.

Moving a resident between the RS and the MR or MRS goes through the internal
transfer: see [Moving between a serviced residence and the nursing
home](residences-services-maison-de-repos.md).

## Going further

- [Serviced residences](../residences-services/index.md)
- [Residences and units](../residences-services/residences-logements.md)
- [Contracts and occupants](../residences-services/contrats.md)
