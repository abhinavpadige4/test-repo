"""
Exercise 5: Group Anagrams

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

def group_anagrams(strs):
    """
    Group anagrams together using character count as the key.
    
    Approach:
    1. For each string, calculate the frequency of each character
    2. Use this frequency tuple as a key in a hash map
    3. Group all strings with the same character frequency
    
    Args:
        strs (List[str]): List of strings to group
    
    Returns:
        List[List[str]]: Groups of anagrams
    
    Time Complexity: O(N * K) where N is number of strings and K is max length of string
    Space Complexity: O(N * K) to store all strings in hash map
    """
    anagram_groups = {}
    
    for s in strs:
        # Count frequency of each character
        char_count = [0] * 26  # For lowercase English letters
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        # Convert to tuple so it can be used as dictionary key
        key = tuple(char_count)
        
        # Add string to its anagram group
        if key in anagram_groups:
            anagram_groups[key].append(s)
        else:
            anagram_groups[key] = [s]
    
    # Return all groups
    return list(anagram_groups.values())

def group_anagrams_sorted(strs):
    """
    Group anagrams together using sorted string as the key.
    
    Alternative approach:
    1. For each string, sort its characters
    2. Use the sorted string as a key in a hash map
    3. Group all strings with the same sorted key
    
    Args:
        strs (List[str]): List of strings to group
    
    Returns:
        List[List[str]]: Groups of anagrams
    
    Time Complexity: O(N * K * log K) where N is number of strings and K is max length of string
    Space Complexity: O(N * K) to store all strings in hash map
    """
    anagram_groups = {}
    
    for s in strs:
        # Sort characters to create key
        key = ''.join(sorted(s))
        
        # Add string to its anagram group
        if key in anagram_groups:
            anagram_groups[key].append(s)
        else:
            anagram_groups[key] = [s]
    
    # Return all groups
    return list(anagram_groups.values())

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    result1 = group_anagrams(strs1)
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]  # Order may vary
    print(f"Test 1: {strs1} => {result1}")
    # Check that all anagram groups are present
    assert len(result1) == 3, f"Expected 3 groups, got {len(result1)}"
    assert set(["bat"]) in [set(group) for group in result1], "Missing 'bat' group"
    assert set(["nat","tan"]) in [set(group) for group in result1], "Missing 'nat','tan' group"
    assert set(["ate","eat","tea"]) in [set(group) for group in result1], "Missing 'ate','eat','tea' group"
    
    # Test Case 2
    strs2 = [""]
    result2 = group_anagrams(strs2)
    expected2 = [[""]]
    print(f"Test 2: {strs2} => {result2}")
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test Case 3
    strs3 = ["a"]
    result3 = group_anagrams(strs3)
    expected3 = [["a"]]
    print(f"Test 3: {strs3} => {result3}")
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("All tests passed!")