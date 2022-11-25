class Recipe:
    recipe_types = ['starter', 'lunch', 'dessert']
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ''):
        self.name = str(name)
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        if recipe_type not in self.recipe_types:
            raise 'recipe_type can be {}, {} or {}'.format(self.recipe_types[0], self.recipe_types[1], self.recipe_types[2])
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.cooking_lvl} - {self.cooking_time} - {self.ingredients} - {self.recipe_type} - {self.description}"

if __name__ == '__main__':
    tourte = Recipe('Mamamia', 5, 10, ['tomatoes', 'botatoes', 'bitches'], 'luncssh', 'walou')
    # print(tourte)


        

    
    

