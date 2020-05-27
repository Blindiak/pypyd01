from book import Book
from recipe import Recipe


tourte = Recipe('tourte', 1, 30, ['pomme', 'poire'], '', 'dessert')
patate_riz = Recipe('patate_riz', 1, 30, ['pa', 'tate', 'riz'], '', 'dessert')
to_print = str(tourte)
print(to_print)
book = Book('lol')
print(book.creation_date)
book.add_recipe(tourte)
book.add_recipe(patate_riz)
book.get_recipe_by_name("tourte")
print(book.last_update)
book.get_recipes_by_types("dessert")
print(book.last_update)
