#
# position.py
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

def sv_from_coe(h, e, RA, i, w, TA, it, mu):
    # From the book Orbital Mechanics: For Engineering Students; Howard Curtis
    r_x = (h**2/mu) * (1/(1 + e*np.cos(TA))) * (np.cos(TA)*np.array([[1],[0],[0]]) + np.sin(TA)*np.array([[0],[1],[0]])) # Equation 3
    R3_RA = np.array([[np.cos(RA), np.sin(RA), 0],[-np.sin(RA), np.cos(RA), 0],[0, 0, 1]])
    R1_i = np.array([[1, 0, 0],[0, np.cos(i), np.sin(i)],[0, -np.sin(i), np.cos(i)]])
    R3_w = np.array([[np.cos(w), np.sin(w), 0],[-np.sin(w), np.cos(w), 0],[0, 0, 1]])
    Q = np.dot(R3_w, np.dot(R1_i, R3_RA)).T # Equation 2
    r = np.dot(Q, r_x) # Equation 1
    #...Convert r and v into row vectors:
    state_r = r.T
    return state_r, Q
