\"\"\"
Exercise 1: Hello World
Topic: Basic Syntax
Difficulty: Easy

Problem Statement:
Write a program that prints "Hello, World!" to the console.

Solution:
\"\"\"
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic output
    import io
    import sys
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    main()
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    assert output == "Hello, World!", f"Expected 'Hello, World!', got '{output}'"
    print("Test Case 1 Passed")

    # Test Case 2: Ensure no extra whitespace
    assert output == "Hello, World!", "Output should be exactly 'Hello, World!'"
    print("Test Case 2 Passed")

    # Test Case 3: Check length
    assert len(output) == 13, f"Expected length 13, got {len(output)}"
    print("Test Case 3 Passed")

print("\\nAll tests passed!")