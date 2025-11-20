from collections.abc import Iterable
from functools import reduce

def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	if not callable(function_to_apply):
		raise ValueError("First Paremeter should be a function")
	if not isinstance(iterable, Iterable):
		raise ValueError("Second Paremeter should be an iterable")
	it = iter(iterable)
	try:
		accumulator = next(it)
	except StopIteration as exc:
		raise TypeError("ft_reduce() of empty sequence with no initial value") from exc
	for elem in it:
		accumulator = function_to_apply(accumulator, elem)
	return accumulator


lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(reduce(lambda u, v: u + v, lst))
print(ft_reduce(lambda u, v: u + v, lst))