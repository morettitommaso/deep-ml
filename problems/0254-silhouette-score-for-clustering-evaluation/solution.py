import numpy as np
import math

def silhouette_score(X: np.ndarray, labels: np.ndarray) -> float:
	"""
	Calculate the Silhouette Score for clustering evaluation.
	
	X: shape (n_samples, n_features) - data points
	labels: shape (n_samples,) - cluster label for each point
	
	Returns: silhouette score (float between -1 and 1)
	"""

	unique = np.unique(labels)

	if len(unique) == 1:
		return 0.0

	if len(unique) == len(X):
		return 0.0

	sils = []

	for i in range(len(X)):
		
		# calcolo a_i
		label_cluster_i = labels[i]

		# ottengo il cluster i
		cluster_i = []
		for k in range(len(X)):
			if labels[k] == label_cluster_i:
				cluster_i.append(X[k])
		
		# calcolo distanze tra il punto e tuttgli gli altri
		dists = []
		for h in range(len(cluster_i)):
			if not np.array_equal(cluster_i[h], X[i]):
				dists.append(math.dist(cluster_i[h], X[i]))
		a_i = np.mean(dists)

		# calcolo b_i
		unique = list(dict.fromkeys(labels))
		dists_clusters = []

		for idx_cluster,j in enumerate(unique):

			if idx_cluster == label_cluster_i:
				continue

			dists = []

			# prendo tutti punti del cluster j
			cluster_j = []
			for k in range(len(X)):
				if labels[k] == j:
					cluster_j.append(X[k])
			
			# calcolo la distanza media tra il punto ed il cluster j
			for h in range(len(cluster_j)):
				if not np.array_equal(cluster_j[h], X[i]):
					dists.append(math.dist(cluster_j[h], X[i]))

			dists_clusters.append(np.mean(dists))

		b_i = min(dists_clusters)
		sil_i = (b_i - a_i) / max(a_i, b_i)
		sils.append(sil_i)

	return round(np.mean(sils), 4)