#
# projection.py
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

def irradiance_field(N_X, pos, r_sun, it, RE):
    F = np.zeros(6)
    for j in range(6):
        F[j] = np.dot(N_X[j,:], r_sun) / np.linalg.norm(r_sun)
        if F[j] < 0:
            F[j] = 0
        else:
            F[j] = F[j]
    return F
