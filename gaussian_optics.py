"""A module containing fuctions to perform Gaussian optics calculations."""

import numpy as np


def rayleigh_distance(w_0, n, Lmbda):
    """A function that calculates the Rayleigh distance of a gaussian beam.

    Inputs:
    w_0 : beam width
    n : refractive index of medium
    Lmbda : wavelength

    Returns:
    The rayleigh distance of the gaussian beam

    Doctests:
    >>> rayleigh_distance(10, 1, np.pi)
    100.0
    """
    z_r = np.pi * (w_0**2) * n / Lmbda

    return(z_r)


def beam_divergence(Lmbda, n, w_0):
    """Calculates beam divergence in the paraxial case.

    Calculates the beam divergence between the central axis and the 1/e**2
    intensity of the beam
    """
    theta = Lmbda / (np.pi * n * w_0)

    return(theta)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
