"""Module containing fuctions to do gaussian optics calculations."""

import numpy as np


def rayleigh_distance(w_0, n, Lmbda):
    """A function that calculates the Rayleigh distance of a gaussian beam."""
    z_r = np.pi * (w_0**2) * n / Lmbda

    return(z_r)
