import numpy as np

def explained_variance_ratio(X):
    """
    Calculate the explained variance ratio for PCA.
    
    Args:
        X: Data matrix of shape (n_samples, n_features)
    
    Returns:
        List of explained variance ratios sorted in descending order
    """

    # centra direttamente la funzione cov 
    cov = np.cov(X, rowvar=False)

    # trovo autovalori
    eigenvalues, _ = np.linalg.eigh(cov)

    eigenvalues = eigenvalues[::-1]

    ratios = eigenvalues / np.sum(eigenvalues)

    return (ratios)