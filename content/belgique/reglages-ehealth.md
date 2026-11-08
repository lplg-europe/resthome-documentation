---
modules: [l10n_health_be_connector, l10n_health_be_perdiem_ehealth, l10n_health_be_mda, l10n_health_be_eagreement_light, l10n_health_be_efact]
sectors: [mr, csj]
---

# eHealth and eFact settings

:::{rh-description}
Configure the eHealth exchanges of a nursing home (MR/MRS): environment, approvals and certificate, federated entity, MDA, eAgreement responsible practitioner, eFact, CIN licence, Account C and invoicing header.
:::

:::{rh-faq}
Where are the eHealth settings?
: In Settings, on the **eHealth** tab, visible to eHealth managers. Account C and the eFact header sit on the **MR/MRS Billing** tab, next to the other billing settings.

Should I choose the Acceptance or Production environment?
: Stay on Acceptance (test servers, no real data) as long as your sendings have not been validated by the CIN and the federated entity. Switch to Production only once accreditation is obtained: from then on, sendings actually bill the health insurance funds.

Where is the eHealth certificate set?
: On the approval: each INAMI number has its own certificate, on the **eHealth** tab of its approval. Import the .p12 file under **eHealth → Configuration → Certificates**, then choose it on the approval.

Where do I get the CIN package licence?
: From the software publisher: the **Contact LPLG** button under **Get a License** prepares the request. The licence (username and password) is issued by the CIN/NIC for the accredited software.

Should stub mode be disabled?
: Stub mode simulates eHealth responses so you can test without a real call. Leave it on during the test phase; turn it off in production, which requires a valid eHealth certificate and a configured package licence.

Why fill in a coordinating physician?
: Their NIHII acts as the responsible practitioner on eAgreement requests when the Katz assessor and the head nurse have no NIHII. It is mandatory for a category D Katz, which requires a physician.

Is Account C mandatory for eFact in Wallonia?
: Yes. In a Walloon MR/MRS, the insurer pays the flat rates to financial account C. Without a bank journal carrying an IBAN and a BIC, WalCareNet rejects the batch (104511 for the missing IBAN, 105311 for the missing BIC).

Which value should I choose for the Invoice Type (Z308)?
: Leave 01 (Hospitalisation): it is the value accepted at the 931000 preliminary check. Only switch to 03 (Ambulatory) if the CIN or the federated entity confirms it for your sector.
:::

These settings hold the **credentials and choices** WideCare uses to talk to
the Belgian eHealth ecosystem (eHealth, MyCareNet, WalCareNet):
[insurability (MDA)](ehealth/mda.md), [agreements
(eAgreement)](ehealth/eagreement.md) and [electronic invoicing
(eFact)](ehealth/efact.md).

They are spread over three places:

- **Settings → eHealth** tab: the environment, the approvals, the federated
  entity, the MDA, eAgreement and eFact choices, the logs, the service desk and
  the CIN licence;
- each **approval** (**eHealth → Configuration → Approvals**): its INAMI number
  and its **eHealth certificate**;
- **Settings → MR/MRS Billing** tab: **Account C** and the **eFact header**.

The **eHealth** tab is only visible to **eHealth managers**. Most values are
set **once**, at start-up.

:::{admonition} Sensitive fields: no value is ever copied from documentation
:class: warning

The **.p12 certificate**, the **CIN package licence** and the **passwords**
are secrets **specific to your establishment**. This page explains what they are
for and where to obtain them, never their content. Enter them only from the
official source.
:::

## eHealth platform

| Setting | What it is for | Recommended value |
|---|---|---|
| **Environment** | **Acceptance**: the eHealth test servers (simulated data). **Production**: the live servers (real billing). | **Acceptance** until accreditation, then **Production**. |
| **Stub Mode (Development)** | Simulated responses, without any real call. | On while testing; off in production (requires a valid certificate and the package licence). |

:::{admonition} Start cautiously
:class: tip

At start-up: **Acceptance** with **Stub Mode** on. You go through the whole
flow without sending anything real. Once accredited, turn **Stub Mode** off,
then switch to **Production**.
:::

## Approvals and certificate

The **Approvals** block of the tab summarises the INAMI numbers configured.
**Manage approvals** opens them: one record per INAMI number, with its identity,
its **eHealth certificate** and the sectors it is approved for. A company that
runs a rest home and a day care centre has two. See [Belgian
settings](reglages.md) for the approval itself.

On the **eHealth** tab of an approval:

- **Certificate**: the establishment's **.p12**, imported first under
  **eHealth → Configuration → Certificates** (or straight from the field);
- its state and its expiry date, shown once a certificate is chosen.

Each stay sends and reads its flows — insurability, agreements, eFact — under
the approval of its sector, with that approval's own certificate.

On the certificate record, **Test connection** checks that the certificate
reaches the eHealth platform before any real sending.

The **Federated entity** setting says which entity finances your MR/MRS:
Wallonia (AViQ), Brussels (Iriscare)… It decides the eHealth platform, the region
code written in the eFact file, whether Account C applies and which pseudo-codes
are billed. The platform it implies is shown under the field.

## Nursing home — MyCareNet

| Setting | What it is for | Recommended value |
|---|---|---|
| **Legal Interest Rate (%)** | The annual Belgian legal rate used to compute the late-payment interest an insurer owes on a sending paid after its deadline. | The rate published for the year; **0** turns the computation off. |
| **CM contact point (PUC)** | The single contact point the Christian mutuality assigned to **your** home, which addresses your CM invoices. | Ask the mutuality for it. Left empty, the default of your federated entity applies. |
| **eFact followers** | The people notified of every insurer answer on your eFact sendings: acceptance, rejection, settlement. They follow each new batch, including those created automatically. | The person in charge of billing. |

## eHealth Automation

| Setting | What it is for | Recommended value |
|---|---|---|
| **Auto MDA Check** | Checks each resident's insurability before the eFact billing is generated, to avoid rejections for invalid insurability. | **On** once the MDA is in production. |
| **Waiting list check** | Every month, asks the health insurance funds about every open admission request, so that a candidate who died in the meantime is closed before anyone phones them. | On if your waiting list is long. |

See [Insurability (MDA)](ehealth/mda.md) and [Admitting a resident in
Belgium](admission.md).

## Insurability (MDA)

| Setting | What it is for | Recommended value |
|---|---|---|
| **Care Provider NIHII** | The NIHII-11 of the healthcare professional who issues the MDA requests, required by WalCareNet / MyCareNet. | The NIHII of a care provider of your establishment. |
| **No-Facet Report Email** | The address used to report to the inter-mutualist an MDA request the platform closed without any insurer answer. | Leave the default address. |

## eAgreement Light

On an [eAgreement](ehealth/eagreement.md) request, the responsible practitioner
is the clinician who carried out the Katz assessment. When they have no NIHII,
the request borrows the identity of the people set here, in this order.

| Setting | What it is for |
|---|---|
| **Head Nurse** | Their NIHII identifies the responsible practitioner when the Katz assessor (nurse, care assistant) has no NIHII. |
| **Coordinating Physician** | Used when no nurse NIHII is available, and **mandatory** for a category D Katz, which requires a physician. |
| **Generic nurse NIHII** | The last resort: the number the federated entity gives a nurse without their own, shared by every home of the entity. |

See [Responsible practitioner and annex
signatures](ehealth/eagreement-signature.md).

## Communication logs

**Log Retention** sets how many days the eHealth communication and audit logs
are kept; older logs are purged every month. The default, **3653 days** (10
years), follows the Belgian tax rule for invoicing records: these logs carry the
proof of each eFact sending.

## Software Service Desk

**Service Desk Contact** is the first point of contact when a problem occurs
with an exchange. Its name, e-mail, phone and logo are used by the **Contact
LPLG** button on eAgreement requests. Leave the default contact.

## CIN Package License

The credentials that allow WideCare to send eFact and MDA requests.

| Setting | What it is for |
|---|---|
| **Package License Username** | The username of the software licence, required for eFact and MDA. |
| **Package License Password** | Its password (masked field). Secret: never share it. |
| **Get a License** | **Contact LPLG** prepares the request to the software publisher. |

:::{admonition} No licence, no real sending
:class: info

The package licence has **no default value**. As long as it is not configured
and stub mode is on, nothing real leaves.
:::

## Account C (Wallonia)

*Settings → MR/MRS Billing → Account C (Wallonia).* Since the 6th State Reform,
the insurer pays the Walloon MR/MRS flat rates to a dedicated **financial
account C**, declared to the CIN when joining eFact.

| Setting | What it is for |
|---|---|
| **Account C Bank Journal** | The bank journal of that account. The **IBAN** and the **BIC** written in the eFact file come from its bank account; they are shown, read-only, under the field. |

:::{admonition} Otherwise, WalCareNet rejects the file
:class: warning

A journal whose bank account has no IBAN or no BIC shows a warning under the
field. Set them on the bank account (and the BIC on its bank): WalCareNet
otherwise **rejects the batch** with **104511** (IBAN) or **105311** (BIC). See
[eFact rejections](ehealth/efact-rejets.md).
:::

## eFact Header

*Settings → MR/MRS Billing → eFact Header.* What each eFact file says about
your establishment.

| Setting | What it is for | Recommended value |
|---|---|---|
| **eFact Contact Person** | The name and phone the insurer reaches for a billing question. | For example the director. Left empty, the establishment name is used. |
| **Invoice Type (Z308)** | 01 Hospitalisation, 03 Ambulatory, 09 Mixed. | **01** (accepted at the 931000 check). Switch to **03** only if the CIN or the federated entity confirms it. |

An approval can override the Account C journal and the contact person on its
own **eFact** tab: a day care centre with its own INAMI number, for example. Left
empty, those of the settings apply. The sending numbers are counted per INAMI
number.

## Further reading

- [Belgian settings](reglages.md)
- [eHealth — overview](ehealth/index.md)
- [Insurability (MDA)](ehealth/mda.md)
- [Agreements (eAgreement)](ehealth/eagreement.md)
- [Electronic invoicing (eFact)](ehealth/efact.md)
- [eFact rejections — causes and solutions](ehealth/efact-rejets.md)
