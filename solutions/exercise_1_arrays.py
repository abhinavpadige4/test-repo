"""
Exercise 1: Two Sum Problem

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""

def two_sum(nums, target):
    """
    Find two indices in the array whose values sum to the target.
    
    Args:
        nums (List[int]): Array of integers
        target (int): Target sum
    
    Returns:
        List[int]: Indices of the two numbers that sum to target
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Create a hash map to store value -> index mapping
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        # Check if complement exists in our map
        if complement in num_map:
            return [num_map[complement], i]
        # Add current number and its index to map
        num_map[num] = i
    
    # This line should never be reached given the problem constraints
    return []

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1} => {result1}")
    assert result1 == [0, 1], f"Expected [0, 1], got {result1}"
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2} => {result2}")
    assert result2 == [1, 2], f"Expected [1, 2], got {result2}"
    
    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3} => {result3}")
    assert result3 == [0, 1], f"Expected [0, 1], got {result3}"
    
    print("All tests passed!")