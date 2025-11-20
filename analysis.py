"""
Data analysis mini project.

Loads a small example dataset and performs basic exploratory
data analysis using pandas and matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str = "data.csv") -> pd.DataFrame:
    """Load the CSV file into a pandas DataFrame."""
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def basic_summary(df: pd.DataFrame) -> None:
    """Print some simple summary statistics."""
    print("Head of data:")
    print(df.head(), "\n")

    print("Summary statistics:")
    print(df[["visitors", "sign_ups"]].describe(), "\n")

    df["conversion_rate"] = df["sign_ups"] / df["visitors"]
    print("Average conversion rate:", df["conversion_rate"].mean().round(3))


def group_by_channel(df: pd.DataFrame) -> pd.DataFrame:
    """Return aggregated metrics by marketing channel."""
    df["conversion_rate"] = df["sign_ups"] / df["visitors"]
    grouped = (
        df.groupby("channel")
        .agg(
            total_visitors=("visitors", "sum"),
            total_sign_ups=("sign_ups", "sum"),
            mean_conversion_rate=("conversion_rate", "mean"),
        )
        .reset_index()
    )
    return grouped


def plot_visitors(df: pd.DataFrame) -> None:
    """Plot visitors over time."""
    plt.figure()
    plt.plot(df["date"], df["visitors"], marker="o")
    plt.title("Daily Website Visitors")
    plt.xlabel("Date")
    plt.ylabel("Visitors")
    plt.tight_layout()
    plt.savefig("visitors_over_time.png")
    # plt.show()  # Uncomment if running locally with a GUI


def main():
    df = load_data()
    basic_summary(df)

    channel_stats = group_by_channel(df)
    print("\nAggregated metrics by channel:")
    print(channel_stats)

    plot_visitors(df)
    print("\nA line chart has been saved as 'visitors_over_time.png'.")


if __name__ == "__main__":
    main()
