"""
Problem Statement:
    Write a function to compute the factorial of a non-negative integer.
    The factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.

Solution:
    Use iterative approach to avoid recursion depth issues.

Test Cases:
    Test Case 1:
        Input: 0
        Expected Output: 1

    Test Case 2:
        Input: 5
        Expected Output: 120

    Test Case 3:
        Input: 7
        Expected Output: 5040

Expected Output:
    For the test cases above, the function should return:
        1
        120
        5040

Time Complexity: O(n) - loop from 1 to n.
Space Complexity: O(1) - constant space.
"""

def factorial(n: int) -> int:
    """
    Return the factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    test_cases = [
        (0, 1),
        (5, 120),
        (7, 5040),
        (1, 1),
        (3, 6),
    ]

    print("Running test cases for factorial:")
    for i, (input_n, expected) in enumerate(test_cases, 1):
        result = factorial(input_n)
        print(f"Test {i}: Input: {input_n} -> Output: {result}, Expected: {expected}")
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
    print("All tests passed!")