---
howto_auto: true
---

# Following a request: deadlines and decision

:::{rh-description}
What happens after an eAgreement Light request is sent: the two acknowledgement levels, the 14-day legal deadline, the 15-day tacit agreement, and how to record the insurer's paper decision in Resthome.
:::

:::{rh-faq}
Does the insurer's decision come back electronically in eAgreement Light?
: No. Electronically you only ever receive an acknowledgement (TAck) or an electronic reject. The medical advisor's actual decision — acceptance or refusal — arrives **on paper**, and you record it in Resthome with the "Paper decision received" button.

What is the difference between "Sent" and "Decision pending"?
: "Sent" means the broker accepted the message: it is on its way, but you have no proof yet that the insurer received it. "Decision pending" means the legal acknowledgement came back — you now have proof of receipt, and you are waiting for the paper letter.

How long do I have to send an eAgreement request?
: 14 calendar days from the resident's admission. Resthome computes the deadline and flags the request when it approaches or passes. The send is never blocked — a late request can still be regularised on a later invoice.

What happens if the insurer never replies?
: After 15 days without a response, the agreement is considered **tacitly granted** under the applicable regulation. Resthome tracks the deadline and lets you record the outcome as "Tacit agreement" — with the same effect as an acceptance.

The status says "Rejected" — is that a refusal?
: No. "Rejected" is an **electronic** reject: the insurer's system refused the message itself (a structural or data problem), usually within 48 hours. A "Refused" is the medical advisor's decision, on paper. A reject is fixed and resent; a refusal is contested.
:::

Sending an [eAgreement request](eagreement.md) is not the end of the story. This
page covers everything that happens next: what comes back electronically, the
two regulatory deadlines to watch, and how to record the insurer's decision.

:::{admonition} The essential asymmetry
:class: important

In eAgreement Light, **only acknowledgements and rejects travel electronically**.
The medical advisor's decision — the one that grants or refuses the allowance —
arrives **by post**. Resthome cannot fetch it: you record it by hand, and the
software then does the rest.
:::

## The two acknowledgement levels

The request status follows what actually came back, which is why there are two
steps rather than one.

| Status | What it means | What you have |
|---|---|---|
| **Sent** | The broker accepted the message. | It is on its way. **No proof** the insurer received it. |
| **Decision pending** | The legal acknowledgement came back. | **Legal proof of receipt** by the insurer. |

The first acknowledgement is a **transport** receipt from the broker — useful,
but with no legal value. The second is the **legal** acknowledgement: signed
proof that the recipient received your message. It is the one that starts the
tacit-agreement clock.

The **Check Response** button, available from **Sent** onwards, asks the platform
whether anything new has arrived. There is no waiting period to respect on your
side: if you ask too often, the platform itself replies with a *"please wait"*
message that Resthome shows you plainly.

:::{admonition} If the acknowledgement comes back negative
:class: warning

A negative acknowledgement (**TAck KO**) means the message was **not** accepted.
A banner appears on the request with the reason returned. This is not a refusal
of the allowance — it is a transport failure: correct what is reported and send
again.
:::

## Deadline 1 — sending: 14 days from admission

Regulation gives the institution **14 calendar days from the resident's
admission** to transmit the request. Resthome computes the deadline from the
admission date and shows a status:

| Status | Meaning |
|---|---|
| **Deadline OK** | You are within the window. |
| **Send quickly** | Three days or fewer remain. |
| **Deadline exceeded** | The window has closed. |

:::{admonition} The send is never blocked
:class: note

Resthome **informs, it does not forbid**: an exceeded deadline still lets you
send. A late request can be refused for lateness by the insurer, but a
regularisation on a later invoice remains possible. Sending late beats not
sending.
:::

## Deadline 2 — the reply: tacit agreement at 15 days

Once the insurer has acknowledged receipt, they have **15 days** to answer.
Beyond that, the agreement is **tacitly granted** under the applicable regulation — silence is
worth acceptance.

Resthome counts from the legal acknowledgement date, falling back on the send
date when no acknowledgement was recorded, and shows where you stand:

| Status | Meaning |
|---|---|
| **Waiting** | The window is open, the insurer can still reply. |
| **Deadline expiring soon** | Three days or fewer remain. |
| **Deadline expired — tacit agreement obtained** | The 15 days have elapsed with no reply. |

A **daily reminder** flags the requests entering their last three days and those
that have passed the deadline, so a tacit agreement is never left hanging.

:::{admonition} A tacit agreement still has to be recorded
:class: warning

Passing the deadline does not close the request on its own. Record the outcome
as **Tacit agreement** (below) so the allowance is billed and the agreement
carries a start and end date. Left in *Decision pending*, it bills nothing.
:::

## Recording the insurer's decision

When the letter arrives — or when the tacit deadline passes — open the request
and click **Paper decision received**. The button is available from **Sent**
onwards.

Three outcomes:

### Acceptance

The insurer grants the allowance. Copy from the letter:

- the **agreement number** printed on it — it also serves as the reference in
  case of dispute;
- the **start** and **end** of the agreement;
- the **agreed category** — which may differ from the one you requested;
- the **CT1/CT2 entitlement code**: pick the pair from the list, the two codes
  always go together.

### Refusal

Record the **reason** as stated on the letter. It is required — a refusal
without a written reason cannot be contested later.

### Tacit agreement

The regulatory fallback when the 15 days elapsed with no reply. Same effect as an
acceptance; fill in the agreement dates and category as you requested them.

### Common to all three

Whatever the outcome, also record:

- the **decision date** written on the letter;
- the **medical advisor** who signed it. Pick from those already registered on
  the resident's insurer, or create one inline — it is filed under that insurer
  so you only type it once;
- the **scanned letter** itself, as proof.

:::{admonition} The agreed category is what gets billed
:class: important

The insurer may grant a category **lower** than the one you requested. What is
recorded here is what is billed — not what you asked for. If the gap is not
justified, contest it with the insurer rather than correcting it by hand.
:::

## Further reading

- [Agreements (eAgreement Light)](eagreement.md) — creating and sending a request.
- [Signing the annexes](eagreement-signature.md) — before sending.
- [Refusals and rejects](eagreement-refus.md) — what to do with a negative outcome.
- [The Katz assessment](../residents/katz.md) — the category that is requested.
