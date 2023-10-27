import math
import numpy as np


def metropolis(ΔΕ, β, rng):
    """
    Evaluate the metropolis acceptance

    Args:
        ΔΕ (float): Change in energ from initial to new state.
        β (float): 1/kT, where K is the boltzmann constant. Units should match ΔΕ.
        rng (np.random.Generator): Random number generator to draw from.

    Returns:
        (bool): _description_
    """
    pm = math.exp(-β * ΔΕ) if ΔΕ > 0 else 1

    # If pm is 1, always accept
    if pm == 1:
        return True
    else:
        return rng.random() < pm


def make_simple_cubic(natoms, side_length, verbose=False):
    # Initialize a grid for the points
    ngridpoints = math.ceil(pow(natoms, 1 / 3))
    spacing = side_length / (ngridpoints + 1)
    if verbose:
        print("Initial spacing (Ang):", spacing)
    coords = (
        np.array(
            np.meshgrid(
                np.arange(0, ngridpoints, 1),
                np.arange(0, ngridpoints, 1),
                np.arange(0, ngridpoints, 1),
            )
        )
        .reshape(
            3, -1
        )  # Reshape into a (3,natoms) grid to ensure points are paired correctly
        .T  # Transpose to the final (natoms,3) point list
    )
    coords = (
        coords[0:natoms] * spacing
    )  # Filter down to natoms and space out by spacing

    if verbose:
        print(coords[2:12].round(5))
    return coords
