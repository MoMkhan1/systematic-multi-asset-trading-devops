import numpy as np
import pandas as pd

class StressTester:
    """
    Stress testing engine for portfolio returns.

    Applies predefined stress scenarios and computes:
    - cumulative return
    - max drawdown
    - volatility
    - final return
    """

    def __init__(self, returns: pd.Series | pd.DataFrame):
        """
        Parameters
        ----------
        returns : pd.Series or pd.DataFrame
            Portfolio net returns time series
        """
        if isinstance(returns, pd.Series):
            self.returns = returns.to_frame(name="portfolio")
        else:
            self.returns = returns.copy()

        self.scenarios = self._define_scenarios()

    # ----------------------------
    # Scenario definitions
    # ----------------------------
    def _define_scenarios(self):
        """
        Define stress scenarios as shock multipliers
        """
        return {
            "Market Crash (-30%)": -0.30,
            "Severe Crash (-50%)": -0.50,
            "Moderate Drawdown (-15%)": -0.15,
            "Bull Shock (+20%)": 0.20,
            "Volatility Spike": "vol_spike",
        }

    # ----------------------------
    # Apply scenarios
    # ----------------------------
    def apply_scenarios(self):
        scenario_returns = {}

        base = self.returns.iloc[:, 0]

        for name, shock in self.scenarios.items():

            if shock == "vol_spike":
                # volatility amplification
                stressed = base * 2.5
            else:
                stressed = base + shock

            scenario_returns[name] = stressed

        scenario_df = pd.DataFrame(scenario_returns, index=self.returns.index)
        return scenario_df

    # ----------------------------
    # Metrics
    # ----------------------------
    def compute_metrics(self, scenario_returns: pd.DataFrame):
        metrics_rows = []

        for col in scenario_returns.columns:
            r = scenario_returns[col]

            cum_returns = (1 + r).cumprod()
            running_max = cum_returns.cummax()
            drawdown = 1 - cum_returns / running_max

            metrics_rows.append({
                "Scenario": col,
                "Final Cumulative Return": float(cum_returns.iloc[-1]),
                "Max Drawdown": float(drawdown.max()),
                "Volatility": float(r.std()),
                "Mean Return": float(r.mean())
            })

        # ✅ pandas 2.x compatible (NO append)
        metrics_df = pd.DataFrame(metrics_rows)
        return metrics_df

    # ----------------------------
    # Main runner
    # ----------------------------
    def run(self):
        scenario_returns = self.apply_scenarios()
        metrics = self.compute_metrics(scenario_returns)

        return {
            "scenario_returns": scenario_returns,
            "metrics": metrics
        }
