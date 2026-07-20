# Document settings

:::{rh-description}
Configure resident document centralization in nursing homes (MR/MRS) — root folder, default tags, automatic filing in the Documents app.
:::

:::{rh-faq}
Where are the document centralization settings?
: In **Settings > Documents > File centralization**, the **Nursing home** block. This block only appears when the Documents app is installed.

What exactly does resident document centralization do?
: When enabled, every attachment added to a resident's record (chatter) is automatically filed in that resident's personal folder, in the Documents app. This way you find all of a resident's files in one place, with no manual filing.

Do I have to create the "Residents" root folder myself?
: No. Resthome automatically creates the "Residents" root folder (with a "Blank forms" subfolder) as soon as the company is created. The "Root folder" field already points to it; there is nothing for you to prepare.

What are the default tags for?
: It is optional. The chosen tags are automatically applied to centralized documents, which then makes searching and filtering easier in the Documents app. You can leave this field empty.

Can I disable centralization?
: Yes, by unchecking the "Nursing home" block. Documents already filed stay in the resident folders; only future attachments are no longer centralized automatically.

Is the setting shared across all my facilities?
: No. It is specific to each company (facility) in the database. Each company has its own "Residents" root folder and its own configuration, which keeps the folders isolated.
:::

The **Settings > Documents** tab gathers the settings of Odoo's **Documents**
app. In the **File centralization** section, Resthome adds a **Nursing home**
block that **automatically files** your residents' attachments into their
**personal folder**. You find these settings in **Settings > Documents
> File centralization**.

:::{admonition} Prerequisite
:class: info

These settings only appear if the **Documents** application is installed. The
residents' root folder is created automatically — there is nothing to prepare
before enabling centralization.
:::

## Resident document centralization

The **Nursing home** block controls automatic document filing. A checkbox
enables centralization; once ticked, it reveals the **root folder** and the
**default tags**.

| Setting | What it does | Recommended value (MR/MRS) |
|---|---|---|
| **Nursing home** (centralization) | Enables automatic filing: every attachment added to a resident's record is filed in their personal folder in the Documents app. | **Enabled** (ticked) |
| **Root folder** | The Documents app folder under which Resthome files all resident folders. | The **"Residents"** folder (created automatically) |
| **Default tags** | The tags automatically applied to centralized documents, to find and filter them. | **Optional** — leave empty, or choose 1 or 2 tags |

:::{admonition} The root folder is created for you
:class: tip

When the company is created, Resthome automatically creates the **"Residents"**
folder (with a **"Blank forms"** subfolder for your templates). The
**Root folder** field already points to it. There is normally no reason to
change it; only modify it if you deliberately store residents elsewhere.
:::

## One folder per resident

You do not create the folders by hand. When a resident is admitted (or when
their resident record is activated), Resthome creates their **personal folder**
under the root folder, with three ready-to-use subfolders:

- **Medical documents**
- **Administrative documents**
- **Billing documents**

The folder is named after the **resident's name** and is renamed automatically
if the name changes. The **Documents** button on the resident's record opens
this folder directly (the counter includes the files in the subfolders).

:::{admonition} Isolated per facility
:class: note

In a multi-company setup, **each company has its own "Residents" root folder**.
The setting is **specific to each facility**: enable centralization in each of
them if you run several homes.
:::

## Default tags (optional)

**Tags** are used to categorize and find documents. Resthome already provides a
list of ready-to-use tags — for example **Katz**, **End of stay**,
**eAgreement**, **OA**, **Convention**, **Medical form**, **Billing**,
**CPAS**, **GDPR**. In **Default tags**, you choose the ones that will be applied
**automatically** to each centralized document.

:::{admonition} Start light
:class: tip

Leave this field **empty** at first, or put a single generic tag in it. You
can always tag each document more precisely afterwards in the Documents app.
:::

## Disabling centralization

Unchecking the **Nursing home** block **stops** the automatic filing of future
attachments. Documents already filed in the resident folders **stay in
place** — nothing is deleted or moved.

## Going further

- [Configuration](index.md)
- [Manage a resident](../residents/gerer-un-resident.md)
- [FAQ](../faq.md) · [Glossary](../glossaire.md)
