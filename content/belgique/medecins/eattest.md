---
modules: [l10n_health_be_eattest, l10n_health_be_eattest_nomenclature]
sectors: [gp]
---

# eAttest

:::{rh-description}
Send an electronic attestation of care given (eAttest) to the patient's mutuality from a WideCare general practice: the acts picked in the INAMI nomenclature, the sending, the answer and the cancellation.
:::

:::{rh-faq}
When do I use the eAttest?
: When the patient pays you on the spot: instead of a paper certificate, the attestation of the acts goes straight to their mutuality, which reimburses them.

Why can't I send an attestation?
: It needs at least one act, a patient with a NISS, and a care provider with an INAMI number. WideCare says which one is missing.

Can I withdraw an accepted attestation?
: Yes: type the **Cancellation reason** on the **Response** tab, then click **Cancel at the mutuality**.

What does the Stub ribbon mean?
: The answer was simulated by WideCare: nothing reached the mutuality. It shows while the eAttest runs in test mode.
:::

The **eAttest** is the electronic attestation of care given: for the acts the
patient paid you, it tells their mutuality what was done, and the mutuality
reimburses the patient.

You need your eHealth identity first: see
[eHealth identity and eID sign-in](identite-ehealth.md).

## The list of attestations

**Practice → Attestations** lists the attestations: reference, patient, care
provider, date, total fee, justification number and status. The search filters
**Draft**, **Accepted** and **Refused / Error**.

## Write an attestation

1. Click **New** in **Practice → Attestations**.
2. Under **Patient**, choose the **Patient**: their **Patient NISS** and
   **Mutuality** show.
3. Under **Care Provider**, check the **Care Provider** (with their **Provider
   INAMI**), the **Attestation Date** and the **Practitioner certificate**.
4. On the **Acts** tab, add a line per act: pick the **INAMI Code** in the
   nomenclature; the code, the description, the unit fee and the patient share
   fill in. Adjust **Performed On** and **Quantity** if needed.
5. Check the **Total Fee** and the **Total Patient Share**, then click
   **Send**.

**Treatment reason**, **Decision reference** and **Railway beneficiary (RCAM)**
are filled in only when the act requires them. Keep **Test Flag** ticked while
you test.

<!-- screenshot to add: an eAttest with two acts picked in the INAMI nomenclature -->

## The answer

| Status | Meaning |
| --- | --- |
| **Draft** | Being written. |
| **Sent** | Sent, waiting for the answer. |
| **Accepted** | The mutuality accepted it. |
| **Refused** | The mutuality refused it. |
| **Error** | The sending failed. |
| **Cancelled** | Withdrawn. |

The **Response** tab shows the **Justification Number**, the **Invoicing
number**, the **Response Code** and the **Response Message**.

- A **refused** attestation, or one in **error**: read the message, click
  **Reset to Draft**, correct and send again.
- An **accepted** attestation: to withdraw it, type the **Cancellation reason**,
  then click **Cancel at the mutuality**.
- A **draft**: **Cancel** drops it.

:::{admonition} Test mode
:class: note

While the eAttest runs in test mode, the answer is simulated: the attestation
shows a **Stub** ribbon and nothing reaches the mutuality. Ask WideCare support
to switch it to real sending once your access to the MyCareNet services is in
place.
:::

## What's next

- [The INAMI nomenclature](nomenclature.md) — the codes and their fees.
- [Insurability (MDA)](assurabilite.md)
