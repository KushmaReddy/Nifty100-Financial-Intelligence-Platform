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

OUTPUT_FOLDER = PROJECT_ROOT / "reports" / "sector"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

styles = getSampleStyleSheet()

# ------------------------------------
# Database
# ------------------------------------

conn = sqlite3.connect(DB_PATH)

# Latest financial ratios
query = """
SELECT
    s.broad_sector,
    c.id,
    c.company_name,
    fr.year,
    fr.roe,
    fr.roce,
    mc.market_cap_crore,
    mc.pe_ratio,
    mc.pb_ratio
FROM sectors s

JOIN companies c
ON s.company_id = c.id

JOIN financial_ratios fr
ON c.id = fr.company_id

LEFT JOIN market_cap mc
ON fr.company_id = mc.company_id
AND fr.year = mc.year
"""

df = pd.read_sql(query, conn)

conn.close()

# Keep latest year
df = (
    df.sort_values("year")
      .groupby("id")
      .tail(1)
)

print("Rows Loaded :", len(df))

# ------------------------------------
# Generate Report
# ------------------------------------

for sector in sorted(df["broad_sector"].dropna().unique()):

    sector_df = df[df["broad_sector"] == sector]

    pdf_file = OUTPUT_FOLDER / f"{sector.replace(' ','_')}_report.pdf"

    doc = SimpleDocTemplate(
        str(pdf_file),
        pagesize=(8.27 * inch, 11.69 * inch)
    )

    elements = []

    elements.append(
        Paragraph(
            f"{sector} Sector Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 0.25 * inch))

    summary = [
        ["Companies", len(sector_df)],
        ["Median ROE", round(sector_df["roe"].median(), 2)],
        ["Median ROCE", round(sector_df["roce"].median(), 2)],
        ["Median PE", round(sector_df["pe_ratio"].median(), 2)],
        ["Median PB", round(sector_df["pb_ratio"].median(), 2)],
    ]

    summary_table = Table(
        summary,
        colWidths=[3 * inch, 2 * inch]
    )

    summary_table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("BACKGROUND", (0,0), (-1,-1), colors.beige),
        ])
    )

    elements.append(summary_table)

    elements.append(Spacer(1, 0.3 * inch))

    elements.append(
        Paragraph(
            "Companies",
            styles["Heading2"]
        )
    )

    company_table = [["Ticker", "Company", "ROE", "ROCE"]]

    for _, row in sector_df.iterrows():

        company_table.append([
            row["id"],
            row["company_name"],
            round(row["roe"],2),
            round(row["roce"],2)
        ])

    table = Table(
        company_table,
        colWidths=[1.2*inch,3.2*inch,1*inch,1*inch]
    )

    table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
            ("BACKGROUND",(0,1),(-1,-1),colors.beige),
        ])
    )

    elements.append(table)

    doc.build(elements)

    print(f"Generated : {sector}")
    
print("\nAll Sector Reports Generated Successfully")