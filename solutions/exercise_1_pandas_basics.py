\"\"\"
Exercise 1: Basic Data Loading and Exploration with Pandas
Topic: Pandas Basics
Difficulty: Easy

Problem Statement:
Write a Python script that:
1. Loads the CSV file 'data.csv' (provided in the same directory) into a pandas DataFrame.
2. Displays the first 5 rows.
3. Shows the shape of the DataFrame.
4. Lists column names and data types.
5. Computes basic statistics (mean, median, std) for numeric columns.
6. Handles missing values by filling them with the column mean.
7. Saves the cleaned DataFrame to 'cleaned_data.csv'.

Assume 'data.csv' contains a mix of numeric and categorical columns with some missing values.

Provide test cases using a small synthetic DataFrame.

\"\"\"
import pandas as pd
import numpy as np
import os

def load_and_explore(file_path):
    """
    Load CSV, explore, clean missing values, and save cleaned data.
    
    Parameters:
    file_path (str): Path to the input CSV file.
    
    Returns:
    pd.DataFrame: Cleaned DataFrame.
    """
    # Load data
    df = pd.read_csv(file_path)
    
    # Display first 5 rows
    print("First 5 rows:")
    print(df.head())
    print("\n")
    
    # Shape
    print(f"Shape: {df.shape}")
    print("\n")
    
    # Column names and data types
    print("Column names and data types:")
    print(df.dtypes)
    print("\n")
    
    # Basic statistics for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print("Basic statistics for numeric columns:")
        print(df[numeric_cols].describe())
        print("\n")
    else:
        print("No numeric columns found.\n")
    
    # Handle missing values: fill with column mean for numeric columns
    df_cleaned = df.copy()
    for col in numeric_cols:
        df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
    
    # For categorical columns, fill missing with mode (optional)
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df_cleaned[col].fillna(df_cleaned[col].mode()[0] if not df_cleaned[col].mode().empty else '', inplace=True)
    
    # Save cleaned data
    output_path = os.path.splitext(file_path)[0] + '_cleaned.csv'
    df_cleaned.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    
    return df_cleaned

# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    # Create a synthetic CSV for testing
    test_data = {
        'Age': [25, 30, np.nan, 40, 35],
        'Salary': [50000, 60000, 55000, np.nan, 65000],
        'Department': ['HR', 'Engineering', 'Engineering', 'HR', np.nan]
    }
    test_df = pd.DataFrame(test_data)
    test_file = 'test_data.csv'
    test_df.to_csv(test_file, index=False)
    
    print("=== Running Exercise 1 Tests ===")
    cleaned = load_and_explore(test_file)
    
    # Verify no missing values remain
    assert cleaned.isnull().sum().sum() == 0, "There are still missing values!"
    # Verify shape unchanged
    assert cleaned.shape == test_df.shape, "Shape changed after cleaning!"
    # Verify file saved
    assert os.path.exists('test_data_cleaned.csv'), "Cleaned file not saved!"
    
    print("\nAll tests passed!")
    
    # Cleanup test files
    os.remove(test_file)
    os.remove('test_data_cleaned.csv')