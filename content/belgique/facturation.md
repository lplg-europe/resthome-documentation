---
modules: [resthome_mr_billing, l10n_health_be_perdiem_ehealth, l10n_health_be_efact, l10n_health_be_perdiem_billing, resthome_mr_ehealth, l10n_health_be_mda, resthome_be]
---

# Billing a month in Belgium

:::{rh-description}
What Belgium adds to the monthly billing in Resthome: the INAMI allowance and its pseudo-codes, the mutuality and resident shares, MDA and eFact at month-end, absences and departures seen by the INAMI, and the CPAS.
:::

:::{rh-faq}
In what order do I bill a month in Belgium?
: Generate → Check MDA → Generate eFact → Create Invoices → confirm the invoices → send the batches and track the responses → Close Period. On the period, the next step is always the highlighted button on the left.

Why must the MDA come before the eFact?
: Because the MDA determines the health insurance fund and the insurability of each resident. Sending the eFact before it means billing the wrong insurer, and the batch comes back rejected. You can also run a batch MDA at the start of the month, before generating: the generation wizard then loads its results.

Can I make corrections after billing?
: As long as the eFact has not been sent, you can set the period back to draft. After sending, correct through a credit note or a corrective batch.

How does an absence affect the INAMI allowance?
: The allowance is computed on presence days, so an absence reduces it for the days concerned. Presence at noon (Brussels time) determines whether a day counts: that is why the exact departure and return times matter.

Which absences must be reported to the health insurance fund?
: An absence of more than 72 hours, or any hospitalisation, prepares an Annexe 11 departure notification; the resident's return prepares an Annexe 7 readmission.

Is the health insurance fund notified of a departure or a death?
: Yes. Closing the stay prepares an Annexe 11 departure notification to the health insurance fund.

Is the INAMI allowance split between the debtors?
: No. Split billing only divides the resident's share — accommodation and supplements. The INAMI allowance goes to the health insurance fund through eFact, in full.

Can a CPAS be one of the debtors?
: Yes. A CPAS that pays part of the resident's share is added as a debtor in split billing, with its percentage; a CPAS that pays everything is set as the resident's billing contact.
:::

The monthly billing described in [Billing](../facturation/index.md) is the same
in every country. This page gathers what **Belgium** adds to it: the **INAMI
allowance** billed to the health insurance fund, the **eHealth** exchanges that
carry it (MDA, eFact, eAgreement), the rules the INAMI applies to absences and
departures, and the **CPAS**.

Each section links to the Belgian page that details the subject.

## Two shares on every invoice

In a Belgian nursing home (**MR** or **MRS**), each month is billed in two
flows, over the same billing period:

- the **mutuality share** — the **[INAMI dependency allowance](forfait-inami.md)**,
  covered 100% by the health insurance fund (third-party payer) and sent
  electronically through **[eFact](ehealth/efact.md)**;
- the **resident's share** — accommodation, supplements and supplement
  agreements, care services, medication, adjusted for absences → standard
  invoices, to the resident, their family or a
  [CPAS](cpas.md).

The allowance is billed under **pseudo-codes**, not under a price list of your
own: the care flat-rate carries its **AViQ pseudo-code** (for example
**770501** for category **O**), and the same code appears on the
[expense note (Annexe 12)](note-de-frais-annexe12.md). The amount is the **same
for every Katz category** under the AViQ rates; the category declares the
dependency profile to the health insurance fund. Details and rates:
[The INAMI dependency allowance](forfait-inami.md).

:::{admonition} MR and MRS
:class: note

In Belgium, the sectors a home is licensed for are **MR** (rest home) and
**MRS** (rest and care home). The **stay type** shown on the resident cards of
the **Supplements** app, and its **MR** / **MRS** filters, are these two
sectors. A supplement convention survives an **MR ↔ MRS** transfer.
:::

## The month, step by step, on the Belgian side

The common guide [Billing a month, step by step](../facturation/facturer-un-mois.md)
gives the sequence common to every country. In Belgium, it gains its eHealth
steps:

1. **Open the period** in **Billing → Facturation → Billing Periods**.
2. **Generate** — in the **Generate Billing** window, **Load MDA Success** (and
   **Load MDA Pending**) pre-fill the residents whose insurability was already
   checked, for instance by a batch MDA run at the start of the month. The
   allowance is computed on the days of presence over the **INAMI intervention
   period**, with the billed Katz category. The period becomes **Generated**.
3. **Check insurability** — click **Check MDA**: one request per resident of the
   period, sent as a batch. The step is done as soon as every resident billed to
   a mutuality has a request — the responses may come later. Fix the flagged
   cases (wrong mutuality, loss of insurability); **Retry Failed MDA** resends
   the requests that ended in an error. See [Insurability (MDA)](ehealth/mda.md).
4. **Generate eFact** — in the **Generate eFact Batches** window, click
   **Generate Batches**: Resthome builds the eFact **batches** from the
   period's mutuality lines, grouped **by union** of mutualities. A resident
   with no Katz assessment blocks this step.
5. **Create Invoices** — the resident's share becomes **draft** invoices; check
   them, then **Confirm** them. The period becomes **Invoiced**.
6. **Send** — open **eHealth → eFact → Cockpit** (or the batches) and click
   **Send all**, or send batch by batch. The submissions go out to the insurers
   through the eHealth network.
7. **Track the responses** — click **Fetch responses** to bring back the
   acknowledgements and settlements. Each batch moves through **Sent →
   Acknowledged → Accepted / Rejected**. In case of a **rejection**, fix the
   cause (insurability, dates, amounts) and **resend**.
8. **Close Period** — possible once no invoice is left in draft, every batch has
   reached a final outcome, no mutuality line is outside a batch and every
   service refused by the insurer has been corrected.
9. **Print the expense notes** — [Annexe 12](note-de-frais-annexe12.md),
   individual and summary, once the month is billed.

The period points at the next step itself: its highlighted button (and the
**To do** column of the **Billing Periods** list) reads **Check insurability
(MDA)**, then **Generate the eFact envoi**, then **Create the invoices**. The
order is advice, not a lock: **Check MDA** and **Generate eFact** stay available
on an **Invoiced** period, for a resident added late or a batch rebuilt.

The screens, the pre-send checks and the advanced buttons are described in
[Electronic invoicing (eFact)](ehealth/efact.md); the whole journey from
admission to payment is in [The billing journey](parcours-facturation.md).

## The month-end checklist, eHealth side

The [Month-end checklist](../facturation/checklist-fin-de-mois.md) applies as is.
In Belgium, it gains the following eHealth steps.

### Insurability (MDA)

Run the **batch MDA** for the month: it confirms who is insured and, above all,
**which mutuality actually responds**. A resident who changed fund without
telling you is caught here — not by an eFact rejection three weeks later.

- Every resident must reach the **Success** status.
- Handle the **Not insured** cases: their share goes to the resident, not to the
  mutuality.
- Retry the **errors** and the **no-responses** — on the period, **Retry
  Failed MDA** resends the requests that ended in an error.

→ [Insurability (MDA)](ehealth/mda.md) · [MDA errors](ehealth/mda-erreurs.md)

:::{admonition} The single most useful step
:class: tip

Most eFact rejections come from a wrong mutuality or a lost insurability.
Running a batch MDA at the **start** of the month (**eHealth → Insurability →
MDA Batches**), then **Check MDA** on the generated period for anyone left,
removes that whole class of problems before the eFact leaves.
:::

### Katz assessments

The billed Katz category is the profile declared to the mutuality with the
allowance. A missing or expired assessment leaves the resident in category
**O** by default, and the billing no longer matches the agreement. The **Katz
to do** counter lists them.

→ [The Katz assessment](katz.md) · [The INAMI dependency allowance](forfait-inami.md)

### eFact batches and responses

**Generate eFact** builds one batch per insurer (per union of mutualities),
right after the MDA and before the invoices. Check them, then send. Each batch then goes through an **acknowledgement** and a
**settlement**:

- **rejected lines** — fix the cause and issue a remainder;
- **rejected batch** — a format problem, to escalate;
- **settlement** — check the amount paid against the amount accepted.

The **eFact Cockpit** gathers everything to be done into stacks: to send,
awaiting insurer, to correct, to reconcile, overdue payments.

→ [eFact rejections](ehealth/efact-rejets.md) · [Settlements and payments](ehealth/efact-paiements.md)

### The deadline

eFact batches must reach the insurer by the **20th of the following month**.
Working backwards, the MDA and the corrections should be done in the **first
week** — which leaves room to handle a rejection without missing the deadline.

| Step | Done when |
|---|---|
| **MDA** | every resident is at **Success** |
| **Katz** | no **Katz to do** left |
| **eFact** | the batches are sent |
| **Follow up** | the **eFact Cockpit** stacks are empty |

## Absences and hospitalisations seen by the INAMI

The common page [Absences and hospitalisations](../facturation/absences.md)
explains how to record an absence. In Belgium, two rules apply on top.

**The noon rule.** The INAMI allowance is computed on the **presence days**.
The count follows a presence-at-**noon** rule (Brussels time): presence at noon
determines whether the day counts. The **dates and times** of departure and
return therefore matter — Resthome relies on them for an exact count.

**Notification to the mutuality.** Some absences must be reported:

- an absence of **more than 72 hours**, or **any hospitalisation**, prepares an
  **Annexe 11** (departure notification);
- the resident's **return** prepares an **Annexe 7** (readmission).

Resthome creates these notifications **at the moment you record the absence and
the return**; you only have to check and send them. Deleting an absence entered
by mistake withdraws them, as long as the mutuality has not validated them.

→ [Agreements (eAgreement)](ehealth/eagreement.md) · [Collective holidays](ehealth/vacances-collectives.md)

## Departure and death

Closing a stay (see [Departure and death](../facturation/depart-deces.md))
prepares the **Annexe 11** departure notification to the health insurance fund.

The INAMI allowance, unlike the accommodation, is billed on the **month actually
served**: it stops at the end of the INAMI intervention. If a resident leaves or
dies during an already invoiced month, the self-check flags the over-declared
allowance and Resthome prepares the credit note or remainder, and a corrective
batch on the mutuality side if needed. The [Annexe 12](note-de-frais-annexe12.md)
reflects the actual days of presence.

→ [Agreements (eAgreement)](ehealth/eagreement.md) · [Electronic invoicing (eFact)](ehealth/efact.md)

## Supplements declared to the mutuality

In the supplements catalog (**Configuration → Catalog**), the **AViQ code**
field holds the **declaration pseudo-code** of a supplement, when it is
declared to the insurance body.

Depending on its **category**, a supplement is either **declared** to the
insurance body in the eFact (**ET50** record), or billed **only on the
resident's invoice**. This setting is made on the product category — see
[Billing settings](../configuration/reglages-facturation.md).

## The CPAS in split billing

A **CPAS** (Public Centre for Social Welfare) steps in on the **resident's
share** only — accommodation and supplements. The INAMI allowance is never
split: it goes to the mutuality through eFact.

- **The CPAS pays everything** → set the resident's **Billing contact** to the
  CPAS.
- **The CPAS pays part of it** → add the CPAS as a debtor in
  [split billing](../facturation-partagee/index.md), with its percentage, and
  the other payers (resident, family) for the balance.

Recording the decision and routing the invoice are detailed in
[CPAS coverage](cpas.md).

## What's next

- [The INAMI dependency allowance](forfait-inami.md) — Katz → category → billed amount.
- [Electronic invoicing (eFact)](ehealth/efact.md) — generate, send and follow the batches.
- [Insurability (MDA)](ehealth/mda.md) — the check to run at the start of the month.
- [Agreements (eAgreement)](ehealth/eagreement.md) — admission, absence, return, departure.
- [The expense note (Annexe 12)](note-de-frais-annexe12.md) — individual and summary notes.
- [CPAS coverage](cpas.md) — when a CPAS pays for the resident.
- [The billing journey](parcours-facturation.md) — from admission to payment.
- [Billing](../facturation/index.md) — the common billing, valid in every country.
