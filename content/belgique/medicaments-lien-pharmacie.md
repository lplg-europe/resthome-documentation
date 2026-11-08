---
modules: [l10n_health_be_pmi]
sectors: [mr, csj]
---

# The pharmacy link

:::{rh-description}
Exchange files with the residents' pharmacies in Belgium over HomeLink: the medication schedule (Therapylink) every day, the sachets to produce (Doselink), the orders (Orderlink) by eHealthBox, and the pharmacy's stock and invoices received back.
:::

:::{rh-faq}
What is the pharmacy link?
: The link between the house and a pharmacy for the HomeLink files Belgian care homes and pharmacies exchange. WideCare sends the residents' medication schedule every day, and receives the pharmacy's stock statement and invoice.

How do the files reach the pharmacy?
: By eHealthBox (sealed for the pharmacy), by SFTP or FTPS on the pharmacy's server, or not at all: with **None (download)**, you make the file and hand it over yourself.

What happens if a file does not leave?
: It is tried again four times, then someone is told: the Medicines workstation shows **Files Not Received** and a line to do, and the file says why.

How is a pharmacy order sent by eHealthBox?
: When the pharmacy's INAMI number is known, the basket leaves sealed by eHealthBox every morning at the hour of the house, with the medication sheets. **Send Now** sends it at once.

Who manages the pharmacy links?
: The head nurse, the administrative staff and the medication manager. A physician reads the link without its buttons.
:::

**HomeLink** is the protocol Belgian care homes and pharmacies exchange files
with. WideCare uses it to send each pharmacy the **medication schedule** of its
residents, the **sachets** it must produce and the **orders**, and to receive
back the pharmacy's **stock** and **invoice**.

The link builds on the [pharmacy orders](../medicaments/pharmacie.md) of the
Care app and on the CNK codes of [SAM](sam-base-medicaments.md): a pharmacy
finds a medicine by its CNK.

## Where to find it

- **Nursing Care → Configuration → Pharmacy → Pharmacies** and **Pharmacy
  Links** (head nurse, medication manager).
- **Nursing Home → Pharmacies**: **Pharmacies**, **Pharmacy Links**, **Files
  Sent**, **Import a Pharmacy File**, **Pharmacy Invoices** and **Pharmacy
  Stock** (administrative staff).
- On the Medicines workstation (**Nursing Care → Medicines**), **Pharmacy**
  tab: the pharmacy links, and **Schedules Sent**, **Pharmacy Stock** and
  **Pharmacy Invoices**; the smart buttons **Files Not Received**, **Pharmacy
  Stock** and **Pharmacy Invoices** (head nurse, medication manager).

## 1. Set up the pharmacy

On the pharmacy's contact (a company with **Is a Pharmacy** ticked), fill in:

- **APB Number** — the number a HomeLink file is addressed to;
- **Pharmacy Group**;
- **INAMI Number (eHealthBox)** — the pharmacy's eHealthBox, for sending the
  orders sealed.

These fields show only once **Is a Pharmacy** is ticked, for a pharmacy in
Belgium. A pharmacy shows in the **Pharmacies** list once it has an APB number
or a resident chose it.

## 2. Create the pharmacy link

One link per pharmacy the residents chose: **Pharmacy Links**, then **New**.

| Group | What to set |
| --- | --- |
| **Pharmacy** | The pharmacy, **The House's Reference Pharmacy** (its file also covers every resident who has no pharmacy of their own), the **APB Number**, the **Residents** it serves and the **Expected Delivery Time** in days. |
| **House** | The **Identification Number** of the house in the files, usually its INAMI number. |
| **Files Sent** | **Therapylink**, **Sent Every Day At**, the **Period** covered (in days, ten at least), the **Sort Order**; **Doselink** and the day it is **Sent On**; **Orderlink**. |
| **Digital Connection** | **Connection**: *None (download)*, *SFTP*, *FTPS* or *eHealthBox*. |
| **Pharmacy's Server** | For SFTP or FTPS: host, port, directory, and the server key (SFTP) or the certificate check (FTPS); the login is for the administrator. |
| **eHealthBox** | The pharmacy's box, **Encrypted**, and **Test: to the House** (sends to the house's own box, for a test). |

**Test the Connection** checks the server or the box. The smart buttons give
the medicines **Without CNK** (a file cannot name them), the **Files** sent,
the **Stock** statements and the **Invoices**.

<!-- screenshot to add: pharmacy link form with its Files Sent and Digital Connection groups -->

## 3. The files sent

### Therapylink — the medication schedule

Every day at the link's hour, WideCare makes the **Therapylink** file: every
active treatment of the pharmacy's residents, each intake on its date and hour
over the period, the *as needed* ones as such, the medicines in the pharmacy's
sachets flagged. The file is checked against the official schema before it is
kept; what cannot be sent (a resident without a national number, a medicine
without CNK, a dose that is not a number) is named, never guessed.

- With a connection, the file leaves by itself; **Send Today's File Now**
  sends it at once, **Make the File Only** makes it without sending.
- With **None (download)**, **Make the Therapylink File** makes it for you to
  hand over.

### Doselink — the sachets to produce

When **Doselink** is ticked, a weekly file tells the pharmacy what to produce
in sachets (robot or by hand) — only the treatments in the pharmacy's sachets.
It leaves on the chosen day at the link's hour; each file starts the day after
the last one sent, without gap or overlap. **Make the Doselink File** and
**Send the Doselink Now** are in the header.

### Orderlink — the order file

When **Orderlink** is ticked, each pharmacy order also leaves as a file the
pharmacy's software imports, next to the PDF the pharmacist reads. **Orderlink
File** on the order downloads it.

### Following the files

**Files Sent** lists each file with its status **Made**, **Sent** or
**Failed**, its journey and, by eHealthBox, when the pharmacy **received** and
**opened** it. A file that fails is tried again four times, then the Medicines
workstation shows **Files Not Received** and a line *The schedule did not reach
the pharmacy*. **Send Again** retries it.

## 4. Orders by eHealthBox

On a [pharmacy order](../medicaments/pharmacie.md), when the pharmacy's
eHealthBox is known:

- the basket **leaves by itself** every morning from the hour set in the Care
  settings, sealed for the pharmacy, with the medication sheets of its
  residents; **Send Now** sends it at once;
- the order follows **Sent**, then **Seen by the Pharmacy** when the pharmacy
  opens it; the **eHealthBox** smart button gives its status;
- the **Medication Schedule** smart button says when the last schedule left
  for that pharmacy and whether it was opened, with the history of the
  schedules;
- the pharmacy's answer is attached to the order: a banner says *The pharmacy
  answered about this order*, with **Read**.

When the box is not known, a banner asks to type the pharmacy's INAMI number on
its contact, rather than sending by e-mail. At night and at the weekend, the
order shows the number of the pharmacy on duty.

## 5. What the pharmacy sends back

The pharmacy's files arrive by eHealthBox and are read by themselves. A file
handed over otherwise is imported with **Import a Pharmacy File** (or **Import
a File From the Pharmacy** on the link): a stock statement (`_ST.xml`) or an
invoice (`_IN.xml`).

### Pharmacy stock (Stocklink)

A pharmacy that keeps the residents' medicines (a robot, drawers) sends its
count. Each line becomes the **Units in the Box** of the resident's treatment,
found by national number and CNK — zero included, so the box is to order. What
matches no resident or no treatment is named; **Apply Again** retries it after
a national number or a CNK was fixed.

### Pharmacy invoices (Invoicelink)

The pharmacy's invoice comes with one block per resident: each resident's part
is placed on the **Pharmacy Invoice**, with the tabs **Residents**, **Lines**
and **VAT**, and the status **Received**, then **Vendor Bill Made**.

1. Check the residents; **Find the Residents Again** retries those not found.
2. Click **Make the Vendor Bill**.
3. Once the vendor bill is posted, pass each resident's part on to them: see
   [Billing medicines in Belgium](medicaments-facturation.md).

## Going further

- [Pharmacy orders](../medicaments/pharmacie.md)
- [The SAM medication database](sam-base-medicaments.md)
- [Prescriptions through the eHealthBox](medicaments-ehealthbox.md)
- [Billing medicines in Belgium](medicaments-facturation.md)
