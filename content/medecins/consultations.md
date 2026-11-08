---
modules: [healthcare_consultation]
sectors: [gp]
---

# Consultations

:::{rh-description}
The consultation in a WideCare general practice: one encounter with a patient, at the practice or at home, its reason, its SOAP note and its status from in progress to done.
:::

:::{rh-faq}
What is a SOAP note?
: The consultation note in four headings: **Subjective** (what the patient reports), **Objective** (what you observe), **Assessment** (your diagnosis) and **Plan** (treatment, follow-up, referral).

Can I change a closed consultation?
: Not as it stands: a closed consultation is read-only. Click **Reopen** to make a correction, then close it again.

How do I record a home visit?
: Choose **Home Visit** as the **Place** of the consultation. The **Home Visits** filter lists them.

Who sees the consultations?
: The users with the **Consultations** access.
:::

A **consultation** is one encounter between a practitioner and a patient. It
records why the patient came, what was found and what was decided.

## The list of consultations

**Practice → Consultations** lists the consultations, the latest first: date,
reference, patient, practitioner, place, reason and status. Switch to the
calendar to see them by week.

The search offers **In Progress**, **Done**, **At the Practice**, **Home
Visits** and **Date**, and grouping by **Patient**, **Practitioner** or
**Date**.

## Start a consultation

- From an appointment: **Start Consultation** (see
  [Appointments](rendez-vous.md)).
- Without an appointment: click **New** in **Practice → Consultations**.

Fill in:

- **Patient** and **Practitioner** (you, by default);
- **Reason**: why the patient came, in a few words;
- **Date** and **Place**: **At the Practice** or **Home Visit**;
- **Appointment**: the appointment it honours, if it was booked. Choosing it
  fills in the patient, the practitioner, the date and the reason.

Each consultation gets a reference that follows the year: `CONS/2026/00001`.

<!-- screenshot to add: a consultation in progress with its SOAP note -->

## The SOAP note

The **SOAP Note** tab has four headings:

- **Subjective**: the complaint and the history, what the patient says;
- **Objective**: the examination and the measurements;
- **Assessment**: the diagnosis, the problem;
- **Plan**: the treatment, the follow-up, the referral.

## Close the consultation

| Status | Meaning |
| --- | --- |
| **In Progress** | The consultation is being written. |
| **Done** | Closed: the consultation is read-only. |
| **Cancelled** | It did not take place. |

- **Close Consultation** sets it to **Done**; its appointment shows **Seen**.
- **Reopen** puts a done or cancelled consultation back in progress.
- **Cancel** cancels a consultation in progress.

The thread at the bottom keeps the messages and every change of patient,
practitioner, date, place, reason and status, with who made it and when.

## Bill the consultation

The **Acts** tab lists the acts performed during the consultation, and
**Create Invoice** turns them into the patient's invoice: see
[Per-act billing](facturation-a-l-acte.md).

## What's next

- [Per-act billing](facturation-a-l-acte.md)
- [Appointments](rendez-vous.md)
