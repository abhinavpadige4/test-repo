\"\"\"
Exercise 2: Data Cleaning with Pandas (Easy-Medium)
Problem Statement:
You are given a CSV file containing information about Titanic passengers.
The data has missing values in the 'Age' column and incorrect data types.
Your task is to:
1. Load the CSV data into a pandas DataFrame.
2. Convert the 'Age' column to numeric, coercing errors to NaN.
3. Fill missing 'Age' values with the median age of the respective passenger class (Pclass).
4. Convert the 'Sex' column to categorical codes (0 for female, 1 for male).
5. Return the cleaned DataFrame.

Note: For simplicity, we'll create a small sample dataset in the code.

Expected Output (after cleaning):
   PassengerId  Survived  Pclass  ...  Fare  Embarked  Sex_code
0            1         0       3  ...   7.2500        S         1
1            2         1       1  ...  71.2833        C         0
...

Time Complexity: O(n) for each operation (loading, converting, filling, mapping).
Space Complexity: O(n) for storing the DataFrame.
\"\"\"
import pandas as pd
import numpy as np

def clean_titanic_data(csv_path: str = None) -> pd.DataFrame:
    """
    Clean the Titanic dataset.

    Parameters:
    csv_path (str): Path to the CSV file. If None, a sample dataset is used.

    Returns:
    pd.DataFrame: Cleaned DataFrame with processed Age, Sex, etc.
    """
    if csv_path is None:
        # Create a sample dataset for demonstration
        data = {
            'PassengerId': [1, 2, 3, 4, 5],
            'Survived': [0, 1, 1, 0, 0],
            'Pclass': [3, 1, 3, 1, 3],
            'Name': ['Braund, Mr. Owen Harris',
                     'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
                     'Heikkinen, Miss. Laina',
                     'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
                     'Allen, Mr. William Henry'],
            'Sex': ['male', 'female', 'female', 'female', 'male'],
            'Age': [22, 38, 26, 35, np.nan],
            'SibSp': [1, 1, 0, 1, 0],
            'Parch': [0, 0, 0, 0, 0],
            'Ticket': ['A/5 21171', 'PC 17599',
                       'STON/O2. 3101282', '113803', '373450'],
            'Fare': [7.25, 71.2833, 7.925, 53.1, 8.05],
            'Cabin': [np.nan, 'C85', np.nan, 'C123', np.nan],
            'Embarked': ['S', 'C', 'S', 'S', 'S']
        }
        df = pd.DataFrame(data)
    else:
        df = pd.read_csv(csv_path)

    # Convert Age to numeric, coercing errors to NaN
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

    # Fill missing Age with median of each Pclass
    df['Age'] = df.groupby('Pclass')['Age'].transform(
        lambda x: x.fillna(x.median())
    )

    # Convert Sex to categorical codes: female -> 0, male -> 1
    df['Sex_code'] = df['Sex'].map({'female': 0, 'male': 1})
    # Alternatively, we can use: df['Sex_code'] = pd.factorize(df['Sex'])[0]

    # For the purpose of this exercise, we return the DataFrame with the new column
    # and we can drop the original 'Sex' column if desired, but we'll keep it for clarity.
    return df

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Test case 1: Using the sample data
    cleaned_df = clean_titanic_data()
    print("Cleaned DataFrame (first 5 rows):")
    print(cleaned_df.head())
    print("\nData types:")
    print(cleaned_df.dtypes)

    # Check that Age has no missing values
    assert cleaned_df['Age'].isna().sum() == 0, "Age still has missing values"

    # Check that Sex_code is present and correctly mapped
    assert 'Sex_code' in cleaned_df.columns, "Sex_code column missing"
    # Check a few known mappings
    # Female -> 0, Male -> 1
    # We can check by looking at the original Sex and the new Sex_code
    for idx, row in cleaned_df.iterrows():
        if row['Sex'] == 'female':
            assert row['Sex_code'] == 0, f"Expected 0 for female at index {idx}"
        elif row['Sex'] == 'male':
            assert row['Sex_code'] == 1, f"Expected 1 for male at index {idx}"

    # Test case 2: If we had a CSV, we would test with a file. We'll skip for now.

    print("\nAll tests passed!")