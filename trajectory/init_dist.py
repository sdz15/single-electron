import numpy as np
from util.config import mu, sigma, num_traj

# Distribution of initial data based on Gaussian

def init_dist():
    return np.random.normal(mu, sigma, size=(1,num_traj))

# Should try to make this 2D instead of 3D