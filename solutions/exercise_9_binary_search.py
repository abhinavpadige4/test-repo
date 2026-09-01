\"\"\"
Exercise 9: Binary Search
Topic: Searching Algorithms
Difficulty: Medium

Problem Statement:
Implement a binary search algorithm to find the index of a target value in a sorted list.
If the target is not found, return -1.

Solution:
\"\"\"
def binary_search(arr, target):
    """
    Perform binary search on a sorted list.
    
    Args:
        arr: Sorted list of elements
        target: Value to search for
        
    Returns:
        Index of target if found, otherwise -1
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

def main():
    # Test the function
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    test_cases = [
        (sorted_list, 7, 3),
        (sorted_list, 1, 0),
        (sorted_list, 19, 9),
        (sorted_list, 4, -1),
        (sorted_list, 20, -1)
    ]
    
    for arr, target, expected in test_cases:
        result = binary_search(arr, target)
        print(f"binary_search({arr}, {target}) = {result} (expected {expected})")
        assert result == expected, f"Failed for target {target}"

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Target in middle
    assert binary_search([1, 3, 5, 7, 9, 11], 7) == 3, "Test 1 failed"
    print("Test Case 1 Passed: Target in middle")
    
    # Test Case 2: Target at beginning
    assert binary_search([1, 3, 5, 7, 9, 11], 1) == 0, "Test 2 failed"
    print("Test Case 2 Passed: Target at beginning")
    
    # Test Case 3: Target at end
    assert binary_search([1, 3, 5, 7, 9, 11], 11) == 5, "Test 3 failed"
    print("Test Case 3 Passed: Target at end")
    
    # Test Case 4: Target not present
    assert binary_search([1, 3, 5, 7, 9, 11], 4) == -1, "Test 4 failed"
    print("Test Case 4 Passed: Target not present")
    
    # Test Case 5: Empty list
    assert binary_search([], 5) == -1, "Test 5 failed"
    print("Test Case 5 Passed: Empty list")
    
    # Test Case 6: Single element, match
    assert binary_search([5], 5) == 0, "Test 6 failed"
    print("Test Case 6 Passed: Single element match")
    
    # Test Case 7: Single element, no match
    assert binary_search([5], 3) == -1, "Test 7 failed"
    print("Test Case 7 Passed: Single element no match")
    
    print("\\nAll tests passed!")