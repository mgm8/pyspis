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
