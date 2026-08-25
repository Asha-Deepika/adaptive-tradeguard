import numpy as np
import pandas as pd


INPUT_FILE = "data/processed/feature_matrix.csv"
OUTPUT_FILE = "data/processed/prepared_features.csv"


def prepare_features():

    print("=" * 60)
    print("FEATURE PREPARATION")
    print("=" * 60)

    # ----------------------------
    # Load feature matrix
    # ----------------------------

    df = pd.read_csv(
        INPUT_FILE,
        parse_dates=["Date"],
    )

    print(
        f"Before preparation: {df.shape}"
    )

    # ----------------------------
    # Handle infinite values
    # ----------------------------

    df = df.replace(
        [np.inf, -np.inf],
        np.nan,
    )

    # ----------------------------
    # Remove missing values
    # ----------------------------

    df = df.dropna().reset_index(
        drop=True
    )

    # ----------------------------
    # Final checks
    # ----------------------------

    missing = (
        df.isna()
        .sum()
        .sum()
    )

    numeric = df.select_dtypes(
        include=np.number
    )

    infinite = np.isinf(
        numeric.to_numpy()
    ).sum()

    print(
        f"After preparation:  {df.shape}"
    )

    print(
        f"Missing values remaining: {missing}"
    )

    print(
        f"Infinite values remaining: {infinite}"
    )

    # ----------------------------
    # Save prepared features
    # ----------------------------

    df.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print(
        "\nFeature preparation completed successfully."
    )

    print(
        f"Saved to: {OUTPUT_FILE}"
    )


if __name__ == "__main__":

    prepare_features()