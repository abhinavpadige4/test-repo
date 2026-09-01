"""
Exercise 14: Single Number
==========================

Problem Statement:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.

Approach:
Use XOR bit manipulation:
1. XOR of a number with itself is 0
2. XOR of a number with 0 is the number itself
3. XOR is commutative and associative
So when we XOR all numbers, the duplicates cancel out and we're left with the single number.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def single_number(nums):
    """
    Find the single number in an array where every other element appears twice.
    
    Args:
        nums (List[int]): Array of integers
        
    Returns:
        int: The single number that appears only once
    """
    result = 0
    
    # XOR all numbers - duplicates will cancel out
    for num in nums:
        result ^= num
    
    return result

# Test cases
def test_single_number():
    # Test case 1: Normal case
    nums1 = [2, 2, 1]
    expected1 = 1
    result1 = single_number(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Multiple pairs
    nums2 = [4, 1, 2, 1, 2]
    expected2 = 4
    result2 = single_number(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Single element
    nums3 = [1]
    expected3 = 1
    result3 = single_number(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_single_number()