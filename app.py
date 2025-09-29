"""
Expense Tracker (my version)

I built this to practice pandas + Streamlit, but also because I wanted
to actually track my spending habits (food vs shopping is my weak spot).

Notes:
- I hit a bug before where totals didn’t update until rerun → fixed with st.rerun().
- At some point I might swap the CSV storage for SQLite.
- TODO: recurring expenses (subscriptions) + monthly auto-report.
"""

import streamlit as st
import pandas as pd
import src.tracker as tracker
import src.visualizer as visualizer
from datetime import datetime

# --- Page setup ---
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

st.title("💰 Expense Tracker")
st.write("Track your expenses by category and visualize your spending.")

# --- Load saved data ---
# At first I forgot to persist data → everything reset on refresh.
# tracker.py handles the CSV read/write for me now.
df = tracker.load_expenses()

# --- Sidebar (input form) ---
st.sidebar.header("Add Expense")
amount = st.sidebar.number_input("Amount", min_value=0.0, step=0.01)
category = st.sidebar.selectbox(
    "Category", ["Food", "Transport", "Shopping", "Bills", "Other"]
)
description = st.sidebar.text_input("Description")

if st.sidebar.button("Add Expense"):
    # NOTE: I cast amount to float in tracker.add_expense because
    # pandas was treating it as string before and broke groupby sum.
    tracker.add_expense(amount, category, description)
    st.sidebar.success("Expense added!")
    st.rerun()  # I tried without this but the table wouldn’t refresh immediately.

# --- Main content ---
st.subheader("All Expenses")
if df.empty:
    st.info("No expenses yet. Add one in the sidebar 👉")
else:
    st.dataframe(df, use_container_width=True)

    # --- Summary ---
    st.subheader("Summary by Category")
    try:
        summary = df.groupby("Category")["Amount"].sum().reset_index()
        st.dataframe(summary, use_container_width=True)
    except Exception as e:
        # leaving this here in case grouping breaks again
        st.error(f"Error creating summary: {e}")

    # --- Visuals ---
    col1, col2 = st.columns(2)
    with col1:
        # Pie chart is nice but gets cramped with too many categories.
        st.plotly_chart(visualizer.plot_category_pie(summary), use_container_width=True)
    with col2:
        # This line chart helps me see spending trends over time.
        st.plotly_chart(visualizer.plot_expenses_over_time(df), use_container_width=True)

# --- Export ---
# CSV export saved me when I accidentally deleted expenses.
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download CSV", csv, "expenses.csv", "text/csv")
