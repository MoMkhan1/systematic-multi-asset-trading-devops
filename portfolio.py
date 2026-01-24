# portfolio.py
"""
Module: portfolio.py
Author: Mohammed Moniruzzaman Khan
Project: Systematic Multi-Asset Trading and Risk Management System
"""

import pandas as pd
import numpy as np

class Portfolio:
    """
    Portfolio class to manage multiple assets, weights, and compute portfolio metrics
    """

    def __init__(self, assets, weights=None):
        """
        Initialize Portfolio

        Parameters:
        assets (list): List of Asset objects
        weights (list or None): Initial weights; if None, equal weights are assigned
        """
        self.assets = assets
        self.num_assets = len(assets)

        if weights is None:
            self.weights = np.array([1/self.num_assets]*self.num_assets)
        else:
            self.weights = np.array(weights)

        self.returns = None
        self.cumulative_returns = None

    def compute_portfolio_returns(self):
        """
        Compute portfolio returns as weighted sum of asset returns
        """
        # Combine all asset returns into one DataFrame
        returns_df = pd.concat([asset.returns for asset in self.assets], axis=1)
        returns_df.columns = [asset.name for asset in self.assets]

        # Ensure weights sum to 1
        self.weights = self.weights / np.sum(self.weights)

        # Compute portfolio returns
        self.returns = (returns_df * self.weights).sum(axis=1)
        self.cumulative_returns = (1 + self.returns).cumprod()
        return self.returns

    def portfolio_mean(self):
        if self.returns is None:
            self.compute_portfolio_returns()
        return self.returns.mean()

    def portfolio_volatility(self):
        if self.returns is None:
            self.compute_portfolio_returns()
        return self.returns.std()

    def portfolio_sharpe(self, risk_free_rate=0.0):
        """
        Compute annualized Sharpe ratio
        """
        if self.returns is None:
            self.compute_portfolio_returns()
        # Daily Sharpe ratio
        sharpe_daily = (self.returns.mean() - risk_free_rate) / self.returns.std()
        # Annualize assuming 252 trading days
        return sharpe_daily * np.sqrt(252)

    def summary(self):
        print("Portfolio Summary")
        print("------------------------------")
        print(f"Assets: {[asset.name for asset in self.assets]}")
        print(f"Weights: {self.weights.tolist()}")
        print(f"Mean return: {self.portfolio_mean():.6f}")
        print(f"Volatility: {self.portfolio_volatility():.6f}")
        print(f"Sharpe ratio: {self.portfolio_sharpe():.6f}")
