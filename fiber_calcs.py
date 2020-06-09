'''

Module to calculate everything for a fiber

'''

from scipy.integrate import simps
import numpy as np

# Extra import just for this
import matplotlib.pyplot as plt

class V_parameter(object):
    '''
    Houses all the functions that calculate the V parameter for a circular step index fiber
    '''

    def V_from_lmda_a_NA(lmda,a,NA):
        '''
        Calculates the V parameter for a circular step index fiber from

        lmda : wavelength
        a : core radius
        NA : numerical aperture
        '''

        V = 2*np.pi*a*NA/lmda

        return V

class MFD(object):
    '''
    Houses all the functions to calculate
    '''

    def MFD_a_V(a,V):
        '''
        work out MFD at 1/e**2

        a = core radius
        V = V parameter

        '''

        MFD = 2*a*(0.65 + (1.619/V**(3/2))+2.879/(V**6))

        return MFD

class single_mode():
    '''
    Houses all the functions related to calculating a single mode
    '''

    def sm(I_max, r_array, MFD):
        '''
        Plot out a single mode using

        I_max : maximum intensity
        r_array : Input r_array
        MFD : mode field diameter
        '''
        intensity_array = I_max*np.exp(-2 * r_array**2 / (MFD**2))

        return(intensity_array)


def overlap_1d(mode1,mode2, x_arr, offset = 0):
    """
    Calculate the overlap integral in one dimension for two fiber modes.

    Currently only works if both modes are on the same axis.

    Uses Simpson's rule.
    Uses https://www.rp-photonics.com/mode_matching.html as a reference.
    """
    eta_top = (simps((np.conj(mode1)*mode2), x_arr))**2
    eta_bottom = simps(mode1**2, x_arr) * simps(mode2**2, x_arr)

    return(eta_top/eta_bottom)


def overlap_2d(mode1,mode2, x_arr, y_arr, offset = 0):
    """
    Calculate the overlap integral in two dimensions for two fiber modes.

    Currently only works if both modes are on the same axes.

    Uses Simpson's rule.
    Uses https://www.rp-photonics.com/mode_matching.html as a reference.
    """

    #simps([simps(zz_x,x) for zz_x in zz],y) - integrate over 2d

    eta_top = (simps((np.conj(mode1)*mode2), x_arr))**2
        eta_bottom = simps(mode1**2, x_arr) * simps(mode2**2, x_arr)

    return(eta_top/eta_bottom)


if __name__ == "__main__":
    # Run series of tests

    # test overlap integral
    if True:
        mode_array = np.linspace(-10, 10, 1000)
        mode1 = np.exp(-np.power(mode_array, 2.))
        mode2 = np.exp(-np.power(mode_array, 2.))
        plt.plot(mode_array, mode1)
        plt.plot(mode_array, mode2)
        plt.show()
        test = overlap_1d(mode1, mode2, mode_array)
        print(test)
