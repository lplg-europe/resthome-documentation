---
modules: [l10n_health_be_mda, l10n_health_be_gp]
sectors: [gp]
---

# Insurability (MDA)

:::{rh-description}
Check a patient's insurability with their mutuality from a WideCare general practice (MyCareNet Member Data): in your own name, for today or yesterday, with the reference pharmacy, the DMG and the palliative status.
:::

:::{rh-faq}
Can I check a past period?
: No. A doctor asks the mutuality for **one day**: today, or yesterday alone. A period is refused.

In whose name is the check made?
: In yours: the request carries your own eHealth certificate as a doctor.

The patient has no NISS yet: can I still check?
: Yes. In the full check, choose **Membership number + OA code** as the **Identification** and type both.

What does a check write on the patient card?
: The insurability, the mutuality and its codes, the BIM status and the date of the check. The identity the mutuality holds is then locked on the card.
:::

The **insurability check** (MyCareNet *Member Data*, MDA) asks the patient's
mutuality whether they are covered on the day of the consultation, and with
which status.

You need your eHealth identity first: see
[eHealth identity and eID sign-in](identite-ehealth.md).

## Check a patient now

On the patient card, click **Verify Insurability**. The button shows when the
card has a NISS or an insurance member code.

WideCare asks the mutuality for **today** and shows the answer at once. The
card is updated: **MDA Insured**, the mutuality, **BIM Status** and **Last MDA
Check**.

<!-- screenshot to add: the answer of an insurability check for a patient -->

## Ask for more

On the answer, **New check** opens the full check:

- **Resident**: the patient;
- **Identification**: **NISS**, or **Membership number + OA code** for a
  patient without a NISS;
- **Period**: choose **Single date (recommended for hospitalisation)** and the
  **Date**, today or yesterday. With **Period**, only the first day is asked;
- **Data to request from the OA**: tick **Hospitalisation**, **Reference
  pharmacy**, **Global Medical File (DMG)** or **Palliative status**.

Click **Check**. **View MDA request** opens the request it created.

## The list of checks

**Practice → Insurability** lists every check of the practice, with its
patient, its day and the mutuality's answer. On a patient card, the **MDA
History** button lists that patient's checks.

## The one-day rule

The mutualities answer a doctor for the day they ask, or the day before. A check
for a period, or for an older day, stops with the message that a doctor asks for
**one** day.

:::{admonition} Test mode
:class: note

While **Stub Mode (Development)** is ticked in the **eHealth** settings, the
answers are simulated and no request leaves WideCare. See
[General practice in Belgium](index.md).
:::

## What's next

- [The patient's file in Belgium](patients-belgique.md)
- [Global medical file (DMG)](dmg.md)
