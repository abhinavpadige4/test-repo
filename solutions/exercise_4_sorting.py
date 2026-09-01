"""
Exercise 4: Merge Sort Implementation

Problem Statement:
Implement the merge sort algorithm to sort an array of integers in ascending order.

Examples:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4
"""

def merge_sort(nums):
    """
    Sort an array using the merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm that divides the array into halves,
    recursively sorts each half, and then merges the sorted halves.
    
    Args:
        nums (List[int]): Array of integers to sort
    
    Returns:
        List[int]: Sorted array in ascending order
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(nums) <= 1:
        return nums
    
    # Divide: split the array into two halves
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]
    
    # Conquer: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combine: merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left (List[int]): Left sorted subarray
        right (List[int]): Right sorted subarray
    
    Returns:
        List[int]: Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add smaller one to result
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
def merge_sort_inplace(nums):
    """
    In-place merge sort implementation.
    
    Args:
        nums (List[int]): Array of integers to sort (modified in place)
    
    Returns:
        List[int]: Reference to the sorted array
    """
    if len(nums) <= 1:
        return nums
    
    def merge_sort_helper(nums, start, end):
        if start >= end:
            return
        
        mid = (start + end) // 2
        merge_sort_helper(nums, start, mid)
        merge_sort_helper(nums, mid + 1, end)
        merge_inplace(nums, start, mid, end)
    
    merge_sort_helper(nums, 0, len(nums) - 1)
    return nums

def merge_inplace(nums, start, mid, end):
    """
    Merge two sorted subarrays in-place.
    """
    # Create temporary arrays for left and right subarrays
    left = nums[start:mid+1]
    right = nums[mid+1:end+1]
    
    i = j = 0
    k = start
    
    # Merge the temporary arrays back into nums[start..end]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left[] if any
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right[] if any
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 2, 3, 1]
    original1 = nums1.copy()
    result1 = merge_sort(nums1)
    expected1 = [1, 2, 3, 5]
    print(f"Test 1: {original1} => {result1}")
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test Case 2
    nums2 = [5, 1, 1, 2, 0, 0]
    original2 = nums2.copy()
    result2 = merge_sort(nums2)
    expected2 = [0, 0, 1, 1, 2, 5]
    print(f"Test 2: {original2} => {result2}")
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test Case 3
    nums3 = [1]
    original3 = nums3.copy()
    result3 = merge_sort(nums3)
    expected3 = [1]
    print(f"Test 3: {original3} => {result3}")
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("All tests passed!")