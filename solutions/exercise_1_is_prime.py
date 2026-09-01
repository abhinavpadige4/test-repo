"""
Exercise 1: Check if a Number is Prime
Topic: Basic Number Theory
Difficulty: Easy

Problem Statement:
Write a function that takes an integer as input and returns True if the number is prime, False otherwise.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Solution:
We check divisibility from 2 to the square root of the number (inclusive). If any divisor is found, the number is not prime.
Edge cases: numbers less than 2 are not prime.
"""

import math

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if n is prime, False otherwise
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
if __name__ == "__main__":
    # Test case 1: Prime number
    test1 = is_prime(11)
    print(f"Test 1 - is_prime(11): {test1} (Expected: True)")
    
    # Test case 2: Non-prime number
    test2 = is_prime(15)
    print(f"Test 2 - is_prime(15): {test2} (Expected: False)")
    
    # Test case 3: Edge case (less than 2)
    test3 = is_prime(1)
    print(f"Test 3 - is_prime(1): {test3} (Expected: False)")
    
    # Test case 4: Even prime
    test4 = is_prime(2)
    print(f"Test 4 - is_prime(2): {test4} (Expected: True)")
    
    # Test case 5: Larger prime
    test5 = is_prime(97)
    print(f"Test 5 - is_prime(97): {test5} (Expected: True)")

"""
Time Complexity: O(√n) - We iterate up to the square root of n.
Space Complexity: O(1) - We use a constant amount of extra space.
"""