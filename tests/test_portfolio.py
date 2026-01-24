# test/test_portfolio.py
from assets import Asset
from portfolio import Portfolio

# Step 1: Load AAPL asset
aapl = Asset("AAPL")
aapl.load_data_csv("data/AAPL.csv")
aapl.compute_returns()
aapl.compute_log_returns()
aapl.summary()

# Step 2: Create Portfolio
portfolio = Portfolio([aapl], [1.0])
portfolio.compute_portfolio_returns()
portfolio.summary()
