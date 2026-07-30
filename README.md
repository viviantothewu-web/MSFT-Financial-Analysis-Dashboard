# 📊 Microsoft Financial Statement Analysis Dashboard

## Overview

This project analyzes **Microsoft Corporation's financial performance over the last five fiscal years (FY2021–FY2025)** using publicly available SEC financial statement data. The goal is to transform raw financial data into meaningful business insights through Python, data analysis, and an interactive Streamlit dashboard.

The dashboard is designed for both technical and non-technical users. Each financial metric is accompanied by plain-English explanations so users without a finance background can understand Microsoft's financial performance.

---

## Project Objectives

* Retrieve Microsoft's financial statement data directly from the SEC Company Facts API.
* Clean and organize the data using Python and pandas.
* Calculate key financial ratios and performance metrics.
* Build interactive visualizations with Plotly.
* Develop a professional dashboard using Streamlit.
* Present financial insights in an accessible, easy-to-understand format.

---

## Dashboard Features

### Executive KPI Cards

Displays Microsoft's latest:

* Revenue
* Net Income
* Free Cash Flow
* Return on Equity (ROE)

Each KPI includes year-over-year changes and a brief explanation.

### Interactive Financial Analysis

Users can explore:

* Revenue
* Gross Profit
* Operating Income
* Net Income
* Free Cash Flow
* Revenue Growth
* Gross Margin
* Operating Margin
* Net Margin
* Return on Assets (ROA)
* Return on Equity (ROE)
* Current Ratio
* Debt-to-Equity Ratio

---

### Financial Visualizations

The dashboard includes:

* Revenue Trend
* Net Income Trend
* Free Cash Flow Trend
* Profitability Margins
* Financial Ratio Summary

Each chart includes descriptions explaining:

* What the metric measures
* Why it matters
* How to interpret changes over time

---

### Beginner-Friendly Financial Glossary

A built-in glossary explains common financial terms such as:

* Revenue
* Gross Profit
* Net Income
* Free Cash Flow
* Gross Margin
* Current Ratio
* Debt-to-Equity
* ROA
* ROE

This makes the dashboard accessible to users without prior finance knowledge.

---

## Technologies Used

* **Python**
* **pandas**
* **Plotly**
* **Streamlit**
* **Requests**
* **SEC Company Facts API**

---

## Project Structure

```text
msft-financial-analysis-dashboard/

├── data/
│   ├── raw/
│   └── processed/
│       ├── msft_financials_5y.csv
│       └── msft_analysis.csv
│
├── src/
│   ├── fetch_msft_financials.py
│   ├── calculate_metrics.py
│   └── create_charts.py
│
├── dashboard/
│   └── app.py
│
├── charts/
├── README.md
└── requirements.txt
```

---

## Data Source

Financial statement data is retrieved from the **U.S. Securities and Exchange Commission (SEC) Company Facts API**, which provides structured XBRL financial information from companies' annual filings (Form 10-K).

Company analyzed:

* Microsoft Corporation (NASDAQ: MSFT)

---

## Financial Metrics Calculated

### Growth Metrics

* Revenue Growth %
* Net Income Growth %
* Free Cash Flow Growth %

### Profitability

* Gross Margin
* Operating Margin
* Net Margin

### Liquidity

* Current Ratio

### Leverage

* Debt-to-Equity Ratio

### Efficiency

* Return on Assets (ROA)
* Return on Equity (ROE)

---

## Key Insights

From the five-year analysis:

* Microsoft demonstrated consistent revenue growth over the analysis period.
* Operating and net margins remained strong, reflecting efficient operations.
* Free cash flow increased significantly, highlighting the company's ability to generate cash from its core business.
* Return on Equity remained high, indicating effective use of shareholder capital.
* Microsoft maintained a strong financial position while continuing to invest heavily in growth initiatives.

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Fetch financial data

```bash
python src/fetch_msft_financials.py
```

### Calculate financial metrics

```bash
python src/calculate_metrics.py
```

### Launch the dashboard

```bash
streamlit run dashboard/app.py
```

---

## Skills Demonstrated

This project demonstrates experience with:

* Financial statement analysis
* Financial ratio analysis
* Data cleaning and transformation
* REST API integration
* Data visualization
* Dashboard development
* Business storytelling with data
* Python programming
* Git and GitHub

---

## Future Improvements

Potential enhancements include:

* Multi-company comparison (e.g., Apple, Microsoft, Amazon)
* Quarterly financial analysis
* Discounted Cash Flow (DCF) valuation model
* Automated PDF reporting
* Industry benchmarking
* Forecasting using time-series models
* Enhanced dashboard filtering and customization

---

## Disclaimer

This project was created for educational and portfolio purposes. Financial data is sourced from publicly available SEC filings. The dashboard is intended to demonstrate financial analysis and data visualization techniques and should not be interpreted as investment advice.
