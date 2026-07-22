import pandas as pd


class ValidationLogger:

    def __init__(self):
        self.failures = []

    def log(
        self,
        rule_id,
        company_id,
        year,
        field,
        issue,
        severity
    ):
        self.failures.append(
            {
                "rule_id": rule_id,
                "company_id": company_id,
                "year": year,
                "field": field,
                "issue": issue,
                "severity": severity
            }
        )

    def to_dataframe(self):
        return pd.DataFrame(self.failures)

    def save(self, path="validation_failures.csv"):
        self.to_dataframe().to_csv(path, index=False)


def validate_company_pk(companies_df, logger):
    duplicate_rows = companies_df[
        companies_df.duplicated(subset=["id"], keep=False)
    ]

    for _, row in duplicate_rows.iterrows():
        logger.log(
            rule_id="DQ-01",
            company_id=row["id"],
            year=None,
            field="id",
            issue="Duplicate company id",
            severity="CRITICAL"
        )
    return duplicate_rows.empty

def validate_annual_pk(df, table_name, logger):
    duplicate_rows = df[
        df.duplicated(subset=["company_id", "year"], keep=False)
    ]

    for _, row in duplicate_rows.iterrows():
        logger.log(
            rule_id="DQ-02",
            company_id=row["company_id"],
            year=row["year"],
            field="company_id, year",
            issue=f"Duplicate record in {table_name}",
            severity="CRITICAL"
        )

    return duplicate_rows.empty
def validate_foreign_key(df, companies_df, logger):
    valid_ids = set(companies_df["id"])

    invalid_rows = df[
        ~df["company_id"].isin(valid_ids)
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-03",
            company_id=row["company_id"],
            year=row["year"],
            field="company_id",
            issue="Company ID not found in companies table",
            severity="CRITICAL"
        )

    return invalid_rows.empty
def validate_balance_sheet(df, logger):
    invalid_rows = df[
        (
            (df["total_assets"] - df["total_liabilities"]).abs()
            / df["total_assets"]
        ) > 0.01
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-04",
            company_id=row["company_id"],
            year=row["year"],
            field="total_assets,total_liabilities",
            issue="Balance Sheet does not balance",
            severity="WARNING"
        )

    return invalid_rows.empty
def validate_opm(df, logger):
    calculated_opm = (df["operating_profit"] / df["sales"]) * 100

    invalid_rows = df[
        (df["opm_percentage"] - calculated_opm).abs() > 1
    ]
    
    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-05",
            company_id=row["company_id"],
            year=row["year"],
            field="opm_percentage",
            issue="OPM does not match calculated value",
            severity="WARNING"
        )

    return invalid_rows.empty
def validate_positive_sales(df, logger):
    invalid_rows = df[df["sales"] <= 0]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-06",
            company_id=row["company_id"],
            year=row["year"],
            field="sales",
            issue="Sales must be greater than zero",
            severity="WARNING"
        )

    return invalid_rows.empty
   
def validate_year_format(df, logger):
    invalid_rows = df[
        ~df["year"].astype(str).str.match(r"^\d{4}$")
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-07",
            company_id=row["company_id"],
            year=row["year"],
            field="year",
            issue="Invalid year format",
            severity="CRITICAL"
        )

    return invalid_rows.empty

def validate_ticker_format(df, logger):

    column = "company_id"

    if "id" in df.columns:
        column = "id"

    invalid_rows = df[
        (
            df[column] != df[column].astype(str).str.strip().str.upper()
        )
        |
        (
            df[column].astype(str).str.len() < 2
        )
        |
        (
            df[column].astype(str).str.len() > 12
        )
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-08",
            company_id=row[column],
            year=row["year"] if "year" in row.index else None,
            field=column,
            issue="Invalid ticker format",
            severity="CRITICAL"
        )

    return invalid_rows.empty
def validate_net_cash_flow(df, logger):
    calculated = (
        df["operating_activity"]
        + df["investing_activity"]
        + df["financing_activity"]
    )

    invalid_rows = df[
        (df["net_cash_flow"] - calculated).abs() > 10
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-09",
            company_id=row["company_id"],
            year=row["year"],
            field="operating_activity,investing_activity,financing_activity",
            issue="Net cash flow mismatch",
            severity="WARNING"
        )

    return invalid_rows.empty

def validate_fixed_assets(df, logger):
    invalid_rows = df[df["fixed_assets"] < 0]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-10",
            company_id=row["company_id"],
            year=row["year"],
            field="fixed_assets",
            issue="Negative fixed assets",
            severity="WARNING"
        )

    return invalid_rows.empty
def validate_tax_rate(df, logger):
    invalid_rows = df[
        (df["tax_percentage"] < 0)
        | (df["tax_percentage"] > 60)
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-11",
            company_id=row["company_id"],
            year=row["year"],
            field="tax_percentage",
            issue="Tax percentage out of range",
            severity="WARNING"
        )

    return invalid_rows.empty
def validate_dividend_payout(df, logger):
    invalid_rows = df[df["dividend_payout"] > 200]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-12",
            company_id=row["company_id"],
            year=row["year"],
            field="dividend_payout",
            issue="Dividend payout exceeds 200%",
            severity="WARNING"
        )

    return invalid_rows.empty
import requests

def validate_urls(df, logger):
    for _, row in df.iterrows():
        try:
            status = requests.head(
                row["annual_report"],
                allow_redirects=True,
                timeout=5
            ).status_code

            if status != 200:
                logger.log(
                    rule_id="DQ-13",
                    company_id=row["company_id"],
                    year=row.get("year"),
                    field="annual_report",
                    issue=f"URL returned {status}",
                    severity="WARNING"
                )

        except Exception:
            logger.log(
                rule_id="DQ-13",
                company_id=row["company_id"],
                year=row.get("year"),
                field="annual_report",
                issue="URL could not be reached",
                severity="WARNING"
            )

    return True
def validate_eps_sign(df, logger):
    invalid_rows = df[
        (df["net_profit"] > 0) &
        (df["eps"] <= 0)
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-14",
            company_id=row["company_id"],
            year=row["year"],
            field="eps",
            issue="EPS sign inconsistent with Net Profit",
            severity="WARNING"
        )

    return invalid_rows.empty
def validate_balance_equality(df, logger):
    invalid_rows = df[
        df["total_assets"] != df["total_liabilities"]
    ]

    for _, row in invalid_rows.iterrows():
        logger.log(
            rule_id="DQ-15",
            company_id=row["company_id"],
            year=row["year"],
            field="total_assets,total_liabilities",
            issue="Assets not equal to liabilities",
            severity="INFO"
        )

    return invalid_rows.empty
def validate_coverage(df, logger):
    coverage = (
        df.groupby("company_id")["year"]
        .nunique()
    )

    invalid = coverage[coverage < 5]

    for company, years in invalid.items():
        logger.log(
            rule_id="DQ-16",
            company_id=company,
            year=None,
            field="year",
            issue=f"Only {years} years of data available",
            severity="WARNING"
        )

    return invalid.empty
def run_validations(datasets):
    logger = ValidationLogger()

    companies = datasets["companies"]
    profitandloss = datasets["profitandloss"]
    balancesheet = datasets["balancesheet"]
    cashflow = datasets["cashflow"]

    validate_company_pk(
        companies,
        logger
    )

    validate_annual_pk(
        profitandloss,
        "profitandloss",
        logger
    )

    validate_annual_pk(
        balancesheet,
        "balancesheet",
        logger
    )

    validate_annual_pk(
        cashflow,
        "cashflow",
        logger
    )

    validate_foreign_key(
        profitandloss,
        companies,
        logger
    )

    validate_foreign_key(
        balancesheet,
        companies,
        logger
    )

    validate_foreign_key(
        cashflow,
        companies,
        logger
    )

    validate_year_format(
        profitandloss,
        logger
    )

    validate_year_format(
        balancesheet,
        logger
    )

    validate_year_format(
        cashflow,
        logger
    )

    validate_ticker_format(
        companies,
        logger
    )

    validate_positive_sales(
        profitandloss,
        logger
    )

    validate_opm(
        profitandloss,
        logger
    )

    validate_fixed_assets(
        balancesheet,
        logger
    )

    validate_balance_sheet(
        balancesheet,
        logger
    )

    validate_balance_equality(
        balancesheet,
        logger
    )

    validate_net_cash_flow(
        cashflow,
        logger
    )

    validate_coverage(
        profitandloss,
        logger
    )

    from collections import Counter

    counts = Counter()

    for failure in logger.failures:
     counts[failure["rule_id"]] += 1

    print("\nValidation Failures by Rule")

    for rule, count in counts.items():
     print(rule, count)
    return logger