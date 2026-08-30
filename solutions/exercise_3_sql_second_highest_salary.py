\"\"\"
Exercise 3: SQL Query - Second Highest Salary
Topic: Data Wrangling and SQL
Difficulty: Easy

Problem Statement:
Write a Python function that returns the SQL query string to find the second highest salary from an Employee table.
The Employee table has columns: id (INT), name (VARCHAR), salary (INT).

Requirements:
- Return a single SQL query string that works in standard SQL
- Handle edge case where there is no second highest salary (return NULL)
- Do not use LIMIT and OFFSET (to demonstrate understanding of subqueries)
- The query should return a single column named 'SecondHighestSalary'

Example:
Given Employee table:
+----+--------+--------+
| id | name   | salary |
+----+--------+--------+
| 1  | Joe    | 70000  |
| 2  | Henry  | 80000  |
| 3  | Sam    | 60000  |
| 4  | Max    | 90000  |
+----+--------+--------+
The query should return 80000 as the second highest salary.
\"\"\"

def get_second_highest_salary_query() -> str:
    """
    Returns the SQL query to find the second highest salary from Employee table.
    
    Returns:
        str: SQL query string
    """
    query = """
    SELECT MAX(salary) AS SecondHighestSalary
    FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee)
    """
    return query.strip()

# Test cases
if __name__ == "__main__":
    import sqlite3
    
    # Test the query by running it on a sample database
    def test_query():
        # Create in-memory database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        # Create Employee table
        cursor.execute('''
            CREATE TABLE Employee (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                salary INTEGER NOT NULL
            )
        ''')
        
        # Insert test data
        employees = [
            (1, 'Joe', 70000),
            (2, 'Henry', 80000),
            (3, 'Sam', 60000),
            (4, 'Max', 90000)
        ]
        cursor.executemany('INSERT INTO Employee (id, name, salary) VALUES (?, ?, ?)', employees)
        conn.commit()
        
        # Get the query and execute it
        query = get_second_highest_salary_query()
        print("Generated SQL Query:")
        print(query)
        print()
        
        cursor.execute(query)
        result = cursor.fetchone()
        print("Query Result:", result)
        print("Expected: (80000,)")
        assert result[0] == 80000, f"Expected 80000, got {result[0]}"
        print("✓ Test 1 passed: Normal case\\n")
        
        # Test edge case: only one employee
        conn.execute('DELETE FROM Employee')
        conn.execute('INSERT INTO Employee (id, name, salary) VALUES (1, \"Solo\", 50000)')
        conn.commit()
        
        cursor.execute(query)
        result = cursor.fetchone()
        print("Test 2 - Only one employee:")
        print("Query Result:", result)
        print("Expected: (None,) because there is no second highest")
        assert result[0] is None, f"Expected None, got {result[0]}"
        print("✓ Test 2 passed: Single employee\\n")
        
        # Test edge case: all same salaries
        conn.execute('DELETE FROM Employee')
        conn.execute('INSERT INTO Employee (id, name, salary) VALUES (1, \"A\", 50000)')
        conn.execute('INSERT INTO Employee (id, name, salary) VALUES (2, \"B\", 50000)')
        conn.execute('INSERT INTO Employee (id, name, salary) VALUES (3, \"C\", 50000)')
        conn.commit()
        
        cursor.execute(query)
        result = cursor.fetchone()
        print("Test 3 - All same salaries:")
        print("Query Result:", result)
        print("Expected: (None,) because no distinct second highest")
        assert result[0] is None, f"Expected None, got {result[0]}"
        print("✓ Test 3 passed: All same salaries\\n")
        
        # Test edge case: empty table
        conn.execute('DELETE FROM Employee')
        conn.commit()
        
        cursor.execute(query)
        result = cursor.fetchone()
        print("Test 4 - Empty table:")
        print("Query Result:", result)
        print("Expected: (None,)")
        assert result[0] is None, f"Expected None, got {result[0]}"
        print("✓ Test 4 passed: Empty table\\n")
        
        conn.close()
        print("All tests passed!")
    
    test_query()

# Complexity Analysis:
# Time Complexity: O(n) where n is number of rows in Employee table
# Space Complexity: O(1) - the query uses constant extra space