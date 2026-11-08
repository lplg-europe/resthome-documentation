---
modules: [l10n_health_be, l10n_health_be_eid, l10n_health_be_mda, l10n_health_be_dmg]
sectors: [gp]
---

# The patient's file in Belgium

:::{rh-description}
What Belgium adds to the patient card of a WideCare general practice: the NISS, the reading of the eID card, the mutuality and the BIM status, and the insurability and DMG answers.
:::

:::{rh-faq}
Can I search a patient by NISS?
: Yes. Type the NISS in the search bar of **Practice → Patients**.

Why can't I edit the mutuality or the date of birth any more?
: Once the mutuality has answered an insurability check, the identity it holds is locked on the card: typing over it would set the patient apart from their file at the mutuality. The next check updates it.

Who fills in the BIM status?
: The insurability check. **BIM Status** is read-only on the card: it shows the mutuality's last answer, and the INAMI nomenclature reads it to price the personal share.
:::

The Belgian patient card carries what the mutualities and the eHealth services
ask for: the **NISS**, the **mutuality** and the answers of the **insurability
check**.

## The NISS

The **NISS** sits on the **Identity** tab, before the date of birth. It
identifies the patient for life, at the mutuality and in every eHealth service:
an eAttest cannot be sent for a patient without it.

## Read the eID card

The card fills in the identity from the chip: name, NISS, date of birth,
gender, nationality, place of birth, address and photo.

1. Insert the patient's card in the reader.
2. On the patient card, click **Contact**, next to the name.
3. Click **Read eID Card** at the top of the contact record.
4. Wait for the message: reading takes up to 30 seconds.

The **eID Card** tab of the contact record keeps the card's number, its chip
number and its validity dates.

Create the patient in **Practice → Patients** first: a contact created from the
card alone is not yet a patient of the practice.

<!-- screenshot to add: the contact record of a patient after reading the eID card -->

## Health insurance

The **Identity** tab shows a **Health Insurance** group:

- **Insurance Regime**: **Standard (Belgian mutuelle)**, or a special regime;
- **Health Insurance**: the patient's mutuality, and the **Insurance Member
  Code**;
- **Mutuality Code (MDA)**, **CT1 (Holder Code)** and **CT2**, as the mutuality
  answered;
- **MDA Insured**, **BIM Status** and **Last MDA Check**, filled in by the
  insurability check.

## The insurability on the card

At the top of the card, a banner says what the last check found:

- **Insurance eligibility not verified**: no check yet;
- **Resident not insured**: the last check found no insurability;
- **Resident hospitalised**, or **Palliative status**, when the mutuality said
  so.

The button **Verify Insurability** asks the mutuality now; the **MDA History**
button lists the checks. See [Insurability (MDA)](assurabilite.md).

When the mutuality reported them, the card also shows the **Reference
Pharmacy**, the **DMG Holder** and the **Palliative Status**.

## The global medical file

The **DMG** button of the card opens the questions asked to the DMG register for
this patient. See [Global medical file (DMG)](dmg.md).

## What's next

- [Insurability (MDA)](assurabilite.md)
- [Patients](../../medecins/patients.md) — the patient card in every country.
