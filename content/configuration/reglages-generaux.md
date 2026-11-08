---
modules: [healthcare_base, healthcare_accommodation, healthcare_medical, healthcare_medication]
---

# General settings (residents, rooms)

:::{rh-description}
Configure the general settings of a nursing home in Resthome: residents, guided tours, demonstration data, accommodation, and the Medical tab (dashboard, falls, prescriptions, clinical records).
:::

:::{rh-faq}
Where are the general settings?
: In Settings → Nursing Home (residents, guided tours, demonstration data, accommodation) and in Settings → Medical (dashboard, falls, prescriptions, clinical records). These screens are reserved for the establishment's managers.

Who receives the room preparation when a resident arrives?
: A room task is created for the housekeeping team. Fill in Named on room tasks to name one person on those tasks instead.

Who receives the administrative move-in tasks?
: The administration team. Fill in Named on move-in tasks to name one person on those tasks instead.

What default values should I use for stay duration and room capacity?
: 30 days for the stay duration and 1 bed for the capacity suit most homes. These are only pre-filled values, editable afterwards on each stay or each room.

Should demonstration data be loaded in production?
: No. Load Demonstration Data creates fictitious residents, rooms and invoices: keep it for a test or training database. Never use it on your real database.

How do I switch the guided tours off?
: Untick Guided tours in Settings → Nursing Home. None of them then appears for anyone. Replay for everyone starts them again from the first one for every user.

What does "Hide Empty Stat Cards" do?
: Off by default, this setting keeps every dashboard card visible even when its counter is 0. Turn it on only if you prefer a cleaner screen.
:::

This page covers the settings that structure the day-to-day running of your
home: how **residents** are managed, the **guided tours**, the **demonstration
data**, **accommodation** (stay duration, capacity, who is named on the move-in
tasks) and the **Medical** tab.

You will find them in the **Settings** application:

- **Settings → Nursing Home** — residents, guided tours, demonstration data,
  accommodation;
- **Settings → Medical** — dashboard, falls, prescriptions, clinical records.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The Belgian pack adds an **Approvals** block to the **Nursing Home** tab (the
establishment's INAMI numbers, its MR/MRS approvals and their beds) and a
**SAM medicines** block to the **Medical** tab. See
[Belgian settings](../belgique/reglages.md).
:::

:::{admonition} Reserved for managers
:class: info

These settings are only visible to users who hold the establishment
**manager** role. They are set once and then rarely change afterwards.
:::

## Residents

*Settings → Nursing Home → Residents.* Two options frame the creation and
follow-up of residents.

| Setting | What it does | Recommended value |
|---|---|---|
| **Medical Information** | Makes medical information mandatory for all residents. | Establishment-specific — turn it on if the head nurse requires a complete medical file from admission onwards. |
| **Family Notifications** | Sends automatic notifications to the resident's family. | Establishment-specific — turn it on if you communicate with families from Resthome. |

## Guided tours

*Settings → Nursing Home → Guided tours.* Step-by-step guides through the
admission and billing flows, started at the first sign-in and from the **?**
menu at the top.

| Setting | What it does | Recommended value |
|---|---|---|
| **Guided tours** | Turned off, no guided tour appears for anyone. | **On** while the team learns Resthome. |
| **Replay for everyone** (button) | Every user follows the guided tours again from the first one, at their next sign-in. | After a training session, or when new staff arrive. |

## Demo Data

*Settings → Nursing Home → Demo Data.* A way to fill a **test** database with
fictitious residents, rooms, stays and invoices.

| Setting | What it does | Recommended value |
|---|---|---|
| **Demonstration data** → **Load Demonstration Data** | Creates invented residents (fictional names and identifiers), rooms, stays, billing periods, medical data and meals: the set to show the product with. | A **test** or training database only. |
| **Update what is loaded** → **Update Data** | Re-runs the loader on the dataset already loaded, to add records added since (furniture, supplements…) without duplicating existing ones. | Testing only. |
| **Load Doc Data** | Shown once demonstration data is loaded. Loads an anonymised dataset and replaces the establishment's identity by a fictitious one, for screenshots. | Testing only. |

:::{admonition} Never on your real database
:class: warning

Demonstration data creates **fictitious residents and invoices**. Only use these
buttons on a test or training database, **never** on your production
environment.
:::

## Accommodation

*Settings → Nursing Home → Accommodation.* This block sets the default values
for rooms and stays, and who is named on the tasks created when a resident
arrives or changes room.

| Setting | What it does | Recommended value |
|---|---|---|
| **Default Stay Duration** | Pre-fills the duration (in days) proposed when a new stay opens. | **30 days** |
| **Room Capacity** | Number of beds pre-filled when creating a new room. | **1 bed** (single room) |
| **Named on room tasks** | A person named on the new room tasks (preparing the room). Empty, the tasks go to the **housekeeping team**. | Empty, unless one person handles every room. |
| **Named on move-in tasks** | A person named on the new administrative move-in tasks (agreement, condition report, inventory…). Empty, the tasks go to the **administration team**. | Empty, or the admission coordinator. |

:::{admonition} Tasks at every move-in
:class: tip

At every **[admission](../residents/gerer-un-resident.md)**, as well as at every
**[room change or transfer](../residents/changement-chambre.md)**, Resthome opens
a new stay and creates the room and move-in tasks on its own. These are work
reminders: they avoid oversights on arrival.
:::

## Medical tab

*Settings → Medical.*

### Dashboard

| Setting | What it does | Recommended value |
|---|---|---|
| **Hide Empty Stat Cards** | Hides the dashboard cards (missed care, attention points, reassessments…) whose counter is 0. | **Leave off** (default): a displayed "0" is a positive signal, not a lack of information. |

### Falls

| Setting | What it does | Recommended value |
|---|---|---|
| **Tell the head nurse of a fall to read** | A recorded fall is always among the head nurse's activities to read. Choose **E-mail and activity** to also send an e-mail, or **Activity only**. | Establishment-specific. |

### Prescriptions

| Setting | What it does | Recommended value |
|---|---|---|
| **Receive prescriptions by e-mail** | Each e-mail sent to the **Alias** address becomes a draft prescription, with its PDF beside the form. | On, if doctors or the pharmacy send prescriptions by e-mail. |
| **Read the lines off the PDF** | Fills in the lines of a received prescription: **Typed by hand** or **Local OCR**. The nurse checks each line before confirming. | Establishment-specific. |
| **Create a missing medicine from the reference catalogue from this certainty (%)** | When a line read off the PDF names a medicine the home does not have yet, it is created from the reference catalogue only above this certainty. | **85** (default). |
| **Track the pillboxes** | Each dose records who prepared it and who checked it; a care assistant gives only a prepared dose, a nurse prepares an unprepared one on the spot. | Establishment-specific. |
| **The house's pharmacy** | Serves the residents who chose no pharmacist of their own: their orders go to it. | The home's usual pharmacy. |
| **The pharmacy's basket leaves at** | Every morning from this hour, what is missing leaves for the pharmacy by itself, with the medication schedule. | **8:00** (default). |

### Clinical Records

| Setting | What it does | Recommended value |
|---|---|---|
| **Body location entry** | How the staff points at a place on the body: a **Drawing** to tap, or a **List** to pick from. | **Drawing** on tablets; **List** if staff prefer it. |

<!-- screenshot to update: Settings, Nursing Home tab, Guided tours and Demo Data blocks -->
<!-- screenshot to add: Settings, Medical tab, Prescriptions block -->

## Going further

- [Configuration](index.md)
- [Managing a resident](../residents/gerer-un-resident.md)
- [Room change and transfer](../residents/changement-chambre.md)
- [Getting started](../premiers-pas.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
