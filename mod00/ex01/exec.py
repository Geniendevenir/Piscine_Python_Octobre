import sys

def main():
	if len(sys.argv) < 2:
		return 0
	words = sys.argv[1::]
	rev = ""
	for i, element in enumerate(words[::-1]):
		rev += element[::-1].swapcase()
		if i < len(words) - 1:
			rev += " "
	print(rev)
	return 0

if __name__ == "__main__":
	main()

