from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {'starter': {}, 'lunch': {}, 'dessert': {}}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if name in self.recipes_list['starter']:
            print(self.recipes_list['starter'][name])
        elif name in self.recipes_list['lunch']:
            print(self.recipes_list['lunch'][name])
        elif name in self.recipes_list['dessert']:
            print(self.recipes_list['dessert'][name])
        else:
            print("This recipe does not exist")
        tmp = self.recipes_list['dessert']
        print(tmp[name])

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        for r in self.recipes_list[recipe_type]:
            print(str(r))

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) is Recipe:
            self.recipes_list[recipe.recipe_type][recipe.name] = recipe
            self.last_update = datetime.now()
        else:
            print("ERROR")
