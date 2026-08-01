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
