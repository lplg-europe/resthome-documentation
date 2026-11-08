---
modules: [l10n_health_be_ehealthbox_medication]
sectors: [mr, csj]
---

# Prescriptions through the eHealthBox

:::{rh-description}
In Belgium, a physician's prescription sent to the house's eHealthBox becomes a draft prescription in WideCare, and the renewal of a prescription is asked from the physician's eHealthBox.
:::

:::{rh-faq}
What happens when a physician sends a prescription to the house's eHealthBox?
: The message becomes a draft prescription, as an e-mail to the prescriptions address does: its PDF beside the form, its lines read where the house reads them, for a nurse to check before confirming.

How does WideCare know which resident the prescription is for?
: By the national number sealed with the message. The physician is recognised by the INAMI number of the box the message came from. Nothing is guessed from the subject.

What if a message does not become a prescription?
: It is handed to the users of the box to read, with an activity.

How is a renewal asked by eHealthBox?
: From the prescription, **Ask for a Renewal**. When the house knows the physician's eHealthBox, the request leaves sealed there, with the resident's national number; the answer, with the new prescription attached, arrives as a new draft.

Where do I read the house's eHealthBox?
: In the Care app: **Nursing Care → eHealthBox**.
:::

Belgian physicians can send their prescriptions to the house's **eHealthBox**,
the secure mailbox of the eHealth platform. WideCare turns these messages into
draft [prescriptions](../soins/prescriptions.md), and asks the renewals through
the same channel. This works automatically as soon as the house uses the
eHealthBox and the medication circuit.

## Reading the house's eHealthBox

**Nursing Care → eHealthBox** opens the house's mailbox, for whoever follows the
pharmacy and the prescriptions. Each message received appears in the
notifications of the box's users; a message from a physician shows the
prescription it became, or asks to renew.

## A prescription received by eHealthBox

A message from a physician's box — or from their practice's — carrying a PDF
or its photo becomes a **draft prescription**:

- the PDF shows beside the form, and its lines are read a moment later, as the
  house reads its prescriptions (see the setting **Read the lines off the
  PDF**);
- the **resident** is the one whose national number was sealed with the
  message; the discussion says how they were recognised, or why not;
- the **physician** is the one whose INAMI number (or national number) the box
  belongs to;
- the sender receives the *read* receipt when the draft is made.

A nurse then checks each line against the PDF and confirms, as for any
prescription. A message that made no draft is left to the users of the box,
with an activity *eHealthBox message to read*.

## Asking for a renewal by eHealthBox

On a prescription in force, **Ask for a Renewal** asks the physician for the
lines to renew:

1. When the house knows the physician's eHealthBox (their INAMI number on their
   record, and their published key), a window opens, sealed for that box, with
   the resident's national number.
2. Check **To**, the **Subject** and the **Message**. The subject travels
   unencrypted: keep health data out of it; by default it is only the
   prescription's reference.
3. Click **Send by eHealthBox**, or **By E-mail Instead**.

The physician's answer, the new prescription attached, arrives as the next
draft. A physician reached only by e-mail is asked by e-mail.

## Going further

- [Prescriptions](../soins/prescriptions.md)
- [The pharmacy link](medicaments-lien-pharmacie.md)
- [The eHealthBox](ehealth/ehealthbox.md) — the box itself, beyond prescriptions.
- [eHealth](ehealth/index.md)
