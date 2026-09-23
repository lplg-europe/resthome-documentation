---
modules: [healthcare_accommodation_billing, resthome_sales]
---

# Billing

:::{rh-description}
Billing periods, the care allowance, supplements, absences and invoices in Resthome.
:::

:::{toctree}
:hidden:

checklist-fin-de-mois
facturer-un-mois
supplements
application-supplements
refacturation-fournisseur
absences
depart-deces
:::

Resthome automates the billing of the home: the **insurer's share** (the care
allowance paid by the health insurer) and the **resident's share**
(accommodation + supplements), period by period.

## Key principles

- **Billing period**: one month. You **generate** it, then **invoice** it.
- **Care allowance**: calculated from the **dependency category** and days of
  presence; this is the share paid by the resident's health insurer.
- **Accommodation**: the share paid by the resident (the room), based on the rate.
- **Supplements**: one-off or recurring services (single room, TV,
  hairdresser…), through the resident's **supplements envelope**.
- **Absences**: an absence (hospitalisation, holidays) **reduces the care
  allowance** for the period concerned and can trigger a notification to the
  health insurer.

:::{admonition} Anticipatory billing
:class: note

For residents billed in advance, one month's accommodation is invoiced
**the previous month**. The care allowance and supplements, however, are
invoiced in the month of service.
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
3. Check the residents' **insurability** with their health insurer.
4. **Create the invoices** (resident's share).
5. **Post** the invoices.
6. **Send the insurer's share** to the health insurers — through the electronic
   exchanges with the health insurer, where the country has them — then track
   the responses.

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

- [Billing a month, step by step](facturer-un-mois.md) — the complete month guide.
- [Month-end checklist](checklist-fin-de-mois.md) — everything a month-end
  requires, in order.
- [Supplements](supplements.md) — supplements envelope, one-off or recurring.
- [Absences and hospitalisations](absences.md) — effect on the care allowance,
  notification to the health insurer.
- [Departure and death](depart-deces.md) — stopping billing, credit note for
  prepaid accommodation.
- [Split billing](../facturation-partagee/index.md) — the resident's share divided
  among several debtors, one invoice each.
- [Managing a resident](../residents/gerer-un-resident.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
