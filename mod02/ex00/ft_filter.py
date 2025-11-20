from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
	Return:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	# ... Your code here ...
	if function_to_apply is not None and not callable(function_to_apply):
		raise ValueError("First Paremeter should be a function")
	if not isinstance(iterable, Iterable):
		raise ValueError("Second Paremeter should be an iterable")
	return (item for item in iterable if function_to_apply(item) is True)

#Test with correct param 
it = [1, 2, 3, 4]
ft = lambda x: x % 2 == 0


#Real Map
f = filter(ft, it)
print(f)
try:
	for elem in f:
		print(elem)
except ValueError:
	print("Map Error")


#Ft_Map Error
f = ft_filter(ft, it)
print(f)
try:
	for elem in f:
		print(elem)
except ValueError:
	print("Ft_Map Error")