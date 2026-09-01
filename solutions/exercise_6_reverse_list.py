\"\"\"
Exercise 6: Reverse a List
Topic: Lists
Difficulty: Medium

Problem Statement:
Write a Python function that reverses a list in place (without using built-in reverse) and returns the reversed list.

Solution:
\"\"\"

def reverse_list(lst):
    """
    Reverses a list in place and returns it.
    
    Args:
        lst (list): List to be reversed
    
    Returns:
        list: The reversed list (same object)
    """
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Test Cases
def test_reverse_list():
    # Test with even length
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    # Test with odd length
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    # Test with empty list
    assert reverse_list([]) == []
    # Test with single element
    assert reverse_list([42]) == [42]
    # Test that it's in place
    original = [1, 2, 3]
    reversed_list = reverse_list(original)
    assert original is reversed_list
    print("All tests passed!")

if __name__ == "__main__":
    test_reverse_list()

# Complexity Analysis:
# Time Complexity: O(n) - we traverse half the list
# Space Complexity: O(1) - constant extra space