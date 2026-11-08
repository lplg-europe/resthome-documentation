---
modules: [resthome_day_care, resthome_geriatric, healthcare_accommodation_billing]
sectors: [csj]
---

# Absences and hospitalisation of a day care user

:::{rh-description}
Absences of a day care user (CSJ) in WideCare: a declared absence, a hospitalisation from the centre or from home, a day cut short, and the unannounced absence.
:::

:::{rh-faq}
A user is on holiday. Do I record each day they do not come?
: No. Record one absence, from the first day to the return. Until it ends, the user is not expected: the screen at the door, the register and the care leave them out.

A user on holiday comes back without warning. What do I do?
: Tick them in as usual. The arrival ends the absence under way, and the file says they are back.

The register refuses a day. Why?
: The day lies inside an absence already closed: the record says the user was away. Correct the absence first if they came that day.

A user left the centre for hospital at 11:00. Does the day earn the forfait?
: Yes. A day cut short by a hospitalisation or a death earns the forfait, however short.

What is an unannounced absence?
: A day the user was expected and did not come, without warning. It is kept apart from the register and billed only where the centre's rules of procedure provide for it.
:::

A day care user is away every day they do not come. What the centre records
is the exception: a **declared absence** — a holiday, a stay in hospital — and
the **unannounced absence**, a day the user was expected and did not come
without warning.

## A declared absence

Record the absence as for any resident, with its **Absence Type** —
**Hospitalization**, **Vacation**, **Family Outing** or **Other** — its
departure, and its return once known. See
[Absences and hospitalisations](../../facturation/absences.md).

For a day care user, an absence means **away until the return**, whatever its
type:

- the screen at the door does not expect the user: the card says since when
  they are away, without a **Did not come** button;
- the register of the day shows the absence in its **Absence** column;
- the care, the medication and the meals of these days are not planned;
- no unannounced absence can be recorded on these days, and nothing is billed
  for them: a day care centre bills the days in its register, never a day of
  absence.

### When the user comes back

- **An absence under way** ends when the user is ticked in: at the door, in
  the register or with **Add a day of attendance**. The absence closes at the
  arrival, and the file says the user is back. Back from hospital, the
  treatments and the care resume. **Add a day of attendance** says it before
  saving.
- **An absence already closed** holds its days: a day inside it is refused by
  the register. Correct the absence first if the user did come that day.
- An absence confirmed over a day the register already holds whole is
  refused, and the absence form says so.

A draft absence with no return is a form being filled in: it holds no day.

## A hospitalisation from the user's file

Click **Hospital departure** on the user's file, as for any resident. When
WideCare cannot tell where the user was — it is one of their days, the centre
is open, and nobody has ticked them in — the dialog asks **Left From**:

- **The day centre**: give the hour they **Arrived At**. The day is written in
  the register from that hour to the departure, as **Hospitalised during the
  day**: it earns the forfait.
- **Home**: nothing is written in the day centre's register.

When the register already knows — the user was ticked in and has not left,
or it is not one of their days — the dialog asks nothing: a user present is
marked **Hospitalised during the day**, at the hour of the departure; a user
who was not at the centre leaves the register as it is.

<!-- screenshot to add: the Hospital departure dialog of a day care user, with Left From set to The day centre and the Arrived At hour -->

## A day cut short in the register

The other way round, the register can say it first: choose **Hospitalised
during the day** or **Died during the day** under **Day Cut Short**, at the
door, in the register or in **Add a day of attendance**.

- **Hospitalised during the day** opens the hospital absence, exactly as the
  **Hospital departure** of the file: the prescriptions are suspended and the
  care of the day cancelled. Today, the departure takes the current hour when
  none was typed.
- **Died during the day** records the date of death on the file, which
  closes the stay.

Either way, the day earns the forfait. The register is never undone by the
file: an absence or a date of death is corrected where it lives.

## The unannounced absence

A user who was expected and did not come, without warning, did not come:
from 13:00, the register counts them absent and their care of the day is
cancelled. When the centre's rules of procedure bill such a day, record it as
an **unannounced absence**:

- at the door, from 13:00: **Did not come** on the user's card;
- on the user's file: **Add a day of attendance**, then tick **Did Not Come**;
- in the list **Day care centre → Register → Unannounced absences**.

Each line carries its **Reason** — **Did not come, not announced** or
**Announced too late** — and **Billable**, ticked by default.

<!-- screenshot to add: the Unannounced absences list, with the Reason and Billable columns -->

An unannounced absence is refused:

- before 13:00 — the user may still come;
- on a day the user is in the register;
- on a day the centre is closed;
- on a day of a declared absence.

A billable day is billed with the **Day care unannounced absence** supplement,
to the users who have that supplement in their conventions. An absence
recorded on a past day is amended only by a manager, and is kept in the audit
log. See [Billing a day care month](facturation.md).

## What's next

- [Recording attendance](presences.md) — the screen at the door and the register.
- [Care for a day care user](soins.md) — what the absence does to the care of the day.
