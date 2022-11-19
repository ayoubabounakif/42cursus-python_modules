cookbook = {
    'sandwich' : {
        'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
        'meal' : 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients' : ["flour", "sugar", "eggs"],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    }
}

# A series of Helpful Function

def print_cookbook():
    print(list(cookbook))

def print_recipe_details(recipe_name = None):
    if (recipe_name == None):
        recipe_name = input("Please enter a recipe name to get its details:\n>> ")
    print('\n', end="")
    try:
        print('Recipe for {}:'.format(recipe_name))
        print('     Ingredients list: {}'.format(list(cookbook[recipe_name]['ingredients'])))
        print('     To be eaten for {}.'.format(cookbook[recipe_name]['meal']))
        print('     Takes {} minutes of cooking.'.format(cookbook[recipe_name]['prep_time']))
    except KeyError:
        base_error('This recipe is not available on the cookbook')

def delete_recipe(recipe_name = None):
    if (recipe_name == None):
        recipe_name = input("Please enter a recipe name to delete:\n>> ")
    print('\n', end="")
    try:
        del cookbook[recipe_name] 
        print(recipe_name, 'deleted successfuly!')
    except KeyError:
        base_error('This recipe is not available on the cookbook')

def add_recipe():
    try:
        recipe_name = input('Enter a name:\n>> ')
        ingredients = []
        print("\nEnter ingredients:")
        while True:
            inp = input()
            if not inp:
                break
            ingredients.append(inp)
        meal_type = input('\nEnter a meal type:\n')
        prep_time = int(input('\nEnter a preparation time:\n'))
        while prep_time < 0:
            prep_time = int(input('\nPlease enter a non-negative integer:\n'))
        cookbook.update({
        recipe_name: {
            'ingredients': list(ingredients),
            'meal': meal_type,
            'prep_time': prep_time,
        }})
    except Exception as error:
        base_error(error)

def quit_program():
    print('Cookbook closed. Goodbye !')
    exit()

def base_error(error_message = 'Sorry, this option does not exist.'):
    print(error_message)
    options_list()

def options_list():
    print("List of available option:\n \
    1: Add a recipe\n \
    2: Delete a recipe\n \
    3: Print a recipe\n \
    4: Print the cookbook\n \
    5: Quit \
")

def option_chosen(arg):
    switcher = {
        '1': add_recipe,
        '2': delete_recipe,
        '3': print_recipe_details,
        '4': print_cookbook,
        '5': quit_program,
    }
    return switcher.get(arg, base_error)

def main():
    print("Welcome to the Python cookbook !")
    options_list()
    while True:
        option = input('\nPlease select an option:\n>> ')
        func_to_execute = option_chosen(option)
        print('\n', end="")
        func_to_execute()

if __name__ == '__main__':
    main()
    