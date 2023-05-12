#
# input_orbit.py
# 
# Copyright The PySPIS Contributors.
# 
# This file is part of PySPIS library.
# 
# PySPIS library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# PySPIS library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with PySPIS library. If not, see <http://www.gnu.org/licenses/>.
# 
#


import numpy as np

from kepler_e import *

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
