"""Generate a reproducible synthetic telecom customer dataset (seeded)."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
n = 3000

contract = rng.choice(["Month-to-month", "One year", "Two year"], n, p=[0.55, 0.25, 0.20])
tenure = np.where(contract == "Month-to-month", rng.integers(1, 30, n),
         np.where(contract == "One year", rng.integers(6, 48, n), rng.integers(12, 72, n)))
internet = rng.choice(["Fiber", "DSL", "No internet"], n, p=[0.45, 0.40, 0.15])
base = {"Fiber": 85, "DSL": 55, "No internet": 25}
monthly = np.array([base[i] for i in internet]) + rng.normal(0, 8, n)
payment = rng.choice(["Credit card", "Bank transfer", "Electronic check"], n, p=[0.35, 0.30, 0.35])
calls = rng.poisson(1.5, n)

# churn probability via logistic model
z = (-1.2
     + 1.6 * (contract == "Month-to-month")
     - 1.0 * (contract == "Two year")
     - 0.03 * tenure
     + 0.012 * (monthly - 60)
     + 0.35 * calls
     + 0.4 * (payment == "Electronic check"))
p = 1 / (1 + np.exp(-z))
churn = rng.random(n) < p

df = pd.DataFrame({
    "customer_id": [f"C{10000 + i}" for i in range(n)],
    "tenure_months": tenure,
    "contract": contract,
    "internet_service": internet,
    "payment_method": payment,
    "monthly_charges": monthly.round(2),
    "support_calls": calls,
    "churn": np.where(churn, "Yes", "No"),
})
df.to_csv("data/customers.csv", index=False)
print("Saved data/customers.csv", df.shape)
