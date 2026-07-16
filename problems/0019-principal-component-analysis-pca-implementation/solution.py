import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """

    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized = (data - mean) / std

    mat_cov = np.cov(standardized, rowvar=False)

    # trovo autovalori
    eigenvalues, eigenvectors = np.linalg.eigh(mat_cov)

    # prendo i maggiori k autovalori 
    idx = np.argsort(eigenvalues)[::-1]

    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # top_k_eigenvalues = eigenvalues[:k]
    top_k = eigenvectors[:, :k]

    # Sign convention
    for i in range(k):
        vec = top_k[:, i]
        for val in vec:
            if abs(val) > 1e-10:
                if val < 0:
                    top_k[:, i] *= -1
                break

    return np.round(top_k, 4)
    
