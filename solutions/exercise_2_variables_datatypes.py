\"\"\"
Exercise 2: Variables and Data Types
Topic: Basic Data Types
Difficulty: Easy

Problem Statement:
Write a program that declares variables of different data types (integer, float, string, boolean) and prints each variable along with its type.

Solution:
\"\"\"
def main():
    # Declare variables of different types
    age = 25                    # integer
    height = 5.9                # float
    name = "Alice"              # string
    is_student = True           # boolean
    
    # Print each variable and its type
    print(f"age: {age}, type: {type(age)}")
    print(f"height: {height}, type: {type(height)}")
    print(f"name: {name}, type: {type(name)}")
    print(f"is_student: {is_student}, type: {type(is_student)}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    import io
    import sys
    import re
    
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    main()
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    
    # Test Case 1: Check all lines are present
    lines = output.split('\n')
    assert len(lines) == 4, f"Expected 4 lines, got {len(lines)}"
    print("Test Case 1 Passed: 4 lines output")
    
    # Test Case 2: Check integer line
    assert re.search(r"age: 25, type: <class 'int'>", lines[0]), f"Line 1 mismatch: {lines[0]}"
    print("Test Case 2 Passed: Integer line correct")
    
    # Test Case 3: Check float line
    assert re.search(r"height: 5\.9, type: <class 'float'>", lines[1]), f"Line 2 mismatch: {lines[1]}"
    print("Test Case 3 Passed: Float line correct")
    
    # Test Case 4: Check string line
    assert re.search(r"name: Alice, type: <class 'str'>", lines[2]), f"Line 3 mismatch: {lines[2]}"
    print("Test Case 4 Passed: String line correct")
    
    # Test Case 5: Check boolean line
    assert re.search(r"is_student: True, type: <class 'bool'>", lines[3]), f"Line 4 mismatch: {lines[3]}"
    print("Test Case 5 Passed: Boolean line correct")
    
    print("\\nAll tests passed!")