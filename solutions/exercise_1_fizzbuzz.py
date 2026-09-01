"""
Exercise 1: FizzBuzz
Difficulty: Easy
Topic: Control Flow, Conditionals

Problem Statement:
Write a function that takes an integer n and returns a list of strings from 1 to n.
For multiples of 3, use "Fizz" instead of the number.
For multiples of 5, use "Buzz" instead of the number.
For multiples of both 3 and 5, use "FizzBuzz".

Example:
Input: 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

Time Complexity: O(n)
Space Complexity: O(n) for the output list
"""

def fizzbuzz(n: int) -> list:
    """
    Generate FizzBuzz sequence from 1 to n.
    
    Args:
        n: Positive integer upper bound
        
    Returns:
        List of strings representing the FizzBuzz sequence
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# Test Cases
def test_fizzbuzz():
    """Test cases for fizzbuzz function."""
    # Test 1: Basic case
    assert fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    print("Test 1 passed: Basic case with n=15")
    
    # Test 2: Small range
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    print("Test 2 passed: Small range n=5")
    
    # Test 3: Single element
    assert fizzbuzz(1) == ["1"]
    print("Test 3 passed: Single element n=1")
    
    # Test 4: Only FizzBuzz
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    print("Test 4 passed: Last element is FizzBuzz")
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_fizzbuzz()
    
    # Demonstrate usage
    print("\nFizzBuzz sequence for n=20:")
    for i, item in enumerate(fizzbuzz(20), 1):
        print(f"{i:2d}: {item}")