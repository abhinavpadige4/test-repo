"""
Problem: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Solution:
We use a hash table to store the difference (target - current number) as we iterate.
If we find a number that is in the hash table, we return the current index and the stored index.

Time Complexity: O(n) - we traverse the list once.
Space Complexity: O(n) - we store up to n elements in the hash table.
"""

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # In case there is no solution, though the problem guarantees one.

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = two_sum(nums1, target1)
    print(f"Test 1: {result1} == {expected1} -> {result1 == expected1}")

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = two_sum(nums2, target2)
    print(f"Test 2: {result2} == {expected2} -> {result2 == expected2}")

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = two_sum(nums3, target3)
    print(f"Test 3: {result3} == {expected3} -> {result3 == expected3}")