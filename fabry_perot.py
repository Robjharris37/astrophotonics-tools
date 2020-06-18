"""Putting together calculations for a fiber Fabry-Perot.

Largely drawn from https://en.wikipedia.org/wiki/Fabry%E2%80%93P%C3%A9rot_interferometer


"""

import scipy.constants
import numpy as np


def FSR_freq(l):
    """
    Calculate the free spectral range (frequency) of a Fabry-Perot etalon.

    Inputs:
    l : the length of cavity

    Returns:
    The free spectral range of the cavity

    Doctests:
    >>> FSR_freq(1)
    149896229.0
    >>> FSR_freq(10)
    1498962290.0

    """
    return (scipy.constants.c/2.*l)


def FSR_wavelength(Lmbda_0, n_g, l, theta=0):
    """Calculate the free spectral range of a Fabry-Perot etalon."""
    return(Lmbda_0**2/(2*n_g*l*np.cos(theta)))


def calc_finesse(R1, R2=None):
    """Estimate the finesse of the system with two mirrors of equal reflectivity.

    Inputs:
    R1 : the reflectivity of M1
    R2 (default = None) : the reflectivity of M2, if not selected, defaults to R1

    Returns:
    The Finesse of the cavity.

    Doctests:
    >>> '%.2f' % calc_finesse(.8)
    '14.05'

    Cite : R. Paschotta, article on 'finesse' in the RP Photonics Encyclopedia, accessed on 2020-06-18
    """
    if R2 is None:
        R2 = R1

    F = np.pi * (R1*R2)**.25 / (1 - (R1*R2)**0.5)

    return(F)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Test free spectral range equation
    # if True:
    #    import matplotlib.pyplot as plt
