import datetime
from recipe import Recipe

class Book:
	def __init__(self, name, last_update, creation_date, recipe_list):
		if type(name) != str:
			print("ERROR: Book name should be a valid string")
			return
		if type(last_update) != datetime:
			print("ERROR: Book Last Update should be a datetime object")
			return
		if type(creation_date) != datetime:
			print("ERROR: Book Creation Date should be a datetime object")
			return
		if type(recipe_list) != dict:
			print("ERROR: Book Recipe List should be a dictionary")
			return
		if list(recipe_list) != {"starter", "lunch", "dessert"}:
			print("ERROR: Book Recipe List should have 3 keys: 'starter', 'lunch' and 'dessert'")
			return

		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipe_list = recipe_list

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name text{name} and returns the instance"""
		if type(name) != str:
			print("ERROR: Get Recipe (Name) fuction needs a valid name string")
			return
		for type, recipes in self.recipe_list.items():
			for recipe in recipes:
				if recipe.name == name:
					return self.recipe_list[name]

	def get_recipes_by_types(self, recipe_type):
		"""Gets all recipes names for a given recipe_type """
		if type(recipe_type) != str or recipe_type not in {"starter", "lunch", "dessert"}:
			print("ERROR: Get Recipe (Types) fuction needs a valid type string")
			return
		for type, recipes in self.recipe_list.items():
			for recipe in recipes:
				print(recipe.name)

	def add_recipe(self, recipe):
		"""Adds a recipe to the book and updates last_update"""
		if type(recipe) != Recipe or recipe.recipe_type not in {"starter", "lunch", "dessert"}:
			print("Error: To add a Recipe it needs to BE a Recipe")
			return
		self.recipe_list[recipe.recipe_type].append(recipe)	
		