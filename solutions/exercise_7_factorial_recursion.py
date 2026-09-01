\"\"\"
Exercise 7: Factorial using Recursion
Topic: Recursion
Difficulty: Medium

Problem Statement:
Write a recursive function to calculate the factorial of a non-negative integer.
The factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.

Solution:
\"\"\"
def factorial(n):
    """
    Calculate factorial of a non-negative integer using recursion.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    # Test the function with examples
    test_values = [0, 1, 5, 7, 10]
    for n in test_values:
        print(f"Factorial of {n} is {factorial(n)}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Factorial of 0
    assert factorial(0) == 1, "Test 1 failed"
    print("Test Case 1 Passed: factorial(0) = 1")
    
    # Test Case 2: Factorial of 1
    assert factorial(1) == 1, "Test 2 failed"
    print("Test Case 2 Passed: factorial(1) = 1")
    
    # Test Case 3: Factorial of 5
    assert factorial(5) == 120, "Test 3 failed"
    print("Test Case 3 Passed: factorial(5) = 120")
    
    # Test Case 4: Factorial of 7
    assert factorial(7) == 5040, "Test 4 failed"
    print("Test Case 4 Passed: factorial(7) = 5040")
    
    # Test Case 5: Factorial of 10
    assert factorial(10) == 3628800, "Test 5 failed"
    print("Test Case 5 Passed: factorial(10) = 3628800")
    
    # Test Case 6: Negative input raises ValueError
    try:
        factorial(-1)
        assert False, "Test 6 failed: Expected ValueError"
    except ValueError:
        print("Test Case 6 Passed: Negative input raises ValueError")
    
    print("\\nAll tests passed!")