"""
Exercise 7: Longest Substring Without Repeating Characters (Medium)
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
"""

def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters using sliding window technique.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of the longest substring without repeating characters
        
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(min(m,n)) where m is the size of the charset
    """
    # Dictionary to store the last index of each character
    char_index_map = {}
    
    # Left pointer of the sliding window
    left = 0
    
    # Maximum length found so far
    max_length = 0
    
    # Right pointer moves through the string
    for right in range(len(s)):
        # If character is already in current window, move left pointer
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        
        # Update the last seen index of current character
        char_index_map[s[right]] = right
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Alternative approach using set
def length_of_longest_substring_set(s):
    """
    Alternative implementation using a set to track characters in current window.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of the longest substring without repeating characters
        
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(min(m,n)) where m is the size of the charset
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character is already in set, shrink window from left
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
    # Test Case 1
    s1 = "abcabcbb"
    result1 = length_of_longest_substring(s1)
    print(f"Test 1 - Input: '{s1}'")
    print(f"Output: {result1}")
    print(f"Expected: 3")
    print(f"Pass: {result1 == 3}\\n")
    
    # Test Case 2
    s2 = "bbbbb"
    result2 = length_of_longest_substring(s2)
    print(f"Test 2 - Input: '{s2}'")
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print(f"Pass: {result2 == 1}\\n")
    
    # Test Case 3
    s3 = "pwwkew"
    result3 = length_of_longest_substring(s3)
    print(f"Test 3 - Input: '{s3}'")
    print(f"Output: {result3}")
    print(f"Expected: 3")
    print(f"Pass: {result3 == 3}\\n")
    
    # Test Case 4
    s4 = ""
    result4 = length_of_longest_substring(s4)
    print(f"Test 4 - Input: '{s4}'")
    print(f"Output: {result4}")
    print(f"Expected: 0")
    print(f"Pass: {result4 == 0}\\n")
    
    # Test Case 5
    s5 = "abcdef"
    result5 = length_of_longest_substring(s5)
    print(f"Test 5 - Input: '{s5}'")
    print(f"Output: {result5}")
    print(f"Expected: 6")
    print(f"Pass: {result5 == 6}\\n")