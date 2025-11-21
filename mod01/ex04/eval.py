class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if words is None or coefs is None:
			return print("Error")
		if not isinstance(words, list) or not isinstance(coefs, list):
			return print("Error")	
		if not all(word for word in words if isinstance(word, str)):
			return print("Error")
		if not all(nbr for nbr in coefs if isinstance(nbr, int)):
			return print("Error")
		if len(words) != len(coefs):
			return -1

		return sum(len(a) * b for a, b in zip(words, coefs))
		
	@staticmethod
	def enumerate_evaluate(coefs, words):
		if words is None or coefs is None:
			return print("Error")
		if not isinstance(words, list) or not isinstance(coefs, list):
			return print("Error")	
		if not all(word for word in words if isinstance(word, str)):
			return print("Error")
		if not all(nbr for nbr in coefs if isinstance(nbr, int)):
			return print("Error")
		if len(words) != len(coefs):
			return -1

		return sum(len(words[i]) * nbr for i, nbr in enumerate(coefs))