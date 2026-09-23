# Institutional allowance

:::{rh-description}
The Resthome Forfait application: computing the institutional allowance (AViQ) from the days billed and the staff present, over the reference period.
:::

:::{rh-faq}
What does the Forfait application compute?
: The institutional allowance paid to the facility for a funding year, from the days billed to the health insurers and the staff actually present over the reference period.

What period does it use?
: The reference period runs from 1 July to 30 June, in four quarters. The allowance computed from it is paid from 1 January to 31 December of the following year.

Who may use it?
: Reading is open to the Forfait reader role; computing, simulating and validating are reserved to the manager role — this is the facility's payroll.
:::

:::{toctree}
:hidden:

calcul
suivi-simulations
:::

The **Forfait** application computes the **institutional allowance**: what the
facility receives per day and per resident, for a funding year.

## The principle

The allowance is, in essence, the funded payroll divided by the days billed. So
it rests on two figures, both taken over the **reference period**:

- the **days billed** to the health insurers, per sector and Katz category;
- the **staff present**, in full-time equivalents per qualification.

From these, Resthome computes the **norm** (how many FTE the facility should
have for its residents), what is **funded**, and the fourteen **parts** of the
allowance (A1 to W1).

:::{admonition} Two periods not to confuse
:class: note

- **Reference period** — 1 July to 30 June, in four quarters. This is what is
  measured.
- **Paid over** — 1 January to 31 December of the following year. This is when
  the allowance computed above is received.
:::

:::{admonition} Losing occupancy raises the allowance
:class: warning

It is counter-intuitive, and it is worth knowing: the allowance is a payroll
divided by days. Fewer days billed over the reference period means a **higher**
daily allowance the following year.
:::

## What Resthome takes, what you enter

- **Taken automatically**: the days billed to the health insurers, the average
  number of residents, the dependency rate, the licensed beds, and the norms,
  salary scales and parameters of the region.
- **Entered by you**: about thirty figures a year — the FTE per qualification
  and per quarter, the seniority, the disoriented residents, the function
  complements, the dementia reference person, and the **allowance notified** by
  the payer.

## Regions

Only the **Wallonia (AViQ)** assembly is implemented. Brussels (Iriscare) and
Flanders raise an error rather than approximate a figure that would be wrong.

## What's next

- [Computing the allowance](calcul.md) — the steps, from collection to the rates.
- [Simulations and live tracking](suivi-simulations.md) — trying a change, following the year in progress.
