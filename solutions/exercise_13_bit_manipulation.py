"""
Exercise 13: Single Number
=========================

Problem Statement:
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one. Implement a solution with linear runtime complexity and use only constant extra space.

Example:
Input: nums = [4,1,2,1,2]
Output: 4

Approach:
Use XOR bitwise operation properties:
- XOR of a number with itself is 0 (a ^ a = 0)
- XOR of a number with 0 is the number itself (a ^ 0 = a)
- XOR is commutative and associative

So when we XOR all numbers together, pairs will cancel out (become 0),
leaving only the single number.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def single_number(nums):
    """
    Find the single number that appears once in array where others appear twice.
    
    Args:
        nums (List[int]): Array of integers
        
    Returns:
        int: The single number that appears once
    """
    result = 0
    
    # XOR all numbers together
    for num in nums:
        result ^= num
    
    return result

# Alternative implementation using reduce (more Pythonic)
from functools import reduce
import operator

def single_number_reduce(nums):
    """
    Find single number using reduce and XOR.
    
    Args:
        nums (List[int]): Array of integers
        
    Returns:
        int: The single number that appears once
    """
    return reduce(operator.xor, nums, 0)

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case
    nums1 = [2, 2, 1]
    result1 = single_number(nums1)
    print(f"Test 1: {nums1} -> {result1}")  # Expected: 1
    
    # Test Case 2: Multiple pairs
    nums2 = [4, 1, 2, 1, 2]
    result2 = single_number(nums2)
    print(f"Test 2: {nums2} -> {result2}")  # Expected: 4
    
    # Test Case 3: Single element
    nums3 = [1]
    result3 = single_number(nums3)
    print(f"Test 3: {nums3} -> {result3}")  # Expected: 1
    
    # Test Case 4: Using reduce implementation
    nums4 = [5, 3, 5, 3, 8]
    result4 = single_number_reduce(nums4)
    print(f"Test 4: {nums4} -> {result4}")  # Expected: 8