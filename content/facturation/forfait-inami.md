# The INAMI dependency allowance

:::{rh-description}
The INAMI dependency allowance in nursing homes (MR/MRS): from the Katz assessment to the category, the amount billed to the insurer, and the OA agreement.
:::

:::{rh-faq}
What is the INAMI dependency allowance?
: It is the daily amount covered by the health insurance fund for a resident's dependency-related care. Under the AViQ rates, it is a single amount, the same for all Katz categories (including O), calculated on days of presence and billed to the insurer (OA) via eFact, not to the resident. The category is used to declare the correct profile and to obtain the health insurance fund's agreement.

Does the allowance amount depend on the Katz category?
: No. Under the AViQ rates, the dependency allowance is the same daily amount for all categories, including category O (independent). The category does not change the amount: it is used to declare the correct dependency profile to the health insurance fund and to obtain the agreement (eAgreement). The rate remains configurable per category in Configuration → INAMI Rates if a convention requires it.

How is the dependency allowance calculated?
: Allowance = the daily allowance rate (identical for all categories) × the number of billable days of presence over the INAMI intervention period. Absences reduce the days (noon rule). The applicable rate is the one in force on the billing date.

Why does the billed category sometimes differ from the clinical category?
: The health insurance fund reimburses the category it approved in the agreement (eAgreement), not necessarily your latest assessment. Until a change is accepted by the insurer (OA), Resthome keeps billing the previous category to avoid a rejection.

Who pays for the dependency allowance?
: The allowance is covered 100% by the health insurance fund (third-party payer, via eFact). Accommodation (the room) is a separate line, charged to the resident.
:::

The **dependency allowance** is the **daily** amount covered by the health
insurance fund for a resident's **care**. It depends on their **degree of
dependency**, measured by the **[Katz assessment](../residents/katz.md)**, and it
is sent to the insurer (OA) via **[electronic billing (eFact)](../ehealth/efact.md)**.

This page explains the full chain: **Katz assessment → category → billed amount**.

## From the Katz assessment to the category

The [Katz assessment](../residents/katz.md) rates **6 criteria** (washing,
dressing, transfer and mobility, going to the toilet, continence, eating) from
**1** (independent) to **4** (fully dependent). From these ratings, Resthome
computes a **dependency category**, which is **declared to the health insurance
fund**:

| Category | Dependency | INAMI allowance |
|---|---|---|
| **O** | Independent | Yes (pseudo-code 770501) |
| **A** | Mild | Yes |
| **B** | Moderate | Yes |
| **C** | Severe | Yes |
| **Cd** | Severe, with disorientation / dementia | Yes |
| **D** | Dementia (specialist diagnosis) | Yes |

:::{admonition} The amount is the same for all categories
:class: important

Under the **AViQ** rates, the **amount** of the dependency allowance is
**identical for all Katz categories**, including **O**: a **single daily rate**,
indexed each year (e.g. **€85.72/day in 2026**). The category therefore does
**not change the amount** — it is used to **declare the correct profile** to the
health insurance fund (the **OA agreement**) and for the **care standards**. The
rate remains **configurable per category** in *Configuration → INAMI Rates* if a
convention requires it.
:::

:::{admonition} Category O by default
:class: note

As long as no Katz assessment is **validated**, the resident is in category **O**
by default and a **"Katz to do"** reminder appears. Validate the Katz assessment
to **declare the correct category** to the health insurance fund and obtain the
corresponding **agreement**.
:::

:::{admonition} Comatose patient
:class: info

The allowance for **comatose** patients is a special **federal** allowance: it
requires a specific **accreditation** of the facility. Without it, the
corresponding allowance line is not generated (accommodation is still billed).
:::

## How the amount is calculated

The allowance billed for a resident follows a simple rule:

> **Allowance = the daily allowance rate (the same for all categories) × the number of billable days of presence**

- The **days of presence** are counted over the **INAMI intervention period**
  (from admission to the end of intervention), **minus absences**. This period can
  be **shorter** than the accommodation (admission mid-month, departure, death, end
  of intervention before the room is vacated).
- An **absence** (hospitalization, holidays) **reduces** the number of days,
  according to the **[noon rule](absences.md)** (Brussels time).
- The **rate** applied is the one **in force on the date** of billing; it is
  indexed over time (see below).

:::{admonition} Allowance = health insurance fund · accommodation = resident
:class: tip

The **dependency allowance** is covered **100% by the health insurance fund**
(third-party payer, via eFact). **Accommodation** (the room) is a **separate
line**, charged to the **resident**. Both proceed in parallel over the same billing
period.
:::

## Clinical category and billed category

Two concepts coexist here, and it is important not to confuse them:

- The **clinical category** — your **latest validated Katz assessment**; it
  reflects the actual dependency and is used for care.
- The **billed category** — the one that appears on the invoice sent to the health
  insurance fund.

**They can differ.** The health insurance fund reimburses **the category it
approved** in the **[agreement (eAgreement)](../ehealth/eagreement.md)**, not
necessarily your latest assessment. In practice:

- If an **OA agreement** is in force → we bill **the category of that agreement**.
- If a **category change** is requested but the agreement is **still pending** with
  the health insurance fund → Resthome **keeps the previous category** for billing.
- Otherwise → we bill the clinical category.

:::{admonition} Why this caution?
:class: warning

Billing a category that **diverges from the agreement** triggers a **rejection**
by the OA ("allowance incompatible with the agreement"). As long as the new
category is not **accepted by the health insurance fund**, Resthome therefore keeps
billing the old one. The clinically displayed category can thus be **higher** than
the billed one.
:::

## Worsening of dependency

If a resident's condition deteriorates, enter a **new Katz assessment** with an
**aggravation reason**. Resthome prepares the update of the care agreement
(**Annexe 10**), with the reason carried over automatically and the clinician's
**signature**. The **new category** only becomes **billed** once the **health
insurance fund's agreement is obtained** (see above).

## Configuring the allowance rates

The rates are configured in the **MR/MRS → Configuration → INAMI Rates** app: one
**rate per Katz category**, with a **validity period**. Resthome automatically
applies the rate in force on the billing date. For the **annual indexation**, you
add a new rate line (new start date) and close the old one. The same screen also
manages the **accommodation rate** (charged to the resident).

## Key points

- The **daily allowance** is the **same amount for all categories** (including
  **O**); the category is used to **declare the correct profile** to the health
  insurance fund (OA agreement).
- The billed allowance = **daily rate × days of presence** (INAMI intervention
  period, minus absences).
- We bill the **category agreed with the health insurance fund** (agreement), not
  necessarily the latest clinical assessment.
- **Allowance = health insurance fund**, **accommodation = resident**, over the
  same period.

## Further reading

- [The Katz assessment](../residents/katz.md)
- [Electronic billing (eFact)](../ehealth/efact.md) · [eFact rejections](../ehealth/efact-rejets.md)
- [Agreements (eAgreement)](../ehealth/eagreement.md)
- [Absences and hospitalizations](absences.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
