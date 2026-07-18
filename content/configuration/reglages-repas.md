# Meal and nutrition settings

:::{rh-description}
Configure Resthome's Meals tab in a nursing home (MR/MRS): nutritional data source, public menu, kiosk, family notifications, and ESPEN targets.
:::

:::{rh-faq}
Should you choose CIQUAL or NUBEL as the nutritional source?
: CIQUAL (ANSES, France) is the default source: its database of 3,484 foods is already loaded, so you can use it right away. NUBEL (Belgium) must be imported first. To get started, keep CIQUAL; switch to NUBEL only if you need the Belgian references and the import has been done.

What is the intake deficit alert threshold for?
: Resthome compares the 3-day average intake against the resident's needs (energy and protein). When that intake covers less than the configured threshold (75% by default), a deficit alert is created. Lower the threshold to be alerted later, raise it to be alerted sooner.

Are the ESPEN targets the same for every resident?
: No. The coefficients (30 kcal/kg, 1 g/kg of protein, 1.6 l for women and 2.0 l for men) are facility-wide settings. Resthome then calculates each resident's own target from their weight and sex. The energy band rises to 35 kcal/kg for an underweight resident (BMI less than or equal to 21).

Why do meal notifications to families have no effect?
: Sending emails requires an outgoing mail server configured on the platform. Without one, enabling the option sends nothing. First configure the outgoing server, then enable the global notification and the per-resident opt-in.

Where are these settings located?
: In Settings > Meals. The tab groups four blocks: Nutrition, Public menu and kiosk, Family notifications, and Nutritional targets (ESPEN).
:::

The **Meals** settings tab brings together the configuration of the Meals app:
the **nutritional data source**, the **appearance of the public menu and the
kiosk**, the **family notifications**, and the **nutritional targets (ESPEN)**
used for undernutrition monitoring. You will find it under **Settings > Meals**.

These settings apply to the whole facility: you define them once, after which
they rarely need adjusting.

## Nutrition

This section indicates which **reference database** Resthome queries to retrieve
the nutritional values of ingredients (calories, protein, etc.).

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Nutritional data source** | Reference database of nutritional values. CIQUAL (ANSES, France): 3,484 foods, already loaded. NUBEL (Belgium): Belgian database, to be imported. | **CIQUAL** (default, already loaded) |

:::{admonition} CIQUAL is enough to get started
:class: tip

The **CIQUAL** database is preloaded: you can build your menus and track
nutrition without any preparation. Only switch to **NUBEL** if you specifically
need the Belgian references — the import must then be carried out beforehand.
:::

## Public menu and kiosk

These settings customise the appearance of the **daily menu**, **weekly menu**,
and **kiosk** pages (see [Family portal and kiosk](../repas/portail-familles.md)).

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Public menu colour** | Main colour of the menu and kiosk pages. | Your brand colour (default `#0d6efd`) |
| **Show company logo** | Displays the company logo at the top of the public menu pages. | Enabled |
| **Kiosk refresh (seconds)** | Automatic refresh interval of the kiosk page (`/menu/kiosk`) shown in the dining room. | 600 s (10 min) |

:::{admonition} Values specific to your facility
:class: note

The **colour** and the **logo** are specific to your facility: use your visual
identity. The kiosk refresh is only useful if a screen displays the
`/menu/kiosk` page continuously.
:::

## Family notifications

This block enables the automatic sending of emails to families who have accepted
it: a **weekly summary** of meals and a **low-intake alert**.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Meal notifications to families** | Sends opted-in families a weekly summary and a low-intake alert. Requires an outgoing mail server. | Enabled **if** an outgoing mail server is configured, otherwise disabled |

:::{admonition} An outgoing mail server is required
:class: warning

Without an **outgoing mail server** configured on the platform, enabling the option
sends nothing. Sending also depends on a **per-resident opt-in**: only families
who have accepted receive the emails. Configure the outgoing server, enable the
global notification, then the opt-in resident by resident.
:::

## Nutritional targets (ESPEN)

These coefficients, drawn from the **ESPEN** geriatric guidelines, are used to
calculate each **resident's own target** (from their weight and sex) and to
trigger the **deficit alerts**.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Energy (kcal/kg/day)** | Energy target per kilo of body weight. | 30 |
| **Energy if underweight (kcal/kg/day)** | Raised target for an undernourished resident (BMI less than or equal to 21); ESPEN suggests 32 to 38. | 35 |
| **Protein (g/kg/day)** | Protein target per kilo of body weight (at least 1; 1.2 to 1.5 in case of illness). | 1 |
| **Fluids — women (ml/day)** | Daily hydration target for women. | 1600 |
| **Fluids — men (ml/day)** | Daily hydration target for men. | 2000 |
| **Intake deficit alert (% coverage)** | Threshold below which an alert is created when the 3-day average intake does not cover enough of the energy or protein target. | 75 |

:::{admonition} A target calculated per resident
:class: info

Here you set the **coefficients**; Resthome derives each resident's
**individual target** from their weight and sex, then compares the actual
**intake** against those targets. Coverage monitoring and undernutrition
screening are described in [Menus, diets, and hydration](../repas/menus-regimes.md).
:::

## Further reading

- [Menus, diets, and hydration](../repas/menus-regimes.md)
- [Family portal and kiosk](../repas/portail-familles.md)
- [Meals overview](../repas/index.md)
- [Clinical registers](../soins/registres.md)
