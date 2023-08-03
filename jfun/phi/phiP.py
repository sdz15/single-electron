from numpy import abs
from wavefunction.phiPlus import phi_plus


def phiP(t, s):
    return abs(phi_plus(t, s)) ** 2
