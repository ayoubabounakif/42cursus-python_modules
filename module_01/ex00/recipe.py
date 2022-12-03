class Recipe:
    def __checkvalidity(self):
        recipe_types = ['starter', 'lunch', 'dessert']
        assert self.name.isdigit() == False, f"name of the recipe should be a string"
        assert isinstance(self.cooking_lvl, int), f"cooking_lvl should be an integer"
        self.cooking_lvl = int(self.cooking_lvl)
        assert (self.cooking_lvl >= 1 and self.cooking_lvl <= 5), f"cooking_lvl should range from 1 to 5"
        assert self.cooking_time >= 0, f"cooking_time should be a positive number"
        assert len(self.ingredients) > 0, f"ingredients should not be empty"
        for i in self.ingredients:
            assert str(i).isdigit() == False, f"ingredients should be a list of strings."
        assert self.description.isdigit() == False, f"description should be a string."
        assert self.recipe_type in recipe_types, f"recipe_type can be {recipe_types[0]}, {recipe_types[1]} or {recipe_types[2]}"

    def __init__(self, name, cooking_lvl: int, cooking_time: int, ingredients, recipe_type, description = ''):
        self.name = str(name)
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = str(recipe_type)
        self.description = str(description)
        self.__checkvalidity()

    def __str__(self):
        s = f"Name: {self.name}\nCooking Level: {self.cooking_lvl}\nCooking Time: {self.cooking_time}\nIngredients: {self.ingredients}\nRecipe Type: {self.recipe_type}\nDescription: {self.description}"
        return s

    def __repr__(self):
        cls = self.__class__
        return f"<{cls.__module__}.{cls.__qualname__} object at {id(self)}>"

if __name__ == '__main__':
    try:
        tourte = Recipe("cooki", 1, 10, ["dough", "sugar", "love"], "dessert", "deliciousness incarnate")
    except Exception as error:
        print(error)
