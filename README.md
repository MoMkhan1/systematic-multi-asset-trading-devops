# Systematic Multi-Asset Trading & Risk Management System

A Python-based **multi-asset trading simulator with portfolio optimization, risk metrics, transaction cost modeling, and stress testing. Integrated with Docker and **CI/CD pipelines** for DevOps deployment.

---

## 🚀 Project Overview

This project implements a systematic trading system for multiple assets (AAPL, MSFT, GOOG, TSLA) using:

- Portfolio construction and mean-variance optimization  
- Equal-weight and inverse-volatility weighting strategies  
- A simulator with configurable rebalancing frequency  
- Transaction cost application  
- Stress testing scenarios (Market Crash, Bull Shock, Volatility Spike)  
- Risk metrics analysis (Max Drawdown, VaR, CVaR, Rolling Volatility, Sharpe Ratio)  
- Dockerized environment for easy deployment  
- CI/CD integration using GitHub Actions  

---

## 📁 Repository Structure

systematic-multi-asset-trading-devops/
│
├─ main.py # Main script to run the simulation
├─ Dockerfile # Docker configuration
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
├─ .dockerignore # Files to ignore in Docker build
├─ assets.py # Asset data handling
├─ portfolio.py # Portfolio computation
├─ strategy.py # Portfolio strategies
├─ sim_engine.py # Simulation engine
├─ simulator.py # Portfolio simulator
├─ transaction_costs.py # Transaction cost application
├─ stress_testing.py # Stress testing module
├─ risk_metrics.py # Risk metrics calculation
├─ visualization.py # Visualization functions
├─ ml_models.py # Machine learning models (optional)
├─ results/ # Output folder for results (generated)
├─ data/ # Historical price data
├─ logs/ # Logs (optional)
├─ .github/workflows/ # CI/CD workflow for GitHub Actions
└─ tests/ # Unit tests (optional)


---

## ⚡ Features

1. Portfolio Analysis
   - Computes returns, volatility, Sharpe ratio
   - Supports multiple weighting strategies  

2. Simulation
   - Forward simulation of portfolio returns  
   - Supports monthly rebalancing (`M`)  

3. Transaction Costs
   - Applies trading cost rates to net returns  

4. Stress Testing
   - Scenarios: Market Crash (-30%, -50%), Bull Shock (+20%), Volatility Spike, Moderate Drawdown  
   - Generates scenario returns and metrics  

5. Risk Metrics
   - Max Drawdown, VaR, CVaR, rolling volatility, Sharpe ratio  

6. Visualizations
   - Cumulative returns, rolling volatility, rolling Sharpe ratio  

---

## 🐳 Docker

Build and run the project in a container:

```bash
# Build Docker image
docker build -t systematic-multi-asset-trading .

# Run the simulation inside Docker
docker run --rm systematic-multi-asset-trading

✅ The results are saved in the results/ folder inside the container.

⚙️ GitHub Actions CI/CD

Workflow file: .github/workflows/docker-ci.yml

Automatically builds Docker image and runs the simulation on every push to main.

Example workflow triggers:
name: Docker CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t systematic-multi-asset-trading .
      - name: Run container
        run: docker run --rm systematic-multi-asset-trading
📊 Results

Simulation Output: Portfolio returns and cumulative returns

Transaction Costs: Net returns after applying trading costs

Stress Testing: Scenario returns and metrics

Risk Metrics: Max Drawdown, VaR, CVaR, Rolling Volatility, Sharpe Ratio

All results are stored in the results/ folder.

⚡ Getting Started

1. Clone the repository:

git clone https://github.com/MoMkhan1/systematic-multi-asset-trading-devops.git
cd systematic-multi-asset-trading-devops

2. Install dependencies:

pip install -r requirements.txt

3. Run the simulation:

python main.py

Or using Docker:

docker build -t systematic-multi-asset-trading .
docker run --rm systematic-multi-asset-trading

☁️ AWS & Deployment (Optional)

Docker container can be deployed to:

AWS ECS or EKS for scalable containerized execution

AWS EC2 for single-instance deployment

Use GitHub Actions to automate CI/CD for AWS deployment.

📄 License

This project is licensed under MIT License.

📌 Author

Mohammed Moniruzzaman Khan
Github:https://github.com/MoMkhan1
LinkedIn: https://www.linkedin.com/in/mohammed-moniruzzaman-khan



