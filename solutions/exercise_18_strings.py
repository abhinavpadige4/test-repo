"""
Exercise 18: Longest Common Prefix
===================================

Problem Statement:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Examples:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

Approach:
Vertical scanning approach:
1. Find the minimum length among all strings
2. Compare characters at each position across all strings
3. Stop when mismatch is found or we reach the end of shortest string

Time Complexity: O(S) where S is the sum of all characters in all strings
Space Complexity: O(1)
"""

def longest_common_prefix(strs):
    """
    Find the longest common prefix among an array of strings.
    
    Args:
        strs (List[str]): Array of strings
        
    Returns:
        str: Longest common prefix string
    """
    if not strs:
        return ""
    
    # Find the minimum length among all strings
    min_length = min(len(s) for s in strs)
    
    # Compare characters at each position
    for i in range(min_length):
        char = strs[0][i]  # Character to match at position i
        
        # Check if all strings have the same character at position i
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return strs[0][:i]  # Return prefix up to position i
    
    # If we've checked all positions up to min_length, 
    # the common prefix is the entire shortest string
    return strs[0][:min_length]

# Alternative approach: Horizontal scanning
def longest_common_prefix_horizontal(strs):
    """
    Find the longest common prefix using horizontal scanning.
    
    Args:
        strs (List[str]): Array of strings
        
    Returns:
        str: Longest common prefix string
    """
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        # Reduce prefix until it matches the beginning of current string
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test cases
def test_longest_common_prefix():
    # Test case 1: Normal case with common prefix
    strs1 = ["flower", "flow", "flight"]
    expected1 = "fl"
    result1 = longest_common_prefix(strs1)
    assert result1 == expected1, f"Test 1 failed: expected '{expected1}', got '{result1}'"
    
    # Test case 2: No common prefix
    strs2 = ["dog", "racecar", "car"]
    expected2 = ""
    result2 = longest_common_prefix(strs2)
    assert result2 == expected2, f"Test 2 failed: expected '{expected2}', got '{result2}'"
    
    # Test case 3: Single string
    strs3 = ["single"]
    expected3 = "single"
    result3 = longest_common_prefix(strs3)
    assert result3 == expected3, f"Test 3 failed: expected '{expected3}', got '{result3}'"
    
    # Test case 4: Empty array
    strs4 = []
    expected4 = ""
    result4 = longest_common_prefix(strs4)
    assert result4 == expected4, f"Test 4 failed: expected '{expected4}', got '{result4}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_common_prefix()