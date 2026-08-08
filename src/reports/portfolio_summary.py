import sqlite3
from pathlib import Path

import pandas as pd

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# ------------------------------------
# Project Paths
# ------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_PATH = PROJECT_ROOT / "db" / "nifty100.db"

RANKING_FILE = PROJECT_ROOT / "output" / "company_rankings.xlsx"

OUTPUT_FOLDER = PROJECT_ROOT / "reports" / "portfolio"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

styles = getSampleStyleSheet()

# ------------------------------------
# Load Database
# ------------------------------------

conn = sqlite3.connect(DB_PATH)

portfolio = pd.read_sql(
    """
    SELECT
        c.id,
        c.company_name,
        s.broad_sector,
        c.roe_percentage,
        c.roce_percentage
    FROM companies c

    LEFT JOIN sectors s
    ON c.id = s.company_id

    ORDER BY c.id
    """,
    conn
)

conn.close()

# ------------------------------------
# Load Ranking Excel
# ------------------------------------

ranking = pd.read_excel(RANKING_FILE)

ranking = ranking[
    ["company_id", "score", "rating"]
]

portfolio = portfolio.merge(
    ranking,
    left_on="id",
    right_on="company_id",
    how="left"
)

print(portfolio.head())

# ------------------------------------
# Create PDF
# ------------------------------------

pdf_file = OUTPUT_FOLDER / "portfolio_summary.pdf"

doc = SimpleDocTemplate(
    str(pdf_file),
    pagesize=(8.27 * inch, 11.69 * inch)
)

elements = []

elements.append(
    Paragraph(
        "NIFTY100 Portfolio Summary",
        styles["Title"]
    )
)

elements.append(Spacer(1, 0.25 * inch))

elements.append(
    Paragraph(
        f"Total Companies : {len(portfolio)}",
        styles["Heading2"]
    )
)

elements.append(Spacer(1, 0.2 * inch))

table_data = [[
    "Ticker",
    "Sector",
    "ROE",
    "ROCE",
    "Score",
    "Rating"
]]

for _, row in portfolio.iterrows():

    table_data.append([
        row["id"],
        row["broad_sector"],
        row["roe_percentage"],
        row["roce_percentage"],
        row["score"],
        row["rating"]
    ])

table = Table(
    table_data,
    colWidths=[
        1.1 * inch,
        2.5 * inch,
        0.8 * inch,
        0.8 * inch,
        0.8 * inch,
        1.2 * inch
    ]
)

table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
    ])
)

elements.append(table)

doc.build(elements)

print("\nPortfolio Summary Generated Successfully")
print(pdf_file)