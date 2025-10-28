import sys
import random

def guess():
	toGuess = random.randint(1, 99)
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!\n")

	i = 0
	while True:
		inp = input("What's your guess between 1 and 99?\n")
		if (inp == "exit"):
			print("Goodbye!")
			return
		try:
			guess = int(inp)
		except:
			print("That's not a number.")
			continue
		if (guess == toGuess):
			if (toGuess == 42):
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if (i == 0):
				print("Congratulations! You got it on your first try!")
				return
			else:
				print(f"You won in {i} attempts!")
				return
		elif (guess < toGuess):
			print("Too low!")
		elif (guess > toGuess):
			print("Too high!")
		i += 1

if __name__ == "__main__":
	guess()