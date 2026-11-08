---
modules: [l10n_health_be_gp]
sectors: [gp]
---

# General practice in Belgium

:::{rh-description}
What WideCare adds for a general practitioner in Belgium: the eID card, the insurability check (MDA), the eAttest, the global medical file (DMG), the INAMI nomenclature and the eFact per act, and what the practice must obtain first.
:::

:::{rh-faq}
Where are the Belgian services of the practice?
: In the **Practice** app, below the patients and the consultations: **Insurability**, **Attestations**, **Global Medical File** and **eID sign-in**. The INAMI nomenclature sits in the **Invoicing** app and the eFact per act in the **eHealth** app.

What must the practice obtain before using the eHealth services?
: Your own eHealth certificate as a doctor, issued to you by the eHealth platform; an eID card reader with the Belgian eID software on your workstation; and the access to the MyCareNet services you use. WideCare does not supply them.

Is WideCare approved for the MyCareNet services of general practitioners?
: The approvals for the general practitioners' services are in preparation. Until your practice goes live, keep the test mode described below: the answers are simulated and nothing reaches the mutualities.

Do I need the eID card of the patient?
: No, but it saves typing: read from the card, the NISS and the identity are right the first time.
:::

:::{toctree}
:hidden:

identite-ehealth
patients-belgique
assurabilite
eattest
dmg
nomenclature
efact-a-l-acte
:::

In Belgium, the practice works with the patient's **NISS** and **mutuality**,
and with the **eHealth** and **MyCareNet** services that a doctor calls in their
own name. WideCare installs them with the practice.

## Before you start

The eHealth services are called **in your name**, as a doctor. Before the first
call:

- **Your eHealth certificate**: the personal certificate (.p12) the eHealth
  platform issues to you as a doctor. Import it as your eHealth identity.
- **Your eID card**: a card reader, the Belgian eID software and the WideCare
  eID reader on your workstation. Once a day, the card signs you in to eHealth.
- **The access to the MyCareNet services** you use: insurability, eAttest, DMG,
  eFact.

See [eHealth identity and eID sign-in](identite-ehealth.md).

:::{admonition} Test mode
:class: warning

The approvals of WideCare for the general practitioners' MyCareNet services are
in preparation. As long as **Stub Mode (Development)** is ticked in
**Settings**, on the **eHealth** tab, the insurability and DMG answers are
simulated: nothing leaves WideCare. The eAttest has its own test mode, shown by
a **Stub** ribbon on the attestation. Keep them on until your practice goes
live.
:::

## What Belgium adds to the Practice app

| Menu | What it opens |
| --- | --- |
| **Insurability** | The insurability checks (MDA) of your patients. |
| **Attestations** | The eAttest: the electronic attestations of care given. |
| **Global Medical File** | **Consultations** of the DMG register and DMG **Notifications**. |
| **eID sign-in** | Your daily eHealth sign-in with your eID card. |

Elsewhere:

- **eHealth → Configuration → My eHealth identity**: your certificate;
- **eHealth → eFact per act**: the third-party payment files;
- **Invoicing → Customers → INAMI Nomenclature**: the codes, fees and personal
  shares.

## What's next

- [eHealth identity and eID sign-in](identite-ehealth.md)
- [The patient's file in Belgium](patients-belgique.md) — NISS, mutuality, eID.
- [Insurability (MDA)](assurabilite.md)
- [eAttest](eattest.md)
- [Global medical file (DMG)](dmg.md)
- [The INAMI nomenclature](nomenclature.md)
- [eFact per act](efact-a-l-acte.md)
- [General practice](../../medecins/index.md) — the practice in every country.
