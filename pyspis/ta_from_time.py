import numpy as np

from kepler_e import *

def ta_from_time(t, e, T, TA0):
    M = 2 * np.pi * t / T
    E = kepler_E(e, M)
    TA = 2 * np.arctan(((1 + e) / (1 - e))**0.5 * np.tan(E / 2)) + TA0
    return TA
