# simulator.py
import pandas as pd
import numpy as np
from strategy import MeanVarianceStrategy

class Simulator:
    """
    Simulator class to run multi-asset portfolio simulations
    with periodic rebalancing using Mean-Variance optimization.
    """
    def __init__(self, assets, rebalance_freq="ME"):
        """
        assets : list of Asset objects
        rebalance_freq : 'ME' (month-end), 'W' (weekly), 'Q' (quarterly)
        """
        self.assets = assets
        self.rebalance_freq = rebalance_freq

    def run(self):
        # Combine returns of all assets
        returns_df = pd.concat([asset.returns for asset in self.assets], axis=1)
        returns_df.columns = [asset.name for asset in self.assets]
        returns_df.dropna(inplace=True)

        portfolio_returns = []
        dates = []

        # Rebalance periodically
        for _, window in returns_df.groupby(pd.Grouper(freq=self.rebalance_freq)):
            if len(window) < 2:
                continue

            # Update returns in assets
            for i, asset in enumerate(self.assets):
                asset.returns = window.iloc[:, i]

            # Optimize weights
            strategy = MeanVarianceStrategy(self.assets)
            weights = strategy.optimize()

            # Apply weights
            for date, row in window.iterrows():
                portfolio_returns.append(np.dot(weights, row))
                dates.append(date)

        return pd.Series(portfolio_returns, index=dates)
