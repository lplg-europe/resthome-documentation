# Billing settings (MR/MRS)

:::{rh-description}
Configure Resthome's MR/MRS settings tab for a nursing home (MR/MRS): automatic billing, journals, Cc accreditation, absences.
:::

:::{rh-faq}
Where are the MR/MRS billing settings located?
: In Settings > MR/MRS. The tab is only visible to MR/MRS managers. It gathers automatic billing, journals, facility accreditation, split billing and absence management.

Should automatic billing refresh be enabled?
: Yes, that is the recommended value. When enabled, it keeps every open billing period up to date as soon as any data changes: supplement, absence, end of stay, change of room or health insurance fund, mid-month admission. Only disable it if you prefer to recalculate solely by clicking "Refresh" on the period.

What is the difference between the INAMI Journal and the Resident Journal?
: The INAMI Journal receives the invoices for the insurer share (sent via eFact); the Resident Journal receives those for the resident share (accommodation and supplements). These are two sales journals of your facility, preferably kept separate for clear accounting tracking.

When should the Cc accreditation be ticked?
: Only if your facility holds the accreditation that authorizes billing the Ccoma coma lump sum. Without this accreditation, a resident classified as Ccoma cannot be billed via eFact; accommodation, however, is still billed. This is a facility-specific value.

Does enabling split billing install a module?
: Yes. Ticking "Split billing (maintenance debtors)" installs the corresponding module; unticking it uninstalls it. Enable it if maintenance debtors share the resident portion.

What is the Katz activity assignee for?
: It is the user to whom Resthome assigns the "New Katz required" activity when a readmission after hospitalization exceeds 30 days. If the field is empty, the activity goes to the current user if they are clinical, otherwise to the first head nurse, nurse or doctor found.
:::

# Billing settings (MR/MRS)

The **MR/MRS** settings tab gathers the parameters that drive the **billing** of
your nursing home: invoice generation, accounting journals, facility accreditation
and absence management. You configure them **once**, then they only change at the
margins.

You will find them under **Settings > MR/MRS**. The tab is only visible to
**MR/MRS managers**.

:::{admonition} eHealth secrets are configured elsewhere
:class: info

The **eHealth certificate (.p12)**, the **CIN license** and the health-insurer
connection credentials are **not** found in this tab, but in the
**[eHealth](../ehealth/index.md)** configuration. This tab contains **no secret
data**; you enter neither password nor key here.
:::

## Automatic billing

This block decides **how** and **when** invoices are produced, and whether open
periods keep themselves up to date on their own.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Automatic billing** | Automatically generates the monthly stay invoices, without going through the manual cycle. Disabled by default. | Depending on your organization; often left **disabled** in favor of the manual cycle (generate → invoice), which gives more control. |
| **Billing day** | Day of the month on which automatic invoices are generated (only visible if automatic billing is enabled). | **1** (start of the month) by default; adjust according to your organization. |
| **Automatic billing refresh** | Keeps every open period up to date as soon as any data changes: supplement, absence, end of stay, change of room or health insurance fund, mid-month admission. | **Enabled** — recommended. |

:::{admonition} Automatic refresh and the "Refresh" button
:class: tip

With refresh **enabled**, adding a supplement or an absence is reflected on the
period on its own: you generally have nothing to do. The period's **"Refresh"**
button remains available for a full on-demand recalculation. See
[Bill a month](../facturation/facturer-un-mois.md).
:::

## Billing journals

Resthome issues **two streams** of invoices: the **insurer share** (dependency
lump sum, sent to the insuring body via eFact) and the **resident share**
(accommodation and supplements). Each stream goes into its own sales journal.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **INAMI Journal** | Sales journal that receives the invoices for the **insurer share** (dependency lump sum sent via eFact). | A sales journal of your facility. |
| **Resident Journal** | Sales journal that receives the invoices for the **resident share** (accommodation and supplements). | A sales journal **separate** from the previous one (recommended). |

:::{admonition} Facility-specific value
:class: warning

These two journals depend on **your chart of accounts**. Choose existing **sales**
journals. Separating them (INAMI on one side, resident on the other) makes
reconciliation and per-payer tracking easier.
:::

## Facility accreditation

Some federal lump sums require a **specific accreditation** of the facility. This
is the case for the **coma (Ccoma)** lump sum.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Cc accreditation (coma lump sum)** | Tick if the facility holds the accreditation allowing it to bill the **Ccoma** coma lump sum. Without it, a resident classified as Ccoma is **not** billable via eFact (neither regional nor federal); accommodation is still billed. | Tick **only** if your facility is accredited. |

:::{admonition} Not to be confused with the lump-sum amount
:class: note

The ordinary **dependency lump sum** is the **same amount** for all Katz
categories; the category is used to **declare the profile** to the health insurance
fund, not to set the amount (see [The INAMI lump sum](../facturation/forfait-inami.md)).
The Cc accreditation, for its part, concerns only the **special case of the coma
lump sum**.
:::

## Optional features

An additional module is installed directly from the settings, by ticking a
checkbox.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Split billing (maintenance debtors)** | Splits the resident share of the monthly invoice among several debtors, each paying a percentage. Ticking this box **installs** the module. | Enable it **if** maintenance debtors share the resident share. |

:::{admonition} What the checkbox does
:class: tip

Ticking installs the module and unticking uninstalls it (Odoo convention). Once
enabled, the split is configured per resident. See
[Maintenance debtors](../facturation/split-billing.md).
:::

## Absence management

The **presence day** rules (noon rule, hospitalization, leave) are **built into**
Resthome and are not configured here. Only the **assignee** of a follow-up activity
is configurable.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Katz activity assignee** | User to whom the "New Katz required" activity is assigned when a hospital readmission exceeds **30 days**. If empty: current user (if clinical), otherwise the first head nurse, nurse or doctor found. | The **head nurse** (or the care manager). |

:::{admonition} Why 30 days?
:class: note

A readmission after more than 30 days of hospitalization requires a **new Katz
assessment**. The assigned activity acts as a reminder. See
[Absences and hospitalizations](../facturation/absences.md).
:::

## Going further

- [Configuration](index.md) — rooms, rates, health insurance funds, facility.
- [Billing overview](../facturation/index.md)
- [Bill a month, step by step](../facturation/facturer-un-mois.md)
- [The INAMI lump sum (dependency)](../facturation/forfait-inami.md)
- [Maintenance debtors](../facturation/split-billing.md)
- [Absences and hospitalizations](../facturation/absences.md)
