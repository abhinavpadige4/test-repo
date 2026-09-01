\"\"\"
Exercise 10: Maximum Subarray
Topic: Dynamic Programming
Difficulty: Medium

Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Solution:
\"\"\"
def max_subarray(nums):
    """
    Find the contiguous subarray with the largest sum.
    
    Args:
        nums (List[int]): List of integers (can be negative)
    
    Returns:
        int: The maximum sum of a contiguous subarray
    """
    if not nums:
        return 0
    
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Test cases
if __name__ == "__main__":
    # Test Case 1: Mixed positive and negative
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Test Case 1: max_subarray({nums1}) = {max_subarray(nums1)}")  # Expected: 6
    
    # Test Case 2: All positive
    nums2 = [1, 2, 3, 4, 5]
    print(f"Test Case 2: max_subarray({nums2}) = {max_subarray(nums2)}")  # Expected: 15
    
    # Test Case 3: All negative
    nums3 = [-2, -3, -1, -5]
    print(f"Test Case 3: max_subarray({nums3}) = {max_subarray(nums3)}")  # Expected: -1
    
    # Test Case 4: Single element
    nums4 = [5]
    print(f"Test Case 4: max_subarray({nums4}) = {max_subarray(nums4)}")  # Expected: 5

# Complexity Analysis:
# Time Complexity: O(n) - where n is the length of the array
# Space Complexity: O(1) - constant extra space