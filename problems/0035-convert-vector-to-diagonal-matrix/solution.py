import numpy as np

def make_diagonal(x):
	
	# creo la matrice di partenza con tutti 0 poi vado ad aggiunger egli elementi sulla diagonale
    m = np.zeros((len(x), len(x)))

    # popolo la diagonale della matrice
    for i in range(len(x)):
        for j in range(len(x)):

            if i==j:
                m[i,j] = x[i]
    return m
        