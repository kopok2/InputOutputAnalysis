# coding=utf-8
"""Basic linear algebra for IO Analysis."""

import numpy as np


def production_estimate(technology, demand):
    """Calculate production estimates that meets demand given technology matrix.

    Formula:
        X = (I - A) ^ -1 d

    Args;
        technology: technology matrix (ndarray).
        demand: demand vector (ndarray).

    Returns:
        production estimates (ndarray).
    """
    return leontief_inverse(technology) @ demand


def technology_matrix(flow, output):
    """Get technology matrix with given intersectoral flow matrix and output vector.

    Args:
        flow: intersectoral flow matrix (ndarray).
        output: economy output vector (ndarray).

    Returns:
        technology matrix (ndarray).
    """
    return flow / output


def mean_relative_error(ground_truth, estimate):
    """Calculate mean relative error of given estimate with respect to given ground truth vector.

    Args:
        ground_truth: true value of calculation (ndarray).
        estimate: model estimate (ndarray).

    Returns:
        mean relative error.
    """
    return np.mean((ground_truth - estimate) / ground_truth)


def leontief_inverse(technology):
    """Calculate Leontief inverse.

    Formula:
        L = (I - A) ^ -1

    Args:
        technology: technology matrix (ndarray).

    Returns:
        Leontief inverse (ndarray).
    """
    return np.linalg.inv(np.identity(technology.shape[0]) - technology)


def taylor_series_estimate(technology, demand, converge_threshold=0.1**10):
    """Calculate Leontief inverse estimate using matrix power series.

    Formula:
        (I - A) ^ -1 = I + A + A^2 + A^3 + A^4 + ...

    Args:
        technology: technology matrix (ndarray).
        demand: demand vector (ndarray).
        converge_threshold: level of convergence when algorithm will stop.

    Returns:
        n - number of rounds economy needs to converge with given threshold to balanced state.
    """
    convex_result = production_estimate(technology, demand)

    print("Calculating Taylor series estimate of Leontief inverse.")
    n = 0
    inverse_estimate = np.identity(tech.shape[0])
    taylor_expansion_term = tech
    while mean_relative_error(convex_result, inverse_estimate @ demand) > converge_threshold:
        inverse_estimate += taylor_expansion_term
        taylor_expansion_term = taylor_expansion_term @ tech
        print(n, convex_result, inverse_estimate @ demand)
        n += 1
    return n


if __name__ == '__main__':
    print("Linear Algebra for IO Analysis.")

    tech = np.array([[10/27, 2/15], [4/27, 2/15]])
    dem = np.array([15, 9])
    taylor_series_estimate(tech, dem)

    tech = np.array([[0.05, 0.2, 0.025], [0.05, 0.1, 0.025], [0.6, 0.6, 0.15]])
    dem = np.array([35 * 3 / 4, 36, 25 * 0.95])
    print(production_estimate(tech, dem))
