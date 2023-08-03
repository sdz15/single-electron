import numpy as np
from initialdata.psi.psip import psip


def i_psip(s):
    return np.imag(psip(s))
