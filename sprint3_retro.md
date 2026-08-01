# Sprint 3 Retrospective

## Sprint Goal

The objective of Sprint 3 was to build a Peer Comparison Analytics module for the Nifty100 project. The sprint included peer percentile calculations, radar chart generation, peer comparison reports, Excel report generation, stock screeners, and validation.

---

## Completed Tasks

- Created the `peer_percentiles` table in SQLite.
- Calculated percentile rankings for 10 financial metrics.
- Generated peer comparison analytics.
- Created radar charts for peer comparison.
- Generated the `peer_comparison.xlsx` workbook with 11 peer group sheets.
- Built and tested six stock screeners:
  - Quality Compounder
  - Growth Accelerator
  - Debt Free Blue Chip
  - Value Pick
  - Dividend Champion
  - Turnaround Watch
- Validated Sprint 3 successfully using the provided test script.

---

## Challenges Faced

- Fixed import errors related to Python modules.
- Corrected merge issues while combining peer group and sector data.
- Handled missing values in financial metrics.
- Installed and configured Matplotlib for radar charts.
- Resolved duplicate records and formatting issues in the Excel report.

---

## Key Learnings

- Performing SQL operations with SQLite.
- Using Pandas for data transformation and pivot tables.
- Calculating percentile rankings within peer groups.
- Creating radar charts using Matplotlib.
- Generating formatted Excel reports with OpenPyXL.
- Building reusable stock screeners using financial ratios.

---

## Sprint Validation

- Peer Percentiles Table: Passed
- Peer Group Count: Passed
- Metrics Validation: Passed
- Percentile Range Validation: Passed
- Duplicate Record Validation: Passed

All Sprint 3 validation tests passed successfully.

---

## Deliverables

- peer_percentiles table
- Radar Charts
- Peer Comparison Excel Report
- Stock Screeners
- Validation Scripts

---

## Next Sprint

Sprint 4 will focus on building dashboards and visualizations using the analytics generated in Sprint 3.