import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("db/nifty100.db")

conn = sqlite3.connect(DB_PATH)

peer_percentiles = pd.read_sql(
    "SELECT * FROM peer_percentiles",
    conn
)

conn.close()

print("=" * 50)
print("SPRINT 3 VALIDATION")
print("=" * 50)

# -------------------------
# Test 1
# -------------------------

if len(peer_percentiles) > 0:
    print("✅ Test 1 Passed : peer_percentiles table is not empty")
else:
    print("❌ Test 1 Failed")

# -------------------------
# Test 2
# -------------------------

peer_groups = peer_percentiles["peer_group_name"].nunique()

if peer_groups == 11:
    print("✅ Test 2 Passed : 11 Peer Groups Found")
else:
    print(f"❌ Test 2 Failed : Found {peer_groups}")

# -------------------------
# Test 3
# -------------------------

metrics = peer_percentiles["metric"].nunique()

if metrics == 10:
    print("✅ Test 3 Passed : 10 Metrics Present")
else:
    print(f"❌ Test 3 Failed : Found {metrics}")

# -------------------------
# Test 4
# -------------------------

minimum = peer_percentiles["percentile_rank"].min()
maximum = peer_percentiles["percentile_rank"].max()

if minimum >= 0 and maximum <= 100:
    print("✅ Test 4 Passed : Percentile Rank between 0 and 100")
else:
    print("❌ Test 4 Failed")

# -------------------------
# Test 5
# -------------------------

duplicates = peer_percentiles.duplicated(
    subset=[
        "company_id",
        "peer_group_name",
        "metric",
        "year"
    ]
).sum()

if duplicates == 0:
    print("✅ Test 5 Passed : No Duplicate Records")
else:
    print(f"❌ Test 5 Failed : {duplicates} duplicates found")

print("=" * 50) 