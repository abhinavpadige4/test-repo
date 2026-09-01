\"\"\"
Exercise 11: Two Sum
Topic: Hash Table
Difficulty: Medium

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Solution:
\"\"\"
def two_sum(nums, target):
    """
    Return indices of the two numbers that add up to target.
    
    Args:
        nums (List[int]): List of integers
        target (int): Target sum
    
    Returns:
        List[int]: Indices of the two numbers
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []  # In case no solution, though problem guarantees one

# Test cases
if __name__ == "__main__":
    # Test Case 1: Basic
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test Case 1: two_sum({nums1}, {target1}) = {two_sum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test Case 2: With negative numbers
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test Case 2: two_sum({nums2}, {target2}) = {two_sum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test Case 3: Duplicate numbers
    nums3 = [3, 3]
    target3 = 6
    print(f"Test Case 3: two_sum({nums3}, {target3}) = {two_sum(nums3, target3)}")  # Expected: [0, 1]
    
    # Test Case 4: Larger array
    nums4 = [1, 5, 3, 4, 2]
    target4 = 7
    print(f"Test Case 4: two_sum({nums4}, {target4}) = {two_sum(nums4, target4)}")  # Expected: [0, 3] or [1, 4] etc.

# Complexity Analysis:
# Time Complexity: O(n) - single pass through the list
# Space Complexity: O(n) - for the hash table