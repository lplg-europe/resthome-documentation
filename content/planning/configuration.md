---
modules: [healthcare_planning]
sectors: [mr, csj]
---

# Configure the planning

:::{rh-description}
Set up staff planning: the roles to plan, the settings of the automatic planning, critical periods with the staff needed, schedule templates and each staff member's hours and preferences.
:::

:::{rh-faq}
Where are the planning settings?
: In Planning → Configuration → Settings, or in the Settings app under Planning. They are set per establishment and are reserved for planning administrators.

Where do the roles of the planning come from?
: They are the staff roles of the Employees app. In Planning → Configuration → Roles, click Add a role and pick one from the list; a role is never typed in Planning.

What is a critical period?
: A time of day the establishment watches closely — rising, lunch, bedtime, the night — with the staff each role must supply during it, either a fixed headcount or one person per number of residents present.

What is the difference between a hard and a soft preference?
: The automatic planning never breaks a hard preference ("never on Wednesdays"). A soft preference only weighs on the choice ("rather mornings").

Why does a part-time staff record show a warning?
: Because the person is planned beyond the hours of their contract, this week or this month. The warning suggests a contract amendment may be needed.
:::

The planning is configured once by a **planning administrator**, then adjusted at
the margins: a new role to plan, a critical period, a different typical week.

## Settings

Open **Planning → Configuration → Settings** (or the **Settings** app, section
**Planning**). The settings apply to the current establishment.

| Setting | What it does |
| --- | --- |
| **Schedule email** | The email each staff member receives with their shifts. |
| **Open shifts** | When ticked, the staff take a published shift without anyone, if they hold its role. On by default. |
| **Rest between two working days** | The hours the automatic planning leaves between the end of a working day and the start of the next one. 11:00 by default. Taking an open shift respects the same rest. |
| **Hours balance** | The period over which the hours performed are set against the contract: **Month**, **Quarter** (default) or **Year**. |
| **Weekly flexibility** | How far a full-time contract may be planned above its week (5:00 by default); its hours are then held over the period of the hours balance. A part-time contract gets none. |

The **Configuration** block of the same page links to the **Roles**, **Critical
periods** and **Schedule templates**.

## Roles to plan

A shift is always planned for a **role** (nurse, care assistant…). The roles are
the **staff roles** of the Employees app; Planning only says which of them it
plans.

1. Open **Planning → Configuration → Roles**.
2. Click **Add a role**, pick the role from the list, then choose its **Team** and
   its **Colour**.
3. Click **Add**.

In the list, drag the rows to set the order of the roles in the schedule, and
change the team or colour in place. To stop planning a role, select it and click
**Remove from the planning**: the role stays a staff role, the schedule no longer
shows it.

- **Team** — the team an open shift of this role belongs to until someone takes
  it. It decides which users see the shift.
- **Colour** — the colour of the role's shifts in the schedule.

New roles are created and renamed in the Employees app, under
**Configuration → Roles**.

<!-- screenshot to add: Planning → Configuration → Roles list with the Add a role and Remove from the planning buttons -->

## Staff records

The schedule plans **staff members** (employees). On each staff record:

- **Work** tab — the person's **Role**. It is planned as it is.
- **Planning** tab, **Roles** — **Other planning roles**: the roles the person
  can also stand in for, besides their own.
- **Planning** tab, **Hours** — read-only figures: **Contract hours per week**,
  **Part time**, **Planned this week**, **Planned this month**, **Due this
  month** and the **Hours balance** with the date it is counted from.
- **Planning** tab, **Scheduling preferences** — the person's preferences (see
  below).
- **Nursing Home** tab, **Scheduling** — **Preferred Shift**, **Personal weekly
  maximum** (the most hours this person may be planned in one week; empty = the
  contract plus the weekly flexibility for a full time), **Can Work Night
  Shifts**, **Can Work Weekends**.
- **Nursing Home** tab, **Sectors** — the **Assigned Sectors**: the automatic
  planning prefers a person in the sector they are assigned to.

A **Shifts** button at the top of the record opens the person's shifts.

:::{admonition} Contract amendment warning
:class: warning

When a **part-time** contract is planned beyond its hours this week or this
month, a yellow banner appears at the top of the staff record: an amendment to
the contract may be needed. A full-time contract never gets the banner: its
extra hours are held over the period of the hours balance.
:::

<!-- screenshot to add: Planning tab of a staff record with the other roles, the hours and the scheduling preferences -->

## Scheduling preferences

Preferences are entered on the staff record (**Planning** tab) or for everyone
in **Planning → Staff preferences**, grouped by staff member.

| Field | Meaning |
| --- | --- |
| **Strength** | **Hard**: the automatic planning never breaks it. **Soft**: it only weighs on the choice. |
| **Availability** | **Unavailable** or **Available**. |
| **Day** | The day of the week; empty = every day. |
| **From** / **To** | The hours concerned. |
| **Sector** | Only shifts of this sector; empty = any sector. |
| **Valid from** / **Valid until** | Limits the preference to a period. |
| **Note** | A free comment. |

A hard **Available** preference restricts that day to the shifts that start
within its hours. A hard unavailability shows in red in the list, an
availability in green.

## Critical periods

A **critical period** is a time of day when enough staff must be present.
Open **Planning → Configuration → Critical periods** and create one:

1. Give it a name (rising, lunch, bedtime, night…) and its **Hours**. An end
   before the start means the period ends the next day.
2. Choose the **Sectors** it watches; empty = the whole establishment.
3. Tick the **Days** it applies to.
4. Under **Staff needed**, add one line per role:
   - **Rule** — **Fixed headcount**, or **Per residents present**;
   - **Staff** — the people needed at the same time (with **Per residents
     present**, the minimum whatever the occupancy);
   - **Residents per staff member** — with **Per residents present** only.

The planned hours of the role during the period are set against the staff
needed × the length of the period. Only shifts held by someone count.

:::{note}
With **Per residents present**, the residents counted are those staying in the
rooms of the period's sectors that day, **minus the residents absent** that day
(hospital stay, leave).
:::

The schedule then shows, above the shifts, whether each period is covered. See
[Build the schedule](construire-le-planning.md) and [Hours, balance and
coverage](heures-et-couverture.md).

## Schedule templates

A **schedule template** holds the empty shifts a typical week needs. Open
**Planning → Configuration → Schedule templates** and create one:

- **Applied to** — **Week** (applied to one week) or **Month** (applied to every
  day of a month, week after week).
- One line per shift: **Day**, **From**, **To** (an end before the start = a
  night ending the next day), **Role**, **Sector**, **Label** (AM, PM, Night…)
  and **Quantity** (identical shifts to create).
- **Shifts per week** counts the shifts the template lays.
- A note says what the template is for.

Applying a template never touches existing shifts. See [Build the
schedule](construire-le-planning.md).

<!-- screenshot to add: a schedule template form with its lines by day, hours, role, sector and label -->

## Users' access

On each **user**, the **Staff planning** field sets the access level: **No
access**, **User — their team, published shifts**, **Manager — every shift, no
settings** or **Administrator — everything and the settings**. See [Staff
planning](index.md).

## Learn more

- [Build the schedule](construire-le-planning.md)
- [Shifts for the staff](postes-du-personnel.md)
- [Hours, balance and coverage](heures-et-couverture.md)
