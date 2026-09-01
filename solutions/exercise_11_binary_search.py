"""
Exercise 11: Search in Rotated Sorted Array
===========================================

Problem Statement:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k.
Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Approach:
Modified binary search:
1. At each step, one half of array is always sorted
2. Check if target lies in sorted half
3. If yes, search in that half; otherwise search in other half
4. Continue until target found or search space exhausted

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search_rotated_array(nums, target):
    """
    Search for target in rotated sorted array.
    
    Args:
        nums (List[int]): Rotated sorted array
        target (int): Element to search for
        
    Returns:
        int: Index of target if found, -1 otherwise
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Check if target lies in left sorted half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            # Check if target lies in right sorted half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Target exists
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = search_rotated_array(nums1, target1)
    print(f"Test 1: {nums1}, target={target1} -> index {result1}")  # Expected: 4
    
    # Test Case 2: Target doesn't exist
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = search_rotated_array(nums2, target2)
    print(f"Test 2: {nums2}, target={target2} -> index {result2}")  # Expected: -1
    
    # Test Case 3: Not rotated array
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    target3 = 5
    result3 = search_rotated_array(nums3, target3)
    print(f"Test 3: {nums3}, target={target3} -> index {result3}")  # Expected: 4