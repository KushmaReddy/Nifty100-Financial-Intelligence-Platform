import re

def normalize_year(value):
    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    if re.fullmatch(r"\d{4}", value):
        return value

    match = re.search(r"(\d{2,4})", value)

    if match:
        year = match.group(1)

        if len(year) == 2:
            year = "20" + year

        return year

    return None

def normalize_ticker(value):
    if value is None:
        return None

    value = str(value).strip().upper()

    if value == "":
        return None

    ticker_mapping = {
        "AGTL": "ATGL"
    }

    return ticker_mapping.get(value, value)