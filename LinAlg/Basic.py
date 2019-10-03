# coding=utf-8
"""Basic linear algebra for IO Analysis."""

import numpy as np


def production_estimate(technology, demand):
    """Calculate production estimates that meets demand given technology matrix.

    Args;
        technology: Technology (Leontief) matrix (ndarray).
        Demand: Demand vector (ndarray).


    Returns:
        production estimates (ndarray).
    """
    return np.dot(np.linalg.inv(np.identity(technology.shape[0]) - technology), demand.T)


if __name__ == '__main__':
    print("Linear Algebra for IO Analysis.")
    tech = np.array([[.1, .01, .01], [.02, .13, .2], [.05, .18, .05]])
    dem = np.array([2350, 4552, 911])
    print(production_estimate(tech, dem))