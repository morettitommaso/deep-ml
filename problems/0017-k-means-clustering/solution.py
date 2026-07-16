import numpy as np

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:

	centroids = initial_centroids
	
	for i in range(max_iterations):

		which_cluster = [None]*len(points)

		# assegno ogni osservazione ad un cluster tra quelli iniziali
		for i in range(len(points)):

			# calcolo la dist di ogni punto da ogni centroide
			dist = []
			for j in range(k):
				dist.append(np.linalg.norm(np.array(points[i]) - np.array(centroids[j])))

			# prendo l'indice della distanze minore (ècome assegnare il punto)
			which_cluster[i] = np.argmin(dist)
		
		# aggiorniamo i centrodi dei cluster
		centroids = [None] * k
		for j in range(k):

			# prendo i punti del cluster
			points_j = []
			for i in range(len(points)):
				if which_cluster[i] == j:
					points_j.append(points[i])

			# ricalcolo centroide
			centroids[j] = (np.mean(points_j, axis=0))
		
	centroids = [tuple(c) for c in centroids]
	return centroids