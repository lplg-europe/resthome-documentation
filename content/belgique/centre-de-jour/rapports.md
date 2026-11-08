---
modules: [resthome_day_care, resthome_day_care_reporting]
sectors: [csj]
---

# Day care figures

:::{rh-description}
The figures of a day care centre (CSJ) in WideCare: attendance days by category and insurer, places occupancy, the printed register, and the CSJ column of the management dashboards.
:::

:::{rh-faq}
How many days did each category bring this year?
: **Day care centre → Reporting → Day care statistics**: the attendance days and the forfait days by month and by CSJ category, this year by default.

How full is the centre?
: **Day care centre → Reporting → Places occupancy**: who came each open day against the places the approval licenses, as an occupancy rate.

Who can see these figures?
: The managers, and whoever may amend a closed register day.

Do the management dashboards count the day care users?
: Yes, in a CSJ column of their own, on the days of the register only — never every calendar day of the stay.
:::

A day care centre reads its activity in days attended, not in nights. Its
figures come from the **attendance register**: a user counts on the days they
came, never on the days their stay merely spans.

## Day care statistics

**Day care centre → Reporting → Day care statistics** opens a pivot table
and a chart of the days recorded, one line per day someone came, with the
CSJ category in force that day and the user's insurer.

- **Attendance Days** counts the days recorded; **Forfait Days** the ones
  that earn the forfait.
- The table reads by month and by **Category**; the chart stacks the
  categories month after month.
- The filters **Forfait due**, **Forfait not due** and **This year** narrow
  it; it groups by **Insurer (OA)**, **Category**, **User** or **Quarter**.

<!-- screenshot to add: Day care statistics, the attendance days by month and CSJ category -->

## Places occupancy

**Day care centre → Reporting → Places occupancy** compares, for each day,
the users who **Came** with the **Places** the approval licenses: the
**Occupancy** rate, week after week. It opens on the days the centre opened
this year.

- **Open days** keeps the days the centre opens; **Over the places** the days
  more users came than places.
- The pivot table can also show the **Forfait Days** of each period, from its
  measures.

<!-- screenshot to add: Places occupancy, the weekly occupancy rate of the year -->

## The billing dashboard

**Billing → Dashboard** carries a card for the centre: **Day care today**
(present against approved places), **Register not kept** (open days of the
last 30 with nobody recorded) and **Day care agreements to renew**. See
[Billing a day care month](facturation.md).

## Printed documents

- **Print the day care register** — the register between two dates, one table
  per month or one page per day, for an inspection. See
  [Recording attendance](presences.md).
- **Staffing norm check** — the yearly check, printed from the check itself.
  See [The staffing norm](norme-personnel.md).

Every print of the register is logged.

## The management dashboards

When the management reporting is installed, its dashboards carry a **CSJ**
column next to the rest home sectors:

- **Residents & Occupancy** — the users and the days by sector;
- **Movements** — admissions and departures, day care included;
- **Days of Presence & Billing** — the days of presence by sector and
  category, against the days billed.

A day care user is counted on the days of the register only. **Movements**
and **Days of Presence & Billing** can be filtered by **Beneficiary Status** —
**Beneficiary**, **Non-beneficiary (covered)** or **Outside INAMI financing**
— down to the days billed.

The **Healthcare → Reports → Occupancy Analysis** report adds, for a day care
user, the **CSJ Category** of the day and whether the **CSJ Forfait Due**
that day.

## What's next

- [Recording attendance](presences.md) — where every figure comes from.
- [The staffing norm](norme-personnel.md) — the billed days that decide the norm.
