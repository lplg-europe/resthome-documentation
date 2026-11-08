---
modules: [l10n_health_be_consent]
---

# eHealth consent

:::{rh-description}
Check, register or revoke at the eHealth platform a resident's consent to the exchange of their health data between the caregivers who treat them.
:::

:::{rh-faq}
What is the eHealth consent?
: The patient's informed agreement that the caregivers who treat them exchange their health data through the eHealth platform. It is registered once, at eHealth, and valid for every caregiver.

How do I know whether a resident has already given their consent?
: Open the resident's record and click the **Consent** smart button, then **Check at eHealth**. The answer says whether a consent is on file, since when, and who registered it.

Can the home register the consent with its own certificate?
: No. The consent is registered under a practitioner's name: the record needs a practitioner's personal eHealth certificate, not the home's.

Can a consent be withdrawn?
: Yes. **Revoke consent** withdraws it at eHealth, with the resident's agreement; the record then shows **Consent revoked** and the date.
:::

Before caregivers share a patient's health data through the eHealth platform,
the patient must give their **informed consent**. It is registered once, at
eHealth, and holds for every caregiver who treats them. Resthome checks it,
registers it and revokes it from the resident's record.

:::{admonition} Before you start
:class: note

- The resident has a **NISS**.
- A practitioner's personal **eHealth certificate** is installed: the consent
  is registered under a practitioner's name, never under the home's.
- The menu and the button are reserved to the **eHealth practitioners**
  (physician, nurse…) and to the **eHealth managers**.
:::

## Checking a resident's consent

1. On the resident's record, click the **Consent** smart button — it shows the
   current state. You can also open **eHealth → Consent → eHealth consents**.
2. Click **Check at eHealth**.

The record shows the answer:

| State | Meaning |
|---|---|
| **Not checked** | Nobody asked eHealth yet |
| **No consent on file** | eHealth knows no consent for this resident |
| **Consent registered** | A consent is on file: the date, and who registered it in **Registered by** |
| **Consent revoked** | A consent was given, then withdrawn: both dates |
| **Error** | The platform answered with an error, shown on the record |

<!-- screenshot to add: the eHealth consent record of a resident, after Check at eHealth -->

## Registering a consent

Register only once the resident — or their representative — has agreed.

1. On the consent record, choose the **Practitioner certificate**.
2. Fill in the resident's **eID card number** (the proof of their presence) or,
   for a resident without an eID, their **ISI+ card number**.
3. Click **Register consent** and confirm.

The record moves to **Consent registered**. A resident has a single consent
record: refresh it with **Check at eHealth** rather than creating another.

## Revoking a consent

On a registered consent, click **Revoke consent** and confirm. The record moves
to **Consent revoked**, with the date.

## Key points to remember

- The **Consent** smart button on the resident shows the state and opens the
  record.
- **Check at eHealth** before anything else: the consent may already be on file.
- Registering needs the resident's agreement and a **practitioner's**
  certificate.

## Going further

- [eHealth](index.md)
- [The resident's file in Belgium](../dossier-resident.md)
- [eHealth and eFact settings](../reglages-ehealth.md)
