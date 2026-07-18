---
howto_auto: true
---

# CPAS coverage

:::{rh-description}
CPAS coverage in a nursing home (MR/MRS): recording the decision, full or partial coverage, and routing the resident-share invoice.
:::

:::{rh-faq}
How do I record that a resident is covered by the CPAS?
: On the resident record, open the Billing tab, tick "Covered by CPAS", choose the responsible CPAS and the coverage (full or partial). These fields record the CPAS decision and are tracked in the financial audit log.

Does the CPAS pay everything or only part of it?
: Both cases are supported. "Full coverage": the CPAS covers the entire resident share. "Partial coverage": the CPAS pays a share and you enter the "CPAS monthly amount"; the rest is borne by the resident or their family.

Does ticking "Covered by CPAS" automatically send the invoice to the CPAS?
: No. The CPAS section is a record of the decision, not a splitting engine. To send the resident share to the CPAS, fill in the resident's "Billing contact" (the CPAS); to split between the CPAS and another payer, use maintenance debtors (split billing).

Where do you create a CPAS in Resthome?
: In the Billing app, Configuration → CPAS. Create the contact (company) and tick "Is a CPAS". Only contacts flagged this way appear in the CPAS field of the resident record.

Is the dependency allowance affected by CPAS coverage?
: No. The dependency allowance goes to the health insurance fund via eFact (third-party payer). CPAS coverage concerns only the resident share: accommodation (the room) and supplements.

Is the CPAS monthly amount the same for all residents?
: No. The amount depends on the CPAS decision for that resident: it is a value specific to each case, to be entered based on the notification received from the CPAS.
:::

When a resident cannot afford their **personal share** (accommodation and
supplements), the **CPAS** (Public Centre for Social Welfare) of their
municipality can **cover it**, in full or in part. Resthome lets you **record
this decision** on the resident record and **route the invoice** to the right
debtor.

You'll find these settings in the **Billing** tab of the resident record, and the
list of CPAS in **Billing → Configuration → CPAS**.

:::{admonition} What the CPAS covers
:class: note

The CPAS steps in on the **resident share** (room + supplements), not on the
**dependency allowance**: the latter is covered 100% by the health insurance fund
and billed via [eFact](../ehealth/efact.md). See
[The INAMI dependency allowance](forfait-inami.md).
:::

## What CPAS coverage is for

Two notions must be distinguished:

- **Record the decision** — who the CPAS is, from when, under which reference, for
  what coverage and what amount. This information documents the case and is
  **tracked in the audit log** (financial category).
- **Route the invoice** — decide **who** Resthome sends the resident share to: the
  resident, their family, or the CPAS. This routing is driven by the **Billing
  contact** or by **maintenance debtors** (see below).

<!-- screenshot to add: a resident's Billing tab with the "Default payer" and "CPAS assistance" groups -->

## 1. Declare the CPAS as an organisation

Before linking a resident to a CPAS, the CPAS must exist as a contact.

1. Open **Billing → Configuration → CPAS**.
2. Click **New** and enter the CPAS **name**, its city, phone and email.
3. Check that the **"Is a CPAS"** box is ticked (it is by default from this menu).
4. **Save.**

:::{admonition} Why tick "Is a CPAS"
:class: tip

The **CPAS** field on the resident record only offers contacts flagged
**"Is a CPAS"**. A CPAS created elsewhere (in the generic contacts) will appear in
the list only if this box is ticked on its record.
:::

## 2. Enter the coverage on the resident record

1. Open the **resident** record and the **Billing** tab.
2. In the **CPAS assistance** group, tick **Covered by CPAS**.
3. Select the responsible **CPAS**.
4. Choose the **CPAS coverage**: *Full coverage* or *Partial coverage*.
5. For partial coverage, enter the **CPAS monthly amount**.
6. Complete the **CPAS decision**: date, reference and, if needed, **CPAS notes**.

| Field | Role |
|---|---|
| **Covered by CPAS** | Activates the coverage and switches the **Default payer** to CPAS |
| **CPAS** | The responsible organisation (list filtered on "Is a CPAS") |
| **CPAS coverage** | *Full* (the CPAS pays everything) or *Partial* (the CPAS pays a share) |
| **CPAS decision date** | Date of the grant decision |
| **CPAS decision reference** | Number / reference of the received decision |
| **CPAS monthly amount** | Amount paid by the CPAS — **partial coverage only** |
| **CPAS notes** | Free text (conditions, contact, remarks) |

:::{admonition} Fields that appear as you go
:class: info

The CPAS, the coverage and the **CPAS decision** block only show once
**"Covered by CPAS"** is ticked. The **CPAS monthly amount** only appears for
**partial** coverage.
:::

## 3. Route the invoice to the CPAS

This is the step that decides **who** the resident-share invoice goes to.

- **The CPAS pays everything** → set the resident's **Billing contact** (in the
  *Default payer* group) to the **CPAS** contact. The monthly resident-share
  invoice will then be **sent to the CPAS**.
- **The CPAS pays part of it** → use
  [maintenance debtors (split billing)](split-billing.md): add the CPAS as a debtor
  with its **percentage**, and the remaining payers (resident, family) for the
  balance.

:::{admonition} The "CPAS assistance" section is a record, not a splitting engine
:class: warning

The fields in the **CPAS assistance** section document the decision and switch the
**Default payer** to CPAS, but **they do not automatically redirect or split the
invoice**. The invoice recipient stays determined by the resident's **Billing
contact** (or the stay's billing contact), and the partial split by **split
billing**. Without one of these two levers, the resident share keeps being sent
**to the resident**.
:::

## What Resthome does — and does not do

| Action | Automatic? |
|---|---|
| Track the CPAS decision (financial audit) | Yes, as soon as it's entered |
| Switch the **Default payer** to CPAS when you tick "Covered by CPAS" | Yes |
| Send the invoice to the CPAS | No — via the **Billing contact** |
| Split the resident share between CPAS and family | No — via [split billing](split-billing.md) |
| Deduct the **CPAS monthly amount** from the billed amounts | No — informational field |

## Key points to remember

- CPAS coverage concerns the **resident share** (room + supplements), not the
  **dependency allowance** (health-insurance-fund share, via eFact).
- First create the CPAS in **Billing → Configuration → CPAS** (**"Is a CPAS"**
  box), then link it to the resident in the **Billing** tab.
- Coverage is **full** or **partial**; the **CPAS monthly amount** only applies to
  partial coverage.
- The **CPAS assistance** section **records** the decision; to **route** the
  invoice, use the **Billing contact** (full coverage) or **split billing**
  (partial coverage).
- The **CPAS monthly amount** and the decision reference are **specific to each
  case**, based on the CPAS notification.

## Going further

- [Manage a resident](../residents/gerer-un-resident.md)
- [Bill a month](facturer-un-mois.md)
- [Maintenance debtors (split billing)](split-billing.md)
- [The INAMI dependency allowance](forfait-inami.md)
