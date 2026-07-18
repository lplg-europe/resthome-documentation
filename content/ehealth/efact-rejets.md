# eFact rejections — causes and solutions

:::{rh-description}
Why a nursing home eFact invoice is rejected by the mutuality and how to fix it in Resthome: insurability, allowance, dates, duplicate, resend.
:::

:::{rh-faq}
Why is an eFact invoice rejected?
: Most often: invalid insurability (MDA), the wrong mutuality on the record, an allowance declared beyond the end of the INAMI intervention, an unclosed absence, a missing Katz category, an incorrect NISS or a duplicate sending. The rejection code and reason returned by the insurance organisation indicate the cause.

What should you do when an eFact batch is rejected?
: You do not resend a batch as-is: you fix the cause at the source (MDA, mutuality, Katz, dates…), regenerate, then resend. The Resends counter tracks retransmissions to avoid duplicates.

What is the difference between a global rejection and a partial rejection?
: A partial rejection refuses only some lines (the rest is paid): you fix and resend only those lines. A global rejection refuses the whole batch: you fix the cause and resend a new batch.

How do I correct an over-invoicing (departure, death, over-declared allowance)?
: Resthome detects it through the self-check and prepares a credit note on the resident side and, if the mutuality share is affected, a corrective batch to the insurance organisation. The credit lines are included in the next sending.
:::

When you send the [eFact](efact.md), the **insurance organisation (OA)** checks
each line and returns a result to you. This page explains **how to read a
response**, **why a batch or a line is rejected**, and **how to fix it, then
resend**.

:::{admonition} Two lines of defence
:class: info

Most rejection causes are **intercepted by Resthome before sending** (period
self-check, checks at generation). They then appear as an **anomaly message**
to handle, not as a rejection. The cases that slip through anyway then come
back as an **OA rejection**. This page covers both.
:::

## The response cycle, in plain terms

After a batch is sent, the OA's responses advance the **batch status** and fill
in the **amounts** (invoiced / accepted / refused):

1. **Acknowledgement of receipt** — the OA confirms having received the file
   and passed the first check. Nothing to do.
2. **OA settlement** — the OA returns the result **line by line**: what is
   **accepted** and what is **refused**. Resthome reconciles this settlement and
   updates the batch amounts.
3. **Acceptance and/or rejection** — three possible outcomes:
    - **everything is accepted** → the batch is settled, then can be closed;
    - **partial rejection** — some lines are refused, the rest is paid: you fix
      and resend **only** the refused lines;
    - **global rejection** — the whole batch is refused, nothing is paid: you
      fix the cause and **resend a new batch**.

:::{admonition} When is a batch rejected globally?
:class: note

The insurance organisation rejects the **whole batch** (920099) in case of a
**blocking error** or when the **error rate exceeds about 5%** of the lines.
Below that, the faulty lines are subject to a **partial rejection** and the
rest is paid — which is why it pays to handle the self-check and the MDA
**before** sending.
:::

On each refused line, a **code** and a **rejection reason** in plain language
point to the cause.

## Frequent rejection causes → action

| Cause | What you see | Action in Resthome |
|---|---|---|
| **Invalid or missing insurability (MDA)** | The **MDA** counter is not green; batch held back at sending; or an OA rejection for insurability | Run **Check MDA**, get the **Success** status for each resident, then **regenerate** the eFact. The MDA must be validated **before** generating. |
| **Wrong or missing mutuality** | The allowance goes to the wrong OA (rejection) or does not appear in the batch | Enter/correct the **mutuality** on the resident's record, then **regenerate**. Check that each resident invoiced under third-party payment does have a mutuality. |
| **Allowance declared beyond the end of the intervention** | Self-check: **"Over-declared OA allowance"**; the OA refuses the extra days | Issue a **credit note / remainder** for the over-declared days (see below). |
| **Room freed / death — accommodation still invoiced** | Self-check: **over-invoicing**; refusal of the undue days | **Close the accommodation** on the correct date + **credit note**. |
| **Unclosed absence** | The **Absences** counter is active; allowance days are distorted | Close the period's absences, then re-check. |
| **Missing Katz category or expired evaluation** | The **"Katz to do"** counter; blocked at generation | Complete or renew the **Katz evaluation**, then **regenerate**. |
| **Missing or incorrect NISS** | Mandatory identification data → technical rejection | Correct the **NISS** on the resident's record, then regenerate. |
| **Duplicate sending** | The OA reports an **already received sending** | Do not resend an **already accepted** batch. For a legitimate resend, rely on the **Resends** counter (anti-duplicate). |
| **Amount / rate mismatch** | The OA returns an **unexpected amount/rate** | Check the applied **rate** and the line amount, correct the configuration, regenerate, resend. |
| **Technical / format rejection** | **Global rejection**: the file did not pass the format check | Rare case to escalate: use **Contact OA** or **Helpdesk**, fix, then resend a new batch. |

## Fix, then resend

The principle: **you do not resend a rejected batch as-is — you fix the cause
at the source, then resend.**

- **Fix → resend loop.** After handling the cause (MDA, mutuality, Katz,
  absence, dates…), regenerate the affected part and resend. The **Resends**
  counter keeps track of each retransmission to **avoid sending the same batch
  twice**.
- **Reintegration.** The **Reintegration** button lets you reintegrate lines
  (for example rejected lines, once corrected) into a **new sending**, rather
  than redoing everything.
- **Credit note / corrective batch.** Whenever you have **invoiced more than
  due** — a departure or death during an already invoiced month, an
  over-declared allowance — Resthome prepares a **credit note** (on the resident
  side) and, if the mutuality share is affected, a **corrective batch** to the
  OA. The credit lines are included in the **next eFact sending**.

## The responses you may come across

Depending on the message returned by the OA, you may see, in the statuses or
the batch log:

| Response | What it means |
|---|---|
| **Acknowledgement of receipt** | The OA has **received** the file and it passed the first check. Normal step. |
| **Notification with warnings** | The batch is **accepted**, but with **warnings** (minor errors) to read. |
| **Settlement** | The **line-by-line result**: **accepted** and **refused** amounts. This is where the partial rejections to fix appear. |
| **Global rejection** | The **whole batch is refused** (too many errors). Fix the cause and **resend a new batch**. |
| **Technical rejection** | The file did not pass the **format check**; retransmission required after correction. |

## Key points

- **Prevent rather than cure**: handle the **self-check** messages and validate
  the **MDA** before invoicing — this way, most rejections are avoided.
- A **partial rejection** is fixed **line by line**; a **global rejection** is
  **resent as a new batch**.
- An **over-invoicing** (departure, death, over-declared allowance) is corrected
  with a **credit note / corrective batch**, not with a simple resend.

## Further reading

- [Electronic invoicing (eFact)](efact.md)
- [Insurability (MDA)](mda.md) · [MDA errors](mda-erreurs.md)
- [Departure and death](../facturation/depart-deces.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
