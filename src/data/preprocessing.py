import pandas as pd


def load_data(file_path):

    # Read Yahoo Finance CSV
    df = pd.read_csv(file_path)

    # Remove the Ticker row
    df = df[df["Price"] != "Ticker"]

    # Rename Price column to Date
    df = df.rename(columns={"Price": "Date"})

    # Convert Date to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Convert numerical columns to numbers
    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Remove invalid rows
    df = df.dropna(
        subset=["Date", "Open", "High", "Low", "Close"]
    )

    # Sort by date
    df = df.sort_values("Date")

    # Remove duplicate dates
    df = df.drop_duplicates(subset="Date")

    # Reset index
    df = df.reset_index(drop=True)

    return df


def clean_data(df):

    # Remove rows with missing important price values
    df = df.dropna(
        subset=["Open", "High", "Low", "Close"]
    )

    return df


if __name__ == "__main__":

    input_file = "data/raw/yahoo_data.csv"
    output_file = "data/processed/cleaned_data.csv"

    # Load data
    df = load_data(input_file)

    print("Data after loading:")
    print(df.head())

    print("\nData shape:", df.shape)

    # Clean data
    df = clean_data(df)

    print("\nData after cleaning:")
    print(df.head())

    print("\nFinal shape:", df.shape)

    # Save cleaned data
    df.to_csv(output_file, index=False)

    print("\nCleaned data saved to:")
    print(output_file)