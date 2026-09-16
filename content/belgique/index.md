# Belgium

:::{rh-description}
What Resthome does that is specific to Belgium: the INAMI dependency allowance, the Katz scale, the eHealth exchanges (eFact, MDA, eAgreement), the institutional allowance and the Belgian annexes.
:::

:::{rh-faq}
Why is there a Belgium section?
: Because everything in it comes from Belgian law or from Belgian institutions: INAMI, AViQ, the health insurers, eHealth. The rest of the documentation — residents, care, meals, accommodation billing — works the same way in any country.

Can Resthome run outside Belgium?
: Yes. The engine is country-neutral: a country pack brings the scale, the identifiers and the billing rules. Belgium is the one documented here; Luxembourg exists in the software.

Where do I find the general billing?
: Under [Billing](../facturation/index.md): periods, supplements, absences and invoices are not Belgian.
:::

:::{toctree}
:hidden:
:::

Everything in this group comes from **Belgian** rules: the allowance paid by the
health insurers, the scale that determines it, the electronic exchanges with
the insurers, and the funding of the facility itself.

The rest of the documentation is **country-neutral** and works the same way
anywhere: residents, admissions, care, meals, the family portal, accommodation
billing and its supplements.

## What is Belgian here

| Subject | What it covers |
| --- | --- |
| [eHealth](../ehealth/index.md) | Insurability (MDA), electronic invoicing (eFact), agreements (eAgreement) |
| [The INAMI package](../facturation/forfait-inami.md) | The dependency allowance paid by the health insurer |
| [The Katz assessment](../residents/katz.md) | The scale that determines the category and the allowance |
| [Institutional allowance](../forfait/index.md) | The AViQ allowance of the facility, from days billed and staff |
| [Expense note (Annexe 12)](../facturation/note-de-frais-annexe12.md) | The Belgian annexe for expenses advanced |
| [Public welfare centre (CPAS)](../facturation/cpas.md) | When a CPAS pays for the resident |
| [The billing journey](../parcours-facturation.md) | Admission → MDA → eAgreement → Katz → eFact → payment |

## The same software elsewhere

Resthome separates the **question** from the **answer**: the engine asks for a
dependency category, a national identifier, a stay type; the country pack
answers with Katz, the NISS, MR/MRS. Another country brings its own pack — and
the neutral pages above do not change.
