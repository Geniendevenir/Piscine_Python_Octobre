import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
# 4 clusters: Venus, Earth, Marth, Belt
# 1 

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):

		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids

	def fit(self, X):
		indices = np.random.choice(X.shape[0], self.ncentroid, replace=False)
		self.centroids = X[indices].copy()

		for _ in range(self.ncentroid):
			labels = np.zeros(X.shape[0], dtype=int)
			for i, x in enumerate(X):
				dists = np.sum((self.centroids - x) ** 2, axis=1)
				labels[i] = np.argmin(dists)

		for k in range(self.ncentroid):
			cluster_points = X[labels == k]
			if len(cluster_points) > 0:
				self.centroids[k] = cluster_points.mean(axis=0)

	def predict(self, X):
		for _ in range(self.ncentroid):
			labels = np.zeros(X.shape[0], dtype=int)
			for i, x in enumerate(X):
				dists = np.sum((self.centroids - x) ** 2, axis=1)
				labels[i] = np.argmin(dists)
		return labels.reshape(X.shape[0], 1)


if __name__ == "__main__":

	if len(sys.argv) != 4:
		print("Invalid number of argument")
		exit(1)

	_, path, ncentroid, max_iter = sys.argv
	max_iter = int(max_iter)
	ncentroid = int(ncentroid)
	print(path)

	if max_iter <= 0:
		print("Invalid argument")
		exit(1)	
	elif ncentroid <= 0:
		print("Invalid argument")
		exit(1)	

	K = KmeansClustering(max_iter, ncentroid)
	with open(path, newline="") as f:
		reader = csv.reader(f)
		data = list(reader)
		arr = np.array(data)[1:, 1:].astype(float)
		K.fit(arr)
		p = K.predict(arr)
		print(repr(p))
		
		fig = plt.figure()
		ax = fig.add_subplot(111, projection="3d")
		ax.scatter(arr[:, 0], arr[:, 1], arr[:, 2], c=p.flatten(), cmap="tab10")

		ax.set_xlabel("Height")
		ax.set_ylabel("Weight")
		ax.set_zlabel("Bones_Density")

		plt.show()

