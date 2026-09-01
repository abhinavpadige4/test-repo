\"\"\"
Exercise 3: Factorial of a Number
Topic: Recursion / Loop
Difficulty: Easy

Problem Statement:
Write a Python function to calculate the factorial of a non-negative integer.

Solution:
\"\"\"

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test Cases
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040
    try:
        factorial(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass
    print("All tests passed!")

if __name__ == "__main__":
    test_factorial()

# Complexity Analysis:
# Time Complexity: O(n) - loop runs n times
# Space Complexity: O(1) - constant space used