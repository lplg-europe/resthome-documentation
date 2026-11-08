---
modules: [l10n_health_be_perdiem_ehealth, l10n_health_be_perdiem_billing, resthome_mr_ehealth, l10n_health_be_mda, l10n_health_be_eagreement_light, l10n_health_be, l10n_health_be_eid_accommodation]
---

# Admitting a resident in Belgium

:::{rh-description}
What a Belgian admission adds in Resthome: the MR, MRS or day care stay type and Annexe 7, the NISS and the eID card, the MDA insurability check before Admitted and on the waiting list, the Katz assessment and the admission agreement (eAgreement) when the stay starts.
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

How do I know whether a candidate on the waiting list has died?
: Filter the admission list on **Waiting list**, select the requests and choose **Check insurability (MDA)** in the **Actions** menu. A death reported by the mutuality closes the request as **Died before admission**.
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
- The **approval** of the sector carries the **INAMI number** and an active
  **eHealth certificate**: the MDA and eAgreement need both. See [Belgian
  settings](reglages.md) and [eHealth and eFact settings](reglages-ehealth.md).

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

Next to each sector, the file shows the free places against the approval
(**3/40 free**, for example), or **not licensed** for a sector the
establishment has no approval for.

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

Rather than typing it, click **Read eID Card** in the header of the admission
request: the card fills in the candidate behind the request — never the relative
who enquires — with the NISS, the date of birth, the gender, the nationality and
the place of birth, and the request takes the name read from the chip. See
[Reading the eID card](lecture-eid.md).

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

The **Katz scale** block, at the top of the **Resident Admission** tab, decides
the orientation before the identity:

- **New Katz** opens an assessment for the candidate;
- **Import a Katz** attaches an assessment done elsewhere — a hospital, the
  previous home — with who assessed it and where.

The category is read in the sector the candidate asks for, and the assessment
follows the resident once admitted. A resident who arrives without a validated
Katz has **no category**: no INAMI allowance is billed for them until it is
validated. See [The Katz assessment](katz.md) and [The INAMI
allowance](forfait-inami.md).

A readmission after a long hospital stay may require a **new Katz
assessment**: Resthome flags it.

## The waiting list checked with the mutualities

A long waiting list ages: some candidates die before a place frees up. Rather
than phoning them, ask their mutualities.

1. In the admission list, filter on **Waiting list** (requests not admitted, not
   refused or withdrawn, not given up).
2. Select the requests and choose **Check insurability (MDA)** in the
   **Actions** menu. One request is checked at once; several open the batch
   wizard, pre-filled with the current month. Requests without a NISS are
   counted and listed.
3. When a mutuality reports a **death**, the request is closed with the reason
   **Died before admission**, a dated note and an activity for the person in
   charge. An admitted request is never touched; an error or a "not insured"
   answer closes nothing.

To run this check every month on its own, turn on **Waiting list check** in the
[eHealth settings](reglages-ehealth.md).

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
- [Reading the eID card](lecture-eid.md)
- [Insurability (MDA)](ehealth/mda.md)
- [The Katz assessment](katz.md)
- [Agreements (eAgreement)](ehealth/eagreement.md)
- [The billing journey](parcours-facturation.md)
