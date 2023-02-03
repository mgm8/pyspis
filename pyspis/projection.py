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
