"""
Modes module.

Calculates everything to do with modes for astrophotonics.

- ADD IN SQUARE MODE CALC!

"""

import numpy as np


def calc_modes_circ(chi=3., Lmbda=0.5e-6, d_t=0.7):
    """Mode equation for a circular aperture.

    chi should be in arcsec
    d_t in m
    Lmbda in m

    NOT ACCOUNTING FOR POLARISATION
    """
    chi_rads = (chi/3600.)*np.pi/180.
    M = (np.pi * chi_rads * d_t/(4. * Lmbda))**2.

    return M


def calc_modes_circ_NA(NA=0.14, Lmbda=0.5e-6, a=5e-6):
    """
    Mode equation using fibre, not including polarisation.

    N : Numerical aperture
    Lmbda : Wavelength
    a = radius of fibre core in m

    Not accounting for polarisation
    """
    V = calc_V(NA, Lmbda, a)

    M = V**2/4

    return M


def calc_V(NA=.14, Lmbda=0.5e-6, a=5e-6):
    """
    Calculate the V parameter for a fibre.

    NA = numerical aperture
    Lmbda = Wavelength
    a = core radius
    """
    V = 2*np.pi*a*NA/Lmbda

    return V
