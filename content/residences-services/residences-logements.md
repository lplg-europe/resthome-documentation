---
howto_auto: true
modules: [serviced_living_billing]
---

# Residences and units

:::{rh-description}
Set up a serviced residence: create the residence, choose its regime, generate its units in one go, then follow them on the units board.
:::

:::{rh-faq}
Where do I create a residence?
: In **Serviced Living → Configuration → Residences**, with **New**. Only the Serviced Living manager role sees the Configuration menu.

How do I create the units of a residence?
: On the residence, click **Generate units**: give the number of floors, the units per floor and the unit type, and the units are numbered floor by floor behind the residence's prefix.

Why do unit numbers carry a prefix?
: A unit number is unique across the whole database: the prefix tells apart the 101 of two residences, or of a residence and a nursing home on the same database.

Can a unit of the residence hold a nursing home resident?
: No. A unit of a residence only holds residents of the residence, and a nursing home room never holds one.

The surface or the number of units does not match the regime. Is it refused?
: No. The residence or the unit shows a warning naming the rule; nothing is blocked, since a regime often allows exceptions for older buildings.
:::

A **residence** is a building of flats run under one set of rules. Its
**units** are the flats it lets. Set up both before the first contract: a
contract is always signed on a unit.

:::{admonition} No unit yet?
:class: tip

On a new database, **New** on the **Residents** list opens the form of a new
residence, with the message *No unit yet: create the residence, then generate
its units.* A new contract shows the same advice for as long as no unit exists.
:::

## 1. Create the residence

Open **Serviced Living → Configuration → Residences** and click **New**.

| Field | Purpose |
| --- | --- |
| **Regime** | The rules the residence runs under — see [Regimes](regimes.md). Required. |
| **Manager** | The person in charge of the residence. |
| **Address** | Where the residence is, when it is not at the company's address. |
| **Invoice journal** | Numbers this residence's invoices apart. Empty: the company's resident journal. |
| **Included in the price** | The services the price already covers: they are never billed on top. |

The right column counts the **Free units** and the **Occupants**. The smart
buttons open the **Units**, the **Contracts**, the **Open complaints** and the
**Councils** of the residence, and, when calls are installed, its **Open calls**
and **Open requests**.

<!-- screenshot to add: a residence form with its regime, its manager, the free units counter and the smart buttons -->

:::{admonition} Care followed here
:class: note

When the medical record is installed, the residence also shows **Care followed
here**. Unticked by default: the residents live at home and their care
providers are their own. Ticked, the residents join the care lists, the care
plan and the care app like the residents of a nursing home.
:::

## 2. Generate the units

1. On the residence, click **Generate units**.
2. Fill in the window:
   - **Building** — the name of the residence by default;
   - **Number Prefix** — proposed from the residence's name (for example `LIN-`
     for *The Lindens*), editable;
   - **Floors** and **First Floor** (0 for the ground floor);
   - **Units per Floor**;
   - **Unit Type** — **Studio** by default.
3. Check the **Numbering** preview, then click **Generate**.

The units are created in the residence, numbered floor by floor (`LIN-001`,
`LIN-101`…). Numbers already taken are left alone, and the message says which.
Run the window again to add another wing or another unit type.

:::{admonition} Three unit types ready to use
:class: note

The application comes with **Studio** (one person), **One-bedroom flat** and
**Two-bedroom flat** (two people each). Change or add types in
**Serviced Living → Configuration → Unit types**. A unit type of the residence
carries no daily rate: the price lives on the contract.
:::

## 3. Complete each unit

Open **Serviced Living → Units**. The units show as a board grouped by status —
**Available**, **Occupied**, **Under maintenance**, **Reserved** — like the rooms
of a nursing home. Each card shows the unit, its residence and its surface.

On the **unit's record**:

- **Unit type** and **Capacity**;
- **Residence** (required) and **Surface (m²)** — a warning shows when the
  surface is below what the regime asks for;
- the **Contract** smart button, while a contract holds the unit;
- the **Contracts** tab — every contract of the unit, with its occupants, its
  dates and its state. A unit's history is its contracts.

The **New contract** button opens a contract on this unit. It hides while a
contract already holds the unit, or while the unit is **Under maintenance** or
**Reserved**.

<!-- screenshot to add: the units board of a residence, grouped by status -->

:::{admonition} One contract per unit
:class: warning

A unit has one contract at a time, whatever the number of occupants. Moving to
another unit means releasing this one and signing a contract on the other — see
[Notice and release of a unit](preavis-liberation.md).
:::

## Warnings on the residence

The residence form says, without blocking anything:

- when the number of units is outside what the regime allows (*… asks for at
  least … units*, *… allows at most … units*);
- when the regime sets a rhythm for the residents' council and none was held in
  time — see [Complaints and council](registres.md);
- when the duty rota leaves nobody on duty right now — see
  [Calls and duty rota](appels.md).

:::{admonition} In Belgium
:class: rh-country rh-country-be

The residence also carries its **Operating title** and its fire certificate,
with a warning before they end, and an **Application** tab for the Katz asked
at application. See [Serviced residences in Belgium](../belgique/residences-services.md).
:::

## Going further

- [Regimes](regimes.md)
- [Contracts and occupants](contrats.md)
