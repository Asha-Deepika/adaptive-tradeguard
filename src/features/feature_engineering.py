import pandas as pd
import numpy as np


def create_features(df):

    # 1. Return
    df["Return"] = df["Close"].pct_change()

    # 2. Log Return
    df["Log Return"] = np.log(
        df["Close"] / df["Close"].shift(1)
    )

    # 3. 20-day Volatility
    df["20-day Volatility"] = (
        df["Return"].rolling(window=20).std()
    )

    # 4. RSI-14
    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    df["RSI-14"] = 100 - (100 / (1 + rs))

    # 5. MACD
    ema_12 = df["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema_26 = df["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    df["MACD"] = ema_12 - ema_26

    # 6. MACD Signal
    df["MACD Signal"] = df["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    # 7. MACD Histogram
    df["MACD Histogram"] = (
        df["MACD"] - df["MACD Signal"]
    )

    # 8. ATR-14
    previous_close = df["Close"].shift(1)

    true_range_1 = df["High"] - df["Low"]

    true_range_2 = (
        df["High"] - previous_close
    ).abs()

    true_range_3 = (
        df["Low"] - previous_close
    ).abs()

    true_range = pd.concat(
        [
            true_range_1,
            true_range_2,
            true_range_3
        ],
        axis=1
    ).max(axis=1)

    df["ATR-14"] = (
        true_range.rolling(window=14).mean()
    )

    # 9. Volume Change
    df["Volume Change"] = df["Volume"].pct_change()

    # 10. Volume MA-20
    df["Volume MA-20"] = (
        df["Volume"].rolling(window=20).mean()
    )

    return df


if __name__ == "__main__":

    input_file = "data/processed/cleaned_data.csv"
    output_file = "data/processed/feature_matrix.csv"

    # Load cleaned data
    df = pd.read_csv(input_file)

    # Create features
    df = create_features(df)

    # Save feature matrix
    df.to_csv(output_file, index=False)

    print("Feature engineering completed.")

    print("\nFirst 10 rows:")
    print(df.head(10))

    print("\nFeatures created:")
    print(df.columns.tolist())

    print("\nFeature matrix saved to:")
    print(output_file)