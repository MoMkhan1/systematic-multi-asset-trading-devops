# risk_metrics.py
"""
Compute portfolio risk metrics: Max Drawdown, Rolling Volatility, VaR, CVaR
"""

import pandas as pd
import numpy as np

class RiskMetrics:
    def __init__(self, returns: pd.Series):
        """
        returns : pd.Series
            Portfolio returns
        """
        self.returns = returns
        self.cumulative_returns = (1 + returns).cumprod()

    def max_drawdown(self):
        cum_max = self.cumulative_returns.cummax()
        drawdown = (cum_max - self.cumulative_returns) / cum_max
        max_dd = drawdown.max()
        return max_dd

    def rolling_volatility(self, window=30):
        return self.returns.rolling(window).std()

    def value_at_risk(self, confidence_level=0.95):
        var = -np.percentile(self.returns, 100 * (1 - confidence_level))
        return var

    def conditional_var(self, confidence_level=0.95):
        var = self.value_at_risk(confidence_level)
        cvar = -self.returns[self.returns <= -var].mean()
        return cvar

    def summary(self):
        print("Risk Metrics Summary:")
        print("--------------------")
        print(f"Max Drawdown: {self.max_drawdown():.4f}")
        print(f"VaR (95%): {self.value_at_risk():.4f}")
        print(f"CVaR (95%): {self.conditional_var():.4f}")
        print(f"Rolling Volatility (last 5 days):\n{self.rolling_volatility().tail()}")
