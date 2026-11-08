---
modules: [serviced_living_billing]
sectors: [rs]
---

# Billing a residence

:::{rh-description}
Bill a serviced residence every month: the contract's price in parts, the deposit, the residents in the month's billing period, adjustments, credit notes and the services included in the price.
:::

:::{rh-faq}
Where is a residence billed?
: In the same monthly billing period as the rest of the house: **Billing → Facturation → Billing Periods**, then **Generate**. Each contract adds its lines for the residents of the residence.

Is the rent reduced when the resident is away?
: No. The price does not depend on the days spent at home: a residence records no absence.

A price was corrected after the month was invoiced. What happens?
: At the next generation, the difference lands on its own adjustment line. When a month only gives money back, its invoice becomes a credit note.

Why is a contract billing nothing?
: It has no price. The contract shows *This contract has no price: it bills nothing*, the period's chatter names it after the generation, and the billing dashboard counts it.

Why is a service not billed?
: It is listed in **Included in the price** on the residence: the price already covers it, so it is never billed on top. The period's chatter names it.

Does the contract fix the VAT?
: No. Each part of the price has a product, and the product carries the VAT and the income account. Set the VAT on the products with your accountant.
:::

A residence bills from its **contracts**: no daily rate, no care allowance, an
ordinary invoice to the resident every month. The residents of the residence
join the **same billing period** as the rest of the house; see
[Billing a month, step by step](../facturation/facturer-un-mois.md) for the
period itself.

## The price of a contract

The **Price** tab of the contract lists the **parts of the price**:

| Column | Purpose |
| --- | --- |
| **Component** | **Rent**, **Charges**, **Common services** or **Care share**. |
| **Product** | Proposed from the component. It carries the VAT and the income account of this part. |
| **Amount** | The amount of this part. |
| **Basis** | **Per month** or **Per day**, proposed from the regime. |
| **From** / **Until** | When this part applies. Empty: from the start, or until the end, of the contract. |

**Price per month** adds up the parts running today. The contracts list shows it
too.

- An **Owner-occupier** contract is never billed its **Rent**: the occupant pays
  for the services only.
- A new contract on a unit starts from the last price of that unit, to read and
  adjust before signing.
- To raise or lower the price of a running contract, use **Change the price**,
  which keeps past months at their price — see
  [Changing the price](changement-prix.md).

<!-- screenshot to add: the Price tab of a contract, with rent and charges, the deposit group and the price changes -->

### The deposit

The **Deposit** group of the **Price** tab keeps:

- **Deposit expected** — what the regime asks for, at the current price;
- **Deposit received** and **Received on**;
- **Deposit account** — the individual account the deposit is kept on;
- **Returned on**.

The contract warns when the deposit received is above what the regime allows.

### Billed from

**Billed from**, in the contract's dates, is the first day billed by the
application — the entry date by default. Move it forward when earlier months
were billed elsewhere, for example before the residence started with the
application.

## The residence's own settings

On the residence (**Serviced Living → Configuration → Residences**):

- **Invoice journal** — numbers this residence's invoices apart. Empty, they use
  the company's resident journal.
- **Included in the price** — the services the price already covers. A
  supplement, a service request or a meal on one of these products is never
  billed on top.

## Billing the month

1. Open the month's period in **Billing → Facturation → Billing Periods**.
2. Click **Generate**, as for any month.
3. In the **Residents** tab, the residents of the residence show beside the
   others, with their **Unit** and their **Contract**, and without presence or
   absence days.
4. Create and confirm the invoices as usual.

For each contract, the generation bills:

- one line per part of the price, on the person **Invoiced to**;
- the supplements of each occupant, on every day spent in the unit;
- the meals taken at the residence, when they are billed — see
  [Meals in a residence](repas.md);
- the service requests done — see [Service requests](demandes.md).

A second occupant only shows in the period when they have something of their
own to pay. A contract's lines follow the contract: to change a price, change it
on the contract, not on the period.

### How an incomplete month is billed

The regime decides:

- **First month pro rata** — the month of entry is billed by the day;
- **Month started is due** — the month of departure is billed in full;
- a price that changes during a month is billed by the day on each side of the
  change.

### Corrections, adjustments and credit notes

Every generation compares, month by month, what is **due** with what was
already **billed**. An entry recorded late, a release, a notice that ends early
or a price corrected afterwards each lands on one **Adjustment** line for the
difference. Generating again gives the same answer.

When a month only gives money back, its invoice is a **credit note**.

### Services on a separate invoice

When the regime ticks **Services on a separate invoice**, the optional services
(supplements, meals, service requests) go on an invoice of their own, and the
contract's price stays on the ordinary one.

### What the period tells you

After the generation, the period's chatter names:

- the contracts without a price, which billed nothing;
- the services included in the price, which were not billed;
- the contracts billed for several months at once — move **Billed from** forward
  if those months were billed elsewhere, then generate again.

## The billing dashboard

When the house has a residence, **Billing → Dashboard** adds a **Serviced
living** lane:

- **Running contracts** — the units billed this month;
- **Contracts without a price** — running and billing nothing;
- **Units to release** — nobody lives there, still billed.

Each figure opens the contracts it counts.

:::{admonition} In Belgium
:class: rh-country rh-country-be

A resident of a residence never enters the insurer's billing: no dependency
category, no insurer share, no electronic invoicing. See
[Serviced residences in Belgium](../belgique/residences-services.md).
:::

## Going further

- [Changing the price](changement-prix.md)
- [Notice and release of a unit](preavis-liberation.md)
- [Supplements](../facturation/supplements.md)
