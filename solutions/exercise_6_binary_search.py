"""
Exercise 6: Binary Search
Topic: Search Algorithms
Difficulty: Medium

Problem Statement:
Implement a binary search algorithm. Given a sorted list of integers and a target value, 
return the index of the target if found, otherwise return -1.

Solution:
Binary search works by repeatedly dividing the search interval in half. 
Compare the target with the middle element; if they are not equal, 
eliminate the half in which the target cannot lie and continue on the remaining half.
"""

def binary_search(arr, target):
    """
    Perform binary search on a sorted list.
    
    Args:
        arr (list): A sorted list of integers
        target (int): The value to search for
        
    Returns:
        int: The index of target in arr if found, otherwise -1
        
    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
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
    # Test case 1: Target in the middle
    test1 = binary_search([1, 2, 3, 4, 5], 3)
    print(f"Test 1 - binary_search([1,2,3,4,5], 3): {test1} (Expected: 2)")
    
    # Test case 2: Target at the beginning
    test2 = binary_search([1, 2, 3, 4, 5], 1)
    print(f"Test 2 - binary_search([1,2,3,4,5], 1): {test2} (Expected: 0)")
    
    # Test case 3: Target at the end
    test3 = binary_search([1, 2, 3, 4, 5], 5)
    print(f"Test 3 - binary_search([1,2,3,4,5], 5): {test3} (Expected: 4)")
    
    # Test case 4: Target not in list
    test4 = binary_search([1, 2, 3, 4, 5], 6)
    print(f"Test 4 - binary_search([1,2,3,4,5], 6): {test4} (Expected: -1)")
    
    # Test case 5: Empty list
    test5 = binary_search([], 5)
    print(f"Test 5 - binary_search([], 5): {test5} (Expected: -1)")
    
    # Test case 6: List with duplicates (returns any index)
    test6 = binary_search([1, 2, 2, 2, 3], 2)
    print(f"Test 6 - binary_search([1,2,2,2,3], 2): {test6} (Expected: 1, 2, or 3)")

"""
Time Complexity: O(log n) - We halve the search space each iteration.
Space Complexity: O(1) - We use a constant amount of extra space.
"""