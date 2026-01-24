# strategy.py
"""
Module: strategy.py
Author: Mohammed Moniruzzaman Khan
Project: Systematic Multi-Asset Trading and Risk Management System
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize

class MeanVarianceStrategy:
    """
    Mean-Variance Optimization: allocates portfolio weights to maximize return for given risk
    """
    def __init__(self, assets):
        self.assets = assets

    def optimize(self):
        # Ensure all assets have returns
        returns = pd.concat([asset.returns for asset in self.assets], axis=1)
        returns.columns = [asset.name for asset in self.assets]

        # Compute mean returns and covariance
        mean_returns = returns.mean()
        cov_matrix = returns.cov()

        num_assets = len(self.assets)
        init_guess = np.array([1/num_assets]*num_assets)
        bounds = [(0, 1) for _ in range(num_assets)]

        # Constraint: weights sum to 1
        constraints = {'type': 'eq', 'fun': lambda w: np.sum(w)-1}

        # Objective: minimize portfolio variance
        def portfolio_variance(weights):
            return weights @ cov_matrix.values @ weights.T

        result = minimize(portfolio_variance, init_guess, bounds=bounds, constraints=constraints)
        return result.x  # optimized weights


# ----------------------------
# Standalone strategies
# ----------------------------

def equal_weight_strategy(assets):
    """
    Equal-weight portfolio
    """
    n = len(assets)
    return np.ones(n) / n


def volatility_weight_strategy(assets):
    """
    Inverse-volatility weighted portfolio
    """
    vols = np.array([a.returns.std() for a in assets])
    inv_vols = 1 / vols
    return inv_vols / inv_vols.sum()
