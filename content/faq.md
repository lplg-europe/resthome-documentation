# FAQ — Frequently Asked Questions

:::{rh-description}
Short answers to frequently asked questions about Resthome: getting started, residents, Katz, MDA, eAgreement, eFact, billing, departure and death.
:::

:::{rh-faq}
How do I check a resident's insurability (MDA)?
: Create an MDA request (eHealth → Insurability → MDA Requests) with the resident, the pre-filled NISS and the period, then click Send (Sync): the response comes back immediately. Do it at the start of the month, before invoicing, to avoid eFact rejections.

How do I generate an eFact period?
: Open the month's period in Draft state, click Generate, leave Residents empty for all active residents, click Load MDA then Generate. The period moves to Generated: the Katz allowance, the INAMI share and the resident share are computed for each resident.

How do I send an eFact period and follow the responses?
: From the eFact Cockpit or the batches, click Send all: the batches go to the mutualities through eHealth. Then click Get responses; each batch moves Sent → Acknowledged → Accepted / Rejected, with Resthome reconciling the amounts automatically.

Why is an eFact invoice rejected, and how do I fix it?
: The rejection code and reason state the cause (insurability, allowance, dates). Fix it then resend; the Resends counter avoids duplicates and the Reintegration button lets you reintegrate lines into a new sending.

What is an eFact batch per union?
: Sendings are grouped by union of mutualities (100 National Alliance, 300 Solidaris, 500 National Union, 600 CAAMI, 900 HR Rail…), not per small individual mutuality. Resthome takes care of the grouping.

How do I score a resident's Katz?
: From the resident file, open Katz, click New and score the 6 criteria (washing, dressing, transfer and mobility, toileting, continence, eating) from 1 to 4, then Confirm and Validate. The category and the allowance update automatically.

What are the Katz categories?
: O (independent), A (light dependency), B (moderate dependency), C (heavy dependency) and Cd / Cc (heavy dependency with disorientation or special cases). Under the AViQ rates, the dependency allowance is the same amount for every category; the category serves to declare the right profile to the mutuality.

How do I invoice a month from A to Z in Resthome?
: Open the period, check the MDA, click Generate, Create invoices then post the resident share; then Generate eFact, send the mutuality share to the insurance organisations and get the responses. The resident share and the mutuality share progress in parallel on the same period.

How do I record an absence or a hospitalisation?
: Open the month's period (or the resident file) and add an absence, giving the type, the departure and return date/time, then Save. The resident's billing synchronises automatically; the allowance is reduced for the absence days according to the noon rule.

What happens when a resident departs or dies?
: Close their stay, giving the exit date and the reason (departure, death, transfer). Resthome stops the billing on the right date, prepares the credit note for the accommodation invoiced in advance and notifies the exit to the mutuality.

What is anticipatory billing in Resthome?
: For residents invoiced in advance, one month's accommodation is invoiced the previous month, while the INAMI allowance and the supplements are invoiced in the month they are provided.

How do I add a supplement to a resident?
: Open the resident's supplement envelope, add a line (product/service, quantity, price), state whether the supplement is one-off or recurring, then Save. Adding it automatically updates the invoice of the resident concerned.
:::

This page gathers short answers to the most common questions. Each answer links
to the documentation page that details it.

---

## Getting started

### How do I log in to Resthome?

Open your browser at the address provided by your institution, enter your email
address and your password, then click **Log in**. If you forget it, use the
"Reset password" link or ask your administrator.
→ [Getting started](premiers-pas.md)

### What are the Resthome applications?

Resthome is organised into applications reachable from the main menu (the grid
icon): **MR/MRS** (residents, stays, billing, Katz, eHealth), **Care**
(prescriptions, care plans, vital signs), **Meals** (menus, diets, family
portal) and **Configuration** (rooms, rates, master data). Depending on your
role, you only see the applications that concern you.
→ [Getting started](premiers-pas.md)

### What is the dashboard for?

The MR/MRS application dashboard gives an overview: the pending tasks (Katz to
do, MDA to check, eFact batches…), clickable counters that open the relevant
list directly, and the month's important alerts. Click a counter (e.g. "Katz to
do") to open the list of items to handle.
→ [Getting started](premiers-pas.md)

### Where do I configure the rooms and rates?

In the **Configuration** application: create your rooms with their type (MR,
MRS, single, double…) and equipment, define the **INAMI rates** (allowance per
Katz category) and the **accommodation rates**, then the supplement types and
the mutualities. Resthome also handles **multiple companies** in the same
database, each with its own residents, rooms and billing kept separate.
→ [Configuration](configuration/index.md)

---

## Residents & Katz

### How do I create a resident?

Open **MR/MRS → Residents**, click **New**, fill in at least the name, the date
of birth, the gender and the **NISS** if known, select the mutuality, then
**Save**. Without a NISS, the MDA check and the eAgreement agreements cannot be
sent, but you can create the resident and complete the NISS later.
→ [Managing a resident](residents/gerer-un-resident.md)

### How do I start a stay?

Open a **stay agreement** (room, MR/MRS type, start date) — the stay is then in
**Draft**. **Confirm** it (the room is reserved, complete the admission
date/time), then click **Start Stay**: the stay moves to **In Progress**.
→ [Managing a resident](residents/gerer-un-resident.md)

### What does starting a stay trigger automatically?

On start, Resthome adds the resident to the open billing periods, creates (for a
resident invoiced in advance) the first accommodation invoice for the admission
month, opens the month's supplement envelope and creates the admission
eAgreement (if the NISS is present).
→ [Managing a resident](residents/gerer-un-resident.md)

### How do I score a resident's Katz?

From the resident file, open **Katz**, click **New** and score the 6 criteria
(washing, dressing, transfer and mobility, toileting, continence, eating) from
**1** (independent) to **4** (totally dependent), then **Confirm** and
**Validate**. Resthome computes the category in line with the regulation and
updates the allowance automatically.
→ [The Katz evaluation](residents/katz.md)

### What are the Katz categories?

**O** (independent), **A** (light dependency), **B** (moderate dependency),
**C** (heavy dependency) and **Cd / Cc** (heavy dependency with disorientation /
special cases). Under the AViQ rates, the **allowance amount is the same for
every category**, including O; the category serves to declare the right profile
to the mutuality.
→ [The Katz evaluation](residents/katz.md)

### What happens as long as there is no validated Katz?

As long as no **validated** Katz exists, the resident is in category **O** by
default, and a "Katz to do" reminder appears on the dashboard. Validate the Katz
and send it through an eAgreement Light request to declare the right category to
the mutuality.
→ [The Katz evaluation](residents/katz.md)

### How do I record a Katz worsening?

If the resident's condition deteriorates, enter a **new evaluation** with a
**worsening reason**. Resthome then prepares the update of the care agreement
(**Annex 10**): the reason is carried over automatically, and the clinician's
signature completes the document.
→ [The Katz evaluation](residents/katz.md)

### How do I change a resident's room or transfer them MR ↔ MRS?

On the **stay**, use the **Change Room** action (or **Internal Transfer** for a
change of care type), give the new room / the new type and the date/time, then
**Validate**. Resthome splits the billing on the right date, at the matching
rate; this is not a new admission and the INAMI intervention (the allowance)
stays continuous.
→ [Room change and transfer](residents/changement-chambre.md)

---

## Insurability (MDA)

### What is the MDA and what is it for?

The **MDA** checks that a resident's **insurability is in order** and identifies
their **exact mutuality** by querying **MyCareNet / WalCareNet** for you over a
given period. It is the essential prerequisite for the eFact sending.
→ [Insurability (MDA)](ehealth/mda.md)

### How do I check a resident's MDA insurability?

Create an **MDA request** (menu **eHealth → Insurability → MDA Requests**) with
the resident, the pre-filled NISS and the period (current month by default),
then click **Send (Sync)**: the sending is immediate and the response comes back
at once. Then read the summary and the insurability periods.
→ [Insurability (MDA)](ehealth/mda.md)

### How do I check several residents at once?

Launch the check **in batch**: select the residents (you can **paste a column**
of names/NISS), the period, then send the whole batch. Use **Immediate sending
(Sync)** for small volumes, or **Grouped sending (Async)** for large monthly
batches — the response is then retrieved with **Check responses** (requires at
least 2 residents).
→ [Insurability (MDA)](ehealth/mda.md)

### When should the MDA be done?

Do the MDA **at the start of the month**, before generating the invoices: this
avoids later eFact rejections due to a wrong mutuality or a loss of
insurability.
→ [Insurability (MDA)](ehealth/mda.md)

### What does "insured but not in order" mean?

If the beneficiary codes come back as zero (insured but unpaid contributions /
problematic file), Resthome shows an **alert**: the resident is affiliated but
**not in order**. This must be clarified with them or their mutuality before
invoicing the OA.
→ [Insurability (MDA)](ehealth/mda.md)

### What does Resthome update after a successful MDA?

The resident file is corrected automatically: the **mutuality (OA)** if it
differs from the profile, the **BIM status**, the **affiliation number**, the
**identity** if fields were missing, and the **date of death** if the OA reports
it. For residents under a special scheme (INIG, CEE, Fedasil, foreign,
private…), Resthome **does not overwrite** the profile's mutuality.
→ [Insurability (MDA)](ehealth/mda.md)

### What to do in case of an MDA error or no response?

For a "No response" answer from the platform, use **Retry no-response**; if it
persists, **Report to InterMut.** For a rejection by the OA, use **Contact the
OA** (the reason is shown); for a technical error, **Report to InterMut.**
→ [Insurability (MDA)](ehealth/mda.md)

### What is reintegration (loss then return of insurability)?

Resthome compares with the previous check: if a resident goes from **not insured
to insured**, a notification appears and the **Reintegration** action switches
the lines that had been invoiced to the resident over to the OA. Conversely
(**insured → not insured**), their allowance is excluded from the period's OA
billing and invoiced to the resident until it is restored.
→ [Insurability (MDA)](ehealth/mda.md)

---

## Agreements (eAgreement)

### What is the eAgreement?

When a resident is admitted, is absent, returns or leaves the institution, the
mutuality must be informed electronically. Resthome **automatically prepares**
the eHealth notification matching your action; most of the time, you have
nothing extra to enter — just to check and, if needed, to send.
→ [Agreements (eAgreement)](ehealth/eagreement.md)

### What is the difference between eAgreement and eAgreement Light?

The **eAgreement** is the care coverage agreement (linked to the Katz category
and the allowance). The **eAgreement Light** groups the simpler notifications
tied to the resident's **movements** (admission, absence, departure, return) —
these are the ones Resthome generates on its own as you go.
→ [Agreements (eAgreement)](ehealth/eagreement.md)

### Which document is prepared depending on the action?

Start a stay → **Admission agreement (Annex 7)**; record an absence /
hospitalisation → **exit notification (Annex 11)**; resident return →
**readmission (Annex 7)**; validated Katz worsening → **update of the care
agreement (Annex 10)**; end of stay / death → **exit notification (Annex 11)**.
→ [Agreements (eAgreement)](ehealth/eagreement.md)

### What are the statuses of an agreement, and what to do if rejected?

An agreement goes through **Draft** (prepared, not sent), **Sent**, **Accepted**
and **Rejected** (with a reason). If rejected, Resthome shows the **reason in
plain language, in French and in Dutch**, directly on the agreement — so you know
what to fix (often NISS, mutuality or dates) before resending.
→ [Agreements (eAgreement)](ehealth/eagreement.md)

### Can a movement be recorded without a NISS?

Without a NISS, the agreement cannot be transmitted. You can still record the
movement (admission, absence…): Resthome notes it and invites you to complete
the NISS as soon as possible.
→ [Agreements (eAgreement)](ehealth/eagreement.md)

---

## Electronic invoicing (eFact)

### What is the eFact?

The **eFact** is the **electronic** sending of the **mutuality share** (the
INAMI allowance) to the **insurance organisations (OA)** through the eHealth /
MyCareNet network. Resthome builds the files, transmits them and **follows the
responses** — acknowledgements of receipt, settlements, acceptances and
rejections.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### What are the states of a billing period?

A period goes through four states, in order: **Draft** (created, nothing
computed), **Generated** (allowances and shares computed, to be checked),
**Invoiced** (invoices posted, the eFact can be built and sent) and **Closed**
(finished and locked).
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### How do I generate an eFact period?

Open the month's period in **Draft** state and click **Generate**; in the
wizard, leave **Residents** empty for all active residents and click **Load
MDA**, then **Generate**. The period moves to **Generated**: Resthome has
computed, for each resident, the Katz allowance, the INAMI share and the
resident share.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### How do I check a period before invoicing?

At the top of the period, counters give the health state of the month
(**Supplements**, **Absences**, **Not invoiced**, **MDA**, **Katz to do**) and
Resthome flags anomalies in the discussion thread on the right. Handle each
point (**Done** button once settled) before invoicing, and run **Check MDA** to
verify insurability.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### How do I generate the eFact batches?

Once the invoices are posted (period **Invoiced**), click **Generate eFact**:
Resthome builds the **batches** — one electronic file per insurance organisation
— then shows the **eFact Batches** list (OA, reference, month, deadline, status,
invoiced/accepted/refused amounts, and code + reason in case of refusal).
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### What is a batch per union?

Sendings are grouped **per union** (the big OA families), not per small
individual mutuality: **100** (National Alliance), **300** (Solidaris), **500**
(National Union), **600** (CAAMI), **900** (HR Rail)… Resthome takes care of the
grouping.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### How do I send an eFact period and follow the responses?

Open **eHealth → eFact → Cockpit** (or the batches) and click **Send all** (or
batch by batch); the sendings go to the mutualities through eHealth. Then click
**Get responses**: each batch moves **Sent → Acknowledged → Accepted /
Rejected**, with Resthome automatically reconciling the accepted/refused
amounts.
→ [Invoice a month, step by step](facturation/facturer-un-mois.md) ·
[Electronic invoicing (eFact)](ehealth/efact.md)

### I receive an acknowledgement of receipt (931000) after sending, should I wait?

**Yes.** The **931000** only confirms that the insurance organisation
**received** the batch and passed the first check — it is not the final result.
There is **nothing to resend**: wait for the **settlement (920900)**, which
states what is accepted and paid (a few days). In the meantime, a **920098**
(warnings, accepted anyway) or a **920099** (global rejection, to fix and
resend) may arrive.
→ [Electronic invoicing (eFact)](ehealth/efact.md) ·
[eFact rejections](ehealth/efact-rejets.md)

### Why is an eFact invoice rejected, and how do I fix it?

If a batch (or part of it) is **rejected**, the rejection **code** and
**reason** tell you why (insurability, allowance, dates…). Fix the cause, then
**resend**: the **Resends** counter keeps track of retransmissions to avoid
duplicates, and the **Reintegration** button lets you, where applicable,
reintegrate lines into a new sending.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### What does "deadline exceeded" mean on a period card?

The **sending deadline** of this period has **passed**. Send without delay —
beyond it, some insurance organisations may refuse the batch.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

---

## Billing & supplements

### How do I invoice a month from A to Z?

Open the period (**MR/MRS → Billing → Billing periods**), **Check the MDA**,
click **Generate**, **Create invoices** then **Post** the resident share, then
**Generate eFact** and send the mutuality share to the OAs, finally **Get the
responses**. Resthome runs in parallel the resident share (classic invoices) and
the mutuality share (eFact) on the same period.
→ [Invoice a month, step by step](facturation/facturer-un-mois.md)

### What is anticipatory billing?

For residents invoiced in advance, one month's **accommodation** is invoiced
**the previous month**, while the **allowance** and the **supplements** are
invoiced in the month they are provided.
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
the resident share is split, not the INAMI allowance (which goes to the
mutuality through the eFact).
→ [Support debtors (split billing)](facturation/split-billing.md)

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
automatically synchronises the billing of the resident concerned.
→ [Absences and hospitalisations](facturation/absences.md)

### What is the effect of an absence on the allowance?

The **INAMI allowance** is computed on the **presence days**; an absence
**reduces** this allowance for the days concerned. The count follows the **"noon
rule"** (Brussels time): it is the presence at noon that determines whether the
day counts, hence the importance of the departure and return dates and times.
→ [Absences and hospitalisations](facturation/absences.md)

### Which absences must be reported to the mutuality?

An absence of **more than 72 h**, or **any hospitalisation**, prepares an
**Annex 11** (exit notification), and the **return** prepares an **Annex 7**
(readmission). Resthome creates these notifications the moment you record the
absence and the return; you only have to check and send them.
→ [Absences and hospitalisations](facturation/absences.md)

### How do I cancel an absence entered by mistake?

Delete it or reset it to draft: Resthome **cleanly rolls back** — the allowance
is recomputed as if the absence had not happened, and the prepared notifications
are withdrawn as long as they have not been validated on the mutuality side. If
the month is already posted, first reset the invoice to draft (or create a
credit note) then refresh.
→ [Absences and hospitalisations](facturation/absences.md)

---

## Departure & death

### What happens when a resident departs or dies?

Simply **close their stay**: open the file → the stay, give the **exit date**
(and time) with the **reason** (departure, death, transfer…), then **Validate**.
Resthome stops the billing on the right date, prepares the regularisation of
what was invoiced in advance and notifies the exit to the mutuality.
→ [Departure and death](facturation/depart-deces.md)

### Why is a credit note created on departure?

Since the accommodation is invoiced **one month in advance**, if the resident
leaves during an already invoiced month, Resthome **automatically prepares a
credit note** to refund the unoccupied period (you are notified of its
creation). The INAMI allowance and the supplements, however, are invoiced in the
month they are provided.
→ [Departure and death](facturation/depart-deces.md)

### Can a stay closed by mistake be reopened?

Yes. If you closed a stay wrongly (or in the case of a death recorded by
mistake), you can **reopen** it: Resthome restores the billing and cancels the
regularisations as long as they are not final. If the month is already posted,
the correction first goes through a reset to draft or a credit note, then a
refresh.
→ [Departure and death](facturation/depart-deces.md)
