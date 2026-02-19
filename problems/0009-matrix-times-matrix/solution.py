def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    import numpy as np
    a = np.array(a)
    b = np.array(b)

    # controllo la compatibilità delle metrici
    if (a.shape[1] != b.shape[0]):
        return -1

    # creo la matrice di output
    c = np.zeros((a.shape[0], b.shape[1]))

    for i, row in enumerate(a): # per ogni riga di a
        
        for j in range(b.shape[1]): # prende ogni colonna di b
            sum_ = 0

            for k in range(b.shape[0]): # ed esegue il prodotto elemento^2 
                sum_ += (row[k]*b[k, j])
            c[i,j] = sum_

            
    result = []
    for row in c:
        new_row = []
        for val in row:
            if val.is_integer():
                new_row.append(int(val))
            else:
                new_row.append(val)
        result.append(new_row)

    return result