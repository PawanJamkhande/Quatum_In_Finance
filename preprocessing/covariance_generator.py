import numpy as np

def generate_covariance(asset_returns):
    "asset_returns: matrix of shape (time_steps, num_assets)"
    return np.cov(asset_returns, rowvar=False)
