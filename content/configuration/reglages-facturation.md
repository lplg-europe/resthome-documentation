---
modules: [healthcare_accommodation_billing, resthome_sales, resthome_split_billing, resthome_supplements, resthome_pocket_money]
sectors: [mr, csj]
---

# Billing settings

:::{rh-description}
Configure WideCare's Billing settings tab for a nursing home: automatic invoicing, billing refresh, journals, the resident fiscal position, pocket money and split billing.
:::

:::{rh-faq}
Where are the billing settings located?
: In Settings → Billing. The tab is only visible to the home's managers. It gathers automatic invoicing, the billing journals and the optional features such as split billing.

Should automatic billing refresh be turned on?
: Yes, that is the recommended value. It keeps every open billing period up to date as soon as the data behind it changes: supplement, absence, end of stay, room change, payer change, mid-month admission. Turn it off only if you prefer to recalculate by clicking Refresh on the period.

What is the Resident Journal for?
: It is the sales journal that receives the invoices for the resident's share (accommodation and supplements). Where the health insurer also pays part of the stay, its share goes into a journal of its own.

Why does the Resident Journal say "From" another house?
: In a group, a house without a journal of its own uses its parent company's. The setting shows which house it comes from; choose a journal to give the house its own.

Does turning on split billing install something?
: Yes. Ticking Split Billing (food debtors) installs the split billing feature, which then adds its own journal and suspense account to the same block.
:::

The **Billing** settings tab gathers the parameters that drive the **billing**
of your nursing home: invoice generation, accounting journals and optional
features. You configure them **once**, then they only change at the margins.

You will find them under **Settings → Billing**, or from the Billing app,
**Configuration → Settings**. The tab is only visible to the home's
**managers**.

<!-- screenshot to update: Settings, Billing tab, with the three blocks -->

:::{admonition} In Belgium
:class: rh-country rh-country-be

The tab is called **MR/MRS Billing** and holds more settings: the **INAMI
Journal**, the establishment's **Cc accreditation** for the coma allowance, and
the **Katz activity assignee** used after a long hospitalization. The eHealth
certificate and credentials are set elsewhere. See
[Belgian settings](../belgique/reglages.md) and
[eHealth and eFact settings](../belgique/reglages-ehealth.md).
:::

## Automatic Invoicing

This block decides **how** and **when** invoices are produced, and whether open
periods keep themselves up to date on their own.

| Setting | What it does | Recommended value |
|---|---|---|
| **Automatic Invoicing** | Generates the monthly stay invoices on its own, without going through the manual cycle. Off by default. | Often left **off** in favour of the manual cycle (generate → invoice), which gives more control. |
| **Invoice Day** … **of the month** | The day of the month automatic invoices are generated. Shown only when Automatic Invoicing is on. | **1** by default; adjust to your organisation. |
| **Automatic billing refresh** | Keeps every open period up to date as soon as the data behind it changes: supplement, absence, end of stay, room change, payer change, mid-month admission. | **On** — recommended. |

:::{admonition} Automatic refresh and the Refresh button
:class: tip

With refresh **on**, adding a supplement or an absence reaches the period on its
own: you generally have nothing to do. The period's **Refresh** button remains
available for a full recalculation on demand. See
[Billing a month](../facturation/facturer-un-mois.md).
:::

## Billing Journals

The **resident's share** (accommodation and supplements) goes into its own
sales journal. Where the country has a care allowance paid by the health
insurer, the country pack adds a second journal for that share, so each payer
is tracked separately.

| Setting | What it does | Recommended value |
|---|---|---|
| **Resident Journal** | Sales journal of the invoices for the **resident's share**. Only sales journals can be chosen. In a group, a house without its own journal shows **From** *parent house*: *journal*. | A sales journal of your facility, **separate** from the health insurer's when there is one. |
| **Resident Fiscal Position** | Applied to the residents' supplement envelopes. Pointed at a VAT-exempt position, everything billed to a resident comes out untaxed, while the products keep their normal taxes elsewhere. | The fiscal position your country applies to accommodation in a care home. |
| **Pocket money journal** | Journal of the **second invoice** of residents with pocket money: what the home bought for them during the month. Empty, everything stays on a single invoice. | A journal of its own, if you hold [pocket money](../argent-de-poche/mise-en-place.md). |
| **Pocket money settlement journal** | When filled in, the second invoice is **settled automatically** out of the pocket money balance as soon as it is posted. Empty, that settlement is entered by hand. | Ask your accountant. |

The two pocket money settings only appear when pocket money is installed.

:::{admonition} Facility-specific value
:class: warning

The journals depend on **your chart of accounts**. Choose existing **sales**
journals. Keeping one journal per payer makes reconciliation and per-payer
tracking easier.
:::

## Optional features

| Setting | What it does | Recommended value |
|---|---|---|
| **Split Billing (food debtors)** | Splits the resident's share of the monthly invoice among several debtors. Ticking it **installs** the feature. | Tick it **if** debtors share the resident's share. |
| **Split Billing Journal** | Sales journal, with its own sequence, of the split-billing resident statements. Shown once split billing is installed. | A journal used for nothing else. |
| **Split Billing Suspense Account** | The suspense account carrying every line of the split-billing resident statements. Shown once split billing is installed. | Ask your accountant. |
| **Other supplement** | Product charged when a [recharged vendor bill](../facturation/refacturation-fournisseur.md) line names no supplement of its own. Empty, such a line stops the recharge instead. | Empty until the home has decided — the safer default. |

:::{admonition} What the split billing checkbox does
:class: tip

Ticking installs the feature and unticking uninstalls it. Once installed, the
split is set per resident. See
[Setting up a split](../facturation-partagee/configuration.md).
:::

## What is set elsewhere

- **Absences** — the discount granted for an absence is set under **Billing →
  Configuration → Absence Discount Rules**. Whether a day counts as a presence
  day is **built in**: a departure after noon or a return before noon counts as
  a presence day, unless the country pack applies its own thresholds. See
  [Absences and hospitalizations](../facturation/absences.md).
- **Prices** — the supplement prices and their yearly increase. See
  [Price indexation](../facturation/indexation-des-prix.md).
- **The invoice type** of each resident (in advance or in arrears) — on the
  resident's contact. See [Invoice type](../facturation/type-de-facture.md).
- **The accounting bridge** — under **Settings → Sync**. See
  [Accounting bridge](../facturation/pont-comptable.md).

## Going further

- [Configuration](index.md) — rooms, rates, health insurers, facility.
- [Billing overview](../facturation/index.md)
- [Billing a month, step by step](../facturation/facturer-un-mois.md)
- [Split billing](../facturation-partagee/index.md)
