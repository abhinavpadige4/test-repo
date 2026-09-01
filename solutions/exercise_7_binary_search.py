\"\"\"
Exercise 7: Binary Search
Topic: Search Algorithms
Difficulty: Medium

Problem Statement:
Implement binary search on a sorted list. Return the index of the target if found, otherwise return -1.

Solution:
\"\"\"
def binary_search(arr, target):
    """
    Perform binary search on a sorted list.
    
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

# Test cases
if __name__ == "__main__":
    # Test Case 1: Target in middle
    arr1 = [1, 3, 5, 7, 9, 11]
    print(f"Test Case 1: binary_search({arr1}, 7) = {binary_search(arr1, 7)}")  # Expected: 3
    
    # Test Case 2: Target at beginning
    print(f"Test Case 2: binary_search({arr1}, 1) = {binary_search(arr1, 1)}")  # Expected: 0
    
    # Test Case 3: Target at end
    print(f"Test Case 3: binary_search({arr1}, 11) = {binary_search(arr1, 11)}")  # Expected: 5
    
    # Test Case 4: Target not present
    print(f"Test Case 4: binary_search({arr1}, 4) = {binary_search(arr1, 4)}")  # Expected: -1
    
    # Test Case 5: Empty list
    print(f"Test Case 5: binary_search([], 5) = {binary_search([], 5)}")  # Expected: -1

# Complexity Analysis:
# Time Complexity: O(log n) - where n is the number of elements in the list
# Space Complexity: O(1) - constant extra space