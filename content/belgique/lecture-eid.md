---
modules: [l10n_health_be_eid, l10n_health_be_eid_accommodation]
sectors: [mr, csj, rs]
---

# Reading the eID card

:::{rh-description}
Read the Belgian eID card in WideCare to fill in a candidate's or a resident's identity and NISS from the chip, on the admission request, on a record or to create a new contact.
:::

:::{rh-faq}
What do I need to read an eID card?
: A card reader on a Windows workstation, the Belgian eID middleware, and the eID reader program of WideCare. When the reader does not answer, WideCare offers **Install the eID reader on this computer**; it installs for your Windows user, without administrator rights.

What does the card fill in?
: The name, the NISS, the date of birth, the gender, the nationality, the place of birth and the address, the card number, the chip number and the validity dates, and the photo.

Does reading a card create a duplicate?
: No. Read from a record, the card updates that record. Read from **New Partner via eID**, it updates the contact of the company that already has the card's NISS, and only creates one when nobody has it.

Does the card fill in the relative who calls for an admission?
: No. On an admission request, the card always fills in the candidate behind the request, never the relative who enquires.

Why does the reader ask me to confirm a server?
: The first time it sends a card to a server, the reader asks whether that server may receive it, then remembers your answer. It only sends to a secure (https) address when the server is not your own workstation.
:::

Typing an identity is where a NISS gets a transposed digit. Reading the
**Belgian eID card** fills in the identity from the chip itself.

## Before the first reading

On each workstation that reads cards:

- a **card reader**, and the **Belgian eID middleware** (the official eID
  software);
- the **eID reader** program of WideCare, which runs on **Windows** only.

When the reader does not answer, WideCare says so and offers **Install the eID
reader on this computer**. Download it, double-click it: it installs for your
Windows user, with no administrator rights. Then click **Read eID Card** again.

:::{admonition} The reader checks where the card goes
:class: note

The first time it sends a card to a server, the reader asks you whether that
server may receive it, then remembers your answer. Outside your own workstation
it only sends to a secure (**https**) address. A web page cannot divert the
identity, the photo or a signature from the card.
:::

## On an admission request

1. Insert the card in the reader.
2. Open the admission request and click **Read eID Card** in its header.
3. Wait for the message: reading takes up to 30 seconds.

The card fills in the **candidate** behind the request — never the relative who
enquires — and the request takes the name read from the chip. The NISS, the date
of birth, the gender, the nationality, the place of birth and the card shown on
the request take the card's values. Each change is tracked in the request's
thread, in the name of the user who clicked.

If you start a new reading while a previous one is still waiting, the previous
one stops: no forgotten "please wait".

See [Admitting a resident in Belgium](admission.md).

## On a resident's or a contact's record

**Read eID Card**, in the header of the record, updates that person from the
card: identity, NISS, address and photo.

The **eID Card** tab of the record keeps:

- **eID Card Number** and **eID Chip Number**;
- **eID Valid From** and **eID Valid Until**;
- **Place of Birth**.

The NISS identifies the **person** for life; the card number identifies the
**card**, which expires and is renewed.

## Creating a contact from a card

**Contacts → New Partner via eID** reads the card and opens the person: found
by NISS when they already exist in the company, created otherwise.

## What's next

- [Admitting a resident in Belgium](admission.md)
- [The resident's file in Belgium](dossier-resident.md)
- [Insurability (MDA)](ehealth/mda.md) — once the NISS is in, check the
  insurability.
