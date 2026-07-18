# Billing

:::{rh-description}
Billing periods, INAMI packages, supplements, absences and invoices in Resthome.
:::

Resthome automates MR/MRS billing: the **insurer's share** (INAMI package)
and the **resident's share** (accommodation + supplements), period by period.

## Key principles

- **Billing period**: one month. You **generate** it, then **invoice** it.
- **INAMI package**: calculated from the **Katz category** and days of
  presence; this is the share reimbursed by the insurer.
- **Accommodation**: the share paid by the resident (the room), based on the rate.
- **Supplements**: one-off or recurring services (single room, TV,
  hairdresser…), through the resident's **supplements envelope**.
- **Absences**: an absence (hospitalisation, holidays) **reduces the package**
  for the period concerned and can trigger an eHealth notification.

:::{admonition} Anticipatory billing
:class: note

For residents billed in advance, one month's accommodation is invoiced
**the previous month**. The package and supplements, however, are invoiced in
the month of service.
:::

## The "Refresh" button

On a billing period, the **Refresh** action recalculates everything in one
click: billing lines, supplements and draft invoices.

:::{admonition} Good to know
:class: tip

- Residents whose invoice is **already posted** are left untouched; everything
  else is recalculated.
- Adding a supplement or an absence **synchronises automatically**: you
  generally don't need to click "Refresh".
:::

## The period cycle

1. **New period** (the month).
2. **Generate** the billing lines.
3. Check the residents' **insurability (MDA)**.
4. **Create the invoices** (resident's share).
5. **Post** the invoices.
6. **Generate the eFact** (insurer's share) then send it.

:::{admonition} Step by step
:class: tip

Follow the detailed guide [Invoicing a month, step by step](facturer-un-mois.md), or
see the whole [billing journey](../parcours-facturation.md).
:::

## What's next

- [Invoicing a month, step by step](facturer-un-mois.md) — the complete month guide.
- [The INAMI package (dependency)](forfait-inami.md) — Katz → category → invoiced amount.
- [Supplements](supplements.md) — supplements envelope, one-off or recurring.
- [Absences and hospitalisations](absences.md) — effect on the package, the
  72-hour rule, automatic eHealth notification.
- [Departure and death](depart-deces.md) — stopping billing, credit note for
  prepaid accommodation.
- [Maintenance debtors](split-billing.md) — split the resident's share between debtors.
- [Agreements (eAgreement)](../ehealth/eagreement.md) — notify the insurer
  (admission, absence, return, discharge).
- [eHealth](../ehealth/index.md) — sending the insurer's share (eFact) and agreements.
- [Managing a resident](../residents/gerer-un-resident.md)
- [The billing journey](../parcours-facturation.md) · [FAQ](../faq.md) · [Glossary](../glossaire.md)
