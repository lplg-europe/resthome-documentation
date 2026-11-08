---
modules: [healthcare_accommodation_billing]
---

# The billing dashboard

:::{rh-description}
The home page of the Billing app: the months waiting for a step, the money flow from invoice to bank, arrivals and departures of the month, and shortcuts.
:::

:::{rh-faq}
What does the Billing app open on?
: On its dashboard: the months still waiting for a step, the accommodation invoices from draft to bank, and buttons to the billing periods, absences and supplements.

How do I create a billing period from the dashboard?
: Click the + (New) button and choose Billing period. You can also click New in the list of billing periods.

What does the badge on Billing periods count?
: The months still waiting for something: to generate, to invoice or to close. A closed month is not counted.

Why are "Paid, not on the bank yet" and "On the bank account" separate?
: Because a registered payment is not money received yet. An invoice moves to "On the bank account" only once its payment meets the bank statement line.
:::

The **Billing** app opens on a dashboard that answers the question of the day:
which month needs something, and where the money stands.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The app is called **MR/MRS Billing**, and the dashboard adds the health insurers' cards:
the eFact Cockpit, what is still to invoice to the mutualities, the
insurability checks and the eAgreement requests. See
[Billing a month in Belgium](../belgique/facturation.md).
:::

<!-- screenshot to add: the Billing dashboard with the buttons next to the title and the Accommodation billing figures -->

## The buttons next to the title

- **Billing periods** — one card per month, each with the button of the step
  it is waiting for (**Generate the period**, **Create the invoices**,
  **Close the period**). Its badge counts the months still waiting for a step.
- **Absences** — the list of absences.
- **Resident supplements** — the recurring supplements of all residents.

The **Billing Lines** list is in the menu: **Billing → Facturation → Billing
Lines**.

## Accommodation billing

A row of figures follows the residents' invoices, step by step. Each figure
opens the invoices behind it.

| Figure | What it counts |
|---|---|
| **Months to bill** | The billing periods waiting for a step. |
| **Invoices to validate** | Resident invoices still in draft. |
| **Invoiced, not yet due** | Posted, unpaid, due date not passed. |
| **Overdue** | Posted, unpaid, due date passed. |
| **Paid, not on the bank yet** | A payment is registered, not yet matched with the bank statement. |
| **On the bank account** | The amount actually received. |

These figures cover what the residents and their debtors are billed. Where
a country bills the health insurer, its flow has a row of its own.

## Create in one click

The **+** (**New**) button offers the three things entered during a month:

- **Absence**;
- **Resident supplement**;
- **Billing period** — the month to open.

## The side panel

The button on the left of the title opens a side panel:

- **The months** — the last six billing periods, with the step each one is
  waiting for. A click opens the period.
- **Arrivals and departures this month** — who came in and who left, with the
  date and the reason. These are the stays that make a month's lines prorated:
  read them before generating. A room change is not listed.
- Shortcuts: **Unpaid invoices** (with their number) and, for managers,
  **Billing rates**, **Supplement types** and **Absence discount rules**.

## Going further

- [Billing a month, step by step](facturer-un-mois.md)
- [Month-end checklist](checklist-fin-de-mois.md)
- [Billing overview](index.md)
