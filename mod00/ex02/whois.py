import sys

def main():
	if len(sys.argv) < 2:
		return 1

	if (len(sys.argv) > 2):
		print(f"Assertion Error: more than one argument is provided")
		return 1

	if not sys.argv[1].isdigit():
		print(f"AssertionError: argument is not an integer")
		return 1

	number = int(sys.argv[1])
	if number == 0:
		print(f"I'm Zero.")
	elif number % 2 == 0:
		print(f"I'm Even.")
	else:
		print(f"I'm Odd.")

if __name__ == "__main__":
	main()