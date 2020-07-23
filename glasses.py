"""
Module for glasses calculations.
"""


def sellmeier(lmbda, B1, B2, B3, C1, C2, C3):
    """
    Estimate refractive index of glass with wavelength.

    Using the Sellmeier equation.

    Input:
    lmbda: the Wavelength
    B(1-3) : B coefficients of glass
    C(1-3) : C coefficients of glass

    Returns:
    n : Fitted refractive index
    """
    n_squ = B1*lmbda**2/(lmbda**2-C1) + B2*lmbda**2/(lmbda**2-C2) + B3*lmbda**2/(lmbda**2-C3) + 1

    return(n_squ**0.5)


def hoya(lmbda, A0, A1, A2, A3, A4, A5):
    """
    Estimate refractive index of glass with wavelength.

    Using the Hoya equation.

    Input:
    lmbda : wavelength
    A(1-5) : A coefficients of glass
    
    Returns:
    n : Fitted refractive index
    """
    n_squ = A0 + A1*lmbda**2 + A2*lmbda**-2 + A3*lmbda**-4 + A4*lmbda**-6 + A5*lmbda**-8

    return(n_squ**0.5)
