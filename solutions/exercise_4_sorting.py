"""
Exercise 4: Merge Sort Implementation
=====================================

Problem Statement:
Implement the merge sort algorithm to sort an array of integers in ascending order.

Examples:
Input: [5,2,3,1]
Output: [1,2,3,5]

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4

Approach:
Merge Sort is a divide-and-conquer algorithm:
1. Divide the array into two halves
2. Recursively sort both halves
3. Merge the sorted halves

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge_sort(nums):
    """
    Sort an array using merge sort algorithm.
    
    Args:
        nums (List[int]): Array of integers to sort
        
    Returns:
        List[int]: Sorted array in ascending order
    """
    if len(nums) <= 1:
        return nums
    
    # Divide
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left (List[int]): Left sorted array
        right (List[int]): Right sorted array
        
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
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Test cases
def test_merge_sort():
    # Test case 1: Normal array
    nums1 = [5, 2, 3, 1]
    expected1 = [1, 2, 3, 5]
    result1 = merge_sort(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Array with duplicates
    nums2 = [5, 1, 1, 2, 0, 0]
    expected2 = [0, 0, 1, 1, 2, 5]
    result2 = merge_sort(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Already sorted array
    nums3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    result3 = merge_sort(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_merge_sort()