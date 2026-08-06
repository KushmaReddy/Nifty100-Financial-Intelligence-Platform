import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "db/nifty100.db"


@st.cache_data(ttl=600)
def load_table(table_name):
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df