"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units
for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.

Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

    Метод set() манипулирует элементами данных итерации до отсортированного набора элементов данных,
не принимая во внимание порядок элементов.
    Итерируемая распаковка, которая была представлена как часть PEP 3132.
 *l, = dict, где l — это пустой список, dict -  словарь.
"""


def cakes(recipe, available, l=[0]):
    *x, = recipe
    *y, = available
    if set(x).issubset(y):
        l = [available[key] // recipe[key] for key, value in recipe.items()]
    return min(l)



recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available = {'sugar': 500, 'flour': 2000, 'milk': 2000}

# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}

# recipe = {'crumbles': 2, 'eggs': 2, 'oil': 70}
# available = {'nuts': 7137, 'chocolate': 3827, 'milk': 699, 'cream': 264, 'crumbles': 9695, 'sugar': 1915, 'cocoa': 9451, 'pears': 3103, 'eggs': 6659, 'apples': 4575}


print(cakes(recipe, available))
