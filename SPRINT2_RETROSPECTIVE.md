# Sprint 2 Retrospective

## Project

N100 Financial Intelligence Platform

## Sprint

Sprint 2 (Days 08 – 14)

---

# Sprint Goal

The primary objective of Sprint 2 was to build a reusable Financial Ratio Engine capable of generating key financial KPIs for every company and every financial year available in the Nifty100 dataset.

The sprint focused on:

- Profitability analysis
- Leverage analysis
- Efficiency analysis
- Growth analysis
- Cash Flow analytics
- Validation
- Database population
- Testing
- Financial sector handling

The final deliverable was a validated financial analytics engine capable of producing reusable financial KPIs for further reporting and dashboard development.

---

# Sprint Objectives

The objectives assigned for Sprint 2 were:

- Calculate profitability ratios
- Calculate leverage ratios
- Calculate efficiency ratios
- Calculate CAGR metrics
- Generate Cash Flow KPIs
- Populate the financial_ratios table
- Validate calculated KPIs
- Handle edge cases
- Perform SQL verification
- Complete testing
- Prepare sprint documentation

---

# Work Completed

## Day 08 – Profitability Ratios

Implemented the complete profitability ratio engine.

The following KPIs were calculated:

- Net Profit Margin
- Operating Profit Margin
- Return on Equity (ROE)
- Return on Capital Employed (ROCE)
- Return on Assets (ROA)
- EBIT

Additional implementation:

- Division-by-zero protection
- Missing value handling
- OPM cross-validation
- Validation log generation

---

## Day 09 – Leverage & Efficiency Ratios

Implemented leverage and operational efficiency KPIs.

The following metrics were added:

- Debt to Equity Ratio
- Interest Coverage Ratio
- Net Debt
- Asset Turnover Ratio
- Debt Free Flag
- High Leverage Flag

Implemented Financial Sector carve-out.

Banks, NBFCs and Insurance companies are no longer flagged as High Leverage even when Debt-to-Equity exceeds the normal threshold.

Integrated the sectors table into the ratio engine for sector-aware calculations.

---

## Day 10 – CAGR Analytics

Developed CAGR Engine.

Calculated:

- Revenue CAGR
- PAT CAGR
- EPS CAGR

Supported:

- 3-Year CAGR
- 5-Year CAGR
- 10-Year CAGR

Handled edge cases:

- Zero base
- Negative values
- Turnaround companies
- Insufficient history

Generated:

- cagr_report.csv

---

## Day 11 – Cash Flow Analytics

Implemented Cash Flow KPIs.

Generated:

- Free Cash Flow
- Cash Flow Quality
- Cash Flow Status
- Capital Allocation Pattern

Capital allocation classifications included:

- Reinvestment
- Expansion
- Mature
- Distressed
- Other cash flow patterns

Generated:

- cashflow_kpis.csv
- capital_allocation.csv

---

## Day 12 – Financial Ratio Table

Created and populated the financial_ratios table.

Generated:

- financial_ratios.csv

Inserted calculated data into SQLite database.

Validated:

- Row count
- KPI values
- SQL joins
- Database schema

---

## Day 13 – Validation

Performed multiple validation activities.

Completed:

### ROE Validation

Compared calculated ROE with source values.

Generated:

- roe_roce_validation.csv

### ROCE Validation

Compared calculated ROCE with source values.

### OPM Validation

Cross-validated calculated Operating Profit Margin against source OPM values.

Generated:

- opm_crosscheck_log.csv

### Edge Case Validation

Created:

- ratio_edge_cases.log

Logged:

- Zero sales
- Zero interest expense
- Division-by-zero scenarios
- Financial calculation exceptions

---

## Day 14 – Testing & Review

Completed final testing.

Performed:

- KPI validation
- Manual SQL verification
- Financial ratio verification
- Database verification
- Edge case verification
- Sprint review

Executed demo SQL queries to verify generated KPIs.

---

# Database Work

Worked with the following tables:

- companies
- balancesheet
- profitandloss
- cashflow
- sectors
- financial_ratios

Created joins between:

- companies
- balance sheet
- profit & loss
- sectors

Validated relationships before KPI generation.

---

# Reports Generated

Generated the following reports:

- financial_ratios.csv
- cagr_report.csv
- cashflow_kpis.csv
- capital_allocation.csv
- roe_roce_validation.csv
- opm_crosscheck_log.csv
- ratio_edge_cases.log

---

# Validation Activities

Completed:

- OPM validation
- ROE validation
- ROCE validation
- SQL validation
- Manual validation
- Financial sector validation
- Database validation

---

# Major Challenges

During Sprint 2 several issues were encountered.

## Database Schema Differences

The actual SQLite schema differed from the project documentation.

Solution:

Updated SQL queries according to the actual schema.

---

## Missing Sector Information

Financial sector companies required special handling.

Solution:

Created and loaded the sectors table.

Integrated the sectors table into the ratio engine.

---

## Division by Zero

Certain companies contained:

- Zero Sales
- Zero Interest
- Zero Equity

Solution:

Added validation conditions before every calculation.

---

## Financial Sector Handling

Banks and NBFCs cannot be evaluated using the same leverage thresholds as manufacturing companies.

Solution:

Implemented Financial Sector carve-out.

High Leverage Flag is automatically disabled for Financial sector companies.

---

# Testing Performed

Performed:

- Unit Testing
- Manual Testing
- SQL Testing
- KPI Validation
- Financial Validation
- Edge Case Testing

---

# Key Learnings

Sprint 2 significantly improved understanding of:

- Financial Statement Analysis
- Ratio Analysis
- SQL
- SQLite
- Python
- Pandas
- Financial KPIs
- CAGR
- Cash Flow Analysis
- Data Validation
- Edge Case Handling
- Business Analytics

---

# Skills Developed

Technical Skills

- Python
- Pandas
- SQLite
- SQL
- Financial Analytics
- KPI Development
- Data Validation

Business Skills

- Financial Statement Analysis
- Company Performance Evaluation
- Ratio Interpretation
- Business Decision Support

---

# Sprint Deliverables

Successfully completed:

- Profitability Ratio Engine
- Leverage Ratio Engine
- Efficiency Ratio Engine
- CAGR Engine
- Cash Flow KPI Engine
- Capital Allocation Analysis
- Financial Ratio Table
- Sector Integration
- Validation Reports
- Testing
- Sprint Documentation

---

# Sprint Outcome

Sprint 2 was successfully completed.

A reusable Financial Ratio Engine was developed capable of generating validated financial KPIs across multiple years for all companies in the dataset.

The solution includes profitability analysis, leverage analysis, efficiency analysis, CAGR analytics, cash flow analytics, sector-aware calculations, validation reports, SQL verification, testing, and automated report generation.

The implementation provides a robust analytical foundation for future dashboard development, financial modeling, and advanced analytics in subsequent sprints.