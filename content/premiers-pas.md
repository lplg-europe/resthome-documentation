---
modules: [healthcare_base, healthcare_accommodation, healthcare_accommodation_billing, lplg_license, healthcare_industries]
---

# Getting started

:::{rh-description}
Log in to Resthome, find the apps, read a dashboard, follow the guided tours and find your way around a screen.
:::

:::{rh-faq}
Why don't I see every app?
: Each role sees the apps it works with. A caregiver does not see Billing, a cook does not see Admissions. Ask your administrator if an app you need is missing.

Where are the dashboards?
: In the **Nursing Care** and **Billing** apps, which open on their own dashboard. The **Nursing Home** app opens on its menus: residents, accommodation, configuration and reports.

How do I restart a guided tour?
: Click the **?** menu at the top of the screen and choose the tour. The tours appear only when your establishment has switched them on.

Who is WideCareBot?
: The signature of the messages the system writes itself in the history of a record: a reminder, a notification, a change made automatically.
:::

This guide introduces Resthome in a few minutes: logging in, the apps, the
dashboards, the guided tours and the parts of a screen.

## Logging in

1. Open your browser at the address provided by your facility.
2. Enter your **email address** and your **password**.
3. Click **Log in**.

:::{admonition} Forgot your password?
:class: note

Use the **Reset password** link on the login page, or ask your
administrator.
:::

## The apps

Resthome is organised into apps, reached from the **main menu** (the grid
icon, top left). They are listed in the order of a resident's journey:

| App | What it's for |
|---|---|
| **Admissions** | Every request for a place, from the first call to the move-in. See [Admissions](admissions/index.md). |
| **Nursing Home** | Residents, rooms, stays, staff tasks, the family portal, reports and the configuration. See [Residents](residents/index.md). |
| **Billing** | Billing periods, supplements, absences and invoices. See [Billing](facturation/index.md). |
| **Nursing Care** | The care dashboard, care plans, observations, evaluation tools, clinical registers and the Medicines workstation. See [Care](soins/index.md) and [Medicines](medicaments/index.md). |
| **Care Tasks** | The care tasks planned for each resident. See [Care tasks](soins/taches-de-soins.md). |
| **Meals** | Menus, diets, textures and the meal round. See [Meals](repas/index.md). |
| **Supplements** | The supplements billed to residents (hairdresser, telephone…). See [The Supplements app](facturation/application-supplements.md). |
| **Planning** | The staff schedule. See [Staff planning](planning/index.md). |
| **Serviced Living** | Serviced residences: units, contracts, calls and requests. See [Serviced residences](residences-services/index.md). |
| **WideCare** | The field app of the staff, on a phone or a tablet. See [WideCare app](soins-mobile/index.md). |
| **WideCare AI** | Questions to the documentation without leaving Resthome. See [WideCare AI assistant](assistant/index.md). |

Odoo's general apps — **Discuss**, **Calendar**, **Documents**, **Contacts** —
come after them. Depending on your role (administrative, caregiver, kitchen,
technical…), you only see the apps that concern you. You can rearrange your own
grid: the order above is only the default.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The grid also shows the Belgian apps: **Forfait** (the institutional
allowance), **eHealth** (the exchanges with the mutualities), the **Health
Directory** and the **Day care centre**. See [Belgium](belgique/index.md).
:::

## The dashboards

The **Nursing Care** and **Billing** apps open on a dashboard, laid out like the
home screen of a phone:

- each **tile** is a door: it opens the list or the screen its menu opens;
- a tile carries a **badge** only when a number calls for an action — no badge
  means nothing is waiting;
- the **To do now** section gathers what must be handled today;
- click the **star** of a tile to keep it at the top, in **Favourites**;
- drag a tile to move it within its section; the **reset** button puts the cards
  back the way the house arranged them;
- the **side panel** (the sliders button next to the title) lists the records
  you opened recently and, on some dashboards, shortcuts;
- the **+** button creates what the dashboard is about (an observation, a
  prescription…).

Where the dashboard follows the sectors of the house, choose a sector at the top
to narrow it; **The whole house** shows everything.

Each user's favourites and order are their own: arranging your dashboard
changes nothing for your colleagues.

<!-- screenshot to add: the Nursing Care dashboard with its tiles, a starred tile in Favourites and the side panel open -->

:::{admonition} In Belgium
:class: rh-country rh-country-be

The Billing dashboard also shows the Belgian steps of the month: the MDA
checks, the eAgreement requests and the eFact cockpit. See [Billing a month in
Belgium](belgique/facturation.md).
:::

## The guided tours

Guided tours walk you through a flow on the real screens: a bubble points at the
field or the button to use, and waits for you to act.

| Tour | Where it starts |
|---|---|
| **Admission request** | The **Admissions** app: create a request, plan the visit, admit. |
| **Stay and resident record** | The **Nursing Home** app: the stay, its states, the room change, the departure. |
| **Monthly billing** | The **Billing** app: a billing period from start to finish. |

Each tour is offered to whoever sees its app. It starts by itself at sign-in
the first time, and stays available afterwards from the **?** menu at the top of
the screen, where a tick shows the tours already followed.

:::{tip}
At the end of the admission tour, **Delete the practice** archives the request,
the person and the visit created while practising: nothing is left behind.
:::

### Turning the tours on

The tours are **off by default**. A manager switches them on in **Nursing Home →
Configuration → General → Settings**, block **Guided tours**:

- tick **Guided tours** — switched off, no tour appears for anyone, the **?**
  menu included;
- **Replay for everyone** makes every user follow the tours again at their next
  sign-in.

Each user also has their own switch: in your preferences (your avatar, top
right), **Guided tours** starts the tours at sign-in or not, and **Replay the
tours** starts them again for you alone.

:::{admonition} In Belgium
:class: rh-country rh-country-be

Two more tours are offered: the agreement of the insurer (eAGL) and the day care
centre. See [Belgium](belgique/index.md).
:::

## Finding your way around a screen

- **Menus at the top**: the sections of the app.
- **Breadcrumb** (at the top left): your position; click a level to go back.
- **Search bar**: filters, groupings and favourites of the list; the panel on
  the left of some lists filters by one click (sector, gender…).
- **View switcher** (top right of a list): kanban, list, calendar…
- **Gear / Actions menu**: the additional actions on the open record or on the
  selected lines.
- **Smart buttons** (top right of a record): counters that open the linked
  records — the stays of a room, the tasks of a resident…
- **History** (right-hand column, or below the record on a narrow screen): the
  messages, notes and changes of the record.

### Messages signed WideCareBot

The messages the system writes on its own in the history of a record — a
reminder, an automatic change, a notification — are signed **WideCareBot**, with
the WideCare icon. A house that renamed this bot keeps its own name.

## Adding a sector pack

Resthome is built from **packs**: one per care sector and per country. The
technical administrator adds a pack from the **Apps** app: the **Industries**
filter lists the WideCare sector packs available for the database, and
**Activate** installs one.

:::{note}
The **Apps** app is reserved for the technical administrator. Ask LPLG support
before adding a pack to a live database.
:::

## What's next?

- [Manage a resident](residents/gerer-un-resident.md)
- [Admissions](admissions/index.md)
- [Configuration](configuration/index.md)
