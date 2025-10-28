import sys
import string

def text_analyzer(text=""):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if text == "":
		text = input("What is the text to analyze?\n")
	elif not isinstance(text, str):
		print(f"AssertionError: argument is not a string")
		return

	print(f"The text contains", sum(1 for c in text if c.isprintable()), f" printable character(s):")
	print(f"-", sum(1 for c in text if c.isupper()), f"upper letter(s)")
	print(f"-", sum(1 for c in text if c.islower()), f"lower letter(s)")
	print(f"-", sum(1 for c in text if c in string.punctuation), f"punctuation mark(s)")
	print(f"-", sum(1 for c in text if c.isspace()), f"space(s)")
	
		
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"AssertionError: One Argument required")
	text_analyzer(sys.argv[1])
