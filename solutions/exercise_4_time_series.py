\"\"\"
Exercise 4: Time Series Analysis with Pandas (Medium)
Problem Statement:
You are given a DataFrame containing daily stock prices for a company over a year.
The DataFrame has a 'Date' column (as strings) and a 'Close' column (closing price).
Your tasks:
1. Convert the 'Date' column to datetime and set it as the index.
2. Resample the data to monthly frequency, calculating the mean closing price for each month.
3. Calculate the month-over-month percentage change in the average closing price.
4. Identify the month with the highest percentage increase and the month with the highest percentage decrease.

Expected Output:
- A DataFrame with monthly average closing prices.
- A Series with month-over-month percentage changes.
- Printed statements about the best and worst months.

Time Complexity: O(n) for reading and converting, O(n) for resampling (grouping by month).
Space Complexity: O(n) for storing the DataFrame.
\"\"\"
import pandas as pd
import numpy as np

def analyze_stock_data(data: pd.DataFrame) -> tuple:
    """
    Analyze stock price data.

    Parameters:
    data (pd.DataFrame): DataFrame with columns 'Date' (string) and 'Close' (float).

    Returns:
    tuple: (monthly_avg, pct_change, best_month, worst_month)
        monthly_avg: DataFrame with monthly average closing prices.
        pct_change: Series with month-over-month percentage changes.
        best_month: (month_string, pct_increase) for the highest increase.
        worst_month: (month_string, pct_decrease) for the lowest increase (most negative).
    """
    # Make a copy to avoid modifying the original
    df = data.copy()

    # Convert Date to datetime and set as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Resample to monthly frequency, calculating the mean closing price
    monthly_avg = df['Close'].resample('M').mean()

    # Calculate month-over-month percentage change
    pct_change = monthly_avg.pct_change() * 100  # as percentage

    # Find the month with the highest percentage increase and lowest (most negative)
    # We skip the first month because it has no previous month to compare
    pct_change_clean = pct_change.dropna()
    if pct_change_clean.empty:
        return monthly_avg, pct_change, None, None

    best_month_idx = pct_change_clean.idxmax()
    worst_month_idx = pct_change_clean.idxmin()

    best_month = (best_month_idx.strftime('%B %Y'), pct_change_clean.loc[best_month_idx])
    worst_month = (worst_month_idx.strftime('%B %Y'), pct_change_clean.loc[worst_month_idx])

    return monthly_avg, pct_change, best_month, worst_month

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Test case 1: Synthetic data for a year
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    # Create a simple trend: increasing over the year with some noise
    np.random.seed(42)
    close_prices = 100 + np.cumsum(np.random.normal(0.1, 0.5, len(dates)))  # random walk
    data = pd.DataFrame({'Date': dates.strftime('%Y-%m-%d'), 'Close': close_prices})

    monthly_avg, pct_change, best_month, worst_month = analyze_stock_data(data)

    print("Monthly Average Closing Prices:")
    print(monthly_avg.head())
    print("\nMonth-over-Month Percentage Change:")
    print(pct_change.head())
    print(f"\nBest Month: {best_month[0]} with {best_month[1]:.2f}% increase")
    print(f"Worst Month: {worst_month[0]} with {worst_month[1]:.2f}% change")

    # Assertions
    assert len(monthly_avg) == 12, "Should have 12 months"
    assert len(pct_change) == 12, "Should have 12 months of pct change (first is NaN)"
    assert not pct_change.isna().all(), "All pct change should not be NaN"
    assert best_month is not None and worst_month is not None, "Best and worst months should be identified"

    # Test case 2: Edge case with constant prices (no change)
    flat_data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=60, freq='D').strftime('%Y-%m-%d'),
        'Close': [100] * 60
    })
    monthly_avg2, pct_change2, best_month2, worst_month2 = analyze_stock_data(flat_data)
    print("\nFlat data test:")
    print("Monthly averages:", monthly_avg2.values)
    print("Pct change:", pct_change2.values)
    # All percentage changes should be 0 (or NaN for the first)
    assert np.allclose(pct_change2.dropna(), 0), "Percentage change should be zero for constant prices"

    print("\nAll tests passed!")