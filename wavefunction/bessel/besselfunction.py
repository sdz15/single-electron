from scipy.special import jv
from math import factorial
import numpy as np
from util.config import omega


def besselfun(x, index):
    if x <= 1e-6:
        return (omega**index)/(factorial(index)*2**index)
    return jv(index, omega*x)/(x**index)
