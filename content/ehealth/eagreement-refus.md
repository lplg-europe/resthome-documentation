# Refused agreement (eAgreement) — causes and solutions

:::{rh-description}
Why an eAgreement notification is refused by the health insurer and how to fix it in Resthome: NISS, insurability, document, Katz, duplicate, then resend.
:::

:::{rh-faq}
What should you do when an eAgreement is refused?
: Read the rejection reason (shown in plain language, FR and NL, on the agreement), fix the cause at the source (NISS, health insurer, MDA insurability, Katz assessment, PDF document or the right business action), then resend the agreement.

Does an acknowledgement of receipt mean the agreement is accepted?
: No. An electronic acknowledgement only confirms that the health insurer received the notification. For eAgreement Light, the substantive decision (acceptance or refusal on the merits) usually comes back by post.

Why is my agreement refused immediately?
: An immediate rejection comes from a blocking data issue: NISS not recognised or malformed, unknown health insurer, missing document or wrong format, missing Katz assessment, unrecognised facility, or duplicate.

What is a tacit agreement?
: If the health insurer does not respond within the regulatory deadline, the agreement is deemed accepted (silence = granted). The acknowledgement of receipt is not enough: it is the absence of refusal within the deadline that counts as agreement.
:::

When a resident **is admitted**, **goes on leave**, **returns** or **leaves** the facility,
Resthome automatically notifies their **health insurer (insurance organisation, OA)**
electronically, with the right official document (Annexe 7, 10 or 11). This service —
**[eAgreement](eagreement.md) Light** — is **accredited** (operational). The health insurer
can then **accept** the agreement, let it become **tacit**, or **refuse** it.

This page explains **why an agreement is refused** and **how to fix it and resend it**.

## Two points where things get stuck

:::{admonition} To distinguish
:class: info

- **Immediate technical rejection** — a piece of data is off (NISS, document, required field)
  and the health insurer or the platform returns an error **right away**. This is what the
  table below covers: it can be **fixed and resent**.
- **Substantive decision from the health insurer** — for eAgreement Light, the **actual answer**
  (acceptance or refusal on the merits, e.g. the Katz category) usually arrives **by post**,
  not electronically.
:::

:::{admonition} An acknowledgement of receipt is not an agreement
:class: warning

An electronic "received" acknowledgement means **received**, **not accepted**. Do not treat
an agreement as granted on the basis of the acknowledgement alone.
:::

## Common refusal causes → action

| Cause | What you see | Action in Resthome |
|---|---|---|
| **NISS not recognised** | Rejection "unknown beneficiary"; the agreement goes back to *Rejected* | Check the NISS (identity card / eID), correct it, resend. |
| **Malformed / incomplete NISS** | Rejection "invalid identifier" (format) | Re-enter the 11 digits of the NISS, resend. |
| **Unknown health insurer number** | Rejection "unknown health insurance fund number" | Check the health insurer and the membership number; prefer identification by NISS; resend. |
| **Insurability (MDA) not confirmed** | Resthome **blocks the send**: insurability not in order | Re-run / update the [MDA check](mda.md), correct health insurer/NISS, try again. *(Discharge/death notifications are not blocked by this check.)* |
| **Incomplete resident data** | Rejection "mandatory data missing" (name, identifier) | Complete the resident record, resend. |
| **Document (annexe) missing or wrong format** | Send blocked if the annexe is empty; otherwise rejection "invalid document format" | Regenerate / attach the Annexe **as a PDF**, check that it opens, resend. |
| **Attachment too large** | The send does not go through | Shrink the PDF (reduce the scan size), resend. |
| **Katz assessment missing or not validated** | Send blocked: "Katz assessment required" | Create, **confirm** then **validate** the Katz; check Annexe 10; resend. |
| **Duplicate agreement** | Rejection "record already exists" | Do not resend an agreement that has already been transmitted; correct the faulty data (Resthome then regenerates a new notification). |
| **Wrong annexe / unsuitable type** | Rejection "agreement type not allowed / inconsistent" | Redo the **correct business action** (admission ≠ leave ≠ discharge): **one situation = one annexe**. |
| **Facility or caregiver not recognised** | Rejection "unknown organisation / provider" | Have the administrator check the eHealth configuration (facility / caregiver INAMI number), resend. |

## Fix, then resend

1. **Read the reason.** In case of rejection, Resthome shows the **reason in plain language, in
   French and Dutch**, directly on the agreement.
2. **Check what was actually sent.** When the rejection concerns a **document**, the
   **Preview sent annexes** button opens the merged PDF **exactly as it was transmitted** to
   the health insurer — you see straight away whether an annex page is missing, blank or
   unreadable. See [Agreements (eAgreement)](eagreement.md).
3. **Fix the cause at the source** (resident record, health insurer/NISS, MDA, Katz assessment,
   PDF document, or the right business action).
4. **Resend the agreement** once the data is corrected.
5. **Acknowledgement of receipt.** It confirms **receipt**, not acceptance.
6. **Tacit agreement.** If the health insurer does not respond within the regulatory deadline,
   the agreement is **tacitly granted** (silence = accepted).

The visible statuses: **Draft → Sent → Accepted / Rejected**, with the reason shown in case of
rejection.

## Best practices (avoiding refusal)

- **MDA first** — check [insurability](mda.md) **before** preparing the agreement: it is the most
  frequent blocker, and it can be anticipated.
- **Complete resident record** — valid NISS (eID), health insurer filled in, correct identity,
  before any movement.
- **The right document, once** — one situation = one annexe (7 admission/return, 10 Katz,
  11 discharge/death). Do not resend an agreement that has already been transmitted.
- **Katz validated** before sending for admissions and aggravations.
- **Active eHealth certificate** and up-to-date facility configuration (INAMI number).
- **Let Resthome do the work** — manage the resident (admission, leave, return, discharge);
  Resthome derives the notification. Most often: check and send.

## Learn more

- [Agreements (eAgreement)](eagreement.md)
- [Insurability (MDA)](mda.md) · [MDA errors](mda-erreurs.md)
- [eFact rejections](efact-rejets.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
