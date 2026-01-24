"""
Main script for Systematic Multi-Asset Trading and Risk Management System

Pipeline:
1. Load assets
2. Build portfolio
3. Apply strategies
4. Run simulator
5. Apply transaction costs
6. Stress testing
7. Risk metrics
8. Save results
9. Visualize outputs
"""

import os
import numpy as np
import pandas as pd

# ----------------------------
# Imports
# ----------------------------
from assets import Asset
from portfolio import Portfolio
from strategy import (
    MeanVarianceStrategy,
    equal_weight_strategy,
    volatility_weight_strategy
)
from sim_engine import Simulator
from visualization import (
    plot_cumulative_returns,
    plot_rolling_volatility,
    plot_rolling_sharpe
)
from risk_metrics import RiskMetrics
from transaction_costs import TransactionCostModel
from stress_testing import StressTester

# ----------------------------
# Step 0: Results folder
# ----------------------------
os.makedirs("results", exist_ok=True)
print("✅ Results folder ready")

# ----------------------------
# Step 1: Load assets
# ----------------------------
tickers = ["AAPL", "MSFT", "GOOG", "TSLA"]
assets_list = []

for ticker in tickers:
    asset = Asset(ticker)
    asset.load_data_csv(f"data/{ticker}.csv")
    asset.compute_returns()
    assets_list.append(asset)

print("\n✅ Assets loaded:")
for a in assets_list:
    print(
        f"{a.name}, data length: {len(a.data)}, "
        f"start: {a.data.index.min().date()}, "
        f"end: {a.data.index.max().date()}"
    )

# ----------------------------
# Step 2: Portfolio
# ----------------------------
portfolio = Portfolio(assets_list)
portfolio.compute_portfolio_returns()

print("\n✅ Portfolio Summary")
portfolio.summary()

# ----------------------------
# Step 3: Strategies
# ----------------------------
mv_strategy = MeanVarianceStrategy(assets_list)
optimized_weights = mv_strategy.optimize()

print("\n✅ Mean-Variance Optimized Weights:")
for asset, w in zip(assets_list, optimized_weights):
    print(f"{asset.name}: {w:.4f}")

ew_weights = equal_weight_strategy(assets_list)
vol_weights = volatility_weight_strategy(assets_list)

print("\nEqual-weight strategy:", ew_weights)
print("Inverse-volatility strategy:", vol_weights.flatten())

# ----------------------------
# Step 4: Simulation
# ----------------------------
print("\n✅ Running Simulator...")
sim = Simulator(assets_list, rebalance_freq="ME")
simulated_returns = sim.run()

cumulative_returns = (1 + simulated_returns).cumprod()

print("\nSimulator output (last 5 returns):")
print(simulated_returns.tail())

print("\nCumulative returns (last 5 rows):")
print(cumulative_returns.tail())

# ----------------------------
# Step 5: Transaction costs
# ----------------------------
print("\n✅ Applying Transaction Costs...")

weights_df = pd.DataFrame(
    np.tile(optimized_weights, (len(simulated_returns), 1)),
    index=simulated_returns.index,
    columns=[a.name for a in assets_list]
)

tc_model = TransactionCostModel(cost_rate=0.001)
net_returns = tc_model.apply(simulated_returns, weights_df)

print("Transaction costs applied ✅")
print("Net returns (last 5 rows):")
print(net_returns.tail())

# ----------------------------
# Step 6: Stress testing
# ----------------------------
print("\n✅ Running Stress Testing...")

stress_tester = StressTester(net_returns)
stress_results = stress_tester.run()

scenario_returns = stress_results["scenario_returns"]
scenario_metrics = stress_results["metrics"]

print("\nStress scenario metrics:")
print(scenario_metrics)

# ----------------------------
# Step 7: Risk metrics
# ----------------------------
print("\n✅ Portfolio Risk Metrics:")
risk = RiskMetrics(net_returns)
risk.summary()

# ----------------------------
# Step 8: Save results
# ----------------------------
simulated_returns.to_csv("results/simulated_returns.csv")
net_returns.to_csv("results/net_returns.csv")
cumulative_returns.to_csv("results/cumulative_returns.csv")
scenario_returns.to_csv("results/stress_scenario_returns.csv")
scenario_metrics.to_csv("results/stress_scenario_metrics.csv")

print("\n✅ All results saved to results/ folder")

# ----------------------------
# Step 9: Visualizations
# ----------------------------
plot_cumulative_returns(cumulative_returns)
plot_rolling_volatility(net_returns)
plot_rolling_sharpe(net_returns)

print("\n🎯 Pipeline completed successfully.")
