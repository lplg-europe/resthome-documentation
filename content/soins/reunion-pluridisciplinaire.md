---
modules: [healthcare_medical, resthome_geriatric]
sectors: [mr, csj]
---

# Multidisciplinary meetings

:::{rh-description}
The multidisciplinary meeting in WideCare: plan it, load the residents waiting, re-evaluate each one from a checklist of where things stand, turn decisions into care, ask for a scale as a task to plan, review records, and print the minutes.
:::

:::{rh-faq}
Which residents does "Load pending residents" add?
: Every resident whose care plan review is overdue, whose record is waiting to be re-read, whose care plan is missing or still a draft, or who has a critical observation since the last meeting. It can be pressed again: it only adds those who became due since.

How do I turn a decision into a care?
: On the resident's re-evaluation, click **Add to the care plan**: the care is added to the plan and carried by the worklist. Press it again for the next decision.

What happens when I ask for a scale during the meeting?
: The button on the checklist (New Braden, New MNA, Weigh…) creates a care task to plan, described as asked by the meeting. The checklist line then shows who asked for it and when, and the minutes say "requested".

What if the meeting does not get to a resident?
: Click **Carry over**: the resident stays pending for the next meeting.

Can I hold the meeting every week at the same time?
: Yes. A **recurring meeting** plans the next ones ahead, with their attendees, location and standing agenda.
:::

The **multidisciplinary meeting** brings the team together to re-read the
residents' situation and adjust their care plans. WideCare prepares the
agenda, shows each resident's situation on one page, and writes the minutes.

## Find the meetings

- **Nursing Care → Care → Plans and Meetings → Multidisciplinary Meetings** — the meetings, as a list or a calendar.
- **Nursing Care → Care → Plans and Meetings → Reviews in Meeting** — each resident's re-evaluation (filters **To do**, **Done**, **Carried over**).
- **Nursing Care → Reports → Record Reviews** — the record reviews.
- **Nursing Care → Reports → Plan Reviews** — the care plan reviews.
- **Nursing Care → Configuration → Recurring Meetings** — the recurring meetings.

Meeting filters: **Upcoming**, **In Progress**, **Done**, **My Meetings**.

## The life of a meeting

| State | Next step |
|---|---|
| **Draft** | **Plan** announces it on the care dashboard; **Start** opens it if it takes place now |
| **Planned** | On the day, **Start** opens each resident's re-evaluation |
| **In Progress** | Open each resident, record the re-evaluation, then **Close the meeting** |
| **Done** | **Print the minutes** |
| **Cancelled** | — |

A blue note at the top of the meeting always says the next step.

<!-- screenshot to add: a meeting in progress with its resident cards and their badges -->

## 1. Prepare the agenda

1. Click **New**, give the title, the date and time, the duration, the
   location, the organizer and the attendees.
2. In the **Residents** tab:
   - **Add residents** picks them by unit;
   - **Load pending residents** adds those waiting (see the FAQ).
3. Each resident gets a card: age, sex, dependency, room, sector, when they
   were last discussed, and a badge **Discuss first**, **To discuss** or
   **Recently discussed**. The **×** takes a resident off the agenda.
4. The **Agenda** tab holds the points to discuss besides the residents.

A resident without a care plan shows **Create the care plan**; a draft plan,
**Activate the care plan**.

## 2. Re-evaluate each resident

Click a resident's card. The re-evaluation opens, with:

- the **Care plan** (and its status) and the care already **put on the plan**;
- **Where things stand** — a checklist of the resident's follow-up: scales,
  weighing, registers, objectives, each with its status (**Up to date**, **Due
  soon**, **Attention**, **Overdue**, **Never done**), a **New** badge for what
  changed since the last meeting, and the period read;
- **Observations of the period**, the most important first;
- **Objectives** — the plan's objectives, to adjust;
- **Decisions** — what was decided for this resident;
- **Record reviews** — the reviews of the record still open.

### Act from the checklist

Each checklist line carries its button: **New Braden**, **New MNA**, **New
MMSE**, **New Tinetti**, **Weigh**, **Register a fall**, **Fall risk (Morse)**,
**Open a wound register**, **Open a continence register**, **New restraint**,
**Lift the restraint**, **New objective**…

:::{admonition} A request becomes a task to plan
:class: tip

A scale or a record asked during the meeting is not filled in there: it
becomes a **care task** for the resident, described as asked by the meeting.
The checklist line then shows who asked for it and when, and the minutes note
it as requested. The care staff fill it in from the task. See
[Care tasks](taches-de-soins.md).
:::

### Decide and record

1. Write the **Decisions**.
2. **Add to the care plan** turns a decision into a care on the plan; press it
   again for the next decision.
3. **Record the re-evaluation** (meeting in progress) closes it: the care plan
   review is written down. **Refresh** reloads the checklist.
4. **Carry over** leaves the resident for the next meeting.

The resident's card on the meeting then shows **Plan review due**, **Plan
adjusted**, **To do** or **Carried over**. The **Re-evaluated** smart button
counts the residents done.

## 3. Close and print

**Close the meeting** when every resident is handled. The **Minutes** tab holds
the **Decisions by resident** and the notes; **Print the minutes** gives the
PDF.

## Record reviews

A **record review** asks the team to re-read a resident's record. It is
created:

- **Periodic**, on the house's rhythm;
- **Requested by a carer**;
- **After a fall**;
- **After a return from hospital**.

Each review is **To do**, **Reviewed** or **Not needed** (with a required
conclusion). **Mark reviewed** and **Not needed** close it; **Open what
triggered it** shows the fall or the return. The meeting's **Record reviews**
tab lists those of the resident; the ones still open when the re-evaluation is
recorded are closed with its decisions. Filters: **To do**, **Overdue**,
**Reviewed**.

## Plan reviews

Each care plan review — validated after revision, confirmed without change,
or recorded in a meeting — is written down. **Nursing Care → Reports → Plan
Reviews** lists them, with the filters **Confirmed without change**,
**Adapted** and **In a meeting**. See [Care plans](plans-de-soins.md).

## Recurring meetings

**Nursing Care → Configuration → Recurring Meetings** (head nurses and
management) plans meetings on a fixed rhythm:

- **Weekday**, **Time**, **Duration** and **Location**;
- **Planned Ahead** — how many days before, the next meeting is created;
- the organizer and the attendees, and who mandated the meeting;
- the **Meeting Title** and the **Standing Agenda**;
- **Also on the Agenda** and **Add the Residents Waiting** — what each meeting
  loads by itself.

**Plan the next meeting** creates it at once; **Meetings** lists those already
planned.

## Going further

- [Care plans](plans-de-soins.md)
- [Evaluations to validate](evaluations-a-valider.md)
- [Clinical registers](registres.md)
