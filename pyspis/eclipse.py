#
# eclipse.py
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

def eclipse(pos, it, r_sun, RE):
    rsat = np.linalg.norm(pos[it])
    rsun = np.linalg.norm(r_sun)

    ## Angle between sun and satellite position vector:
    theta = np.arccos(np.dot(pos[it], r_sun) / rsat / rsun) * 180 / np.pi

    ## Angle between the satellite position vector and the radial to the point of tangency with the earth of a line from the satellite:
    theta_sat = np.arccos(RE / rsat) * 180 / np.pi

    ## Angle between the sun position vector and the radial to the point of tangency with the earth of a line from the sun:
    theta_sun = 90

    if theta_sat + theta_sun <= theta:
        csi = 0 # eclipse
    else:
        csi = 1 # no eclipse

    return csi
