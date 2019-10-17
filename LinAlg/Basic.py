# coding=utf-8
"""Basic linear algebra for IO Analysis."""

import numpy as np


def production_estimate(technology, demand):
    """Calculate production estimates that meets demand given technology matrix.

    Args;
        technology: Technology (Leontief) matrix (ndarray).
        demand: Demand vector (ndarray).

    Returns:
        production estimates (ndarray).
    """
    return np.linalg.inv(np.identity(technology.shape[0]) - technology) @ demand


if __name__ == '__main__':
    print("Linear Algebra for IO Analysis.")

    tech = np.array([[10/27, 2/15], [4/27, 2/15]])
    dem = np.array([15, 9])
    print(tech, dem)
    a = (production_estimate(tech, dem))
    l = np.identity(tech.shape[0])
    c = tech
    x = 2
    while np.mean((a - (l @ dem)) / a) > 0.1 ** 15:
        l += c
        c = c @ tech
        print(l @ dem, np.mean((a - (l @ dem)) / a), x)
        x += 1

    print(a)

    tech = np.array([[0.05, 0.2, 0.025], [0.05, 0.1, 0.025], [0.6, 0.6, 0.15]])
    dem = np.array([35 * 3 / 4, 36, 25 * 0.95])
    print(production_estimate(tech, dem))
