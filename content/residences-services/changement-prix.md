---
howto_auto: true
modules: [serviced_living_billing]
---

# Changing the price

:::{rh-description}
Raise or lower the price of serviced residence contracts by a percentage, with the notice, the yearly cap and the index steps of the regime checked before the new price applies.
:::

:::{rh-faq}
How do I index the price of every contract at once?
: In **Serviced Living → Contracts**, select the contracts, then **Actions → Change the price**. The same change applies to each of them.

Do past months change?
: No. Each part of the price stops the day before the new price and starts again at the new amount: the months already billed keep their price.

Why is the increase refused?
: Either the new price starts too soon after the notice, or the increase above the index goes beyond the regime's yearly cap. The message gives the earliest date or the cap.

Is a decrease checked too?
: No. The notice and the cap only apply to an increase.

Who can change a price?
: The Serviced Living manager role only.
:::

A price change raises or lowers every running part of a contract's price by a
percentage, from a given date. The regime's rules are checked first: the notice
before the new price, the cap above the index, the steps of indexation.

## 1. Open the window

- On one contract, **Running** or **Under notice**: click **Change the price**.
- On several contracts: select them in **Serviced Living → Contracts**, then
  **Actions → Change the price**.

## 2. Fill in the change

- **Change (%)** — the change of the price; negative for a decrease.
- **Of which index (%)** — the part of the change that follows the index. Only
  what is above it counts against the yearly cap. Proposed by the country's
  pack when it knows the index.
- **Notified on** — the day the residents were told, today by default.
- **Applies from** — proposed from **Notified on** plus the regime's notice.
- **Contracts** — the contracts concerned.

A warning shows when the regime asks for the approval of a public body before
an increase, or when the index part is not a multiple of the regime's index
step.

## 3. Apply

Click **Apply**. For each contract:

- each part of the price running on **Applies from** stops the day before and
  starts again at the new amount;
- the change is added to the **Price changes** list of the **Price** tab, with
  **Applies from**, **Notified on**, **Change (%)** and **Index (%)**;
- the contract's chatter records it.

The next generation of a billing period bills the new price from its date.

## What is refused

- **Too early** — the regime asks for a number of days between the notice and
  the new price; the message gives the earliest date for each contract.
- **Above the cap** — the increases above the index of the same calendar year,
  added up, go beyond the regime's **Increase above the index (% per year)**.

<!-- screenshot to add: the Change the price window with the change, the index part, the dates and the contracts -->

:::{admonition} In Belgium
:class: rh-country rh-country-be

The index part is read from the health index typed in under
**Serviced Living → Configuration → Health index**. See
[Serviced residences in Belgium](../belgique/residences-services.md).
:::

## Going further

- [Billing a residence](facturation.md)
- [Regimes](regimes.md)
