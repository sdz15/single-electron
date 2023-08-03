from numpy import sin, cos, exp, pi
from util.config import sigma, k, mu


def el_0(s):
    return (2 * pi * sigma ** 2) ** (-0.25) * exp(
        -((s - mu) ** 2) / (4 * sigma ** 2) + (1j * k * s))
