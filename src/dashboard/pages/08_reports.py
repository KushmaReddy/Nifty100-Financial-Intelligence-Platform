import streamlit as st
from pathlib import Path

st.title("📄 Reports Center")

# -----------------------------
# Output Folder
# -----------------------------
OUTPUT_PATH = Path("outputs")

files = list(OUTPUT_PATH.glob("*"))

# -----------------------------
# No Reports
# -----------------------------
if not files:

    st.error("❌ No reports found.")

    st.stop()

# -----------------------------
# KPIs
# -----------------------------
st.metric(
    "Available Reports",
    len(files)
)

# -----------------------------
# Search
# -----------------------------
search = st.text_input(
    "🔍 Search Report",
    ""
)

# -----------------------------
# File Type Filter
# -----------------------------
file_types = ["All", "CSV", "Excel"]

selected = st.selectbox(
    "Filter by Type",
    file_types
)

filtered = files

if search:

    filtered = [
        f for f in filtered
        if search.lower() in f.name.lower()
    ]

if selected == "CSV":

    filtered = [
        f for f in filtered
        if f.suffix == ".csv"
    ]

elif selected == "Excel":

    filtered = [
        f for f in filtered
        if f.suffix in [".xlsx", ".xls"]
    ]

# -----------------------------
# Report List
# -----------------------------
st.subheader("Available Reports")

if len(filtered) == 0:

    st.warning("⚠️ Report unavailable.")

else:

    for file in filtered:

        c1, c2 = st.columns([4,1])

        c1.write(f"📄 {file.name}")

        with open(file, "rb") as f:

            c2.download_button(
                "Download",
                data=f,
                file_name=file.name,
                mime="application/octet-stream",
                key=file.name
            )