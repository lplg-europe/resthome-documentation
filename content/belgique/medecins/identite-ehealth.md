---
modules: [l10n_health_be_connector, l10n_health_be_eid, l10n_health_be_gp]
sectors: [gp]
---

# eHealth identity and eID sign-in

:::{rh-description}
Set up your eHealth identity as a general practitioner in WideCare: import your personal eHealth certificate, link it to your user, and sign in to eHealth every day with your eID card.
:::

:::{rh-faq}
Where do I get my eHealth certificate?
: From the eHealth platform, which issues it to you as a doctor. WideCare does not issue certificates: it stores the one you import and signs your calls with it.

Can I use the certificate of a colleague?
: No. A user carries only their own practitioner certificate: WideCare refuses a certificate that names another practitioner.

How often do I sign in with my eID card?
: Once a day. **eHealth sign-in valid until**, in your preferences, shows until when your calls are signed in your name; sign in again afterwards.

What does the quality of my certificate change?
: The menus. A certificate with the quality **Doctor (natural person)** gives you the **Practice** app and the doctor's eHealth services.
:::

Every eHealth call of the practice — insurability, eAttest, DMG — is made **in
your name**, as a doctor. WideCare needs your **eHealth certificate**, and your
**eID card** signs you in every day.

## What you need

- your **personal eHealth certificate** (a .p12 file and its password), issued
  by the eHealth platform to you as a doctor;
- your **INAMI number** (11 digits) and your **NISS**;
- for the eID sign-in: a **card reader**, the **Belgian eID software** and the
  **WideCare eID reader** on your Windows workstation, and your eID card with
  its PIN.

## Import your certificate

1. Open **eHealth → Configuration → My eHealth identity**. Without a
   certificate yet, a new one opens, with the quality **Doctor (natural
   person)** and your name as **Practitioner**.
2. Fill in:
   - **INAMI Number**: your 11-digit number;
   - **SSIN**: your national number, as on your eID card;
   - **Environment**: **Acceptance** to test, **Production** for real calls;
   - **Certificate File (.p12)** and its **Password**.
3. Save, then click **Activate**.
4. Click **Test connection** to check that the eHealth platform accepts it.

The certificate becomes **your** practitioner certificate at once: your
preferences show it under **My practitioner certificate**, and the eHealth
menus of a doctor open.

<!-- screenshot to add: the doctor's certificate with its quality, INAMI number and environment -->

:::{admonition} Your certificate stays yours
:class: note

A user carries only their own practitioner certificate. The password and the
.p12 file are secrets: never send them by email, and never copy them from a
document.
:::

## Sign in with your eID card

Once a day, before your first eHealth call:

1. Insert your eID card in the reader.
2. Click **Practice → eID sign-in**, or **Sign in with my eID card** in your
   preferences.
3. Type your PIN in the window of the eID software.

WideCare confirms **Signed in to eHealth.** Your preferences show **eHealth
sign-in valid until**: until then, your calls are signed in your name.

If the reader does not answer, check that the WideCare eID reader and the eID
software are installed and that the card is inserted, then try again.

## Your preferences

Your own preferences (**My Preferences** in your user menu) show, in the
**eHealth** group:

- **My practitioner certificate** and its **eHealth quality**;
- **eHealth sign-in valid until** and **Sign in with my eID card**.

## The test mode of the practice

In **Settings**, the **eHealth** tab sets for the whole practice:

- **Environment**: **Acceptance** (the eHealth test servers, no real data) or
  **Production**;
- **Stub Mode (Development)**: while it is ticked, the answers are simulated
  and no call leaves WideCare.

Keep the **Acceptance** environment and the stub mode until your access to the
MyCareNet services is in place: the approvals of WideCare for the general
practitioners' services are in preparation.

## What's next

- [The patient's file in Belgium](patients-belgique.md)
- [Insurability (MDA)](assurabilite.md)
