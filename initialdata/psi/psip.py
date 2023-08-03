from util.config import theta
from initialdata.psi.gaussian.el_0 import el_0
from numpy import sin


def psip(s):
    return sin(theta)*el_0(s)
