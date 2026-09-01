\"\"\"
Exercise 3: Factorial
Topic: Recursion / Loops
Difficulty: Easy

Problem Statement:
Write a Python function to compute the factorial of a non-negative integer n.

Solution:
\"\"\"
def factorial(n):
    """
    Return the factorial of n (n!).
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test cases
if __name__ == "__main__":
    # Test Case 1: factorial of 0
    print(f"Test Case 1: factorial(0) = {factorial(0)}")  # Expected: 1
    
    # Test Case 2: factorial of 5
    print(f"Test Case 2: factorial(5) = {factorial(5)}")  # Expected: 120
    
    # Test Case 3: factorial of 7
    print(f"Test Case 3: factorial(7) = {factorial(7)}")  # Expected: 5040
    
    # Test Case 4: Error handling
    try:
        factorial(-1)
    except ValueError as e:
        print(f"Test Case 4: factorial(-1) raised ValueError: {e}")

# Complexity Analysis:
# Time Complexity: O(n) - Loop runs n times
# Space Complexity: O(1) - Constant extra space