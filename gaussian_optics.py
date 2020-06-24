"""A module containing fuctions to perform Gaussian optics calculations."""

import numpy as np


def beam_divergence(Lmbda, n, w_0):
    """Calculate beam divergence in the paraxial case.

    Calculates the beam divergence between the central axis and the 1/e**2
    intensity of the beam
    """
    theta = Lmbda / (np.pi * n * w_0)

    return(theta)


def fwhm_to_1e2(fwhm):
    """Convert FWHM to 1/e**2."""
    return(fwhm / np.sqrt(2 * np.ln(2)))


def radius_of_curvature(z, z_r):
    """Radius of curvature of a gaussian beam."""
    return(z * (1 + (z_r/z)**2))


def rayleigh_distance(w_0, n, Lmbda):
    """Calculate the Rayleigh distance of a gaussian beam.

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


def beam_size(w_0, z, z_r):
    """Calculate the 1/e**2 value (r).

     at a point along an expanding gaussian beam
    measured from the focus.

    """
    w = w_0 * np.sqrt(1 + (z/z_r)**2)
    return(w)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
