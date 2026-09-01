"""
Exercise 16: Palindrome Number
==============================

Problem Statement:
Given an integer x, return true if x is a palindrome, and false otherwise.

Examples:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left.

Constraints:
- -2^31 <= x <= 2^31 - 1

Approach:
Without converting to string:
1. Negative numbers are not palindromes
2. Numbers ending in 0 (except 0 itself) are not palindromes
3. Reverse half of the number and compare with the other half
4. Stop when reversed number >= original number

Time Complexity: O(log n) where n is the value of input number
Space Complexity: O(1)
"""

def is_palindrome(x):
    """
    Check if an integer is a palindrome.
    
    Args:
        x (int): Integer to check
        
    Returns:
        bool: True if x is a palindrome, False otherwise
    """
    # Negative numbers and numbers ending in 0 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    original = x
    
    # Reverse half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # For even digit numbers, x should equal reversed_half
    # For odd digit numbers, we need to remove the middle digit from reversed_half
    return x == reversed_half or x == reversed_half // 10

# Optimized approach - convert to string
def is_palindrome_string(x):
    """
    Check if an integer is a palindrome by converting to string.
    
    Args:
        x (int): Integer to check
        
    Returns:
        bool: True if x is a palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Convert to string and check if it reads the same forwards and backwards
    str_x = str(x)
    return str_x == str_x[::-1]

# Test cases
def test_is_palindrome():
    # Test case 1: Palindrome number
    x1 = 121
    expected1 = True
    result1 = is_palindrome(x1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Negative number
    x2 = -121
    expected2 = False
    result2 = is_palindrome(x2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Number ending in 0
    x3 = 10
    expected3 = False
    result3 = is_palindrome(x3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    # Test case 4: Single digit
    x4 = 5
    expected4 = True
    result4 = is_palindrome(x4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_is_palindrome()