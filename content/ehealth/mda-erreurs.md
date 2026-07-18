# MDA errors — causes and solutions

:::{rh-description}
Resolve MDA (insurability) errors and special cases in Resthome: incorrect NISS, unknown beneficiary, "not in order", no response, transfer, special schemes.
:::

:::{rh-faq}
What should I do when the MDA returns an error?
: Depending on the message: if the NISS is the cause (the most common), correct it on the record then Retry; if it is "no response" (often outside office hours), retry later; if the error is technical or persists, Report to the inter-mutualist.

What does "insured but not in order" mean?
: The resident is affiliated but their coverage is not valid for the period (unpaid contributions, file to be regularised). Do not bill the insurance organisation: clarify with the resident or their mutuality, and bill the share to the resident in the meantime.

Why did the MDA not find the resident?
: Either the NISS is entered incorrectly (format rejected), or it is correct but not yet known to the platform (very recent registration, special case). Check the NISS; if it is correct, contact the mutuality.

What does Resthome update after a successful MDA?
: The actual mutuality (insurance organisation), the BIM status, the affiliation number, the identity if fields were missing, and the date of death if the organisation reports it. For a special scheme, the profile's mutuality is not overwritten.
:::

The [MDA](mda.md) queries the mutualities platform (MyCareNet / WalCareNet) on
your behalf to confirm that a resident is **insured for the period** and to
identify **the mutuality that actually covers them**. It is the **prerequisite
for eFact**. This page gathers the errors and special cases, with the steps to
follow.

:::{admonition} The right habit
:class: tip

Run the MDA **at the start of the month, before generating the invoices**: you
avoid later [eFact rejections](efact-rejets.md) caused by a wrong mutuality or a
loss of insurability discovered too late.
:::

## MDA situations → action

Reminder of the statuses Resthome may display: **Draft · Sent / Pending ·
Success · Not insured · No response · Error**. Available actions: **Send · Check
the response · Retry · Contact the OA · Report to the inter-mutualist.**

| Situation | What Resthome displays | Likely cause | Action |
|---|---|---|---|
| **NISS not recognised** | **Error**: the request is refused before reaching a mutuality | The **NISS** is entered incorrectly (transposed digit, typo): invalid format | Check the NISS (ID card), **correct it**, then **Retry**. This is the most common cause. |
| **Beneficiary not found** | **Error**: "not found" | Well-formed NISS but **not (yet) known** to the platform (very recent registration, special case) | Confirm the NISS and the affiliation. If the number is correct: **Contact the OA**; as a last resort **Report to the inter-mutualist.** |
| **Insured but "not in order"** | **Not insured** + **alert** | Existing affiliation but **invalid coverage** (unpaid contributions, file to be regularised) | Do not bill the OA for this period. **Contact the OA** or the resident to regularise; bill the share **to the resident** in the meantime. |
| **No mutuality on the record** | Non-blocking: after a successful MDA, the mutuality is **filled in automatically** | Incomplete profile (new resident) | Run the MDA: if it succeeds, Resthome **fills in** the mutuality and the affiliation number. Otherwise, re-check the NISS. |
| **Change of mutuality (transfer)** | **Transfer detected**: the profile is **updated** | The resident has changed mutuality; the profile was out of date | Let Resthome correct the profile; **check** the new mutuality before billing. |
| **"No response"** | **No response** | The platform closed the request without a response — often **outside office hours** (evening/weekend) or a temporary unavailability. This is not a mistake on your part | **Retry** during business hours. If it persists, **Report to the inter-mutualist.** |
| **Technical error** | **Error** + technical detail | Temporary outage on the platform or mutuality side | **Retry** later; if the error recurs, **Report to the inter-mutualist.** Do not retry in a loop. |
| **Death reported by the mutuality** | **Date of death** on the record + alert | The OA reports a death (coverage closed) | Check and **stop billing** at the correct date. |
| **Special scheme** | The MDA response is **ignored**; the profile's mutuality **stays unchanged** | The resident falls under a special scheme (see below) | Do not correct anything: the safeguard is **intentional**. Bill according to the special scheme. |

## Special schemes

Some residents do **not** fall under the standard mutuality flow. In these
cases, Resthome **does not overwrite** the mutuality on their profile with the
MDA response, and billing is often done **on paper**, addressed to the actual
payer (or to the resident), rather than through eFact.

- **BIM status (increased reimbursement)** — this is not a separate scheme: the
  MDA **retrieves and updates it on its own**. It grants the resident a
  **reduced co-payment** (the share they pay decreases); the daily allowance,
  however, is unchanged.
- **War invalids / civilian victims** — the resident has **two coverages**:
  their standard mutuality (visible in the MDA) **and** a specific coverage that
  **does not go through** the MDA. The safeguard avoids overwriting this
  configuration.
- **Retirees of international institutions** — covered by a scheme specific to
  their organisation, not by a standard Belgian mutuality.
- **Foreign pensioners** — coverage from a foreign scheme via the European
  coordination forms; in practice, many still join a Belgian mutuality.

:::{admonition} When in doubt
:class: warning

For a special scheme, if in doubt about which organisation to bill, get in touch
with the mutuality or the organisation concerned before issuing the invoice.
:::

## Best practices

- **MDA at the start of the month, before billing.**
- **Individual check** (immediate) for a specific resident; **batch check** for
  a whole period — paste a column of names/NISS if needed.
    - **Immediate send (Sync)** for **small volumes**;
    - **Grouped send (Async)** for **large monthly batches**: the request goes
      out, then you **retrieve the responses** a little later with **Check
      responses** (requires at least 2 residents).
- The batch displays **counters** (Insured, Not insured, Errors, Pending,
  Deaths) to spot at a glance what remains to process.
- **What Resthome updates** after a successful MDA: the actual **mutuality
  (OA)**, the **BIM status**, the **affiliation number**, the **identity** if
  fields were missing, and the **date of death** if the organisation reports it.
  Exception: the mutuality of a **special scheme** is not overwritten.

## Further reading

- [Insurability (MDA)](mda.md)
- [eFact rejections](efact-rejets.md) · [Electronic invoicing (eFact)](efact.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
