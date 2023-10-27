import numpy as np


def del1d(arr1d, index):
    """Remove a single array element from an array.

    This is similar to np.delete, but is faster and can only remove 1 element.
    """
    mask = np.ones(len(arr1d), dtype=int)
    mask[index] = 0
    return arr1d[mask]
