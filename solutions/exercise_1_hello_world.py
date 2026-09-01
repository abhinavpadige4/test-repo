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

# Test cases
if __name__ == "__main__":
    # Test Case 1: Basic functionality
    print("Test Case 1:")
    hello_world()  # Expected: Hello, World!
    
    # Test Case 2: Verify it's a function
    print("\\nTest Case 2: Function type")
    print(type(hello_world))  # Expected: <class 'function'>
    
    # Test Case 3: Verify it returns None
    print("\\nTest Case 3: Return value")
    result = hello_world()
    print(f"Return value: {result}")  # Expected: None

# Complexity Analysis:
# Time Complexity: O(1) - Constant time operation
# Space Complexity: O(1) - No additional space used