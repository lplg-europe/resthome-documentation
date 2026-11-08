---
modules: [healthcare_consultation]
sectors: [gp]
---

# Appointments

:::{rh-description}
The diary of a general practice in WideCare: booking an appointment, its status from planned to seen, the no-show, and opening the consultation from the appointment.
:::

:::{rh-faq}
How long is a new appointment?
: Fifteen minutes by default. Change the end time on the appointment for a longer slot.

Who sees the patient's name and the reason of an appointment?
: Only the users with the **Consultations** access. A colleague who shares the calendar without it sees the time slot, not who comes or why.

Does the appointment follow the consultation?
: Yes. Starting the consultation sets the appointment to **Arrived**; closing it sets the appointment to **Seen**.

Can I start a consultation without an appointment?
: Yes: click **New** in **Practice → Consultations**. See [Consultations](consultations.md).
:::

**Practice → Appointments** is the diary of the practice. An appointment is a
time slot with a **patient**, a **practitioner** and a **reason**, and a status
that follows the visit.

## The diary

The diary opens on the week, one colour per practitioner. The panel on the side
filters the practitioners shown. Switch to the list to read the appointments in
rows: start, duration, patient, practitioner, reason and status.

<!-- screenshot to add: the weekly diary with the appointments of two practitioners -->

The search offers:

- **To Come**: appointments planned, confirmed or with the patient arrived;
- **Seen** and **No-Show**;
- **Date**, and grouping by **Practitioner** or **Appointment Status**.

## Book an appointment

1. Click the slot in the diary, or **New**.
2. On the **Patient** tab, **Practice Appointment** is ticked: choose the
   **Patient**.
3. Check the **Practitioner** (you, by default) and type the **Reason for
   Visit**.
4. Adjust the time if needed, then save.

The **Patient** field offers the patients of the practice. For a new patient,
create the card first in **Practice → Patients**.

An appointment is a calendar event: it also shows in the calendar of its
attendees.

## The status of an appointment

| Status | Meaning |
| --- | --- |
| **Planned** | Booked. |
| **Confirmed** | The patient confirmed. |
| **Arrived** | The patient is in the waiting room, or the consultation has started. |
| **Seen** | The consultation is closed. |
| **No-Show** | The patient did not come. |
| **Cancelled** | The appointment will not take place. |

The buttons at the top of the appointment change it:

- **Confirm**, on a planned appointment;
- **Patient Arrived** and **No-Show**, on a planned or confirmed appointment;
- **Cancel Appointment**, until the patient is seen.

## Start the consultation

Click **Start Consultation** on the appointment. The consultation opens with
the patient, the practitioner, the date and the reason of the appointment; the
first click creates it, the next ones reopen it.

The appointment then shows **Arrived**, and **Seen** once the consultation is
closed. Its **Consultations** button opens the consultation again.

## What's next

- [Consultations](consultations.md) — the SOAP note.
- [Patients](patients.md)
