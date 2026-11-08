---
modules: [healthcare_accommodation_billing, resthome_sales, resthome_supplements]
---

# Billing

:::{rh-description}
Billing periods, the care allowance, supplements, absences, invoice types and invoices in Resthome.
:::

:::{toctree}
:hidden:

tableau-de-bord
checklist-fin-de-mois
facturer-un-mois
type-de-facture
supplements
application-supplements
refacturation-fournisseur
absences
depart-deces
indexation-des-prix
pont-comptable
:::

Resthome automates the billing of the home: the **insurer's share** (the care
allowance paid by the health insurer) and the **resident's share**
(accommodation + supplements), period by period.

## Key principles

- **Billing app**: its **dashboard** shows the months to bill, the invoices to
  validate and what is still unpaid.
- **Billing period**: one month. You **generate** it, then **invoice** it.
- **Invoice type**: each resident is billed **in advance** (anticipatory, the
  default) or **in arrears**. The type is set on the resident's contact and can
  change for one month only.
- **Care allowance**: calculated from the **dependency category** and days of
  presence; this is the share paid by the resident's health insurer.
- **Accommodation**: the share paid by the resident (the room), based on the rate.
- **Supplements**: one-time or recurring services (single room, TV,
  hairdresser…), through the resident's **supplements envelope**, at the price
  in force that month.
- **Absences**: an absence (hospitalisation, holidays) can **reduce the
  accommodation** through the absence discount rules and, where the country
  pack bills one, the care allowance.

:::{admonition} Anticipatory billing
:class: note

For residents billed in advance, one month's accommodation is invoiced
**the previous month**. The care allowance and supplements, however, are
invoiced in the month of service. See [Invoice type](type-de-facture.md).
:::

## The "Refresh" button

On a billing period, the **Refresh** action recalculates everything in one
click: billing lines, supplements and draft invoices. In the list of periods,
select several and use the gear menu → **Refresh**.

:::{admonition} Good to know
:class: tip

- Residents whose invoice is **already posted** are left untouched; everything
  else is recalculated. When a change reaches one of them, a **Corrections
  pending** banner appears on the period: **Refresh** creates the supplementary
  invoice or the credit note.
- Adding a supplement or an absence **synchronises automatically**: you
  generally don't need to click "Refresh".
:::

## The period cycle

1. **New period** (the month) — from the dashboard, **Months to bill**.
2. **Generate** the billing lines.
3. Check the residents' **insurability** with their health insurer, where the
   country pack bills a care allowance.
4. **Create the invoices** (resident's share).
5. **Post** the invoices, and send them to the accounting database when it is
   kept elsewhere.
6. **Send the insurer's share** to the health insurers — through the electronic
   exchanges with the health insurer, where the country has them — then track
   the responses.
7. **Close** the period.

:::{admonition} Step by step
:class: tip

Follow the detailed guide [Billing a month, step by step](facturer-un-mois.md),
and the [Month-end checklist](checklist-fin-de-mois.md).
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

The care allowance is the INAMI dependency allowance, set from the Katz
assessment and sent to the mutualities through eFact after an MDA insurability
check; absences and departures are notified through eAgreement. See
[Billing a month in Belgium](../belgique/facturation.md) and
[The billing journey](../belgique/parcours-facturation.md).
:::

## What's next

- [The billing dashboard](tableau-de-bord.md) — the month at a glance.
- [Billing a month, step by step](facturer-un-mois.md) — the complete month guide.
- [Month-end checklist](checklist-fin-de-mois.md) — everything a month-end
  requires, in order.
- [Invoice type](type-de-facture.md) — in advance or in arrears, for a stay or
  for one month.
- [Supplements](supplements.md) — supplements envelope, one-time or recurring.
- [The Supplements app](application-supplements.md) — entering supplements
  resident by resident or for several at once.
- [Recharging a vendor bill](refacturation-fournisseur.md) — passing a
  supplier's bill on to the residents.
- [Absences and hospitalisations](absences.md) — absence discount rules and
  their effect on the month.
- [Departure and death](depart-deces.md) — stopping billing, credit note for
  prepaid accommodation.
- [Price indexation](indexation-des-prix.md) — raising the prices from a date.
- [Pocket money](../argent-de-poche/index.md) — the money held for a resident.
- [Accounting bridge](pont-comptable.md) — sending the invoices to an
  accounting kept elsewhere.
- [Split billing](../facturation-partagee/index.md) — the resident's share divided
  among several debtors, one invoice each.
- [Managing a resident](../residents/gerer-un-resident.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
