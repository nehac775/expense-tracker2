# 💰 Expense Tracker (Python + Streamlit)

A simple yet powerful expense tracker built with Python and Streamlit. Add daily expenses, categorize them, and visualize your spending with interactive charts.

## ✨ Features
- Add expenses (amount, category, description)
- View all expenses in a table
- Summary by category
- Interactive charts: pie chart and bar chart over time
- Export data to CSV
- Runs fully on Streamlit Cloud

## 🚀 Quickstart (Local)
```bash
git clone <YOUR_REPO_URL>
cd expense-tracker

# Create virtual env
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate  # Windows

pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deployment
- Push to GitHub
- Deploy on [Streamlit Cloud](https://streamlit.io/cloud) with `app.py` as entrypoint
