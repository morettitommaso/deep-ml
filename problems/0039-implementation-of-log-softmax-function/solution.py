import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	
	scores = np.array(scores)
	sum_ = np.log(np.sum(np.exp(scores)))

	return scores - sum_