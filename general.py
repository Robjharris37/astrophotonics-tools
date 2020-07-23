"""A list of generally useful functions for astrophotonics."""

import numpy as np


def brewsters_angle(n1, n2):
    """Brewster's angle."""
    return(np.arctan(n2/n1))


def reflection_s(n2, n1, theta_i=0):
    """
    Reflectance for s-polarized light.

    https://en.wikipedia.org/wiki/Fresnel_equations
    Derived using Snell's law

    Inputs:
    n1 : Refractive index of medium 1 (input)
    n2 : Refractive index of medium 2 (output)
    theta_i : Input light angle (radians), measured from normal to
    surface

    Returns:
    R : The percentage of reflected light

    Doctests:
    >>> '%.2f' % reflection_s(1.5,1, 0)
    '0.04'
    """
    top = n1*np.cos(theta_i) - n2 * np.sqrt(1 - (n1/n2 * np.sin(theta_i))**2)
    bot = n1*np.cos(theta_i) + n2 * np.sqrt(1 - (n1/n2 * np.sin(theta_i))**2)
    R_s = (top/bot)**2
    return(R_s)

def reflection_p(n2, n1, theta_i=0):
    """
    Reflectance for s-polarized light.

    https://en.wikipedia.org/wiki/Fresnel_equations
    Derived using Snell's law

    Inputs:
    n1 : Refractive index of medium 1 (input)
    n2 : Refractive index of medium 2 (output)
    theta_i : Input light angle (radians), measured from normal to
    surface

    Returns:
    R : The percentage of reflected light

    Doctests:
    >>> '%.2f' % reflection_p(1.5,1, 0)
    '0.04'
    """
    top = n1 * np.sqrt(1 - (n1/n2 * np.sin(theta_i))**2) - n2*np.cos(theta_i)
    bot = n1 * np.sqrt(1 - (n1/n2 * np.sin(theta_i))**2) + n2*np.cos(theta_i)
    R_s = (top/bot)**2
    return(R_s)


def reflection_normal(n1, n2):
    """
    Fresnel reflection losses for normal incidence.

    For normal incidence no difference between s and p polarisation.

    Inputs:
    n1 : Refractive index of medium 1 (input)
    n2 : Refractive index of medium 2 (output)

    Returns:
    R : The Fresnel

    Doctests:
    >>> '%.2f' % reflection_normal(1.5,1)
    '0.04'
    """
    return((n1-n2)/(n1+n2))**2.


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
    A 2d gaussian.

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
    return g #  .ravel()      - ravel if you want a 1d version for fitting


def circular_mask(pixels,radius, origin="Centre", inside = "True"):
    """
    Return a circular mask.

    Useful to create pupils, circular microlens stuff mode_matching

    Inputs:
    pixels (int) : Number of pixels in the mask, to make x and y different, use [y,x]
    radius : radius of the circle in pixels,
    origin (centre) : Where the circle is located, default in centre, otherwise [y,x].
    inside (True) : Where the pixels are equal to 1, default is inside radius, False means outside.

    Returns:
    mask_array : The array of

    Doctests:

    #TBD - add in angle and allow to be elliptical??
    """
    if (type(pixels)==int):
        x_pixels = y_pixels = pixels
    else:
        y_pixels = pixels[0]
        x_pixels = pixels[1]
    # setup arrays
    if origin == "Centre":
        x_points_array = np.linspace(-x_pixels/2, x_pixels/2, x_pixels+1)
        y_points_array = np.linspace(-y_pixels/2, y_pixels/2, y_pixels+1)
    else:
        x_points_array = np.linspace(0, x_pixels, x_pixels+1)-origin[1]
        y_points_array = np.linspace(0, y_pixels, y_pixels+1)-origin[0]

    x, y = np.meshgrid(y_points_array, x_points_array)
    mask_array = (x**2+y**2)**0.5

    # Remove central obstruction and limit lenses
    if inside == "True":
        mask_array = np.where(mask_array < radius, 1, 0)
    elif inside == "False":
        mask_array = np.where(mask_array > radius, 1, 0)

    return(mask_array)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    if False:
        import matplotlib.pyplot as plt
        n1 = 1    # input glass
        n2 = 1.5  # output air
        angles = np.arange(0, np.pi / 2, 0.001)
        angles_deg = angles.copy()*180/np.pi
        ref_s = reflection_s(n2, n1, angles)
        ref_p = reflection_p(n2, n1, angles)

        plt.plot(angles, ref_s)
        plt.plot(angles, ref_p)
        plt.axvline(brewsters_angle(n1, n2))
        plt.ylim(0, 1)
        plt.show()
