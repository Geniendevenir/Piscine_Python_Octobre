import datetime
from book import Book
from recipe import Recipe

def main():
	"""Test Parser"""
	print("I - TEST PASER (Recipe)")
	print("Test 1: Invalid name")
	Recipe(55, 2, 10, ["pate", "tomates", "fromage"], "lunch", "")

	print("Test 2: Invalid cooking level (< 5)")
	Recipe("Pate", -5, 10, ["pate", "tomates", "fromage"], "lunch", "")

	print("Test 3: Invalid cooking level (string)")
	Recipe("Pate", "Yes", 10, ["pate", "tomates", "fromage"], "lunch", "")

	print("Test 4: Invalid cooking time (string)")
	Recipe("Pate", 2, "Yes", ["pate", "tomates", "fromage"], "lunch", "")

	print("Test 5: Invalid ingredients (int)")
	Recipe("Pate", 2, 10, 6, "lunch", "")

	print("Test 6: Invalid ingredients (str)")
	Recipe("Pate", 2, 10, "pate", "lunch", "")

	print("Test 7: Invalid Recipe Type (str)")
	Recipe("Pate", 2, 10, ["pate", "tomates", "fromage"], "5", "")

	print(f"{'*':<10}")
	print("II - TESTS")
	pate = Recipe("Pate", 2, 10, ["pate", "tomates", "fromage"], "lunch", "")

if __name__ == "__main__":
	main()