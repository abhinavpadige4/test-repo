"""
Exercise 5: Palindrome Check
Topic: String Manipulation
Difficulty: Easy

Problem Statement:
Write a function that checks if a given string is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Solution:
We can clean the string (remove non-alphanumeric and convert to lower case) and then check if it equals its reverse.
"""

import re

def is_palindrome(s):
    """
    Check if a string is a palindrome, ignoring non-alphanumeric characters and case.
    
    Args:
        s (str): The string to check
        
    Returns:
        bool: True if s is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]

# Test cases
if __name__ == "__main__":
    # Test case 1: Classic palindrome with punctuation and spaces
    test1 = is_palindrome("A man, a plan, a canal: Panama")
    print(f"Test 1 - is_palindrome('A man, a plan, a canal: Panama'): {test1} (Expected: True)")
    
    # Test case 2: Simple palindrome
    test2 = is_palindrome("racecar")
    print(f"Test 2 - is_palindrome('racecar'): {test2} (Expected: True)")
    
    # Test case 3: Non-palindrome
    test3 = is_palindrome("hello")
    print(f"Test 3 - is_palindrome('hello'): {test3} (Expected: False)")
    
    # Test case 4: Empty string
    test4 = is_palindrome("")
    print(f"Test 4 - is_palindrome(''): {test4} (Expected: True)")
    
    # Test case 5: Single character
    test5 = is_palindrome("a")
    print(f"Test 5 - is_palindrome('a'): {test5} (Expected: True)")
    
    # Test case 6: Numeric palindrome
    test6 = is_palindrome("12321")
    print(f"Test 6 - is_palindrome('12321'): {test6} (Expected: True)")

"""
Time Complexity: O(n) - We traverse the string to clean it and then compare with its reverse.
Space Complexity: O(n) - We create a cleaned version of the string.
"""