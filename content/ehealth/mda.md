# Insurability (MDA)

:::{rh-description}
Check a nursing home resident's insurability via MDA (MyCareNet) in Resthome — health insurance fund, BIM status, individual or batch check.
:::

:::{rh-faq}
How do I check a resident's insurability (MDA)?
: From the resident's record or a billing period, run Check MDA. Resthome queries MyCareNet/WalCareNet and confirms coverage, as an individual check (immediate) or as a batch for a whole period.

What does Resthome update after a successful MDA?
: The actual health insurance fund (insurer), the BIM status, the membership number, identity details if fields were missing, and the date of death if the insurer reports it.

What should I do if a resident isn't insured?
: Don't bill them under third-party payer (tiers payant) for the period, or the invoice will be rejected. Clarify the situation with the resident or their health insurance fund, and bill the amount to the resident in the meantime.
:::

Before billing, you must make sure the resident's **insurability is in order** and
know their exact **health insurance fund**. The **MDA** queries **MyCareNet /
WalCareNet** for you and retrieves up-to-date information for a given
**period**. It's the essential prerequisite before sending
[eFact](efact.md).

Menu: **eHealth → Insurability → MDA Requests** (and **MDA Batches**).

## What the MDA retrieves

- **Insured or not** for the period.
- The **health insurance fund (OA)** that actually responded — compared with the
  one on the profile (a **change** of health insurance fund is detected and flagged).
- The **BIM status** (increased reimbursement).
- The **coverage periods** (start/end dates; several sub-periods if the insurance
  changed during the interval).
- The **membership number** with the health insurance fund.
- Where applicable: **third-party payer (tiers payant)**, **date of death** reported
  by the OA, and depending on the request, the **reference pharmacy**, the **DMG**,
  the **palliative status**, or a **hospitalization**.

:::{admonition} The "not in order" case
:class: warning

If the beneficiary codes come back as zero (insured but unpaid contributions /
a problematic file), Resthome shows an **alert**: the resident is affiliated but
**not in order**. Clarify this with them or their health insurance fund before
billing the OA.
:::

## Prerequisites

:::{admonition} To check
:class: warning

- The resident has a valid **NISS**.
- The facility's **INAMI number** is configured.
- The **eHealth certificate** is active.

The **profile's health insurance fund** isn't blocking (the actual OA is
identified by the response), but filling it in helps spot changes.
:::

Resthome also applies automatic period rules: the end must be after the start, at
most **5 years** of history, and a standard MDA doesn't go beyond the current month.

## Individual check

1. Create an **MDA request** (resident, NISS pre-filled, period = the current
   month by default).
2. Click **Send (Sync)**: sending is **immediate** and the response comes back
   right away.
3. Review the summary and the insurability periods.

:::{admonition} One MDA per resident and per period
:class: note

Running a check again for the same resident and the same period **reuses** the
existing request — no duplicate.
:::

## Batch check (recommended at the start of the month)

For a whole period, run the **batch** check: select the residents (you can
**paste a column** of names/NISS), the period, and send the whole batch at once.

- **Immediate send (Sync)**: for small volumes.
- **Grouped send (Async)**: for **large monthly batches** — the request goes out,
  and the response is retrieved a bit later with **Check responses** (requires at
  least 2 residents).

The batch shows **counters**: Insured, Not insured, Errors, Pending, and
"Deaths detected".

:::{admonition} The right habit
:class: tip

Run the MDA **at the start of the month**, before generating invoices: you avoid
later eFact rejections caused by a wrong health insurance fund or a loss of
insurability.
:::

## Statuses

| Status | Meaning |
|---|---|
| **Draft** | Not yet sent |
| **Sent / Pending** | Transmitted, response awaited (especially when grouped) |
| **Success** | Response received, resident insured |
| **Not insured** | Response OK, but resident not covered |
| **No response** | The platform closed without a response from an OA (retry) |
| **Error** | The OA or the platform returned an error |

## Buttons

| Button | Effect |
|---|---|
| **Send (Sync)** | Immediate send, response right away |
| **Check response** | Retrieves a response from a grouped send |
| **Retry** | Resets to draft to resend |
| **Contact the OA** | Opens a pre-filled email to the health insurance fund that responded |
| **Report to InterMut** | Opens an email to the CIN for platform blockages |

On a batch, the same actions exist in grouped form (**Send**, **Check responses**,
**Retry errors**, **Retry no-responses**).

## What Resthome updates automatically

After a successful response, the resident record is **corrected automatically**:

- **Health insurance fund (OA)**: if the OA that responds differs from the profile,
  the profile is updated (and the OA created if it was missing).
- **BIM status**, **membership number**, and **identity** (name, date of birth,
  sex) if fields were missing.
- **Date of death** if the OA reports it → alert on the record.

:::{admonition} Safeguard for special schemes
:class: warning

For residents under a **special scheme** (INIG, EEC, Fedasil, foreign, private…),
Resthome **does not overwrite** the profile's health insurance fund: a message
explains that the MDA response was ignored so as not to break a non-standard
coverage.
:::

## Reinstatement (loss then return of insurability)

Resthome compares with the previous check:

- **Not insured → insured**: a notification appears on the period, and the
  **Reinstatement** action lets you move the lines that had been billed to the
  resident over to the OA.
- **Insured → not insured**: Resthome flags that the resident is "no longer in
  order" — their dependency fee (forfait) is excluded from OA billing for the
  period and billed to the resident until they are reinstated.

## Error handling

| Situation | What to do |
|---|---|
| **No response** (platform) | **Retry no-responses**; if it persists, **Report to InterMut** |
| **OA rejection** | **Contact the OA** (reason shown) |
| **Technical error** | **Report to InterMut** |
| **Resident with no health insurance fund** | Non-blocking: the actual OA comes from the response |
| **Pending (grouped)** | **Check responses** or wait |

## Learn more

- [MDA errors — causes and solutions](mda-erreurs.md)
- [Electronic billing (eFact)](efact.md)
- [Agreements (eAgreement)](eagreement.md)
- [Billing overview](../facturation/index.md)
