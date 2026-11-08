---
modules: [healthcare_accommodation_helpdesk]
---

# Technical interventions

:::{rh-description}
Technical interventions in the residents' rooms with Resthome and the Helpdesk app: a ticket linked to the resident, the room and the stay, and its full cost.
:::

:::{rh-faq}
What is a technical intervention in Resthome?
: A Helpdesk ticket of a room maintenance team: a repair or a job in a resident's room, linked to the resident, the room and the stay, with what it cost.

What does an intervention cost?
: The products used, the time spent (from the timesheets) and, when an outside provider did the job, their vendor bill. Resthome adds them up in **Ticket Cost**.

Where do I find the interventions of a room or a resident?
: On the room, the resident's record and the stay: an **Interventions** button lists them, as soon as there is one.

Is the intervention billed to the resident?
: Only if you decide so, with **Bill the intervention** on the ticket. See [Billing an intervention](facturer.md).
:::

:::{toctree}
:hidden:

suivre-une-intervention
facturer
:::

A dripping tap, a broken bed rail, a lamp to replace: the technical team handles
the residents' rooms through the **Helpdesk** app. Resthome turns the tickets of
a **room maintenance** team into **interventions**: each one knows the resident,
the room and the stay concerned, and adds up what it cost.

:::{admonition} Prerequisite
:class: info

Interventions rely on the **Helpdesk** app and its timesheets. Once Helpdesk is
installed, turn on **Rooms maintenance** on the team that handles the rooms.
:::

## Set up the room maintenance team

1. Open **Helpdesk → Configuration → Helpdesk Teams** and the team that
   handles the rooms (or create one).
2. Tick **Rooms maintenance**. **Timesheets** turns on with it: the time spent
   is part of the cost.
3. Save.

Only the tickets of a team with **Rooms maintenance** show the **Resident**,
**Room** and **Resident Stay** fields and the **Products** tab. The other
Helpdesk teams are left as they are.

:::{admonition} Billing to the resident
:class: note

When intervention billing is installed, the same setting also asks for an
**Intervention Service Product**: see [Billing an intervention](facturer.md).
:::

## What an intervention brings together

| Part | Where it comes from |
| --- | --- |
| **Resident**, **Room**, **Resident Stay** | Chosen on the ticket; the room and the stay are filled in from the resident |
| **Products** | The products used, valued at their cost |
| **Timesheets** | The time spent by the technicians, valued at their hourly cost |
| **Vendor Bill** | The invoice of an outside provider, when the job was subcontracted |
| **Ticket Cost** | The total of the three |

The ticket's **Requestant** is the person who asked for the intervention —
the resident by default.

## What's next

- [Following an intervention](suivre-une-intervention.md) — create, value and find interventions.
- [Billing an intervention](facturer.md) — charge the cost to the resident.
- [Rooms](../residents/chambres.md)
