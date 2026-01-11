import numpy as np

def penalty_encoding(returns, covariance, budget, penalty=10):
    N = len(returns)
    Q = np.zeros((N, N))

    # Objective: maximize return - risk
    for i in range(N):
        Q[i, i] -= returns[i]
        for j in range(N):
            Q[i, j] += covariance[i, j]

    # Budget constraint: (sum x_i - B)^2
    for i in range(N):
        Q[i, i] += penalty * (1 - 2 * budget)
        for j in range(N):
            if i != j:
                Q[i, j] += 2 * penalty

    return Q
