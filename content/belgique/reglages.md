---
modules: [l10n_health_be_perdiem_billing, resthome_mr_billing, l10n_health_be, resthome_geriatric_be, l10n_health_be_sam, resthome_documents]
sectors: [mr, csj]
---

# Belgian settings

:::{rh-description}
The settings the Belgian pack adds to WideCare: the approvals and their INAMI numbers, the INAMI Journal, the Cc accreditation, the INAMI rates and pseudo-codes, health insurers and CPAS.
:::

:::{rh-faq}
Where are the MR/MRS billing settings located?
: In Settings > MR/MRS Billing (MR/MRS/CSJ Billing when the day care centre is installed). The tab is only visible to managers. On top of the common billing settings, it holds the INAMI Journal, the Cc accreditation and the Katz activity assignee.

What is the difference between the INAMI Journal and the Resident Journal?
: The INAMI Journal receives the invoices for the insurer share (the dependency allowance sent via eFact); the Resident Journal receives those for the resident share (accommodation and supplements). These are two sales journals of your facility, preferably kept separate for clear accounting tracking.

When should the Cc accreditation be ticked?
: Only if your facility holds the accreditation that authorizes billing the Ccoma coma allowance. Without this accreditation, a resident classified as Ccoma cannot be billed via eFact; accommodation, however, is still billed. This is a facility-specific value.

What is the Katz activity assignee for?
: It is the user to whom WideCare assigns the "New Katz required" activity when a readmission after hospitalization exceeds 30 days. If the field is empty, the activity goes to the current user if they are clinical, otherwise to the first head nurse, nurse or doctor found.

Where do I record the INAMI number and the approvals of the home?
: In **Healthcare → Configuration → General → Approvals** (also reachable from **Manage approvals** in the settings). One approval per INAMI number, with one line per approved sector (MR, MRS, CSJ) and the number of beds or places it covers.

What default values should I use for stay duration and room capacity in an MR/MRS?
: 30 days for the stay duration and 1 bed for the capacity suit most MR/MRS. These are only pre-fill values, editable afterwards on each stay or each room.
:::

The Belgian pack adds its own settings to the common ones: the **INAMI
numbers** and **approvals** of the establishment, the journal and the
accreditation used to bill the **dependency allowance**, the **INAMI rates** and
their **pseudo-codes**, and the lists of **health insurers** and **CPAS**. This
page gathers them; the common settings are described under
[Configuration](../configuration/index.md).

The eHealth certificate, the CIN license and the eFact header are described
on their own page: see [eHealth and eFact settings](reglages-ehealth.md).

## Where the Belgian settings are

With the Belgian pack, some common screens change their name:

- the **Billing** settings tab is called **MR/MRS Billing** — **MR/MRS/CSJ
  Billing** when the [day care centre](centre-de-jour/index.md) is installed;
- the **Billing Rates** menu is called **INAMI Rates**;
- the **Nursing Home** settings tab gains an **Approvals** block;
- the billing configuration gains the **Mutuelles**, **Billing Codes** and
  **CPAS** menus;
- an **eHealth** settings tab appears — see [eHealth and eFact
  settings](reglages-ehealth.md).

The settings are only visible to the home's **managers**, and are set **once**,
at start-up.

## Approvals

*Healthcare → Configuration → General → Approvals.* The home is licensed by
sector: **MR** (rest home), **MRS** (rest and care home) and, for a day care
centre, **CSJ**. WideCare records these sectors on the **approval** of the
INAMI number they were granted to. A company holds one approval per type of
establishment: a rest home and a day care centre make two; a second site of the
same type is a branch or another company.

In the settings, the **Nursing Home** tab shows a summary under **Approvals of
the establishment**, with a **Manage approvals** link, and the **Conventioned
Establishment** box: tick it if the establishment adheres to the agreement with
the health insurers, which decides the tariff applied.

On the approval itself:

- **INAMI identity**: the **INAMI Number**; the **Establishment Type**,
  proposed from the first three digits of the number and editable; the
  **Competence Code**, the last three digits of the NIHII-11 (**000** for a day
  care centre, **110** for a rest home, **210** for some MRS); the **NIHII-11**;
- the company, the **Address** and the **Notes**;
- the **Sectors** tab: one line per approved sector, with its **Beds / places**,
  the beds **Occupied**, the **Occupancy**, the **Approval Reference** and the
  **Approval Date**. A line opens its own form, where the **Approval PDF** is
  kept. The tab also holds the resident journal of this establishment;
- the **eHealth** tab: the establishment's **certificate**;
- the **eFact** tab: the Account C journal and the contact person of this INAMI
  number, when they differ from the settings.

The beds recorded here are what the **occupancy** is measured against, and what
decides which **sectors** an admission may offer. Archive a superseded sector
line rather than deleting it: its beds are what the occupancy of those months
was measured against.

:::{admonition} The approval warns, it does not refuse
:class: note

A red banner says a sector is recorded twice; an orange one says more residents
occupy a category than the approval covers, or that a sector does not match the
type of its INAMI number — a day care centre has its own number, separate from
the rest home's. For the daily view, see [Occupancy MR / CS /
MRS](occupation-mr-mrs.md).
:::

:::{admonition} Two approvals in one company
:class: tip

A company that runs a rest home and a day care centre holds **two** INAMI
numbers, so **two** approvals, each with its own certificate. See
[Setting up a day care centre](centre-de-jour/configuration.md).
:::

## Billing: journal, accreditation and Katz

*Settings > MR/MRS Billing.* Next to the common blocks (see
[Billing settings](../configuration/reglages-facturation.md)), the Belgian pack
adds three settings. This tab contains **no secret data**: the eHealth
certificate, the CIN license and the health-insurer credentials are set in the
[eHealth and eFact settings](reglages-ehealth.md).

### INAMI Journal

WideCare issues **two streams** of invoices: the **insurer share** (the
dependency allowance, sent to the health insurer via
[eFact](ehealth/efact.md)) and the **resident share** (accommodation and
supplements). Each stream goes into its own sales journal.

| Setting | What it does | Recommended value |
|---|---|---|
| **INAMI Journal** | Sales journal that receives the invoices for the **insurer share** (dependency allowance sent via eFact). | A sales journal of your facility, **separate** from the **Resident Journal**. |

Separating the two journals (INAMI on one side, resident on the other) makes
reconciliation and per-payer tracking easier. A branch with no INAMI Journal of
its own uses the one of its parent company; the setting says so under the empty
field.

### Establishment accreditation

Some federal allowances require a **specific accreditation** of the facility.
This is the case for the **coma (Ccoma)** allowance.

| Setting | What it does | Recommended value |
|---|---|---|
| **Cc accreditation (comatose forfait)** | Tick if the facility holds the accreditation allowing it to bill the **Ccoma** coma allowance. Without it, a resident classified as Ccoma is **not** billable via eFact (neither regional nor federal); accommodation is still billed. | Tick **only** if your facility is accredited. |

:::{admonition} Not to be confused with the allowance amount
:class: note

The ordinary **dependency allowance** is the **same amount** for all Katz
categories; the category is used to **declare the profile** to the health
insurance fund, not to set the amount (see
[The INAMI dependency allowance](forfait-inami.md)). The Cc accreditation
concerns only the **special case of the coma allowance**.
:::

### Absence management

The **AViQ presence-day rules** are **built into** WideCare and are not
configured here: the noon rule for leave, and their own thresholds for a
hospitalization. Only the **assignee** of a follow-up activity is configurable.

| Setting | What it does | Recommended value |
|---|---|---|
| **Katz activity assignee** | User to whom the "New Katz required" activity is assigned when a hospital readmission exceeds **30 days**. If empty: current user (if clinical), otherwise the first head nurse, nurse or doctor found. | The **head nurse** (or the care manager). |

:::{admonition} Why 30 days?
:class: note

A readmission after more than 30 days of hospitalization requires a **new Katz
assessment**. The assigned activity acts as a reminder. See
[The Katz assessment](katz.md) and
[Absences and hospitalizations](../facturation/absences.md).
:::

## INAMI rates and pseudo-codes

*Billing → Configuration → INAMI Rates.* The rate grid carries the amounts of
the **INAMI dependency allowance** (rate type **INAMI Forfait**) and of the
accommodation, dated by **Start Date** and **End Date**.

- **Katz Category**: O, A, B, C, Cd, D and Ccoma. Under the **AViQ** rates the
  amount is the **same** for every category, including O; the grid stays
  configurable per category if a convention requires it.
- **Stay Type**: the sector the rate prices (MR, MRS, CSJ). A rate left empty
  applies whatever the sector; the sector-specific one wins when both exist.
- **Generate a year**, above the list, creates the rates of a whole year from
  the amounts you enter once; **New** adds a single row.

When an eFact is built for a year that has no rate yet, WideCare stops and
offers to open or create the INAMI rates of that year.

*Billing → Configuration → Billing Codes.* The **pseudo-codes** the health
insurer is billed with. Each code carries its **Pseudo-code**, its
**Category**, and, for the daily allowance:

- **Federated entity**: who publishes the code — Wallonia (AViQ), Brussels
  (Iriscare)… Each entity has its own series for the same Katz categories;
- **Katz category** and **Sector**: a Katz B resident in an MR is billed with
  the MR code, never the MRS one — the health insurer rejects a pseudo-code
  that does not match the agreed sector;
- **Partial intervention (IP)**: the variant where the patient carries part of
  the allowance.

A supplement declared to the health insurer carries its **Pseudo-code** on the
product, and its product category is **Declared to the OA (ET50)** (see
[Applying supplements](../facturation/application-supplements.md)).

## Health insurers and CPAS

- **Mutuelles** (*Billing → Configuration → Mutuelles*): the list of health
  insurers (insurance organisations, OA), used for
  [insurability (MDA)](ehealth/mda.md) and [eFact](ehealth/efact.md).
- **CPAS** (*Billing → Configuration → CPAS*): the public welfare centres that
  pay for some residents. See [CPAS coverage](cpas.md).

## Other Belgian settings

- **Nursing Home** tab: with the Belgian pack, the **Nursing Home** settings
  are those of an **MR/MRS**; the default values of the
  [general settings](../configuration/reglages-generaux.md) (30 days, 1 bed)
  suit most of them.
- **Medical** tab: the **Hide Empty Stat Cards** setting also hides the
  **Katz renewals** card when it is at 0; the **SAM medicines** block connects
  WideCare to the Belgian medicines database (see
  [The SAM medication database](sam-base-medicaments.md)).
- **Documents**: the ready-made tags include **Katz evaluation**, **MR/MRS
  agreement (eAgreement)**, **OA allocation** and **CPAS**, next to the common
  ones (see [Document settings](../configuration/reglages-documents.md)).
- **Approvals**: the INAMI number and the certificate of each approval are
  those used in the eHealth exchanges (MDA, eFact, eAgreement) — see
  [eHealth and eFact settings](reglages-ehealth.md).

## What's next

- [eHealth and eFact settings](reglages-ehealth.md)
- [The INAMI dependency allowance](forfait-inami.md)
- [The Katz assessment](katz.md)
- [The billing journey](parcours-facturation.md)
- [Billing settings](../configuration/reglages-facturation.md)
- [Belgium](index.md)
