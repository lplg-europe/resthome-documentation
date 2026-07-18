# General settings (residents, rooms)

:::{rh-description}
Configure the general settings of a nursing home (MR/MRS) in Resthome: residents, accommodation, and the room and move-in managers.
:::

:::{rh-faq}
Where are the general settings?
: In Settings > Nursing Home (residents, accommodation, demo data) and in Settings > Medical (dashboard). These screens are reserved for the establishment's managers.

What is the "Rooms Technical Manager" for?
: It is the user who receives the "prepare the room" activity every time a resident arrives, or a room change or transfer opens a new stay. It is a choice specific to your establishment.

What is the "Move-in Procedure Manager" for?
: It is the user who receives the move-in checklist (agreement, condition report, inventory, medication locker, laundry, disinfection) on the resident's record when a stay opens. Left empty, the procedure is disabled.

What default values should I use for stay duration and room capacity?
: 30 days for the stay duration and 1 bed for the capacity suit most MR/MRS. These are only pre-fill values, editable afterwards on each stay or each room.

Should demo data be loaded in production?
: No. The "Load Demo Data" button creates fictitious residents, rooms and invoices: keep it for a test environment. Never use it on your real database.

What does "Hide Empty Stat Cards" do?
: Disabled by default, this setting keeps all dashboard cards visible even when their counter is 0. Enable it only if you prefer a cleaner screen.
:::

This tab brings together the settings that structure the day-to-day running of
your home: how **residents** are managed, **accommodation** (stay duration,
capacity, managers), and the display of the care **dashboard**.

You will find them in the **Settings** application:

- **Settings > Nursing Home (MR/MRS)** — residents, accommodation, demo data;
- **Settings > Medical** — dashboard.

:::{admonition} Reserved for managers
:class: info

These settings are only visible to users who hold the establishment
**manager** role. They are set once and then rarely change afterwards.
:::

## Residents

*Settings > Nursing Home > Residents.* Two options frame the creation and
follow-up of residents.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Medical Information** | Makes medical information mandatory for all residents. | Establishment-specific — enable it if the head nurse requires a complete medical file from admission onwards. |
| **Family Notifications** | Sends automatic notifications to the resident's family. | Establishment-specific — enable it if you communicate with families from Resthome. |

## Accommodation

*Settings > Nursing Home > Accommodation.* This block sets the default values for
rooms and stays, and designates **who** is notified when a resident arrives or
changes room.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Default Stay Duration** | Pre-fills the duration (in days) proposed when a new stay opens. | **30 days** |
| **Room Capacity** | Number of beds pre-filled when creating a new room. | **1 bed** (single room) |
| **Rooms Technical Manager** | User who receives the "prepare the room" activity when a resident arrives or during a room change / transfer. | The technical or maintenance staff member of your home. |
| **Move-in Procedure Manager** | User who receives the move-in checklist (agreement, condition report, inventory, medication locker, laundry, disinfection) on the resident's record. | The admission coordinator — **leave empty to disable** the procedure. |

:::{admonition} Two complementary managers
:class: tip

At every **[room change or transfer](../residents/changement-chambre.md)** as
well as at **[admission](../residents/gerer-un-resident.md)**, Resthome opens a
new stay and automatically triggers:

- a **"prepare the room"** activity for the **technical manager**;
- the **move-in checklist** (if a **procedure manager** is defined) on the
  resident's record.

These are work reminders: setting them avoids oversights on arrival.
:::

## Dashboard

*Settings > Medical > Dashboard.* A single setting, which controls the display of
the care dashboard's stat cards.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Hide Empty Stat Cards** | Hides the dashboard cards (missed care, attention points, Katz renewals, etc.) whose counter is 0. | **Leave disabled** (default): a displayed "0" is a positive signal, not a lack of information. |

## Demo Data

*Settings > Nursing Home > Demo Data.* A way to fill a **test** database with
fictitious residents, rooms, stays and invoices.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Load Demo Data** | Creates fictitious residents, rooms, stays, billing periods, medical data and meals. | Keep it for a **test** environment. |
| **Update Demo Data** | Re-runs the loader to add demo records added since (furniture, supplements, etc.) without duplicating existing ones. | Testing only. |

:::{admonition} Never on your real database
:class: warning

Demo data creates **fictitious residents and invoices**. Only use these buttons on
a test or training database, **never** on your production environment.
:::

## Going further

- [Configuration](index.md)
- [Manage a resident](../residents/gerer-un-resident.md)
- [Room change and transfer](../residents/changement-chambre.md)
- [Getting started](../premiers-pas.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
