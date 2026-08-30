\"\"\"
Exercise 2: Data Cleaning with Pandas (Medium)
Problem Statement:
Given a CSV file with missing values and inconsistent data, perform the following:
1. Load the data (we'll simulate with a dictionary for simplicity)
2. Handle missing values: fill numeric columns with mean, categorical with mode
3. Remove duplicates
4. Convert data types appropriately
5. Output cleaned DataFrame and summary

Expected Output:
- Original shape and cleaned shape
- Information about missing values before and after
- Data types after cleaning

Solution:
\"\"\"
import pandas as pd
import numpy as np

def create_sample_data():
    """Create a sample dataset with issues for demonstration."""
    data = {
        'age': [25, np.nan, 30, 35, 25, 40, np.nan, 28],
        'salary': [50000, 60000, np.nan, 80000, 50000, 90000, 70000, np.nan],
        'department': ['HR', 'IT', 'Finance', 'HR', 'HR', 'IT', np.nan, 'Finance'],
        'experience': [2, 3, 5, np.nan, 2, 7, 4, 3]
    }
    df = pd.DataFrame(data)
    # Add some duplicates
    df = pd.concat([df, df.iloc[[0, 2]]], ignore_index=True)
    return df

def clean_data(df):
    """Clean the DataFrame."""
    # Make a copy to avoid modifying original
    df_clean = df.copy()
    
    # 1. Handle missing values
    # Numeric columns: fill with mean
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df_clean[col].fillna(df_clean[col].mean(), inplace=True)
    
    # Categorical columns: fill with mode
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df_clean[col].fillna(df_clean[col].mode()[0] if not df_clean[col].mode().empty else 'Unknown', inplace=True)
    
    # 2. Remove duplicates
    df_clean.drop_duplicates(inplace=True)
    
    # 3. Convert data types (if needed)
    # For example, convert experience to int if it's whole number after filling
    df_clean['experience'] = df_clean['experience'].round().astype(int)
    
    return df_clean

if __name__ == "__main__":
    # Create sample data
    df_original = create_sample_data()
    print("Original DataFrame:")
    print(df_original)
    print(f"\nOriginal shape: {df_original.shape}")
    print("\nMissing values in original:")
    print(df_original.isnull().sum())
    
    # Clean the data
    df_cleaned = clean_data(df_original)
    print("\n" + "="*50)
    print("Cleaned DataFrame:")
    print(df_cleaned)
    print(f"\nCleaned shape: {df_cleaned.shape}")
    print("\nMissing values after cleaning:")
    print(df_cleaned.isnull().sum())
    print("\nData types after cleaning:")
    print(df_cleaned.dtypes)
    
    # Test cases
    assert df_cleaned.isnull().sum().sum() == 0, "There are still missing values!"
    assert df_cleaned.shape[0] == 6, f"Expected 6 rows after removing duplicates, got {df_cleaned.shape[0]}"
    assert df_cleaned['experience'].dtype == 'int64', "Experience should be integer"
    print("\nAll tests passed!")

\"\"\"
Time Complexity: O(n) for most operations (filling, dropping duplicates) where n is number of rows.
Space Complexity: O(n) for storing the DataFrame.
\"\"\"