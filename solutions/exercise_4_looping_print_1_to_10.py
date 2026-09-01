\"\"\"
Exercise 4: Looping - Print Numbers 1 to 10
Topic: Loops
Difficulty: Easy

Problem Statement:
Write a program that prints the numbers from 1 to 10 (inclusive) each on a new line.

Solution:
\"\"\"
def main():
    for i in range(1, 11):
        print(i)

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    import io
    import sys
    
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    main()
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    
    # Test Case 1: Check number of lines
    lines = output.split('\n')
    assert len(lines) == 10, f"Expected 10 lines, got {len(lines)}"
    print("Test Case 1 Passed: 10 lines")
    
    # Test Case 2: Check each line is correct
    for i, line in enumerate(lines, start=1):
        assert line == str(i), f"Line {i} expected '{i}', got '{line}'"
    print("Test Case 2 Passed: All lines correct")
    
    # Test Case 3: Check no extra whitespace
    assert output == '\n'.join(str(i) for i in range(1, 11)), "Output has extra whitespace"
    print("Test Case 3 Passed: No extra whitespace")
    
    print("\\nAll tests passed!")