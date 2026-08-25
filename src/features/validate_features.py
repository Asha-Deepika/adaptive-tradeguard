import numpy as np
import pandas as pd


FEATURE_PATH = (
    "data/processed/"
    "prepared_features.csv"
)


def validate_features():

    df = pd.read_csv(
        FEATURE_PATH,
        parse_dates=["Date"],
    )

    print("=" * 60)
    print("FEATURE MATRIX VALIDATION")
    print("=" * 60)

    # ----------------------------
    # Shape
    # ----------------------------

    print(
        f"\nRows: {len(df)}"
    )

    print(
        f"Columns: {len(df.columns)}"
    )

    # ----------------------------
    # Required Features
    # ----------------------------

    required_features = [
        "Date",
        "Adj Close",
        "Close",
        "High",
        "Low",
        "Open",
        "Volume",
        "Return",
        "Log Return",
        "20-day Volatility",
        "RSI-14",
        "MACD",
        "MACD Signal",
        "MACD Histogram",
        "ATR-14",
        "Volume Change",
        "Volume MA-20",
    ]

    for feature in required_features:

        assert feature in df.columns

    print(
        "Required features: PASS"
    )

    # ----------------------------
    # Dates
    # ----------------------------

    assert df["Date"].notna().all()

    assert df["Date"].is_unique

    assert df[
        "Date"
    ].is_monotonic_increasing

    print(
        "Date validation: PASS"
    )

    # ----------------------------
    # Missing values
    # ----------------------------

    missing = (
        df.isna()
        .sum()
        .sum()
    )

    assert missing == 0

    print(
        "Missing values: PASS"
    )

    # ----------------------------
    # Infinite values
    # ----------------------------

    numeric = df.select_dtypes(
        include=np.number
    )

    assert np.isfinite(
        numeric.to_numpy()
    ).all()

    print(
        "Infinite values: PASS"
    )

    # ----------------------------
    # RSI
    # ----------------------------

    assert df["RSI-14"].between(
        0,
        100,
    ).all()

    print(
        "RSI range: PASS"
    )

    # ----------------------------
    # ATR
    # ----------------------------

    assert (
        df["ATR-14"] >= 0
    ).all()

    print(
        "ATR non-negative: PASS"
    )

    # ----------------------------
    # Volatility
    # ----------------------------

    assert (
        df["20-day Volatility"] >= 0
    ).all()

    print(
        "Volatility non-negative: PASS"
    )

    # ----------------------------
    # MACD Histogram
    # ----------------------------

    macd_difference = (
        df["MACD"]
        - df["MACD Signal"]
        - df["MACD Histogram"]
    ).abs()

    assert (
        macd_difference.max()
        < 1e-10
    )

    print(
        "MACD consistency: PASS"
    )

    # ----------------------------
    # Volume MA-20
    # ----------------------------

    assert (
        df["Volume MA-20"] >= 0
    ).all()

    print(
        "Volume MA-20: PASS"
    )

    # ----------------------------
    # Volume Change
    # ----------------------------

    assert np.isfinite(
        df["Volume Change"].to_numpy()
    ).all()

    print(
        "Volume Change: PASS"
    )

    # ----------------------------
    # Return
    # ----------------------------

    assert np.isfinite(
        df["Return"].to_numpy()
    ).all()

    print(
        "Return: PASS"
    )

    # ----------------------------
    # Log Return
    # ----------------------------

    assert np.isfinite(
        df["Log Return"].to_numpy()
    ).all()

    print(
        "Log Return: PASS"
    )

    # ----------------------------
    # Final Result
    # ----------------------------

    print(
        "\nALL VALIDATIONS PASSED."
    )


if __name__ == "__main__":

    validate_features()