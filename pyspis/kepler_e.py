import math

def kepler_E(e, M):
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
