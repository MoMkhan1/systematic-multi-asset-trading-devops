# scripts/download_data.py
"""
Download historical stock data using yfinance
"""

import yfinance as yf
import os

# List of asset tickers
assets = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]

# Data folder
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

# Date range
start_date = "2020-01-01"
end_date = "2025-01-01"

# Download data
for ticker in assets:
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data[['Close']]  # Keep only 'Close' price
    csv_file = os.path.join(data_folder, f"{ticker}.csv")
    data.to_csv(csv_file)
    print(f"{ticker} data saved to {csv_file}")

print("All asset data downloaded successfully!")
