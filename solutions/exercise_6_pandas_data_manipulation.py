\"\"\"
Exercise 6: pandas - Data Manipulation (Filtering, Grouping, etc.)
Difficulty: Medium
Topic: pandas

Problem Statement:
Write a Python script using pandas to:
1. Load a sample dataset (we'll create a DataFrame simulating employee data)
2. Filter rows based on conditions (e.g., salary > 50000)
3. Group data by a column and calculate aggregates (e.g., average salary by department)
4. Pivot table to show average salary by department and job title
5. Handle missing values by filling or dropping

Expected Output:
Original DataFrame:
      name  department  salary  job_title  years_experience
0    Alice          HR   50000     Manager                 5
1      Bob        IT   60000  Developer                 3
2  Charlie        IT   70000  Developer                 7
3    Diana        HR   45000   Analyst                 2
4     Eve      Finance   55000   Analyst                 4
5   Frank      Finance   65000  Manager                 6
6    Grace          IT   52000000  Developer                 1
7   Henry          HR   48000   Analyst                 3

Filtered DataFrame (salary > 50000):
      name  department  salary  job_title  years_experience
1      Bob        IT   60000  Developer                 3
2  Charlie        IT   70000  Developer                 7
4     Eve      Finance   55000   Analyst                 4
5   Frank      Finance   65000  Manager                 6

Grouped by department (average salary):
department
Finance    60000.0
HR         47666.7
IT         60666.7
Name: salary, dtype: float64

Pivot table (average salary by department and job_title):
job_title    Analyst  Developer  Manager
department                            
Finance   55000.0        NaN  65000.0
HR        46500.0        NaN  50000.0
IT             NaN  61333.3        NaN

DataFrame after filling missing values with 0:
job_title    Analyst  Developer  Manager
department                            
Finance   55000.0      0.0  65000.0
HR        46500.0      0.0  50000.0
IT             0.0  61333.3      0.0
\"\"\"

import pandas as pd
import numpy as np

def pandas_data_manipulation():
    """
    Demonstrate pandas data manipulation techniques.
    Returns:
        dict: Results for testing
    """
    # Create sample DataFrame
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
        'department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
        'salary': [50000, 60000, 70000, 45000, 55000, 65000, 50000, 48000],
        'job_title': ['Manager', 'Developer', 'Developer', 'Analyst', 'Analyst', 'Manager', 'Developer', 'Analyst'],
        'years_experience': [5, 3, 7, 2, 4, 6, 1, 3]
    }
    df = pd.DataFrame(data)
    
    # 1. Filter rows (salary > 50000)
    filtered_df = df[df['salary'] > 50000]
    
    # 2. Group by department and calculate mean salary
    grouped = df.groupby('department')['salary'].mean()
    
    # 3. Pivot table: average salary by department and job_title
    pivot_table = df.pivot_table(values='salary', index='department', columns='job_title', aggfunc='mean')
    
    # 4. Handle missing values in pivot table (fill with 0)
    pivot_filled = pivot_table.fillna(0)
    
    # Print results
    print("Original DataFrame:")
    print(df)
    print("\nFiltered DataFrame (salary > 50000):")
    print(filtered_df)
    print("\nGrouped by department (average salary):")
    print(grouped)
    print("\nPivot table (average salary by department and job_title):")
    print(pivot_table)
    print("\nDataFrame after filling missing values with 0:")
    print(pivot_filled)
    
    # Return for testing
    return {
        "df": df,
        "filtered_df": filtered_df,
        "grouped": grouped,
        "pivot_table": pivot_table,
        "pivot_filled": pivot_filled
    }

# Test cases
if __name__ == "__main__":
    result = pandas_data_manipulation()
    
    # Test 1: Original DataFrame shape
    assert result["df"].shape == (8, 5), f"DataFrame shape failed: {result['df'].shape}"
    
    # Test 2: Filtered DataFrame (salary > 50000) should have 4 rows (Bob, Charlie, Eve, Frank)
    assert len(result["filtered_df"]) == 4, f"Filtered DataFrame length failed: {len(result['filtered_df'])}"
    
    # Test 3: Check specific filtered row (Alice with salary 50000 is not > 50000, so excluded)
    assert "Alice" not in result["filtered_df"]["name"].values, "Alice should not be in filtered DataFrame (salary not > 50000)"
    
    # Test 4: Grouped Finance average salary
    finance_avg = result["grouped"]["Finance"]
    assert abs(finance_avg - 60000.0) < 0.001, f"Finance average salary failed: {finance_avg}"
    
    # Test 5: Pivot table has NaN for missing combinations
    # Check that the pivot table has NaN for HR, Developer (since there is no Developer in HR)
    assert pd.isna(result["pivot_table"].loc["HR", "Developer"]), "Expected NaN for HR, Developer"
    
    # Test 6: After filling, the NaN becomes 0
    assert result["pivot_filled"].loc["HR", "Developer"] == 0.0, f"Expected 0.0 after fillna, got {result['pivot_filled'].loc['HR', 'Developer']}"
    
    print("\nAll tests passed!")