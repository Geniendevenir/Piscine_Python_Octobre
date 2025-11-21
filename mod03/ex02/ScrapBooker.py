import numpy as np

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)):
		if not isinstance(array, np.ndarray) or len(dim) < 2 or len(position) <2:
			return None

		rowStart = position[0]
		rowEnd = rowStart + dim[0]

		colStart = position[1]
		colEnd = position[1] + dim[1]

		if rowEnd <= 0 or colEnd <= 0:
			return None
		if rowEnd > array.shape[0] or colEnd > array.shape[1]:
			return None

		return array[rowStart:rowEnd, colStart:colEnd].copy()

	def thin(self, array, n, axis):
		if not isinstance(array, np.ndarray) or n <= 0 or axis not in (0, 1):
			return None
		elif n >= array.shape[axis]:
			return None

		idx = np.s_[n - 1::n]	
		return np.delete(array, idx, axis=axis)

	def juxtapose(self, array, n, axis):
		if not isinstance(array, np.ndarray) or n <= 0 or axis not in (0, 1):
			return None
		return np.concatenate([array] * n, axis=axis)

	def mosaic(self, array, dim):
		if not isinstance(array, np.ndarray) or not isinstance(dim, tuple):
			return None
		elif len(dim) != 2 or dim[0] < 0 or dim[1] < 0:
			return None
		arr = np.concatenate([array] * dim[0], axis=0)
		return np.concatenate([arr] * dim[1], axis=1)

#[3, 2, 1]
#[2, 3, 1]
#[1, 2, 3]
""" arr = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
print(arr)
print(np.shape(arr))
test = ScrapBooker()

print(test.crop(arr, (1, 0), (0, 0))) """
