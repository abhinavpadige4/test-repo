"""
Problem Statement:
    Write a program that converts a temperature from Celsius to Fahrenheit.
    The formula is: F = (C * 9/5) + 32

Solution:
    Read a Celsius value from input, apply the formula, and print the result.

Test Cases:
    Test Case 1:
        Input: 0
        Expected Output: 32.0

    Test Case 2:
        Input: 100
        Expected Output: 212.0

    Test Case 3:
        Input: -40
        Expected Output: -40.0

Expected Output:
    For the test cases above, the program should output:
        32.0
        212.0
        -40.0

Time Complexity: O(1)
Space Complexity: O(1)
"""

def celsius_to_fahrenheit(c):
    """
    Convert Celsius to Fahrenheit.
    """
    return (c * 9/5) + 32

if __name__ == "__main__":
    test_cases = [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),  # body temperature
    ]

    print("Running test cases for celsius_to_fahrenheit:")
    for i, (c_input, expected) in enumerate(test_cases, 1):
        result = celsius_to_fahrenheit(c_input)
        print(f"Test {i}: Input: {c_input}°C -> Output: {result}°F, Expected: {expected}°F")
        assert abs(result - expected) < 1e-9, f"Test {i} failed: got {result}, expected {expected}"
    print("All tests passed!")

    # Uncomment below to run interactively:
    # c = float(input("Enter temperature in Celsius: "))
    # print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")