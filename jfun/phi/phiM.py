from numpy import abs
from wavefunction.phiMinus import phi_minus


def phiM(t, s):
    return abs(phi_minus(t, s)) ** 2
