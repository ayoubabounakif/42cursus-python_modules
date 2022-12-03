from time import sleep
from book import Book
from recipe import Recipe

if __name__ == '__main__':
    b = Book("My seductive recipes")
    print('Book created:', b.creation_date)
    print('Book updated:', b.last_update)
    
    crumble = Recipe("Crumble" , 1, 25, ["apples", "flour", "sugar"], "dessert", "delicious")
    crumble_two = Recipe("Crumble Two" , 1, 25, ["apples", "flour", "sugar"], "dessert", "delicious")

    print('-------')
    sleep(0.5)
    b.add_recipe(crumble)
    print(b.recipes_list['dessert'])
    print('Book updated: ', b.last_update)
    sleep(1)
    print('-------')
    b.add_recipe(crumble_two)
    print(b.recipes_list['dessert'])
    print('Book updated: ', b.last_update)
    sleep(1)

    print()

    print('--------------||||||||||||||||||||||--------------')
    print('--------------||| Recipe by name |||--------------')
    print('--------------||||||||||||||||||||||--------------')
    recipe = b.get_recipe_by_name('Crumble Two')
    print(recipe.__str__())
    print(recipe.__repr__())
    sleep(1)

    print()

    print('--------------||||||||||||||||||||||--------------')
    print('--------------||| Recipe by type |||--------------')
    print('--------------||||||||||||||||||||||--------------')
    print(b.get_recipes_by_types("dessert")[0])
    # b.get_recipes_by_types("asdasd")
