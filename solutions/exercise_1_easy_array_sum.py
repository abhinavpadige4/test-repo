"""
Problem: Given an array of integers, return the sum of all elements.
Solution: Use the built-in sum function or iterate.
"""

def array_sum(arr):
    """
    Calculate the sum of an array of integers.
    Args:
        arr: List[int]
    Returns:
        int: sum of elements
    """
    return sum(arr)

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 10),
        ([], 0),
        ([-1, 1], 0)
    ]
    for arr, expected in test_cases:
        result = array_sum(arr)
        assert result == expected, f"Failed for {arr}: expected {expected}, got {result}"
    print("All tests passed!")

# Complexity: Time O(n), Space O(1)