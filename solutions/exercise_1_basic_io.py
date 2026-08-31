"""
Problem Statement:
    Write a program that takes two numbers as input and prints their sum.

Solution:
    We will read two numbers from the user using input(), convert them to float, add them, and print the result.

Test Cases:
    Test Case 1:
        Input: 5, 3
        Expected Output: 8.0

    Test Case 2:
        Input: -2, 7
        Expected Output: 5.0

    Test Case 3:
        Input: 0, 0
        Expected Output: 0.0

Expected Output:
    For the test cases above, the program should output:
        8.0
        5.0
        0.0

Time Complexity: O(1) - constant time operations.
Space Complexity: O(1) - constant space.
"""

def add_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

if __name__ == "__main__":
    # We'll run the test cases
    print("Running test cases for add_two_numbers:")
    test_cases = [
        (5, 3, 8.0),
        (-2, 7, 5.0),
        (0, 0, 0.0)
    ]

    for i, (a, b, expected) in enumerate(test_cases, 1):
        result = add_two_numbers(a, b)
        print(f"Test {i}: Input ({a}, {b}) -> Output: {result}, Expected: {expected}")
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
    print("All tests passed!")

    # Additionally, we can take user input if desired, but for testing we use the above.
    # Uncomment the following lines to run interactively:
    # num1 = float(input("Enter first number: "))
    # num2 = float(input("Enter second number: "))
    # print(f"The sum is: {add_two_numbers(num1, num2)}")