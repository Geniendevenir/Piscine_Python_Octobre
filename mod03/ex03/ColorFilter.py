import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ImageProcessor import ImageProcessor as ip

class ColorFilter:
	def invert(self, array):
		if not isinstance(array, np.ndarray):
			return None
		inv = array.copy() 
		inv[..., :] = 255 - inv[..., :]
		return inv

	def to_blue(self, array):
		if not isinstance(array, np.ndarray):
			return None

		h, w, _ = array.shape
		red = np.zeros((h, w), dtype=array.dtype)
		green = np.zeros((h, w), dtype=array.dtype)
		blue = array[..., 2]

		return np.dstack((red, green, blue))



	def to_green(self, array):
		if not isinstance(array, np.ndarray):
			return None
		
		green = array.copy()
		green[..., 0] = 0
		green[..., 2] = 0
		return green

	def to_red(self, array):
		if not isinstance(array, np.ndarray):
			return None
		red = array.copy()
		red[..., 1] = 0
		red[..., 2] = 0
		return red

	def to_celluloid(self, array):
		if not isinstance(array, np.ndarray):
			return None

		cell = np.linspace(array.min(), array.max(), num = 5)

		arr = array.copy()
		for i in np.arange(1, cell.size):
			low = cell[i-1]
			high = cell[i]
			mask = (arr >= low) & (arr < high)
			arr[mask] = low
		return arr

	def to_grayscale(self, array, filter, **kwargs):
		if not isinstance(array, np.ndarray):
			return None
		arr = array.copy()

		if filter == "m" or filter == "mean":
			arr.sum()
			r = arr[..., 0]
			g = arr[..., 1]
			b = arr[..., 2]
			print(r)	
		elif filter == "w" or filter == "weight":
			r_weight, g_weight, b_weight = kwargs
			pass
		else:
			return None


test = ip()
arr = test.load("Mandela.jpg")
""" print(arr.shape)
print(f"{repr(arr)}\n")
i = 0
for elem in arr:
	if i == 0:
		print(f"{elem}\n")
	i += 1

print(f"{arr[0][0]}\n") """
col = ColorFilter()
#test.display(col.invert(arr))
#test.display(col.to_blue(arr))
#test.display(col.to_green(arr))
#test.display(col.to_red(arr))
#test.display(col.to_celluloid(arr))
test.display(col.to_grayscale(arr, "m"))