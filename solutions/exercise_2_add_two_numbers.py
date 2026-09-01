\"\"\"
Exercise 2: Add Two Numbers
Topic: Basic Arithmetic
Difficulty: Easy

Problem Statement:
Write a Python function that takes two numbers as input and returns their sum.

Solution:
\"\"\"

def add_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Sum of a and b
    """
    return a + b

# Test Cases
def test_add_two_numbers():
    assert add_two_numbers(2, 3) == 5
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(0, 0) == 0
    assert add_two_numbers(2.5, 3.5) == 6.0
    print("All tests passed!")

if __name__ == "__main__":
    test_add_two_numbers()

# Complexity Analysis:
# Time Complexity: O(1) - constant time operation
# Space Complexity: O(1) - constant space used