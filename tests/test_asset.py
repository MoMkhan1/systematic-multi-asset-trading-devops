from assets import Asset

# Create Asset object
aapl = Asset("AAPL")

# Load historical CSV data
aapl.load_data_csv("data/AAPL.csv")  # Works even if numbers have commas

# Compute returns
aapl.compute_returns()
aapl.compute_log_returns()

# Show summary
aapl.summary()
