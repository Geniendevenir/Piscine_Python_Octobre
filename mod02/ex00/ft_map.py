from collections.abc import Iterable

def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
	Return:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	if function_to_apply is not None and not callable(function_to_apply):
		raise ValueError("First Paremeter should be a function")
	if not isinstance(iterable, Iterable):
		raise ValueError("Second Paremeter should be an iterable")
	for x in iterable:
		yield function_to_apply(x)

def ft_map2(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
		function_to_apply: a function taking an iterable.
		iterable: an iterable object (list, tuple, iterator).
	Return:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	if function_to_apply is not None and not callable(function_to_apply):
		raise ValueError("First Paremeter should be a function")
	if not isinstance(iterable, Iterable):
		raise ValueError("Second Paremeter should be an iterable")
	return (function_to_apply(x) for x in iterable)


#Test with param 1 not a function
""" it = [1, 2, 3, 4]
ft = 1 """

#Test with param 2 not an iterable
""" it = 1
ft = lambda x: x + 1 """

#Test with correct param 
it = [1, 2, 3, 4]
ft = lambda x: x + 1


#Real Map
m = map(ft, it)
print(m)
try:
	for elem in m:
		print(elem)
except ValueError:
	print("Map Error")


#Ft_Map Error
m = ft_map(ft, it)
print(m)
try:
	for elem in m:
		print(elem)
except ValueError:
	print("Ft_Map Error")
