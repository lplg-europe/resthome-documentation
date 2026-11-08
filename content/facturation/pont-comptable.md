---
modules: [healthcare_accounting_bridge]
---

# Accounting bridge

:::{rh-description}
Send the posted resident invoices and credit notes to an accounting database kept elsewhere, and read back whether they are paid.
:::

:::{rh-faq}
When do I need the accounting bridge?
: When the home's accounting is kept in another database, for example the accountant's own Odoo, while the invoices are issued in Resthome.

What is sent to the accounting database?
: Posted customer invoices and credit notes, and the customers they are addressed to. Drafts, purchases and the split-billing resident statement are never sent.

How do I send the invoices?
: Invoicing → Customers → Accounting bridge → Send to accounting lists the posted invoices not filed yet. Select them and use Actions → Send to accounting.

How do I know an invoice is paid?
: The bridge reads the payment state back from the accounting database. The invoice shows the Ledger Payment State, the Ledger Residual and the Ledger Settled On date.

Does the bridge create missing accounts or journals over there?
: No. It looks them up and stops when one is missing. Run the Preflight check first: it lists everything the accounting database still lacks.
:::

Many homes issue their invoices in Resthome but keep their accounts somewhere
else — often in the accountant's own Odoo. The **accounting bridge** carries
each posted resident invoice and credit note there, and brings back its
payment state, so the billing team sees in Resthome what is still unpaid.

## What travels

| Sent to the accounting database | Never sent |
|---|---|
| Posted customer invoices and credit notes | Drafts — a document that can still change is not a receivable |
| The customers they are addressed to (name, address, VAT number) | Vendor bills and miscellaneous entries — those belong to the accounting itself |
| The cancellation of a document already sent | The split-billing resident statement — the debtors' invoices next to it are the real receivables |

Only what an invoice needs travels: a customer's billing identity, never their
care record.

A posted document is never rewritten over there. To correct a sent invoice,
issue a credit note: it travels like any other document.

## 1. Prepare the accounting database

The bridge **looks up** the journal, the accounts, the taxes and the products
in the accounting database; it never creates them. Before switching it on:

1. Make sure the same journals, accounts and taxes exist on both sides.
2. On each sales journal sending invoices, fill in **Code in the accounting
   database** when the code differs there.
3. On the accounting database, create a user for the bridge, then an API key
   for that user (**Preferences → Account Security → New API Key**). The key is
   shown once: copy it. An account password does not work.

## 2. Switch the bridge on

1. Open **Settings → Sync**, block **Accounting bridge**.
2. Tick **Bridge the accounting**.
3. Choose the **Accounting database**:
   - **Paired Odoo** — the accounting database runs Resthome's sync engine
     too; the two exchange signed events.
   - **Standard Odoo** — an ordinary Odoo (an online one, the accountant's
     instance) where nothing can be installed; Resthome drives it with a user
     and an API key.
4. For a **Standard Odoo**, fill in the **Standard Odoo connection** block:
   **Odoo URL**, **Database**, **Login** (the bridge user's e-mail) and
   **API Key**. Click **Test the connection**.
5. **Save**.

<!-- screenshot to add: Settings, Sync tab, Accounting bridge and Standard Odoo connection blocks -->

## 3. Run the preflight check

Click **Preflight check** (in the settings, or under **Invoicing → Customers →
Accounting bridge**). It asks the accounting database every question the bridge
will ask — the journal by its code, the accounts by their codes, the taxes —
and lists everything missing at once. Create what is missing over there, then
click **Check again** until nothing blocks.

## 4. Send the invoices

With a **Standard Odoo**, the **Invoicing → Customers → Accounting bridge**
menu appears:

- **Send to accounting** — the posted invoices and credit notes, filtered on
  **To send**. Select them and use **Actions → Send to accounting**. The
  columns **Filed**, **Filed on**, **Ledger state** and **Still open** follow
  each one; the **Already filed** and **Still open in accounting** filters
  find the rest.
- **Preflight check** — the check above.
- **Billing identities** — the customers already sent.

On a posted invoice, the **Send to accounting** button does the same for that
one document. Once it is filed, **Check in accounting** confirms it is present
over there, posted, with the same total.

Invoices issued before the bridge was switched on can be sent the same way:
select them in the list.

:::{admonition} When a document fails
:class: note

A document the accounting database refuses (a missing account, for example)
stays queued and is retried automatically. The notification after sending says
how many went through, how many will be retried and how many could not be
filed. Run the preflight check to see what is missing.
:::

## 5. Follow the payments

The bridge reads the settlements back from the accounting database on a
schedule; **Read settlements now** in the settings does it at once. Each sent
invoice then shows, under its due date:

- **Ledger Payment State** — paid, partially paid, not paid;
- **Ledger Residual** — what is still open over there;
- **Ledger Settled On** — the date of the last settlement;
- **Filed in the accounts on** and **Id in the accounting database**.

With a **Paired Odoo**, the same information appears under **Sync Engine →
Monitoring**: **Settlements**, **Billing Identities** and **Accounting
preflight**.

:::{admonition} Pocket money needs the accounting in Resthome
:class: warning

[Pocket money](../argent-de-poche/index.md) balances are read from the accounting
entries. When the accounting is kept in another database, they cannot be
shown.
:::

## Going further

- [Billing a month, step by step](facturer-un-mois.md)
- [The billing dashboard](tableau-de-bord.md)
- [Billing settings](../configuration/reglages-facturation.md)
