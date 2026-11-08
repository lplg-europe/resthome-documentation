---
modules: [resthome_meal, resthome_family_portal_meal]
sectors: [mr, csj]
---

# Family portal and public menu

:::{rh-description}
Share meals beyond the team in WideCare: the family portal pages, the meal e-mails to families, the public and printable menu with its QR code, and the dining-room kiosk.
:::

:::{rh-faq}
What can families see on the portal?
: The day's menu and, for their resident, each meal of the day: where it was eaten, whether it was served or refused, and how much was eaten. They also see a 30-day history, the resident's diets and allergies. Nothing else of the record.

Who decides which relative sees the meals?
: With the Family portal application, the access given to the relative: only an access with **Meals** ticked opens these pages. See [Accesses](../portail-famille/acces.md).

Can families receive the meals by e-mail?
: Yes, when **Family Meal Notifications** is on in the settings and **Notify Family of Meals** is ticked on the resident: a weekly summary, and an alert the same evening when a meal was eaten at 25% or less, or refused.

Can the menu be published publicly?
: Yes. The day's and the week's menus have public pages, without sign-in, with a printable version carrying a QR code back to the online menu.

What is the kiosk for?
: It displays the day's menu full screen on a television in the dining room, and refreshes itself.

Do I have to update the menu in several places?
: No. The portal, the public pages and the kiosk all read the menus in WideCare. Only **confirmed** or **served** menus are shown.
:::

WideCare shares the meals **with families** and **in the dining room**, from the
same menus and the same meal round as the team uses.

## Family portal

A relative signed in to the portal finds a **Meals** entry (**View Meals**). Once
the Family portal application is installed, the meal pages follow the
**accesses**: only a relative whose access has **Meals** ticked sees them, and a
**Meals** tile appears on the resident's family page. See [Family
portal](../portail-famille/index.md).

The relative finds:

- **Today's Meals** — the date, **Today's Menu** (the dishes of each meal), then
  for each of their residents a table **Meal**, **Location** (**Dining Room**,
  **In Room**, **Absent**), **Served** (or **Refused**) and **Consumption** (the
  amount eaten).
- **Meal History** — the meals day by day, served with the amount eaten,
  **Refused** or **Not Served**.
- **The resident's page** — **Meals (30 days)**: **Meals Served**, **Well Eaten
  (75%+)**, the **Diets** and **Allergies**, and the detail of each day.

Coming from the resident's family page, the breadcrumb leads back to it.

<!-- screenshot to add: family portal Today's Meals page with the menu and the resident's meals table -->

## Meal e-mails to families

WideCare can e-mail the family contacts of a resident:

- a **weekly meal summary** — the meals of the last 7 days, served or refused,
  with the amount eaten;
- a **meal alert** — the same evening, when a meal was eaten at **25% or less**
  or refused. Each plate triggers at most one alert.

To switch them on:

1. In **Meals → Configuration → Settings**, block **Family Notifications**, tick
   **Family Meal Notifications**.
2. On the resident, tab **Nutrition**, tick **Notify Family of Meals**.
3. Make sure the resident's family contacts have an e-mail address.

:::{admonition} An outgoing mail server is needed
:class: warning

Without an outgoing mail server, the e-mails are not sent, even with both boxes
ticked.
:::

## Public menu pages

The menus can be read without signing in, at the home's address followed by:

| Address | Page |
| --- | --- |
| `/menu` | **Today's Menu**, with the previous and next days that have a menu |
| `/menu/week` | The menu of the week, Monday to Sunday, today highlighted |
| `/menu/print` | The **printable menu** of the day, with a QR code |
| `/menu/kiosk` | The dining-room **kiosk** |

The day's page has the buttons **Week**, **Print** and **Kiosk**. The dishes
carry the badges **Vegetarian**, **Gluten-Free** and **Diabetic-Safe**, taken
from the dish catalogue. Days without a confirmed menu show **Menu in
preparation** or **No menu available for this date**.

### The printable menu and its QR code

The printable menu lists the day's meals and their dishes, a legend of the
badges and the note "For allergies or special dietary needs, please contact the
staff." Its QR code (**Scan to see the menu online**) opens the online menu, so
a printed sheet always leads to the latest version.

### The kiosk

The kiosk shows the day's menu **full screen**, for a screen or a television in
the dining room. It refreshes itself at the interval set in **Kiosk Refresh
(seconds)** (every 10 minutes by default, 30 seconds at least).

### Look of the public pages

In **Meals → Configuration → Settings**, block **Public Menu & Kiosk**:

- **Public Menu Color** — the main colour of the menu, week and kiosk pages;
- **Show Company Logo** — the home's logo at the top of the pages;
- **Kiosk Refresh (seconds)**.

See [Meal and nutrition settings](../configuration/reglages-repas.md).

:::{admonition} Always up to date
:class: tip

The portal, the public pages and the kiosk read the menus in WideCare: they
show the latest version automatically, with no double entry. Dates are written
in the reader's language.
:::

## Going further

- [Family portal](../portail-famille/index.md) — the accesses that open the
  meals to a relative, and everything else they may see.
- [The meal round](distribution.md)
- [Menus, diets and allergies](menus-regimes.md)
- [Meals overview](index.md)
