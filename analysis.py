"""Customer churn analysis: KPIs, drivers, charts."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customers.csv")
print("Rows:", len(df), "| Missing:", int(df.isna().sum().sum()),
      "| Duplicate IDs:", int(df.customer_id.duplicated().sum()))

df["churned"] = (df.churn == "Yes").astype(int)
df["tenure_group"] = pd.cut(df.tenure_months, [0, 12, 24, 48, 72],
                            labels=["0-12", "13-24", "25-48", "49-72"])
df["calls_group"] = df.support_calls.clip(upper=4).map(
    lambda x: "4+" if x == 4 else str(x))

overall = df.churned.mean()
by_contract = df.groupby("contract").churned.mean().sort_values(ascending=False)
by_tenure = df.groupby("tenure_group", observed=True).churned.mean()
by_calls = df.groupby("calls_group").churned.mean()
by_payment = df.groupby("payment_method").churned.mean().sort_values(ascending=False)
by_internet = df.groupby("internet_service").churned.mean().sort_values(ascending=False)
avg_charge = df.groupby("churn").monthly_charges.mean()

print(f"Overall churn: {overall:.1%}")
for name, s in [("contract", by_contract), ("tenure", by_tenure),
                ("calls", by_calls), ("payment", by_payment), ("internet", by_internet)]:
    print(f"\nChurn by {name}:\n{(s*100).round(1).to_string()}")
print("\nAvg monthly charge:\n", avg_charge.round(1).to_string())
mtm = df[df.contract == "Month-to-month"]
print(f"\nMonth-to-month share of customers: {len(mtm)/len(df):.1%}")
print(f"Month-to-month share of churners: {mtm.churned.sum()/df.churned.sum():.1%}")

plt.style.use("seaborn-v0_8-whitegrid")

def bar(series, title, path, color):
    fig, ax = plt.subplots(figsize=(7, 4))
    (series * 100).plot.bar(ax=ax, color=color, rot=0)
    ax.set_title(title); ax.set_ylabel("Churn rate (%)")
    ax.axhline(overall * 100, ls="--", color="gray", label=f"Average ({overall:.0%})")
    ax.legend(); fig.tight_layout(); fig.savefig(path, dpi=150); plt.close()

bar(by_contract, "Churn Rate by Contract Type", "charts/churn_by_contract.png", "#dc2626")
bar(by_tenure, "Churn Rate by Tenure (months)", "charts/churn_by_tenure.png", "#2563eb")
bar(by_calls, "Churn Rate by Support Calls", "charts/churn_by_support_calls.png", "#f59e0b")
