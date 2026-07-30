from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="MSFT Financial Statement Dashboard",
    page_icon="📊",
    layout="wide",
)

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("msft_analysis.csv")
    return df

df = load_data()

# Sort just in case
df = df.sort_values("Fiscal Year").reset_index(drop=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Microsoft Dashboard")
st.sidebar.caption("Financial Statement Analysis | FY2021–FY2025")

metric_options = [
    "Revenue",
    "Gross Profit",
    "Operating Income",
    "Net Income",
    "Free Cash Flow",
    "Revenue Growth %",
    "Net Margin %",
    "Operating Margin %",
    "Gross Margin %",
    "ROE %",
    "ROA %",
    "Current Ratio",
    "Debt to Equity",
]

selected_metric = st.sidebar.selectbox(
    "Choose a metric",
    metric_options,
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.markdown("### What this dashboard shows")
st.sidebar.write(
    "A 5-year view of Microsoft's financial performance, profitability, liquidity, and returns."
)

# -----------------------------
# Title
# -----------------------------
st.title("Microsoft Financial Statement Analysis")
st.caption("A 5-year dashboard built from SEC company facts data.")

# -----------------------------
# KPI Cards
# -----------------------------
latest = df.iloc[-1]
previous = df.iloc[-2]

def format_big_number(x):
    return f"${x/1e9:,.1f}B"

def format_pct(x):
    return f"{x:.1f}%"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue",
        format_big_number(latest["Revenue"]),
        delta=f'{((latest["Revenue"] / previous["Revenue"]) - 1) * 100:.1f}%',
    )

with col2:
    st.metric(
        "Net Income",
        format_big_number(latest["Net Income"]),
        delta=f'{((latest["Net Income"] / previous["Net Income"]) - 1) * 100:.1f}%',
    )

with col3:
    st.metric(
        "Free Cash Flow",
        format_big_number(latest["Free Cash Flow"]),
        delta=f'{((latest["Free Cash Flow"] / previous["Free Cash Flow"]) - 1) * 100:.1f}%',
    )

with col4:
    st.metric(
        "ROE",
        format_pct(latest["ROE %"]),
        delta=f'{latest["ROE %"] - previous["ROE %"]:.1f} pts',
    )

st.markdown("---")

# -----------------------------
# Main chart
# -----------------------------
left, right = st.columns([2, 1])

with left:
    fig = px.line(
        df,
        x="Fiscal Year",
        y=selected_metric,
        markers=True,
        title=f"{selected_metric} Over Time",
    )
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Latest Year Snapshot")
    snapshot = df[[
        "Fiscal Year",
        "Revenue",
        "Net Income",
        "Free Cash Flow",
        "Gross Margin %",
        "Operating Margin %",
        "Net Margin %",
        "Current Ratio",
        "Debt to Equity",
        "ROE %",
    ]].tail(1)

    st.dataframe(snapshot, use_container_width=True, hide_index=True)

# -----------------------------
# Charts row
# -----------------------------
st.subheader("Key Trends")

col5, col6 = st.columns(2)

with col5:
    revenue_fig = px.bar(
        df,
        x="Fiscal Year",
        y="Revenue",
        title="Revenue",
        text_auto=".2s",
    )
    revenue_fig.update_layout(template="plotly_white")
    st.plotly_chart(revenue_fig, use_container_width=True)

with col6:
    fcf_fig = px.bar(
        df,
        x="Fiscal Year",
        y="Free Cash Flow",
        title="Free Cash Flow",
        text_auto=".2s",
    )
    fcf_fig.update_layout(template="plotly_white")
    st.plotly_chart(fcf_fig, use_container_width=True)

# -----------------------------
# Profitability chart
# -----------------------------
margins = df[[
    "Fiscal Year",
    "Gross Margin %",
    "Operating Margin %",
    "Net Margin %",
]].melt(
    id_vars="Fiscal Year",
    var_name="Metric",
    value_name="Percent",
)

margin_fig = px.line(
    margins,
    x="Fiscal Year",
    y="Percent",
    color="Metric",
    markers=True,
    title="Profitability Margins",
)
margin_fig.update_layout(template="plotly_white")
st.plotly_chart(margin_fig, use_container_width=True)

# -----------------------------
# Ratios table
# -----------------------------
st.subheader("Financial Ratios")

ratio_table = df[[
    "Fiscal Year",
    "Current Ratio",
    "Debt to Equity",
    "ROA %",
    "ROE %",
    "Revenue Growth %",
    "FCF Growth %",
]].copy()

st.dataframe(ratio_table, use_container_width=True, hide_index=True)

# -----------------------------
# Simple insights
# -----------------------------
st.subheader("Key Observations")

revenue_cagr = ((df["Revenue"].iloc[-1] / df["Revenue"].iloc[0]) ** (1 / (len(df) - 1)) - 1) * 100
fcf_change = ((df["Free Cash Flow"].iloc[-1] / df["Free Cash Flow"].iloc[0]) - 1) * 100
roe_latest = df["ROE %"].iloc[-1]

st.write(f"- Revenue grew at an approximate **{revenue_cagr:.1f}% CAGR** over the period.")
st.write(f"- Free cash flow changed by about **{fcf_change:.1f}%** from FY2021 to FY2025.")
st.write(f"- Latest ROE was **{roe_latest:.1f}%**, which is strong for a large-cap company.")

st.markdown("---")
st.caption("Source: SEC company facts data pulled into pandas and analyzed in Python.")