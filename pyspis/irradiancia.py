import numpy as np
import matplotlib.pyplot as plt

from attitude import *
from eclipse import *
from input_orbit import *
from j0 import *
from kepler_e import *
from position import *
from projection import *
from solar_position import *
from ta_from_time import *

# User input
G = 1367  # Solar irradiance [W/m^2]
eta = 0.30  # solar cell efficiency [-]
A = 0.01  # Solar cell area [m^2]
timestep = 10  # timestep [s]

# Initialization
it = 0  # counter
t0 = 0  # initial time [s]

# Conversion factors:
hours = 3600  # Hours to seconds
days = 24 * hours  # Days to seconds
rad = np.pi / 180  # Degrees to radians

# Constants:
mu = 398600  # Gravitational parameter (km^3/s^2)
RE = 6378  # Earth radius (km)

# Read TLE & further arguments (angles in degrees)
h, e, RA, i, w, TA0, year, month, day, T = inputOrbit(mu, rad)

# Compute the position of the sun r_sun at a given day
r_sun = solar_position(year, month, day)

# Initialize arrays for storage
time = np.array([])
Power = np.zeros((0, 6))
Power_total = np.array([])

pos = np.empty((1,3))
P = list()

# Solver
while t0 <= T:
    it = it + 1  # iteration
    time = np.append(time, (it - 1) * timestep)  # time [s]

    # transformation from time [s] to true anomaly [rad]
    TA = ta_from_time(time[it - 1], e, T, TA0)

    # position of the satellite - Equation 1, 2, 3
    state_r, Q = sv_from_coe(h, e, RA, i, w, TA, it, mu)
    pos = np.vstack([pos, state_r])

    # eclipse of the earth - Equation 5
    csi = eclipse(pos, it, r_sun, RE)

    # attitude of the satellite - Equation 6, 7, 8, 9
    N_X = attitude(h, e, RA, i, w, TA, it, Q, T, r_sun, time[it - 1])

    # view factor - Equation 10
    F = irradiance_field(N_X, pos, r_sun, it, RE)

    # power generation - Equation 11
    P_k = eta * G * A * F * csi
    P.append(P_k)

    t0 = time[it - 1]  # used in the loop

# Post processing
Power = np.array(P).reshape(it, 6)
Power_total = np.sum(Power, axis=1)

# Plot
fig, ax = plt.subplots()
ax.plot(time, Power[:, 0], time, Power[:, 1], time, Power[:, 2], time, Power[:, 3], time, Power[:, 4], time, Power[:, 5], time, Power_total)
ax.legend(['X_{+}', 'X_{-}', 'Y_{+}', 'Y_{-}', 'Z_{+}', 'Z_{-}', 'Total'])
ax.set_xlabel("Time [s]")
ax.set_ylabel("Power [W]")
#plt.savefig("test.png")
plt.show()
