# 📊 Nifty100 Financial Intelligence Platform

A Financial Intelligence Platform built using **Python**, **SQLite**, and **Pandas** to analyze financial data of Nifty 100 companies. The project follows an end-to-end ETL workflow, beginning with data ingestion and validation, and will gradually expand into financial ratio analysis, company comparison, dashboards, and reporting.

---

## 🚀 Project Overview

The objective of this project is to build a centralized platform that processes financial information of Nifty 100 companies and converts raw Excel datasets into structured, validated, and queryable data.

The project is being developed in multiple sprints.

---

# 📅 Sprint Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 – ETL Foundation 
| Sprint 2 – Financial Ratio Engine 
| Sprint 3 – Company Analysis 
| Sprint 4 – Dashboard Development 
| Sprint 5 – Advanced Analytics
| Sprint 6 – Final Integration & Documentation

---

# ✅ Sprint 1 Deliverables

Sprint 1 focused on building the data foundation of the project.

### Completed Tasks

- Project environment setup
- Project folder structure
- Excel data loader
- Data cleaning pipeline
- Year normalization
- Ticker normalization
- Duplicate removal
- Data quality validation
- Validation report generation
- Load audit report generation
- SQLite database creation
- Loading cleaned datasets into SQLite
- Exploratory SQL queries
- Database integrity verification
- Git version control
- GitHub repository setup

---

# 📂 Datasets Used

The project processes **12 datasets**:

- Companies
- Profit & Loss
- Balance Sheet
- Cash Flow
- Analysis
- Documents
- Pros & Cons
- Financial Ratios
- Market Cap
- Peer Groups
- Sectors
- Stock Prices

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| SQLite | Database |
| OpenPyXL | Excel File Handling |
| Git | Version Control |
| GitHub | Repository Hosting |
| VS Code | Development Environment |

---

# 📁 Project Structure

```
Nifty100_Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── etl/
│   ├── reports/
│   ├── validator.py
│   ├── utils.py
│   └── query.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── main.py
├── check_db.py
├── check_fk.py
├── check_tables.py
├── run_queries.py
└── exploratory_queries.sql
```

---

# 🔄 Sprint 1 Workflow

```
Excel Files
      │
      ▼
Data Loading
      │
      ▼
Data Cleaning
      │
      ▼
Normalization
      │
      ▼
Validation Rules
      │
      ▼
SQLite Database
      │
      ▼
SQL Verification
      │
      ▼
Reports Generated
```

---

# 📊 Sprint 1 Results

Successfully:

- Loaded all project datasets
- Cleaned duplicate records
- Normalized financial years
- Normalized company ticker symbols
- Applied data quality validation rules
- Generated `validation_failures.csv`
- Generated `load_audit.csv`
- Created SQLite database
- Verified database integrity
- Executed exploratory SQL queries

---

# 📄 Reports Generated

- `load_audit.csv`
- `validation_failures.csv`
- `exploratory_queries.sql`
- `sprint1_retro.md`

---

# 🎯 Upcoming Work

Sprint 2 will focus on:

- Financial Ratio Calculations
- Profitability Analysis
- Liquidity Ratios
- Solvency Ratios
- Efficiency Ratios
- Financial Performance Insights

---

# 💻 How to Run

Clone the repository

```bash
git clone https://github.com/KushmaReddy/Nifty100-Financial-Intelligence-Platform.git
```

Move into the project folder

```bash
cd Nifty100-Financial-Intelligence-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# 📌 Project Status

**Current Sprint:** Sprint 1 ✅ Completed

The ETL pipeline has been successfully implemented and verified. The project is ready to move to Sprint 2.

---

# 👩‍💻 Author

**Kushma Reddy**

PGDM – Data Science & Business Analytics



---

## ⭐ If you found this project useful, consider giving it a star! Business Analytics
