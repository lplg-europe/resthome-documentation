---
modules: [widecare_ai]
sectors: [mr, csj, rs, gp]
---

# WideCare AI assistant

:::{rh-description}
Ask the WideCare documentation a question without leaving WideCare: the assistant answers with the relevant passages and a link to each page they come from.
:::

:::{rh-faq}
How do I ask the assistant a question?
: Click the assistant's icon in the top bar, type your question in plain words, then press Enter. The answer comes with the pages it is drawn from.

Does the assistant read the residents' records?
: No. It only reads the published documentation. When a language model is connected, only the question and the passages found are sent to it, never a resident's data.

Does the assistant work without an internet connection or a paid service?
: Yes. Out of the box it searches the documentation shipped with it and returns the best passages with their links. A language model, when an administrator connects one, only adds a written answer built from the same passages.

What happens when the daily limit of written answers is reached?
: The assistant falls back to the documentation search, which always answers.
:::

The **WideCare AI** assistant answers "how do I do this?" from inside WideCare. It
knows one thing only: the published WideCare documentation. Every answer shows
the pages it comes from.

## Ask a question

1. Click the assistant's icon (a sparkle) in the top bar, available to every
   user.
2. Type your question in plain words — the name of the screen or of the step
   works best.
3. Press **Enter** or click the search button.

The window then shows:

- **the answer** — the best passage, with its heading, its page and a link to
  open the full page; or, when a language model is connected, a written answer;
- **the other passages** — further leads, or the sources of the written answer,
  each with its link.

When nothing matches, the assistant says so: try other words.

<!-- screenshot to add: WideCare AI window with a question, the best passage and its link, and the other passages -->

## Browse the documentation index

**WideCare AI → Documentation** lists the sections the assistant searches, by
language, page and heading, with the link to each page. Search it by word, and
group by language or page.

## Configure the assistant

System administrators open **WideCare AI → Configuration** (or the **Settings**
app, section **WideCare AI**):

- **Answer engine** — documentation search only (the default: no key, no
  network), or a language model, hosted or on a local server, which writes an
  answer from the same passages and cites them.
- **Key** — for a hosted model, paste the provider's key and save. It is never
  shown again; leave the field empty to keep it, or delete it to go back to
  search only. Save, then use the test button to check it.
- **Model** — leave empty to use the usual model of the chosen engine.
- **Written answers per day** — the limit for the whole database; beyond it,
  the assistant falls back to the documentation search.
- **Documentation index** — shows the documentation loaded; reload it after an
  update of the application.

:::{admonition} Privacy
:class: note

The assistant reads only the published documentation. The question asked and
the passages found are the only things sent to a language model provider —
never a resident's data.
:::

## Learn more

- [Getting started](../premiers-pas.md)
- [FAQ](../faq.md)
