"""
Exercise 10: Longest Substring Without Repeating Characters
============================================================

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Approach:
Use sliding window technique with a hash set:
1. Maintain a window [left, right] with no repeating characters
2. Expand window by moving right pointer
3. If character is repeated, shrink window from left until no repetition
4. Track maximum window size

Time Complexity: O(n)
Space Complexity: O(min(m,n)) where m is charset size
"""

def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.
    
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
    
    # Expand window by moving right pointer
    for right in range(len(s)):
        # If character is repeated, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
def test_length_of_longest_substring():
    # Test case 1: Normal case with repetitions
    s1 = "abcabcbb"
    expected1 = 3
    result1 = length_of_longest_substring(s1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: All same characters
    s2 = "bbbbb"
    expected2 = 1
    result2 = length_of_longest_substring(s2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: No repeating characters
    s3 = "pwwkew"
    expected3 = 3
    result3 = length_of_longest_substring(s3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_longest_substring()