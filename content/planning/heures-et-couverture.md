---
modules: [healthcare_planning, healthcare_planning_attendance]
sectors: [mr, csj]
---

# Hours, balance and coverage

:::{rh-description}
Follow the staff hours in WideCare: planned hours against each contract, the hours balance, the coverage of the critical periods and, with attendances, the hours planned against the hours worked.
:::

:::{rh-faq}
Where do I compare the planned hours with the contracts?
: In Planning → Reporting → Planned hours: per staff member and day, the planned hours, the hours of the contract and the difference.

What is the hours balance?
: The hours performed minus the hours due by the contract, leaves deducted, since the start of the balance period chosen in the settings (month, quarter or year). Positive: ahead of the contract; negative: behind it.

How do I know whether there were enough staff at lunch every day last week?
: Open Planning → Reporting → Critical period coverage, choose the dates and click Show. Each day, period and role is marked Under-planned, As needed or Over-planned.

How do I see who did not come to a planned shift?
: With the Attendances app installed, each past shift shows its worked hours and an Attendance badge: Worked, Partly worked or No attendance. Planning → Reporting → Planned versus attended sums it up per staff member and day.
:::

The **Reporting** menu of Planning is reserved for planning managers. It answers
three questions: are the contracts respected, are the critical times covered,
and was the schedule actually worked.

## Planned hours

Open **Planning → Reporting → Planned hours**. Per **staff member** and **day**:

- **Planned hours** — the hours of their shifts;
- **Contract hours** — the hours the working schedule of the contract asks for,
  leaves deducted;
- **Difference** — planned minus contract.

The report opens as a pivot table by week; switch to the graph or the list.
Filter on **Confirmed shifts** or **This week**, and group by **Staff member**,
**Role**, **Sector**, **Team**, **Week** or **Day**.

:::{note}
The contract hours belong to a person, not to a role or a sector: grouped by
role or sector, they fall under "None".
:::

## Hours on the staff record

The **Planning** tab of each staff record shows the person's figures:
**Contract hours per week**, **Planned this week**, **Planned this month**,
**Due this month** and the **Hours balance**, counted since the date shown
beside it.

- The **hours balance** is the hours performed minus the hours due by the
  contract, leaves deducted, since the start of the balance period (setting
  **Hours balance**: month, quarter or year), or since the first shift if it
  came later.
- Without the Attendances app, the hours performed are those of the confirmed
  shifts already finished. With it, they are the hours of the attendances.
- A **part-time** contract planned beyond its hours shows a warning on the
  record: an amendment to the contract may be needed.

The automatic planning uses this balance: a person behind on their contract
gets priority, a person ahead steps back.

## Critical period coverage

Open **Planning → Reporting → Critical period coverage**:

1. Choose the dates (three months at most).
2. Tick or untick **Count draft shifts** (unticked: only the confirmed shifts
   count, as the staff see them).
3. Click **Show**.

Each line gives a **day**, a **Critical period**, a **Role**, the **Planned** and
**Needed** hours, the **Gap**, the **Residents present** (for a rule per
residents) and a **Status**:

- **Under-planned** (red) — not enough staff;
- **As needed** (green);
- **Over-planned** (orange) — more than needed.

Filter on **Under-planned** or **Over-planned**, or switch to the pivot table.
The same colours appear on the schedule chart, period by period. See [Build the
schedule](construire-le-planning.md).

<!-- screenshot to add: Critical period coverage list with coloured lines by day, period and role -->

## Planned versus attended

When the **Attendances** app is installed, WideCare sets each shift against the
attendances of its staff member (managers only):

- on the shift, **Worked** gives the hours of attendance within the shift, and an
  **Attendance** badge says **Upcoming**, **Worked**, **Partly worked** or **No
  attendance**; the **Attendances** button opens the attendances concerned;
- the shift list shows the same two columns;
- the staff record adds **Attended this month** to its hours.

**Planning → Reporting → Planned versus attended** sets the **Planned** hours
against the **Attended** hours per staff member and day, with the
**Difference** (attended minus planned). A difference beyond a quarter of an
hour is coloured; the **With a difference** filter keeps only those lines.

Only confirmed shifts that have already started are compared: a shift of
tomorrow has no attendance yet.

## Learn more

- [Configure the planning](configuration.md)
- [Build the schedule](construire-le-planning.md)
- [Work entries from attendances](prestations-presences.md)
