---
howto_auto: true
---

# Payment tracking and settlement reconciliation

:::{rh-description}
Find out whether the health insurance fund has paid your nursing home (MR/MRS) lump sums: read the settlement (920900), reconcile it automatically and chase overdue OAs.
:::

:::{rh-faq}
What is the difference between the acknowledgement of receipt (931000) and the settlement (920900)?
: The acknowledgement (931000) only confirms that the insurer received your batch and passed the first check — nothing has been paid yet. The settlement (920900) is the final result: it shows, line by line, what is accepted and what is rejected, and serves as a payment notice under Account C. Until the settlement arrives, no amount is final.

How can I tell whether an eFact batch has been paid in Resthome?
: Open the batch: the Payment tab shows Paid, the payment reference and the amount. Under Account C, as soon as the settlement carries a real payment reference, Resthome marks the batch Paid automatically. For an overview, the eFact Cockpit gathers the settled batches not yet reconciled and the overdue OAs.

What does it mean to "reconcile" a settlement?
: Reconciling means confirming that the money announced by the settlement has actually been received. Resthome automatically matches each settlement to its batch; you confirm receipt by opening the settlement and clicking Mark Reconciled.

An insurer is late paying: can I claim late-payment interest?
: Yes, if the batch was submitted on time (by the 20th of month M+1 at the latest). The OA must pay by the end of the 2nd month following submission; beyond that, Resthome calculates the late-payment interest (accepted amount × legal rate × days late / 365). The legal rate is set in the eHealth settings.

The settlement shows both accepted AND rejected amounts: what should I do?
: This is a partial rejection: the accepted part is paid, the rejected lines must be corrected and resent. Resthome automatically creates a remainder for the rejected lines and lists them in the Cockpit's Rejected lines list.

Where can I see the list of all settlements and responses received from the OAs?
: The eFact Cockpit offers the OA retrievals list: all retrieved messages (acknowledgements, settlements, rejections), filterable by OA, month and type, with XLSX export. The eFact Settlements list, in contrast, shows only the settlements (920900).
:::

Once your lump sums have been sent via [eFact](efact.md), the real question
remains: **"have I been paid?"**. This page explains how Resthome answers it,
from the automatically reconciled **settlement (920900)** to **chasing overdue
insurers (OA)**.

You'll find everything in the **MR/MRS → eHealth → eFact** app:

- the **Cockpit** — your "what to do now" control board;
- **eFact Settlements** — the list of **settlements** received;
- **eFact Batches** — each batch and its **Payment tab**.

:::{admonition} Acknowledgement of receipt ≠ settlement
:class: info

Don't confuse the two OA responses. The **acknowledgement of receipt
(931000)** just says "received". The **settlement (920900)** says "here is
what I'm paying". It's the settlement that matters for the money.
:::

## Acknowledgement (931000) or settlement (920900): how to tell them apart

| Response | What it means | Is there a payment? |
|---|---|---|
| **Acknowledgement of receipt (931000)** | The OA has **received** your batch and passed the first format check. | No — nothing is decided yet. You must wait for the settlement. |
| **Settlement (920900)** | The **final result**, line by line: **accepted** and **rejected** amounts. Under Account C, it **serves as a payment notice**. | Yes — this is where what is actually paid appears. |

:::{admonition} Account C (Wallonia / AViQ)
:class: note

Since 2025, Walloon MR/MRS billing operates under **Account C**: the OA pays
and **the settlement acts as a payment notice**. The settlement therefore
carries the **payment reference** and the **amount**, but **no payment date**
(the format doesn't provide for one). Resthome never fabricates a date: it
stays empty until a real bank date is entered.
:::

## 1. The settlement (920900) reconciled automatically

When a settlement comes back from the OA (via automatic retrieval or a batch's
**Process Response** button), Resthome **reconciles it on its own**, with no
input from you:

1. it creates a **Settlement** record attached to the batch;
2. it **re-links each line** of the settlement to the billed line of the right
   resident (by NISS and amount);
3. it marks each line **accepted** or **rejected**; an accepted lump sum is not
   repeated in the settlement, so **any line not mentioned is deemed accepted**
   (AViQ rule);
4. it **updates the batch status**: **settled** (all accepted), **rejected**
   (all rejected) or **partial_reject** (a mix, or a partial settlement awaiting
   the rest);
5. if lines are rejected, it **automatically prepares a remainder** to resubmit
   them (see [eFact rejections](efact-rejets.md)).

Under Account C, as soon as the settlement carries a **real payment reference**
and a **positive accepted amount**, the batch is marked **Paid** automatically.
A fully rejected settlement (€0 accepted) carries a reference but pays nothing —
so it is **not** marked paid.

## 2. The eFact Settlements screen (the settlements)

Menu **eHealth → eFact → eFact Settlements**. This is the list of all
**settlements (920900)** received, one per payment.

The list shows: the **reference**, the **batch** concerned, the **receipt
date**, the **Accepted** / **Rejected** / **Paid** amounts and the **payment
reference**, plus a **status** badge.

<!-- screenshot to add: eFact Settlements list — one settlement per line with accepted/rejected/paid amounts and a status badge -->

Open a settlement for the details. The screen is **read-only** (nothing is
entered by hand) and follows three states:

| State | Meaning |
|---|---|
| **Received** | The settlement has just arrived. |
| **Processed** | Its lines have been allocated to the batch. Resthome does this step **automatically** on receipt. |
| **Reconciled** | You have **confirmed** that the money was actually received. |

- The **Process** button appears only if a settlement has stayed in *Received*
  without processing — click it to allocate the lines.
- The **Mark Reconciled** button confirms receipt of the payment once verified
  on your bank statement.

The **Lines** tab details, line by line: no., resident, amount claimed,
accepted, rejected, the **Accepted** checkbox, and — in case of refusal — the
**code** and **rejection reason**. Rejected lines stand out in red.

:::{admonition} Read the settlement as the OA sent it
:class: tip

A **Decoded 920900** button (reserved for eHealth managers) shows the raw
settlement file, zone by zone, to check a value as close to the source as
possible.
:::

## 3. A batch's Payment tab

On a batch ([eFact batches](efact.md)), once the batch has been sent, the
**Payment** group summarizes the payment status:

- **Paid** — the checkbox turns green when the batch is paid;
- **Payment Reference** — the OA's payment reference;
- **Payment Date** — the date (often empty under Account C, see above);
- **Total Paid** — the amount paid.

:::{admonition} Marking paid manually
:class: info

Some OAs pay without a usable payment reference in the settlement. An eHealth
manager can then enable **Marked Paid Manually** to attest to a payment
received outside the flow.
:::

A **Status** box shows in a badge what the batch is waiting for: *Awaiting OA
response*, *Awaiting settlement (920900)*, *Complete* or *Rejected*. When a
batch is **settled**, the **Close** button lets you file it away for good.

In the batch list, the **Paid** / **Unpaid** filters and the optional **Payment
Ref.**, **Payment Date**, **Amount Paid** columns help you take stock month by
month.

## 4. The eFact Cockpit: "have I been paid?" at a glance

Menu **eHealth → eFact → Cockpit** (also accessible from a period or a
dashboard card). The Cockpit organizes all the work into **action stacks**,
with a counter and a button per stack. Three stacks answer the payment question
directly.

<!-- screenshot to add: eFact Cockpit — counter buttons (To reconcile, Overdue payments, Rejected lines, OA retrievals) and the "Rejects by cause" table -->

- **To reconcile** — the batches **settled but whose payment is not yet
  confirmed**. The total expected amount is shown; the **Reconcile payments**
  button opens the list to reconcile them one by one.
- **Overdue payments** — the batches **accepted but still unpaid** whose **OA
  payment deadline has passed**. See chasing below.
- **Rejected lines** — the **worklist** of rejected lines still to be resent
  (resident + code + amount), filterable by cause, OA and month.

Two markers round out the picture:

- **OA retrievals** — the **complete log** of everything the OA has returned:
  acknowledgements, settlements and rejections, filterable by OA, month and
  type, with an **Export XLSX** button.
- **Rejects by cause** — a table that groups the rejected lines **by reason**,
  to tackle the systemic cause rather than line by line.

:::{admonition} Fetch the responses
:class: tip

If batches stay pending, the **Fetch responses** button queries the OA platform
and updates the statuses. Responses also arrive automatically, but this button
forces an immediate check.
:::

## 5. Chasing an overdue OA

The **Overdue payments** stack lists the batches **submitted on time**,
**accepted** by the OA but **unpaid** beyond the deadline. The **Chase (by
OA)** button opens these batches **grouped by insurer**: you immediately see
**who to chase** and **for how much** (the accepted total is summed per OA).

To write to the OA, the **Contact OA** button (present on each batch) prepares
contact with the right billing correspondent.

## 6. Late-payment interest (moratory interest)

A batch paid too late may entitle you to **late-payment interest**. Resthome
applies the AViQ rule:

- the batch must have been **submitted on time** (sent by the **20th of month
  M+1** at the latest) — this is the **eligibility** condition;
- the OA must pay **by the end of the 2nd month following submission**: this is
  the **OA Payment Deadline**;
- past this date, interest accrues, calculated as:
  **accepted amount × annual legal rate × days late / 365**.

On the batch, as soon as the deadline has passed and the batch is still unpaid,
a **Late-payment interest (OA)** group appears with the **deadline**, the **days
late** and the **interest due**. The batch list offers the **OA Payment
Overdue** filter and an **OA Pay Deadline** column (in red if passed).

:::{admonition} Enter the legal rate
:class: warning

The calculation stays at **0 as long as the legal rate is not entered**. Enter
the **annual legal interest rate** published under **eHealth → Settings → Legal
Interest Rate (%)** — see [eHealth settings](../configuration/reglages-ehealth.md).
This is a value **specific to your establishment / to the current year**.
:::

## Key points to remember

- The **acknowledgement (931000)** pays nothing; only the **settlement
  (920900)** tells you what is actually paid.
- Resthome **reconciles the settlement automatically**: lines allocated, batch
  status updated, remainder created for the rejections.
- Under **Account C**, a settlement with a real payment reference marks the
  batch **Paid** automatically (the payment date may stay empty).
- **Reconciling** a settlement (**Mark Reconciled**) means confirming the money
  received; the Cockpit gathers the **To reconcile** and the **OAs to chase**.
- **Late-payment interest** is only calculated after entering the **legal rate**
  in the eHealth settings.

## Further reading

- [Electronic billing (eFact)](efact.md)
- [eFact rejections — causes and solutions](efact-rejets.md)
- [Billing a month](../facturation/facturer-un-mois.md)
- [eHealth settings](../configuration/reglages-ehealth.md)
- [eHealth overview](index.md)
