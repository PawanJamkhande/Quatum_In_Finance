import numpy as np

def generate_asset_returns(num_assets, time_steps=100):
    """
    Generates simulated asset return time-series.
    
    num_assets: number of assets (N)
    time_steps: historical length
    """
    # Mean return and volatility (assumed)
    mean = 0.01
    std_dev = 0.05

    # Shape: (time_steps, num_assets)
    returns = np.random.normal(
        mean,
        std_dev,
        size=(time_steps, num_assets)
    )

    return returns
