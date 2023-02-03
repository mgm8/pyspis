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
