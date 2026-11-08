---
howto_auto: true
modules: [serviced_living_billing]
sectors: [rs]
---

# Contracts and occupants

:::{rh-description}
Welcome a resident into a serviced residence: write the contract on a unit, add its occupants, complete the file, sign, then move in.
:::

:::{rh-faq}
How do I add a new resident to a residence?
: In **Serviced Living → Residents**, click **New**: a new contract opens, where you add the person as an occupant. A person is never created alone, without a contract.

A couple shares a flat. One contract or two?
: One. A contract holds one unit and as many occupants as needed, so a couple pays one rent. The invoice goes to the person in **Invoiced to**, the first occupant by default.

Why is Sign refused?
: The contract needs at least one occupant, every piece of the file ticked **Required to sign** must be received, and, when the regime asks for it, the date the house rules were handed over must be filled in. The message names what is missing.

Why can I not move the resident in?
: Nobody moves in on an unsigned contract. Sign it first; **Move in** then appears.

Can I delete a contract?
: Only one that was never signed. A signed contract is part of the file the regime asks to keep: cancel it before the move-in, or end it by releasing the unit.

How do I readmit a former resident?
: On their record, in the **Stay Agreement** tab, click **Readmit**: a new contract opens with the person already listed as an occupant.
:::

In a residence, the **contract** carries everything: the unit, the people who
live there, the price, the file and the dates. Admissions, meals, the care app
and the billing all follow it.

<!-- screenshot to add: a contract form with its status bar, the unit, the dates and the Occupants tab -->

## The states of a contract

| State | Meaning |
| --- | --- |
| **To sign** | Being prepared: unit, occupants, price and file. |
| **Signed** | Signed, waiting for the move-in. |
| **Running** | The occupants live there; the unit is billed. |
| **Under notice** | Notice was given; the unit is still billed. |
| **Ended** | The unit was handed back. |
| **Cancelled** | Given up before the move-in. **Back to draft** brings it back to **To sign**. |

**Serviced Living → Contracts** opens on the current contracts. The filters
**To sign**, **Under notice** and **To release** pick out what needs action; the
list also shows the occupants, the **Price per month** and the end of a notice.

## 1. Open a new contract

Three doors lead to the same contract:

- **Serviced Living → Residents**, then **New**;
- **Serviced Living → Contracts**, then **New**;
- the **New contract** button on a free unit.

Choose the **Unit**: the **Residence** and its **Regime** follow. The **Entry
date** is required. The **Reference** is given on saving.

:::{admonition} A unit let again
:class: tip

A new contract on a unit starts from the last price of that unit, still to read
and adjust before signing. See [Billing a residence](facturation.md).
:::

## 2. Add the occupants

In the **Occupants** tab, add a line per person and choose them, or create them
with **Create and edit…**. Each line shows the age, **Moved in** and **Left on**.

- A person added as an occupant becomes a **resident**. A spouse already known
  as a family contact becomes a resident on the day they are added.
- **Invoiced to** — who receives the invoice: the first occupant, unless you
  choose someone else.
- **Owner-occupier** — the occupant owns the unit and pays for the services
  only: the rent part of the price is not billed.

The contract warns, without refusing, when an occupant is younger than the
regime's minimum age, or when there are more occupants than the unit holds.

## 3. Set the price

The **Price** tab holds the parts of the price, the deposit and the price
changes. See [Billing a residence](facturation.md).

## 4. Complete the file

The **File** tab starts with the pieces the regime asks for. For each piece,
fill in **Received on** and attach the scan in **Files**. A piece ticked
**Required to sign** holds the signature back until it is received.

Fill in **House rules handed over on** when the house rules are handed over:
some regimes ask for it before the signature.

## 5. Sign

Click **Sign**. WideCare checks that:

- the contract has at least one occupant;
- the house rules were handed over, when the regime asks for it before the
  signature;
- every required piece of the file was received.

The contract becomes **Signed** and **Signed on** is filled in with today's
date, unless you entered another one. When the regime has them, **Trial until**
and **Withdrawal until** appear.

## 6. Move in

On the day the occupants arrive, click **Move in**. The contract becomes
**Running**: from now on the unit is occupied and billed.

:::{admonition} The unit is chosen until the move-in
:class: note

The **Unit** can only be changed while the contract is **To sign**. After that,
another unit is another contract.
:::

## From the Admissions application

An application for a residence follows the same pipeline as any other: see
[Admissions](../admissions/index.md).

- The admission request shows a **Residence** field as soon as the house has a
  residence. In a house of flats only, it is filled in already; in a house that
  also has beds, choose it to apply for a flat.
- The request then offers the residence's **unit types**, and the availability
  panel lists its units by type, with the free ones.
- **Admit** places the person in the chosen unit, on a contract: the running
  contract of that unit when there is one (a second occupant joins it), or a new
  contract **To sign**.

Price the contract, complete its file, then **Sign** and **Move in**.

:::{admonition} In Belgium
:class: rh-country rh-country-be

In a house that also runs a nursing home, the request asks for the stay type
first; choosing the residence's sector fills in the residence. See
[Serviced residences in Belgium](../belgique/residences-services.md).
:::

## The resident's record

**Serviced Living → Residents** lists the people living in a unit, as cards or
as a list. Their record is the house's ordinary resident record, with what fits
a flat:

- a **Unit** group instead of the stay: **Current unit**, the current
  **Contract** and **Moved in**;
- a **Contracts** smart button;
- the **Stay Agreement** tab lists their **Contracts** instead of the stays;
- **Home nurse** and **Home care service / coordination**: the resident's own
  care providers.

The stay exists underneath, but the residence's screens never show it: it opens
and closes with the contract.

:::{admonition} No absences in a residence
:class: note

The rent does not depend on the days spent at home. The **Absences** button and
tab do not show for a resident of a residence, and a stay in hospital opens no
absence.
:::

## Going further

- [Notice and release of a unit](preavis-liberation.md)
- [Billing a residence](facturation.md)
- [Regimes](regimes.md)
