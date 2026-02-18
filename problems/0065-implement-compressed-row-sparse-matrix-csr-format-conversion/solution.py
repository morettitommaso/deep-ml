import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	values = []
	col_idx = []
	row_ptr = [0]  

	for row in dense_matrix:
		for j, element in enumerate(row):
			if element != 0:
				values.append(element)
				col_idx.append(j)
        
		row_ptr.append(len(values))

	return values, col_idx, row_ptr
