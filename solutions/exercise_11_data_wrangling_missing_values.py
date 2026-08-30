\"\"\"
Exercise 11: Data Wrangling - Handling Missing Values
Difficulty: Easy
Topic: Data Wrangling

Problem Statement:
Write a Python script using pandas to:
1. Create a DataFrame with missing values (NaN) in multiple columns
2. Identify missing values using isnull() and notnull()
3. Count missing values per column
4. Remove rows with missing values (dropna)
5. Fill missing values with a specific value (e.g., 0)
6. Fill missing values with column mean
7. Fill missing values with forward fill and backward fill

Expected Output:
Original DataFrame with NaN:
      A     B     C
0   1.0   1.0   1.0
1   2.0   NaN   2.0
2   3.0   3.0   NaN
3   NaN   4.0   4.0
4   5.0   5.0   5.0

Missing values count:
A    1
B    1
C    1
dtype: int64

DataFrame after dropping rows with any NaN:
      A     B     C
0   1.0   1.0   1.0
4   5.0   5.0   5.0

DataFrame after filling NaN with 0:
      A     B     C
0   1.0   1.0   1.0
1   2.0   0.0   2.0
2   3.0   3.0   0.0
3   0.0   4.0   4.0
4   5.0   5.0   5.0

DataFrame after filling NaN with column mean:
      A     B     C
0   1.0   1.0   1.0
1   2.0   3.25  2.0
2   3.0   3.0   3.6666666666666665
3   2.75  4.0   4.0
4   5.0   5.0   5.0

DataFrame after forward fill:
      A     B     C
0   1.0   1.0   1.0
1   2.0   1.0   2.0
2   3.0   3.0   2.0
3   3.0   4.0   4.0
4   5.0   5.0   5.0

DataFrame after backward fill:
      A     B     C
0   1.0   1.0   1.0
1   2.0   4.0   2.0
2   3.0   3.0   4.0
3   5.0   4.0   4.0
4   5.0   5.0   5.0
\"\"\"

import pandas as pd
import numpy as np

def handle_missing_values():
    """
    Demonstrate various techniques for handling missing values in pandas.
    Returns:
        dict: Results for testing
    """
    # Create a DataFrame with missing values
    df = pd.DataFrame({
        'A': [1.0, 2.0, 3.0, np.nan, 5.0],
        'B': [1.0, np.nan, 3.0, 4.0, 5.0],
        'C': [1.0, 2.0, np.nan, 4.0, 5.0]
    })
    
    # Identify missing values
    missing_count = df.isnull().sum()
    
    # Drop rows with any missing values
    df_dropped = df.dropna()
    
    # Fill missing values with 0
    df_filled_0 = df.fillna(0)
    
    # Fill missing values with column mean
    df_filled_mean = df.fillna(df.mean())
    
    # Forward fill
    df_ffill = df.fillna(method='ffill')
    
    # Backward fill
    df_bfill = df.fillna(method='bfill')
    
    # Print results
    print("Original DataFrame with NaN:")
    print(df)
    print("\nMissing values count:")
    print(missing_count)
    print("\nDataFrame after dropping rows with any NaN:")
    print(df_dropped)
    print("\nDataFrame after filling NaN with 0:")
    print(df_filled_0)
    print("\nDataFrame after filling NaN with column mean:")
    print(df_filled_mean)
    print("\nDataFrame after forward fill:")
    print(df_ffill)
    print("\nDataFrame after backward fill:")
    print(df_bfill)
    
    # Return for testing
    return {
        "df": df,
        "missing_count": missing_count,
        "df_dropped": df_dropped,
        "df_filled_0": df_filled_0,
        "df_filled_mean": df_filled_mean,
        "df_ffill": df_ffill,
        "df_bfill": df_bfill
    }

# Test cases
if __name__ == "__main__":
    result = handle_missing_values()
    
    # Test 1: Original DataFrame shape
    assert result["df"].shape == (5, 3), f"DataFrame shape failed: {result['df'].shape}"
    
    # Test 2: Missing values count
    expected_missing = pd.Series([1, 1, 1], index=['A', 'B', 'C'])
    assert result["missing_count"].equals(expected_missing), f"Missing count failed: {result['missing_count']}"
    
    # Test 3: Dropped DataFrame shape (should have 2 rows)
    assert result["df_dropped"].shape == (2, 3), f"Dropped DataFrame shape failed: {result['df_dropped'].shape}"
    
    # Test 4: Filled with 0 - check specific value
    assert result["df_filled_0"].loc[1, 'B'] == 0.0, f"Fill with 0 failed: {result['df_filled_0'].loc[1, 'B']}"
    
    # Test 5: Filled with mean - check that the mean of column B is (1+3+4+5)/4 = 3.25
    # Note: we filled NaN in B with the mean of the non-NaN values in B: (1+3+4+5)/4 = 3.25
    assert abs(result["df_filled_mean"].loc[1, 'B'] - 3.25) < 0.001, f"Fill with mean failed: {result['df_filled_mean'].loc[1, 'B']}"
    
    # Test 6: Forward fill - check that the NaN in row 1, column B is filled with the previous value (1.0)
    assert result["df_ffill"].loc[1, 'B'] == 1.0, f"Forward fill failed: {result['df_ffill'].loc[1, 'B']}"
    
    # Test 7: Backward fill - check that the NaN in row 3, column A is filled with the next value (5.0)
    assert result["df_bfill"].loc[3, 'A'] == 5.0, f"Backward fill failed: {result['df_bfill'].loc[3, 'A']}"
    
    print("\nAll tests passed!")