\"\"\"
Exercise 8: Merge Sort
Topic: Sorting Algorithms
Difficulty: Medium

Problem Statement:
Implement the merge sort algorithm to sort a list of integers in ascending order.

Solution:
\"\"\"

def merge_sort(arr):
    """
    Sorts a list using merge sort algorithm.
    
    Args:
        arr (list): List of integers
    
    Returns:
        list: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    
    Args:
        left (list): Sorted list
        right (list): Sorted list
    
    Returns:
        list: Merged sorted list
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test Cases
def test_merge_sort():
    assert merge_sort([5, 2, 8, 3, 1, 6]) == [1, 2, 3, 5, 6, 8]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([3, 3, 3]) == [3, 3, 3]
    assert merge_sort([5, -1, 3, 2]) == [-1, 2, 3, 5]
    print("All tests passed!")

if __name__ == "__main__":
    test_merge_sort()

# Complexity Analysis:
# Time Complexity: O(n log n) - splits and merges
# Space Complexity: O(n) - temporary arrays during merge