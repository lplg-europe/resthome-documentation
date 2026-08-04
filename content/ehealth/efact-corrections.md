---
howto_auto: true
---

# Correcting an already-settled sending

:::{rh-description}
How to correct an eFact sending the insurer has already settled: credit notes for what was over-billed, and remainders to re-bill a rejected line after fixing it.
:::

:::{rh-faq}
How do I cancel an allowance already paid by the insurer?
: Create a credit note from the settled batch. Resthome builds a dedicated correction sending that references the original invoice — you do not simply put a negative line in next month's file.

Can I credit only one service instead of the whole invoice?
: Yes. The credit-note assistant lists every service in the sending, all ticked by default. Untick the correct ones to credit only the incorrect service.

A line was rejected but the amount was simply wrong — do I resend everything?
: No. Use "Correct & re-bill" on the rejected line: enter the right amount and Resthome adds it to a remainder that re-introduces only that line, referencing the original invoice.

What is the difference between a credit note and a remainder?
: A credit note **takes back** something already accepted and paid. A remainder **re-introduces** something the insurer refused, after you fixed the cause. Opposite directions, different regulatory codes.
:::

Once a sending is **settled**, it is history: you never edit it. Two instruments
exist to correct it afterwards, and picking the right one matters — the insurer
reads them differently.

| Instrument | Use it when | Direction |
|---|---|---|
| **Credit note** | The insurer **accepted and paid** something that should not have been billed. | Takes money back |
| **Remainder** | The insurer **refused** a line, and you have fixed the cause. | Re-bills what was refused |

## Credit note — taking back what was over-billed

Typical cases: a resident died or left mid-month and the allowance was billed to
the end; a category was billed higher than the one finally agreed.

From a **settled** or **closed** batch, click **Create credit note**. An
assistant lists every service in the sending, **all ticked by default**.

- Leave everything ticked to credit the **whole** invoice.
- Untick the correct services to credit **only** the incorrect one.

Confirm: Resthome creates a **dedicated correction sending**, a first-class
batch of its own, visible in the eFact list with its own message. It carries the
regulatory markers of a credit note and **back-references the original invoice**,
so the insurer can match it to what it paid.

:::{admonition} Never a negative line in next month's file
:class: warning

A credit note is **not** a negative line slipped into the next monthly sending.
That form carries no reference to the original invoice and does not comply with
the INAMI instructions — the insurer cannot tell what is being taken back. Always
go through **Create credit note** from the batch concerned.
:::

:::{admonition} Only from a settled sending
:class: note

The button is offered only on **settled** or **closed** batches. Before that
there is nothing to credit: a sending still awaiting its settlement is corrected
by fixing the period and regenerating.
:::

## Remainder — re-billing a line the insurer refused

When a settlement refuses part of a sending, the rest is paid and only the
refused lines need attention. On a rejected line, **Correct & re-bill** opens an
assistant showing:

- the amount **originally billed**;
- the insurer's **rejection** — code and reason, as returned;
- the **corrected amount** to re-bill, pre-filled with the original.

Enter the right amount, add a short note on what you corrected, and confirm.

Resthome then:

- **leaves the original line rejected** — that is the insurer's own follow-up
  status and it must not be rewritten;
- adds the corrected amount to a **remainder** sending, which re-introduces the
  line with a back-reference to the original invoice.

The remainder is an ordinary batch: generate its message, run the [pre-send
checks](efact.md) and send it like any other.

:::{admonition} Correct the cause first, the amount second
:class: important

Re-billing the same line with a different amount does not fix a rejection whose
cause was insurability, dates or category. Read the reject reason: if it points
at the resident's file, fix that first — otherwise the remainder comes back
refused too.
:::

## Further reading

- [Rejections and how to fix them](efact-rejets.md) — reading a settlement, reject codes.
- [Settlements and payments](efact-paiements.md) — what the insurer actually paid.
- [Electronic invoicing (eFact)](efact.md) — the full cycle.
- [Departure and death](../facturation/depart-deces.md) — the most common cause of an over-billed allowance.
