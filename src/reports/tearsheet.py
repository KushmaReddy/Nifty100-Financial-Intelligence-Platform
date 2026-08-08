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

OUTPUT_FOLDER = PROJECT_ROOT / "reports" / "tearsheets"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

styles = getSampleStyleSheet()


# ------------------------------------
# Generate PDF
# ------------------------------------

def generate_tearsheet(company_id):

    conn = sqlite3.connect(DB_PATH)

    print(f"\nGenerating PDF for {company_id}...")
    print("Loading Company Data...")

    company = pd.read_sql(
        """
        SELECT *
        FROM companies
        WHERE id = ?
        """,
        conn,
        params=[company_id]
    )

    if company.empty:
        print(f"{company_id} not found.")
        conn.close()
        return

    ratios = pd.read_sql(
        """
        SELECT *
        FROM financial_ratios
        WHERE company_id = ?
        ORDER BY year
        """,
        conn,
        params=[company_id]
    )

    pros_cons = pd.read_sql(
        """
        SELECT *
        FROM prosandcons
        WHERE company_id = ?
        """,
        conn,
        params=[company_id]
    )

    analysis = pd.read_sql(
        """
        SELECT *
        FROM analysis
        WHERE company_id = ?
        """,
        conn,
        params=[company_id]
    )

    cashflow = pd.read_sql(
        """
        SELECT *
        FROM cashflow
        WHERE company_id = ?
        ORDER BY year
        """,
        conn,
        params=[company_id]
    )

    print("Company Rows :", len(company))
    print("Ratios Rows  :", len(ratios))
    print("Pros/Cons    :", len(pros_cons))
    print("Analysis     :", len(analysis))
    print("Cashflow     :", len(cashflow))

    conn.close()

    # ------------------------------------
    # Create PDF
    # ------------------------------------

    pdf_file = OUTPUT_FOLDER / f"{company_id}_tearsheet.pdf"

    doc = SimpleDocTemplate(
        str(pdf_file),
        pagesize=(8.27 * inch, 11.69 * inch)
    )

    elements = []

    # ------------------------------------
    # Title
    # ------------------------------------

    elements.append(
        Paragraph(
            company.iloc[0]["company_name"],
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 0.25 * inch))

    # ------------------------------------
    # Basic Information
    # ------------------------------------

    info = [
        ["Company ID", company.iloc[0]["id"]],
        ["ROE %", company.iloc[0]["roe_percentage"]],
        ["ROCE %", company.iloc[0]["roce_percentage"]],
        ["Face Value", company.iloc[0]["face_value"]],
        ["Book Value", company.iloc[0]["book_value"]],
    ]

    table = Table(
        info,
        colWidths=[2.2 * inch, 3.8 * inch]
    )

    table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ])
    )

    elements.append(table)

    elements.append(Spacer(1, 0.3 * inch))

    # ------------------------------------
    # About Company
    # ------------------------------------

    elements.append(
        Paragraph(
            "About Company",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            str(company.iloc[0]["about_company"]),
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 0.3 * inch))

    # ------------------------------------
    # Pros
    # ------------------------------------

    elements.append(
        Paragraph(
            "Pros",
            styles["Heading2"]
        )
    )

    for p in pros_cons["pros"].dropna():
        elements.append(
            Paragraph(
                f"• {p}",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 0.2 * inch))

    # ------------------------------------
    # Cons
    # ------------------------------------

    elements.append(
        Paragraph(
            "Cons",
            styles["Heading2"]
        )
    )

    for c in pros_cons["cons"].dropna():
        elements.append(
            Paragraph(
                f"• {c}",
                styles["BodyText"]
            )
        )

    # ------------------------------------
    # Build PDF
    # ------------------------------------

    doc.build(elements)

    print("\nPDF Generated Successfully")
    print(pdf_file)


if __name__ == "__main__":
    generate_tearsheet("TCS")