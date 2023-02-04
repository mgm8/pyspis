#
# pyspis.py
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


import math

import numpy as np
import matplotlib.pyplot as plt

class SPIS:
    """
    PySPIS main class.
    """

    def __init__(self):
        """
        Class constructor.

        :return: None.
        :rtype: None
        """
        pass

    def __str__(self):
        """
        Represents the class as a string.

        :return: a brief description of the class.
        :rtype: str
        """
        return 'Satellite Input Power Simulation'

    def compute(self, G, n, A, ts):
        """
        General procedure to obtain the instances' power input
        
        This function receives as inputs the solar irradiance (G), solar cell efficiency (n), and solar cell area (A), as well as a time step (ts).

        :param G: Solar irradiance in Watts per square meter.
        :type G: float

        :param n: Cell efficiency (index).
        :type n: float

        :param A: Solar cell area in square meter.
        :type A: float

        :param ts: Timestep in seconds
        :type ts: int

        :return: Generated power in Watts.
        :rtype: float
        """
        pass

    def _attitude(self, h, e, ra, i, w, ta, it, q, t, r_sun, t):
        """

        :param h:
        :type h:

        :param e:
        :type e:

        :param ra:
        :type ra:

        :param i:
        :type i:

        :param w:
        :type w:

        :param ta:
        :type ta:

        :param it:
        :type it:

        :param q:
        :type q:

        :param t:
        :type t:

        :param r_sun:
        :type r_sun:

        :param t:
        :type t:

        :return: 
        :rtype: TODO
        """
        pass

    def _eclipse(self, pos, it, r_sun, RE):
        """

        :param pos:
        :type pos:

        :param it:
        :type it:

        :param r_sun:
        :type r_sun:

        :param RE:
        :type RE:

        :return: .
        :rtype:
        """
        pass

    def _input_orbit(self, mu, rad):
        """

        :param mu:
        :type mu:

        :param rad:
        :type rad:

        :return: .
        :rtype: None
        """
        pass

    def _j0(self, y, m, d):
        """

        :param y: Year.
        :type y: int

        :param m: Month.
        :type m: int

        :param d: Day.
        :type d: int

        :return: .
        :rtype None
        """
        pass

    def _kepler_e(self, e, M):
        """

        :param e:
        :type e:

        :param M:
        :type M:

        :return: .
        :rtype: None
        """
        pass

    def _sv_from_coe(self, h, e, RA, i, w, TA, it, mu):
        """

        :param h:
        :type h:

        :param e:
        :type e:

        :param RA:
        :type RA:

        :param i:
        :type i:

        :param w:
        :type w:

        :param TA:
        :type TA:

        :param it:
        :type it:

        :param mu:
        :type mu:

        :return: .
        :rtype None
        """
        pass

    def _irradiance_field(self, N_X, pos, r_sun, it, RE):
        """

        :param N_X:
        :type N_X:

        :param pos:
        :type pos:

        :param r_sun:
        :type r_sun:

        :param it:
        :type it:

        :param RE:
        :type RE:

        :return: .
        :rtype: None
        """
        pass

    def _solar_position(self, d, m, y):
        """

        :param d: Day.
        :type d: int

        :param m: Month.
        :type m: int

        :param y: Year.
        :type y: int

        :return: .
        :rtype: 
        """
        pass

    def _ta_from_time(self, t, e, T, TA0):
        """

        :param t:
        :type t:

        :param e:
        :type e:

        :param T:
        :type T:

        :param TA0:
        :type TA0:

        :return: .
        :rtype: None
        """
        pass
