from scipy.integrate import quad
from util.config import omega, step

from initialdata.psi.psip import psip
from initialdata.imag.i_psim import i_psim
from initialdata.imag.i_psip import i_psip
from initialdata.real.r_psim import r_psim
from initialdata.real.r_psip import r_psip
from wavefunction.bessel.besselfunction import besselfun
from wavefunction.bessel.besselterm import besselterm


def phi_plus(t, s):
    x = psip(s - t)

    r_j1 = lambda sigma: besselfun(besselterm(t, s, sigma), 1) * (t - s + sigma) * r_psip(sigma)
    i_j1 = lambda sigma: besselfun(besselterm(t, s, sigma), 1) * (t - s + sigma) * i_psip(sigma)
    y = -(omega / 2) * (quad(r_j1, s - t, s + t)[0] + quad(i_j1, s - t, s + t)[0])

    r_j0 = lambda sigma: besselfun(besselterm(t, s, sigma), 0) * r_psim(sigma)
    i_j0 = lambda sigma: besselfun(besselterm(t, s, sigma), 0) * i_psim(sigma)
    z = -(1j * omega / 2) * (quad(r_j0, s - t, s + t)[0] + quad(i_j0, s - t, s + t)[0])

    return x + y + z
