meals = ['lunch', 'dessert']

dish = {
    'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500
}

for tup in zip(dish.keys(), dish.values()):
    print(tup[0])

cookbook = {
    'sandwich' : {
        'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
        'meal' : meals[0],
        'prep_time': 10,
    },
    'cake': {
        'ingredients' : ["flour", "sugar", "eggs", "tomatoes"],
        'meal': meals[1],
        'prep_time': 60,
    },
    'salad': {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': meals[0],
        'prep_time': 15,
    }
}

# print(cookbook.items())
# pairs = zip(cookbook.keys(), cookbook.values())
# print(list(pairs)[2][1])

# def print_all_recipe_names(cookbook):
#     print(cookbook[0]['ingredients'])

# print_all_recipe_names(cookbook)