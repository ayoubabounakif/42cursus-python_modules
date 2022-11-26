from datetime import datetime
from recipe import Recipe

class Book:

    _recipe_types = ['starter', 'lunch', 'dessert']

    def __checkvalidity(self):
        assert self.name.isdigit() == False, f"Name of the book should be a string"

    def __init__(self, name: str):
        self.name = str(name)
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {
            self._recipe_types[0]: [],
            self._recipe_types[1]: [],
            self._recipe_types[2]: []
        }
        self.__checkvalidity()

    def get_recipe_by_name(self, name: str):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for key in self.recipes_list:
            for list_key in range(0, len(self.recipes_list[key])):
                if getattr(self.recipes_list[key][list_key], 'name') == name:
                    return self.recipes_list[key][list_key]
        return None
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        assert recipe_type in self._recipe_types, f"recipe_type doesn't exist"
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        assert isinstance(recipe, Recipe), f"param should be an instance of Recipe class"
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

if __name__ == '__main__':
    b = Book("My seductive recipes")
    print(b.creation_date)
    print(b.last_update)
