import plotly.express as px
import pandas as pd

def plot_category_pie(summary_df):
    if summary_df.empty:
        return px.pie(values=[1], names=["No data"], title="No expenses yet")
    return px.pie(summary_df, values="Amount", names="Category", title="Expenses by Category")

def plot_expenses_over_time(df):
    if df.empty:
        return px.bar(title="No expenses yet")
    df["Date"] = pd.to_datetime(df["Date"])
    grouped = df.groupby(df["Date"].dt.date)["Amount"].sum().reset_index()
    return px.bar(grouped, x="Date", y="Amount", title="Expenses Over Time")
