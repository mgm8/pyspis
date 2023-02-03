import math

def solar_position(year, month, day):
    # Compute Julian day
    jd = J0(year, month, day)

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
    r_S = rS * u

    return r_S
