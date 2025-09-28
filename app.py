import streamlit as st
import pandas as pd
import src.tracker as tracker
import src.visualizer as visualizer
from datetime import datetime

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

st.title("💰 Expense Tracker")
st.write("Track your expenses by category and visualize your spending.")

# Load data
df = tracker.load_expenses()

# Sidebar - Add new expense
st.sidebar.header("Add Expense")
amount = st.sidebar.number_input("Amount", min_value=0.0, step=0.01)
category = st.sidebar.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
description = st.sidebar.text_input("Description")
if st.sidebar.button("Add Expense"):
    tracker.add_expense(amount, category, description)
    st.sidebar.success("Expense added!")
    st.experimental_rerun()

# Main - Show data and visualizations
st.subheader("All Expenses")
st.dataframe(df)

st.subheader("Summary by Category")
summary = df.groupby("Category")["Amount"].sum().reset_index()
st.dataframe(summary)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(visualizer.plot_category_pie(summary), use_container_width=True)
with col2:
    st.plotly_chart(visualizer.plot_expenses_over_time(df), use_container_width=True)

# Export button
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "expenses.csv", "text/csv")
