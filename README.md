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

# ✅ Sprint 5 – Financial Intelligence, NLP & Automated Reports

## 🎯 Objective

Sprint 5 focused on transforming raw financial data into intelligent insights by combining **Natural Language Processing (NLP)**, **Financial Intelligence**, **Company Ranking**, and **Automated PDF Report Generation**.

The objective was to automate the generation of company-level and sector-level investment reports while enhancing the platform with intelligent financial analysis.

---

# 🧠 NLP Financial Intelligence Module

Developed an NLP pipeline to extract structured financial information from unstructured textual analysis.

### Features Implemented

- Financial Analysis Parser
- Regex-Based Text Extraction
- CAGR Information Extraction
- ROE Extraction
- Stock Price CAGR Extraction
- Profit Growth Extraction
- Sales Growth Extraction
- Automatic Parsing Validation
- Parsing Failure Detection
- Confidence-Based Data Cleaning

### Reports Generated

- analysis_parsed.csv
- parse_failures.csv

---

# 📈 Pros & Cons Intelligence Engine

Built an automated intelligence engine that converts raw textual company analysis into structured investment insights.

### Features

- Pros Extraction
- Cons Extraction
- Company-wise Aggregation
- Duplicate Removal
- Summary Generation

### Reports Generated

- pros_cons_generated.csv

---

# 💰 Cash Flow Intelligence Engine

Developed an intelligent cash flow analyzer to evaluate a company's financial health.

### Features

- Operating Cash Flow Analysis
- Investing Cash Flow Analysis
- Financing Cash Flow Analysis
- Cash Flow Classification
- Capital Allocation Detection
- Strong Cash Flow Identification
- Weak Cash Flow Identification

### Intelligence Labels

- Strong Operating Cash Flow
- Investing for Future Growth
- Debt Repayment
- Shareholder Returns
- Weak Cash Flow

### Reports Generated

- cashflow_intelligence.xlsx

---

# 🚨 Financial Distress Detection

Implemented an automated Financial Distress Engine to identify financially weak companies.

### Metrics Used

- ROE
- ROCE
- Debt-to-Equity Ratio
- Interest Coverage Ratio
- Free Cash Flow
- Debt-Free Status
- High Leverage Flag

### Features

- Distress Score Calculation
- Financial Health Classification
- Company Risk Identification
- Early Warning Detection

### Output

- distress_alerts.csv

---

# 🏆 Company Ranking Engine

Built a financial scoring system to rank companies based on multiple financial metrics.

### Ranking Parameters

- ROE
- ROCE
- Debt-to-Equity
- Interest Coverage
- Free Cash Flow
- Debt-Free Flag
- High Leverage Flag

### Rating Categories

- Excellent
- Good
- Average
- Weak

### Reports Generated

- company_rankings.xlsx

---

# 📄 Company Tearsheet Generator

Developed an automated PDF generator for creating professional company reports.

Each tearsheet includes:

- Company Overview
- Business Description
- ROE
- ROCE
- Face Value
- Book Value
- Pros
- Cons

Generated PDF reports for all companies in the dataset.

### Output Folder

```
reports/
└── tearsheets/
```

---

# 🏢 Sector Report Generator

Generated sector-level analytical reports.

Each report includes:

- Sector Overview
- Company List
- Median ROE
- Median ROCE
- Median P/E
- Median P/B
- Sector Statistics

Generated reports for all sectors available in the dataset.

### Output Folder

```
reports/
└── sector/
```

---

# 📑 Portfolio Summary Report

Created an executive portfolio summary containing:

- Company Name
- Sector
- ROE
- ROCE
- Investment Score
- Company Rating

### Output

```
reports/
└── portfolio/
    └── portfolio_summary.pdf
```

---

# 📊 Reports Generated

### CSV Reports

- analysis_parsed.csv
- parse_failures.csv
- pros_cons_generated.csv
- distress_alerts.csv

### Excel Reports

- company_rankings.xlsx
- cashflow_intelligence.xlsx

### PDF Reports

- Company Tearsheets
- Sector Reports
- Portfolio Summary Report

---

# 🎯 Sprint 5 Achievements

Successfully implemented:

- NLP-Based Financial Text Parsing
- Automated Pros & Cons Generation
- Cash Flow Intelligence Engine
- Financial Distress Detection
- Company Ranking System
- Automated Company PDF Reports
- Sector-Level PDF Reports
- Portfolio Summary Report

---

# 🚀 Skills Demonstrated

### Programming

- Python
- Object-Oriented Programming

### Data Processing

- Pandas
- NumPy

### Database

- SQLite
- SQL Queries

### NLP

- Regular Expressions (Regex)
- Text Parsing
- Structured Information Extraction

### Financial Analytics

- Financial Ratio Analysis
- Cash Flow Analysis
- Company Ranking
- Financial Health Assessment

### Reporting

- ReportLab PDF Generation
- Excel Report Automation
- Automated Portfolio Reports

---

# 📌 Sprint 5 Deliverables

| Deliverable | Status |
|-------------|--------|
| NLP Parser | ✅ Completed |
| Pros & Cons Generator | ✅ Completed |
| Cash Flow Intelligence | ✅ Completed |
| Financial Distress Engine | ✅ Completed |
| Company Ranking Engine | ✅ Completed |
| Company Tearsheet Generator | ✅ Completed |
| Batch Tearsheet Generation | ✅ Completed |
| Sector Report Generator | ✅ Completed |
| Portfolio Summary PDF | ✅ Completed |

---

## 🎉 Sprint 5 Summary

Sprint 5 transformed the platform from a financial analytics engine into a **Financial Intelligence Platform** capable of automatically generating structured insights, ranking companies, detecting financial distress, and producing professional PDF reports for companies, sectors, and portfolios.
---

# 👩‍💻 Author

**Kushma Reddy**

PGDM – Data Science & Business Analytics

ISBR Business School

---

⭐ If you found this project useful, consider giving it a star!
