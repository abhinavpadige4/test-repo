"""
Exercise 2 (Medium): Two Sum
----------------------------
Problem Statement:
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. You may assume exactly one
solution exists and you may not use the same element twice.

Example:
    two_sum([2, 7, 11, 15], 9) -> [0, 1]
    two_sum([3, 2, 4], 6) -> [1, 2]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers in nums that sum to target."""
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution (should not happen per constraints)


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, expected in tests:
        result = two_sum(nums, target)
        assert sorted(result) == sorted(expected), (
            f"Failed: {nums}, {target} -> {result}, expected {expected}"
        )
        print(f"two_sum({nums}, {target}) = {result}  (expected {expected})")
    print("All tests passed!")