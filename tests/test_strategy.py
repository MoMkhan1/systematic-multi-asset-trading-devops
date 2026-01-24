from assets import Asset
from portfolio import Portfolio
from strategy import MeanVarianceStrategy

# Load assets
aapl = Asset("AAPL")
aapl.load_data_csv("data/AAPL.csv")
aapl.compute_returns()

msft = Asset("MSFT")
msft.load_data_csv("data/MSFT.csv")
msft.compute_returns()

goog = Asset("GOOG")
goog.load_data_csv("data/GOOG.csv")
goog.compute_returns()

# Portfolio
portfolio = Portfolio([aapl, msft, goog])
portfolio.compute_portfolio_returns()
portfolio.summary()

# Strategy
strategy = MeanVarianceStrategy([aapl, msft, goog])
weights = strategy.optimize()

print("\nMean-Variance Optimized Weights:")
for asset, w in zip(["AAPL", "MSFT", "GOOG"], weights):
    print(f"{asset}: {w:.4f}")
