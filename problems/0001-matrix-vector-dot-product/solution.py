def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
	import numpy as np

	# ottengo il numero di colonne e della matrice e del vettore
	m_col = len(a[0])
	v_row = len(b)

	if m_col != v_row:
		return -1

	# creo la matrice per il risultato
	out = np.zeros(len(a))
	
	# la popolo
	for i in range(len(a)):
		out[i] = np.dot(a[i], b)

	return [int(x) if isinstance(x, float) and x.is_integer() else x
            for x in out]