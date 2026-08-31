"""
Problem Statement:
    Write a function that checks if a given string is a palindrome.
    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
    Ignore spaces, punctuation, and capitalization.

Solution:
    We will clean the string by removing non-alphanumeric characters and converting to lowercase.
    Then compare the cleaned string with its reverse.

Test Cases:
    Test Case 1:
        Input: "A man, a plan, a canal: Panama"
        Expected Output: True

    Test Case 2:
        Input: "racecar"
        Expected Output: True

    Test Case 3:
        Input: "hello"
        Expected Output: False

Expected Output:
    For the test cases above, the function should return:
        True
        True
        False

Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(n) for the cleaned string.
"""

import re

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring non-alphanumeric characters and case.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("racecar", True),
        ("hello", False),
        ("", True),  # Empty string is palindrome
        ("a", True),
    ]

    print("Running test cases for is_palindrome:")
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_palindrome(input_str)
        print(f"Test {i}: Input: \"{input_str}\" -> Output: {result}, Expected: {expected}")
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
    print("All tests passed!")