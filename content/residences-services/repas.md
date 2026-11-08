---
howto_auto: true
modules: [serviced_living_meal]
sectors: [rs]
---

# Meals in a residence

:::{rh-description}
Serve and bill the meals residents of a serviced residence take at the residence: the meals chosen on their record, the couvert laid by the kitchen, the meals served billed on the month.
:::

:::{rh-faq}
Is a couvert laid for every resident of the residence?
: No. A resident of a residence eats at home unless they say otherwise: a couvert is laid only for the meal types listed in **Meals taken here** on their record.

How is a meal billed?
: Each meal marked as served during the month is billed on the resident's next invoice, one line per meal type, at the price of the product linked to that meal type.

Which meals are billed?
: Only the meal types that have a product in **Billed in serviced living as**. A meal type without one is served but never billed.

The meal is included in the price. Is it billed anyway?
: No. When its product is listed in **Included in the price** on the residence, it is not billed on top.
:::

A resident of a residence lives at home: they eat in their flat unless they come
down to the restaurant. The **Meals** application serves them like any other
resident, but only for the meals they take here, and the meals served are billed
with the month.

## 1. Link each meal type to a product

In **Meals → Configuration → Meal Types**, fill in **Billed in serviced living
as** for each meal type a resident of the residence may pay: lunch, dinner…
The product carries the price, the VAT and the income account. Leave it empty
for a meal type that is never billed.

## 2. Say which meals the resident takes here

On the resident's record, fill in **Meals taken here** with the meal types they
take at the residence. The rest of the time, no couvert is laid for them.

<!-- screenshot to add: the resident's record with the Meals taken here field next to the home nurse -->

## 3. Serve the meal

Nothing changes for the kitchen and the floor: confirming the menu lays the
couverts of the day, and the meal round records who was **Served**. See
[The meal distribution round](../repas/distribution.md).

Nobody asks how much a resident of a residence ate, unless the residence follows
their care.

## 4. Bill the month

At the month's generation, the meals **Served** during the month are billed on
the resident's invoice: one line per meal type, with the number of meals, at the
price of the meal type's product. See [Billing a residence](facturation.md).

:::{admonition} Included meals
:class: note

When the price of the residence already covers a meal, list its product in
**Included in the price** on the residence: the meal is still served, but never
billed on top.
:::

## Going further

- [The meal distribution round](../repas/distribution.md)
- [Billing a residence](facturation.md)
