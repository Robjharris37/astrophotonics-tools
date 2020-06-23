"""A list of generally useful functions for astrophotonics."""

import numpy as np

def fresnel_reflection_s(R1,R2):
    """
    Fresnel reflection losses for s polarisation.


    """
    # TBD

def fresnel_reflection_p(R1,R2):
    """
    Fresnel reflection losses for p polarisaion.


    """


def reflection_normal(n1,n2):
    """
    Fresnel reflection losses for normal incidence.

    For normal incidence no difference between s and p polarisation.

    Inputs:
    n1 : Refractive index of medium 1
    n2 : Refractive index of medium 2

    Returns:
    R : The Fresnel

    Doctests:
    >>> reflection_normal(1.5,1)
    '0.04'
    """
    return((n1-n2)/(n1+n2)**2)


def twoD_Gaussian(x, y, amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
    """
    Function to create a 2d gaussian.

    Source code taken from
    https://stackoverflow.com/questions/21566379/fitting-a-2d-gaussian-function-using-scipy-optimize-curve-fit-valueerror-and-m

    Inputs:
    x : the array of x
    y : the array of y
    amplitude : The amplitude
    xo : x center
    yo : y center
    sigma_x : Standard deviation of x
    sigma_y : Standard deviation of y
    theta : angle
    offset : offset in position

    Returns:

    Doctests:

    """
    x, y = np.meshgrid(x, y)
    xo = float(xo)
    yo = float(yo)
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    g = offset + amplitude*np.exp(- (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo)
                            + c*((y-yo)**2)))
    return g # .ravel()      - ravel if you want a 1d version for fitting
