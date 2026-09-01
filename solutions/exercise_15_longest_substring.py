\"\"\"
Exercise 15: Longest Substring Without Repeating Characters
Topic: Sliding Window / Hash Table
Difficulty: Medium

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Solution:
\"\"\"
def length_of_longest_substring(s):
    """
    Return the length of the longest substring without repeating characters.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of the longest substring without repeating characters
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Test Case 1: Basic
    print(f"Test Case 1: length_of_longest_substring('abcabcbb') = {length_of_longest_substring('abcabcbb')}")  # Expected: 3
    
    # Test Case 2: All same
    print(f"Test Case 2: length_of_longest_substring('bbbbb') = {length_of_longest_substring('bbbbb')}")  # Expected: 1
    
    # Test Case 3: No repeats
    print(f"Test Case 3: length_of_longest_substring('pwwkew') = {length_of_longest_substring('pwwkew')}")  # Expected: 3
    
    # Test Case 4: Empty string
    print(f"Test Case 4: length_of_longest_substring('') = {length_of_longest_substring('')}")  # Expected: 0

# Complexity Analysis:
# Time Complexity: O(n) - where n is the length of the string
# Space Complexity: O(min(m, n)) - where m is the size of the charset (e.g., ASCII)