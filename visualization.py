# visualization.py
"""
Module: visualization.py
Author: Mohammed Moniruzzaman Khan
Project: Systematic Multi-Asset Trading and Risk Management System
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_cumulative_returns(cumulative_returns, save_path="results/cumulative_returns.png"):
    """
    Plot cumulative portfolio returns
    """
    plt.figure(figsize=(10, 6))
    cumulative_returns.plot()
    plt.title("Cumulative Portfolio Returns")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def plot_rolling_volatility(returns, window=20, save_path="results/rolling_volatility.png"):
    """
    Plot rolling volatility
    """
    rolling_vol = returns.rolling(window=window).std()
    plt.figure(figsize=(10, 6))
    rolling_vol.plot()
    plt.title(f"Rolling Volatility ({window} periods)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def plot_rolling_sharpe(returns, window=20, save_path="results/rolling_sharpe.png"):
    """
    Plot rolling Sharpe ratio
    """
    rolling_mean = returns.rolling(window=window).mean()
    rolling_std = returns.rolling(window=window).std()
    rolling_sharpe = rolling_mean / rolling_std
    plt.figure(figsize=(10, 6))
    rolling_sharpe.plot()
    plt.title(f"Rolling Sharpe Ratio ({window} periods)")
    plt.xlabel("Date")
    plt.ylabel("Sharpe Ratio")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
