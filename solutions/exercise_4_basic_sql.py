\"\"\"
Exercise 4: Basic SQL - SELECT Query
Topic: SQL querying
Difficulty: Easy

Problem Statement:
Given a table 'students' with columns: id (INTEGER), name (TEXT), age (INTEGER), grade (REAL).
Write a function that returns the SQL query to select the name and grade of students who are older than 18 and have a grade above 80.

Solution:
We'll construct the SQL query string.

Additionally, we'll demonstrate using sqlite3 to create an in-memory database, insert sample data, and run the query to verify.
\"\"\"

import sqlite3

def get_select_query():
    \"\"\"Return the SQL query string for selecting name and grade of students with age>18 and grade>80.\"\"\"
    return \"\"\"SELECT name, grade FROM students WHERE age > 18 AND grade > 80;\"\"\"

# Demonstration with sqlite3
if __name__ == \"__main__\":
    # Test the query string
    query = get_select_query()
    expected = \"\"\"SELECT name, grade FROM students WHERE age > 18 AND grade > 80;\"\"\"
    print(f\"Generated query: {query}\")
    assert query.strip() == expected.strip(), \"Query mismatch\"
    print(\"Query string test passed.\")
    
    # Create an in-memory database and test the query
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''CREATE TABLE students (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        grade REAL
                    )''')
    
    # Insert sample data
    sample_data = [
        (1, 'Alice', 20, 85.5),
        (2, 'Bob', 17, 90.0),
        (3, 'Charlie', 19, 75.0),
        (4, 'Diana', 22, 92.0),
        (5, 'Eve', 18, 80.0)
    ]
    cursor.executemany('INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)', sample_data)
    conn.commit()
    
    # Execute the query
    cursor.execute(get_select_query())
    results = cursor.fetchall()
    print(f\"Query results: {results}\")
    # Expected: Alice (20,85.5) and Diana (22,92.0) -> note: Eve is 18 (not >18) and grade 80 (not >80)
    expected_results = [('Alice', 85.5), ('Diana', 92.0)]
    assert set(results) == set(expected_results), f\"Expected {expected_results}, got {results}\"
    print(\"Database query test passed.\")
    
    conn.close()
    print(\"All tests passed.\")
\"\"\"