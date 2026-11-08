---
modules: [resthome_day_care_ehealth]
sectors: [csj]
---

# The day care agreement

:::{rh-description}
The agreement of a day care user (CSJ) in WideCare: the admission request and its prefilled Annexe 14, the insurer's answer, the yearly renewal and the end of care.
:::

:::{rh-faq}
When is the agreement requested?
: When the stay starts, WideCare prepares the admission request. Send it within 14 days of the admission, with its Annexe 14 and the Katz scale.

What if the health insurer does not answer?
: After 15 days of silence, the request is approved: it is recorded as a tacit agreement. A letter that arrives later replaces it.

How long does a day care agreement run?
: One year from its start, unless the insurer wrote another end date. It is then renewed with a new request.

What happens when the insurer refuses?
: The days covered by the refusal earn no forfait: the month bills the day price only, and the forfait is never claimed for them.

Do I sign the end-of-care notification?
: No. There is no official form for it: WideCare prints the centre's own notification, and the eHealth certificate stands for its signature.
:::

A day care centre is paid its forfait only for a user the health insurer has
agreed to. The agreement is asked with a request of its own, **csj-in**, and
its **Annexe 14**; the end of care is declared with a **csj-out**. Both follow
the same steps as the rest home's requests: see
[Agreements (eAgreement)](../ehealth/eagreement.md).

The requests are listed under **eHealth → eAgreement → eAgreement Light**, with
the filters **Day care centre — admission**, **Day care centre — end of care**
and **Day care renewal due**.

## Prerequisites

- The user's stay is a **CSJ** stay, started, under the centre's own INAMI
  number.
- The Katz evaluation is validated and gives a CSJ category: **F**, **Fp**,
  **Fd** or **D**. A scale that meets none of them asks nothing of the
  insurer — no forfait is due.
- The evaluation was completed and signed by a **nurse** or a **physician**,
  as recorded on their employee file.
- For a **D**: the date of the diagnostic assessment and the specialist who
  made it are on the evaluation.

## Send the admission request

Starting the stay prepares the admission request. Send it **within 14 days**
of the admission: a late request takes effect on the day it is filed, not on
the admission.

1. Open the request, from the user's file or from the eAgreement list.
2. Click **Generate prefilled Annexe 14**: the official form is filled in with
   the centre and its approval, the insurer, the user, the day and hour they
   came in, the category asked for, and first request or renewal.
3. Click **Sign Annexe 14** to sign it in the app — or print it, have it signed
   on paper and load the signed version under **Annexe 2**.
4. Send the request.

<!-- screenshot to add: a csj-in request with the Generate prefilled Annexe 14 and Sign Annexe 14 buttons and the "Annexe 14 to attach" note -->

Before it leaves, the request is checked: a category D without its
diagnostic assessment, an evaluator who is not a nurse or a physician, or a
scale with no day care category each stop the sending and say what to
correct.

## The insurer's answer

The insurer answers on paper, with an **Annexe 15** (grant) or an
**Annexe 16** (refusal). Record its decision on the request, as for any
agreement. See [Following up an agreement](../ehealth/eagreement-suivi.md).

- **Granted**: the request records the category granted — F, Fp, Fd or D —
  and the agreement start.
- **Silent for 15 days**: the request is approved, recorded as a **tacit
  agreement**. A decision that arrives later replaces it.
- **Refused**: no forfait is due on the days the refusal covers, until a new
  request is granted. The month still bills the user's day price.

A day care agreement belongs to the insurer that received it: when the user
changes insurer, a new request is needed.

## Renew the agreement every year

A day care agreement runs for **one year** from its start, unless the insurer
wrote another end. **Covered Until** on the request gives that last day.

- From 30 days before that date, a banner on the agreement says
  **A day care agreement is renewed every year**, with the date, and an
  activity **Renew the day care agreement (Annexe 14)** is scheduled for
  whoever made the request.
- The **Billing** dashboard counts the **Day care agreements to renew** on the
  day care card, in red once one is overdue.

To renew it:

1. Click **Prepare the renewal** on the agreement: it opens a new admission
   request for the same user, marked as a renewal. It is created only once.
2. Generate and sign its Annexe 14, which now says « renewal », with a current
   Katz scale.
3. Send it before the end date.

The 14-day rule of the first request does not apply to a renewal.

:::{warning}
A forfait billed past the end of the agreement is flagged before the eFact
sending: a warning while a renewal awaits the insurer, a blocking problem
when none was sent. Prepare the renewal and send it, or hold these days until
it is granted.
:::

## Declare the end of care

When the user stops coming — the stay ends, or the user dies — WideCare
prepares the end-of-care request, **csj-out**.

1. Open it, and click **Generate the end-of-care notification**: the centre's
   own notice says who, since when, until when, and why.
2. Send the request. No signature is expected: the eHealth certificate stands
   for it.

An end of care closes the agreement. A user who comes back later is admitted
again with a **new** request.

## A respite in the rest home

In a house that also runs a rest home, a short stay in a bed between two
periods at the day care is a **respite**: the agreement runs on, nothing is
notified on the way out, and no new request is filed on the way back while
the agreement still covers the user. See
[Admitting a day care user](admission.md).

## What's next

- [Billing a day care month](facturation.md) — what the agreement allows the month to claim.
- [Electronic invoicing (eFact)](../ehealth/efact.md) — sending the forfaits under the centre's number.
