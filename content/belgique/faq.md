---
modules: []
---

# FAQ — Belgium

:::{rh-description}
Short answers to frequently asked questions on what is Belgian in Resthome: Katz, NISS, MDA insurability, eAgreement, eFact, the INAMI allowance, annexes and absences seen by the mutuality.
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

How do I invoice a month from A to Z in Belgium?
: Open the period, check the MDA, click Generate, Create invoices then post the resident share; then Generate eFact, send the mutuality share to the insurance organisations and get the responses. The resident share and the mutuality share progress in parallel on the same period.
:::

This page gathers the short answers to the questions that only arise in
**Belgium**: the Katz scale, the NISS, the exchanges with the mutualities over
eHealth and the INAMI allowance. Each answer links to the page that details it.
The questions valid in every country are in the [FAQ](../faq.md).

---

## Getting started in Belgium

### What does the dashboard show in Belgium?

On the **Nursing Home** dashboard, the pending tasks include the Belgian
ones: **Katz to do**, **MDA to check**, **eFact batches**… Click a counter
(e.g. "Katz to do") to open the list of items to handle.
→ [Getting started](../premiers-pas.md)

### Where do I configure the Belgian rooms and rates?

In the **Configuration** application: give each room its type (**MR**,
**MRS**, single, double…), define the **INAMI rates** (allowance per Katz
category) next to the accommodation rates, and create the **mutualities**.
→ [Configuration](../configuration/index.md) ·
[The INAMI dependency allowance](forfait-inami.md)

---

## Residents & Katz

### What must I enter on a resident's file in Belgium?

The **NISS** if known, and the **mutuality**. Without a NISS, the MDA check and
the eAgreement agreements cannot be sent, but you can create the resident and
complete the NISS later.
→ [Admitting a resident in Belgium](admission.md)

### Which stay types exist in Belgium?

A stay is **MR**, **MRS** or **day care (CSJ)**: the stay agreement carries the
type, and it drives the INAMI rates and the annexes sent to the mutuality.
→ [Admitting a resident in Belgium](admission.md)

### What does starting a stay trigger in Belgium?

On top of what it does in every country, starting the stay creates the
**admission eAgreement** (Annexe 7), if the NISS is present.
→ [Admitting a resident in Belgium](admission.md)

### How do I score a resident's Katz?

From the resident file, open **Katz**, click **New** and score the 6 criteria
(washing, dressing, transfer and mobility, toileting, continence, eating) from
**1** (independent) to **4** (totally dependent), then **Confirm** and
**Validate**. Resthome computes the category in line with the regulation and
updates the allowance automatically.
→ [The Katz assessment](katz.md)

### What are the Katz categories?

**O** (independent), **A** (light dependency), **B** (moderate dependency),
**C** (heavy dependency) and **Cd / Cc** (heavy dependency with disorientation /
special cases). Under the AViQ rates, the **allowance amount is the same for
every category**, including O; the category serves to declare the right profile
to the mutuality.
→ [The Katz assessment](katz.md)

### What happens as long as there is no validated Katz?

As long as no **validated** Katz exists, the resident is in category **O** by
default, and a "Katz to do" reminder appears on the dashboard. Validate the Katz
and send it through an eAgreement Light request to declare the right category to
the mutuality.
→ [The Katz assessment](katz.md)

### How do I record a Katz worsening?

If the resident's condition deteriorates, enter a **new evaluation** with a
**worsening reason**. Resthome then prepares the update of the care agreement
(**Annexe 10**): the reason is carried over automatically, and the clinician's
signature completes the document.
→ [The Katz assessment](katz.md)

### How do I transfer a resident MR ↔ MRS?

On the **stay**, use **Internal Transfer**, give the new type and the date/time,
then **Validate**. Resthome splits the billing on the right date, at the
matching rate; this is not a new admission and the INAMI intervention (the
allowance) stays continuous.
→ [Internal transfer (MR ↔ MRS)](ehealth/eagreement-transfert.md)

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
→ [MDA errors — causes and solutions](ehealth/mda-erreurs.md)

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

Start a stay → **Admission agreement (Annexe 7)**; record an absence /
hospitalisation → **exit notification (Annexe 11)**; resident return →
**readmission (Annexe 7)**; validated Katz worsening → **update of the care
agreement (Annexe 10)**; end of stay / death → **exit notification (Annexe 11)**.
→ [Agreements (eAgreement)](ehealth/eagreement.md)

### What are the statuses of an agreement, and what to do if rejected?

An agreement goes through **Draft** (prepared, not sent), **Sent**, **Accepted**
and **Rejected** (with a reason). If rejected, Resthome shows the **reason in
plain language, in French and in Dutch**, directly on the agreement — so you know
what to fix (often NISS, mutuality or dates) before resending.
→ [Refused agreement (eAgreement) — causes and solutions](ehealth/eagreement-refus.md)

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

### How do I generate an eFact period?

Open the month's period in **Draft** state and click **Generate**; in the
wizard, leave **Residents** empty for all active residents and click **Load
MDA**, then **Generate**. The period moves to **Generated**: Resthome has
computed, for each resident, the Katz allowance, the INAMI share and the
resident share.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

### How do I check a period before invoicing in Belgium?

Among the counters at the top of the period, **MDA** and **Katz to do** are
Belgian: handle them with the others, and run **Check MDA** to verify
insurability before invoicing.
→ [Billing a month in Belgium](facturation.md)

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
→ [Billing a month in Belgium](facturation.md) ·
[Electronic invoicing (eFact)](ehealth/efact.md)

### I receive an acknowledgement of receipt (931000) after sending, should I wait?

**Yes.** The **931000** only confirms that the insurance organisation
**received** the batch and passed the first check — it is not the final result.
There is **nothing to resend**: wait for the **settlement (920900)**, which
states what is accepted and paid (a few days). In the meantime, a **920098**
(warnings, accepted anyway) or a **920099** (global rejection, to fix and
resend) may arrive.
→ [Electronic invoicing (eFact)](ehealth/efact.md) ·
[eFact rejections — causes and solutions](ehealth/efact-rejets.md)

### Why is an eFact invoice rejected, and how do I fix it?

If a batch (or part of it) is **rejected**, the rejection **code** and
**reason** tell you why (insurability, allowance, dates…). Fix the cause, then
**resend**: the **Resends** counter keeps track of retransmissions to avoid
duplicates, and the **Reintegration** button lets you, where applicable,
reintegrate lines into a new sending.
→ [eFact rejections — causes and solutions](ehealth/efact-rejets.md)

### What does "deadline exceeded" mean on a period card?

The **sending deadline** of this period has **passed**. Send without delay —
beyond it, some insurance organisations may refuse the batch.
→ [Electronic invoicing (eFact)](ehealth/efact.md)

---

## Billing in Belgium

### How do I invoice a month from A to Z in Belgium?

Open the period (**Billing → Facturation → Billing Periods**), **Check the MDA**,
click **Generate**, **Create invoices** then **Post** the resident share, then
**Generate eFact** and send the mutuality share to the OAs, finally **Get the
responses**. Resthome runs in parallel the resident share (classic invoices) and
the mutuality share (eFact) on the same period.
→ [Billing a month in Belgium](facturation.md)

### Is the INAMI allowance split between the debtors?

No. Split billing only divides the resident share; the INAMI allowance goes to
the mutuality through the eFact.
→ [Split billing](../facturation-partagee/index.md)

---

## Absences & hospitalisations

### What is the effect of an absence on the INAMI allowance?

The **INAMI allowance** is computed on the **presence days**; an absence
**reduces** this allowance for the days concerned. The count follows the **"noon
rule"** (Brussels time): it is the presence at noon that determines whether the
day counts, hence the importance of the departure and return dates and times.
→ [Billing a month in Belgium](facturation.md)

### Which absences must be reported to the mutuality?

An absence of **more than 72 h**, or **any hospitalisation**, prepares an
**Annexe 11** (exit notification), and the **return** prepares an **Annexe 7**
(readmission). Resthome creates these notifications the moment you record the
absence and the return; you only have to check and send them.
→ [Absences and hospitalisations](../facturation/absences.md) ·
[Agreements (eAgreement)](ehealth/eagreement.md)

---

## Departure & death

### What is sent to the mutuality on a departure or a death?

Closing the stay prepares the **exit notification (Annexe 11)** for the
mutuality. The INAMI allowance is invoiced in the month it is provided, so the
credit note only concerns the accommodation invoiced in advance.
→ [Departure and death](../facturation/depart-deces.md) ·
[Agreements (eAgreement)](ehealth/eagreement.md)

---

## What's next

- [FAQ](../faq.md) — the questions valid in every country.
- [Glossary — Belgium](glossaire.md)
- [The billing journey](parcours-facturation.md)
