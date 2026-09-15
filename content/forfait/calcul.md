---
howto_auto: true
---

# Computing the allowance

:::{rh-description}
Computing the institutional allowance in Resthome, step by step: collect the billed days, enter the staff, compute, compare with the notified figure, validate and apply to the INAMI rates.
:::

:::{rh-faq}
Which staff do I enter?
: The FTE actually worked, excluding Maribel, mobile teams, job-creation schemes 21-24, management, the dementia reference person and end-of-career measures.

Why is the nursing norm shown on two lines?
: Because A1 and A2 nurses share a single norm. It appears on both lines and must not be counted twice.

What does "Apply to the INAMI rates" do?
: It writes the computed allowance into the billing rate grid for the whole funding year, and closes the previous rates the day before.
:::

## 1. Open a calculation

Go to **Forfait → Calculations** and create one for the **funding year**, with
the **region** and the **reference period**.

## 2. Collect the billed days

Click **Collect billed days**: Resthome rebuilds the grid from what was actually
invoiced to the health insurers over the period, per sector and Katz category,
quarter by quarter.

:::{admonition} What was claimed, not what was lived
:class: note

These are the days **claimed** to the health insurers. A day that was never
billed is missing here too — deliberately: the payer counts what it received.
:::

## 3. Enter the staff

In the **Staff** tab, **Add the missing rows**, then fill in, per qualification
and per quarter, the **FTE actually worked** and the **seniority**.

Leave out what is funded elsewhere: Maribel, mobile teams, job-creation schemes
21-24, management, the dementia reference person and end-of-career measures.

The other figures — disoriented residents, function complements, dementia
reference person, A2 educator, care logistics assistant — go in the **Other
inputs** tab.

## 4. Compute

Click **Compute**. Resthome fills in:

- the **norm** in FTE, the **present** and the **funded** FTE;
- the **staff-shortage penalty**, if the facility is below the norm;
- the fourteen **parts** of the allowance, in the **Parts** tab;
- the **allowance computed**, and what is **left to the house**.

Enter the **allowance notified** by the payer: Resthome then shows the **gap**,
and what it represents over a year.

## 5. Validate

**Validate** freezes the file: it becomes the figure that was discussed with the
payer. A validated calculation no longer moves — to explore a change, duplicate
it as a [simulation](suivi-simulations.md).

**Back to draft** reopens it, and clears the results shown.

## 6. Apply to the INAMI rates

**Apply to the INAMI rates** writes the computed allowance into the billing rate
grid, for the whole funding year, and closes the previous rates the day before.

:::{admonition} Only from a validated calculation
:class: warning

The action refuses a calculation that is not validated, and refuses a
simulation. Running it again replaces the rates — it never stacks them.
:::

## What's next

- [Simulations and live tracking](suivi-simulations.md)
- [The INAMI package (dependency)](../facturation/forfait-inami.md)
