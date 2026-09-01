"""
Exercise 15: Pow(x, n)
=====================

Problem Statement:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example:
Input: x = 2.00000, n = 10
Output: 1024.00000

Approach:
Use fast exponentiation (exponentiation by squaring):
- For positive n: x^n = (x^(n/2))^2 if n is even, x*(x^(n/2))^2 if n is odd
- For negative n: x^n = 1/(x^(-n))
- Base cases: x^0 = 1, x^1 = x

This reduces time complexity from O(n) to O(log n) by halving the exponent at each step.

Time Complexity: O(log n)
Space Complexity: O(log n) due to recursion stack
"""

def my_pow(x, n):
    """
    Calculate x raised to the power n.
    
    Args:
        x (float): Base
        n (int): Exponent
        
    Returns:
        float: x^n
    """
    # Handle base cases
    if n == 0:
        return 1.0
    if n == 1:
        return x
    
    # For negative exponents, compute reciprocal of positive power
    if n < 0:
        return 1.0 / my_pow(x, -n)
    
    # Recursive computation using exponentiation by squaring
    # x^n = (x^(n/2))^2 if n is even
    # x^n = x * (x^(n/2))^2 if n is odd
    half_power = my_pow(x, n // 2)
    
    if n % 2 == 0:
        return half_power * half_power
    else:
        return x * half_power * half_power

# Iterative implementation (to avoid recursion stack overflow for large n)
def my_pow_iterative(x, n):
    """
    Calculate x raised to the power n (iterative approach).
    
    Args:
        x (float): Base
        n (int): Exponent
        
    Returns:
        float: x^n
    """
    # Handle negative exponent
    if n < 0:
        x = 1.0 / x
        n = -n
    
    result = 1.0
    current_product = x
    
    # Process exponent bit by bit
    while n > 0:
        # If n is odd, multiply result by current product
        if n % 2 == 1:
            result *= current_product
        
        # Square the current product and halve the exponent
        current_product *= current_product
        n //= 2
    
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Positive exponent
    x1, n1 = 2.0, 10
    result1 = my_pow(x1, n1)
    print(f"Test 1: {x1}^{n1} = {result1}")  # Expected: 1024.0
    
    # Test Case 2: Negative exponent
    x2, n2 = 2.0, -2
    result2 = my_pow(x2, n2)
    print(f"Test 2: {x2}^{n2} = {result2}")  # Expected: 0.25
    
    # Test Case 3: Fractional base
    x3, n3 = 2.1, 3
    result3 = my_pow(x3, n3)
    print(f"Test 3: {x3}^{n3} = {result3}")  # Expected: 9.261
    
    # Test Case 4: Zero exponent
    x4, n4 = 5.0, 0
    result4 = my_pow(x4, n4)
    print(f"Test 4: {x4}^{n4} = {result4}")  # Expected: 1.0
    
    # Test Case 5: Using iterative implementation
    x5, n5 = 3.0, 4
    result5 = my_pow_iterative(x5, n5)
    print(f"Test 5: {x5}^{n5} = {result5}")  # Expected: 81.0