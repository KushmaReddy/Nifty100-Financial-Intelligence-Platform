import pandas as pd


def create_load_audit(datasets):
    audit_data = []

    for name, df in datasets.items():
        audit_data.append(
            {
                "dataset": name,
                "rows": len(df),
                "columns": len(df.columns),
                "status": "SUCCESS"
            }
        )

    audit_df = pd.DataFrame(audit_data)

    audit_df.to_csv(
        "load_audit.csv",
        index=False
    )

    print("load_audit.csv generated successfully.")