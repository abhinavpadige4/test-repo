"""
Problem: Given a string, return the reversed version of it.
Solution: Use slicing or two-pointer approach.
"""

def reverse_string(s):
    """
    Reverse a given string.
    Args:
        s: str
    Returns:
        str: reversed string
    """
    return s[::-1]

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
        ("NeuroVerse", "esrevoruN")
    ]
    for s, expected in test_cases:
        result = reverse_string(s)
        assert result == expected, f"Failed for '{s}': expected '{expected}', got '{result}'"
    print("All tests passed!")

# Complexity: Time O(n), Space O(n)