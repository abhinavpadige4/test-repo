\"\"\"
Exercise 4: Palindrome Check
Topic: Strings
Difficulty: Easy

Problem Statement:
Write a Python function that checks if a given string is a palindrome (reads the same forwards and backwards), ignoring case and non-alphanumeric characters.

Solution:
\"\"\"

import re

def is_palindrome(s):
    """
    Returns True if s is a palindrome, False otherwise.
    Ignores case and non-alphanumeric characters.
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', '', s).lower()
    # Alternatively, using regex to keep only alphanumeric
    cleaned = re.sub(r'[^a-z0]', '', s.lower())
    return cleaned == cleaned[::-1]

# Test Cases
def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("12321") == True
    print("All tests passed!")

if __name__ == "__main__":
    test_is_palindrome()

# Complexity Analysis:
# Time Complexity: O(n) - where n is length of string (cleaning and reversing)
# Space Complexity: O(n) - for cleaned string