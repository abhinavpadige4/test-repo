\"\"\"
Exercise 5: FizzBuzz
Topic: Loops / Conditionals
Difficulty: Easy

Problem Statement:
Write a Python program that prints the numbers from 1 to n. But for multiples of three print "Fizz" instead of the number, for multiples of five print "Buzz", and for numbers which are multiples of both three and five print "FizzBuzz".

Solution:
\"\"\"

def fizzbuzz(n):
    """
    Prints FizzBuzz sequence from 1 to n.
    
    Args:
        n (int): Upper limit (inclusive)
    """
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test Cases
def test_fizzbuzz():
    import io
    import sys
    # Test for n=15
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    fizzbuzz(15)
    output = sys.stdout.getvalue().strip().split('\n')
    sys.stdout = old_stdout
    expected = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert output == expected, f"Expected {expected}, got {output}"
    # Test for n=1
    sys.stdout = io.StringIO()
    fizzbuzz(1)
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    assert output == "1", f"Expected '1', got '{output}'"
    print("All tests passed!")

if __name__ == "__main__":
    test_fizzbuzz()

# Complexity Analysis:
# Time Complexity: O(n) - loop runs n times
# Space Complexity: O(1) - constant space (excluding output)