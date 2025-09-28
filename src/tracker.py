import pandas as pd
from datetime import datetime
import os

DATA_PATH = "data/expenses.csv"

def load_expenses():
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
    return pd.read_csv(DATA_PATH)

def add_expense(amount, category, description):
    df = load_expenses()
    new_entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Amount": amount,
        "Category": category,
        "Description": description
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

def export_expenses(path="expenses_export.csv"):
    df = load_expenses()
    df.to_csv(path, index=False)
