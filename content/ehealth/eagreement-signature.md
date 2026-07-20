# Responsible practitioner and annex signatures

:::{rh-description}
eAgreement responsible practitioner and signing Annexes 7/10/11 in the app for a nursing home (MR/MRS): NIHII resolution and rule-compliant signing without printing.
:::

:::{rh-faq}
Who is the responsible practitioner on an eAgreement request?
: It is the clinician who carried out the Katz assessment (the assessor), not the person who sends the request — a medical secretary can perfectly well submit it. Resthome records their personal NIHII on the request. If they have no NIHII, the request borrows the identity of the head nurse, then of the coordinating physician configured in the eHealth settings.

Where do I enter a caregiver's NIHII and signature?
: On their employee record (Employees app, Nursing Home tab). The NIHII, role and signature image live on the employee — not on a user account — so that caregivers who sign occasionally do not consume a user license.

How do I sign an Annexe 10, 7 or 11 without printing or scanning?
: Upload a signature image on the employee record, then, on the eAgreement request in Draft, click Sign Annexe 10 (or Sign Annexe 7 / Sign Annexe 11). Resthome places your signature on the PDF and marks it signed. If no image is configured, the old print / sign / scan route remains possible.

Who is allowed to sign an Annexe 10 (signature rules)?
: By default, a physician OR a nurse. A physician's signature becomes mandatory for a Katz category D (or Cd) and for a quick revision (a new assessment less than 6 months after the previous one). Annexes 7 and 11 are signed by the institution's manager, with no medical rule.

Can I sign on behalf of a colleague?
: No, unless you have eHealth manager rights. Everyone signs with their own signature image; signing on behalf of another clinician, whose name and role appear on a legal annex, requires eHealth manager rights. The actual author remains tracked in the log.

What happens for a foreign physician without a Belgian NIHII?
: Tick "Foreign physician (no Belgian NIHII)" on their employee record (visible only for a physician). Resthome then uses the generic number provided by the eHealth specification for foreign practitioners, accepted by the insurance bodies.
:::

An [eAgreement](eagreement.md) request must designate a **responsible
practitioner** and carry a **signature** on its annexes. This page explains the
two mechanisms Resthome puts in place:

- **Who is identified** as the responsible practitioner on the electronic request
  — and how their **NIHII** number is determined automatically;
- **How to sign** **Annexes 7, 10 and 11** directly in the application, from a
  stored **signature image**, instead of printing, signing and scanning.

The signing buttons appear on the **eAgreement request** (reachable from the
resident record or the billing period). Identities are configured on the
**employee record** and in the **eHealth settings**.

:::{admonition} Two identities not to confuse
:class: note

- **The responsible practitioner**: the **electronic** identity recorded in the
  request sent to the health insurer — the clinician who carried out the **Katz**
  assessment. Resthome **resolves it automatically** (see below).
- **The signer**: the person whose **signature image** is placed on the annex
  **PDF**. By default, this is **you** (the logged-in user).

In most cases these two roles coincide, but they are distinct: a secretary can
send a request whose responsible practitioner is the nurse who scored the Katz.
:::

## The responsible practitioner

The responsible practitioner is the **clinician who carried out the
[Katz](../residents/katz.md) assessment** — the assessor — **not** the person who
sends the request. Resthome determines their **NIHII** by walking down a fallback
chain, so that a consistent identity is always transmitted to the health insurer.

| Order | Resthome uses… | When |
|---|---|---|
| 1 | **The Katz assessor**, if they have a personal NIHII | Normal case |
| 2 | The configured **head nurse** (their NIHII) | The assessor (nurse, care assistant) has no NIHII |
| 3 | The configured **coordinating physician** (their NIHII) | Neither the assessor nor the head nurse has a NIHII |
| 4 | A **generic AViQ nurse number** | Last resort, no NIHII available |

:::{admonition} Katz category D: a physician is mandatory
:class: warning

For a Katz **category D** (or **Cd**), the specification requires a **physician**
as the responsible practitioner. Resthome then uses the assessor if they are a
physician (with a NIHII), otherwise the configured **coordinating physician**. If
no physician is available, sending is **blocked** with an explicit message:
configure a coordinating physician in the eHealth settings.
:::

:::{admonition} The generic number is a last resort
:class: info

If no one in the chain has a usable NIHII, Resthome falls back on the **generic
AViQ nurse number**. This is a safety net: for a correct identity, enter the
caregiver's personal NIHII, or at least a fallback head nurse and coordinating
physician.
:::

## Where identities are stored (employee record)

A caregiver's **NIHII**, **role** and **signature image** live on their **employee
record**, not on a user account. This way, a caregiver who signs an Annexe 10 from
time to time **does not consume a user license**: they only need to exist as an
employee.

**Employees app → employee record → Nursing Home tab.**

| Field | What it is for |
|---|---|
| **INAMI Number** (NIHII/INAMI number) | The caregiver's personal NIHII, used as the responsible practitioner on the eAgreement request. 11 digits. |
| **Care role** | The job (nurse, head nurse, care assistant, physician…). It determines the eHealth role. |
| **eHealth Role** | Derived automatically from the care role: *nurse* (nurse / head nurse / care assistant) or *physician* (physician). Read-only. |
| **Foreign physician (no Belgian NIHII)** | Tick this for a cross-border physician without a Belgian NIHII. Visible only for a physician. |
| **Signature image (Annexe 10)** | The signature scan (PNG/JPG, transparent background preferred), placed on the PDF when signing in the app. |

:::{admonition} A clean signature image
:class: tip

Prefer a **PNG image with a transparent background**, cropped to the strokes.
Resthome places it in the annex's "Signature" box while **preserving its
proportions** — a well-cropped image gives a clean result.
:::

## Configuring the fallback identities

**Settings > Nursing Home > eAgreement Responsible Practitioner.** These two
settings provide the fallback NIHII when the Katz assessor does not have their own.

| Setting | What it is for |
|---|---|
| **Head Nurse (NIHII fallback)** | Their NIHII identifies the responsible practitioner when the assessor (nurse, care assistant) has no personal NIHII. |
| **Coordinating Physician (NIHII fallback)** | Fallback when no nurse NIHII is available, and **mandatory** for a Katz category D. |

See also [eHealth and eFact settings](../configuration/reglages-ehealth.md).

:::{admonition} The Katz category is for declaring, not for setting the amount
:class: note

The **dependency fee** is the **same amount** for all Katz categories (AViQ
rates); the category serves to **declare the resident's profile** to the health
insurer. A **D** category does, however, require a **physician** as the
responsible practitioner — hence the importance of the fallback coordinating
physician.
:::

## The foreign physician

A **cross-border** physician who does **not** have a Belgian NIHII cannot provide
a personal number. On their employee record (*physician* role), tick **Foreign
physician (no Belgian NIHII)**. Resthome then records on the request the **generic
number provided by the eHealth specification** for foreign practitioners, which
the insurance bodies accept. You have no number to enter yourself.

## Signing an annex in the application

Rather than **printing, signing by hand and then scanning**, Resthome places your
**signature image** on the annex PDF and saves it — a route compliant with the
**applicable signature rules**. The annexes concerned:

- **Annexe 10** — the Katz scale (care agreement);
- **Annexe 7** — the admission agreement (admission / readmission);
- **Annexe 11** — the end-of-stay notification.

<!-- screenshot to add: eAgreement request in Draft with the Sign Annexe 10 / Sign Annexe 7 buttons in the action bar -->

The path, on a request in **Draft**:

1. **Generate the annex** if not already done (Annexe 10 is produced from the
   Katz; Annexe 7 or 11 from the request).
2. Click **Sign Annexe 10** (or **Sign Annexe 7** / **Sign Annexe 11**). These
   buttons appear only in Draft, when the annex exists and is **not yet signed**.
3. In the **Sign annex** window, check the **Signer** (you by default), their
   **role**, the **signature date** and the signature **preview**.
4. Click **Sign & replace PDF**. Resthome regenerates a clean PDF, places the
   signature on it and ticks the annex as **signed** (a green ✓ "Signed" appears
   next to the annex).

:::{admonition} Signing is a prerequisite for sending
:class: tip

As long as a generated annex is **not signed**, the **Send Request** button stays
hidden. Sign all the annexes first, then send. Re-signing is safe: Resthome starts
from a blank PDF each time, without stacking signatures.
:::

:::{admonition} Katz already signed during the assessment
:class: note

If the Katz assessment was **signed in the app** at scoring time, the Annexe 10
PDF already carries the signature: Resthome marks it **signed automatically** and
the step above is not needed.
:::

### Who can sign (signature rules)

| Situation | Allowed signer |
|---|---|
| Annexe 10 — standard case | **Physician OR nurse** |
| Annexe 10 — Katz **category D / Cd** | **Physician mandatory** (no nurse fallback) |
| Annexe 10 — **quick revision** (new Katz less than 6 months after the previous one) | **Physician mandatory** |
| Annexe 7 (admission) / Annexe 11 (end of stay) | **Institution manager** — no medical rule |

The signing window recalls the applicable rule in a **signature rules**
banner. If the rule requires a physician and the signer is not one, the signature
is refused with a clear message.

:::{admonition} Readmission after a long absence
:class: info

A **readmission** after more than 30 days of absence may require a **new Katz
assessment**, but it does **not** require a physician: the Annexe 10 can be signed
by a **physician OR a nurse**.
:::

### Everyone signs with their own signature

For safety, you can only sign **with your own** signature image. Signing **on
behalf of another** clinician — whose name and role appear on a legal annex
transmitted to the health insurer — requires **eHealth manager** rights. In all
cases, the **actual author** of the action remains recorded in the audit log.

### If no signature image is configured

If the signer has **no** signature image on their employee record, the window
warns you and the **Sign & replace PDF** button is not offered. Two options:

- **upload a signature image** on the employee record, then start again;
- **keep the manual route**: print the annex, have it signed, scan the signed
  document and re-upload it on the request (for Annexe 7 / 11, tick **Annex
  signed**).

## Key points to remember

- The **responsible practitioner** is the **Katz assessor**, not the sender;
  Resthome resolves their **NIHII** in a cascade: assessor → head nurse →
  coordinating physician → generic number.
- A Katz **category D** requires a **physician**; configure a fallback
  **coordinating physician** in the eHealth settings.
- The **NIHII**, **role** and **signature image** live on the **employee record**
  (*Nursing Home* tab) — no user license needed for caregivers who sign
  occasionally.
- **Sign Annexe 10 / 7 / 11** places your signature image on the PDF: no more
  printing / signing / scanning. Signing is a **prerequisite for sending**.
- **Signature rules**: physician OR nurse by default; **physician mandatory** in
  category D or a quick revision (< 6 months).
- You sign **only with your own** signature, unless you have **eHealth manager**
  rights.

## Further reading

- [Agreements (eAgreement)](eagreement.md)
- [Refused agreement (eAgreement) — causes and solutions](eagreement-refus.md)
- [The dependency scale (Katz)](../residents/katz.md)
- [eHealth and eFact settings](../configuration/reglages-ehealth.md)
- [eHealth overview](index.md)
