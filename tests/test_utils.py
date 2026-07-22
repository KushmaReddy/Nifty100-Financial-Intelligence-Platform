from src.utils import normalize_year, normalize_ticker

def test_normalize_year():
    assert normalize_year("Mar-24") == "2024"
    assert normalize_year("FY22") == "2022"
    assert normalize_year("2021") == "2021"
    assert normalize_year("") is None
    assert normalize_year(None) is None

def test_normalize_ticker():
    assert normalize_ticker("tcs") == "TCS"
    assert normalize_ticker(" infy ") == "INFY"
    assert normalize_ticker("Reliance") == "RELIANCE"
    assert normalize_ticker("") is None
    assert normalize_ticker(None) is None