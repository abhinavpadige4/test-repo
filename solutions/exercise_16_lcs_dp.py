\"\"\"
Exercise 16: Longest Common Subsequence (Dynamic Programming)
Topic: Dynamic Programming
Difficulty: Hard

Problem Statement:
Given two strings, find the length of their longest common subsequence (LCS).
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

Solution:
\"\"\"
def longest_common_subsequence(text1, text2):
    """
    Compute the length of the longest common subsequence of two strings.
    
    Args:
        text1: First string
        text2: Second string
        
    Returns:
        Length of LCS
    """
    m, n = len(text1), len(text2)
    # Create a DP table of size (m+1) x (n+1) initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def main():
    # Example usage
    examples = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("AGGTAB", "GXTXAYB")
    ]
    for s1, s2 in examples:
        lcs_length = longest_common_subsequence(s1, s2)
        print(f"LCS of '{s1}' and '{s2}' is {lcs_length}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    assert longest_common_subsequence("abcde", "ace") == 3, "Test 1 failed"
    print("Test Case 1 Passed: 'abcde' & 'ace' -> 3")
    
    # Test Case 2: Identical strings
    assert longest_common_subsequence("abc", "abc") == 3, "Test 2 failed"
    print("Test Case 2 Passed: 'abc' & 'abc' -> 3")
    
    # Test Case 3: No common subsequence
    assert longest_common_subsequence("abc", "def") == 0, "Test 3 failed"
    print("Test Case 3 Passed: 'abc' & 'def' -> 0")
    
    # Test Case 4: Longer example
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == 4, "Test 4 failed"
    print("Test Case 4 Passed: 'AGGTAB' & 'GXTXAYB' -> 4")
    
    # Test Case 5: Empty string
    assert longest_common_subsequence("", "abc") == 0, "Test 5 failed"
    assert longest_common_subsequence("abc", "") == 0, "Test 5 failed"
    print("Test Case 5 Passed: Empty string")
    
    # Test Case 6: Single character
    assert longest_common_subsequence("a", "a") == 1, "Test 6 failed"
    assert longest_common_subsequence("a", "b") == 0, "Test 6 failed"
    print("Test Case 6 Passed: Single character")
    
    print("\\nAll tests passed!")