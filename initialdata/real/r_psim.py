import numpy as np
from initialdata.psi.psim import psim


def r_psim(s):
    return np.real(psim(s))
