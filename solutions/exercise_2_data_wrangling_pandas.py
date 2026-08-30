\"\"\"
Exercise 2: Data Wrangling with Pandas - Handling Missing Values
Topic: Data Wrangling and SQL
Difficulty: Easy

Problem Statement:
Write a Python function that takes a pandas DataFrame and handles missing values according to the following strategy:
- For numeric columns: fill missing values with the median of the column
- For categorical columns: fill missing values with the mode of the column
- Return the cleaned DataFrame

Requirements:
- Do not modify the original DataFrame (return a copy)
- Handle edge cases where a column might be all NaN
- Use pandas built-in functions

Example:
Input DataFrame:
   age  salary department
0   25   50000        IT
1   30      NaN        HR
2   NaN  60000        IT
3   35   55000      NaN
4   NaN      NaN        IT

Output:
   age  salary department
0  25.0  50000        IT
1  30.0  55000        HR
2  30.0  60000        IT
3  35.0  55000        IT
4  30.0  55000        IT
\"\"\"

import pandas as pd
import numpy as np
from typing import Union

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.
    
    Args:
        df: Input pandas DataFrame
        
    Returns:
        DataFrame with missing values handled:
        - Numeric columns filled with median
        - Categorical columns filled with mode
    """
    # Create a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Identify numeric and categorical columns
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    
    # Handle numeric columns: fill with median
    for col in numeric_cols:
        if df_clean[col].isnull().any():
            median_val = df_clean[col].median()
            # If all values are NaN, median will be NaN, so fill with 0
            if pd.isna(median_val):
                median_val = 0
            df_clean[col] = df_clean[col].fillna(median_val)
    
    # Handle categorical columns: fill with mode
    for col in categorical_cols:
        if df_clean[col].isnull().any():
            mode_val = df_clean[col].mode()
            # If mode is empty (all NaN), fill with 'Unknown'
            if mode_val.empty:
                mode_val = 'Unknown'
            else:
                mode_val = mode_val.iloc[0]
            df_clean[col] = df_clean[col].fillna(mode_val)
    
    return df_clean

# Test cases
if __name__ == "__main__":
    # Test case 1: Mixed data with missing values
    data1 = {
        'age': [25, 30, np.nan, 35, np.nan],
        'salary': [50000, np.nan, 60000, 55000, np.nan],
        'department': ['IT', 'HR', 'IT', np.nan, 'IT']
    }
    df1 = pd.DataFrame(data1)
    result1 = handle_missing_values(df1)
    print("Test 1 - Original DataFrame:")
    print(df1)
    print("\\nAfter handling missing values:")
    print(result1)
    
    # Expected values:
    # age: median of [25, 30, 35] = 30 -> fill NaNs with 30
    # salary: median of [50000, 60000, 55000] = 55000 -> fill NaNs with 55000
    # department: mode is 'IT' -> fill NaN with 'IT'
    expected_age = [25.0, 30.0, 30.0, 35.0, 30.0]
    expected_salary = [50000.0, 55000.0, 60000.0, 55000.0, 55000.0]
    expected_dept = ['IT', 'HR', 'IT', 'IT', 'IT']
    
    assert result1['age'].tolist() == expected_age
    assert result1['salary'].tolist() == expected_salary
    assert result1['department'].tolist() == expected_dept
    print("✓ Test 1 passed\\n")
    
    # Test case 2: All NaN in a column
    data2 = {
        'all_nan_num': [np.nan, np.nan, np.nan],
        'all_nan_cat': [np.nan, np.nan, np.nan],
        'normal': [1, 2, 3]
    }
    df2 = pd.DataFrame(data2)
    result2 = handle_missing_values(df2)
    print("Test 2 - Original DataFrame:")
    print(df2)
    print("\\nAfter handling missing values:")
    print(result2)
    
    # all_nan_num: median is NaN -> fill with 0
    # all_nan_cat: mode is empty -> fill with 'Unknown'
    # normal: unchanged
    assert result2['all_nan_num'].tolist() == [0, 0, 0]
    assert result2['all_nan_cat'].tolist() == ['Unknown', 'Unknown', 'Unknown']
    assert result2['normal'].tolist() == [1, 2, 3]
    print("✓ Test 2 passed\\n")
    
    # Test case 3: No missing values
    data3 = {
        'x': [1, 2, 3],
        'y': ['a', 'b', 'c']
    }
    df3 = pd.DataFrame(data3)
    result3 = handle_missing_values(df3)
    print("Test 3 - Original DataFrame:")
    print(df3)
    print("\\nAfter handling missing values (should be unchanged):")
    print(result3)
    
    assert result3.equals(df3)
    print("✓ Test 3 passed\\n")
    
    print("All tests passed!")

# Complexity Analysis:
# Time Complexity: O(n*m) where n is number of rows, m is number of columns
# Space Complexity: O(n*m) for the copy of the DataFrame