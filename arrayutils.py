import math
import numpy as np


def norm1d(v1d):
    """
    Compute the norm of a one dimensional vector.

    Args:
        v1d (np.array): Input vector

    Returns:
        norm1d: Magnitude of the vector (scalar)
    """
    return math.sqrt(np.square(v1d).sum())


def norm2d(arr2d):
    """
    Take the norm across the first axis of a 2d array.

    Args:
        arr2d (np.array): Array of values (typically vector rij or similar) (N,2)

    Returns:
        np.array: (N,) array of norms
    """

    return np.sqrt(np.einsum("ij,ij->i", arr2d, arr2d))


def inner1d(arr2d_0, arr2d_1):
    """
    Take the dot product along the first axis of a 2d array.

    Args:
        arr2d_0 (np.array): Array of values (N,2)
        arr2d_1 (np.array): Array of values (N,2)

    Returns:
        np.array: (N,) array of dot products
    """

    return np.sqrt(np.einsum("ij,ij->i", arr2d_0, arr2d_1))
