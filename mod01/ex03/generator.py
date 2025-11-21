import random

def generator(text, sep=" ", option=None):
	if not isinstance(text, str) or not text.isprintable():
		return "ERROR"
	stext = text.split(sep)
	if option is None:
		for w in stext:
			yield w	

	elif option == "shuffle":
		random.shuffle(stext)
		for w in stext:
			yield w	


	elif option == "unique":
		unique_order = []
		for word in text.split(sep):
			if word not in unique_order:
				yield word
			unique_order.append(word)

	elif option == "ordered":
		sorText = sorted(text.split(sep))
		for w in sorText:
			yield w	


	else:
		return "ERROR"
