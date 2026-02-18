import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

    a = np.array(a)

    if a.size != new_shape[0] * new_shape[1]:
        return []

    reshaped = a.reshape(new_shape)

    return [
        [int(x) if isinstance(x, float) and x.is_integer() else x
         for x in row]
        for row in reshaped.tolist()
    ]
