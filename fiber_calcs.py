"""Module to calculate everything for a fiber.

TBD:

- overlap intergrals don't deal with complex arrays right now"""

from scipy.integrate import simps
import numpy as np

class V_parameter(object):
    """Houses all the functions that calculate the V parameter for a circular step index fiber."""

    def V_from_lmda_a_NA(lmda, a, NA):
        """
        Calculates the V parameter for a circular step index fiber.

        lmda : wavelength
        a : core radius
        NA : numerical aperture
        """
        V = 2*np.pi*a*NA/lmda

        return V


class MFD(object):
    """Houses all the functions to calculate."""

    def MFD_a_V(a, V):
        """
        Work out MFD at 1/e**2.

        a = core radius
        V = V parameter

        """

        MFD = 2*a*(0.65 + (1.619/V**(3/2))+2.879/(V**6))

        return MFD


class single_mode():
    """Houses all the functions related to calculating a single mode."""

    def sm(I_max, r_array, MFD):
        """
        Plot out a single mode.

        I_max : maximum intensity
        r_array : Input r_array
        MFD : mode field diameter
        """
        intensity_array = I_max*np.exp(-2 * r_array**2 / (MFD**2))

        return(intensity_array)


def overlap_1d(mode1, mode2, x_arr, offset=0):
    """
    Calculate the overlap integral in one dimension for two fiber modes.

    Currently only works if both modes are on the same axis.

    Uses Simpson's rule.
    Uses https://www.rp-photonics.com/mode_matching.html as a reference.
    """
    eta_top = (simps((np.conj(mode1)*mode2), x_arr))**2
    eta_bottom = simps(mode1**2, x_arr) * simps(mode2**2, x_arr)

    return(eta_top/eta_bottom)


def overlap_2d(mode1, mode2, x_arr, y_arr, offset=0):
    """
    Calculate the overlap integral in two dimensions for two fiber modes.

    Currently only works if both modes are on the same axes.

    Uses Simpson's rule.
    Uses https://www.rp-photonics.com/mode_matching.html as a reference.

    integration with help from
    https://stackoverflow.com/questions/20668689/
    integrating-2d-samples-on-a-rectangular-grid-using-scipy
    """
    eta_top = simps([simps(zz_x, x_arr) for zz_x in np.conj(mode1) * mode2], y_arr)**2
    eta_bottom = simps([simps(zz_x, x_arr) for zz_x in mode1**2], y_arr) * simps([simps(zz_x, x_arr) for zz_x in mode2**2], y_arr)

    return(eta_top/eta_bottom)


if __name__ == "__main__":
    # Run series of tests

    # test 1d overlap integral
    if False:
        import matplotlib.pyplot as plt

        mode_array = np.linspace(-10, 10, 1000)
        mode1 = np.exp(-np.power(mode_array, 2.))
        mode2 = np.exp(-np.power(mode_array, 2.))
        plt.plot(mode_array, mode1)
        plt.plot(mode_array, mode2)
        plt.show()
        test = overlap_1d(mode1, mode2, mode_array)
        print(test)

    # test 2d overlap integral
    if True:
        import general
        import matplotlib.pyplot as plt
        
        x = y = np.linspace(-10, 10, 1000)
        mode1 = general.twoD_Gaussian(x, y, 1, 0, 0, 1, 1, 1, 0)
        mode2 = general.twoD_Gaussian(x, y, 1, 0, 0, 1, 1, 1, 0)
        #plt.imshow(mode1 - mode2)
        #plt.show()
        test = overlap_2d(mode1, mode2, x, y)
        print(test)
