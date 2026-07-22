SELECT COUNT(*) AS total_companies
FROM companies;

SELECT COUNT(*) AS total_records
FROM profitandloss;

SELECT COUNT(*) AS total_records
FROM balancesheet;

SELECT COUNT(*) AS total_records
FROM cashflow;

SELECT COUNT(*) AS total_records
FROM analysis;

SELECT COUNT(*) AS total_records
FROM documents;

SELECT COUNT(*) AS total_records
FROM prosandcons;

SELECT
    company_id,
    COUNT(year) AS total_years
FROM profitandloss
GROUP BY company_id
ORDER BY total_years DESC;

SELECT
    company_id,
    COUNT(year) AS total_years
FROM profitandloss
GROUP BY company_id
HAVING COUNT(year) < 5;

SELECT
    MIN(year) AS earliest_year,
    MAX(year) AS latest_year
FROM profitandloss;


