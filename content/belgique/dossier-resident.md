---
modules: [l10n_health_be, l10n_health_be_eid, resthome_mr_billing, l10n_health_be_perdiem_ehealth, resthome_mr_ehealth, l10n_health_be_mda, resthome_geriatric_be]
---

# The resident's file in Belgium

:::{rh-description}
What the Belgian pack adds to the resident's file in Resthome: the NISS and the eID reading, the mutualité (OA), the MR, MRS and short-stay sectors, the Katz category and the annexes at admission and transfer.
:::

:::{rh-faq}
Is the NISS mandatory to create a resident?
: No. You can create a resident without a NISS, but insurability checks (MDA) and agreements (eAgreement) cannot be sent without it, so fill it in as soon as possible.

What is a BIS number?
: The number the Crossroads Bank issues to someone who is not in the National Register — a cross-border worker, a person under MediPrima. It has the NISS shape, with the birth month shifted by 20 or 40, and eHealth accepts it where a NISS is asked. Resthome recognises it and shows it in the NISS type field.

How do I fill in the identity from the eID card?
: With a card reader connected to the workstation, read the card from the resident's record to update it, or use the New Partner via eID menu entry: Resthome looks the person up by NISS and creates the record if it does not exist yet.

What does Resthome do automatically when a stay starts?
: On top of the billing steps common to every country, it creates the admission eAgreement (Annexe 7) when the NISS is present.

Is a short stay (court séjour) a sector?
: No. It is a modality of an MR bed: tick Short stay on an MR stay, or choose CS at admission. Resthome refuses the short-stay flag on an MRS stay.

What happens if the resident has no validated Katz assessment?
: The resident stays in category O by default and a "Katz to do" reminder appears on the dashboard, since the Katz category is what is declared to the mutualité for the INAMI allowance.
:::

In Belgium, the resident's file carries what the health insurers and eHealth
need: the **NISS**, the **mutualité**, the **sector** of the stay (MR, MRS) and
the **Katz category**. This page gathers what the Belgian pack adds to the
country-neutral record described in [Manage a resident](../residents/gerer-un-resident.md).

## The NISS

The **NISS** field holds the resident's national number: **11 digits** from the
National Register, in the format `YYMMDD-XXX-CC`. It is also a search key: you
can find a resident by typing their NISS.

- **National number** — a birth month from 01 to 12.
- **BIS number** — issued by the Crossroads Bank to someone who is not in the
  National Register (month shifted by 20 or 40). Every eHealth service accepts
  it where a NISS is asked; a BIS holder usually has no mutualité.
- **Not a valid number** — the **NISS type** field flags a number that has
  neither shape.

:::{admonition} The NISS is required for eHealth
:class: warning

Without a NISS, insurability verification (MDA) and agreements (eAgreement)
cannot be sent. You can create the resident without a NISS, but remember to fill
it in as soon as possible.
:::

The NISS identifies the **person** for life; the **ID Card Number** identifies
the **card**, which expires and is renewed. The admission file keeps both.

### Reading the eID card

Rather than typing the identity in, you can **read the resident's eID card**.
Resthome fills in the name, the date of birth, the gender and the **NISS** from
the card itself — no typo, no transposed digit.

- From an **existing record**, the eID reading **updates** that resident.
- From the **New Partner via eID** menu entry, Resthome looks the person up by
  NISS and **creates** the record if it does not exist yet.

A card reader must be connected to the workstation.

## The mutualité (OA)

The **Health Insurance** field points at the resident's **mutualité** — the
federation, not one of its local contacts. Around it, the record keeps:

| Field | Purpose |
| --- | --- |
| **Code OA** | The 3-digit INAMI code of the mutualité: 1xx CM, 3xx Solidaris, 5xx MLOZ, 6xx CAAMI, 9xx HR Rail. |
| **Insurance Member Code** | The resident's membership number with the mutualité. |
| **Holder Code** | The holder's code for billing, when it differs. |
| **BIM Status** | Beneficiary of increased intervention. |
| **Insurance Regime** | **Standard** (Belgian mutualité), **INIG** (war invalid), **CEE** (European institution), **Fedasil** (asylum seeker), **Foreign / cross-border**, **Private insurance / revalidation**. |

:::{admonition} Special insurance regimes
:class: note

A resident under a non-standard **Insurance Regime** is left out of the MDA
batches, and MDA never overwrites their **Health Insurance**: MyCareNet would
otherwise return a standard Belgian mutualité for a resident actually covered by
INIG, CEE or Fedasil.
:::

### Checking insurability (MDA)

Before billing, check that the resident is properly insured:

1. Open the month's billing period, or the resident record.
2. Run an **MDA check** (MyCareNet/WalCareNet insurability).
3. Resthome automatically updates the **Health Insurance** and the **BIM
   Status** where applicable.

See [Insurability (MDA)](ehealth/mda.md). When a **CPAS** pays for the resident,
the invoice can be addressed to it — see [CPAS coverage](cpas.md).

## The sectors: MR, MRS and short stay

The **Stay Type** of a Belgian stay is the sector the home is accredited for:

- **MR** — maison de repos;
- **MRS** — maison de repos et de soins, which only takes Katz categories **B
  and above**;
- the day care centre (CSJ), when the home runs one — see
  [Day care centre (CSJ)](centre-de-jour/index.md).

A **short stay** (court séjour, 90 days at most) is not a sector: it is a
modality of an **MR** bed, carried by the **Short stay** box. At admission,
Resthome offers it as **CS** beside MR and MRS, and turns it into an MR stay
with the flag ticked. It has its own AViQ pseudo-codes (123214 to 123516), its
own forfait, and the "Court Séjour OUI" toggle on the Annexe 7. Resthome refuses
the flag on any other sector.

:::{admonition} MRS and the Katz category
:class: warning

Resthome refuses to **put or keep a stay in MRS** for a resident assessed at O
or A — at admission and at transfer time. A room change is not blocked; the
banner on the record and the **MRS → MR** badge flag the resident until the
transfer is entered — see [The Katz assessment](katz.md).
:::

## The Katz category on the record

The resident's record shows the **Katz category** (O, A, B, C, Cd) as a badge,
next to the stay type. It is the category declared to the mutualité for the
INAMI dependency allowance.

As long as no validated Katz exists, the resident is in category **O** by
default, and a "Katz to do" reminder appears on the dashboard. Scoring,
renewal and worsening are described in [The Katz assessment](katz.md); the
allowance itself in [The INAMI dependency allowance](forfait-inami.md).

Validated assessments — Katz and the geriatric scales alike — cannot be deleted:
health data must be retained under the GDPR and the INAMI rules.

## Annexes at admission and transfer

The stay has two dates. The **stay start date** starts the accommodation
billing; the **Admission Date** is the start of the **INAMI intervention** — the
"date d'entrée" of the Annexe 7, from which the forfait is paid.

| Event | What Resthome prepares for the mutualité |
| --- | --- |
| **Start of the stay** | The **admission eAgreement** (Annexe 7), when the NISS is present. |
| **Room change** | Nothing: the INAMI intervention stays continuous, the Admission Date is unchanged, no new agreement is requested. |
| **Internal transfer (MR ↔ MRS)** | An end-of-stay notice (**Annexe 11**) then a new request (**Annexe 7**); the Admission Date moves to the transfer date. |
| **Worsening of dependency** | The agreement update (**Annexe 10**), with the new Katz assessment. |
| **Absence / hospitalization** | The forfait is adjusted, and an eHealth notification (**Annexe 11**) can be generated. |

The **Stay Type** is read-only once the stay is confirmed: a bare edit would
produce no document for the mutualité. The **Internal Transfer** button is the
only way to change sector — see [Internal transfer (MR ↔ MRS)](ehealth/eagreement-transfert.md).

## What's next

- [The Katz assessment](katz.md) — scoring, category and renewal.
- [Insurability (MDA)](ehealth/mda.md)
- [Agreements (eAgreement)](ehealth/eagreement.md)
- [Internal transfer (MR ↔ MRS)](ehealth/eagreement-transfert.md)
- [The INAMI dependency allowance](forfait-inami.md)
- [The billing journey](parcours-facturation.md)
- [Manage a resident](../residents/gerer-un-resident.md)
