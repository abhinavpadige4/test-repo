"""
Exercise 10: Longest Substring Without Repeating Characters
==========================================================

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Approach:
Use sliding window technique with two pointers:
1. Use a set to track characters in current window
2. Expand window by moving right pointer
3. If duplicate character found, shrink window from left until no duplicate
4. Track maximum window size throughout process

Time Complexity: O(n) - each character visited at most twice
Space Complexity: O(min(m,n)) where m is charset size
"""

def length_of_longest_substring(s):
    """
    Find length of longest substring without repeating characters.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of longest substring without repeating characters
    """
    if not s:
        return 0
    
    char_set = set()
    left = 0
    max_length = 0
    
    # Right pointer expands window
    for right in range(len(s)):
        # If duplicate found, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case
    s1 = "abcabcbb"
    result1 = length_of_longest_substring(s1)
    print(f"Test 1: '{s1}' -> {result1}")  # Expected: 3 ("abc")
    
    # Test Case 2: All same characters
    s2 = "bbbbb"
    result2 = length_of_longest_substring(s2)
    print(f"Test 2: '{s2}' -> {result2}")  # Expected: 1 ("b")
    
    # Test Case 3: No repeating characters
    s3 = "pwwkew"
    result3 = length_of_longest_substring(s3)
    print(f"Test 3: '{s3}' -> {result3}")  # Expected: 3 ("wke")