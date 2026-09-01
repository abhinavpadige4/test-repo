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
    Print FizzBuzz sequence from 1 to n.
    
    Args:
        n (int): Upper limit (inclusive)
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test cases
if __name__ == "__main__":
    # Test Case 1: n = 15
    print("Test Case 1: fizzbuzz(15)")
    fizzbuzz(15)
    # Expected output:
    # 1
    # 2
    # Fizz
    # 4
    # Buzz
    # Fizz
    # 7
    # 8
    # Fizz
    # Buzz
    # 11
    # Fizz
    # 13
    # 14
    # FizzBuzz
    
    print("\\nTest Case 2: n = 5")
    fizzbuzz(5)
    # Expected: 1, 2, Fizz, 4, Buzz
    
    print("\\nTest Case 3: n = 1")
    fizzbuzz(1)
    # Expected: 1

# Complexity Analysis:
# Time Complexity: O(n) - Loop runs n times
# Space Complexity: O(1) - Constant extra space