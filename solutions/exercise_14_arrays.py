"""
Exercise 14: Product of Array Except Self (Medium)
Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Examples:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
"""

def product_except_self(nums):
    """
    Calculate product of array except self using prefix and suffix products.
    
    Args:
        nums (List[int]): Input array of integers
    
    Returns:
        List[int]: Array where each element is product of all other elements
        
    Time Complexity: O(n)
    Space Complexity: O(1) extra space (not counting output array)
    """
    n = len(nums)
    result = [1] * n
    
    # First pass: calculate prefix products
    # result[i] will contain product of elements to the left of i
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Second pass: multiply by suffix products
    # right_product keeps track of product of elements to the right of i
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# Alternative approach with explicit prefix and suffix arrays
def product_except_self_explicit(nums):
    """
    Calculate product of array except self using explicit prefix and suffix arrays.
    
    Args:
        nums (List[int]): Input array of integers
    
    Returns:
        List[int]: Array where each element is product of all other elements
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    
    # Calculate prefix products (products of elements to the left)
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]
    
    # Calculate suffix products (products of elements to the right)
    suffix = [1] * n
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]
    
    # Multiply prefix and suffix for each position
    result = []
    for i in range(n):
        result.append(prefix[i] * suffix[i])
    
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    result1 = product_except_self(nums1)
    print(f"Test 1 - Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [24, 12, 8, 6]")
    print(f"Pass: {result1 == [24, 12, 8, 6]}\\n")
    
    # Test Case 2
    nums2 = [-1, 1, 0, -3, 3]
    result2 = product_except_self(nums2)
    print(f"Test 2 - Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [0, 0, 9, 0, 0]")
    print(f"Pass: {result2 == [0, 0, 9, 0, 0]}\\n")
    
    # Test Case 3
    nums3 = [2, 3, 4, 5]
    result3 = product_except_self(nums3)
    print(f"Test 3 - Input: {nums3}")
    print(f"Output: {result3}")
    expected3 = [60, 40, 30, 24]  # 3*4*5, 2*4*5, 2*3*5, 2*3*4
    print(f"Expected: {expected3}")
    print(f"Pass: {result3 == expected3}\\n")
    
    # Test Case 4
    nums4 = [1, 2]
    result4 = product_except_self(nums4)
    print(f"Test 4 - Input: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: [2, 1]")
    print(f"Pass: {result4 == [2, 1]}\\n")
    
    # Test explicit approach
    nums5 = [4, 3, 2, 1]
    result5 = product_except_self_explicit(nums5)
    print(f"Explicit Approach - Input: {nums5}")
    print(f"Output: {result5}")
    expected5 = [6, 8, 12, 24]  # 3*2*1, 4*2*1, 4*3*1, 4*3*2
    print(f"Expected: {expected5}")
    print(f"Pass: {result5 == expected5}\\n")