---
modules: [l10n_health_be_dmg]
sectors: [gp]
---

# Global medical file (DMG)

:::{rh-description}
Ask the DMG register who holds a patient's global medical file, and notify a DMG to the mutuality, from a WideCare general practice.
:::

:::{rh-faq}
What does the register answer?
: Whether a global medical file exists for the patient, who holds it (name and NIHII), since when and until when, and whether the fee was paid.

In whose name is a DMG notified?
: In yours: the notification carries your practitioner certificate. WideCare asks you to confirm before it leaves.

The patient has no NISS: can I still ask?
: Yes. Fill in the **OA code** and the **Membership number** of the patient instead.
:::

The **global medical file** (DMG) is held by one general practitioner per
patient. WideCare asks the register who holds it, and notifies the mutuality
when you take it on or renew it.

You need your eHealth identity first: see
[eHealth identity and eID sign-in](identite-ehealth.md).

## Ask who holds the DMG

1. Open **Practice → Global Medical File → Consultations** and click **New**,
   or click the **DMG** button on the patient card.
2. Under **Question**, choose the **Resident** (the patient) and check the
   **Request Date** and the **Practitioner certificate**. Without a NISS, fill
   in the **OA code** and the **Membership number**.
3. Click **Ask the register**.

The answer shows at the top:

- **DMG held by** the holder, with their NIHII;
- or **The register holds no Global Medical File for this resident.**

Under **Answer**: **DMG held**, the **Holder contact** when the holder is in
your contacts, the dates, **Fee paid** and **Mutuality (answer)**. **Ask again**
asks the register once more.

<!-- screenshot to add: the answer of the DMG register for a patient -->

## Notify a DMG

1. Open **Practice → Global Medical File → Notifications** and click **New**.
2. Under **Declaration**, choose the **Resident** (the patient), check the
   **Nomenclature code** — it proposes 102771, the yearly fee for managing the
   DMG — and the **Encounter Date**.
3. Click **Notify** and confirm.

The notification shows **Accepted**, or **Refused / error** with the reason
under the form.

:::{admonition} Test mode
:class: note

While **Stub Mode (Development)** is ticked in the **eHealth** settings, the
register's answers are simulated and no notification leaves WideCare.
:::

## What's next

- [Insurability (MDA)](assurabilite.md) — the DMG holder can also come with the
  insurability answer.
- [The patient's file in Belgium](patients-belgique.md)
