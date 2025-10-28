class Recipe:
	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, description=""):
		if type(name) != str:
			print("ERROR: Name should be a valid string")
			return	
		if not cooking_lvl.isdigit() or int(cooking_lvl) not in range(5):
			print("ERROR: Cooking_lvl should be an int between 1 and 5")
			return	
		if not cooking_time.isdigit() or int(cooking_time) < 0:
			print("ERROR: Cooking_time should be a valid positive int")
			return	
		if type(ingredients) != list:
			print("ERROR: Ingredients should be a list")
			return	
		else:
			for element in list:
				if not element.isalpha():
					print("ERROR: Ingredients should be valid alpha string")
					return	
		if type(recipe_type) != str or recipe_type not in {"starter", "lunch", "dessert"}:
			print("ERROR: Recipe Type should be either: starter, lunch or dessert")
			return	
		if description.isalpha():
			print("ERROR: Description should be empty or a valid alpha string")
			return	

		self.name = name
		self.cooking_lvl = int(cooking_lvl)
		self.cooking_time = int(cooking_time)
		self.ingredients = ingredients
		self.recipe_type = recipe_type
		self.description = description	

	def __str__(self):
		"""Returns the string to print with the recipe’s info"""
		txt = ""
		txt += f"Recipe Name:\t{self.name}"
		txt += f"Cooking Level:\t{self.cooking_lvl}"
		txt += f"Cooking Time:\t{self.cooking_time}"
		txt += f"Ingredients:\t{self.ingredients}"
		txt += f"Recipe Type:\t{self.recipe_type}"
		txt += f"Desciption:\t{self.description}"
		return txt
	
