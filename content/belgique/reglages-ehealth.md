# eHealth and eFact Settings

:::{rh-description}
Configure your nursing home's (MR/MRS) eHealth and eFact settings: certificate, platform, Walloon Account C, CIN license and invoicing header.
:::

:::{rh-faq}
Should I choose the Acceptance or Production environment?
: Stay on Acceptance (test servers, no real data) as long as your submissions have not been validated by the CIN and AViQ. Switch to Production only once accreditation is obtained: from then on, submissions actually bill the health insurance funds.

Where do I get the eHealth certificate and the CIN Package License?
: The .p12 certificate is obtained from the eHealth portal (ehealth.fgov.be), after registering the institution and appointing the access manager. The Package License (username and password) is issued by the CIN/NIC when the software is accredited. These elements never appear in plain text in the documentation.

Should stub mode be disabled?
: Stub mode simulates eHealth responses so you can test without a real call. Leave it enabled during the test phase; disable it in production, which requires a valid eHealth certificate and a configured CIN Package License.

Why fill in a coordinating physician?
: Their NIHII number acts as the responsible practitioner on eAgreement requests when the Katz assessor has no personal NIHII. It is mandatory for a category D Katz, which requires a physician.

Is Account C mandatory for eFact in Wallonia?
: Yes. In a Walloon MR/MRS, the insurer pays the flat-rate fees to financial account C. Without a C bank journal filled in, WalCareNet rejects the batch (104511 for the missing IBAN, 105311 for the missing BIC).

Which value should I choose for the Invoice Type (Z308)?
: Leave 01 (Hospitalisation) by default: it is the value accepted at the 931000 preliminary check. Only switch to 03 (Ambulatory) if the CIN or AViQ confirms it for your sector.
:::

This screen brings together the **technical credentials and choices** that Resthome
uses to communicate with the Belgian e-health ecosystem (eHealth, MyCareNet,
WalCareNet): [MDA](../ehealth/mda.md) insurability,
[eFact](../ehealth/efact.md) billing and [eAgreement](../ehealth/eagreement.md)
agreements.

The settings are split across **two tabs**:

- **Settings > Nursing Home**: the **eHealth** part (certificate, platform,
  automation, responsible practitioner, CIN license).
- **Settings > MR/MRS**: the **Walloon billing** part (Account C and eFact
  header).

Most of these values are set **once**, at start-up, and then only change
marginally afterwards.

:::{admonition} Sensitive fields — no value is ever copied from documentation
:class: warning

The **.p12 certificate**, the **CIN Package License** and the **passwords** are
secrets **specific to your establishment**. Here we explain **what they are for**
and **where to obtain them** (eHealth portal, CIN/NIC), never their content.
Do not share them, and enter them only from the official source.
:::

## eHealth Platform

**Settings > Nursing Home > eHealth Platform.** The foundation: which identity,
which environment and which platform Resthome uses for all exchanges.

| Setting | What it is for | Recommended value (MR/MRS) |
|---|---|---|
| **Active Certificate** | The eHealth **.p12** certificate that authenticates the institution and signs the SOAP messages. Import it first under *eHealth / Certificates*, then select it here. | **Your establishment's** certificate, obtained from **ehealth.fgov.be**. Never a copied value. |
| **Institution INAMI Number** | Your institution's INAMI/RIZIV number, used in the STS, MDA, eFact and eAgreement requests. | **Your number**: 8 digits (institution) or 11 digits (NIHII-11). |
| **Competence Code** | The last 3 digits of the NIHII-11 (MR/MRS only, not CSJ); fallback when the certified NIHII-11 cannot be read from the token. | **110** (MR) or **210** (some MRS). |
| **Legal Interest Rate (%)** | The annual Belgian legal rate used to calculate the late-payment interest an insurer owes on a submission paid past the deadline. | The **rate published for the year**; **0** disables the calculation. |
| **Care Provider NIHII** | The **personal** NIHII-11 of the caregiver (nurse, physician) who issues the MDA insurability requests — required by WalCareNet/MyCareNet. | The NIHII of the **care provider at your establishment** (11 digits). |
| **Environment** | *Acceptance* = test servers (simulated data); *Production* = real servers (real billing). | **Acceptance** as long as not validated, then **Production** after accreditation. |
| **Default Platform** | The target network: WalCareNet (AViQ, Wallonia), MyCareNet (federal), IrisCareNet (Brussels, MDA). | **WalCareNet** for a Walloon MR/MRS. |
| **Stub Mode (Development)** | Simulates eHealth responses without a real call — for testing. | **Enabled** in test; **disabled** in production (requires a valid certificate + CIN license). |

:::{admonition} Start cautiously
:class: tip

At start-up: **Acceptance + Stub Mode enabled**. You validate the whole flow
without sending anything real. Once accreditation is obtained, switch **Stub Mode
disabled**, then **Production**.
:::

## eHealth Automation

**Settings > Nursing Home > eHealth Automation.** The automatic behaviours
around insurability and logs.

| Setting | What it is for | Recommended value (MR/MRS) |
|---|---|---|
| **Auto MDA Check** | Automatically checks each resident's insurability before generating the eFact — avoids rejections for invalid insurability (see [MDA](../ehealth/mda.md)). | **Enabled** as soon as the MDA is in production. |
| **Log Retention (days)** | Number of days communication and audit logs are kept; the oldest are purged by the monthly cron. | **2555** (7 years, Belgian legal requirement for health data). |
| **No-Facet Report Email** | Address used by the *Report to intermut* button on an MDA request that remained "no-facet" (no insurer answered within 24 h) — to be escalated to the CIN/intermut. | Leave the default **intermut** address. |

## Software Service Desk

**Settings > Nursing Home > Software Service Desk.** The **first point of
contact** when a provider has a problem — an AViQ accreditation requirement.

| Setting | What it is for | Recommended value (MR/MRS) |
|---|---|---|
| **Service Desk Contact** | The software publisher's contact (name, email, phone, logo), shown by the *Contact LPLG* button on eAgreement requests. | Leave the default **LPLG contact**. |

## eAgreement Responsible Practitioner

**Settings > Nursing Home > eAgreement Responsible Practitioner.** On an
[eAgreement](../ehealth/eagreement.md) request, the responsible practitioner is
the clinician who carried out the Katz assessment. If they have no personal
NIHII, the request borrows the identity of the head nurse, then of the
coordinating physician.

| Setting | What it is for | Recommended value (MR/MRS) |
|---|---|---|
| **Head Nurse (NIHII fallback)** | Their NIHII identifies the responsible practitioner when the Katz assessor (nurse, care assistant) has no NIHII. | Fill in the establishment's **head nurse**. |
| **Coordinating Physician (NIHII fallback)** | Fallback when no nurse NIHII is available, and **mandatory** for a category D Katz (physician required). | Fill in the **coordinating physician** — essential for category D Katz. |

:::{admonition} The Katz category is for declaring, not for setting the amount
:class: note

The **dependency flat rate** is the **same amount** for all Katz categories
(AViQ tariffs); the category serves to **declare the resident's profile** to the
health insurance fund. A category **D** nonetheless requires a **physician** as
the eAgreement's responsible practitioner — hence the importance of this field.
:::

## CIN Package License

**Settings > Nursing Home > CIN Package License.** The credentials that
authorise Resthome to send via GenAsync (eFact) and CommonInput (MDA).

| Setting | What it is for | Recommended value (MR/MRS) |
|---|---|---|
| **Package License Username** | Username of the software license, required for eFact and MDA. | Provided by the **CIN/NIC** at accreditation — specific to your software. |
| **Package License Password** | Password of the software license (masked field). | Provided by the **CIN/NIC**; **secret**, do not disclose it. |

:::{admonition} Where to obtain it
:class: info

The Package License is issued by the **CIN/NIC** when the software is accredited.
It has **no default value**: as long as it is not configured (and stub mode
disabled), real submissions remain blocked.
:::

## Account C (Wallonia)

**Settings > MR/MRS > Account C (Wallonia).** Since the 6th State Reform, the
insurer pays the Walloon MR/MRS flat-rate fees to a dedicated **financial account
C**, declared to the CIN during eFact registration.

| Setting | What it is for | Recommended value (MR/MRS) |
|---|---|---|
| **Account C Bank Journal** | The bank journal of the Walloon account. The **IBAN** (ET 10 Z 45-47a) and the **BIC** (Z 53-54a) written in the 920000 are derived from it. | Your establishment's **Account C journal**. Fill in the IBAN on the bank account and the BIC on the bank. |

:::{admonition} Otherwise, WalCareNet rejection
:class: warning

Without a valid Account C, WalCareNet **rejects the batch**: **104511** (missing
IBAN) or **105311** (missing BIC). The IBAN and BIC shown under the field are
read-only — they come from the journal's bank account. See
[eFact Rejections](../ehealth/efact-rejets.md).
:::

## eFact Header

**Settings > MR/MRS > eFact Header.** The header information carried by each
[eFact](../ehealth/efact.md) 920000 message (segment 300).

| Setting | What it is for | Recommended value (MR/MRS) |
|---|---|---|
| **eFact Contact Person** | Name and phone written in the header (Z305 surname / Z306 first name / Z307 phone) — the person an insurer contacts for a billing question. | For example, the establishment's **director**. If empty, the establishment name is used. |
| **eFact Invoice Type (Z308)** | The Z308 "invoice type" zone: 01 Hospitalisation, 03 Ambulatory, 09 Mixed. | **01** by default (accepted at the 931000 check). Only switch to **03** if AViQ/CIN confirms it. |

## Further reading

- [Configuration](index.md)
- [eHealth — overview](../ehealth/index.md)
- [Electronic billing (eFact)](../ehealth/efact.md)
- [Insurability (MDA)](../ehealth/mda.md)
- [Agreements (eAgreement)](../ehealth/eagreement.md)
- [eFact rejections — causes and solutions](../ehealth/efact-rejets.md)
