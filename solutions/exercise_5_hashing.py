"""
Exercise 5: Two Sum Problem
===========================

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
- Only one valid answer exists.

Approach:
Use a hash map to store the value and its index as we iterate through the array.
For each element, check if (target - current_element) exists in the hash map.
If it does, we've found our pair.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    """
    Find indices of two numbers that add up to target.
    
    Args:
        nums (List[int]): Array of integers
        target (int): Target sum
        
    Returns:
        List[int]: Indices of the two numbers
    """
    # Hash map to store value -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    # This line should never be reached given the problem constraints
    return []

# Test cases
def test_two_sum():
    # Test case 1: Normal case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = two_sum(nums1, target1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Not first two elements
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = two_sum(nums2, target2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Duplicate elements
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = two_sum(nums3, target3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()