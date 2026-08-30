\"\"\"
Exercise 5: pandas - Series and DataFrames
Difficulty: Easy
Topic: pandas

Problem Statement:
Write a Python script using pandas to:
1. Create a pandas Series from a list of numbers
2. Create a pandas DataFrame from a dictionary of lists
3. Perform basic operations on Series (sum, mean, max)
4. Perform basic operations on DataFrame (info, describe, column access)
5. Add a new column to the DataFrame based on existing columns

Expected Output:
Series: [10 20 30 40 50]
Series sum: 150
Series mean: 30.0
Series max: 50
DataFrame shape: (4, 3)
DataFrame columns: ['name', 'age', 'salary']
DataFrame info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  -----
 0   name    4 non-null      object
 1   age     4 non-null      int64
 2   salary  4 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 208.0+ bytes
None
DataFrame describe:
              age       salary
count  4.000000  4.000000
mean   27.500000  55000.000000
std     5.333333  12909.944487
min    22.000000  40000.000000
25%    24.250000  45000.000000
50%    26.500000  52500.000000
75%    30.750000  62500.000000
max    33.000000  70000.000000
DataFrame with bonus column:
    name  age  salary  bonus
0  Alice   22   50000   5000
1    Bob   25   60000   6000
2  Charlie   33   70000   7000
3   Diana   26   40000   4000
\"\"\"

import pandas as pd
import numpy as np

def pandas_basics():
    """
    Demonstrate pandas Series and DataFrame basics.
    Returns:
        dict: Results for testing
    """
    # 1. Create a pandas Series
    series = pd.Series([10, 20, 30, 40, 50])
    
    # 2. Create a pandas DataFrame from dictionary
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'age': [22, 25, 33, 26],
        'salary': [50000.0, 60000.0, 70000.0, 40000.0]
    }
    df = pd.DataFrame(data)
    
    # 3. Series operations
    series_sum = series.sum()
    series_mean = series.mean()
    series_max = series.max()
    
    # 4. DataFrame operations
    df_shape = df.shape
    df_columns = df.columns.tolist()
    df_info = df.info()  # This prints to stdout
    df_describe = df.describe()
    
    # 5. Add new column
    df['bonus'] = df['salary'] * 0.1  # 10% bonus
    
    # Print results
    print(f"Series: {series.values}")
    print(f"Series sum: {series_sum}")
    print(f"Series mean: {series_mean}")
    print(f"Series max: {series_max}")
    print(f"DataFrame shape: {df_shape}")
    print(f"DataFrame columns: {df_columns}")
    print("DataFrame info:")
    df.info()
    print("DataFrame describe:")
    print(df_describe)
    print("DataFrame with bonus column:")
    print(df)
    
    # Return for testing
    return {
        "series": series,
        "series_sum": series_sum,
        "series_mean": series_mean,
        "series_max": series_max,
        "df": df,
        "df_shape": df_shape,
        "df_columns": df_columns,
        "df_describe": df_describe
    }

# Test cases
if __name__ == "__main__":
    result = pandas_basics()
    
    # Test 1: Series values
    expected_series = pd.Series([10, 20, 30, 40, 50])
    assert result["series"].equals(expected_series), "Series creation failed"
    
    # Test 2: Series sum
    assert result["series_sum"] == 150, f"Series sum failed: {result['series_sum']}"
    
    # Test 3: Series mean
    assert abs(result["series_mean"] - 30.0) < 0.001, f"Series mean failed: {result['series_mean']}"
    
    # Test 4: Series max
    assert result["series_max"] == 50, f"Series max failed: {result['series_max']}"
    
    # Test 5: DataFrame shape
    assert result["df_shape"] == (4, 3), f"DataFrame shape failed: {result['df_shape']}"
    
    # Test 6: DataFrame columns
    expected_columns = ['name', 'age', 'salary']
    assert result["df_columns"] == expected_columns, f"DataFrame columns failed: {result['df_columns']}"
    
    # Test 7: Bonus column
    expected_bonus = [5000.0, 6000.0, 7000.0, 4000.0]
    assert list(result["df"]["bonus"]) == expected_bonus, f"Bonus column failed: {list(result['df']['bonus'])}"
    
    print("\nAll tests passed!")