"""
Exercise 1: Array Rotation
==========================

Problem Statement:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

Approach:
Use the reversal algorithm for array rotation:
1. Reverse the entire array
2. Reverse the first k elements
3. Reverse the remaining elements

Time Complexity: O(n)
Space Complexity: O(1)
"""

def rotate_array(nums, k):
    """
    Rotate array to the right by k steps.
    
    Args:
        nums (List[int]): Input array
        k (int): Number of steps to rotate
        
    Returns:
        List[int]: Rotated array
    """
    if not nums or k == 0:
        return nums
    
    n = len(nums)
    k = k % n  # Handle cases where k > n
    
    # Helper function to reverse array in place
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse entire array
    reverse(0, n - 1)
    
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)
    
    return nums

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    result1 = rotate_array(nums1.copy(), k1)
    print(f"Test 1: {nums1} rotated by {k1} = {result1}")
    # Expected: [5, 6, 7, 1, 2, 3, 4]
    
    # Test Case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    result2 = rotate_array(nums2.copy(), k2)
    print(f"Test 2: {nums2} rotated by {k2} = {result2}")
    # Expected: [3, 99, -1, -100]
    
    # Test Case 3
    nums3 = [1]
    k3 = 1
    result3 = rotate_array(nums3.copy(), k3)
    print(f"Test 3: {nums3} rotated by {k3} = {result3}")
    # Expected: [1]