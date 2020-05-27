class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        valid = 1
        if name == "":
            valid = 0
        if isinstance(cooking_lvl, int) \
                and (cooking_lvl < 1 or cooking_lvl > 5):
            valid = 0
        if isinstance(cooking_time, int) and cooking_time < 0:
            valid = 0
        if recipe_type not in ["starter", "lunch", "dessert"]:
            valid = 0
        if valid == 1:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = recipe_type
        else:
            exit(1)


    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = " ".join(["Recette:", self.name, "\ncook lvl:", str(
                                                 self.cooking_lvl),
                    "\ntime:", str(self.cooking_time), " minutes",
                        "\ningredients :"])
        tmp = " ".join(self.ingredients)
        txt = " ".join([txt, tmp, self.description, self.recipe_type, "\n"])
        return txt
