import sys
import string

def filter_word():
	if len(sys.argv) != 3:
		print("ERROR")
		return
	S = sys.argv[1].split(" ")
	try:
		N = int(sys.argv[2])
	except:
		print("ERROR")
		return
	print("[", end="")
	i = 0
	for w in S:
		w_clean = "".join(c for c in w if c not in string.punctuation)
		if len(w_clean) > N:
			if (i > 0):
				print(", ", end="")
			print(f"\'{w_clean}\'", end="")
			i += 1
	print("]")

if __name__ == "__main__":
	filter_word()