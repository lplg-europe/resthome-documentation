---
modules: [resthome_meal]
---

# Meal and nutrition settings

:::{rh-description}
Configure Resthome's Meals tab in a nursing home: nutritional data source, public menu, kiosk, family notifications, and ESPEN targets.
:::

:::{rh-faq}
Which nutritional source should I choose?
: Keep CIQUAL (ANSES, France), the default: its database of foods is already loaded, so you can use it right away. Another source must be imported before you switch to it.

What is the intake deficit alert threshold for?
: Resthome compares the 3-day average intake against the resident's needs (energy and protein). When that intake covers less than the configured threshold (75% by default), a deficit alert is created. Lower the threshold to be alerted later, raise it to be alerted sooner.

Are the ESPEN targets the same for every resident?
: No. The coefficients (30 kcal/kg, 1 g/kg of protein, 1.6 l for women and 2.0 l for men) are facility-wide settings. Resthome then calculates each resident's own target from their weight and sex. The energy band rises to 35 kcal/kg for an underweight resident (BMI less than or equal to 21).

Why do meal notifications to families have no effect?
: Sending emails requires an outgoing mail server configured in Odoo. Without one, enabling the option sends nothing. First configure the outgoing server, then enable the global notification and the per-resident opt-in.

Where are these settings located?
: In Settings → Meals. The tab groups four blocks: Nutrition, Public Menu & Kiosk, Family Notifications, and Nutritional Targets (ESPEN).
:::

The **Meals** settings tab brings together the configuration of the Meals app:
the **nutritional data source**, the **appearance of the public menu and the
kiosk**, the **family notifications**, and the **nutritional targets (ESPEN)**
used for undernutrition monitoring. You will find it under **Settings → Meals**.

These settings apply to the whole facility: you define them once, after which
they rarely need adjusting.

## Nutrition

This section indicates which **reference database** Resthome queries to retrieve
the nutritional values of ingredients (calories, protein, etc.).

| Setting | What it does | Recommended value |
|---|---|---|
| **Nutrition Data Source** | Reference database of nutritional values. **CIQUAL (ANSES - France)** is already loaded. | **CIQUAL** (default, already loaded) |

:::{admonition} CIQUAL is enough to get started
:class: tip

The **CIQUAL** database is preloaded: you can build your menus and track
nutrition without any preparation.
:::

:::{admonition} In Belgium
:class: rh-country rh-country-be

A second choice, **NUBEL (Belgium)**, uses the Belgian food composition
references. It must be imported before you switch to it.
:::

## Public Menu & Kiosk

These settings customise the appearance of the **daily menu**, **weekly menu**,
and **kiosk** pages (see [Family portal and public menu](../repas/portail-familles.md)).

| Setting | What it does | Recommended value |
|---|---|---|
| **Public Menu Color** | Main colour of the menu and kiosk pages. | Your brand colour (default blue) |
| **Show Company Logo** | Displays the company logo at the top of the public menu pages. | On |
| **Kiosk Refresh (seconds)** | Automatic refresh interval of the kiosk page shown in the dining room. | 600 s (10 min) |

:::{admonition} Values specific to your facility
:class: note

The **colour** and the **logo** are specific to your facility: use your visual
identity. The kiosk refresh is only useful if a screen displays the kiosk page
continuously.
:::

## Family Notifications

This block enables the automatic sending of emails to families who have accepted
it: a **weekly summary** of meals and a **low-intake alert**.

| Setting | What it does | Recommended value |
|---|---|---|
| **Family Meal Notifications** | Sends opted-in families a weekly summary and a low-intake alert. Requires an outgoing mail server. | Enabled **if** an outgoing mail server is configured, otherwise disabled |

:::{admonition} An outgoing mail server is required
:class: warning

Without an **outgoing mail server** configured in Odoo, enabling the option
sends nothing. Sending also depends on a **per-resident opt-in**: only families
who have accepted receive the emails. Configure the outgoing server, enable the
global notification, then the opt-in resident by resident.
:::

## Nutritional Targets (ESPEN)

These coefficients, drawn from the **ESPEN** geriatric guidelines, are used to
calculate each **resident's own target** (from their weight and sex) and to
trigger the **deficit alerts**.

| Setting | Field | What it does | Recommended value |
|---|---|---|---|
| **Energy target** | **Energy (kcal/kg/day)** | Energy target per kilo of body weight. | 30 |
| | **Energy if underweight (kcal/kg/day)** | Raised target for an undernourished resident (BMI less than or equal to 21); ESPEN suggests 32 to 38. | 35 |
| **Protein target** | **Protein (g/kg/day)** | Protein target per kilo of body weight (at least 1; 1.2 to 1.5 in case of illness). | 1 |
| **Fluid targets** | **Fluids — women (ml/day)** | Daily hydration target for women. | 1600 |
| | **Fluids — men (ml/day)** | Daily hydration target for men. | 2000 |
| **Intake deficit alert** | **Intake Deficit Alert (% coverage)** | Threshold below which an alert is created when the 3-day average intake does not cover enough of the energy or protein target. | 75 |

:::{admonition} A target calculated per resident
:class: info

Here you set the **coefficients**; Resthome derives each resident's
**individual target** from their weight and sex, then compares the actual
**intake** against those targets. Coverage monitoring and undernutrition
screening are described in [Nutritional monitoring and undernutrition](../repas/suivi-nutritionnel.md).
:::

## Further reading

- [Menus, diets and allergies](../repas/menus-regimes.md)
- [Nutritional monitoring and undernutrition](../repas/suivi-nutritionnel.md)
- [Family portal and public menu](../repas/portail-familles.md)
- [Meals overview](../repas/index.md)
- [Clinical registers](../soins/registres.md)
