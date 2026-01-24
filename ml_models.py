# ml_models.py
"""
Simple ML models for return and volatility prediction.
These models are intentionally lightweight and interpretable,
suitable for systematic trading research pipelines.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# ==========================================================
# Return Predictor
# ==========================================================
class ReturnPredictor:
    def __init__(self, asset):
        """
        asset: Asset object containing returns (pd.Series)
        """
        self.asset = asset
        self.model = LinearRegression()
        self.is_trained = False

    def train(self):
        """
        Train linear regression on lagged returns
        """
        # Convert Series → DataFrame explicitly
        df = pd.DataFrame(self.asset.returns, columns=["returns"])

        # Lagged features
        df["lag1"] = df["returns"].shift(1)
        df["lag2"] = df["returns"].shift(2)
        df["lag3"] = df["returns"].shift(3)

        df.dropna(inplace=True)

        X = df[["lag1", "lag2", "lag3"]]
        y = df["returns"]

        self.model.fit(X, y)
        self.is_trained = True

    def predict_next(self):
        """
        Predict next-period return using last observed lags
        """
        if not self.is_trained:
            raise RuntimeError("ReturnPredictor must be trained before prediction.")

        last_vals = self.asset.returns.iloc[-3:].values.reshape(1, -1)
        return float(self.model.predict(last_vals))


# ==========================================================
# Volatility Predictor
# ==========================================================
class VolatilityPredictor:
    def __init__(self, asset, window=20):
        """
        asset: Asset object
        window: rolling window for volatility estimation
        """
        self.asset = asset
        self.window = window
        self.model = LinearRegression()
        self.is_trained = False

    def train(self):
        """
        Train linear regression on lagged rolling volatility
        """
        returns = self.asset.returns

        # Rolling volatility
        rolling_vol = returns.rolling(self.window).std()

        # Convert to DataFrame
        df = pd.DataFrame(rolling_vol, columns=["volatility"])

        # Lagged volatility features
        df["lag1"] = df["volatility"].shift(1)
        df["lag2"] = df["volatility"].shift(2)

        df.dropna(inplace=True)

        X = df[["lag1", "lag2"]]
        y = df["volatility"]

        self.model.fit(X, y)
        self.is_trained = True

    def predict_next(self):
        """
        Predict next-period volatility
        """
        if not self.is_trained:
            raise RuntimeError("VolatilityPredictor must be trained before prediction.")

        rolling_vol = self.asset.returns.rolling(self.window).std()
        last_vals = rolling_vol.iloc[-2:].values.reshape(1, -1)

        return float(self.model.predict(last_vals))
