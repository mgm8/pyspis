#
# ta_from_time.py
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

def ta_from_time(t, e, T, TA0):
    M = 2 * np.pi * t / T
    E = kepler_E(e, M)
    TA = 2 * np.arctan(((1 + e) / (1 - e))**0.5 * np.tan(E / 2)) + TA0
    return TA
