"""
Simulation engine for Systematic Multi-Asset Trading and Risk Management System
Uses the Simulator class to compute portfolio returns and cumulative returns.
"""

from assets import Asset
from simulator import Simulator

# ----------------------------
# Step 1: Load Assets
# ----------------------------
tickers = ["AAPL", "MSFT", "GOOG", "TSLA"]
assets_list = []

for ticker in tickers:
    asset = Asset(ticker)
    asset.load_data_csv(f"data/{ticker}.csv")
    asset.compute_returns()
    assets_list.append(asset)

# ----------------------------
# Step 2: Run simulation
# ----------------------------
sim = Simulator(assets_list, rebalance_freq="ME")  # Month-end rebalance
simulated_returns = sim.run()

# Compute cumulative returns
cumulative_returns = (1 + simulated_returns).cumprod()

# Display results
print("\nSimulation complete!")
print("Final Portfolio Value:", cumulative_returns.iloc[-1])
print("Simulator returns (last 5 rows):")
print(simulated_returns.tail())
print("Cumulative returns (last 5 rows):")
print(cumulative_returns.tail())

# Optional: save results
simulated_returns.to_csv("results/simulated_portfolio_returns.csv")
cumulative_returns.to_csv("results/cumulative_portfolio_returns.csv")
print("\nResults saved in results/ folder")
