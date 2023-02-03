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
