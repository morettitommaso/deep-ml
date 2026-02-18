def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	
	import numpy as np

	matrix = np.array(matrix)

	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			matrix[i,j] = matrix[i,j]*scalar	

	return matrix