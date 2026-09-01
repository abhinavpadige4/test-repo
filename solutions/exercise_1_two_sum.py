"""
Exercise 1: Two Sum (Easy)

Problem Statement:
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use
the same element twice. Return the answer in any order.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1].

Concepts: Hash Map, Array, Lookup Optimization
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two indices whose values sum to the target using a hash map.

    Args:
        nums: List of integers.
        target: The target sum.

    Returns:
        A list of two indices [i, j] such that nums[i] + nums[j] == target.
    """
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No solution (should not happen per problem constraints)


# --- Test Cases ---
def run_tests():
    test_cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        (([1, 5, 8, 2], 10), [1, 2]),
    ]
    for (nums, target), expected in test_cases:
        result = two_sum(nums, target)
        assert sorted(result) == sorted(expected), f"Failed: {nums}, {target} -> {result}"
        print(f"two_sum({nums}, {target}) = {result}  (expected {expected})")
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()

"""
Time Complexity:  O(n) - single pass over the array.
Space Complexity: O(n) - hash map stores up to n elements.
"""