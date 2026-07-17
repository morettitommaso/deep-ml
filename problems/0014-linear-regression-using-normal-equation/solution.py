import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	
	X = np.array(X)
	y = np.array(y)

	theta = np.linalg.inv((np.transpose(X) @ X)) @ (np.transpose(X) @ y)

	return np.round(theta, 4).tolist()