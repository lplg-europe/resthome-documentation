---
modules: [healthcare_billing_core, healthcare_consultation_billing]
sectors: [gp]
---

# Per-act billing

:::{rh-description}
Billing per act in a WideCare general practice: the acts of a consultation, the fee and the patient share, third-party payment, and the invoice of each patient.
:::

:::{rh-faq}
What does the patient's invoice carry?
: The whole fee of each act, or only the patient share when the act is in third-party payment: the insurer's share is then claimed from the insurer.

Can I change an invoiced act?
: No. Cancel its invoice first: the act goes back to **To Invoice**, ready to correct and invoice again.

Can I invoice several acts at once?
: Yes. In **Practice → Billable Acts**, select the acts and use **Create Invoices** in the **Actions** menu: one invoice per patient.

Is VAT applied to the acts?
: No. Each line is booked on the **Healthcare Act** product, a service without tax. Your accountant sets its income account.
:::

A **billable act** is one act performed for one patient on one day: its code,
its fee and who pays what. The acts of a consultation become the patient's
invoice.

## Who pays what

Each act carries:

- **Code** and **Description**: the act in your country's nomenclature;
- **Quantity** and **Unit Fee**;
- **Fee**: quantity × unit fee;
- **Patient Share**: what the patient owes under the insurance rules;
- **Insurer Share**: the fee minus the patient share;
- **Third-Party Payment**: ticked when the insurer is billed directly for its
  share.

Without third-party payment, the patient's invoice carries the **whole fee**.
With it, the invoice carries the **patient share** only.

The patient share lies between zero and the fee, and the quantity is always
positive.

## Bill a consultation

1. Open the consultation and go to the **Acts** tab.
2. Add a line per act: **Code**, **Description**, **Quantity**, **Unit Fee**,
   **Patient Share**, and tick **Third-Party Payment** when it applies.
3. Check the **Total Fee** and the **Total Patient Share** under the lines.
4. Click **Create Invoice**.

WideCare prices the acts not priced yet, then creates the invoice. The
**Invoices** button of the consultation opens it.

<!-- screenshot to add: the Acts tab of a consultation with two acts and their totals -->

## The billable acts

**Practice → Billable Acts** lists every act, open on those **To Invoice**. The
same list sits in **Invoicing → Customers → Billable Acts**, next to the
customer invoices.

| Status | Meaning |
| --- | --- |
| **Draft** | Recorded, not priced yet. |
| **To Invoice** | Priced, waiting for its invoice. |
| **Invoiced** | On an invoice: locked. |
| **Cancelled** | Will not be billed. |

On an act:

- **Price** prices the act and moves it to **To Invoice**: the amounts you
  typed stay, unless your country's tariff gives them;
- **Create Invoice** invoices it;
- **Reset to Draft** brings back a cancelled act or one to invoice;
- **Cancel** withdraws an act that is not invoiced.

To invoice a batch, select the acts in the list, then **Actions → Create
Invoices**: one invoice per patient.

## The invoice

The invoice is an ordinary customer invoice of the **Invoicing** app: one line
per act, without tax. Its **Acts** button opens the acts it carries.

When an invoice is cancelled or deleted, its acts go back to **To Invoice**. An
invoiced act can be neither changed nor deleted.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The INAMI nomenclature prices the act — the fee and the personal share,
ordinary or BIM — and the acts in third-party payment are claimed from the
mutualities with the eFact per act: see
[The INAMI nomenclature](../belgique/medecins/nomenclature.md) and
[eFact per act](../belgique/medecins/efact-a-l-acte.md).
:::

## What's next

- [Consultations](consultations.md)
- [Practice settings](reglages.md) — the access to billing.
