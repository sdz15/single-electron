from jfun.phi.phiM import phiM
from jfun.phi.phiP import phiP
from jfun.j1 import j1
from jfun.j0 import j0


def velocity(s,t):
    pM = phiM(t, s)
    pP = phiP(t, s)

    Q = [0, 0]
    j_0 = j0(pM, pP)
    if j_0 > 1e-14:
        j_1 = j1(pM, pP)
        Q = j_1 / j_0

    return Q
