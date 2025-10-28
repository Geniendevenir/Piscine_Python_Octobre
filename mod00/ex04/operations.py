import sys

def calcul(A, B):
	print(f"Sum:\t\t{A+B}")
	print(f"Difference:\t{A-B}")
	print(f"Product:\t{A*B}")
	if (B == 0):
		print(f"Quotient:\tERROR (division by zero)")
		print(f"Remainder:\tERROR (modulo by zero)")
	else:
		print(f"Quotient:\t{A/B}")
		print(f"Remainder:\t{A%B}")	

def main():
	if (len(sys.argv) <= 1):
		print(f"Usage: python operations.py <number1> <number2>")
		return
	elif (len(sys.argv) == 2):
		print(f"Usage: three arguments needed") 
		return
	elif (len(sys.argv) > 3):
		print(f"AssertionError: too many arguments")
		return
	if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
		print(f"AssertionError: only integers")
		return

	calcul(int(sys.argv[1]), int(sys.argv[2]))

if __name__ == "__main__":
	main()