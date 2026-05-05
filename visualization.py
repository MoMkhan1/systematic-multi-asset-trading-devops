# visualization.py
"""
Module: visualization.py
Author: Mohammed Moniruzzaman Khan
Project: Systematic Multi-Asset Trading and Risk Management System
"""
import os
import matplotlib.pyplot as plt
# Folder where graphs will be saved
GRAPH_FOLDER = r"F:\GITHUB\systematic-multi-asset-trading-devops\results"

# Create folder automatically if it doesn't exist
os.makedirs(GRAPH_FOLDER, exist_ok=True)
#import matplotlib.pyplot as plt


# ----------------------------
# 1. CUMULATIVE RETURNS
# ----------------------------
def plot_cumulative_returns(cumulative_returns, save_path="results/cumulative_returns.png"):
    plt.figure(figsize=(10, 6))
    cumulative_returns.plot()
    plt.title("Cumulative Portfolio Returns")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()


# ----------------------------
# 2. ROLLING VOLATILITY
# ----------------------------
def plot_rolling_volatility(returns, window=20, save_path="results/rolling_volatility.png"):
    rolling_vol = returns.rolling(window=window).std()

    plt.figure(figsize=(10, 6))
    rolling_vol.plot()
    plt.title(f"Rolling Volatility ({window} periods)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()


# ----------------------------
# 3. ROLLING SHARPE
# ----------------------------
def plot_rolling_sharpe(returns, window=20, save_path="results/rolling_sharpe.png"):
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
    plt.savefig(save_path, dpi=300)
    plt.show()


# ----------------------------
# ⭐ 4. LINKEDIN / QUANT DASHBOARD (NEW)
# ----------------------------
def save_quant_dashboard(cum_returns, returns):

    import matplotlib.pyplot as plt
    import os

    fig, axs = plt.subplots(2, 2, figsize=(16, 10))

    # Cumulative returns
    cum_returns.plot(ax=axs[0, 0])
    axs[0, 0].set_title("Cumulative Returns")
    axs[0, 0].grid(True)

    # Volatility
    vol = returns.rolling(20).std()
    vol.plot(ax=axs[0, 1])
    axs[0, 1].set_title("Rolling Volatility")
    axs[0, 1].grid(True)

    # Sharpe
    sharpe = returns.rolling(20).mean() / returns.rolling(20).std()
    sharpe.plot(ax=axs[1, 0])
    axs[1, 0].set_title("Rolling Sharpe Ratio")
    axs[1, 0].grid(True)

    # Summary box
    axs[1, 1].axis("off")
    axs[1, 1].text(
        0.1, 0.6,
        "Systematic Trading System\nMean-Variance Optimization\nRisk Metrics Included",
        fontsize=11
    )

    plt.tight_layout()

    save_path = os.path.join(GRAPH_FOLDER, "quant_dashboard.png")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()