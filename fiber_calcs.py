'''

Module to calculate everything for a fiber

'''

import numpy as np

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
