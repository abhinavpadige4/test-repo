"""
Exercise 4: Find Maximum Element in a List
Topic: List Operations & Iteration
Difficulty: Easy

Problem Statement:
Write a function that takes a list of integers and returns the maximum element.
Do not use Python's built-in max() function.

Solution:
Iterate through the list, keeping track of the largest element seen so far.
Handle edge case of empty list by returning None or raising an exception.
"""

def find_max(lst):
    """
    Find the maximum element in a list without using max().
    
    Args:
        lst (list): A list of comparable elements (e.g., integers)
        
    Returns:
        The maximum element, or None if the list is empty
        
    Examples:
        >>> find_max([3, 1, 4, 1, 5, 9, 2])
        9
        >>> find_max([-5, -2, -10])
        -2
    """
    if not lst:  # Empty list
        return None
    
    max_element = lst[0]
    for element in lst[1:]:
        if element > max_element:
            max_element = element
    return max_element

# Test cases
if __name__ == "__main__":
    # Test case 1: Normal list with positive numbers
    test1 = find_max([3, 1, 4, 1, 5, 9, 2])
    print(f"Test 1 - find_max([3, 1, 4, 1, 5, 9, 2]): {test1} (Expected: 9)")
    
    # Test case 2: List with negative numbers
    test2 = find_max([-5, -2, -10, -1])
    print(f"Test 2 - find_max([-5, -2, -10, -1]): {test2} (Expected: -1)")
    
    # Test case 3: Single element list
    test3 = find_max([42])
    print(f"Test 3 - find_max([42]): {test3} (Expected: 42)")
    
    # Test case 4: Empty list
    test4 = find_max([])
    print(f"Test 4 - find_max([]): {test4} (Expected: None)")
    
    # Test case 5: List with duplicates
    test5 = find_max([7, 7, 7, 7])
    print(f"Test 5 - find_max([7, 7, 7, 7]): {test5} (Expected: 7)")

"""
Time Complexity: O(n) - We iterate through the list once.
Space Complexity: O(1) - We use a constant amount of extra space.
"""