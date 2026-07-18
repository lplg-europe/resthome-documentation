# Agreements (eAgreement)

:::{rh-description}
eAgreement and eAgreement Light in Resthome (nursing home MR/MRS) — make an agreement request, notify the mutuality on admission, in case of absence, on departure and on return (Annexes 7, 10, 11).
:::

:::{rh-faq}
How do I make an agreement request (eAgreement) in Resthome?
: In most cases you don't have to create it by hand: Resthome automatically prepares the notification matching your business action — start a stay (admission agreement, Annexe 7), validate a Katz aggravation (care agreement update, Annexe 10), record an absence or a departure (departure notification, Annexe 11). Check that the resident has a valid NISS and mutuality and that the eHealth certificate is active, then send. You then follow the status: Draft → Sent → Accepted or Rejected.

Where do I see the status of an agreement or a request in Resthome?
: From the resident record or the billing period: you see the list of agreements and their status (Draft, Sent, Accepted, Rejected), with a link to the detail.

What is the difference between eAgreement and eAgreement Light?
: eAgreement is the care coverage agreement, linked to the Katz category and the allowance. eAgreement Light groups the simpler notifications related to the resident's movements (admission, absence, departure, return), which Resthome generates automatically as you go.

What should I do if an agreement request is rejected?
: Resthome displays the rejection reason in plain language (French and Dutch) directly on the agreement. Fix the cause — most often the NISS, the mutuality or the dates — then resend.
:::

When a resident is admitted, is absent, returns or leaves the facility, the
**mutuality (insurance organisation)** must be informed electronically. Resthome
takes care of it: at the right moment, it **automatically prepares** the eHealth
notification matching your action. Most of the time you have **nothing extra to
enter** — just to check and, if needed, to send.

:::{admonition} Two related concepts
:class: note

- **eAgreement**: the care coverage agreement (linked to the **Katz** category
  and the allowance).
- **eAgreement Light**: the simpler notifications related to the resident's
  **movements** — admission, absence, departure, return. These are the ones
  Resthome generates on its own as you go.
:::

## When does Resthome create an agreement?

You perform the usual business action; Resthome deduces the notification.

| Your action in Resthome | Notification prepared | Document |
|---|---|---|
| **Start a stay** (admission) | Admission agreement | Annexe 7 |
| **Record an absence** / hospitalisation | Departure notification | Annexe 11 |
| **Return** of the resident (end of absence) | Readmission | Annexe 7 |
| **Katz aggravation** validated | Care agreement update | Annexe 10 |
| **End of stay / death** | Departure notification | Annexe 11 |

:::{admonition} The principle, in one sentence
:class: tip

You manage the **resident** (admission, absence, return, departure); Resthome
manages the **eHealth** behind the scenes. The billing and agreement operations
you see appear are the automatic reflection of what you have just done.
:::

## What you need before sending

:::{admonition} To check
:class: warning

- The resident has a valid **NISS** (national number).
- Their **mutuality** is filled in.
- The facility's **eHealth certificate** is active.

Without a NISS, the agreement cannot be transmitted. You can still record the
movement (admission, absence…): Resthome notes it and invites you to complete
the NISS as soon as possible.
:::

## Following an agreement

Each agreement goes through clear **statuses**:

1. **Draft** — prepared by Resthome, not yet sent.
2. **Sent** — transmitted to the mutuality via eHealth.
3. **Accepted** — the mutuality has given its agreement.
4. **Rejected** — the mutuality refuses, with a **reason**.

From the resident record or the billing period, you see the list of agreements
and their status, with a link to the detail.

### In case of rejection

If the mutuality rejects a request, Resthome displays the **rejection reason in
plain language, in French and Dutch**, directly on the agreement. You immediately
know what to fix (often: NISS, mutuality, or dates) before resending.

## Useful special cases

- **Short absence**: an absence of more than **72 h** (or any
  **hospitalisation**) triggers the departure **Annexe 11**; the **return**
  generates the readmission **Annexe 7**. See [Absences and
  hospitalisations](../facturation/absences.md).
- **Billing already closed**: if the invoice of the month concerned is **already
  posted** for this resident, Resthome **does not recreate** a duplicate
  agreement for this month — it protects consistency. Reset the invoice to draft
  (or issue a credit note) if you really must modify this month, then refresh.
- **Readmission after a long leave**: depending on the duration, the readmission
  may require a **new Katz evaluation** — Resthome flags it for you.

## Going further

- [Refused agreement (eAgreement) — causes and solutions](eagreement-refus.md)
- [Absences and hospitalisations](../facturation/absences.md)
- [Departure and death](../facturation/depart-deces.md)
- [eHealth overview](index.md)
