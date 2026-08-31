"""
Problem Statement:
    Given a list of integers, return a new list where each element is doubled.

Solution:
    Use list comprehension to multiply each element by 2.

Test Cases:
    Test Case 1:
        Input: [1, 2, 3]
        Expected Output: [2, 4, 6]

    Test Case 2:
        Input: [0, -1, 5]
        Expected Output: [0, -2, 10]

    Test Case 3:
        Input: []
        Expected Output: []

Expected Output:
    For the test cases above, the function should return:
        [2, 4, 6]
        [0, -2, 10]
        []

Time Complexity: O(n) where n is the length of the list.
Space Complexity: O(n) for the new list.
"""

def double_list(lst):
    """
    Return a new list with each element doubled.
    """
    return [x * 2 for x in lst]

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [2, 4, 6]),
        ([0, -1, 5], [0, -2, 10]),
        ([], []),
    ]

    print("Running test cases for double_list:")
    for i, (input_lst, expected) in enumerate(test_cases, 1):
        result = double_list(input_lst)
        print(f"Test {i}: Input: {input_lst} -> Output: {result}, Expected: {expected}")
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
    print("All tests passed!")