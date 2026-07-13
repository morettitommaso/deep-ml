import numpy as np

def fn(seed, mean, std, n, bins):
    # return (counts, edges) as plain Python lists

    np.random.seed(seed)
    sample = np.random.normal(loc=mean, scale=std, size=n)

    counts = list()

    if isinstance(bins, int):
        _, bins = np.histogram(sample, bins=bins)
    
    for i in range(len(bins)-1):

        low = bins[i]
        high = bins[i+1]

        nums = len([j for j in sample if (j>=low and j<=high)])
        counts.append(nums)

    return (counts,  [float(x) for x in bins])