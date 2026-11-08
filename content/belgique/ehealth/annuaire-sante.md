---
modules: [l10n_health_be_addressbook, l10n_health_be_cobrha]
sectors: [mr, csj]
---

# Health Directory and CoBRHA

:::{rh-description}
Look a doctor, a nurse, a pharmacy or a hospital up in the national eHealth registers from WideCare, turn the answer into a contact, and see the names behind the NIHII numbers the mutuality returns.
:::

:::{rh-faq}
What is the Health Directory?
: An application that searches the national eHealth registers of healthcare professionals and institutions, by name, NIHII, national number or company number. What comes back is kept in WideCare and becomes a contact in one click.

How do I find a resident's general practitioner?
: On the resident's record, click **Find in the Health Directory** under their physician. The search opens on physicians; **Contact** on a result makes them the resident's physician.

Who can use the Health Directory?
: The users of the eHealth group, once the home's eHealth certificate is installed.

What is CoBRHA?
: The federal register behind the directory. WideCare asks it for the name of a NIHII — the reference pharmacy or the holder of the global medical file the mutuality returns — and keeps the answer 30 days.

Are past searches kept?
: Yes. Each search is kept in **Search history**, with who searched and what came back, so it can be reopened instead of asked again.
:::

The **Health Directory** looks professionals and institutions up in the
national eHealth registers: the exact name, the NIHII, the profession, the work
address. It saves typing, and spelling mistakes, when you add a doctor, a
pharmacy or a hospital to WideCare.

:::{admonition} Before you start
:class: note

- The home's **eHealth certificate** is installed — see [eHealth and eFact
  settings](../reglages-ehealth.md).
- Your user belongs to the **eHealth** group; without it, the application and
  its buttons do not show.
:::

## Searching the directory

1. Open the **Health Directory** application, then **Professionals and
   institutions**.
2. Click **Search the directory**.
3. Choose the **Kind of search**:
   - **Professional by name** — last name, first name, profession;
   - **Professional by NIHII**;
   - **Professional by SSIN** — the national number;
   - **Organisation by name** — name, type of institution, city, postcode;
   - **Organisation by NIHII / CBE / EHP** — its NIHII, its company number or
     its eHealth number.
4. Click **Search**.

In a name, a star stands for the rest of a word: `*bordet*` finds every name
that contains it. Accents and case do not matter. When the directory has more
answers than it sends, a banner asks you to narrow the search.

<!-- screenshot to add: the Search the Health Directory window with a few results -->

Every answer is kept in **Professionals and institutions**. On an entry:

- **Create / open contact** turns it into a contact — a physician when the
  profession says so — or opens the contact it is already linked to;
- **Ask the platform again** refreshes it.

**Search history** lists the past searches, with who ran them and what came
back: **Reopen** one instead of typing it again.

## From a record

The directory also opens where you need it:

- on a **resident**, **Find in the Health Directory** under their physician:
  the search opens on physicians, and **Contact** on a result makes them the
  resident's physician;
- on a **physician's** contact, **Search the Health Directory** completes that
  contact rather than creating a second one;
- on an **employee** who holds an INAMI number, **Search the Health Directory**
  finds their NIHII.

## Names behind the NIHII numbers (CoBRHA)

When the [insurability check (MDA)](mda.md) returns the NIHII of a resident's
**reference pharmacy** or of the doctor who holds their **global medical file**,
WideCare asks **CoBRHA**, the federal register, for the name behind the number:
the **Check Insurability** window shows it. In the residents list, the
**Pharmacy** and **DMG Holder** columns can be added from the optional columns.

Each answer is kept **30 days**, so the same number is not asked again every
time. The eHealth managers find the kept answers in **eHealth → Configuration →
CoBRHA Cache**. A failed lookup never blocks the MDA: the name simply stays
empty.

## Key points to remember

- In **Health Directory → Professionals and institutions**, the **Search the
  directory** button searches by name, NIHII, national number or company number.
- **Create / open contact** turns an answer into a contact, without duplicates.
- **Find in the Health Directory** on a resident assigns their physician.
- CoBRHA names the reference pharmacy and the DMG holder returned by the MDA.

## Going further

- [eHealth](index.md)
- [Insurability (MDA)](mda.md)
- [The eHealthBox](ehealthbox.md)
- [The resident's file in Belgium](../dossier-resident.md)
