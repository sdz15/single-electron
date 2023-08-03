import numpy as np
from initialdata.psi.psim import psim


def i_psim(s):
    return np.imag(psim(s))
