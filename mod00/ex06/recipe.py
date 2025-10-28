def cook():
	cookbook = { 
		"Sandwich" : {
			"Ingredients": (["ham"], ["bread"], ["cheese"], ["tomatoes"]), 
   			"Meal": "lunch",
			"Prep_Time": 10
		},
		"Cake" : {
			"Ingredients": (["flour"], ["sugar"], ["eggs"]), 
   			"Meal": "desert",
			"Prep_Time": 60
		},
		"Salad" : {
			"Ingredients": (["avocado"], ["arugula"], ["tomatoes"], ["spinach"]), 
   			"Meal": "lunch",
			"Prep_Time": 15
		}
	}	
	return cookbook

def printCookbook(cookbook):
	print(list(cookbook))
	print("\n")

def printRecipe(cookbook):
	recipeName = input(f"Please enter a recipe name to get its details:\n")
	try:
		recipe = cookbook[recipeName]
	except:
		print("Error: Recipe doesnt exist")
		return
	print(f"Recipe for {recipeName}:")
	print(f"\tIngredients list: {recipe['Ingredients']}")
	print(f"\tTo be eaten for {recipe['Meal']}")
	print(f"\tTakes {recipe['Prep_Time']} minutes of cooking.")
	print("\n")

def deleteRecipe(cookbook):
	while True:
		toDelete = input(f"Which recipe would you like to delete?:\n\n")
		try:
			del cookbook[toDelete]
			break
		except:
			print("Error: Couldnt Delete Recipe - No Recipe of that name exist")

def addRecipe(cookbook):
	name = input("Enter a name:\n")
	ingredient = input("Enter ingredients:\n").split(', ')
	meal = input("Enter a meal type:\n")
	while True:
		try:
			prep_time = int(input("Enter a preparation time:\n"))
			break
		except:
			print(f"Preparation time must be a positive integer")
	cookbook[name] = {
		"Ingredients": ingredient, 
		"Meal": meal,
		"Prep_Time": prep_time 
	}

def main():
	cookbook = cook()
	print(f"Welcome to the Python Cookbook !")
	while True:
		print(f"List of available options:")
		print(f"\t1: Add a recipe")
		print(f"\t2: Delete a recipe")
		print(f"\t3: Print a recipe")
		print(f"\t4: Print the cookbook")
		print(f"\t5: Quit")
		while True:
			option = input(f"Please select an option:\n\n")
			if not option.isdigit():
				print("Sorry the option does not exist")
			break
		if (option == "1"):
			addRecipe(cookbook)
		elif (option == "2"):
			deleteRecipe(cookbook)
		elif (option == "3"):
			printRecipe(cookbook)
		elif (option == "4"):
			printCookbook(cookbook)
		elif (option == "5"):
			print("Cookbook closed. Goodbye !")
			return

if __name__ == "__main__":
	main()