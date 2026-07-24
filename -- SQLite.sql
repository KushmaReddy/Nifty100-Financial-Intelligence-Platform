SELECT
    company_id,
    year,
    equity_capital,
    reserves,
    borrowings,
    total_assets
FROM balancesheet
WHERE company_id = 'BEL'
AND year = 2024;
SELECT
    company_id,
    year,
    net_profit_margin,
    operating_profit_margin,
    roe,
    roce,
    roa,
    debt_to_equity,
    interest_coverage,
    asset_turnover,
    free_cash_flow,
    cashflow_quality,
    cashflow_status
FROM financial_ratios
LIMIT 5;
SELECT
    company_id,
    broad_sector,
    sub_sector
FROM sectors
WHERE broad_sector = 'Financials';
SELECT
    fr.company_id,
    s.broad_sector,
    fr.debt_to_equity,
    fr.high_leverage_flag
FROM financial_ratios fr
JOIN sectors s
ON fr.company_id = s.company_id
WHERE s.broad_sector = 'Financials'
LIMIT 20;
PRAGMA table_info(financial_ratios);