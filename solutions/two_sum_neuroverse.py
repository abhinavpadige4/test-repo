def two_sum(nums, target):
    """
    Returns the indices of the two numbers in `nums` that add up to `target`.

    Uses a hash map to store each number's index as we iterate, allowing us to
    find the complement (target - num) in O(1) average time.

    Time Complexity:  O(n)
    Space Complexity: O(n)

    Args:
        nums (list[int]): List of integers.
        target (int): The target sum.

    Returns:
        list[int]: Indices of the two numbers, or an empty list if none found.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution found


if __name__ == "__main__":
    # Test cases
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
    print(two_sum([3, 3], 6))           # [0, 1]
    print(two_sum([1, 2, 3], 10))       # []
