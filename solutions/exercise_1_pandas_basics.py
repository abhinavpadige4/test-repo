\"\"\"
Exercise 1: Basic Data Manipulation with Pandas (Easy)
Problem Statement:
Given a dictionary of student scores for three subjects (Math, Science, English),
create a pandas DataFrame, calculate the mean and median score for each subject,
and return the results as a new DataFrame.

Steps:
1. Import pandas.
2. Create a DataFrame from the provided data.
3. Compute mean and median for each subject.
4. Return a DataFrame with index ['mean', 'median'] and columns as subjects.

Example Input:
data = {
    'Math': [88, 92, 79, 85, 90],
    'Science': [84, 89, 78, 92, 85],
    'English': [90, 85, 88, 91, 87]
}

Expected Output:
           Math  Science  English
mean   86.8    85.6     88.2
median 88.0    89.0     88.0

Time Complexity: O(n*m) where n = number of rows, m = number of columns (single pass).
Space Complexity: O(m) for storing results.
\"\"\"
import pandas as pd

def compute_statistics(data: dict) -> pd.DataFrame:
    """
    Compute mean and median for each subject in the data dictionary.

    Parameters:
    data (dict): Keys are subject names, values are lists of scores.

    Returns:
    pd.DataFrame: DataFrame with index ['mean', 'median'] and columns as subjects.
    """
    df = pd.DataFrame(data)
    stats = pd.DataFrame({
        'mean': df.mean(),
        'median': df.median()
    }).T  # Transpose to have mean and median as rows
    return stats

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Test case 1: Provided example
    data1 = {
        'Math': [88, 92, 79, 85, 90],
        'Science': [84, 89, 78, 92, 85],
        'English': [90, 85, 88, 91, 87]
    }
    result1 = compute_statistics(data1)
    expected1 = pd.DataFrame({
        'Math': [86.8, 88.0],
        'Science': [85.6, 89.0],
        'English': [88.2, 88.0]
    }, index=['mean', 'median'])
    print("Test 1 - Result:")
    print(result1)
    print("Expected:")
    print(expected1)
    assert result1.round(2).equals(expected1.round(2)), "Test 1 failed"

    # Test case 2: Single student
    data2 = {'Math': [100], 'Science': [85], 'English': [90]}
    result2 = compute_statistics(data2)
    expected2 = pd.DataFrame({
        'Math': [100.0, 100.0],
        'Science': [85.0, 85.0],
        'English': [90.0, 90.0]
    }, index=['mean', 'median'])
    print("\nTest 2 - Result:")
    print(result2)
    assert result2.equals(expected2), "Test 2 failed"

    # Test case 3: Empty lists (should produce NaN)
    data3 = {'Math': [], 'Science': [], 'English': []}
    result3 = compute_statistics(data3)
    print("\nTest 3 - Result (empty data):")
    print(result3)
    # Check that all values are NaN
    assert result3.isna().all().all(), "Test 3 failed"

    print("\nAll tests passed!")