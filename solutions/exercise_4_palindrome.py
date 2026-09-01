\"\"\"
Exercise 4: Palindrome Check
Topic: Strings
Difficulty: Easy

Problem Statement:
Write a Python function that checks if a given string is a palindrome (reads the same forwards and backwards), ignoring spaces, punctuation, and capitalization.

Solution:
\"\"\"
import re

def is_palindrome(s):
    """
    Return True if s is a palindrome, False otherwise.
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if s is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

# Test cases
if __name__ == "__main__":
    # Test Case 1: Simple palindrome
    print(f"Test Case 1: is_palindrome('racecar') = {is_palindrome('racecar')}")  # Expected: True
    
    # Test Case 2: With punctuation and spaces
    print(f"Test Case 2: is_palindrome('A man, a plan, a canal: Panama') = {is_palindrome('A man, a plan, a canal: Panama')}")  # Expected: True
    
    # Test Case 3: Not a palindrome
    print(f"Test Case 3: is_palindrome('hello') = {is_palindrome('hello')}")  # Expected: False
    
    # Test Case 4: Empty string
    print(f"Test Case 4: is_palindrome('') = {is_palindrome('')}")  # Expected: True

# Complexity Analysis:
# Time Complexity: O(n) - where n is the length of the string (cleaning and reversing)
# Space Complexity: O(n) - for the cleaned string