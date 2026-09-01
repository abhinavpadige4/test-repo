"""
Exercise 1: Two Sum Problem (Easy)
Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Each input would have exactly one solution, and you may not use the same element twice.

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
    
    # This should never happen according to problem constraints
    return []

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Test 1 - Input: {nums1}, Target: {target1}")
    print(f"Output: {result1}")
    print(f"Expected: [0, 1]")
    print(f"Pass: {result1 == [0, 1]}\\n")
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Test 2 - Input: {nums2}, Target: {target2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 2]")
    print(f"Pass: {result2 == [1, 2]}\\n")
    
    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Test 3 - Input: {nums3}, Target: {target3}")
    print(f"Output: {result3}")
    print(f"Expected: [0, 1]")
    print(f"Pass: {result3 == [0, 1]}\\n")