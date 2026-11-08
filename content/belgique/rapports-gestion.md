---
modules: [resthome_reporting]
---

# Management reports

:::{rh-description}
The reports of a Belgian nursing home in Resthome: the KAPPA control documents, the movement list and analysis, the occupancy of rooms and sectors, occupancy by approval and Katz category, the residence certificate and the management dashboards.
:::

:::{rh-faq}
Where are the management reports?
: In **Nursing Home → Reports**: KAPPA control, Movement list, Movements, Occupancy Analysis and Occupancy by approval. The last three are reserved to managers.

What does Resthome print for a KAPPA control?
: **Nursing Home → Reports → KAPPA control**: the alphabetical list of the patients for the draw, the patients present with their Katz category for the sealed envelope, the staff under contract that day, and a preparation page that stays in the house.

How long did a room stand empty this year?
: **Nursing Home → Reports → Occupancy Analysis** shows, room by room and sector by sector, the days in the period, the days of presence, the days without presence and the occupancy rate. It opens on the current year.

Does a hospital stay count as an empty bed?
: No. The bed is still held by the resident's stay: the days of a hospital stay or a holiday count as presence in the occupancy analysis.

Where do I print a residence certificate?
: On the resident's record, **Documents** tab, tile **Residence certificate**, while the resident has a stay in progress.
:::

The **Reports** menu gathers what a Belgian home hands over to an inspection
and reads back to steer the house: the KAPPA documents, the movements, the
occupancy of beds and rooms.

Menu: **Nursing Home → Reports**.

| Report | What it answers | Who |
|---|---|---|
| **KAPPA control** | The documents to hand over on the day of a KAPPA control. | Users of the app |
| **Movement list** | The printed list of admissions, transfers, exits and absences over a period. | Users of the app |
| **Movements** | The same movements, to filter and count. | Managers |
| **Occupancy Analysis** | How many days each room and sector was occupied, or empty. | Managers |
| **Occupancy by approval** | The residents by Katz category and sector, against the approved beds. | Managers |

## The KAPPA control

A **KAPPA control** is the visit of a local college of the mutualités'
advisory physicians and nurses, who re-assess the Katz scale of a sample of
residents and compare it with the home's. Resthome prepares the documents the
home hands over on that day.

1. Open **Nursing Home → Reports → KAPPA control** — or **Nursing Care →
   Reports → KAPPA control** for the head nurse and the medical manager.
2. Check the **Control date and time** (now by default) and, with several
   houses, the **Establishment**.
3. Tick **Include the day care centre** only if its users must be listed too.
4. Click **Print**.

The PDF holds one document per page:

1. the **alphabetical list of the patients**, which the college draws from;
2. the **patients present with their dependency category**, for the sealed
   envelope;
3. the **staff under contract or appointed** on that day;
4. a **preparation** page — an internal document, **not to hand over** — with,
   for each resident, the Katz in force, its date, what the mutualité agreed and
   what was billed, and the changes pending.

Everything is read at the **time of the control**. The staff list comes out
for those who prepare the control: the head nurse, the medical manager, the
management and the HR users.

<!-- screenshot to add: the KAPPA control window with the date, the establishment and the day care centre box -->

## The movements

### The movement list (print)

**Nursing Home → Reports → Movement list** prints the movements of a period,
grouped by type:

1. Set **From** and **To** — last month by default.
2. Choose the **Establishment** if needed, and **Include the day care centre**
   if its users count.
3. Click **Print**.

### The movement analysis

**Nursing Home → Reports → Movements** lists the same movements, one line per
dated event:

- **Admission** and **Readmission**;
- **Internal transfer** (with the sector left, **From sector**);
- **Definitive exit** (with the **Departure Reason** and the day the room was
  freed);
- **Absence departure** and **Return from absence** (with the **Absence Type**
  and the destination).

Each line shows the date and time, the resident, the room, the sector and the
Katz category in force that day. The filters **Admissions**, **Internal
transfers**, **Definitive exits**, **Absences** and **Date** narrow the list; the
pivot view counts the movements by type and sector, by month if you group by
**Month**.

## Occupancy of the rooms

**Nursing Home → Reports → Occupancy Analysis** reads the occupancy from the
**rooms**: every room, every day, whether a stay held its beds.

The pivot table opens on the **current year**, with one row per sector and,
under it, its rooms (the establishment first, with several houses). Four
measures:

| Measure | Meaning |
|---|---|
| **Days in period** | The days of the period up to today, once per bed. |
| **Days of presence** | The bed-days a stay held. |
| **Days without presence** | The bed-days no stay held. |
| **Occupancy rate** | Days of presence over days in period. |

:::{admonition} How the days are counted
:class: note

- Everything counts **bed-days**: a double room counts two a day.
- A bed is held from the day its stay is **confirmed**, and an **ended** stay
  still counts for the days it covered.
- A **hospital stay** or a **holiday** does not free the bed: those days count as
  presence.
- The days to come are not counted: "this year" means the year so far.
- The sector shown is the room's **current** sector.
:::

Change the **Period** in the search bar, keep only the **Days without
presence**, or group by **Sector**, **Room**, **Room Type**, **Month** or
**Establishment**. The list view shows the same figures day by day.

<!-- screenshot to add: Occupancy Analysis pivot, sectors and rooms in rows, the four measures in columns -->

## Occupancy by approval

**Nursing Home → Reports → Occupancy by approval** counts the **residents** by
**Katz category** (rows) and **sector** (columns), next to the **approved beds**
of each sector. It opens on **today**.

The filters answer the inspection's questions: **Present**, **Absent**,
**Hospitalized**, **Without valid Katz**, **Katz expiring (30 days)**, and the
beneficiary status — **Beneficiaries**, **Non-beneficiaries (covered)**,
**Outside INAMI financing**. The list view, grouped by resident, shows each
resident's day, room, stay type, category and absence.

For the quarter's occupancy against the approved beds and the residents an MRS
bed could take, see [Occupancy MR / CS / MRS](occupation-mr-mrs.md).

## The residence certificate

On a resident's record, the **Documents** tab carries a **Residence
certificate** tile while a stay is in progress. It prints a certificate, signed
by the house, stating that the resident lives there and since when.

## The management dashboards

The **Dashboards** app has a **Rest Home** section, each dashboard for the roles
it concerns:

| Dashboard | Content | Who |
|---|---|---|
| **Residents & Occupancy** | Residents by Katz category and sector, filterable by day. | Managers |
| **Movements** | Admissions, transfers, exits and absences. | Managers |
| **Days of Presence & Billing** | Stay days against the days billed, by sector and Katz category. | Management and administrators |
| **Billing & eFact** | Amounts billed by payer, eFact batches and claims to the mutualités, billing periods, admission pipeline. | Management and administrators |
| **Care Quality** | Falls, infections, restraints in force, open clinical follow-ups. | Head nurse, medical manager, administrators |

**Care Quality** is also reachable from **Nursing Care → Reports → Care
Quality**. The institutional allowance has its own dashboard — see
[Simulations and live tracking](forfait/suivi-simulations.md).

<!-- screenshot to add: the Residents & Occupancy dashboard with the Katz × sector table -->

## Further reading

- [Occupancy MR / CS / MRS](occupation-mr-mrs.md)
- [The Katz assessment](katz.md)
- [Rooms and occupancy](../residents/chambres.md)
- [Day care figures](centre-de-jour/rapports.md)
