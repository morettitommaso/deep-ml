import numpy as np
import scipy.stats as sp

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    # calcolo la std cosi che l aposso elevare al quadrato
    # e sprecare meno calcoli
    std_ = np.std(data)
    
    my_dict = {
        'mean': np.mean(data), 
        'median': np.median(data), 
        'mode': (sp.mode(data)).mode, 
        'variance': std_**2, 
        'standard_deviation': std_,
        '25th_percentile': q1,
        '50th_percentile': np.percentile(data, q=50), 
        '75th_percentile': q3, 
        'interquartile_range': q3-q1
    }

    return my_dict