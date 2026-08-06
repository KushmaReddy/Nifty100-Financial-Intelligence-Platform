# 📊 N100 Financial Intelligence Platform

Python | SQLite | Pandas | Streamlit | Plotly | Financial Analytics | Data Engineering

A Financial Intelligence Platform built using Python, SQLite, Pandas and Streamlit to analyze financial data of Nifty 100 companies. The project follows an end-to-end ETL pipeline, financial ratio engine, company intelligence modules, and an interactive dashboard for investment analysis.

---

# 🚀 Project Overview

The objective of this project is to build a centralized financial intelligence platform that converts raw financial statements of Nifty100 companies into structured, validated, queryable and interactive analytical insights.

The platform consists of:

- ETL Pipeline
- Data Validation Framework
- Financial Ratio Engine
- Company Analytics
- Peer Comparison
- Stock Screener
- Interactive Dashboard
- Valuation Module
- Downloadable Reports

---

# 📅 Sprint Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 – ETL Foundation | ✅ Completed |
| Sprint 2 – Financial Ratio Engine | ✅ Completed |
| Sprint 3 – Company Intelligence & Analytics | ✅ Completed |
| Sprint 4 – Dashboard & Valuation Module | ✅ Completed |

---

# ✅ Sprint 1 – ETL Foundation

## Objective

Built the complete ETL pipeline for loading, validating and storing financial datasets.

### Features Implemented

- Project environment setup
- Folder structure
- Excel loader
- Data cleaning
- Duplicate removal
- Missing value handling
- Year normalization
- Company ticker normalization
- Validation framework
- Data quality rules
- SQLite database creation
- Database loading
- SQL verification
- Exploratory SQL queries
- Load audit generation
- Validation reports
- Git version control

### Reports Generated

- load_audit.csv
- validation_failures.csv
- sprint1_retro.md

---

# ✅ Sprint 2 – Financial Ratio Engine

## Objective

Developed a complete Financial Ratio Engine for all Nifty100 companies.

### Profitability Ratios

- ROE
- ROCE
- ROA
- Net Profit Margin
- Operating Profit Margin

### Leverage Ratios

- Debt to Equity
- Interest Coverage Ratio
- Debt Free Flag
- High Leverage Flag

### Growth Metrics

- Revenue CAGR
- PAT CAGR
- EPS CAGR
- 3-Year CAGR
- 5-Year CAGR
- 10-Year CAGR
- Turnaround Detection

### Cash Flow KPIs

- Free Cash Flow
- FCF Conversion
- CFO Quality Score
- CapEx Intensity
- Capital Allocation Classification

### Validation

- ROE validation
- ROCE validation
- OPM validation
- Edge case testing
- Manual verification

### Reports Generated

- financial_ratios.csv
- cagr_report.csv
- cashflow_kpis.csv
- capital_allocation.csv
- roe_roce_validation.csv
- ratio_edge_cases.log

---

# ✅ Sprint 3 – Company Intelligence & Analytics

## Objective

Built advanced analytical modules to compare companies and generate investment insights.

### Modules Developed

### Company Profile

- Company overview
- Sector information
- Business description
- Key financial metrics

### Peer Comparison

- Peer group identification
- Industry benchmarking
- Financial comparison
- Radar chart generation

### Stock Screener

- Multi-factor screening
- Quality filters
- Growth filters
- Dividend filters
- Value filters

### Trend Analysis

- Revenue trend
- Profit trend
- ROE trend
- ROCE trend
- Multi-year analysis

### Reports Generated

- peer_comparison.xlsx
- screener_results.csv
- radar chart outputs
- sector analytics

---

# ✅ Sprint 4 – Dashboard & Valuation

## Objective

Built a complete Streamlit Financial Dashboard and Valuation Engine.

### Dashboard Pages

- Home Dashboard
- Company Profile
- Stock Screener
- Peer Comparison
- Trend Analysis
- Sector Analysis
- Capital Allocation
- Reports

### Dashboard Features

- Interactive charts using Plotly
- Sidebar filters
- Company search
- KPI cards
- Sector insights
- Download reports
- Responsive navigation

### Valuation Module

Calculated

- FCF Yield
- Sector Median P/E
- Sector Median P/B
- Sector Median EV/EBITDA

Generated valuation labels

- Undervalued
- Fairly Valued
- Overvalued

### Reports Generated

- valuation_summary.xlsx
- valuation_flags.csv

### Testing

Completed

- Dashboard testing
- Screen validation
- Company search testing
- CSV export testing
- Edge case testing
- Integration testing

---

# 📂 Datasets Used

The project processes multiple financial datasets including

- Companies
- Profit & Loss
- Balance Sheet
- Cash Flow
- Analysis
- Documents
- Pros & Cons
- Financial Ratios
- Market Capitalization
- Peer Groups
- Sectors
- Stock Prices

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| SQLite | Database |
| Streamlit | Dashboard Development |
| Plotly | Interactive Charts |
| OpenPyXL | Excel Handling |
| Git | Version Control |
| GitHub | Repository Hosting |
| VS Code | Development |

---

# 📁 Project Structure

```
Nifty100_Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── db/
│
├── outputs/
│
├── src/
│   ├── analytics/
│   ├── dashboard/
│   ├── etl/
│   ├── reports/
│   ├── validator.py
│   ├── utils.py
│
├── tests/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# 📊 Reports Generated

- load_audit.csv
- validation_failures.csv
- financial_ratios.csv
- cagr_report.csv
- cashflow_kpis.csv
- capital_allocation.csv
- peer_comparison.xlsx
- screener_results.csv
- valuation_summary.xlsx
- valuation_flags.csv

---

# ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/KushmaReddy/N100-Financial-Intelligence-Platform.git
```

Navigate to project

```bash
cd N100-Financial-Intelligence-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

# 🎯 Key Features

- ETL Pipeline
- Data Validation
- Financial Ratio Engine
- CAGR Analysis
- Free Cash Flow Analysis
- Company Intelligence
- Peer Comparison
- Stock Screener
- Trend Analysis
- Sector Analysis
- Capital Allocation
- Interactive Dashboard
- Valuation Engine
- Excel Report Generation

---

# 📌 Current Project Status

## ✅ Sprint 1 Completed
## ✅ Sprint 2 Completed
## ✅ Sprint 3 Completed
## ✅ Sprint 4 Completed

The Financial Intelligence Platform now includes a complete ETL pipeline, financial analytics engine, company intelligence modules, interactive Streamlit dashboard, valuation engine and downloadable reports.

---

# 👩‍💻 Author

**Kushma Reddy**

PGDM – Data Science & Business Analytics

ISBR Business School

---

⭐ If you found this project useful, consider giving it a star!