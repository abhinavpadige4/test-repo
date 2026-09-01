"""
Exercise 9: Search in Rotated Sorted Array
==========================================

Problem Statement:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4

Approach:
Use modified binary search:
1. At each step, at least one half of the array is sorted
2. Check if target lies in the sorted half
3. If yes, search that half; otherwise, search the other half

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search_rotated_array(nums, target):
    """
    Search for target in a rotated sorted array.
    
    Args:
        nums (List[int]): Rotated sorted array
        target (int): Target value to search for
        
    Returns:
        int: Index of target if found, otherwise -1
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
            # Check if target is in left sorted half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            # Check if target is in right sorted half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Test cases
def test_search_rotated_array():
    # Test case 1: Target exists
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    expected1 = 4
    result1 = search_rotated_array(nums1, target1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Target doesn't exist
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    expected2 = -1
    result2 = search_rotated_array(nums2, target2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Single element array, target doesn't exist
    nums3 = [1]
    target3 = 0
    expected3 = -1
    result3 = search_rotated_array(nums3, target3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_search_rotated_array()