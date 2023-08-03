from util.config import theta
from initialdata.psi.gaussian.el_0 import el_0
from numpy import cos


def psim(s):
    return cos(theta)*el_0(s)
