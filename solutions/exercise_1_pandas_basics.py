\"\"\"
Exercise 1: Basic Pandas DataFrame Operations (Easy)
Problem Statement:
Create a DataFrame from a dictionary containing student data (name, age, grade).
Then compute basic statistics: mean age, count of students per grade, and filter students older than 18.

Expected Output:
- DataFrame printed
- Mean age: X.X
- Grade counts: ...
- Students older than 18: (list of names)

Solution:
\"\"\"
import pandas as pd

def student_dataframe():
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [17, 19, 20, 18, 17],
        'grade': ['A', 'B', 'A', 'C', 'B']
    }
    df = pd.DataFrame(data)
    return df

def analyze_students(df):
    mean_age = df['age'].mean()
    grade_counts = df['grade'].value_counts().to_dict()
    older_than_18 = df[df['age'] > 18]['name'].tolist()
    return mean_age, grade_counts, older_than_18

if __name__ == "__main__":
    df = student_dataframe()
    print("Student DataFrame:")
    print(df)
    print()
    mean_age, grade_counts, older_than_18 = analyze_students(df)
    print(f"Mean age: {mean_age:.2f}")
    print(f"Grade counts: {grade_counts}")
    print(f"Students older than 18: {older_than_18}")
    
    # Simple test cases
    assert abs(mean_age - 18.2) < 0.01, f"Expected mean age 18.2, got {mean_age}"
    assert grade_counts == {'A': 2, 'B': 2, 'C': 1}, f"Grade counts mismatch: {grade_counts}"
    assert older_than_18 == ['Bob', 'Charlie'], f"Older than 18 mismatch: {older_than_18}"
    print("\nAll tests passed!")

\"\"\"
Time Complexity: O(n) for creating DataFrame and O(n) for each operation (mean, value_counts, filtering) -> overall O(n)
Space Complexity: O(n) for storing the DataFrame.
\"\"\"