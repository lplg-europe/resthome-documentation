---
modules: [serviced_living_billing]
---

# Regimes

:::{rh-description}
The regime of a serviced residence holds the rules of the authority that licenses it: who may enter, how the price is billed, how it may rise, the deposit, the notice and what the file must keep.
:::

:::{rh-faq}
What is a regime?
: The set of rules one public authority sets for the residences it licenses. Each residence runs under one regime, and the contracts, the billing and the registers read their rules from it.

Where do the regimes come from?
: Your country's pack brings them, ready to use. A house may also write its own in **Serviced Living → Configuration → Regimes**.

Can I change a value of a regime?
: Yes, on the regime itself. A value the authority sets differently for your residence is changed there, never anywhere else.

Does a regime refuse a contract?
: Only where the rule is strict: a missing piece of the file, the house rules not handed over before the signature, an increase above the cap. The age of an occupant or the surface of a unit only shows a warning.

Which pieces does the file ask for?
: The ones listed in **Serviced Living → Configuration → Pieces of the file**. A piece ticked **Required to sign** holds the signature back until it is received.
:::

Each authority that licenses serviced residences sets its own rules: an
entry age, a price per month or per day, a cap on increases, a notice period, a
register of calls. The **regime** holds those rules in one place, and the
application applies them on every residence that runs under it.

Open **Serviced Living → Configuration → Regimes**.

## The regime's sheet

Next to its **Code**, its **Country** and its **Authority**, a regime groups its
rules by theme. A value left at 0 means "no rule".

### Who and where

- **Minimum age** — the age required on entry. A younger occupant shows a
  warning on the contract, without refusing it.
- **Minimum units** / **Maximum units** — the size of a residence. Outside the
  range, the residence shows a warning.
- **Surface for one person (m²)** / **Surface for two people (m²)** — the
  smallest unit. A smaller unit shows a warning on its record.

### Price

- **Price basis** — **Per month** or **Per day**. A new part of the price
  starts on this basis.
- **First month pro rata** — the month of entry is billed by the day.
- **Month started is due** — the last month is billed in full, whatever the
  day the unit is released.
- **Days due after a death** — days billed after the death of the last
  occupant; 0 bills until the unit is released.
- **Services on a separate invoice** — the optional services are invoiced apart
  from the rent.

### Price increases

- **Increase above the index (% per year)** — the largest increase per calendar
  year on top of the index.
- **Increase notice (days)** — days between the notice and the new price.
- **Increase needs approval** — a public body approves the increase beforehand.
- **Index step (%)** — indexation applies in multiples of this step.

How these rules apply is described in [Changing the price](changement-prix.md).

### Deposit

**Deposit** and **Deposit unit** (**Months of price** or **Days of price**): the
contract shows the expected deposit, and warns when the deposit received is
higher.

### Ending the contract

- **Notice unit** (**Months** or **Days**), **Notice from the resident**,
  **Notice from the manager**;
- **Manager states the reason** — a notice from the manager cannot be given
  without its reason;
- **Trial period (days)** and **Notice during the trial (days)** — during the
  trial, the notice on either side is the shorter one;
- **Withdrawal period (days)** — days to withdraw, from the day after the
  signature.

The contract shows **Trial until** and **Withdrawal until** when the regime has
them. See [Notice and release of a unit](preavis-liberation.md).

### Keeping the file

- **House rules before signature** — the contract cannot be signed before the
  date the house rules were handed over is filled in;
- **Call register required** — a call cannot be closed without when it was
  answered and what came of it;
- **Residents' council (months)** — the longest gap between two councils;
- **File retention (years)** — how long the file is kept after departure. The
  ended contract shows **File kept until**.

### Legal basis

The texts the sheet was read from, and what is still to confirm with the
authority.

<!-- screenshot to add: a regime sheet with its groups Who and where, Price, Price increases, Deposit, Ending the contract and Keeping the file -->

:::{admonition} A starting point, not a legal opinion
:class: warning

The regimes a country pack brings are read from the published texts. Check each
value with your authority, and change it on the regime when your licence says
otherwise.
:::

## Pieces of the file

**Serviced Living → Configuration → Pieces of the file** lists what a candidate
hands in: identity document, medical certificate, inventory of the unit…

- **Required to sign** — the contract cannot be signed until the piece is
  received.
- **Regimes** — the regimes that ask for this piece; empty, all of them.

Every new contract starts its **File** tab with the pieces of its regime. See
[Contracts and occupants](contrats.md).

:::{admonition} In Belgium
:class: rh-country rh-country-be

The Belgian pack brings the regimes of Wallonia, of Brussels (two
authorities) and of Flanders, the usual pieces of a Belgian file and the health
index. See [Serviced residences in Belgium](../belgique/residences-services.md).
:::

## Going further

- [Residences and units](residences-logements.md)
- [Changing the price](changement-prix.md)
