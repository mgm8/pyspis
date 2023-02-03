import numpy as np

def inputOrbit(mu, rad):
    data = {"tle": [0, 90, 0, 0.000001, 0, 15.21981]}

    RA0 = data["tle"][0] * rad
    i0 = data["tle"][1] * rad
    w0 = data["tle"][2] * rad
    e0 = data["tle"][3]
    Ma0 = data["tle"][4] * rad
    Ea0 = kepler_E(e0, Ma0)
    TA0 = 2 * np.arctan((((1 + e0) / (1 - e0))**0.5) * np.tan(Ea0 / 2))
    Mm0 = data["tle"][5] / (24 * 3600)
    a0 = (mu**(1 / 3)) / ((2 * np.pi * Mm0)**(2 / 3))
    h0 = (a0 * mu * (1 - e0**2))**0.5

    year = 2023
    month = 3
    day = 21

    T = 2 * np.pi * (a0**1.5) / (mu**0.5)

    return h0, e0, RA0, i0, w0, TA0, year, month, day, T
