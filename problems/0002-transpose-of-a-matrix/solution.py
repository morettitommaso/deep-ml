def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """

    import numpy as np

    a = np.array(a)

    # creo la matrice di output
    m = np.zeros((a.shape[1], a.shape[0]), dtype=object)

    for i in range(a.shape[1]):
        for j in range(a.shape[0]):

            val = a[j, i]

            # converte in int solo se è matematicamente intero
            if isinstance(val, float) and val.is_integer():
                val = int(val)

            m[i, j] = val

    return m.tolist()