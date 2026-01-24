# transaction_costs.py
"""
Module: transaction_costs.py
Handles transaction cost modeling for portfolio strategies
"""

import numpy as np
import pandas as pd


class TransactionCostModel:
    """
    Simple proportional transaction cost model
    """

    def __init__(self, cost_rate=0.001):
        """
        Parameters
        ----------
        cost_rate : float
            Cost per unit turnover (e.g. 0.001 = 10 bps)
        """
        self.cost_rate = cost_rate

    def apply(self, returns, weights):
        """
        Apply transaction costs to portfolio returns

        Parameters
        ----------
        returns : pd.Series
            Portfolio returns
        weights : pd.DataFrame
            Portfolio weights over time (index aligned with returns)

        Returns
        -------
        pd.Series
            Net returns after transaction costs
        """
        # Compute turnover
        turnover = weights.diff().abs().sum(axis=1)
        turnover.iloc[0] = 0.0

        # Transaction cost per period
        transaction_costs = self.cost_rate * turnover

        # Net returns
        net_returns = returns - transaction_costs

        return net_returns
