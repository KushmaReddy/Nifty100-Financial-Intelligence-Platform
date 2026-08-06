# Sprint 4 Retrospective

## Sprint Goal

The objective of Sprint 4 was to develop a complete Streamlit-based Financial Intelligence Dashboard with interactive visualizations, company analysis, stock screening, peer comparison, valuation analysis, downloadable reports, and end-to-end testing.

---

## Features Completed

- Built an 8-page Streamlit dashboard.
- Implemented company search and profile analysis.
- Developed a stock screener with multiple financial filters.
- Created peer comparison functionality.
- Added trend analysis for company financial metrics.
- Built sector analysis and capital allocation pages.
- Developed the reports page for downloading generated reports.
- Implemented the valuation module with FCF Yield and sector-based valuation analysis.
- Generated valuation_summary.xlsx and valuation_flags.csv.

---

## Challenges Faced

- Understanding the Streamlit multi-page application structure.
- Integrating SQLite queries with dashboard components.
- Handling missing financial values without causing dashboard errors.
- Ensuring all pages loaded correctly for every company.
- Maintaining consistent performance across multiple dashboard pages.

---

## Solutions Implemented

- Used shared database utility functions for efficient data retrieval.
- Added validation checks for missing values.
- Optimized SQL queries for better performance.
- Standardized dashboard layouts across all pages.
- Performed integration testing across different company sectors.

---

## Testing Performed

- Verified all dashboard pages loaded successfully.
- Tested company search functionality.
- Validated report generation and downloads.
- Checked valuation outputs.
- Tested multiple company tickers across different sectors.
- Fixed minor UI and data handling issues.

---

## Deliverables

- Streamlit Dashboard
- 8 Dashboard Pages
- valuation_summary.xlsx
- valuation_flags.csv
- peer_comparison.xlsx
- screener_results.csv
- Updated README documentation

---

## Lessons Learned

This sprint provided practical experience in building an end-to-end financial analytics application using Python, SQLite, Pandas, Plotly, and Streamlit. It improved understanding of dashboard development, data visualization, SQL integration, financial analysis, and project documentation.
