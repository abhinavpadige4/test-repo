\"\"\"
Exercise 1: Pandas Basics (Easy)
Problem Statement:
Given a CSV file containing student scores in three subjects (Math, Science, English),
write a Python script that:
1. Loads the data into a pandas DataFrame.
2. Calculates the average score for each student.
3. Adds a new column 'Average' with these averages.
4. Filters students who have an average score above 80.
5. Saves the filtered DataFrame to a new CSV file 'top_students.csv'.

Assume the input CSV 'students.csv' has columns: StudentID, Name, Math, Science, English.

Provide a solution that includes reading from a string (for self-contained testing) and writing to a string.
\"\"\"
import pandas as pd
import io

def process_student_scores(csv_data: str) -> str:
    """
    Process student scores CSV data and return filtered CSV as string.
    
    Args:
        csv_data: CSV content as a string.
    
    Returns:
        CSV string of students with average > 80.
    """
    # Load data
    df = pd.read_csv(io.StringIO(csv_data))
    
    # Calculate average
    df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
    
    # Filter
    filtered = df[df['Average'] > 80].copy()
    
    # Return as CSV string
    output = io.StringIO()
    filtered.to_csv(output, index=False)
    return output.getvalue()

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Test data
    test_csv = """StudentID,Name,Math,Science,English
1,Alice,85,90,95
2,Bob,70,75,80
3,Charlie,90,85,88
4,David,60,65,70
5,Eve,95,92,96
"""
    
    result = process_student_scores(test_csv)
    print("Filtered CSV (Average > 80):")
    print(result)
    
    # Expected output (for verification)
    expected_lines = [
        "StudentID,Name,Math,Science,English,Average",
        "1,Alice,85,90,95,90.0",
        "3,Charlie,90,85,88,87.66666666666667",
        "5,Eve,95,92,96,94.33333333333333"
    ]
    expected = "\n".join(expected_lines) + "\n"
    
    assert result == expected, "Test failed: Output does not match expected."
    print("All tests passed!")
    
    # Complexity Analysis:
    # Time Complexity: O(n) where n is number of rows (each row processed constant times)
    # Space Complexity: O(n) for storing the DataFrame