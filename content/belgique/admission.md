---
modules: [l10n_health_be_perdiem_ehealth, l10n_health_be_perdiem_billing, resthome_mr_ehealth, l10n_health_be_mda, l10n_health_be_eagreement_light, l10n_health_be]
---

# Admitting a resident in Belgium

:::{rh-description}
What a Belgian admission adds in Resthome: the MR, MRS or day care stay type and Annexe 7, the NISS, the MDA insurability check before Admitted, the Katz assessment and the admission agreement (eAgreement) when the stay starts.
:::

:::{rh-faq}
Why is the move to Admitted refused?
: Either the **Desired stay type** is empty — Annexe 7 cannot be produced without it — or the insurability has not been verified by an MDA request. Click **Check insurability** on the file, or untick **MDA check required** for a case that does not need it.

Can I admit a candidate who has no NISS?
: Yes: untick **MDA check required** and admit. The movement is recorded, but the admission agreement cannot be sent to the mutuality without a NISS: complete it as soon as possible.

The NISS already belongs to a resident. What do I do?
: Click **Link to that resident**: the file is repointed at the existing record, and the empty duplicate is archived. This is also the normal path for readmitting a former resident.

How many short-stay days can a resident use?
: **90 days per calendar year**. Enter the days already used on the file — ask the family, or confirm with the mutuality — before accepting the admission.

When is the mutuality told about the admission?
: When the stay is **started**. Resthome then prepares the admission agreement (Annexe 7), sent through eAgreement.
:::

The admission journey — pipeline, candidate's file, wizard — is described in
[Admissions](../admissions/index.md) and works the same way in every country.
This page gathers what **Belgium** adds to it: the sectors, the NISS, the MDA
insurability check, the Katz assessment and the admission agreement sent to the
mutuality.

## Before the first admission

- The facility's **approvals** are recorded: they decide which stay types the
  file offers. Without them, the banner **This establishment has no approval on
  file yet** appears on the file, with a **Record the approvals** link.
- The facility's **INAMI number** is configured and its **eHealth certificate**
  is active: the MDA and eAgreement need both. See [eHealth and eFact
  settings](reglages-ehealth.md).

## The stay type: MR, MRS or day care

The **Desired stay type** on the **Resident Admission** tab offers **MR**,
**MRS** or **day care (CSJ)**, according to the facility's approvals. It is not
required to fill in the file, but it is required to admit: it determines the
bed and **Annexe 7**, the admission document sent to the mutuality.

- An **MRS** bed only takes Katz categories **B and above**; a resident at
  **O or A** belongs in an **MR** bed. Keep the candidate's dependency in mind
  when choosing the sector — see [The Katz assessment](katz.md).
- A day care user is admitted with a **CSJ** stay in a day place — see
  [Admitting a day care user](centre-de-jour/admission.md).

:::{admonition} Short stay: 90 days a year
:class: info

The law caps short stays at **90 days per calendar year**. Enter the days
already used in **number of short-stay days used** — ask the family, or confirm
with the mutuality — before accepting the admission. The mutuality answers a
short-stay request with Annexe 15 or 16 — see [Agreements
(eAgreement)](ehealth/eagreement.md).
:::

## The NISS

The **NISS** is entered with the candidate's identity on the **Resident
Admission** tab. Everything that follows depends on it: the MDA request and the
admission agreement cannot be sent without it.

- **Check insurability** asks for the NISS first when it is missing.
- If the NISS entered already belongs to a resident, a banner names the existing
  record and the admission is refused until you click **Link to that resident**
  — the normal path for readmitting a former resident. See [Admitting a
  candidate](../admissions/admettre.md).
- Before any MDA reply, the identity fields are free: that is how the candidate
  is created. Once a reply exists, the insurer's values for name, date of birth,
  sex and mutuality win and the fields lock — see [Insurability
  (MDA)](ehealth/mda.md).

## Insurability before the admission (MDA)

The health insurer block of the file carries the Belgian fields:

- **Mutuelle**, **insurance regime**, **membership code**, **CT1**, **CT2**,
  **BIM status**;
- **MDA Check**: **MDA check required**, **latest MDA**, **MDA status**,
  **Insured**, **last check**.

The **Check insurability** button sends an [MDA request](ehealth/mda.md) and
fills in the mutuality, the BIM status and the CT1/CT2 codes on its own.

:::{admonition} The MDA gates the admission
:class: warning

As long as the check has not succeeded, moving to **Admitted** is refused. For
a case that does not require it — a candidate with no NISS, for example —
untick **MDA check required**.

If the answer comes back **not insured**, the admission is still possible: an
orange banner warns that billing will have to be addressed to the resident, and
the answer is recorded in the file's history.
:::

When the MDA fails, see [MDA errors](ehealth/mda-erreurs.md).

## The Katz assessment

The admission opens the resident's record: continue with the **Katz
assessment**. As long as no Katz is validated, the resident is in category
**O** by default and a "Katz to do" reminder appears on the dashboard. The
validated category is the one declared to the mutuality for the [INAMI
allowance](forfait-inami.md).

A readmission after a long leave may require a **new Katz assessment**:
Resthome flags it. See [The Katz assessment](katz.md).

## When the stay starts: the admission agreement

The wizard's **Stay start date** starts the accommodation billing. The
**Admission Date**, set when the stay is started (**Start Stay**), is the one
from which the INAMI allowance runs.

Starting the stay is also what tells the mutuality: Resthome prepares the
**admission agreement** (**Annexe 7**) as an eAgreement request, with nothing
extra to enter. It needs a valid **NISS**, the **mutuality** and an active
**eHealth certificate**; the request then follows **Draft → Sent → Accepted**
or **Rejected**.

- Annexe 7 is signed by the institution manager — see [Responsible practitioner and
  annex signatures](ehealth/eagreement-signature.md).
- A rejected request shows its reason on the agreement — see [Agreements
  (eAgreement)](ehealth/eagreement.md).

## What's next

- [Admitting a candidate](../admissions/admettre.md)
- [Insurability (MDA)](ehealth/mda.md)
- [The Katz assessment](katz.md)
- [Agreements (eAgreement)](ehealth/eagreement.md)
- [The billing journey](parcours-facturation.md)
