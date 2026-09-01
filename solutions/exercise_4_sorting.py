\"\"\"
Exercise 4: Merge Sort Implementation

Problem Statement:
Implement the merge sort algorithm to sort an array of integers in ascending order.

Merge Sort is a divide-and-conquer algorithm that works by:
1. Dividing the array into two halves
2. Recursively sorting each half
3. Merging the sorted halves back together

Examples:
Input: [5, 2, 3, 1]
Output: [1, 2, 3, 5]

Input: [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4
\"\"\"

def merge_sort(arr):
    \"\"\"
    Sort an array using the merge sort algorithm.
    
    Args:
        arr (List[int]): Array of integers to sort
    
    Returns:
        List[int]: Sorted array in ascending order
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    \"\"\"
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Conquer: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combine: merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    \"\"\"
    Merge two sorted arrays into one sorted array.
    
    Args:
        left (List[int]): First sorted array
        right (List[int]): Second sorted array
    
    Returns:
        List[int]: Merged sorted array
    \"\"\"
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add the smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array (if any)
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right array (if any)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

# Alternative in-place merge sort implementation
def merge_sort_inplace(arr):
    \"\"\"
    In-place merge sort implementation.
    
    Args:
        arr (List[int]): Array of integers to sort (modified in place)
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    \"\"\"
    if len(arr) <= 1:
        return arr
    
    # Create a copy to avoid modifying the original during merging
    helper = [0] * len(arr)
    _merge_sort_helper(arr, helper, 0, len(arr) - 1)
    return arr

def _merge_sort_helper(arr, helper, low, high):
    \"\"\"Helper function for in-place merge sort.\"\"\"
    if low < high:
        mid = (low + high) // 2
        _merge_sort_helper(arr, helper, low, mid)
        _merge_sort_helper(arr, helper, mid + 1, high)
        _merge(arr, helper, low, mid, high)

def _merge(arr, helper, low, mid, high):
    \"\"\"Merge function for in-place merge sort.\"\"\"
    # Copy both halves to helper array
    for i in range(low, high + 1):
        helper[i] = arr[i]
    
    # Initialize pointers for left and right halves
    helper_left = low
    helper_right = mid + 1
    current = low
    
    # Iterate through helper array and copy the smallest element
    # from either left or right side back to original array
    while helper_left <= mid and helper_right <= high:
        if helper[helper_left] <= helper[helper_right]:
            arr[current] = helper[helper_left]
            helper_left += 1
        else:
            arr[current] = helper[helper_right]
            helper_right += 1
        current += 1
    
    # Copy remaining elements from left side (if any)
    remaining = mid - helper_left + 1
    for i in range(remaining):
        arr[current + i] = helper[helper_left + i]

# Test cases
if __name__ == \"__main__\": 
    # Test case 1
    arr1 = [5, 2, 3, 1]
    sorted_arr1 = merge_sort(arr1.copy())
    print(f\"Test 1: Original = {arr1}\")
    print(f\"Expected: [1, 2, 3, 5], Got: {sorted_arr1}\")
    assert sorted_arr1 == [1, 2, 3, 5]
    
    # Test case 2
    arr2 = [5, 1, 1, 2, 0, 0]
    sorted_arr2 = merge_sort(arr2.copy())
    print(f\"\\nTest 2: Original = {arr2}\")
    print(f\"Expected: [0, 0, 1, 1, 2, 5], Got: {sorted_arr2}\")
    assert sorted_arr2 == [0, 0, 1, 1, 2, 5]
    
    # Test case 3
    arr3 = [1]
    sorted_arr3 = merge_sort(arr3.copy())
    print(f\"\\nTest 3: Original = {arr3}\")
    print(f\"Expected: [1], Got: {sorted_arr3}\")
    assert sorted_arr3 == [1]
    
    # Test case 4
    arr4 = []
    sorted_arr4 = merge_sort(arr4.copy())
    print(f\"\\nTest 4: Original = {arr4}\")
    print(f\"Expected: [], Got: {sorted_arr4}\")
    assert sorted_arr4 == []
    
    # Test in-place version
    arr5 = [9, 9, 3, 2, 1, 5]
    original_arr5 = arr5.copy()
    merge_sort_inplace(arr5)
    print(f\"\\nIn-place Test: Original = {original_arr5}\")
    print(f\"Sorted in-place: {arr5}\")
    assert arr5 == [1, 2, 3, 5, 9, 9]
    
    print(\"\\nAll tests passed!\")