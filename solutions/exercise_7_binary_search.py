\"\"\"
Exercise 7: Binary Search
Topic: Searching Algorithms
Difficulty: Medium

Problem Statement:
Implement a binary search algorithm that returns the index of a target value in a sorted list. If the target is not found, return -1.

Solution:
\"\"\"

def binary_search(arr, target):
    """
    Performs binary search on a sorted list.
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
    
    Returns:
        int: Index of target if found, otherwise -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test Cases
def test_binary_search():
    # Test with odd length
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    # Test with even length
    assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
    # Test target not present
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    # Test target at beginning
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    # Test target at end
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    # Test empty list
    assert binary_search([], 1) == -1
    print("All tests passed!")

if __name__ == "__main__":
    test_binary_search()

# Complexity Analysis:
# Time Complexity: O(log n) - halves the search space each iteration
# Space Complexity: O(1) - constant extra space