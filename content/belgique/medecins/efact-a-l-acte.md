---
modules: [l10n_health_be_efact_per_act]
sectors: [gp]
---

# eFact per act

:::{rh-description}
Prepare the eFact file of the acts billed in third-party payment from a WideCare general practice: one batch per doctor, mutuality and day, the 920000 file and its follow-up.
:::

:::{rh-faq}
Which acts can be claimed in eFact?
: The acts in third-party payment, priced, with an insurer share, and not yet in a batch.

Why did some acts stay out of the batch?
: One batch holds one billed month, and a doctor sends at most one file a day to each mutuality. The acts of a later month, or those beyond today's file, wait for the next batch: the batch's thread says how many.

Does WideCare send the file to MyCareNet?
: Not yet. WideCare builds and checks the 920000 file; **Mark as sent** records that it left.

What must I set before the first batch?
: On your eHealth certificate: the **eFact profession code**, your **Agreement status** and the **eFact bank account** the mutualities pay you on.
:::

In **third-party payment**, the patient pays only their personal share and the
mutuality pays you the rest. WideCare gathers those acts into **eFact
batches** and builds the **920000 file** of each.

## Before the first batch

On your certificate (**eHealth → Configuration → My eHealth identity**), the
**eFact per act** group holds:

- **eFact profession code**: the code of your profession in the INAMI table;
- **Agreement status**: **0 - No agreement**, **1 - Adhering to the
  agreement**, **2 - Partially adhering** or **9 - Not adhering**;
- **eFact bank account**: the account the mutualities pay you on.

Each patient needs a mutuality on their card.

## Claim the acts

1. Open **Practice → Billable Acts** and select the acts in third-party payment.
2. Click **Actions → Claim in eFact**.

WideCare puts the acts in today's batches, **one per doctor and per
mutuality**, and opens them. An act that cannot be claimed is left aside, with
the reason in the batch's thread.

## The batch

**eHealth → eFact per act** lists the batches: reference, envoi date,
practitioner, insurer, envoi number, number of acts, amount claimed and status.

A batch shows, under **Envoi**, the **Practitioner certificate**, the
**Third-party payer NIHII**, the **Insurer** and its **OA code**; under
**File**, the **Environment**, the **Bank account**, the **Patients**, the
amount **Claimed from the insurer** and the **Patient shares**. The **Acts** tab
lists the acts with their **eFact invoice number**.

<!-- screenshot to add: an eFact per-act batch with its acts and the generated file -->

| Status | Meaning |
| --- | --- |
| **Draft** | The acts are gathered. |
| **Generated** | The 920000 file is built. |
| **Sent** | The file left. |
| **Cancelled** | The acts left the batch and can be claimed again. |

1. Click **Generate the file**. When the file cannot be built, the **Validation
   errors** say why: correct the acts or the patient, then click **Generate
   again**.
2. Download the **920000 file**.
3. Once the file has left, click **Mark as sent**.

**Reset to Draft** brings a generated batch back to draft; **Cancel** frees its
acts, until it is sent.

:::{admonition} Sending and answers
:class: warning

WideCare builds and checks the file; it does not send it to MyCareNet nor read
the mutualities' answers yet. The approvals of WideCare for the general
practitioners' eFact are in preparation.
:::

## What's next

- [Per-act billing](../../medecins/facturation-a-l-acte.md)
- [The INAMI nomenclature](nomenclature.md)
