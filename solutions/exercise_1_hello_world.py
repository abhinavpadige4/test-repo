\"\"\"
Exercise 1: Hello World
Topic: Basic Syntax
Difficulty: Easy

Problem Statement:
Write a Python program that prints "Hello, World!" to the console.

Solution:
\"\"\"

def hello_world():
    """
    Prints Hello, World! to the console.
    """
    print("Hello, World!")

if __name__ == "__main__":
    hello_world()

# Test Cases
def test_hello_world():
    import io
    import sys
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    hello_world()
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    assert output == "Hello, World!", f"Expected 'Hello, World!', got '{output}'"

# Run tests
if __name__ == "__main__":
    test_hello_world()
    print("All tests passed!")

# Complexity Analysis:
# Time Complexity: O(1) - constant time operation
# Space Complexity: O(1) - constant space used