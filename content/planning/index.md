---
modules: [healthcare_planning]
sectors: [mr, csj]
---

# Staff planning

:::{rh-description}
The Planning application plans the care staff's shifts by role and sector, checks the staff needed at critical times, and sends each person their schedule.
:::

:::{rh-faq}
What is the Planning application for?
: It builds the schedule of the care teams: shifts by role, sector and team, drafted, then confirmed and sent to the staff. It also compares the hours planned with each contract and with the staff needed at critical times of the day.

Do I need the Care application to use Planning?
: No. Planning is an application of its own on the home screen. It uses the sectors, the teams and the staff records, not the residents' care records.

Who sees what in Planning?
: A user sees the confirmed shifts of their team and their own shifts. A manager sees and plans every shift. An administrator also changes the settings, the roles, the critical periods and the schedule templates.

Do the staff see a shift as soon as it is created?
: No. A new shift is a draft, seen only by the planners. It becomes visible to the staff when it is confirmed, and the staff concerned are told when the schedule is sent.

Can a staff member take a free shift?
: Yes, when the setting allows it: a confirmed shift without anyone appears in Open shifts, and anyone holding its role can take it, from the back office or from the personal page opened from the schedule email.
:::

:::{toctree}
:hidden:

configuration
construire-le-planning
postes-du-personnel
heures-et-couverture
prestations-presences
:::

The **Planning** application organises the **shifts of the care staff**: who
works, in which **role**, in which **sector**, from what time to what time. It
has its own tile on the home screen and does not need the care records: the
people who build the schedule and those who read it do not all work in the
residents' files.

<!-- screenshot to add: the Planning schedule over a week, rows by role then staff member, open shifts on top, critical periods banner above -->

## How it works

1. **Configure** the roles to plan, the critical periods of the day and one or
   more schedule templates (administrator). → [Configure the planning](configuration.md)
2. **Lay the shifts** of a week or a month from a template, in draft and
   without anyone.
3. **Plan the staff**: let **Auto plan the open shifts** fill them, then adjust
   by hand. A shift that breaks a rule is marked **To check**.
4. **Confirm** the drafts: the staff now see them.
5. **Send the schedule**: only the people whose shifts changed receive an
   email, with a link to their personal page.
   → [Build the schedule](construire-le-planning.md)

The staff read their shifts in **My shifts** or on their personal page, and take
an **open shift** when one is offered to their role.
→ [Shifts for the staff](postes-du-personnel.md)

## Main menus

- **Schedule** — every shift, opened on the schedule chart, with the calendar,
  list, kanban, pivot and graph views.
- **My shifts** — your own published shifts.
- **Open shifts** — the confirmed shifts that still have nobody.
- **Staff preferences** — the availabilities and wishes of each staff member
  (managers).
- **Reporting** — **Planned hours**, **Critical period coverage** and, with the
  Attendances app, **Planned versus attended** (managers).
  → [Hours, balance and coverage](heures-et-couverture.md)
- **Configuration** — **Settings**, **Roles**, **Critical periods**,
  **Schedule templates** (administrators).

## Access levels

The level of each person is set on their **user**, in the **Staff planning**
field:

| Level | Sees | Does |
| --- | --- | --- |
| **No access** | Nothing | — |
| **User — their team, published shifts** | The confirmed shifts of their team, their own shifts and the shifts without a team | Takes an open shift of their role |
| **Manager — every shift, no settings** | Every shift | Applies templates, plans automatically, confirms, sends the schedule, edits preferences |
| **Administrator — everything and the settings** | Everything | Also the settings, roles, critical periods and schedule templates |

:::{note}
A user whose staff record has no team is not limited to one team: they see
every confirmed shift.
:::

## Care tasks and the schedule

When the care records are installed, the confirmed shifts can also be used to
share out the day's care tasks between the care staff on duty. This is a care
setting, off by default; while it is off, nothing about it shows in the care
screens. See [Automatic assignment of care tasks](../soins/assignation-automatique.md).

## Going further

- [Configure the planning](configuration.md)
- [Build the schedule](construire-le-planning.md)
- [Shifts for the staff](postes-du-personnel.md)
- [Hours, balance and coverage](heures-et-couverture.md)
- [Work entries from attendances](prestations-presences.md)
- [Automatic assignment of care tasks](../soins/assignation-automatique.md)
