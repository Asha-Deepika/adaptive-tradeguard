import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    file_path = "data/processed/feature_matrix.csv"

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def plot_closing_price(df):
    plt.figure(figsize=(12, 6))

    plt.plot(df["Date"], df["Close"])

    plt.title("NIFTY 50 Closing Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")

    plt.grid(True)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":

    print("Loading feature matrix...")

    df = load_data()

    print("Data loaded successfully.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nCreating Closing Price visualization...")

    plot_closing_price(df)

    print("Data visualization completed.")