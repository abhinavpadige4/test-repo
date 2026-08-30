\"\"\"
Exercise 2: Pandas DataFrames Basics
Problem Statement:
Write a function `analyze_dataframe` that takes a dictionary of lists (representing columns) and returns:
- A pandas DataFrame constructed from the dictionary.
- The summary statistics (describe) of the numeric columns.
- The data types of each column.

Requirements:
- Import pandas as pd.
- If the input dictionary is empty, return an empty DataFrame and None for stats and dtypes.
- Round numeric summary statistics to 2 decimal places.

Test Cases:
1. Input: {'A': [1, 2, 3, 4], 'B': [5.5, 6.5, 7.5, 8.5], 'C': ['x', 'y', 'z', 'w']}
   Expected Output: 
        df: DataFrame with columns A, B, C.
        stats: describe() for A and B (rounded to 2 decimals).
        dtypes: A: int64, B: float64, C: object.
2. Input: {'X': [10, 20, 30]}
   Expected Output: df with one column X, stats for X, dtypes: X: int64.
3. Input: {}
   Expected Output: empty DataFrame, stats: None, dtypes: None.

Complexity Analysis:
Time Complexity: O(n*m) where n is number of rows, m is number of columns (for DataFrame construction and describe).
Space Complexity: O(n*m) for storing the DataFrame.
\"\"\"

import pandas as pd
import numpy as np

def analyze_dataframe(data_dict):
    \"\"\"Create DataFrame from dict and compute summary stats and dtypes.
    
    Args:
        data_dict (dict): Keys are column names, values are lists of data.
        
    Returns:
        tuple: (DataFrame, stats_dict, dtypes_dict)
               stats_dict is None if DataFrame is empty or no numeric columns.
               dtypes_dict is None if DataFrame is empty.
    \"\"\"
    if not data_dict:
        df = pd.DataFrame()
        return df, None, None
    
    df = pd.DataFrame(data_dict)
    
    # Get dtypes
    dtypes_dict = df.dtypes.astype(str).to_dict()
    
    # Get summary statistics for numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        stats_dict = None
    else:
        stats = numeric_df.describe().round(2)
        # Convert to dict of dicts for easier reading
        stats_dict = stats.to_dict()
    
    return df, stats_dict, dtypes_dict


# Test cases
if __name__ == \"__main__\":
    # Test 1
    data1 = {'A': [1, 2, 3, 4], 'B': [5.5, 6.5, 7.5, 8.5], 'C': ['x', 'y', 'z', 'w']}
    df1, stats1, dtypes1 = analyze_dataframe(data1)
    print(\"Test 1:\")
    print(\"DataFrame:\\n\", df1)
    print(\"Statistics:\\n\", stats1)
    print(\"Dtypes:\\n\", dtypes1)
    print()
    
    # Test 2
    data2 = {'X': [10, 20, 30]}
    df2, stats2, dtypes2 = analyze_dataframe(data2)
    print(\"Test 2:\")
    print(\"DataFrame:\\n\", df2)
    print(\"Statistics:\\n\", stats2)
    print(\"Dtypes:\\n\", dtypes2)
    print()
    
    # Test 3
    data3 = {}
    df3, stats3, dtypes3 = analyze_dataframe(data3)
    print(\"Test 3:\")
    print(\"DataFrame:\\n\", df3)
    print(\"Statistics:\", stats3)
    print(\"Dtypes:\", dtypes3)