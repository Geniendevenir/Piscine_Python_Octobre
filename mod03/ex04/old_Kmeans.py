import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import random
# 4 clusters: Venus, Earth, Marth, Belt
# 1 

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):

		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids

	def fit(self, X):
		#1: Randomly take ncentroid random points among X.validIndex:
		for i in range(self.ncentroid):
			self.centroids.append(random.randint(0, X.shape[0]))
		print(self.centroids)

		#2: Repeat Kmean algorithm max_iter time
		for i in range(self.max_iter):
			labels = np.zeros(X.shape[0])

			#2: Kmean algorithm
			for i, x in enumerate(X):
				if i not in self.centroids:
					dists = []
					#For each data points calculate its distance compared to each centroids
					for elem in self.centroids:
						dists.append((x[0] - X[elem][0]) ** 2 + (x[1] - X[elem][1]) ** 2 + (x[2] - X[elem][2]) ** 2)

					#map the index of lowest dist with data point
					lowestDist = min(dists)
					lowestDistIndex = dists.index(lowestDist)
					labels[i] = self.centroids[lowestDistIndex]
			#For each centroid Calculate the Mean Dist between its points
			newCentroid = []
			for cenIndex in self.centroids:
				j = 0
				meanCentroid = 0
				for i, x in enumerate(X):
					if labels[i] == cenIndex and i not in self.centroids:
						meanCentroid += i
						j += 1
				if j > 0:
					meanCentroid /= j
				newCentroid.append(int(meanCentroid))
			#Get the index represented by the result (mean), it becomes the new centroid
			self.centroids.clear()
			self.centroids = newCentroid	
			print(self.centroids)

	def predict(self, X):
		pass

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
