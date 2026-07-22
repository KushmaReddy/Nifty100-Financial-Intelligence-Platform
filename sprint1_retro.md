# Sprint 1 Retrospective

## Sprint Goal
Build a robust ETL pipeline for the Nifty100 Financial Intelligence Platform by loading source datasets, performing data quality validation, and storing the cleaned data in a SQLite database.

---

## Work Completed

- Set up the project environment and folder structure.
- Loaded all source Excel datasets successfully.
- Normalized ticker symbols and financial years.
- Removed duplicate records from Profit & Loss, Balance Sheet, and Cash Flow datasets.
- Implemented data quality validation rules.
- Generated `validation_failures.csv`.
- Created `load_audit.csv`.
- Created SQLite database (`nifty100.db`).
- Loaded all processed datasets into SQLite.
- Wrote and verified 10 exploratory SQL queries.
- Enabled SQLite foreign key enforcement.
- Verified database integrity using `PRAGMA foreign_key_check`.

---

## Challenges Faced

- Duplicate records in financial datasets.
- Inconsistent company IDs across datasets.
- Invalid OPM values.
- Source data issues resulting in DQ-03, DQ-06, DQ-09, and DQ-16 warnings.
- Difficulty using the VS Code SQLite extension to execute SQL queries.

---

## Solutions Implemented

- Removed duplicate records before loading data.
- Normalized ticker symbols and year values.
- Investigated all validation warnings individually.
- Confirmed that remaining validation issues were due to source data rather than ETL logic.
- Used Python's `sqlite3` library to verify SQL queries and database integrity.

---

## Key Learnings

- Building an ETL pipeline using Python and SQLite.
- Data cleaning and normalization techniques.
- Writing and applying data quality validation rules.
- Loading data into relational databases.
- Writing exploratory SQL queries.
- Verifying database integrity using foreign key checks.

---

## Sprint Outcome

Sprint 1 was successfully completed.

### Deliverables

- ✅ nifty100.db
- ✅ load_audit.csv
- ✅ validation_failures.csv
- ✅ exploratory_queries.sql

The ETL pipeline successfully loads, validates, and stores the project datasets in SQLite. The database passed the foreign key integrity check with no violations and is ready for Sprint 2.