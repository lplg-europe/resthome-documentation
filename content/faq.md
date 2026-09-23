---
modules: []
---

# FAQ — Frequently Asked Questions

:::{rh-description}
Short answers to frequently asked questions about Resthome: getting started, residents and stays, billing periods, supplements, absences, departure and death.
:::

:::{rh-faq}
How do I invoice a month from A to Z in Resthome?
: Open the month's billing period, click Generate, check it, click Create invoices then post the resident share. Where the country pays a care allowance through the health insurer, its share is sent from the same period, in parallel.

How do I record an absence or a hospitalisation?
: Open the month's period (or the resident file) and add an absence, giving the type, the departure and return date/time, then Save. The resident's billing synchronises automatically; the care allowance is reduced for the absence days according to the country's day-counting rule.

What happens when a resident departs or dies?
: Close their stay, giving the exit date and the reason (departure, death, transfer). Resthome stops the billing on the right date, prepares the credit note for the accommodation invoiced in advance and, where the country requires it, notifies the exit to the health insurer.

What is anticipatory billing in Resthome?
: For residents invoiced in advance, one month's accommodation is invoiced the previous month, while the care allowance and the supplements are invoiced in the month they are provided.

How do I add a supplement to a resident?
: Open the resident's supplement envelope, add a line (product/service, quantity, price), state whether the supplement is one-off or recurring, then Save. Adding it automatically updates the invoice of the resident concerned.

What are the states of a billing period?
: Draft (created, nothing computed), Generated (amounts computed, to be checked), Invoiced (invoices posted) and Closed (finished and locked).
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

The questions on the Katz, the NISS, insurability (MDA), agreements
(eAgreement), electronic invoicing (eFact), the INAMI allowance and the annexes
are gathered in [FAQ — Belgium](belgique/faq.md).
:::

This page gathers short answers to the most common questions, valid in every
country. Each answer links to the documentation page that details it.

---

## Getting started

### How do I log in to Resthome?

Open your browser at the address provided by your institution, enter your email
address and your password, then click **Log in**. If you forget it, use the
"Reset password" link or ask your administrator.
→ [Getting started](premiers-pas.md)

### What are the Resthome applications?

Resthome is organised into applications reachable from the main menu (the grid
icon): **Nursing Home** (residents, stays, billing,
dependency assessments), **Care** (prescriptions, care plans, vital signs),
**Meals** (menus, diets, family portal) and **Configuration** (rooms, rates,
master data). Depending on your role, you only see the applications that
concern you.
→ [Getting started](premiers-pas.md)

### What is the dashboard for?

The dashboard gives an overview: the pending tasks (assessments to do, checks
to run, sendings to follow…), clickable counters that open the relevant list
directly, and the month's important alerts. Click a counter to open the list of
items to handle.
→ [Getting started](premiers-pas.md)

### Where do I configure the rooms and rates?

In the **Configuration** application: create your rooms with their type (the
sector they belong to, single, double…) and equipment, define the
**accommodation rates** and, where the country pays one, the care allowance
rates, then the supplement types and the health insurers. Resthome also handles
**multiple companies** in the same database, each with its own residents, rooms
and billing kept separate.
→ [Configuration](configuration/index.md)

---

## Residents & stays

### How do I create a resident?

Open **Residents**, click **New**, fill in at least the name, the date of birth,
the gender and the **national identification number** if known, select the
resident's health insurer, then **Save**. Without the national identification
number, the electronic exchanges with the health insurer, where the country has
them, cannot be sent — but you can create the resident and complete the number
later.
→ [Managing a resident](residents/gerer-un-resident.md)

### How do I start a stay?

Open a **stay agreement** (room, stay type, start date) — the stay is then in
**Draft**. **Confirm** it (the room is reserved, complete the admission
date/time), then click **Start Stay**: the stay moves to **In Progress**.
→ [Managing a resident](residents/gerer-un-resident.md)

### What does starting a stay trigger automatically?

On start, Resthome adds the resident to the open billing periods, creates (for a
resident invoiced in advance) the first accommodation invoice for the admission
month and opens the month's supplement envelope. Where the country requires it,
it also prepares the admission notification to the health insurer.
→ [Managing a resident](residents/gerer-un-resident.md)

### How is a resident's dependency assessed?

Each country has its own dependency scale. The assessment is recorded on the
resident's file; it gives the **dependency category**, which drives the care
allowance where the country pays one. As long as no assessment is validated,
the resident keeps the country's default category and a reminder appears on the
dashboard.
→ [Managing a resident](residents/gerer-un-resident.md)

### How do I change a resident's room or sector?

On the **stay**, use the **Change Room** action (or **Internal Transfer** for a
change of sector), give the new room / the new sector and the date/time, then
**Validate**. Resthome splits the billing on the right date, at the matching
rate; this is not a new admission and the care allowance stays continuous.
→ [Room change and transfer](residents/changement-chambre.md)

### Does Resthome exchange data electronically with the health insurer?

Where the country has them, yes: the insurability check, the notifications of
the resident's movements and the electronic invoicing of the care allowance are
prepared and sent from the resident's file and the billing period. Each country
space describes its own exchanges.

---

## Billing & supplements

### How do I invoice a month from A to Z?

Open the billing period, click **Generate**, check it, click **Create
invoices** then **Post** the resident share. Where the country pays a care
allowance through the health insurer, its share is sent from the same period:
Resthome runs the resident share and the insurer share in parallel.
→ [Invoice a month, step by step](facturation/facturer-un-mois.md)

### What are the states of a billing period?

A period goes through four states, in order: **Draft** (created, nothing
computed), **Generated** (allowances and shares computed, to be checked),
**Invoiced** (invoices posted) and **Closed** (finished and locked).
→ [Invoice a month, step by step](facturation/facturer-un-mois.md)

### How do I check a period before invoicing?

At the top of the period, counters give the health state of the month
(**Supplements**, **Absences**, **Not invoiced**…) and Resthome flags anomalies
in the discussion thread on the right. Handle each point (**Done** button once
settled) before invoicing.
→ [Invoice a month, step by step](facturation/facturer-un-mois.md)

### What is anticipatory billing?

For residents invoiced in advance, one month's **accommodation** is invoiced
**the previous month**, while the **care allowance** and the **supplements**
are invoiced in the month they are provided.
→ [Billing](facturation/index.md)

### What is the "Refresh" button for?

On a period, the **Refresh** action recomputes everything in one click (billing
lines, supplements, draft invoices). Residents whose invoice is already posted
are left untouched; since adding a supplement or an absence synchronises
automatically, it is usually not necessary to click "Refresh".
→ [Billing](facturation/index.md)

### How do I add a supplement?

Open the resident's **supplement envelope** (from their file or the period), add
a line (product/service, quantity, price), state whether it is **one-off**
(once) or **recurring** (every month), then **Save**. Adding, editing or
removing it automatically updates the invoice of the resident concerned — no
need to click "Refresh".
→ [The supplements](facturation/supplements.md)

### How do I split the resident share across several debtors?

On the resident file (or their period), open the **split** tab, add the debtors
and their **percentage** (the total must be 100%), then **Save**. On each
monthly invoice, Resthome splits the resident share according to this key; only
the resident share is split, not the care allowance paid by the health insurer.
→ [Support debtors (split billing)](facturation-partagee/index.md)

### What happens when an invoice is already posted?

Once **posted**, a resident's invoice is **locked** for that month (protection
against double invoicing). To correct it, reset it to **draft** or make a
**credit note**, then **Refresh**; the other residents are not affected.
→ [Invoice a month, step by step](facturation/facturer-un-mois.md)

---

## Absences & hospitalisations

### How do I record an absence or a hospitalisation?

Open the month's billing period (or the resident file) and add an **absence**,
giving the resident, the **type** (hospitalisation, holidays…), the **departure
date/time** and the **return date/time** (or leave the return empty as long as
they have not come back), then **Save**. Adding, editing or deleting an absence
automatically synchronises the billing of the resident concerned. Where the
country requires it, Resthome also prepares the notification to the health
insurer; you only have to check and send it.
→ [Absences and hospitalisations](facturation/absences.md)

### What is the effect of an absence on the care allowance?

Where the country pays a care allowance, it is computed on the **presence
days**; an absence **reduces** it for the days concerned. The country's
day-counting rule decides whether a day counts, hence the importance of the
departure and return dates and times.
→ [Absences and hospitalisations](facturation/absences.md)

### How do I cancel an absence entered by mistake?

Delete it or reset it to draft: Resthome **cleanly rolls back** — the allowance
is recomputed as if the absence had not happened, and the prepared notifications
are withdrawn as long as they have not been validated on the insurer's side. If
the month is already posted, first reset the invoice to draft (or create a
credit note) then refresh.
→ [Absences and hospitalisations](facturation/absences.md)

---

## Departure & death

### What happens when a resident departs or dies?

Simply **close their stay**: open the file → the stay, give the **exit date**
(and time) with the **reason** (departure, death, transfer…), then **Validate**.
Resthome stops the billing on the right date, prepares the regularisation of
what was invoiced in advance and, where the country requires it, notifies the
exit to the health insurer.
→ [Departure and death](facturation/depart-deces.md)

### Why is a credit note created on departure?

Since the accommodation is invoiced **one month in advance**, if the resident
leaves during an already invoiced month, Resthome **automatically prepares a
credit note** to refund the unoccupied period (you are notified of its
creation). The care allowance and the supplements, however, are invoiced in the
month they are provided.
→ [Departure and death](facturation/depart-deces.md)

### Can a stay closed by mistake be reopened?

Yes. If you closed a stay wrongly (or in the case of a death recorded by
mistake), you can **reopen** it: Resthome restores the billing and cancels the
regularisations as long as they are not final. If the month is already posted,
the correction first goes through a reset to draft or a credit note, then a
refresh.
→ [Departure and death](facturation/depart-deces.md)
