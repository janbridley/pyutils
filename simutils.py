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
