\"\"\"
Exercise 10: Merge Sort
Topic: Sorting Algorithms
Difficulty: Medium

Problem Statement:
Implement the merge sort algorithm to sort a list of integers in ascending order.

Solution:
\"\"\"
def merge_sort(arr):
    """
    Sort a list using the merge sort algorithm.
    
    Args:
        arr: List of integers
        
    Returns:
        A new sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def main():
    # Test the function
    test_cases = [
        [5, 2, 8, 3, 9, 1],
        [1],
        [],
        [3, 3, 3],
        [10, -1, 2, 5, 0]
    ]
    
    for arr in test_cases:
        sorted_arr = merge_sort(arr)
        print(f"Original: {arr}")
        print(f"Sorted:   {sorted_arr}")
        # Verify it's sorted
        assert sorted_arr == sorted(arr), f"Merge sort failed on {arr}"
        print("Verified: Correctly sorted\\n")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Random order
    assert merge_sort([5, 2, 8, 3, 9, 1]) == [1, 2, 3, 5, 8, 9], "Test 1 failed"
    print("Test Case 1 Passed: [5,2,8,3,9,1] -> [1,2,3,5,8,9]")
    
    # Test Case 2: Single element
    assert merge_sort([42]) == [42], "Test 2 failed"
    print("Test Case 2 Passed: [42] -> [42]")
    
    # Test Case 3: Empty list
    assert merge_sort([]) == [], "Test 3 failed"
    print("Test Case 3 Passed: [] -> []")
    
    # Test Case 4: Duplicates
    assert merge_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3], "Test 4 failed"
    print("Test Case 4 Passed: [3,1,2,3,1] -> [1,1,2,3,3]")
    
    # Test Case 5: Negative numbers
    assert merge_sort([10, -1, 2, 5, 0]) == [-1, 0, 2, 5, 10], "Test 5 failed"
    print("Test Case 5 Passed: [10,-1,2,5,0] -> [-1,0,2,5,10]")
    
    print("\\nAll tests passed!")