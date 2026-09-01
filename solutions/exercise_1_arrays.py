"""
Exercise 1: Array Rotation
==========================

Problem Statement:
Given an array of integers and a number k, rotate the array to the right by k steps.

Examples:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

Approach:
Use the reversal algorithm:
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
    
    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)
    
    return nums

# Test cases
def test_rotate_array():
    # Test case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    expected1 = [5, 6, 7, 1, 2, 3, 4]
    result1 = rotate_array(nums1.copy(), k1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    expected2 = [3, 99, -1, -100]
    result2 = rotate_array(nums2.copy(), k2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    nums3 = [1]
    k3 = 1
    expected3 = [1]
    result3 = rotate_array(nums3.copy(), k3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_rotate_array()