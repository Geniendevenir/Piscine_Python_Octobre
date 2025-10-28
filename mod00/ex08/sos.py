import sys
import string

MORSE = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-...",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    " ":"/"
}

def strToMorse():
	if len(sys.argv) <= 1:
		return
	elif len(sys.argv) > 2:
		s = " ".join(w for w in sys.argv[1::])
	else:
		s = sys.argv[1]
	for char in s:
		if char not in string.ascii_letters and char not in string.digits and char not in string.whitespace:
			print("ERROR")
			return
	s_up = s.upper()
	i = 0
	for c in s_up:
		if i > 0:
			print(" ", end="")
		print(f"{MORSE[c]}", end="")
		i += 1
	print("\n", end="")

if __name__ == "__main__":
	strToMorse()