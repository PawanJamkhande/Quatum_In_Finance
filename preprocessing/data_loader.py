import numpy as np
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_data():
    returns = np.loadtxt(os.path.join(DATA_DIR, "returns.csv"), delimiter=",")
    covariance = np.loadtxt(os.path.join(DATA_DIR, "covariance.csv"), delimiter=",")
    
    with open(os.path.join(DATA_DIR, "constraints.json")) as f:
        constraints = json.load(f)

    if covariance.shape[0] != len(returns):
        raise ValueError(
        "Covariance matrix size must match number of assets"
    )

    return returns, covariance, constraints
