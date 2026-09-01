\"\"\"
Exercise 2: Add Two Numbers
Topic: Basic Arithmetic
Difficulty: Easy

Problem Statement:
Write a Python function that takes two numbers as input and returns their sum.

Solution:
\"\"\"
def add_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Sum of a and b
    """
    return a + b

# Test cases
if __name__ == "__main__":
    # Test Case 1: Positive integers
    result1 = add_two_numbers(3, 5)
    print(f"Test Case 1: 3 + 5 = {result1}")  # Expected: 8
    
    # Test Case 2: Negative and positive
    result2 = add_two_numbers(-2, 7)
    print(f"Test Case 2: -2 + 7 = {result2}")  # Expected: 5
    
    # Test Case 3: Floating point
    result3 = add_two_numbers(3.5, 2.5)
    print(f"Test Case 3: 3.5 + 2.5 = {result3}")  # Expected: 6.0

# Complexity Analysis:
# Time Complexity: O(1) - Constant time operation
# Space Complexity: O(1) - No additional space used