import numpy as np

def extract_features(returns, covariance, constraints):
    N = len(returns)

    density = np.count_nonzero(covariance) / covariance.size
    condition_number = np.linalg.cond(covariance)

    features = {
        "num_assets": N,
        "density": density,
        "condition": condition_number,
        "constraint_type": constraints["type"],
        "fractional": constraints.get("allow_fractional", False)
    }

    return features
