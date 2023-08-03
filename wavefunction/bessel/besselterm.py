from numpy import sqrt
from util.config import omega


def besselterm(t, s, sigma):
    return omega*sqrt((t**2)-((s-sigma)**2))
