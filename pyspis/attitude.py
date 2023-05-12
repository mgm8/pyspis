#
# attiude.py
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

def attitude(h, e, RA, i, w, TA,it,Q,T,r_sun,t):
    ## Equation 6
    n = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    
    Rspin1 = np.array([[np.cos(TA), np.sin(TA), 0], [-np.sin(TA), np.cos(TA), 0], [0, 0, 1]])
    th = -0 * 1 * (2 * np.pi * t) / T # theta*
    
    Rspin2 = np.array([[1, 0, 0], [0, np.cos(th), np.sin(th)], [0, -np.sin(th), np.cos(th)]])
    Rspin3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    
    ## Equation 8
    M = np.dot(Rspin3, np.dot(Rspin2, Rspin1)).T
    
    ## Equation 7
    N_x = np.zeros((6, 3))
    for j in range(6):
        N_x[j, :] = np.dot(M, n[j, :])
    
    ## Equation 9
    N_X = np.zeros((6, 3))
    for j in range(6):
        N_X[j, :] = np.dot(Q, N_x[j, :])
    
    return N_X
