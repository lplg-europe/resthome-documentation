---
modules: [healthcare_accommodation_billing]
---

# Billing settings

:::{rh-description}
Configure Resthome's Billing settings tab for a nursing home: automatic invoicing, billing refresh, journals and split billing.
:::

:::{rh-faq}
Where are the billing settings located?
: In Settings > Billing. The tab is only visible to the home's managers. It gathers automatic invoicing, the billing journals and the optional features such as split billing.

Should automatic billing refresh be enabled?
: Yes, that is the recommended value. When enabled, it keeps every open billing period up to date as soon as any data changes: supplement, absence, end of stay, change of room or health insurer, mid-month admission. Only disable it if you prefer to recalculate solely by clicking "Refresh" on the period.

What is the Resident Journal for?
: It is the sales journal that receives the invoices for the resident share (accommodation and supplements). Where the health insurer also pays part of the stay, its share goes into a journal of its own, kept separate for clear accounting tracking.

Does enabling split billing install a module?
: Yes. Ticking "Split billing (maintenance debtors)" installs the corresponding module; unticking it uninstalls it. Enable it if maintenance debtors share the resident portion.
:::

The **Billing** settings tab gathers the parameters that drive the **billing** of
your nursing home: invoice generation, accounting journals and optional
features. You configure them **once**, then they only change at the margins.

You will find them under **Settings > Billing**. The tab is only visible to the
home's **managers**.

:::{admonition} In Belgium
:class: rh-country rh-country-be

The tab is called **MR/MRS Billing** and holds three more blocks: the **INAMI
Journal**, the establishment's **Cc accreditation** for the coma allowance, and
the **Katz activity assignee** used after a long hospitalization. The eHealth
certificate and credentials are set elsewhere. See
[Belgian settings](../belgique/reglages.md) and
[eHealth and eFact settings](../belgique/reglages-ehealth.md).
:::

## Automatic billing

This block decides **how** and **when** invoices are produced, and whether open
periods keep themselves up to date on their own.

| Setting | What it does | Recommended value |
|---|---|---|
| **Automatic billing** | Automatically generates the monthly stay invoices, without going through the manual cycle. Disabled by default. | Depending on your organization; often left **disabled** in favor of the manual cycle (generate → invoice), which gives more control. |
| **Billing day** | Day of the month on which automatic invoices are generated (only visible if automatic billing is enabled). | **1** (start of the month) by default; adjust according to your organization. |
| **Automatic billing refresh** | Keeps every open period up to date as soon as any data changes: supplement, absence, end of stay, change of room or health insurer, mid-month admission. | **Enabled** — recommended. |

:::{admonition} Automatic refresh and the "Refresh" button
:class: tip

With refresh **enabled**, adding a supplement or an absence is reflected on the
period on its own: you generally have nothing to do. The period's **"Refresh"**
button remains available for a full on-demand recalculation. See
[Bill a month](../facturation/facturer-un-mois.md).
:::

## Billing journals

The **resident share** (accommodation and supplements) goes into its own sales
journal. Where the country has a care allowance paid by the health insurer, the
country pack adds a second journal for that share, so each payer is tracked
separately.

| Setting | What it does | Recommended value |
|---|---|---|
| **Resident Journal** | Sales journal that receives the invoices for the **resident share** (accommodation and supplements). | A sales journal of your facility, **separate** from the health insurer's one when there is one (recommended). |

:::{admonition} Facility-specific value
:class: warning

The journal depends on **your chart of accounts**. Choose an existing **sales**
journal. Keeping one journal per payer makes reconciliation and per-payer
tracking easier.
:::

## Optional features

An additional module is installed directly from the settings, by ticking a
checkbox.

| Setting | What it does | Recommended value |
|---|---|---|
| **Split billing (maintenance debtors)** | Splits the resident share of the monthly invoice among several debtors, each paying a percentage. Ticking this box **installs** the module. | Enable it **if** maintenance debtors share the resident share. |

:::{admonition} What the checkbox does
:class: tip

Ticking installs the module and unticking uninstalls it (Odoo convention). Once
enabled, the split is configured per resident. See
[Maintenance debtors](../facturation-partagee/index.md).
:::

## Absences

Absences are **not** configured in this tab. The discount granted for an absence
is set under **Billing > Configuration > Absence Discount Rules**. Whether a day
counts as a presence day is **built in**: a departure after noon or a return
before noon counts as a presence day, unless the country pack applies its own
thresholds. See
[Absences and hospitalizations](../facturation/absences.md).

## Going further

- [Configuration](index.md) — rooms, rates, health insurers, facility.
- [Billing overview](../facturation/index.md)
- [Bill a month, step by step](../facturation/facturer-un-mois.md)
- [Maintenance debtors](../facturation-partagee/index.md)
- [Absences and hospitalizations](../facturation/absences.md)
