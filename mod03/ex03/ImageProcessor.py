import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor:
	def load(self, path):
		if not isinstance(path, str):
			raise TypeError("Invalid Type")
		try:
			arr = mpimg.imread(path)
		except FileNotFoundError:
			return None
		except PermissionError:
			return None
		
		return arr

	def display(self, array):
		if not isinstance(array, np.ndarray):
			print("Must be a valid nparray")
			return

		plt.imshow(array)
		plt.axis("off")
		plt.show()