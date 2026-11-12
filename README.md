# Customer Churn Analysis (Python)

An exploratory analysis of 3,000 telecom customers to find **who is leaving and why**, ending with retention recommendations.

> **Note:** The dataset is synthetic (generated with a fixed random seed in `generate_data.py`) so the project is reproducible with no downloads. You can swap in a real churn dataset (e.g. the Telco Customer Churn dataset on Kaggle) with similar columns.

## Business Questions
1. What is the overall churn rate?
2. Which customer segments churn the most?
3. Do tenure, contract type, and support calls relate to churn?

## Key Findings
| Metric | Result |
|---|---|
| Overall churn rate | 42.4% |
| Month-to-month contract churn | 63.9% (vs 5.7% for two-year) |
| Churn in first 12 months of tenure | 64.5% (vs 3.1% after 48 months) |
| Customers with 4+ support calls | 55.1% churn (vs 31.9% with none) |
| Month-to-month share of all churners | 82.6% |

- **Contract type is the biggest driver:** month-to-month customers are 55% of the base but account for 82.6% of churners.
- **New customers are the most at risk:** churn falls steadily with tenure.
- **Support friction matters:** churn rises with every additional support call.
- **Electronic check payers churn more** (46.1%) than credit card payers (38.0%).
- **Price alone is not the story:** average monthly charges are similar for churned ($64.9) and retained ($62.7) customers.

## Recommendations
1. Offer discounts or perks to move month-to-month customers onto 1- or 2-year plans.
2. Build an onboarding and check-in program for customers in their first year.
3. Flag customers with 3+ support calls for proactive outreach.
4. Encourage automatic card payments over electronic checks.

## Charts
![Churn by contract](charts/churn_by_contract.png)
![Churn by tenure](charts/churn_by_tenure.png)
![Churn by support calls](charts/churn_by_support_calls.png)

## How to Run
```bash
pip install -r requirements.txt
python generate_data.py   # creates data/customers.csv
python analysis.py        # prints metrics, saves charts/
```

## Tech Stack
Python, pandas, NumPy, Matplotlib

## Project Structure
```
├── data/customers.csv
├── charts/
├── generate_data.py
├── analysis.py
├── requirements.txt
└── README.md
```
