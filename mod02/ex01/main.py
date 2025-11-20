""" 
CORE MATERIAL:

-> Positional Argument vs Keyword Arguments:
	-> Positional Argument: ft_example(10, "Hello", ("oui", "non"))
	-> Keyword Argument: ft_example(key="value")

-> *args && **kwargs: Python Variadic Arguments
	-> *args: tuple containing all the Positional Argument
	-> **kwargs: Dictionary containing all the Keyword Argument

-> Class Object vs Instance Object
-> ObjectC = Represents a Class Object, In python a class is dynamically allocated, I can access it at runtime modify functions or attributes...

-> Builtin Function getattr():
-> Builtin Function setattr(): Set or Add an attribute at Runtime.
	setattr(obj, "attrName", attrValue)

-> dir(*Class Instance*) = List all attributes of a class

"""


def what_are_the_vars(*args, **kwargs):
	inst = ObjectC()
	x = 0
	for elem in args:
		setattr(inst, f"var_{x}", elem)
		x += 1
	for elem in kwargs:
		setattr(inst, str(elem), kwargs[elem])
	return inst

class ObjectC(object):
	def __init__(self):
		""""""

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)