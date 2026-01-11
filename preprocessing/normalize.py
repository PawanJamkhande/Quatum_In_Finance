import numpy as np

def normalize_data(returns, covariance):
    returns_norm = returns / np.max(np.abs(returns))
    cov_norm = covariance / np.max(np.abs(covariance))
    return returns_norm, cov_norm
