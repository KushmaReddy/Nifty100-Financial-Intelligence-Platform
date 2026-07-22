from src.utils import normalize_ticker

test_values = [
    "tcs",
    " infy ",
    "Reliance",
    "",
    None
]

for value in test_values:
    print(value, "->", normalize_ticker(value))