"""
Exercise 5: Move Zeroes (Easy)
Problem Statement:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Examples:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?
"""

def move_zeroes(nums):
    """
    Move all zeroes to the end of the array while maintaining the relative order of non-zero elements.
    
    Args:
        nums (List[int]): Array of integers
    
    Returns:
        None: Modifies the input list in-place
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Position pointer for non-zero elements
    pos = 0
    
    # First pass: move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    
    # Second pass: fill the rest with zeros
    while pos < len(nums):
        nums[pos] = 0
        pos += 1

# Alternative single-pass solution
def move_zeroes_optimized(nums):
    """
    Optimized version that minimizes the number of operations.
    
    Args:
        nums (List[int]): Array of integers
    
    Returns:
        None: Modifies the input list in-place
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Position pointer for non-zero elements
    pos = 0
    
    # Single pass: swap non-zero elements to their correct positions
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    print(f"Test 1 - Input: {nums1}")
    move_zeroes(nums1)
    print(f"Output: {nums1}")
    print(f"Expected: {expected1}")
    print(f"Pass: {nums1 == expected1}\\n")
    
    # Test Case 2
    nums2 = [0]
    expected2 = [0]
    print(f"Test 2 - Input: {nums2}")
    move_zeroes(nums2)
    print(f"Output: {nums2}")
    print(f"Expected: {expected2}")
    print(f"Pass: {nums2 == expected2}\\n")
    
    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    print(f"Test 3 - Input: {nums3}")
    move_zeroes(nums3)
    print(f"Output: {nums3}")
    print(f"Expected: {expected3}")
    print(f"Pass: {nums3 == expected3}\\n")
    
    # Test optimized version
    nums4 = [0, 1, 0, 3, 12]
    expected4 = [1, 3, 12, 0, 0]
    print(f"Optimized Test - Input: {nums4}")
    move_zeroes_optimized(nums4)
    print(f"Output: {nums4}")
    print(f"Expected: {expected4}")
    print(f"Pass: {nums4 == expected4}\\n")