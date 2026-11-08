---
modules: [l10n_health_be_ehealthbox]
---

# The eHealthBox

:::{rh-description}
Read and send secure eHealthBox messages from Resthome: the home's mailbox, writing to a caregiver or an institution, receipts, notifications and who has access.
:::

:::{rh-faq}
What is the eHealthBox?
: The secure mailbox of the eHealth platform. Caregivers and institutions exchange encrypted messages in it, addressed by NIHII or company number. Resthome reads and sends the home's messages without leaving the application.

Who can open the home's eHealthBox in Resthome?
: The users of the eHealthBox group, which the head nurse and the eHealth manager hold by default. The menus that read another box or list every message are reserved to the eHealth managers.

How often does Resthome fetch new messages?
: Every 10 minutes. A new message raises a notification in the Odoo bell of every user of the mailbox.

Can I link a message to a resident?
: Yes. When you write a message, pick the **Resident** it concerns: the message shows it, and opens the resident in one click.

How do I know a message was read?
: Open the message in **Sent Messages**: the **Receipts** show when it was delivered, when the recipient listed their box, and when they read it.
:::

The **eHealthBox** is the secure mailbox of the eHealth platform. Doctors,
pharmacies, hospitals and nursing homes send each other encrypted messages
through it, addressed by **NIHII** or company number. Resthome opens the home's
box in a familiar mail screen: you read, answer and write without going to the
eHealth website.

:::{admonition} Before you start
:class: note

- The home's **eHealth certificate** is installed and its connection tested —
  see [eHealth and eFact settings](../reglages-ehealth.md).
- Your user belongs to the **eHealthBox** group: the head nurse and the eHealth
  manager have it by default.
:::

## Opening the mailbox

Open **eHealth → eHealthBox → Mailbox**. The screen has the usual folders:

- **Inbox** — the messages received;
- **Sent Messages** — what the home sent, with its receipts;
- **Drafts** — the messages started and not sent;
- **Deleted** — the messages removed from the other folders.

Resthome fetches new messages **every 10 minutes**. Each new message raises a
notification in the **Odoo bell** of every user of the mailbox, so nobody has to
watch the folder.

<!-- screenshot to add: the eHealthBox mailbox with its folders and an open message -->

A banner warns you when the box is nearly **full**: delete the messages you no
longer need, the platform refuses new ones beyond the limit.

## Reading a message

Click a message to open it. Its attachments open or download from the message.
From an open message you can:

- **Reply** or **Forward** it;
- **Mark Unread** to come back to it later;
- **Pin** it to keep it at the top;
- **Delete** it — it goes to **Deleted**.

The message shows the **Resident** it concerns, when the sender named one, and
whether it is **Encrypted end to end**. **Metadata** shows the technical details
the sender attached, when you need them.

## Writing a message

1. Click **New Message**.
2. Add the recipients: type a box number (NIHII, national number, company number
   or eHealth number), or click **Search the eHealth directory** to look the
   caregiver or the institution up by name. You can add several recipients.
3. Fill in the **Subject** and the text, and attach files if needed.
4. Pick the **Resident** the message concerns, when it concerns one.
5. Tick **Encrypted** for health data — only the recipients can open it — and
   **Important** for an urgent message. Choose the receipts you want back:
   **Receipt: delivered**, **Receipt: listed**, **Receipt: read**.
6. Click **Send**.

From a message already sent, **Send a Copy** sends it again as it went, to the
recipients you choose. If a recipient announced an **absence**, the message is
delivered all the same and the **Away** line shows the dates.

A message the platform refuses stays with the reason, and its sender gets an
activity to deal with it.

## Receipts

On a sent message, the **Receipts** show, for each recipient, the moments you
asked for: **Delivered to the server**, **Listed** (they opened their box) and
**Read** (they opened the message). They come back with the next reading of the
box; an empty one does not mean the message was lost.

## Simulation mode

While the eHealth connection is in simulation, a banner says so on the mailbox:
the messages shown are examples, nothing leaves for the platform. Switch to the
real platform in the eHealth settings.

## For the eHealth managers

Two more menus help when something looks wrong:

- **Read a Box (Scenarios)** — reads one box by hand, at once: its state, its
  waiting messages and its receipts, as the eHealth acceptance tests ask;
- **All Messages** and **Recorded Exchanges** — every message and every exchange
  with the platform, to trace a problem; **Download the Report** packs the
  exchanges for eHealth.

## Key points to remember

- **eHealth → eHealthBox → Mailbox** opens the home's secure mailbox.
- New messages arrive every **10 minutes** and ring the Odoo bell.
- Link a message to its **Resident**; tick **Encrypted** for health data.
- The **Receipts** say when a message was delivered, listed and read.

## Going further

- [eHealth](index.md)
- [Health Directory and CoBRHA](annuaire-sante.md)
- [eHealth and eFact settings](../reglages-ehealth.md)
