---
modules: [resthome_meal]
---

# Dishes and nutritional values

:::{rh-description}
Describe each dish once in the Resthome catalogue: ingredients, nutritional values per portion, dietary flags, allergens and the textures it can be served in.
:::

:::{rh-faq}
Do I have to enter the calories of every dish by hand?
: No. Add the ingredients with their quantity in grams, then click **Compute Nutrition**: Resthome looks up the values per 100 g in the reference table chosen in the settings and adds them up.

Why does a resident's intake stay at zero?
: The intake is computed from the values **per portion**. Check that the dishes served carry their nutritional values and the right **Portions per Recipe**.

What does Available Textures change?
: It says in which textures the kitchen can prepare the dish. Left empty, the dish is offered in every texture. Resthome uses it to warn when a dish does not suit a resident's texture.
:::

A dish is described **once** in the catalogue, then reused in every menu. Its
nutritional values feed the residents' **intake**, its flags and allergens feed
the **dietary alerts**, and its textures the **texture** check.

## The catalogue

- **Meals → Catalog → Dishes** — the dishes, grouped by category. The filters
  **Diabetic Safe**, **Low Salt**, **Gluten Free**, **Vegetarian** and **Halal**
  narrow the list.
- **Meals → Catalog → Dish Categories** — starter, main course, dessert…, in the
  order of the menu.
- **Meals → Catalog → Products** — the food products used as ingredients, each
  with its **Nutrition /100g** tab.

## Creating a dish

1. In **Meals → Catalog → Dishes**, click **New** and give the dish its name.
2. Choose its **Category**.
3. In **Available Textures**, pick the textures the kitchen can prepare it in;
   leave the field empty if the dish is offered in every texture. See [Food
   textures (IDDSI)](textures.md).
4. Fill in the tabs below, then save.

### Ingredients

List the products of the recipe with their **Quantity** and **Unit of Measure**.
The columns show the contribution of each line (kcal, and optionally protein,
carbohydrates, fat, sugar and salt).

### Nutrition

- **Compute Nutrition** fetches the values per 100 g of each ingredient that has
  none yet from the reference table, switches the unit to grams when needed, and
  adds up the dish totals. The result (found, already known, not found) is
  written in the dish history.
- **Energy (whole recipe)** and **Other** — the totals of the recipe: calories,
  proteins, carbohydrates, fat, sugar, salt. Without ingredients, enter them by
  hand.
- **Per Portion** — **Portions per Recipe** divides the recipe:
  **Kcal / portion** and **Proteins / portion (g)** are what one plate brings.

:::{admonition} The intake comes from the portion
:class: tip

When a resident eats half a plate, Resthome counts half of the **per portion**
values of the dishes served. A dish without values or with the wrong number of
portions gives a wrong intake.
:::

The reference table (**CIQUAL (ANSES - France)** or **NUBEL (Belgium)**) is
chosen in **Nutrition Data Source**: see [Meal and nutrition
settings](../configuration/reglages-repas.md).

### Diets and allergens

- **Dietary Flags** — **Diabetic Safe**, **Low Salt**, **Gluten Free**,
  **Vegetarian**, **Halal**. Resthome compares them with the residents' diets.
- **Contains allergens** — the allergens of the dish.
- **Compatible with diets** — the diets this dish suits.

The flags **Vegetarian**, **Gluten-Free** and **Diabetic-Safe** also appear as
badges on the public menu.

<!-- screenshot to add: dish form with the Ingredients tab and the Compute Nutrition button -->

## Going further

- [Menus, diets and allergies](menus-regimes.md)
- [Food textures (IDDSI)](textures.md)
- [Nutritional monitoring and undernutrition](suivi-nutritionnel.md)
