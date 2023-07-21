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

_PYSPIS_MU              = 398600    # Gravitational parameter (km^3/s^2)
_PYSPIS_EARTH_RADIUS_KM = 6378      # Earth radius in kilometers

class SPIS:
    """
    PySPIS main class.
    """

    def __init__(self, G=0, n=0, A=0):
        """
        Class constructor.

        :param G: Solar irradiance in Watts per square meter.
        :type G: float

        :param n: Cell efficiency (index).
        :type n: float

        :param A: Solar cell area in square meter.
        :type A: float

        :return: None.
        :rtype: None
        """
        self.set_solar_irradiance(G)
        self.set_solar_cell_efficiency(n)
        self.set_solar_panel_area(A)

        # Conversion factors
        self._rad = np.pi / 180 # Degrees to radians

    def __str__(self):
        """
        Represents the class as a string.

        :return: a brief description of the class.
        :rtype: str
        """
        return 'Satellite Input Power Simulation'

    def set_orbit_from_tle_file(self, filename):
        """
        :param filename: .
        :type filename: string

        :return: .
        :rtype: None
        """
        pass

    def set_orbit_from_tle_string(self, tle_str):
        """
        :param tle_str: .
        :type tle_str: string

        :return:
        :rtype: None
        """
        pass

    def set_solar_irradiance(self, G):
        """
        :param G: .
        :type G: integer

        :return:
        :rtype: None
        """
        self._G = G

    def set_solar_cell_efficiency(self, n):
        """
        :param n: .
        :type n: integer

        :return:
        :rtype: None
        """
        self._n = n

    def set_solar_panel_area(self, A):
        """
        :param A: .
        :type A: integer

        :return:
        :rtype: None
        """
        self._A = A

    def compute_orbit(self, ts=10):
        """
        General procedure to obtain the instances' power input in a single orbit

        This function receives as inputs the solar irradiance (G), solar cell efficiency (n), and solar cell area (A), as well as a time step (ts).

        :param ts: Timestep in seconds.
        :type ts: int

        :return: Generated power in Watts.
        :rtype: float
        """
        # Initialization
        it = 0  # counter
        t0 = 0  # initial time [s]

        # Read TLE & further arguments (angles in degrees)
        h, e, RA, i, w, TA0, year, month, day, T = self._input_orbit(_PYSPIS_MU, self._rad)

        # Compute the position of the sun r_sun at a given day
        r_sun = self._solar_position(year, month, day)

        # Initialize arrays for storage
        time = np.array([])
        Power = np.zeros((0, 6))
        Power_total = np.array([])

        pos = np.empty((1,3))
        P = list()

        # Solver
        while t0 <= T:
            it = it + 1  # iteration
            time = np.append(time, (it - 1) * ts)  # time [s]

            # transformation from time [s] to true anomaly [rad]
            TA = self._ta_from_time(time[it - 1], e, T, TA0)

            # position of the satellite - Equation 1, 2, 3
            state_r, Q = self._sv_from_coe(h, e, RA, i, w, TA, it, _PYSPIS_MU)
            pos = np.vstack([pos, state_r])

            # eclipse of the earth - Equation 5
            csi = self._eclipse(pos, it, r_sun, _PYSPIS_EARTH_RADIUS_KM)

            # attitude of the satellite - Equation 6, 7, 8, 9
            N_X = self._attitude(h, e, RA, i, w, TA, it, Q, T, r_sun, time[it - 1])

            # view factor - Equation 10
            F = self._irradiance_field(N_X, pos, r_sun, it)

            # power generation - Equation 11
            P_k = self._n * self._G * self._A * F * csi
            P.append(P_k)

            t0 = time[it - 1]  # used in the loop

        # Post processing
        self._Power = np.array(P).reshape(it, 6)
        self._Power_total = np.sum(self._Power, axis=1)

        return time, self._Power, self._Power_total

    def get_average_power(self):
        """
        :return:
        :rtype: TODO
        """
        return np.average(self._Power_total)

    def get_peak_power(self):
        """
        :return:
        :rtype: TODO
        """
        return max(self._Power_total)

    def get_average_power_sunlight(self):
        """
        :return:
        :rtype: TODO
        """
        buf = list()
        for i in self._Power_total:
            if i > 0:
                buf.append(i)
        return np.average(buf)

    def _attitude(self, h, e, RA, i, w, TA, it, Q, T, r_sun, t):
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
        # Equation 6
        n = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])

        Rspin1 = np.array([[np.cos(TA), np.sin(TA), 0], [-np.sin(TA), np.cos(TA), 0], [0, 0, 1]])
        th = -0 * 1 * (2 * np.pi * t) / T # theta*

        Rspin2 = np.array([[1, 0, 0], [0, np.cos(th), np.sin(th)], [0, -np.sin(th), np.cos(th)]])
        Rspin3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        # Equation 8
        M = np.dot(Rspin3, np.dot(Rspin2, Rspin1)).T

        # Equation 7
        N_x = np.zeros((6, 3))
        for j in range(6):
            N_x[j, :] = np.dot(M, n[j, :])

        # Equation 9
        N_X = np.zeros((6, 3))
        for j in range(6):
            N_X[j, :] = np.dot(Q, N_x[j, :])

        return N_X

    def _eclipse(self, pos, it, r_sun, re):
        """

        :param pos:
        :type pos:

        :param it:
        :type it:

        :param r_sun:
        :type r_sun:

        :param re: Earth radius in kilometers
        :type re: int

        :return: .
        :rtype:
        """
        rsat = np.linalg.norm(pos[it])
        rsun = np.linalg.norm(r_sun)

        # Angle between sun and satellite position vector:
        theta = np.arccos(np.dot(pos[it], r_sun) / rsat / rsun) * 180 / np.pi

        # Angle between the satellite position vector and the radial to the point of tangency with the earth of a line from the satellite:
        theta_sat = np.arccos(re / rsat) * 180 / np.pi

        # Angle between the sun position vector and the radial to the point of tangency with the earth of a line from the sun:
        theta_sun = 90

        if theta_sat + theta_sun <= theta:
            csi = 0 # eclipse
        else:
            csi = 1 # no eclipse

        return csi

    def _input_orbit(self, mu, rad):
        """

        :param mu: Gravitational parameter (km^3/s^2)
        :type mu: int

        :param rad:
        :type rad:

        :return: .
        :rtype: None
        """
        data = {"tle": [0, 90, 0, 0.000001, 0, 15.21981]}

        RA0 = data["tle"][0] * rad
        i0 = data["tle"][1] * rad
        w0 = data["tle"][2] * rad
        e0 = data["tle"][3]
        Ma0 = data["tle"][4] * rad
        Ea0 = self._kepler_e(e0, Ma0)
        TA0 = 2 * np.arctan((((1 + e0) / (1 - e0))**0.5) * np.tan(Ea0 / 2))
        Mm0 = data["tle"][5] / (24 * 3600)
        a0 = (mu**(1 / 3)) / ((2 * np.pi * Mm0)**(2 / 3))
        h0 = (a0 * mu * (1 - e0**2))**0.5

        year = 2023
        month = 3
        day = 21

        T = 2 * np.pi * (a0**1.5) / (mu**0.5)

        return h0, e0, RA0, i0, w0, TA0, year, month, day, T

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
        return 367 * y - int(7 * (y + int((m + 9) / 12)) / 4) + int(275 * m / 9) + d + 1721013.5

    def _kepler_e(self, e, M):
        """

        :param e:
        :type e:

        :param M:
        :type M:

        :return: .
        :rtype: None
        """
        error = 1e-8

        if M < math.pi:
            E = M + e / 2
        else:
            E = M - e / 2

        ratio = 1
        while abs(ratio) > error:
            ratio = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
            E = E - ratio

        return E

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

    def _irradiance_field(self, N_X, pos, r_sun, it):
        """

        :param N_X:
        :type N_X:

        :param pos:
        :type pos:

        :param r_sun:
        :type r_sun:

        :param it:
        :type it:

        :return: .
        :rtype: None
        """
        F = np.zeros(6)

        for j in range(6):
            F[j] = np.dot(N_X[j,:], r_sun) / np.linalg.norm(r_sun)
            if F[j] < 0:
                F[j] = 0
            else:
                F[j] = F[j]

        return F

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
        # Compute Julian day
        jd = self._j0(y, m, d)

        # Astronomical unit (km):
        AU = 149597870.691

        # Julian days since J2000:
        n = jd - 2451545

        # Julian centuries since J2000:
        cy = n / 36525

        # Mean anomaly (deg):
        M = 357.528 + 0.9856003 * n
        M = M % 360

        # Mean longitude (deg):
        L = 280.460 + 0.98564736 * n
        L = L % 360

        # Apparent ecliptic longitude (deg):
        lamda = L + 1.915 * math.sin(math.radians(M)) + 0.020 * math.sin(2 * math.radians(M))
        lamda = lamda % 360

        # Obliquity of the ecliptic (deg):
        eps = 23.439 - 0.0000004 * n

        # Unit vector from earth to sun:
        u = [math.cos(math.radians(lamda)), math.sin(math.radians(lamda)) * math.cos(math.radians(eps)), math.sin(math.radians(lamda)) * math.sin(math.radians(eps))]

        # Distance from earth to sun (km):
        rS = (1.00014 - 0.01671 * math.cos(math.radians(M)) - 0.000140 * math.cos(2 * math.radians(M))) * AU

        # Geocentric position vector (km):
        r_S = [i * rS for i in u]

        return r_S

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
        M = 2 * np.pi * t / T
        E = self._kepler_e(e, M)
        TA = 2 * np.arctan(((1 + e) / (1 - e))**0.5 * np.tan(E / 2)) + TA0

        return TA
