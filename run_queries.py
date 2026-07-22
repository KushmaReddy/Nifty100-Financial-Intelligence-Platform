import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

queries = [
    (
        "Query 1",
        """
        SELECT COUNT(*) AS total_companies
        FROM companies;
        """
    ),
    (
        "Query 2",
        """
        SELECT COUNT(*) AS total_records
        FROM profitandloss;
        """
    ),
    (
        "Query 3",
        """
        SELECT COUNT(*) AS total_records
        FROM balancesheet;
        """
    ),
    (
        "Query 4",
        """
        SELECT COUNT(*) AS total_records
        FROM cashflow;
        """
    ),
    (
        "Query 5",
        """
        SELECT COUNT(*) AS total_records
        FROM analysis;
        """
    ),
    (
        "Query 6",
        """
        SELECT COUNT(*) AS total_records
        FROM documents;
        """
    ),
    (
        "Query 7",
        """
        SELECT COUNT(*) AS total_records
        FROM prosandcons;
        """
    ),
    (
        "Query 8",
        """
        SELECT
            company_id,
            COUNT(year) AS total_years
        FROM profitandloss
        GROUP BY company_id
        ORDER BY total_years DESC;
        """
    ),
    (
        "Query 9",
        """
        SELECT
            company_id,
            COUNT(year) AS total_years
        FROM profitandloss
        GROUP BY company_id
        HAVING COUNT(year) < 5;
        """
    ),
    (
        "Query 10",
        """
        SELECT
            MIN(year) AS earliest_year,
            MAX(year) AS latest_year
        FROM profitandloss;
        """
    )
]
for title, query in queries:
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

conn.close()
