import numpy as np
from collections.abc import Iterable

class NumpyCreator:
	def from_list(self, lst):
		if not isinstance(lst, list):
			return None
		try:
			result = np.array(lst)
		except:
			return None
		return repr(result)

	def from_tuple(self, tpl):
		if not isinstance(tpl, tuple):
			return None
		try:
			result = np.array(tpl)
		except:
			return None
		return repr(result)

	def from_iterable(self, itr):
		if not isinstance(itr, Iterable):
			return None
		try:
			result = np.array(itr)
		except:
			return None
		return repr(result)

	def from_shape(self, shape, value=0):
		try:
			result = np.full(shape, value)
		except:
			return None
		return repr(result)

	def random(self, shape):
		rng = np.random.default_rng(42)
		return repr(rng.random(shape))

	def identity(self, n):
		return repr(np.eye(n))
