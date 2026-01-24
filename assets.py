# assets.py
"""
Module: assets.py
Author: Mohammed Moniruzzaman Khan
Project: Systematic Multi-Asset Trading and Risk Management System
"""

import pandas as pd
import numpy as np

class Asset:
    """
    Asset Class to represent a single financial instrument
    """

    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.returns = None
        self.log_returns = None

    def load_data_csv(self, file_path, price_col='Close', date_col=None, date_format="%Y-%m-%d"):
        """
        Load historical data from CSV

        Parameters:
        file_path (str): Path to CSV file
        price_col (str): Column name of prices
        date_col (str or None): Column name of dates; if None, use first column
        date_format (str or None): Format string for parsing dates
        """
        df = pd.read_csv(file_path)

        # Detect date column
        if date_col is None:
            date_col = df.columns[0]

        # Convert date column to datetime explicitly
        df[date_col] = pd.to_datetime(df[date_col], format=date_format, errors='coerce')

        # Drop rows with invalid dates
        df = df.dropna(subset=[date_col])

        # Set date as index
        df.set_index(date_col, inplace=True)
        df.sort_index(inplace=True)

        # Keep only the price column
        if price_col not in df.columns:
            raise ValueError(f"Column '{price_col}' not found in CSV")
        
        # Ensure price column is numeric (handles strings like "1,234.56")
        df[price_col] = pd.to_numeric(df[price_col].astype(str).str.replace(',', ''), errors='coerce')
        df = df.dropna(subset=[price_col])

        self.data = df[[price_col]]

    def compute_returns(self):
        if self.data is None:
            raise ValueError("Data not loaded")
        self.returns = self.data.pct_change(periods=1, fill_method=None).dropna()
        return self.returns

    def compute_log_returns(self):
        if self.data is None:
            raise ValueError("Data not loaded")
        self.log_returns = np.log(self.data / self.data.shift(1)).dropna()
        return self.log_returns

    def moving_average(self, window=20):
        if self.data is None:
            raise ValueError("Data not loaded")
        return self.data.rolling(window=window).mean()

    def volatility(self, window=20):
        if self.returns is None:
            self.compute_returns()
        return self.returns.rolling(window=window).std()

    def correlation(self, other_asset, window=20):
        if self.returns is None:
            self.compute_returns()
        if other_asset.returns is None:
            other_asset.compute_returns()
        return self.returns.rolling(window).corr(other_asset.returns)

    def summary(self):
        print(f"Asset: {self.name}")
        print(f"Data length: {len(self.data)}")
        print(f"Start date: {self.data.index.min().date()}")
        print(f"End date: {self.data.index.max().date()}")
        if self.returns is not None:
            mean_return = self.returns.mean().iloc[0]
            vol = self.volatility().mean().iloc[0]
            print(f"Mean return: {mean_return:.6f}")
            print(f"Volatility: {vol:.6f}")
        else:
            print("Returns not computed yet")
